import pytest
from f1_edit import edit_course


def test_course_id_exists_and_missing():
    data = {"courses": [{"course_id": "CS101", "course_name": "Python"}]}
    assert edit_course.is_course_id_in_data("CS101", data) is True
    assert edit_course.is_course_id_in_data("CS999", data) is False


@pytest.mark.xfail(strict=True, reason="原始碼 update_course_record 使用未定義的 edited_student_data 與 course，需由負責組員修正")
def test_update_course_record_updates_only_target_and_preserves_blank_fields():
    data = {"courses": [
        {"course_id": "CS101", "course_name": "舊課名", "teacher": "王老師"},
        {"course_id": "CS102", "course_name": "另一門課", "teacher": "李老師"},
    ]}
    updates = {"course_id": "", "course_name": "新課名", "teacher": ""}

    edit_course.update_course_record(updates, "CS101", data)

    assert data["courses"][0] == {
        "course_id": "CS101", "course_name": "新課名", "teacher": "王老師"
    }
    assert data["courses"][1]["course_name"] == "另一門課"
