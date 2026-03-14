# --- 設定項目 ---
initial_monthly = 30000        # 最初の月額（3万円）
later_monthly = 50000          # 途中で変更する月額（5万円）
change_year = 5                # 何年目に積立額を変えるか
total_years = 20               # 全体の運用期間
annual_rate = 0.05             # 年利（5%）
tax_rate = 0.20315             # 利益にかかる税率（20.315%）

# --- 計算準備 ---
total_amount = 0               # 最終的な資産額
total_invested = 0             # 自分で出した元本の合計
monthly_rate = annual_rate / 12 # 月利に変換

print("【年ごとの資産推移】")
print("-" * 40)

# --- シミュレーション開始 ---
for month in range(1, total_years * 12 + 1):
    current_year = (month - 1) // 12 + 1
    
    if current_year <= change_year:
        monthly_deposit = initial_monthly
    else:
        monthly_deposit = later_monthly
    
    total_amount = (total_amount + monthly_deposit) * (1 + monthly_rate)
    total_invested += monthly_deposit

    # ★ここが新しい部分！：12ヶ月（1年）ごとに画面に表示する
    if month % 12 == 0:
        profit = total_amount - total_invested
        print(f"{current_year:2}年目 | 元本: {total_invested:9,.0f}円 | 資産: {total_amount:9,.0f}円 | 利益: {profit:9,.0f}円")

print("-" * 40)

# --- 税金と最終利益の計算 ---
final_profit = total_amount - total_invested
tax = final_profit * tax_rate
final_amount = total_amount - tax

print(f"\n【最終結果】")
print(f"税引き前資産: {total_amount:,.0f}円")
print(f"引かれる税金: {tax:,.0f}円")
print(f"最終手取り額: {final_amount:,.0f}円")