etfs = {
    "芯片ETF": 88,
    "电网设备ETF": 82,
    "中证500ETF": 79,
    "黄金ETF": 65,
    "证券ETF": 61
}

sorted_etf = sorted(etfs.items(), key=lambda x: x[1], reverse=True)

print("今日ETF强度排名：")
for i in sorted_etf:
    print(i[0], i[1])

print("建议持仓：前2名")
