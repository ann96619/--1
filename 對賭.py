import random
import colorama
from colorama import Fore

# 初始化 colorama
colorama.init(autoreset=True)

# 初始資金
initial_balance = 100000000  # 1 億
balance = initial_balance  # 當前資金

# 更新後的賠率和機率對應
odds = {
    "1/2": {"probability": 0.5, "multiplier": 1.85},
    "2/3": {"probability": 2/3, "multiplier": 1.32},
    "3/4": {"probability": 3/4, "multiplier": 1.2},
    "1/3": {"probability": 1/3, "multiplier": 2.75},
    "1/9": {"probability": 1/9, "multiplier": 8.8},
    "4/5": {"probability": 4/5, "multiplier": 1.15},
    "3/5": {"probability": 3/5, "multiplier": 1.55},
}


# 顯示歡迎界面
def show_welcome():
    print(Fore.GREEN + "\n歡迎來到對賭程式！")
    print(Fore.YELLOW + f"當前資金: {balance} 元")
    print(Fore.CYAN + "可選擇的賠率和機率:")
    for rate, details in odds.items():
        print(Fore.YELLOW + f"{rate}: 機率 {details['probability'] * 100}% 賠率 {details['multiplier']}")
    print(Fore.CYAN + "\n請選擇一個賠率來進行下注，這個選擇將適用於所有後續的賭局。")


# 設置初始賠率
def set_initial_odds():
    print(Fore.CYAN + "請選擇您想要的賠率：")
    for rate in odds:
        print(Fore.YELLOW + rate)
    chosen_odds = input(Fore.GREEN + "請輸入賠率（例如 '1/2'）：").strip()

    if chosen_odds in odds:
        print(Fore.GREEN + f"您選擇了賠率 {chosen_odds}")
        return chosen_odds
    else:
        print(Fore.RED + "無效的選擇，請重新選擇。")
        return set_initial_odds()


# 進行賭局
def make_bet(chosen_odds):
    global balance
    print(Fore.CYAN + "\n選擇您要參加的賭局")
    bet_amount = float(input(Fore.GREEN + f"請輸入賭注金額（剩餘資金 {balance} 元）: "))

    # 檢查賭注金額是否合法
    if bet_amount <= 0 or bet_amount > balance:
        print(Fore.RED + "賭注金額無效，請確保您的賭注金額大於 0 且不超過剩餘資金。")
        return

    # 確定賠率和機率
    prob = odds[chosen_odds]["probability"]
    multiplier = odds[chosen_odds]["multiplier"]

    # 隨機決定是否中獎
    outcome = random.random()  # 隨機生成 0 到 1 之間的浮動數
    print(Fore.CYAN + f"隨機結果: {outcome:.4f}")

    if outcome <= prob:  # 如果隨機結果小於等於選擇的機率，表示中獎
        win_amount = bet_amount * multiplier
        balance += win_amount - bet_amount  # 贏得賠率後獲得的金額，扣除原賭注
        print(
            Fore.GREEN + f"白羊毛噴出！您中獎了！您獲得了 {win_amount - bet_amount:.2f} 元，當前資金為 {Fore.WHITE}{balance:.2f} 元。")
    else:  # 否則為黑羊毛
        balance -= bet_amount  # 輸掉賭注
        print(
            Fore.RED + f"黑羊毛噴出！很遺憾，您沒中獎。您失去了 {Fore.WHITE}{bet_amount:.2f} 元，當前資金為 {Fore.WHITE}{balance:.2f} 元。")


# 退出程序
def exit_program():
    print(Fore.GREEN + f"您最終的資金為 {Fore.WHITE}{balance:.2f} 元。感謝遊玩！")
    exit()


# 主程式循環
def main():
    global balance
    show_welcome()

    # 用戶選擇一個賠率
    chosen_odds = set_initial_odds()

    # 無限循環賭局
    while True:
        make_bet(chosen_odds)


# 程式入口
if __name__ == "__main__":
    main()
