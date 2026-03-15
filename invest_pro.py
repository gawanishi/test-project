import matplotlib.pyplot as plt

# --- ユーザー入力 ---
target_amount = int(input("目標金額（円）: "))
initial_monthly = int(input("最初の毎月の積立額（円）: "))
later_monthly = int(input("5年目以降の積立額（円）: "))
total_years = int(input("運用期間（年）: "))
annual_rate_percent = float(input("期待する年利（%）: "))

# ★新しい入力：暴落の設定
crash_year = int(input("暴落が起きる年（例: 10）: "))
crash_rate_percent = float(input("何%暴落させますか？（例: 30）: "))

# --- 設定と準備 ---
change_year = 5
annual_rate = annual_rate_percent / 100
monthly_rate = annual_rate / 12
total_amount = 0
total_invested = 0

years_list = []
amounts_list = []
invested_list = []

# --- シミュレーション開始 ---
for month in range(1, total_years * 12 + 1):
    current_year = (month - 1) // 12 + 1
    
    if current_year <= change_year:
        monthly_deposit = initial_monthly
    else:
        monthly_deposit = later_monthly
    
    total_amount = (total_amount + monthly_deposit) * (1 + monthly_rate)
    total_invested += monthly_deposit

    # ★ここが新しい！：暴落の処理
    # 「指定した年の最後の月（12ヶ月目）」に一度だけ暴落させます
    if current_year == crash_year and month % 12 == 0:
        reduction = total_amount * (crash_rate_percent / 100) # 減る額を計算
        total_amount = total_amount - reduction             # 資産から引く
        print(f"【⚠️警告】{current_year}年目に{crash_rate_percent}%の暴落が発生！")

    if month % 12 == 0:
        years_list.append(current_year)
        amounts_list.append(total_amount)
        invested_list.append(total_invested)

# --- 税金と最終利益の計算 ---
final_profit = total_amount - total_invested
tax = max(0, final_profit * 0.20315) # 利益がマイナスの時は税金0
final_amount = total_amount - tax

# --- 結果発表 ---
difference = target_amount - final_amount
print("-" * 50)
print(f"最終受取額: {final_amount:,.0f}円")
if difference > 0:
    print(f"結果：目標まであと {difference:,.0f}円 足りません。")
else:
    print(f"結果：目標を {-difference:,.0f}円 上回りました！")
print("-" * 50)

# --- グラフの作成 ---

plt.figure(figsize=(10, 6))
plt.plot(years_list, amounts_list, label="Total Assets (with Crash)", marker="o", color="red")
plt.plot(years_list, invested_list, label="Total Invested", linestyle="--", color="blue")
plt.title(f"Crash Simulation at Year {crash_year} (-{crash_rate_percent}%)")
plt.xlabel("Year")
plt.ylabel("Amount (Yen)")
plt.grid(True)
plt.legend()
plt.savefig("investment_crash_graph.png")
plt.show()