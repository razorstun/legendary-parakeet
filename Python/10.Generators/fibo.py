def gen_fibo(num):

    a = 1
    b = 1
    for i in range(num):
        yield a
        a,b = b,a+b

for number in gen_fibo(10):
    print(number)