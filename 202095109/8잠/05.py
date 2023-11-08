'''
작성일:20203년 11월 8일
작성자:양사호 202095109
설명:생화문제 8-3
    학번,이름, 전화번호의 3방의 요쇼를 가지는
    student_tuple라는 튜들이 촌제한다
    
    이유츨을 수정하여 {학번:(이름,전화번호)}의 창으로
    이부어진 딕서너리를 만들이 출력하시오
    
    이 정보를 이용하여 학생의 학번을 입력 받아
    이츰과 전화번호를 출력하는 학사정보 츠르그램을 작성
    
    student_tuple의 마지막 항목으로 학점을 추가한다
    이 정보를 바탕으로 딕셔너를 만들이 출력하시오
    
    핛생의 학점 평균을 출력하시오
'''

student_tuple=[('202095109','양사호','010-5941-0819'),('202095110','양오호','010-5941-0820'),('202095111','양육호','010-5941-0821'),('202095112','양질호','010-5941-0822')]
student_dict={}

for id_num,name,phone in student_tuple:
    student_dict[id_num]=[name,phone]
    
for key,value in student_dict.items():
    print(f"{key}:{value}")

number=input("enter student id:")
print(f"name:{student_dict[number][0]}")
print(f"phone:{student_dict[number][1]}")

student_dict['202095109'].append(4.5)
student_dict['202095110'].append(3)
student_dict['202095111'].append(2.5)
student_dict['202095112'].append(3.2)

for key,value in student_dict.items():
    print(f"{key}:{value}")
print()

sum=0
for key,value in student_dict.items():
    sum+=student_dict[key][2]
print(f"{sum/len(student_dict):.2f}")