from P_visuals import *


def SB_and_BB(T, OOAP, MI, game, is_SB_or_BB):
    if is_SB_or_BB == "SB":
        factor = 1
    elif is_SB_or_BB == "BB":
        factor = 2

    if game // 5 == 0:
        k = factor
    else:
        k = (game // 5) * 2 * factor

    for i in OOAP.GFM_name_and_coins:
        i.undraw()
    for i in OOAP.GFM_bid:
        i.undraw()

    if OOAP.coins > k:
        OOAP.bid += k
        OOAP.coins -= k
        OOAP.last_diff = k
        OOAP.GFM_name_and_coins = name_and_coins(T, OOAP)
        OOAP.GFM_bid = bid(T, OOAP)
        action_text(T, OOAP, "{} is {} with {}. ".format(OOAP.name, is_SB_or_BB, k))
    else:
        OOAP.bid += OOAP.coins
        OOAP.last_diff = OOAP.coins
        OOAP.coins = 0      
        MI.did_someone_all_in = "yes"
        OOAP.GFM_name_and_coins = name_and_coins(T, OOAP)
        OOAP.GFM_bid = bid(T, OOAP)
        action_text(T, OOAP, "{} allined. ".format(OOAP.name))


def BB_diff(game):
    if game // 5 == 0:
        BB = 2
    else:
        BB = (game // 5) * 4

    return BB
