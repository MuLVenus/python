'''
작성일:20203년 11월 15일
작성자:양사호 202095109
설명
'''

s="happy day"
print(s[0])
print(s[6:10])
print(s[:-2])

s="welcome to python"
print(s.split())

s="2023.11.15"
print(s.split('.'))

s="hello, world"
print(s.split(','))

s="welcom,to,python,and,bla,bla"
print(s.strip())
print([x.strip()for x in s.split(',')])

print(list('hello,world'))

print(','.join(['apple','grape','banana']))
print('-'.join('010.5941.0819'.split('.')))

print('010.5941.0819'.replace('.','-'))

s='hello,world'
print(s)
slist=list(s)
print(slist)

print(''.join(slist))

a_string='today as well,\n\thava a happy day'
print(a_string)

word_list=a_string.split()
print(word_list)

refined_string=' '.join(word_list)
print(refined_string)

s='Hello,World'
print(s)
print(s.lower())
print(s.upper())

s='           hello,world'
print(s.strip())
print(s.lstrip())
print(s.rstrip())

s='##########hello,world############'
print(s)
print(s.strip('#'))
print(s.lstrip('#'))
print(s.rstrip('#'))

s='www.silla.ac.kr'
print(s.find('.kr'))
print(s.find('x'))