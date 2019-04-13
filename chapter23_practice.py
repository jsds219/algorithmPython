def fib(n):
    if n in (1, 2):
        return 1
    return fib(n-1) + fib(n-2)

print(fib(10))

memo = {}

def fib2(n):
    if n in memo:
        return memo[n]

    if n in (1,2):
        memo[n] = 1
        return 1
    result = fib2(n-1) + fib2(n-2)

    memo[n] = result

    return result

print(fib2(64))
