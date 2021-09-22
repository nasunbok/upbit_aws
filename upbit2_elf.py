import pyupbit
import pprint
import time
import datetime

access = ""          # 본인 값으로 변경
secret = ""          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)
balances = upbit.get_balances()
balance = upbit.get_balance("KRW-ELF")


while True:
    now = datetime.datetime.now()
    balance = upbit.get_balance("KRW-ELF")
    xrp_price = upbit.get_avg_buy_price("KRW-ELF")     # KRW-XRP 매수평균가
    xrp_now_price = pyupbit.get_current_price("KRW-ELF") # KRW-XRP 현재가
    print(now, xrp_price, xrp_now_price) #XRP매수가 출력

    if 0 == balance:
        resp = upbit.buy_market_order("KRW-ELF",5500) #시장가 매수
    elif 59==now.minute and 40<= now.second <= 49 and 0.98 <= xrp_now_price/xrp_price <1.03:
        print(now, "-2%~ 3% 사이에서는 5500원 매수")
        resp = upbit.buy_market_order("KRW-ELF",5500) #시장가 매수
    elif 59==now.minute and 40<= now.second <= 49 and 0.96 <= xrp_now_price/xrp_price <0.98:
        print(now, "-4%~ -2% 사이에서는 6000원 매수")
        resp = upbit.buy_market_order("KRW-ELF",6000) #시장가 매수
    elif 59==now.minute and 40<= now.second <= 49 and 0.94 <= xrp_now_price/xrp_price <0.96:
        print(now, "-6%~ -4% 사이에서는 6500원 매수")
        resp = upbit.buy_market_order("KRW-ELF",6500) #시장가 매수
    elif 59==now.minute and 40<= now.second <= 49 and 0.92 <= xrp_now_price/xrp_price <0.94:
        print(now, "-8%~ -6% 사이에서는 7000원 매수")
        resp = upbit.buy_market_order("KRW-ELF",7000) #시장가 매수
    elif 59==now.minute and 40<= now.second <= 49 and 0.9 <= xrp_now_price/xrp_price <0.92:
        print(now, "-10%~ -8% 사이에서는 7500원 매수")
        resp = upbit.buy_market_order("KRW-ELF",7500) #시장가 매수
    elif 59==now.minute and 40<= now.second <= 49 and 0.9 > xrp_now_price/xrp_price:
        print(now, "-10% 이하에서는 10000원 매수")
        resp = upbit.buy_market_order("KRW-ELF",7000) #시장가 매수
    elif 59==now.minute and 40<= now.second <= 49 and 1.03 < xrp_now_price/xrp_price:
        print(now, "60분 종가에서 3% 이상이면 전체 매도")
        resp = upbit.sell_market_order("KRW-ELF",balance) #시장 가 매도
    elif 1.05 < xrp_now_price/xrp_price:
        print(now, "10초씩 모니터링 하다가 5% 이상이며 전체 매도")
        resp = upbit.sell_market_order("KRW-ELF",balance) #시장 가 매도
    time.sleep(10)



