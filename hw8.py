def buy(d):
    print('[구입]')
    item=input('상품명? ')
    if item=='':
        return False

    n=input('수량은? ')
    d[item]=n
    print(f'장바구니에 {item} {n}개가 담겼습니다.\n')
    
def show(d):
    print(f'\n>>>장바구니 보기:{d}')


def find(d):
    print('\n[검색]')
    n=input('장바구니에서 확인하고자 하는 상품은? ')
    if n not in d:
        print(f'장바구니에 {n}은(는) 없습니다.')
    else:
        print(f'{n}은(는) {d.get(n)}개 담겨 있습니다.')

shopping_bag={}
while True:
    if buy(shopping_bag)==False:
        break

show(shopping_bag)
find(shopping_bag)
