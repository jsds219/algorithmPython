"""
1) 다음의 출력 결과는 ?
"""
d = {'a': 2, 'b': 4, 'c': 9}
for x in sorted(d):
    print(d[x], end="")

"""
2) 다음의 출력 결과는 ?
"""
d = {'a': 2, 'b': 4, 'c': 9}
for x in sorted(d.values()):
    print(x, end="")

"""
3) 다음의 출력 결과는 ?
"""
d = {'a': 2, 'b': 4, 'c': 9}
for x in sorted(d.items()):
    print(x, end="")
    
