import akshare as ak
import pandas as pd

# 示例ETF代码（可继续扩展）
pool = {
    "芯片ETF": "159995",
    "中证500ETF": "510500",
    "黄金ETF": "518880",
    "证券ETF": "512880",
    "电力ETF": "561560"
}

rows = []

for name, code in pool.items():
    try:
        df = ak.fund_etf_hist_em(symbol=code, period="daily", adjust="")
        latest = df.iloc[-1]
        prev = df.iloc[-2]
        pct = round((latest["收盘"] - prev["收盘"]) / prev["收盘"] * 100, 2)
        rows.append([name, code, pct])
    except:
        pass

rank = pd.DataFrame(rows, columns=["名称", "代码", "日涨幅"])
rank = rank.sort_values("日涨幅", ascending=False)

print("今日ETF排名：")
print(rank)

print("建议持仓：前2名")
