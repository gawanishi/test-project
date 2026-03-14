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

# --- シミュレーション開始 ---
for month in range(1, total_years * 12 + 1):
    # 現在が何年目かを計算
    current_year = (month - 1) // 12 + 1
    
    # 積立額の判定（change_yearを境に金額を変える）
    if current_year <= change_year:
        monthly_deposit = initial_monthly
    else:
        monthly_deposit = later_monthly
    
    # 資産額の計算：(今の資産 + 今月の積立) × 利息
    total_amount = (total_amount + monthly_deposit) * (1 + monthly_rate)
    total_invested += monthly_deposit

# --- 税金と最終利益の計算 ---
profit = total_amount - total_invested # 利益
tax = profit * tax_rate                 # 税金
final_amount = total_amount - tax       # 税引き後の手残り

# --- 結果発表 ---
print(f"【{total_years}年後のシミュレーション結果】")
print(f"投資元本: {total_invested:,.0f}円")
print(f"税引き前資産: {total_amount:,.0f}円")
print(f"税金（{tax_rate*100:.3f}%）: {tax:,.0f}円")
print(f"最終受取額: {final_amount:,.0f}円")