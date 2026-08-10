"""Lab 01 public functions.

Implement the published contract without changing the function names or
parameters. Keep this module free of input(), print(), files, and UI code.
"""


def classify_score(score: int) -> str:
    if type(score) is not int:
        raise TypeError
    if score < 0 or score > 100:
        raise ValueError
    if score >= 80:
        return "green"
    elif score >= 60:
        return "amber"
    else:
        return "red"
def format_student_record(name: str, score: int) -> str:
    """Return ``<trimmed name> | <score> | <classification>``."""
    if type(name) is not str:
        raise TypeError
    trimmed_name = name.strip()
    if not trimmed_name:
        raise ValueError
    classification = classify_score(score)
    return f"{trimmed_name} | {score} | {classification}"