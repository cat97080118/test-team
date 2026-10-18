import valid_tool

def instructionToBool(string: str, debug = False):
    if string == 'yes': return True
    elif string == 'no': return False
    else:
        if debug: print("instructionToBool(): Invalid input. Input should be yes or no")
        return -1

def strTofloat(string: str):
    return float(string)

def strToInteger(string: str):
    return int(string)

def removeBlank(ls_section: list):
    delete_times = ls_section.count("")
    for i in range(delete_times):
        ls_section.remove("")
    return ls_section

def errMessage(exit_code, debug = False):
    if exit_code is None: return
    code_dict = {"BLANK", "ID_REAPET", "INPUT_INVALID", "BUSY_TEACHER", "ROOM_NOT_EXISTED", "STUDENT_ID_REPEAT"}
    if (exit_code is str) and (exit_code in code_dict):
        exit_code = code_dict[exit_code]
    meg = {
        0: "錯誤: 輸入資料不可為空白。",
        1: "錯誤: 經查此代碼已存在於資料庫。",
        2: "錯誤: 輸入格式不符或不符需求。",
        3: "錯誤: 輸入老師在其餘課堂互相衝突",
        4: "錯誤: 輸入教室並不存在。",
        5: "錯誤: 輸入學號已存在於資料庫中"
    }
    if exit_code in meg: print(meg[exit_code])
    else: 
        if debug:
            print("errMessage(): Invalid exit_code")
            return -1

def course_add(ls_db = None):
    c_id = input("請輸入課程代號: ")
    exit_code = valid_tool.c_validate_id(c_id, ls_db)
    if exit_code is not None: 
        errMessage(exit_code)
        return -1
    
    c_name = input("請輸入課程名稱: ")
    exit_code = valid_tool.c_validate_name(c_name, ls_db)
    if exit_code is not None:
        errMessage(exit_code)
        return -1
    
    c_section = removeBlank(input("請輸入課堂時段 (多時段以空白分開): ").split(" "))
    exit_code = valid_tool.c_validate_section(c_section, ls_db)
    if exit_code is not None:
        errMessage(exit_code)
        return -1

    c_teacher = input("請輸入課程教師: ")
    exit_code = valid_tool.c_validate_teacher(c_teacher)
    if exit_code is not None:
        errMessage(exit_code)
        return -1

    c_room = input("請輸入課程所在教室編號: ")
    exit_code = valid_tool.c_validate_room(c_room)
    if exit_code is not None:
        errMessage(exit_code)
        return -1

    c_isRequired = input("請輸入是否為必修課程(yes/no): ")
    exit_code = valid_tool.c_validate_required(c_isRequired)
    if exit_code is not None:
        errMessage(exit_code)
        return -1
    else: c_isRequired = instructionToBool(c_isRequired)

    c_credit = input("請輸入該課堂的學分數: ")
    exit_code = valid_tool.c_validate_credits(c_credit)
    if exit_code is not None:
        errMessage(exit_code)
        return -1
    else: c_credit = strTofloat(c_credit)

    c_capacity = input("請輸入課程之人數上限: ")
    exit_code = valid_tool.c_validate_int(c_capacity)
    if exit_code is not None:
        errMessage(exit_code)
        return -1
    else: c_capacity = strToInteger(c_capacity)
    return {"course_id": c_id, "course_name": c_name, "credits": c_credit, "teacher": c_teacher, "member_limit": c_capacity, "enrolled": 0, "class_time": c_section, "class_room": c_room, "is_required": c_isRequired}