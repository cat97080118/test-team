import re
# c_: course function
# s_: student function

def roomInData(room: str, ls_db: list):
    return room in ls_db

def isBusy(sections: list, ls_db: list):
    for each in sections:
        if each in ls_db: return True
    return False

def id_isOccupy(id_: str, ls_db: list):
    for each in ls_db:
        if id_ == each: return True
    else: False

def c_validate_id(data: str, ls_db = None):
    if data == "": return 0
    if len(data) != 9: return 2
    if ls_db is None: ls_db = calldata("c_id")
    if id_isOccupy(data, ls_db): return 1
    else: return None

def c_validate_name(data: str):
    if data == "": return 0
    else: return None

def c_validate_section(data: list, ls_db = None):
    if data == []: return 0
    for each in data:
        if not re.match(r"^[1-7][1-9a-c]$", each): return 1
    return None

def c_validate_required(string: str):
    if string == "": return 0
    if string != 'yes' or string != 'no': return 2
    else: return None

def c_validate_int(integer: str):
    if integer == "": return 0
    try:
        int(integer)
    except: return 2
    else: return None

def c_validate_credits(credits: str):
    if credits == "": return 0
    return 2 if (credits * 2 % 1 != 0) else None

def c_validate_teacher(teacher: str, sections: list, ls_db = None):
    if teacher == "": return 0
    if ls_db is None: ls_db = calldata("section", key = teacher)
    if isBusy(teacher, sections, ls_db): return 3
    else: return None

def c_validate_room(room: str, ls_db = None):
    if room == "": return 0
    if ls_db is None: ls_db = calldata("classroom")
    if not roomInData(room, ls_db): return 4
    else: return None

def s_validate_id(data: str, ls_db = None):
    if data == "": return 0
    if len(data) != 7: return 2
    if ls_db is None: ls_db = calldata("s_id")
    if id_isOccupy(data, ls_db): return 5
    else: return None

def s_valid_name(name: str):
    if name == "": return 0
    else: return None

def s_validate_class(string: str):
    department = ('資工', '資財', '化工', '電子', '車輛', '機械', '電機', '土木', '能源', '分子', '工管', '經管', '建築', '互動', '英文', '電資', '材資', '光電')
    grade = ('一', '二', '三', '四')
    cls = ('', '甲', '乙', '丙', '丁')
    if string == "": return 0
    if len(string) > 4: return 2
    dep_in = string[:2]
    grade_in = string[2]
    cls_in = string[3] if len(string) > 3 else ""
    if dep_in not in department: return 2
    if grade_in not in grade: return 2
    if cls_in not in cls: return 2
    return None

def s_validate_creditsCap(credits: str):
    if credits == "": return 0
    try: int(credits)
    except: return 2
    else: return None

def s_validate_enrolled(courses: list):
    if courses == []: return 0
    for each in courses: 
        if len(each) != 7: return 2
    return None