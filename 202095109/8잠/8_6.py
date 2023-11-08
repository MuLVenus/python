'''
    심화문제8.6
    오늘의 마지막 문제 
    해결 한 사람은 제출하고 수업 끝
'''
student_tuple=[('211101','강이안','010-123-1111'),('211102','박도민','010-123-2222'),('211103','김수정','010-123-3333')]
student_dict={}

for id,name,phone in student_tuple:
    print(f"{id}:{name}")
    student_dict[id]=[name,phone]
    
while(True):
    num=input("enter the student id:")
    print(f"{num} student is {student_dict[num][0]}, the phone number is {student_dict[num][1]}")