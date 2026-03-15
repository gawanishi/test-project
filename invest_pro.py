import matplotlib.pyplot as plt

# --- ユーザー入力 (ここに追加) ---
target_amount = int(input("目標金額を入力してください（円）: ")) # 新しい変数！
initial_monthly = int(input("最初の毎月の積立額（円）: "))
later_monthly = int(input("5年目以降の積立額（円）: "))
total_years = int(input("運用期間（年）: "))
annual_rate_percent = float(input("期待する年利（%）: "))

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

    if month % 12 == 0:
        years_list.append(current_year)
        amounts_list.append(total_amount)
        invested_list.append(total_invested)

# --- 税金と最終利益の計算 ---
final_profit = total_amount - total_invested
tax = final_profit * 0.20315
final_amount = total_amount - tax

# --- 目標との比較計算 (ここが新しい！) ---
difference = target_amount - final_amount # 引き算で差額を出す

# --- 結果発表 ---
print("-" * 50)
print(f"最終受取額: {final_amount:,.0f}円")
print(f"目標金額  : {target_amount:,.0f}円")

if difference > 0:
    # 目標に届かなかった場合
    print(f"結果：目標まであと 【{difference:,.0f}円】 足りませんでした。")
    print("積立額を増やすか、運用期間を延ばしてみましょう！")
else:
    # 目標を達成した場合（差額が0かマイナス）
    print(f"結果：おめでとうございます！目標を 【{-difference:,.0f}円】 上回りました！")
    print("素晴らしい計画ですね！")
print("-" * 50)

# (グラフ作成コードはそのまま続く...)