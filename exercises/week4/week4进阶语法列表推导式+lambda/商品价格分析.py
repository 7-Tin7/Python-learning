prices = {"苹果": 3.5, "香蕉": 2.0, "西瓜": 15.0, "榴莲": 45.0, "樱桃": 60.0}
discount = [round(p*0.8,2) for p in prices.values()]
expensive = [name for name, p in prices.items() if p >= 30]
cheap = [name for name,p in prices.items() if p < 30]
ranking = sorted(prices.items(),key = lambda x:x[1],reverse = True)
print(discount)
print(expensive)
print(cheap)
print(ranking)