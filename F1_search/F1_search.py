def course(course_list:list,
           course_id:str = None,
           course_name:str = None,
           teacher:str = None,
           week:int = None,
           section:str = None,
           is_required:bool = None,
           is_available:bool = False):
    result = []
    for course in course_list:
        if course_id and course_id.upper() not in course.get("course_id","").upper():
            continue    
        if course_name and course_name.upper() not in course.get("course_name","").upper():
            continue
        if teacher and teacher not in course.get("teacher",""):
            continue
        if week is not None and week != course.get("week",""):
            continue
        if section is not None and section != course.get("section",""):
            continue
        if is_required is not None and course.get("is_required","") != is_required:
            continue
        if is_available:
            enrolled = course.get("enrolled",0)
            member_limit = course.get("member_limit",0)
            if enrolled>=member_limit:
                continue
        result.append(course)  
    return result

def student(student_list:list,
            student_id:str = None,
            student_name:str = None,
            department:str = None,
            enrolled_class:list = None):
    result = []
    for student in student_list:
        if student_id and student_id.upper() not in student.get("student_id","").upper():
            continue
        if student_name and student_name.upper() not in student.get("student_name").upper():
            continue
        if department and department.upper() not in student.get("department","").upper():
            continue 
        if enrolled_class:
            cla = student.get("enrolled_class","")
            match = any(enrolled_class.upper() in c.upper() for c in cla)
            if not match:
                continue
        result.append(student)
    return result



