def read_single_digit(b):
    if b==0:
        return '영'
    elif b==1:
        return '일'
    elif b==2:
        return '이'
    elif b==3:
        return '삼'
    elif b==4:
        return '사'
    elif b==5:
        return '오'
    elif b==6:
        return '육'
    elif b==7:
        return '칠'
    elif b==8:
        return '팔'
    else:
        return '구'
    

def read_number(a):
    n1=a//100
    a%=100
    n2=a//10
    a%=10
    n3=a
    n1temp=read_single_digit(n1)
    n2temp=read_single_digit(n2)
    n3temp=read_single_digit(n3)
    return f'{n1temp} {n2temp} {n3temp}'


n=int(input('세 자리 정수 입력: '))
result=read_number(n)
print(result)
