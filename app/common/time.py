import re
_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

def validate_date(date_key: str) -> bool:
    return bool(_DATE_RE.match(date_key or ""))
