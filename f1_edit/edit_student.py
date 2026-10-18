import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

from general_fun import credit_input

def get_edited_student_data(student_data):
    print("請依照指示輸入學生資料，留空為不修改\n")
    target_student_id = input("請輸入欲修改之學生學號（必填）：\n")
    
    while target_student_id == "":
        target_student_id = input("學號不可為空，請重新輸入：\n")
        
    while not is_student_id_in_data(target_student_id, student_data):
        target_student_id = input("學生不存在於現有名單中，請重新輸入：\n")

    new_student_id = input("請輸入該學生之新學號：\n")
    if is_student_id_in_data(new_student_id, student_data):
        if new_student_id == target_student_id:
            new_student_id = ""
        else:
            print(f"此學號 {new_student_id} 已存在學生，請先修改該學生之學號後重試")
            return get_edited_student_data(student_data)

    new_student_name = input("請輸入該學生之新姓名：\n")
    new_student_department = input("請輸入該學生之新系所：\n")
    
    new_course_ids = []
    while True:
        input_course_id = input("請輸入已修課程編號：\n")
        if input_course_id == "":
            if len(new_course_ids) != 0:
                break
            else:
                new_course_ids = ""
                break
        else:
            """
            放修課檢查邏輯
            """
            new_course_ids.append(input_course_id)


    new_activity_ids = []
    while True:
        input_activity_id = input("請輸入活動編號：\n")

        if input_activity_id == "":
            if len(new_course_ids) != 0:
                break
            else:
                new_activity_ids = ""
                break
        else:
            """
            放活動檢查邏輯
            """
            new_activity_ids.append(input_activity_id)


    new_credits_max = credit_input("請輸入學分上限：\n")
    new_credits_min = credit_input("請輸入學分下限：\n")
    
    while new_credits_max != "" and new_credits_min != "" and int(new_credits_min) > int(new_credits_max):
        new_credits_max = credit_input("下限不可大於上限，請重新輸入上限")
        new_credits_min = credit_input("請重新輸入下限")

    """
    這邊要先判斷已選的課有沒有符合學分上下限結果
    """

    edited_student_data = {
        "student_id": new_student_id, 
        "name": new_student_name, 
        "department": new_student_department, 
        "course_id": new_course_ids,
        "activity_id": new_activity_ids, 
        "credits_min": new_credits_min,
        "credits_max": new_credits_max
    }

    return edited_student_data, target_student_id

def is_student_id_in_data(student_id, student_data):
    return any(student_record["student_id"] == student_id for student_record in student_data["students"])

def update_student_record(edited_student_data: dict, target_student_id: str, student_data: dict):
    
    valid_updates = {key: value for key, value in edited_student_data.items() if value != ""}

    for student_record in student_data["students"]:
        if student_record.get("student_id") == target_student_id:
            student_record.update(valid_updates)
            break
            

def edit_student_process(student_data):
    
    edited_student_data, target_student_id = get_edited_student_data(student_data)
    update_student_record(edited_student_data, target_student_id, student_data)
