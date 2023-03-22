def get_integer(prompt):
    a=int(input(prompt))
    return a

def exchange(b):
    n500=b//500
    b%=500
    n100=b//100
    b%=100
    n50=b//50
    b%=50
    n10=b//10

    print('500원 동전의 개수:', n500)
    print('100원 동전의 개수:', n100)
    print('50원 동전의 개수:', n50)
    print('10원 동전의 개수:', n10)


prompt='동전으로 교환하고자 하는 금액은? '
res=get_integer(prompt)
exchange(res)
    
