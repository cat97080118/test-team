'''
注意！該目錄下的 data.json 為測試用的假資料！
'''

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent # 取得專案根目錄
sys.path.append(str(PROJECT_ROOT)) # 將根目錄加入 Python 搜尋路徑中

from general_fun import load_json, save_json, clear_screen

def del_ui():
    while True:
        data = load_json("data.json")
        
        print("\n=== 資料刪除 ===\n[0] 返回主菜單\n[1] 學生資料\n[2] 課程資料")
        del_type = input("請選擇要刪除的資料類型：")
        if (del_type == "0"):
            return
        if (del_type == "1"):
            clear_screen()
            stu_list = [f"{s['student_id']} - {s['name']}" for s in data.get('students', [])]
            print(f"=== 刪除學生資料 ===\n當前學生清單：{', '.join(stu_list)}")
            del_stuid = input("請輸入要刪除的學生學號：")
            if del_stuid == '':
                clear_screen()
                print("請輸入內容！")
                continue
            print(del_student(del_stuid, data))
        elif (del_type == "2"):
            clear_screen()
            c_list = [f"{s['course_id']} - {s['course_name']}" for s in data.get('courses', [])]
            print(f"=== 刪除課程資料 ===\n當前課程清單：{', '.join(c_list)}")
            del_cid = input("請輸入要刪除的課程課號：")
            if del_cid == '':
                clear_screen()
                print("請輸入內容！")
                continue
            print(del_course(del_cid, data))
        else:
            clear_screen()
            print("輸入錯誤！請重新輸入\n")

def del_student(mydel: str, data):
    stu_list = data.get('students',[])
    for i, student in enumerate(stu_list):
        if student.get('student_id') == mydel:
            del stu_list[i]
            save_json("data.json", data)
            clear_screen()
            return f"已刪除學生 { mydel }"
    clear_screen()
    return f"未找到學生 {mydel} 或是已被刪除"

def del_course(mydel: str, data):
    stu_list = data.get('students',[])
    for student in stu_list:
        if mydel in student.get('enrolled_class',[]):
            clear_screen()
            return f"課程 {mydel} 未刪除，因為有學生已選該課程"

    c_list = data.get('courses',[])
    for i, course in enumerate(c_list):
        if course.get('course_id') == mydel:
            del c_list[i]
            save_json("data.json", data)
            clear_screen()
            return f"已刪除課程 { mydel }"
    clear_screen()
    return f"未找到課程 { mydel } 或是已被刪除"

if __name__ == "__main__":
    clear_screen()
    del_ui()