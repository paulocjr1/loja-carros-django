from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
import re


def parse_brl(value):
    """Convert numbers or common Brazilian/US currency strings to Decimal."""
    if value is None:
        return None

    text = str(value).strip()
    if not text:
        return None

    negative = "-" in text or (text.startswith("(") and text.endswith(")"))
    cleaned = re.sub(r"[^0-9.,]", "", text)
    if not cleaned:
        return None

    comma = cleaned.rfind(",")
    dot = cleaned.rfind(".")

    if comma >= 0 and dot >= 0:
        if comma > dot:  # 1.234,56
            cleaned = cleaned.replace(".", "").replace(",", ".")
        else:  # 1,234.56
            cleaned = cleaned.replace(",", "")
    elif comma >= 0:
        parts = cleaned.split(",")
        if len(parts) > 2:
            decimals = parts[-1]
            cleaned = "".join(parts[:-1]) + ("." + decimals if len(decimals) in (1, 2) else decimals)
        else:
            whole, decimals = parts
            cleaned = whole + decimals if len(decimals) == 3 else whole + "." + decimals
    elif dot >= 0:
        parts = cleaned.split(".")
        if len(parts) > 2:
            decimals = parts[-1]
            cleaned = "".join(parts[:-1]) + ("." + decimals if len(decimals) in (1, 2) else decimals)
        elif len(parts[-1]) == 3:
            cleaned = "".join(parts)

    try:
        amount = Decimal(cleaned)
    except InvalidOperation:
        return None

    if negative:
        amount = -abs(amount)
    return amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def format_brl(value):
    """Format common numeric and Brazilian-formatted strings as BRL."""
    amount = parse_brl(value)
    if amount is None:
        return "—"

    formatted = f"{abs(amount):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    sign = "-" if amount < 0 else ""
    return f"R$ {sign}{formatted}"
