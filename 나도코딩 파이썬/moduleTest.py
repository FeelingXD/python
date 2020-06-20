#import theater_module as mv
'''mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)
'''
#from theater_module import * # import 내용물 전부 가져오기 import 후 가져올 부분만 가져올수잇음

# ex from random import *

from theater_module import price_soldier as price
price(3)  # price_soldier 의 기능이 실행된다
