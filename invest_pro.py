import matplotlib.pyplot as plt  # グラフを描くための道具を読み込む

# --- ユーザー入力 ---
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

# ★グラフ用のデータを貯める「リスト（箱）」を準備
years_list = []      # 何年目か
amounts_list = []    # その時の資産額
invested_list = []   # その時の元本合計

# --- シミュレーション開始 ---
for month in range(1, total_years * 12 + 1):
    current_year = (month - 1) // 12 + 1
    
    if current_year <= change_year:
        monthly_deposit = initial_monthly
    else:
        monthly_deposit = later_monthly
    
    total_amount = (total_amount + monthly_deposit) * (1 + monthly_rate)
    total_invested += monthly_deposit

    # 1年（12ヶ月）ごとにデータをリストに追加する
    if month % 12 == 0:
        years_list.append(current_year)     # 年数を貯める
        amounts_list.append(total_amount)   # 資産を貯める
        invested_list.append(total_invested) # 元本を貯める

# --- グラフの作成 ---
plt.figure(figsize=(10, 6)) # グラフのサイズを設定

# 2本の線を引く（資産と元本）
plt.plot(years_list, amounts_list, label="Total Assets", marker="o") 
plt.plot(years_list, invested_list, label="Total Invested", linestyle="--")

# グラフのラベルやタイトル
plt.title(f"Investment Simulation ({annual_rate_percent}% Annual Rate)")
plt.xlabel("Year")
plt.ylabel("Amount (Yen)")
plt.grid(True)     # 網掛けを表示
plt.legend()      # 凡例（ラベルの説明）を表示

# グラフを「investment_graph.png」という名前の画像として保存
plt.savefig("investment_graph.png")
print("\nグラフを 'investment_graph.png' として保存しました！")

# 画面にグラフを表示する（VS Codeの設定によっては別ウィンドウが開きます）
plt.show()