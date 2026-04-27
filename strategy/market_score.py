trend = 70
volume = 68
sector = 75
fund = 60

score = (trend + volume + sector + fund) / 4

print("市场综合评分：", score)

if score >= 75:
    print("建议仓位：80%")
elif score >= 60:
    print("建议仓位：60%")
else:
    print("建议仓位：30%")
