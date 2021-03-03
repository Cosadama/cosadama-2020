
#-*-coding :cp949 -*-

"""
작성자 : 김문희
제목: 1주차 실습
"""

#실습 1

print(12345678901234567890 * 98765432109876543210) #1
print(0xaa + 55) #2
print(1/3+1/3+1/3) #3
print(0.1+0.1+0.1) #4

a = 1.2 * 3.4 * 5.6 * 7.8

print(a) #5

print(a - int(a)) #6

print(0.0000000001234*9876)

#실습 2
import math
print(round(0.1 + 0.1 + 0.1, 2)) #1
print(math.pi * 5.2**2)#2

#실습 3

print(((1000%99)%8)%5) #1
print(4**4**4 + 3**3 + 2) # 2
import fractions
print(fractions.Fraction(3**4/5**(-2)) # 3
print((1+137%7)%7)
from math import pi
print(int(pi*1000)/1000)

#3. 변수

#실습 1
radius = 3.5 # 1번
area = math.pi*radius**2
print(area)

money = 100
rate = 0.25
sum_1 = money*(1+rate)**12 #2번
sum_2 = money*(1+rate)**24
sum_3 = money*(1+rate)**36
print(sum_1,sum_2,sum_3)

#실습 2
print("당신의 생년,월,일을 차례로 입력하세요")
year=int(input('생년?'))
month=int(input('월?'))
day=int(input('일?'))
print('당신은',year,'년',month,'월',day,'일에 태어났습니다.')
print('생년월일을 합하면',year+month+day,"입니다.")

#실습 3
a = int(input('a=?')) #1
b = int(input('b=?'))
c=int(input('c=?'))
print((-b+math.sqrt(b**2-4*a*c)/2*a), (-b-math.sqrt(b**2-4*a*c)/2*a))

r = int(input('반지름을 입력하세요'))
print('원주:',round(math.pi*2*r,2))
print("면적:",round(math.pi*r**2,2))
