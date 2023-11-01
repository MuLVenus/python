'''
    작성일:2023년 11원 1일
    작성자:양사호
    설명:lab 7-6
'''

city_info=[('서울',9765),('부산',3441),('인천',2954),('광주',1591),('대전',1531)]

max_pop=0
min_pop=999999999999999
total_pop=0

max_city=None
min_city=None

for city in city_info:
    total_pop+=city[1]
    if city[1]>max_pop:
        max_pop=city[1]
        max_city=city
    if city[1]<min_pop:
        min_pop=city[1]
        min_city=city
        
print(f"the most pop city is {max_city[0]}: {max_pop}")
print(f"the least pop city is {min_city[0]}: {min_pop}")
print(f"the totol pop in country is {total_pop}")
print(f"the average pop is {total_pop/len(city_info)}")