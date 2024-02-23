import math
from typing import Union

import phonenumbers


class FormatUtil:
    @staticmethod
    def string_to_bool(input_str: str) -> bool:
        input_str = input_str.lower().strip()
        return bool(input_str and input_str != "false" and input_str != "0")

    @staticmethod
    def string_to_int(input_str: str, default: int = 0) -> int:
        if isinstance(input_str, str):
            input_str = input_str.lower().strip()
        try:
            return int(input_str)
        except ValueError:
            return default

    @staticmethod
    def string_to_float(input_str: str, default: float = 0.0) -> float:
        if isinstance(input_str, str):
            input_str = input_str.lower().strip()
        try:
            return float(input_str)
        except ValueError:
            return default

    @staticmethod
    def phone_to_local_format(mobile: str) -> str:
        if not mobile:
            return ""
        return f"0{mobile[3:]}" if mobile.startswith("+84") else mobile

    @staticmethod
    def phone_to_canonical_format(mobile: str) -> str:
        if not mobile:
            return ""
        mobile = mobile.replace(" ", "")
        mobile = mobile.strip()
        prefix = mobile[:4]
        if prefix == "+840":
            return f"+84{mobile[4:]}"
        return f"+84{mobile[1:]}" if mobile.startswith("0") else mobile

    @staticmethod
    def check_valid_mobile(value: str) -> bool:
        if not value:
            return False

        try:
            mobile = phonenumbers.parse(value, None)
        except phonenumbers.phonenumberutil.NumberParseException:
            try:
                mobile = phonenumbers.parse(value, "VN")
            except phonenumbers.phonenumberutil.NumberParseException:
                return False
        return bool(phonenumbers.is_valid_number(mobile))

    @staticmethod
    def mask_prefix(input_str: str, mask_length: int = 4) -> str:
        remain = input_str[-mask_length:]
        prefix = "*" * (len(input_str) - mask_length)
        return f"{prefix}{remain}"

    @staticmethod
    def mask_email(email: str) -> str:
        email_arr = email.split("@")
        suffix = email_arr[1]
        name = email_arr[0]
        length = len(name)

        if length == 1:
            return f"*@{suffix}"

        mask_length = math.ceil(length / 2) if length <= 4 else 4
        name = FormatUtil.mask_prefix(name, mask_length)

        return f"{name}@{suffix}"

    @staticmethod
    def to_bool(input_value: Union[str, int, bool, None]) -> bool:
        return input_value not in [0, "0", "", False, "False", "false", "FALSE", None]

    @staticmethod
    def get_transfer_data_source(key: str, title: str, description: str = "") -> dict:
        return dict(
            key=str(key or ""),
            title=str(title or ""),
            description=str(description or ""),
        )
