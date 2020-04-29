def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


print(prime_factors(40))

[2,3,4,5,6]

6! =120

2+2+2+2+2+2+2+2+2+2+2+