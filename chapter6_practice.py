"""
1) 다음 프로그램의 결과값은 ?
"""
xlist = []
xlist.append('Good')
xlist.append('Morning')
print(xlist)

xlist.append([3, 4])
print(xlist)

"""
2) 다음 명령어의 결과값은 ?
"""
list1 = list(range(-3, 3))
print(list1)

list2 = list(range(-3, 3, 3))
print(list2)

list3 = list(range(-3))
print(list3)

"""
3) 다음 list 의 element 를 오름차순으로 정렬 (ascending sort) 한다.
또한, 내림차순 (descending order)으로 정렬한다.
sort(), sort(reverse=True) 함수를 사용한다.
"""
xlist = [2, 1, 3, 5, 4]

print(sorted(xlist))
print(sorted(xlist, reverse=True))

"""
4)    ∑𝑛𝑘=1𝑘  을 계산하는 함수 sigma(n) 을 작성하라. (n 은 정수)
"""
def sigma(n):
    k = list(range(1, n+1))
    return sum(k)

print(sigma(10))

"""
5) xlist = [1, 2, 3, 4] 를 한줄에 출력하고 각 element 의 사이는 '/' 로 구분하라.
"""
xlist = [1, 2, 3, 4]

for n in xlist:
    print(n, end="/")
