import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("root_f1_search", ROOT / "F1_search.py")
search_module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(search_module)
course = search_module.course
student = search_module.student


def test_course_search_by_partial_id_case_insensitive():
    courses = [
        {"course_id": "CS101", "course_name": "Python", "teacher": "王老師",
         "week": 2, "section": "3", "is_required": 1, "enrolled": 10, "member_limit": 30},
        {"course_id": "EE202", "course_name": "Circuit", "teacher": "李老師",
         "week": 3, "section": "2", "is_required": 0, "enrolled": 30, "member_limit": 30},
    ]
    assert course(courses, course_id="cs1") == [courses[0]]


def test_course_search_filters_by_multiple_conditions():
    courses = [
        {"course_id": "CS101", "course_name": "Python", "teacher": "王老師",
         "week": 2, "section": "3", "is_required": 1, "enrolled": 10, "member_limit": 30},
        {"course_id": "CS102", "course_name": "Python advanced", "teacher": "李老師",
         "week": 2, "section": "4", "is_required": 1, "enrolled": 30, "member_limit": 30},
    ]
    assert course(courses, course_name="python", week=2, is_available=True) == [courses[0]]


def test_course_search_no_match_returns_empty_list():
    assert course([{"course_id": "CS101", "course_name": "Python"}],
                  course_id="NOT-FOUND") == []


def test_student_search_by_id_and_department():
    students = [
        {"student_id": "S001", "student_name": "小明", "department": "資工系",
         "enrolled_class": ["CS101"]},
        {"student_id": "S002", "student_name": "小華", "department": "電機系",
         "enrolled_class": ["EE202"]},
    ]
    assert student(students, student_id="s00", department="資工") == [students[0]]


def test_student_search_by_enrolled_class():
    students = [
        {"student_id": "S001", "student_name": "小明", "department": "資工系",
         "enrolled_class": ["CS101", "CS102"]},
        {"student_id": "S002", "student_name": "小華", "department": "電機系",
         "enrolled_class": ["EE202"]},
    ]
    assert student(students, enrolled_class="cs10") == [students[0]]


def test_student_search_no_match_returns_empty_list():
    students = [{"student_id": "S001", "student_name": "小明",
                 "department": "資工系", "enrolled_class": []}]
    assert student(students, student_name="小美") == []
