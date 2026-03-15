import matplotlib.pyplot as plt

# --- ユーザー入力 ---
initial_monthly = int(input("毎月の積立額（円）: "))
total_years = int(input("運用期間（年）: "))
rate_low_percent = float(input("手堅い年利（%）: "))
rate_high_percent = float(input("積極的な年利（%）: "))

# --- 設定と計算 ---
monthly_rate_low = (rate_low_percent / 100) / 12
monthly_rate_high = (rate_high_percent / 100) / 12
total_low = 0
total_high = 0

years_list = []
amounts_low = []
amounts_high = []

for month in range(1, total_years * 12 + 1):
    total_low = (total_low + initial_monthly) * (1 + monthly_rate_low)
    total_high = (total_high + initial_monthly) * (1 + monthly_rate_high)
    
    if month % 12 == 0:
        years_list.append(month // 12)
        amounts_low.append(total_low)
        amounts_high.append(total_high)

# ★ここが今回の主役！：結果をテキストファイルに書き出す
# 'w' は Write（書き込み）の意味です
with open("invest_result.txt", "w", encoding="utf-8") as f:
    f.write("【積立投資シミュレーション結果報告書】\n")
    f.write("-" * 40 + "\n")
    f.write(f"運用期間: {total_years}年\n")
    f.write(f"毎月の積立額: {initial_monthly:,}円\n\n")
    f.write(f"シナリオ1（{rate_low_percent}%）の結果: {total_low:,.0f}円\n")
    f.write(f"シナリオ2（{rate_high_percent}%）の結果: {total_high:,.0f}円\n")
    f.write(f"その差額: {total_high - total_low:,.0f}円\n")
    f.write("-" * 40 + "\n")
    f.write("この結果を元に、投資計画を検討しましょう。")

print("\n>>> 計算結果を 'invest_result.txt' に保存しました！")

# --- グラフの作成 ---
plt.figure(figsize=(10, 6))
plt.plot(years_list, amounts_low, label=f"Safe ({rate_low_percent}%)")
plt.plot(years_list, amounts_high, label=f"Aggressive ({rate_high_percent}%)")
plt.legend()
plt.savefig("comparison_graph.png")
plt.show()