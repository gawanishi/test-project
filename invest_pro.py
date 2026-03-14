# --- ユーザーに入力を求める ---
# input() で打ち込まれた文字を受け取り、int() や float() で数字に変換します
initial_monthly = int(input("最初の毎月の積立額（円）を入力してください: "))
later_monthly = int(input("5年目以降の積立額（円）を入力してください: "))
total_years = int(input("何年間運用しますか？（年）: "))
annual_rate_percent = float(input("期待する年利（%）を入力してください（例: 5）: "))

# --- 計算用のデータに調整 ---
change_year = 5                
annual_rate = annual_rate_percent / 100  # 5% を 0.05 に直す
tax_rate = 0.20315             

# --- 計算準備 ---
total_amount = 0               
total_invested = 0             
monthly_rate = annual_rate / 12 

print(f"\n【年利 {annual_rate_percent}% での資産推移】")
print("-" * 50)

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
        profit = total_amount - total_invested
        print(f"{current_year:2}年目 | 元本: {total_invested:10,.0f}円 | 資産: {total_amount:10,.0f}円")

print("-" * 50)

# --- 税金と最終利益の計算 ---
final_profit = total_amount - total_invested
tax = final_profit * tax_rate
final_amount = total_amount - tax

print(f"最終手取り額（税引き後）: {final_amount:,.0f}円")