import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

from general_fun import credit_input, class_time_input, classroom_conflict

def get_edited_course_data(course_data):
    target_course_id = input("請輸入欲修改的課程代碼：\n")
    
    while target_course_id == "":
        target_course_id = input("課程代碼不可留空，請重新輸入：\n")

    while not is_course_id_in_data(target_course_id, course_data):
        target_course_id = input("此課程不存在於現有資料庫，請重新輸入：\n")

    new_course_id = input("請輸入該課程之新課程編號：\n")
    if is_course_id_in_data(new_course_id, course_data):
        if new_course_id == target_course_id:
            target_course_id = ""
        else:
            print(f"此課程代碼{new_course_id}已存在課程，請先修改後重試\n")
            return get_edited_course_data(course_data)
    
    new_course_name = input("請輸入新課程名稱：\n")

    new_credits = credit_input("請輸入課程新學分數：\n")
    """
    此處應加入學分檢核(檢查有沒有學生因學分改變受影響，去validator寫函數)
    """
    
    new_teacher = input("請輸入新教師姓名：\n")
    """
    此處應加入教師衝堂檢核(去general func寫函數)
    """

    new_member_limit = int(input("請輸入新人數上限：\n"))
    """
    此處應加入:
    1. 教室容積檢查(如果data有要新增這個資料的話)
    2. 人數限制有沒有影響到原本有修這堂課的學生
    3. 人數數字格式檢查
    """

    new_class_time = class_time_input("請輸入新課程時段：\n")

    if new_class_time != "":
        new_classroom = input("請輸入新教室：（因有修改時段，故必填）\n")
        while new_classroom == "" or classroom_conflict(new_classroom, new_class_time, course_data):
            new_classroom = input("請重新輸入新教室：（必填且不得衝堂）\n")



    is_required = input("1. 必修\n2. 選修\n")
    while True:
        if is_required == "1":
            is_required = 1
            break
        elif is_required == "2":
            is_required = 0
            break
        else:
            print("格式錯誤，請重新輸入")
            is_required = input("1. 必修\n2. 選修\n")

    
    edited_course_data = {
        "course_id": new_course_id,
        "course_name": new_course_name,
        "credits": new_credits,
        "teacher": new_teacher,
        "member_limit": new_member_limit,
        "class_time": new_class_time,
        "class_room": new_classroom,
        "is_required": is_required
    }

    return edited_course_data, target_course_id
    

def update_course_record(edited_course_data: dict, target_course_id: str, course_data:dict):
    valid_updates = {key: value for key, value in edited_student_data.items() if value != ""}

    for course_record in course["course"]:
        if course_record.get("course_id") == target_course_id:
            course_data.update(valid_updates)
            break


def is_course_id_in_data(course_id, course_data):
    return any(course_record["course_id"] == course_id for course_record in course_data["courses"])

def edit_course_process(course_data):
    edited_course_data, target_course_id = get_edited_course_data(course_data)
    update_course_record(edited_course_data, target_course_id, course_data)
