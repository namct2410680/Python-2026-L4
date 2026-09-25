number_std = int(input("Enter number of student: "))
list_std =[]
for i in range(number_std):
    print(f"Enter infomation of student {i+1}: ")
    student_map={}
    student_map["id"] = input("Enter the id: ")
    student_map["name"] = input("Enter the name: ")
    student_map["DoB"] = input("Enter the Date of Birth: ")
    list_std.append(student_map)

number_course = int(input("Enter number of course"))
list_course=[]
for i in range(number_course):
    print(f"Enter infomation of course {i+1}: ")
    course_map={}
    course_map["id"] = input("Enter the id: ")
    course_map["name"] = input("Enter the name course: ")
    list_course.append(course_map)

mark_map = {}
selected_course_id = input("Enter the course ID to input marks: ")
mark_map[selected_course_id] = {}
for student in list_std:
    student_id = student["id"]
    student_name = student["name"]
    mark=float(input(f"Enter the mark for {student_id}-{student_name}"))
    mark_map[selected_course_id][student_id] = mark

print("List of student")
for student in list_std:
    print(f"Student ID: {student['id']}")
    print(f"Student name: {student['name']}")
    print(f"Date of Birth: {student['DoB']}")

print("List of course")
for course in list_course:
    print(f"Course ID: {course['id']}")
    print(f"Course name: {course['name']}")

course_to_show = input("\nEnter the course ID to show marks: ")
if course_to_show in mark_map:
    print(f"\n--- Marks for Course ID: {course_to_show} ---")
    for student in list_std:
        student_id = student["id"]
        if student_id in mark_map[course_to_show]:
            mark = mark_map[course_to_show][student_id]
            print(f"Student: {student['name']}, Mark: {mark}")
else:
    print("error")