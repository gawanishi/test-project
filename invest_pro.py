import matplotlib.pyplot as plt

# --- ユーザー入力 ---
initial_monthly = int(input("毎月の積立額（円）: "))
total_years = int(input("運用期間（年）: "))

# 2種類の利率を入力してもらう
rate_low_percent = float(input("手堅いシナリオの年利（%）（例: 3）: "))
rate_high_percent = float(input("積極的なシナリオの年利（%）（例: 5）: "))

# --- 設定 ---
monthly_rate_low = (rate_low_percent / 100) / 12
monthly_rate_high = (rate_high_percent / 100) / 12

# 2つの未来を貯めるためのリスト（箱）
years_list = []
amounts_low = []   # 手堅い方の結果用
amounts_high = []  # 積極的な方の結果用

total_low = 0
total_high = 0

# --- シミュレーション開始 ---
for month in range(1, total_years * 12 + 1):
    # 両方のシナリオを同時に計算していく
    total_low = (total_low + initial_monthly) * (1 + monthly_rate_low)
    total_high = (total_high + initial_monthly) * (1 + monthly_rate_high)
    
    if month % 12 == 0:
        year = month // 12
        years_list.append(year)
        amounts_low.append(total_low)
        amounts_high.append(total_high)

# --- 結果発表 ---
print("-" * 50)
print(f"{total_years}年後の差額は 【{total_high - total_low:,.0f}円】 です！")
print("-" * 50)

# --- グラフの作成 ---
plt.figure(figsize=(10, 6))

# 2本の線を引く（labelを変えるのがポイント）
plt.plot(years_list, amounts_low, label=f"Safe ({rate_low_percent}%)", color="blue")
plt.plot(years_list, amounts_high, label=f"Aggressive ({rate_high_percent}%)", color="orange")

plt.title("Comparison of Two Scenarios")
plt.xlabel("Year")
plt.ylabel("Amount (Yen)")
plt.grid(True)
plt.legend() # これでどっちの線が何かを表示する
plt.savefig("comparison_graph.png")
plt.show()