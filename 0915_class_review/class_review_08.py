# 클래스
# 생성자
# 메소드
# __str__  __eq__  __ne__  __lt__  __gt__  __le__  __ge__
# property
# 객체생성

# 상품관리 클래스명 Product
# 상품명 : product_name , 가격 : product_price , 재고 : product_stock
# property , getter , setter , deleter , private 함수를 변수처럼 사용

class Product:
    def __init__(self , name , price , stock):
        self.product_name = name
        self.product_price = price
        self.product_stock = stock

        @property
        def name(self):
            return self._product_name
        
        def price(self):
            return self._price
        
        def stock(self):
            return self._stock
        
        def __str__(self):
            return f'상품명 : {self.product_name} / 가격 : {self.product_price} / 재고 : {self.product_stock}' #\n 줄바꿈

Products = [
    Product('아이폰', 1700000, 55),
    Product('맥북', 3300000, 10),
    Product('에어팟', 360000, 200)
]

for p in Products:
    # 노트북의 가격을 20% 인하
    if p.product_name == '노트북':
        p.product_price = p.product_price * 0.8 # 코드값

for p in Products:
    # 스마트폰은 가격을 10% 인상
    if p.product_name == '아이폰':
        p.product_price = p.product_price * 1.1 + p.product_price * 0.1
    print(p.product_name, p.product_price, p.product_stock)

# 전체제품 출력
for p in Products:
    print(p)



# 제품 추가
# 제품 삭제 = 수량이 남아 있으면 삭제 못하게
# 현재 모든 제품의 수량의 합
# 가격 X 수량을 기준으로 같다 , 크다 , 크거나같다 , 작다 , 작거나같다









