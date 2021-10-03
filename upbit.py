import pyupbit
import pprint
import time
import datetime

access = "LFtnM2WspI7TBJqkTEJg5lhVYd5ZZB48MJf2GeLa"          # 본인 값으로 변경
secret = "LYHByNlrfxyoS6Sd3xxEsZMFJ58UHvB633DhS7vm"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)
balances = upbit.get_balances()
balance = upbit.get_balance("KRW-XRP")



while True:
    now = datetime.datetime.now()
    balance = upbit.get_balance("KRW-XRP")
    # print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 보유 수량 조회
    # print(upbit.get_balance("KRW"))         # 보유 현금 조회
    xrp_price = upbit.get_avg_buy_price("KRW-XRP")     # KRW-XRP 매수평균가
    xrp_now_price = pyupbit.get_current_price("KRW-XRP") # KRW-XRP 현재가
    print(now, xrp_price, xrp_now_price) #XRP매수가 출력
    # print(now, xrp_now_price) #XRP 현재가 출력
    if 0 == balance:
        resp = upbit.buy_market_order("KRW-XRP",5500) #시장가 매수
    elif 59==now.minute and 1<= now.second <= 10 and 0.95 <= xrp_now_price/xrp_price <1.02:
        print(now, "-10%~ 3% 사이에서는 5500원 매수")
        resp = upbit.buy_market_order("KRW-XRP",5500) #시장가 매수
    elif 59==now.minute and 1<= now.second <= 10 and 0.95 > xrp_now_price/xrp_price:
        print(now, "-10% 이하 니까 10000원 매수")
        resp = upbit.buy_market_order("KRW-XRP",10000) #시장가 매수
    elif 59==now.minute and 1<= now.second <= 10 and 1.02 < xrp_now_price/xrp_price:
        print(now, "3% 이상 이니까 전체 매도")
        resp = upbit.sell_market_order("KRW-XRP",balance) #시장 가 매도
    elif 1.03 < xrp_now_price/xrp_price:
        print(now, "5% 이상 이니까 전체 매도")
        resp = upbit.sell_market_order("KRW-XRP",balance) #시장 가 매도
    time.sleep(9)



# resp = upbit.buy_market_order("KRW-XRP",5500) #시장가 매수
# resp = upbit.sell_market_order("KRW-XRP",balance) #시장 가 매도




# 매수 조건
# 1번 조건 : 60분 조회시 마다 이익이 2%이상이면 전체 매도
# 2번 조건 : 2% 미만 -10% 이상이면 5500 시장가로 구매




# print(pyupbit.get_current_price("KRW-XRP")) # XRP 현재 가격



# 매수 조건
# 60분 조회시 마다 이익이 3%이상이면 전체 매도
# 




# print(pyupbit.get_current_price("KRW-XRP")) # XRP 현재 가격
# print(upbit.get_balances([1]))
# print(upbit.avg_buy_price("KRW-XRP"))   # 매수 평균값 조회 방법??

#주문
# upbit = pyupbit.Upbit(access, secret)
# ret = upbit.buy_limit_order("KRW-XRP", 1000, 10) xrp 지정가 1000원으로 10개 구매
# print(ret)

# coinlist = ["KRW-XRP"]

# while(True): 
#     for i in range(len(coinlist)): 
#         data = pyupbit.get_ohlcv(ticker=coinlist[i], interval="minute3") 
#         now_rsi = rsi(data, 14).iloc[-1] 
#         print("코인명: ", coinlist[i]) 
#         print("현재시간: ", datetime.datetime.now()) 
#         print("RSI :", now_rsi) 
#         print() 
#         time.sleep(0.5)