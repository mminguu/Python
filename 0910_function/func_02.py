
# 매개변수 O 반환값 O

def name(ming):
    return (f'내 별명은{ming}이야.')
print(name('ming'))



# 매개변수 O 반환값 X

def name(ming):
    print(f'내 별명은{ming}이야.')
print(name('ming'))



# 매개변수 X 반환값 O

def name():
    return ('ming')



# 매개변수 X 반환값 X

def name():
    print('안녕')
print(f'내 별명은 ming 이야.')


