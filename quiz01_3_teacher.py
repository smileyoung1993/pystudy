# quiz01_3
# list와 dictionary

students = [
    {   
        "name": "Kim",
        "kor": 80,
        "eng": 90,
        "math": 80
    },
    {   
        "name": "Lee",
        "kor": 90,
        "eng": 85,
        "math": 85
    }
]
# 리스트에서 하나씩 받아온다.
for student in students: 
    total = student.get('kor')+student.get('eng')+student.get('math') # 사전에서 값을 받아와서 더한다
    average = total / 3
    student['total'] = total # 사전에 value값 추가
    student['average'] = average

print("students:",students)