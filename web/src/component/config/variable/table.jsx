import * as React from 'react';
import { useEffect, useState } from 'react';
import { useSetRecoilState } from 'recoil';
import { Row, Col, Table } from 'antd';
import Pagination, { defaultPages } from 'component/common/table/pagination';
import SearchInput from 'component/common/table/search_input';
import {
    AddNewBtn,
    RemoveSelectedBtn,
    EditBtn,
    RemoveBtn
} from 'component/common/table/buttons';
import PemCheck from 'component/common/pem_check';
import Util from 'service/helper/util';
import RequestUtil from 'service/helper/request_util';
import Dialog from './dialog';
import { variableOptionSt } from './state';
import { urls, labels, messages } from './config';

const PEM_GROUP = 'variable';

export default function VariableTable() {
    const [queryParam, setQueryParam] = useState({});
    const [init, setInit] = useState(false);
    const [list, setList] = useState([]);
    const [ids, setIds] = useState([]);
    const [pages, setPages] = useState(defaultPages);
    const setVariableOption = useSetRecoilState(variableOptionSt);

    function getList() {
        setInit(true);
        RequestUtil.apiCall(urls.crud, queryParam)
            .then((resp) => {
                setPages(resp.data.pages);
                setList(Util.appendKey(resp.data.items));
                setVariableOption(resp.data.extra.option);
            })
            .finally(() => {
                setInit(false);
            });
    }

    function searchList(keyword) {
        const qParam = { ...queryParam };
        delete qParam.page;
        setQueryParam({ ...qParam, q: keyword });
    }

    useEffect(() => {
        getList();
    }, [queryParam]);

    function onDelete(id) {
        const r = window.confirm(messages.deleteOne);
        if (!r) return;

        Util.toggleGlobalLoading(true);
        RequestUtil.apiCall(`${urls.crud}${id}`, {}, 'delete')
            .then(() => {
                setList([...list.filter((item) => item.id !== id)]);
            })
            .finally(() => Util.toggleGlobalLoading(false));
    }

    function onBulkDelete(ids) {
        const r = window.confirm(messages.deleteMultiple);
        if (!r) return;

        Util.toggleGlobalLoading(true);
        RequestUtil.apiCall(`${urls.crud}?ids=${ids.join(',')}`, {}, 'delete')
            .then(() => {
                setList([...list.filter((item) => !ids.includes(item.id))]);
            })
            .finally(() => Util.toggleGlobalLoading(false));
    }

    function onChange(data, id) {
        if (!id) {
            setList([{ ...data, key: data.id }, ...list]);
        } else {
            const index = list.findIndex((item) => item.id === id);
            data.key = data.id;
            list[index] = data;
            setList([...list]);
        }
    }

    const columns = [
        {
            key: 'key',
            title: labels.key,
            dataIndex: 'key'
        },
        {
            key: 'value',
            title: labels.value,
            dataIndex: 'value'
        },
        {
            key: 'type',
            title: labels.type,
            dataIndex: 'type_label',
            width: 120
        },
        {
            key: 'action',
            title: '',
            fixed: 'right',
            width: 90,
            render: (_text, record) => (
                <div className="flex-space">
                    <PemCheck pem_group={PEM_GROUP} pem="update">
                        <EditBtn onClick={() => Dialog.toggle(true, record.id)} />
                    </PemCheck>
                    <PemCheck pem_group={PEM_GROUP} pem="delete">
                        <RemoveBtn onClick={() => onDelete(record.id)} />
                    </PemCheck>
                </div>
            )
        }
    ];

    const rowSelection = {
        onChange: (ids) => {
            setIds(ids);
        }
    };

    return (
        <div>
            <Row>
                <Col span={12}>
                    <PemCheck pem_group={PEM_GROUP} pem="delete">
                        <RemoveSelectedBtn ids={ids} onClick={onBulkDelete} />
                    </PemCheck>
                </Col>
                <Col span={12} className="right">
                    <PemCheck pem_group={PEM_GROUP} pem="create">
                        <AddNewBtn onClick={() => Dialog.toggle()} />
                    </PemCheck>
                </Col>
            </Row>

            <SearchInput onChange={searchList} />

            <Table
                rowSelection={{
                    type: 'checkbox',
                    ...rowSelection
                }}
                loading={init}
                columns={columns}
                dataSource={list}
                scroll={{ x: 1000 }}
                pagination={false}
            />
            <Pagination
                next={pages.next}
                prev={pages.prev}
                onChange={(page) => {
                    const qParam = { ...queryParam };
                    if (!page) {
                        delete qParam.page;
                        setQueryParam({ ...qParam });
                    } else {
                        setQueryParam({ ...queryParam, page });
                    }
                }}
            />
            <Dialog onChange={onChange} />
        </div>
    );
}

VariableTable.displayName = 'VariableTable';
