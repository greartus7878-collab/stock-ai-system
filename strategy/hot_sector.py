sectors = {
    "芯片": 92,
    "电力": 85,
    "军工": 79,
    "证券": 72,
    "黄金": 66
}

rank = sorted(sectors.items(), key=lambda x:x[1], reverse=True)

print("今日热点板块：")
for i in rank:
    print(i[0], i[1])
