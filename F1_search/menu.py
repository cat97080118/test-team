from F1_search import course
from F1_search import student

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

from general_fun import load_json, save_json

data = load_json("search.json")
course_data = data['course']
student_data = data['student']
print("========查詢功能========")
print("[1] 課程查詢")
print("[2] 學生查詢")
s_c = input("請選擇查詢項目：").strip()
if s_c == "1":
     id = input("請輸入課程代碼：").strip() or None
     name = input("請輸入課程名稱：").strip() or None
     teacher = input("請輸入教師：").strip() or None
     week = input("請輸入星期：").strip() or None
     section = input("請輸入節次：").strip() or None
     required = input("請輸入必選修 (1為必修，0為選修)：").strip() or None
     available = input("是否篩選額滿課程 (1為是，0為否)：").strip() or None

     res1 = course(course_data,course_id = id,course_name = name,teacher = teacher,week = week,section = section,is_required = required,is_available = available)
     if res1:
          for c in res1:  #c是res1拿出來的一個課程，res1放了所有符合條件的課程
               print("=========================================")
               print(f"課程代碼：{c.get("course_id","無")}")
               print(f"課程名稱：{c.get("course_name","無")}")
               print(f"授課教師：{c.get("teacher","無")}")
               print(f"上課時間：星期{c.get("week","=")}第{c.get("section","=")}節")
               print(f"必選修：{"必修" if c.get("is_required","無") else "選修"}")
               enr = c.get("enrolled",0)
               limit = c.get("member_limit",0)
               status = "額滿" if enr>=limit else f"{enr}/{limit}"
               print(f"修課人數：{status} ")
               print("=========================================")
     else:
          print("查無資料")
elif s_c == "2":
     id = input("請輸入學生代碼：").strip() or None
     name = input("請輸入學生姓名：").strip() or None
     department = input("請輸入系級：").strip() or None
     enrolled = input("請輸入已選課程：").strip() or None
     
     
     res2 = student(student_data,student_id = id,student_name = name,department = department,enrolled_class = enrolled,)
     if res2:
          for s in res2:
               print("=========================================")
               print(f"學號：{s.get("student_id","無")}")
               print(f"姓名：{s.get("student_name","無")}")
               print(f"系級：{s.get("department","無")}")
               print(f"已選課程：{s.get("enrolled_class","無")}")
               print(f"學分上限：{s.get("credits_max","無")}")
               print("=========================================")
     else:
          print("查無資料")
else:
     print("請輸入正確查詢項目！")

