from f1_edit import edit_student


def test_student_id_exists_and_missing():
    data = {"students": [{"student_id": "S001", "name": "小明"}]}
    assert edit_student.is_student_id_in_data("S001", data) is True
    assert edit_student.is_student_id_in_data("S999", data) is False


def test_update_student_record_changes_nonempty_fields():
    data = {"students": [
        {"student_id": "S001", "name": "小明", "department": "資工系", "credits_max": 20}
    ]}
    updates = {"student_id": "", "name": "小明新", "department": "", "credits_max": 24}

    edit_student.update_student_record(updates, "S001", data)

    assert data["students"][0] == {
        "student_id": "S001", "name": "小明新", "department": "資工系", "credits_max": 24
    }


def test_update_student_record_leaves_other_students_unchanged():
    data = {"students": [
        {"student_id": "S001", "name": "小明"},
        {"student_id": "S002", "name": "小華"},
    ]}
    edit_student.update_student_record({"name": "新名字"}, "S001", data)
    assert data["students"][0]["name"] == "新名字"
    assert data["students"][1]["name"] == "小華"
