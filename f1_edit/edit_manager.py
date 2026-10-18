import edit_student
import edit_course

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

from general_fun import load_json, save_json

def edit_menu():
    while True:
        print("請選擇需要修改的資料類型代號：\n")
        print("1. 編輯學生資料")
        print("2. 編輯課程資料")
        print("0. 返回主選單")
        
        choice = input()
        
        if choice == "1":
            full_data = load_json("data.json")

            edit_student.edit_student_process(full_data)

            save_json("data.json", full_data)

        elif choice == "2":
            full_data = load_json("data.json")

            edit_course.edit_course_process(full_data)

            save_json("data.json", full_data)
            

        elif choice == "0":
            print("返回主選單\n")
            break


if __name__ == "__main__":
    edit_menu()