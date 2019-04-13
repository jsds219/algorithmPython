"""
1) 다음 list 에서 10 과 30 사이의 숫자 중 홀수만 골라 출력하라.
    xlist = [-5, 5, 10, 12, 13, 14, 15, 25, 30, 40, 55, 100]
"""
xlist = [-5, 5, 10, 12, 13, 14, 15, 25, 30, 40, 55, 100]

for n in xlist:
    if n >= 10 and n <= 30:
        if n % 2 == 1:
            print(n)

"""
2) 다음 영어 문장에서 너(you)는 몇번 나오는가 ?
    "You don't go to school on Saturday. I want you be happy.
    I miss you very much. You don't forget me"
"""
s = "You don't go to school on Saturday. I want you be happy. I miss you very much. You don't forget me"

s = s.lower()
print(s.count("you"))

"""
3) 파이썬 강좌의 수강생 목록은 다음과 같다. 어떤 사람이 수강생 목록에 존재하는지
    check 하는 함수를 작성하라.
    목록에 존재하면 True, 존재하지 않으면 False 를 반환한다.

   학생부 : ["김철수", "홍길동", "문재인", "김정은", "트럼프", "성춘향"]
"""
def check_list(lst, name):
    if name in lst:
        return True
    else:
        return False

students = ["김철수", "홍길동", "문재인", "김정은", "트럼프", "성춘향"]

print(check_list(students, "홍길동"))

"""
4) 다음의 주민번호 리스트에서 남, 녀 별로 90 년생 이후 출생자를 골라내라.
"""
id_list = ['920801-1041798', '800902-2048746', '971010-1023987', '871203-2014987',
         '820801-1041798', '900902-2048746', '941010-1023987', '971203-2014987']

man = []
lady = []

for id in id_list:
    if id[:2] >= '90' and id[7] == '1':
        man.append(id)
    else:
        lady.append(id)

print('남성 =', man)
print('여성 =', lady)
