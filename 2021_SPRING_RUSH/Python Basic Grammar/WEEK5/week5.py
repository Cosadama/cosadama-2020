"""
작성자 : 김문희
내용 : 함수, 파일입출력
"""
#함수
#실습 1

def print_dan(x):
	for i in list(range(1,10)):
		print (x * i)

dan = int(input("숫자를 입력하세요"))
while dan != 0:
	print_dan(dan)
	dan = int(input())

# 실습 2

num = float(input('온도는?, 단 숫자만 입력하라.'))
scale = str(input('섭씨는 c, 화씨는f를 입력하세요')).lower()

def celtofah(x):
	f = ((9/5) * x) + 32
	return f

def fahtocel(x):
	c = ((5/9) * (x - 32))
	return c

if scale == 'c' :
	print('섭씨 %0.1f도는 화씨 %0.1f도이다' % (num, celtofah(num)))
elif scale == 'f':
	print('화씨 %0.1f도는 섭씨 %0.1f도이다.' % (num, fahtocel(num)))

#파일입출력
#실습 1
def Memopad ():
	f = open('input.txt','w')
	while True:
		data = str(input('내용을 한 줄씩 입력하세요'))
		if data != 'end':
			f.write((data+'\n'))
		else:
			f.close()
			print('파일을 저장하였습니다.')
			break
	f = open('input.txt','r')
	mlines = f.readlines()
	for line in mlines:
		print(line)
	print('이 파일을 %d행으로 구성되어있습니다' % len(mlines))
#실습 2
import os
os.chdir('C:/Users/lunar/Downloads')
f = open('score.csv','r',encoding='utf-8')
while True:
	line = f.readline()
	if line =='':break
	v = line.split(',')
	v = v[:-1]
	try:
		int(v[0])
		for i in range(4) :
			v[i] = int(v[i])
		dict = {}
		dict[v[0]] = [v[1:4],v[1]+v[2]+v[3],(v[1]+v[2]+v[3])/3]
		print("%s학생의 총점은 %d점, 평균은 %0.2f점입니다."
		%(v[0],dict[v[0]][1],dict[v[0]][2]))
	except ValueError:
		continue

# 과제 1
f1 = open('test.txt','w')
data = str(input("데이터를 입력하세요"))
f1.write(data)
f1.close()
f2 = open('test.txt','r')
print(f2.read())

# 과제 2
def lotto_generator(x):
	import random
	valist = list(range(1,46))
	lottery_nums = []
	for i in range(6):
		random.shuffle(valist)
		val  = random.choice(valist)
		lottery_nums.append(val)
	print("\n%s회 :" % x , end = " ")
	for i in lottery_nums:
		print(i,end = " ")
	return lottery_nums

def lotto_stat(x):
    results = {}
    for i in range(1,46):
        results[i] = 0
    for i in range(1,x+1):
        lottery_nums = lotto_generator(i)
        for i in lottery_nums:
            results[i] = results[i] + 1
    print("\n")
    for i in results.keys():
        print("%s : %d회" % (i,results[i]))
    return results


results = lotto_stat(30) """ 람다에 들어가서 무한 루프하는 것을
 							방지하기 위해 담아줍니다."""

this_nums = sorted(results, key= lambda c :results[c], reverse=True)[:6]

print("이 주의 로또 번호 :",end = " ")
for i in this_nums:
    print(i, end = " ")

#과제 3
def voc():
    import os
    os.chdir('C:/Users/lunar/Downloads')
    f = open('dict_test.txt','r')
    voca = {}
    while True:
        v = f.readline()
        if v == '' : break
        v = v[:-1]
        v_list = v.split(':')
        voca[v_list[0].strip()] = v_list[1]

    key = str(input('단어?')).lower()
    print('%s %s' % (key, voca[key]))

# 과제 4
dict = voc()
voc_list = []
p_key = 'apple'
while True:
        key = str(input('%s 끝말잇기?, 종료하려면 end를 입력하세요.' %p_key))
        if  key == 'end':break
        elif len(key) > 5 :
            print('단어가 길어요')
            continue
        elif key not in dict :
            print('사전에 없는 말이에요')
            continue
        elif key in voc_list:
            print('중복된 단어에요')
            continue
        elif key[0] != p_key[-1]:
            print('%s의 끝 문자로 시작하세요' %p_key)
        elif len(key) < 5 :
            print('단어가 짧아요')
        elif dict[key].find('n.') == -1:
            print('명사를 입력하세요')
        else :
            print('%s 끝말잇기?' % key)
            voc_list.append(key)
            p_key = key

#과제 5
import os
os.chdir('C:/Users/lunar/Downloads')
f = open('score.csv','r')
report = []
while True:
	v = f.readline()
	v = v[:-1]
	if v == '' : break
	v = v. split(',')
	if v[0] == '번호':
		v.insert(0,'석차')
		v.append('총점')
		v.append('평균')
		report.insert(0,v)
	else :
		for i in range(4):
			v[i] = int(v[i])
		v.append(v[1]+v[2]+v[3])
		v.append((v[4]/3))
		report.append(v)

report[1:] = sorted(report[1:],key = lambda k:k[-1], reverse= True)
for i in range(1,11):
	report[i].insert(0,i)
f1= open('report.txt','w')

for i in report:
    print(i)
    if type(i[0]) == str:
        data = "%s " *7 % (i[0],i[1],i[2],i[3],i[4],i[5],i[6])
    else:
        data  = "%4d %4s %4d %4d %4d %4d %0.1f" % (i[0],i[1],i[2],i[3],i[4],i[5],i[6])
    f1.write(data)
    f1.write('\n')
f1.close()
