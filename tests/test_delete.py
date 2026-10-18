import f1_del_model as delete_model


def test_delete_existing_student(monkeypatch):
    data = {"students": [{"student_id": "S001", "name": "小明"}], "courses": []}
    saved = []
    monkeypatch.setattr(delete_model, "save_json", lambda path, payload: saved.append((path, payload.copy())))
    monkeypatch.setattr(delete_model, "clear_screen", lambda: None)

    result = delete_model.del_student("S001", data)

    assert result == "已刪除學生 S001"
    assert data["students"] == []
    assert len(saved) == 1


def test_delete_missing_student_does_not_save(monkeypatch):
    data = {"students": [{"student_id": "S001", "name": "小明"}], "courses": []}
    saved = []
    monkeypatch.setattr(delete_model, "save_json", lambda *args: saved.append(args))
    monkeypatch.setattr(delete_model, "clear_screen", lambda: None)

    result = delete_model.del_student("S999", data)

    assert result == "未找到學生 S999 或是已被刪除"
    assert len(data["students"]) == 1
    assert saved == []


def test_delete_course_blocked_when_student_enrolled(monkeypatch):
    data = {
        "students": [{"student_id": "S001", "enrolled_class": ["CS101"]}],
        "courses": [{"course_id": "CS101", "course_name": "Python"}],
    }
    saved = []
    monkeypatch.setattr(delete_model, "save_json", lambda *args: saved.append(args))
    monkeypatch.setattr(delete_model, "clear_screen", lambda: None)

    result = delete_model.del_course("CS101", data)

    assert result == "課程 CS101 未刪除，因為有學生已選該課程"
    assert len(data["courses"]) == 1
    assert saved == []


def test_delete_unenrolled_course(monkeypatch):
    data = {
        "students": [{"student_id": "S001", "enrolled_class": []}],
        "courses": [{"course_id": "CS101", "course_name": "Python"}],
    }
    saved = []
    monkeypatch.setattr(delete_model, "save_json", lambda path, payload: saved.append(path))
    monkeypatch.setattr(delete_model, "clear_screen", lambda: None)

    result = delete_model.del_course("CS101", data)

    assert result == "已刪除課程 CS101"
    assert data["courses"] == []
    assert len(saved) == 1
