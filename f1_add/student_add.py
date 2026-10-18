from course_add import errMessage
import valid_tool

def strToInteger(string: str):
    return int(string)

def removeBlank(ls_section: list):
    delete_times = ls_section.count("")
    for i in range(delete_times):
        ls_section.remove("")
    return ls_section

def student_add(ut_flag = False):
    s_id = input("請輸入學生學號: ")
    exit_code = valid_tool.s_validate_id(s_id)
    if exit_code is not None:
        errMessage(exit_code)
        return -1

    s_name = input("請輸入學生姓名: ")
    exit_code = valid_tool.s_valid_name(s_name)
    if exit_code is not None:
        errMessage(exit_code)
        return -1

    s_class = input("請輸入學生系級: ")
    exit_code = valid_tool.s_validate_class(s_class)
    if exit_code is not None:
        errMessage(exit_code)
        return -1

    s_credits_cap = input("請輸入該名學分上限: ")
    exit_code = valid_tool.s_validate_creditsCap(s_credits_cap)
    if exit_code is not None:
        errMessage(exit_code)
        return -1
    else: s_credits_cap = strToInteger(s_credits_cap)

    if ut_flag:
        s_enrolled = removeBlank(input("請輸入學生已選課程代號 (一個或多個，以空白分開): ").split())
        exit_code = s_enrolled(s_enrolled)
        if exit_code is not None:
            errMessage(exit_code)
            return -1
    else: s_enrolled = []
    return {"student_id": s_id, "name": s_name, "department": s_class, "course_id": s_enrolled, "activity_id": [], "credits_max": s_credits_cap, "credits_min": None}
