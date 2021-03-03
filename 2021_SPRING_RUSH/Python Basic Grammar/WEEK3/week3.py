"""
작성자 : 김문희
작성일 : 2020-01-21
"""

# 실습1

info = {'950102-1010101':['홍길동','흑석동1-1','010-4444-5555'],
        '961212-2211221':['홍길녀','흑석동2-2','010-8888-1111']}

# Key = 주민등록번호
# Value의 자료형 : List

# 실습2

teldic = {'강감찬' : '010-3333-4444', '김유신':'010-3928-0391',
	  '이순신' : '010-8492-3092', '홍길동' : '010-2727-0948'}
name_list = list(teldic.keys())
name = input("이름은?")

while name :
    if  name in name_list:
        print(name,"의 전화번호는",teldic[name],sep='' )
        
    elif name not in name_list:
        print(name,"는(은) 없어요",sep='')

    break

# 실습3
n =100000
s = []
while n in range(100000,-1,-1):
    if n == 0:
        s.sort()
        print("27과 86의 최소공배수는 ",s[0],"입니다.",sep='')
    if n%27==0 and n%86 ==0:
        s.append(n)
    n=n-1

# 실습 4

a = {'홍길동':['서울시 동작구 흑석로 84','02-820-0001']}
id_list = list(a.keys())
id = str(input("이름?"))
if id in id_list :
	print("주소 :", a[id][0])
	print("전화번호:",a[id][1])
if id not in id_list :
	print("새로운 데이터입니다")
	a[id] = []
	a[id].append(str(input("주소를 입력하세요 : ")))
	a[id].append(str(input("전화번호를 입력하세요 :")))


# 과제

# 과제 1
from math import *

while True :
    a = float(input("숫자를 입력하세요. (종료하려면 숫자 0을 입력하세요.)"))
    if a == 0:
        break
    if a - int(a) == 0:
        print(int(sqrt(a**2)))
    else:
        print(sqrt(a**2))
        
#과제 2
district_list = ['흑석동','사당동','상도동','노량진동','규동']
district = str(input("동을 입력하세요"))
if district not in district_list:
    district_list.append(district)
    print(district_list.index(district)+1,"번째 동으로 등록합니다.")
else :
    print(district_list.index(district)+1,"번째 동입니다.")

#과제 3
menu = {'noodle' : 500, 'ham' : 200, 'egg':200, 'spagheiit' : 900}
dishes = tuple(menu.keys())

while True :
    order = str(input(dishes))
    if order in dishes :
        print(menu[order],"원 입니다.", sep = '')
        break
    if order not in dishes : 
        print("그런 메뉴는 없습니다.")
        continue
#과제 4
def printing():
	a = []
	print("데이터를 입력하세요(입력을 마치려면 0을 입력하세요)")
	while True :
		b=int(input())
		if b!=0:
			a.append(b)
			continue
		break
	print("결과 : ", end="")
	for x in a:
		print(x,sep=" ",end=" ")
	print("(",len(a),"개)")

#과제 5
def game():
	import random
	round = 0
	p1_score = 0
	p2_score = 0
	p1 = input("1 플레이어의 이름은?")
	p2 = input("2 플레이어의 이름은?")
	while p1_score < 30 and p2_score <30:
			round = round + 1
			p1_dice = random.randint(1,6)
			p2_dice = random.randint(1,6)
			p1_score = p1_score + p1_dice
			p2_score = p2_score + p2_dice
			print(round,"라운드:",p1,"은",p1_dice,"가 나왔습니다.","현재 위치",p1_score)
			print(p2,"은",p2_dice,"가 나왔습니다.","현재 위치",p2_score)
	if p1_score >= 30:
		print(round,"라운드만에",p1,"이 이겼습니다.")
	else:
		print(round,"라운드만에",p2,"이 이겼습니다.")
        
