def to_decimal_str(value: float | int | str, digits: int = 2) -> str:
    """
    แปลงค่าตัวเลขให้เป็น string ที่มีทศนิยมตามจำนวน digits (ค่าเริ่มต้นคือ 2)
    ถ้า value ไม่สามารถแปลงได้ จะคืนค่า "0.00"

    Example:
        to_decimal_str(50)        -> "50.00"
        to_decimal_str(50.156)    -> "50.16"
        to_decimal_str("12.5")    -> "12.50"
        to_decimal_str(None)      -> "0.00"
    """
    try:
        return f"{float(value):.{digits}f}"
    except (ValueError, TypeError):
        return f"{0:.{digits}f}"
