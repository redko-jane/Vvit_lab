def is_prime(number):
    x=True
    for i in range(2,int(number**0.5)+1):
        if number%i==0:
            x=False
            break
    if number==2:
        return True
    else:
        return x
n=int(input('Введите число: '))
print(is_prime(n))
