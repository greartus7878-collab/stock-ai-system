stocks = {
    "凯盛科技": 78,
    "西藏珠峰": 73,
    "奥拓电子": 55,
    "吉林化纤": 49
}

rank = sorted(stocks.items(), key=lambda x:x[1], reverse=True)

print("个股优先级：")
for i in rank:
    print(i[0], i[1])
