import pyupbit
import pprint
import time
import datetime

access = "LFtnM2WspI7TBJqkTEJg5lhVYd5ZZB48MJf2GeLa"          # 본인 값으로 변경
secret = "LYHByNlrfxyoS6Sd3xxEsZMFJ58UHvB633DhS7vm"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)
balances = upbit.get_balances()
balance = upbit.get_balance("KRW-ELF")



while True:
    now = datetime.datetime.now()
    balance = upbit.get_balance("KRW-ELF")
    # print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 보유 수량 조회
    # print(upbit.get_balance("KRW"))         # 보유 현금 조회
    xrp_price = upbit.get_avg_buy_price("KRW-ELF")     # KRW-XRP 매수평균가
    xrp_now_price = pyupbit.get_current_price("KRW-ELF") # KRW-XRP 현재가
    print(now, xrp_price, xrp_now_price) #XRP매수가 출력
    # print(now, xrp_now_price) #XRP 현재가 출력
    if 0 == balance:
        resp = upbit.buy_market_order("KRW-ELF",5500) #시장가 매수
    elif 59==now.minute and 1<= now.second <= 10 and 0.9 <= xrp_now_price/xrp_price <1.03:
        print(now, "-10%~ 3% 사이에서는 5500원 매수")
        resp = upbit.buy_market_order("KRW-ELF",5500) #시장가 매수
    elif 59==now.minute and 1<= now.second <= 10 and 0.9 > xrp_now_price/xrp_price:
        print(now, "-10% 이하 니까 10000원 매수")
        resp = upbit.buy_market_order("KRW-ELF",10000) #시장가 매수
    elif 59==now.minute and 1<= now.second <= 10 and 1.03 < xrp_now_price/xrp_price:
        print(now, "3% 이상 이니까 전체 매도")
        resp = upbit.sell_market_order("KRW-ELF",balance) #시장 가 매도
    elif 1.05 < xrp_now_price/xrp_price:
        print(now, "5% 이상 이니까 전체 매도")
        resp = upbit.sell_market_order("KRW-ELF",balance) #시장 가 매도
    time.sleep(10)



