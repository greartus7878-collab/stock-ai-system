import pandas as pd

# 模拟真实ETF池（第二阶段先稳定运行）
data = {
    "ETF": ["芯片ETF", "中证500ETF", "电力ETF", "黄金ETF", "证券ETF"],
    "涨幅": [2.6, 1.9, 1.4, 0.5, -0.3]
}

df = pd.DataFrame(data)
df = df.sort_values("涨幅", ascending=False)

print("今日ETF强度排名：")
print(df)

print("建议持仓：前2名ETF")
