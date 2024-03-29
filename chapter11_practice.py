"""
1) 다음의 print 결과는 ?
"""
s = "Python is awesome"
print(s[1:3])

"""
2) "Spam and Eggs" 를 입력할 때 다음 프로그램의 출력 결과는 ?
"""
def main():
    msg = input("Enter a phrase:  ")
    for w in msg.split():
        print(w[0], end="")

main()

"""
3) 다음의 출력 결과는 ?
"""
for x in "Mississippi".split("i"):
    print(x, end="")

"""
4) 다음 출력 결과는 ?
"""
s = "Jane Doe"
print(s[3 : 1 : -1])

"""
5) s = "Hello, Python World" 을 alphabet 별로 몇개인지 계산 (단, 대소문자 무시)
    * hint : dictionary 와 s.lower() 사용
"""
s = "Hello, Python World"
s = s.replace(" ", "")
s = s.replace(",", "")
word_cnt = {}
for letter in s:
    if letter in word_cnt:
        word_cnt[letter] += 1
    else:
        word_cnt[letter] = 1

for k, v in sorted(word_cnt.items()):
    print(k, '=', str(v), end=", ")
