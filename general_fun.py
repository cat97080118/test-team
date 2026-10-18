'''
此 Python file 為存放通用 function 的地方，可自行新增通用 function 或導入來呼叫
'''

import json
import subprocess
import os
from pathlib import Path
from typing import Any, Union

PathLike = Union[str, Path] # 定義路徑型別別名


def save_json(file_path: PathLike, data: Any, indent: int = 2) -> None:
    """
    將資料序列化並儲存為 JSON 檔案。
    若目標資料夾不存在，會自動創建相應目錄。
    參數 file_path: JSON 檔案路徑。
    """
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=indent)


def load_json(file_path: PathLike, default: Any = None) -> Any:
    """
    讀取 JSON 檔案並轉換為 Python 物件。
    參數 file_path: JSON 檔案路徑。
    參數 default: 若指定此參數，在檔案不存在時會回傳 default 值而非報錯。
    """
    path = Path(file_path)

    if not path.exists():
        if default is not None:
            return default
        raise FileNotFoundError(f"找不到指定的 JSON 檔案：{path.resolve()}")

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def course_conflict(schedule: list) -> Any:
    """
    注意：list 格式為暫定使用，之後可能會更改成使用 dict 格式。

    課程衝堂檢查功能。
    參數 schedule：課表。
    課表格式：[課程號碼, [時間1, 時間2, 時間3, ...]]。
    內部參數：id, time = 課程號碼, 課程時間陣列。
    內部參數 conflict：比對後是否衝堂。
    """

    for i in range(len(schedule)):
        for j in range(i+1, len(schedule)):
            id1, time1 = schedule[i]
            id2, time2 = schedule[j]

            for t1 in time1:
                for t2 in time2:
                    if t1 == t2:
                        return f"{id1} 與 {id2} 在 {t1} 時有衝堂！"
                    
    return "課程無衝堂"

def clear_screen():
    """
    用於清除終端機顯示的內容。
    在 Windows、Linux 及 macOS 上皆可使用。
    """
    subprocess.run(['cls' if os.name == 'nt' else 'clear'], shell=True)

def classroom_conflict(classroom: str, class_time: str, data: dict):
    target_times = [class_time] if isinstance(class_time, str) else list(class_time)
    has_conflict = False

    for course in data.get("courses", []):
        if course.get("class_room") == classroom:
            conflict_times = [t for t in target_times if t in course.get("class_time", [])]
            if conflict_times:
                print(f"衝突課程: {course['course_id']} {course['course_name']}, 衝突時段: {conflict_times}")
                has_conflict = True

    return not has_conflict

def credit_input(placeholder: str, allow_null_string: bool = True):
    
    """
    用於檢查輸入學分的格式並返回轉為float的學分
    placeholder : 提示輸入詞
    allow_null_string : 使否允許空字串輸入，若為True且輸入空字串，將return空字串
    """

    credits = input(placeholder)
    while True:
        if credits == "":
            if allow_null_string:
                return credits
            else:
                print("【錯誤】此欄位不可為空，請輸入學分數！")
                credits = input(placeholder)
                continue
                
        if credits.lower() == 'q':
            if not allow_null_string:
                print("【錯誤】此欄位不可為空，必須輸入學分數才能離開！")
                credits = input(placeholder)
                continue
            return ""

        try:
            val = float(credits)
            
            if val < 0:
                print("【錯誤】學分數不得為負！")
                credits = input("請重新輸入，或輸入 'q' 取消並離開：\n")
                
            elif val * 2 != int(val * 2):
                print("【錯誤】學分數只能為大於0之0.5的倍數！")
                credits = input("請重新輸入，或輸入 'q' 取消並離開：\n")
                
            else:
                return val

        except ValueError:
            print("【格式錯誤】學分數只能為數字，且為大於0之0.5的倍數！")
            credits = input("請重新輸入，或輸入 'q' 取消並離開：\n")
            
        except Exception as e:
            print(f"【未知錯誤】發生錯誤：\n{e}\n請聯絡管理員")
            credits = input("請重新輸入，或輸入 'q' 取消並離開：\n")



def class_time_input(placeholder: str, allow_null_string: bool = True):
    class_time_list = []
    
    valid_days = "1234567"
    valid_periods = "123456789abc"
    
    class_time = input(placeholder)
    
    while True:

        if class_time == "":
            if class_time_list:
                return class_time_list
            else:

                if allow_null_string:
                    return ""
                else:
                    print("【錯誤】此欄位不可為空，請至少輸入一個時段！")
                    class_time = input(placeholder)
                    continue
        
        if class_time.lower() == 'q':
            if not class_time_list and not allow_null_string:
                print("【錯誤】此欄位不可為空，必須至少輸入一節課才能離開！")
                class_time = input(placeholder)
                continue
            return class_time_list if class_time_list else ""
            
        class_time = class_time.lower()
        
        if len(class_time) != 2 or class_time[0] not in valid_days or class_time[1] not in valid_periods:
            print("【格式錯誤】請輸入兩碼，例如 41 (週四第1節)、5a (週五第a節)。")
            class_time = input("請重新輸入，或輸入 'q' 取消並離開：\n")
            continue
            
        if class_time in class_time_list:
            print(f"【重複輸入】時段 {class_time} 已經在列表中了！")
            class_time = input("請重新輸入其他時段，或直接按 Enter 結束：\n")
            continue
            

        class_time_list.append(class_time)
        print(f"成功加入：{class_time} (目前課程時段: {class_time_list})")
        

        class_time = input("請輸入下一個時段（直接按 Enter 結束輸入）：\n")

# if __name__ == "__main__":
#     result = classroom_conflict("科研231", "25", load_json("data.json"))
#     print(result)