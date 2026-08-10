"""Add at least four focused student-authored tests below."""
import pytest
from src.lab01 import classify_score, format_student_record

def test_classify_score_normal():
    assert classify_score(87) == "green"
    assert classify_score(93) == "green"

def test_classify_score_boundaries():
    assert classify_score(59) == "red"
    assert classify_score(60) == "amber"
    assert classify_score(79) == "amber"
    assert classify_score(80) == "green"
    assert classify_score(0) == "red"
    assert classify_score(100) == "green"

def test_classify_score_reject_bool():
    with pytest.raises(TypeError):
        classify_score(True)
    with pytest.raises(TypeError):
        classify_score(False)

def test_format_student_record_trimmed():
    result = format_student_record("   Alan   ", 85)
    assert result == "Alan | 85 | green"

def test_invalid_types_and_values():
    # 測試無效的分數與姓名
    with pytest.raises(ValueError):
        classify_score(-1)
    with pytest.raises(ValueError):
        classify_score(101)
    with pytest.raises(TypeError):
        format_student_record(123, 90)

# Begin with one normal case, two threshold boundaries, and one exception.
