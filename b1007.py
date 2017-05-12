# -*- coding:utf-8 -*-
# time out when prime > 1000

def odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = odd_iter()
    while True:
        k = next(it)
        yield k
        it = filter(not_divisible(k), it)
def main():
    n = int(input())
    ans = 0
    b = 2
    for a in primes():
        if a <= n:
            if a - b == 2:
                ans = ans + 1
            b = a
        else:
            break

    print(ans)
    return 0


if __name__ == '__main__':
    main()
