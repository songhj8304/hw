def get_fixed_price(dp):
    global dr
    p=100/(100-dr)*dp
    return p

dr=int(input('할인율은? '))
    
adp=float(input('A 상품의 할인된 가격은? '))
bdp=int(input('B 상품의 할인된 가격은? '))

atemp=get_fixed_price(adp)
print('A 상품의 정가는' ,atemp,'원')

btemp=get_fixed_price(bdp)
print('B 상품의 정가는' ,btemp,'원')




