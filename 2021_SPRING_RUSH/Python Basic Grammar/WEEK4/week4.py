"""
작성자 : 김문희
내용 : 문자열
"""


 #실습 1
a = str(input("문장을 입력하세요"))
word_count = a.count(" ") + 1
a = a.replace(" ","\n")
print(a)
print("(총",word_count,"단어)")




#실습 2
def num():
	number_list = []
	sum = 0
	while True:
		number = int(input("""숫자를 입력하세요.
                                   단, 1부터 10000사이의 정수를 입력하세요"""))
		number_list.append(number)
		for i in number_list:
			print("+ %4d" % i)
			sum = sum + i
		print("= %4d" %sum)


#실습 3
a = str(input("수식을 입력하세요. 단, 덧셈만 가능합니다."))
b = a.split("+")
sum = 0
for i in b :
    sum = sum + int(i)
print("합계는 %d" % sum)

# 과제

#1
print("%7s" % "HONG")
print("%4d" % 273)
print("%9.3f%%" %153.288)

#2
student = ['a','b','c','d','e']
import random
Report_card = {}
for i in student:
	k = int(random.randint(1,101))
	e = int(random.randint(1,101))
	m = int(random.randint(1,101))
	Report_card[i] = [[k,e,m],k+e+m,(k+e+m)/3]
	print("""%s학생의 %s점수는 %d점,\n%10s점수는 %d점,\n%10s점수는 %d점,
총점은 %d점, 평균은 %0.2f점입니다.\n""" % (i,"국어",k,"영어",e,"수학",
				m,Report_card[i][1],Report_card[i][2]))

#3

sentence ="""Not all that Mrs Bennet however with the assistance of her five daughters could ask on the subject was sufficient to draw from her husband any satisfactory description of Mr Bingley"""

a = sentence.upper()
print("m은 총 %d회 출현합니다." % a.count("M"))

word_list = list(a.split(" "))
word_list.sort()
word_dic = {}
for i in word_list:
    if i in word_dic.keys():
        word_dic[i] = word_dic[i] + 1
    else:
        word_dic[i] = 1
for i in word_dic:
    print("%-20s 출현횟수 : %d회" % (i,word_dic[i]))
#4
a = str(input("수식을 입력하세요. 단, 덧셈과 뺄셈만 가능합니다."))
a = a.replace("-","+-")
a = a.split("+")
sum = 0
for i in a:
    sum = sum + float(i)
print("결과는 %d" % sum)

#5
introduction = str(input("문장을 입력하세요."))

i= introduction.split('.')[0]

if i.find('저는') == -1:
    name = i[i.index('이름은')+3:i.index('입니다')].strip()
elif i.find('라고') != -1 :
    name = i[i.index("저는")+2:i.index('라고')].strip()
else :
    name = i[i.index('저는')+2:i.index('입니다')].strip()
print("이름: %s" % name)
