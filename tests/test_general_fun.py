import pytest
import general_fun


def test_save_and_load_json_round_trip(tmp_path):
    path = tmp_path / "nested" / "data.json"
    data = {"students": [{"name": "小明"}]}
    general_fun.save_json(path, data)
    assert general_fun.load_json(path) == data


def test_load_json_missing_file_without_default_raises(tmp_path):
    with pytest.raises(FileNotFoundError):
        general_fun.load_json(tmp_path / "missing.json")


def test_load_json_missing_file_returns_default(tmp_path):
    default = {"courses": []}
    assert general_fun.load_json(tmp_path / "missing.json", default=default) == default


def test_course_conflict_detects_shared_time():
    schedule = [["CS101", ["21", "22"]], ["CS102", ["22", "23"]]]
    assert general_fun.course_conflict(schedule) == "CS101 與 CS102 在 22 時有衝堂！"


def test_course_conflict_when_no_overlap():
    schedule = [["CS101", ["21"]], ["CS102", ["32"]]]
    assert general_fun.course_conflict(schedule) == "課程無衝堂"


def test_classroom_conflict_returns_false_when_room_and_time_overlap(capsys):
    data = {"courses": [
        {"course_id": "CS101", "course_name": "Python",
         "class_room": "教室A", "class_time": ["21", "22"]}
    ]}
    assert general_fun.classroom_conflict("教室A", ["22"], data) is False
    assert "CS101" in capsys.readouterr().out


def test_classroom_conflict_returns_true_when_no_conflict():
    data = {"courses": [
        {"course_id": "CS101", "course_name": "Python",
         "class_room": "教室A", "class_time": ["21"]}
    ]}
    assert general_fun.classroom_conflict("教室B", ["21"], data) is True


def test_credit_input_accepts_half_credit(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _prompt="": "2.5")
    assert general_fun.credit_input("學分：") == 2.5


def test_credit_input_empty_returns_empty_string_by_default(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _prompt="": "")
    assert general_fun.credit_input("學分：") == ""


def test_credit_input_retries_invalid_then_accepts(monkeypatch, capsys):
    answers = iter(["abc", "-1", "1.5"])
    monkeypatch.setattr("builtins.input", lambda _prompt="": next(answers))
    assert general_fun.credit_input("學分：") == 1.5
    output = capsys.readouterr().out
    assert "格式錯誤" in output
    assert "不得為負" in output


def test_class_time_input_accepts_time_and_stops_on_blank(monkeypatch):
    answers = iter(["21", ""])
    monkeypatch.setattr("builtins.input", lambda _prompt="": next(answers))
    assert general_fun.class_time_input("時段：") == ["21"]


def test_class_time_input_rejects_bad_format_then_accepts(monkeypatch, capsys):
    answers = iter(["x1", "2a", ""])
    monkeypatch.setattr("builtins.input", lambda _prompt="": next(answers))
    # '2a' is a valid day/period according to current implementation.
    assert general_fun.class_time_input("時段：") == ["2a"]
    assert "格式錯誤" in capsys.readouterr().out
