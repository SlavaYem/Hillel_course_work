from utils import live_course, my_account_balance, buy_usd, sell_usd, \
    buy_all_usd, sell_all_usd, restart_game, course_change
from argparse import ArgumentParser

if __name__ == "__main__":
    test_1 = ArgumentParser()
    test_1.add_argument("param_1", type=str, nargs='?')
    test_1.add_argument("pr_2", type=str, nargs='?')
    test_1 = vars(test_1.parse_args())
    if test_1['param_1'] == "RATE":
        live_course()
    elif test_1['param_1'] == "AVALIABLE":
        my_account_balance()
    elif test_1['param_1'] == "BUY":
        if test_1['pr_2'] == "ALL":
            buy_all_usd()
        else:
            buy_usd(int(test_1['pr_2']))
    elif test_1['param_1'] == "SELL":
        if test_1['pr_2'] == "ALL":
            sell_all_usd()
        else:
            sell_usd(int(test_1['pr_2']))
    elif test_1['param_1'] == "NEXT":
        course_change()
    elif test_1['param_1'] == "RESTART":
        restart_game()
