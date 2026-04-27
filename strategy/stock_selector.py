stocks = {
    "凯盛科技": 86,
    "西藏珠峰": 82,
    "中国卫通": 79,
    "奥拓电子": 63,
    "吉林化纤": 58
}

rank = sorted(stocks.items(), key=lambda x: x[1], reverse=True)

print("今日个股Top5：")
for i in rank:
    print(i[0], i[1])

print("建议关注前2名")
