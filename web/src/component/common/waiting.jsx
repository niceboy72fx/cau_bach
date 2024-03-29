import * as React from 'react';
import { Spin } from 'antd';

export default function Waiting() {
    return (
        <div className="backdrop">
            <Spin tip="Loading..." size="large">
                <div className="spin-content" />
            </Spin>
        </div>
    );
}
