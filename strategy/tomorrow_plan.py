market_state = "震荡偏强"

print("明日计划：")

if market_state == "强势":
    print("仓位提高至75%，做强势主线")
elif market_state == "震荡偏强":
    print("仓位维持60%，低吸热点ETF")
else:
    print("仓位降至35%，防守为主")

print("纪律：不追高，不满仓")
