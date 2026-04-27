profit = 4.5
drawdown = 1.2

if profit > 3:
    print("建议：锁定部分利润")
elif drawdown > 3:
    print("建议：减仓防守")
else:
    print("继续持有")
