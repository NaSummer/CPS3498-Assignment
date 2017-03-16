def fac(n):
    i = 1
    ans = 1
    while (i < n):
        i = i + 1
        ans = ans * i
    return ans

def c(n, k):

    i = k + 1
    tmp = 1
    while (i <= n):
        tmp = tmp * i
        i = i + 1

    # print(tmp)
    # print(fac(n - k))

    tmp = tmp / fac(n - k)

    print(tmp)

    return int(tmp)

# print(c(1, 0))


def num_odd(n):
    count = 0
    k = 0
    while (k <= n):
        if (c(n, k) % 2 == 1):
            count += 1
        k += 1
    return count

def calculate_k(n):
    k = 0
    while(n!=0):
        if (n % 2 == 1):
            k += 1
        n = int(n / 2)
    return k


n = 57
i = 57
while (n <= i):
    k = calculate_k(n)
    print(num_odd(n))
    if (num_odd(n) == pow(2, k)):
        print("n = " + str(n) + "; k = " + str(k) +": True")
    else:
        print("n = " + str(n) + "; k = " + str(k) +": False")
    n += 1