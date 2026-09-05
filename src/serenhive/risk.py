from pydantic import BaseModel

SENSITIVE_TERMS = (
    "cure", "treat", "heals", "healing", "eczema", "acne cure",
    "allergic reaction", "burn", "refund", "legal", "payment dispute",
)

class Assessment(BaseModel):
    risk: str
    requires_human_approval: bool
    reasons: list[str]

def assess_content(text: str) -> Assessment:
    normalized = text.lower()
    reasons = [term for term in SENSITIVE_TERMS if term in normalized]
    if reasons:
        return Assessment(
            risk="sensitive",
            requires_human_approval=True,
            reasons=reasons,
        )
    return Assessment(risk="low", requires_human_approval=False, reasons=[])
