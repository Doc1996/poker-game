import random
from P_visuals import *


def action(T, OOAP, PP, MI):

    def checking(T, OOAP):
        for i in OOAP.GFM_name_and_coins:
            i.undraw()
        for i in OOAP.GFM_bid:
            i.undraw()

        OOAP.did_move = "AM"
        OOAP.GFM_name_and_coins = name_and_coins(T, OOAP)
        OOAP.GFM_bid = bid(T, OOAP)
        action_text(T, OOAP, "{} checked. ".format(OOAP.name))


    def calling(T, OOAP, MI):
        OOAP.bid += MI.diff - OOAP.last_diff
        OOAP.coins -= MI.diff - OOAP.last_diff
        OOAP.last_diff = MI.diff
        MI.diff_remembered_for_raising = MI.diff
        OOAP.did_move = "AM"


    def all_in(T, OOAP, MI):
        for i in OOAP.GFM_name_and_coins:
            i.undraw()
        for i in OOAP.GFM_bid:
            i.undraw()

        OOAP.bid += OOAP.coins
        OOAP.last_diff = OOAP.coins
        OOAP.coins = 0
        MI.did_someone_all_in = "yes"
        OOAP.did_move = "AM"
        OOAP.GFM_name_and_coins = name_and_coins(T, OOAP)
        OOAP.GFM_bid = bid(T, OOAP)
        action_text(T, OOAP, "{} allined. ".format(OOAP.name))


    def raising(T, OOAP, PP, MI, function_calling):
        for i in OOAP.GFM_name_and_coins:
            i.undraw()
        for i in OOAP.GFM_bid:
            i.undraw()

        min_or_max = ""
        bet_or_raise = MI.diff

        if OOAP.coins <= MI.min_raise:
            raise_for = OOAP.coins
            min_or_max = "min"
        else:
            if OOAP not in PP:
                if MI.min_raise <= OOAP.coins: 
                    if bet_or_raise == 0:
                        raise_for = raising_text_and_entry(T, OOAP, "How much you want to bet? The minimum is {}, and the maximum {}. "\
                            .format(MI.min_raise, OOAP.coins), MI.min_raise, OOAP.coins)
                    else:
                        raise_for = raising_text_and_entry(T, OOAP, "For how much you want to raise? The minimum is {}, and the maximum {}. ".\
                            format(MI.min_raise, OOAP.coins), MI.min_raise, OOAP.coins)
                    if raise_for < MI.min_raise:
                        raise_for = MI.min_raise
                    if raise_for >= OOAP.coins:
                        raise_for = OOAP.coins
                        min_or_max = "max"
            else:
                if OOAP.decisiveness <0.85:
                    raise_for = MI.min_raise
                else:
                    raise_for = round(MI.min_raise * random.choice([2, 2.25, 2.5]))
                    if raise_for >= OOAP.coins:
                        raise_for = OOAP.coins
                        min_or_max = "max"

        function_calling
        MI.diff = MI.diff_remembered_for_raising + raise_for
        OOAP.bid += raise_for
        OOAP.coins -= raise_for
        OOAP.last_diff = MI.diff
        OOAP.did_move = "AM"
        OOAP.GFM_name_and_coins = name_and_coins(T, OOAP)
        OOAP.GFM_bid = bid(T, OOAP)

        if OOAP.coins == (0 or 0.0) and min_or_max == "min":
            if bet_or_raise == 0:
                action_text(T, OOAP, "{} allined because the minimum amount for betting was {}. ".format(OOAP.name, MI.min_raise))
            else:
                action_text(T, OOAP, "{} allined because the minimum amount for raising was {}. ".format(OOAP.name, MI.min_raise))
            MI.did_someone_all_in = "yes"
        elif OOAP.coins == (0 or 0.0) and min_or_max == "max":
            if bet_or_raise == 0:
                action_text(T, OOAP, "{} allined because the maximum amount for betting was {}. ".format(OOAP.name, raise_for))
            else:
                action_text(T, OOAP, "{} allined because the maximum amount for raising was {}. ".format(OOAP.name, raise_for))
            MI.did_someone_all_in = "yes"
        else:
            if bet_or_raise == 0:
                action_text(T, OOAP, "{} bet {}. ".format(OOAP.name, raise_for))
            else:
                action_text(T, OOAP, "{} raised for {}. ".format(OOAP.name, raise_for))

        MI.min_raise = 2 * raise_for


    def folding(T, OOAP):
        for i in OOAP.GFM_name_and_coins:
            i.undraw()
        for i in OOAP.GFM_bid:
            i.undraw()
        for i in OOAP.GFM_hole:
            i.undraw()

        OOAP.in_game = "out"
        OOAP.last_diff = MI.diff
        OOAP.did_move = "AM"
        OOAP.GFM_name_and_coins = name_and_coins(T, OOAP)
        OOAP.GFM_bid = bid(T, OOAP)
        action_text(T, OOAP, "{} folded. ".format(OOAP.name))


    if OOAP.did_move == "AM":
        if OOAP.coins > MI.diff - OOAP.last_diff:
            if MI.diff - OOAP.last_diff == 0 or 0.0:
                if OOAP not in PP:
                    act = action_button(T, "fold", "check", "-")
                    if act == "fold":
                        folding(T, OOAP)
                    elif act == "check":
                        checking(T, OOAP)
                else:
                    checking(T, OOAP)
            else:
                if OOAP not in PP:
                    act = action_button(T, "fold", "call", "-")
                    if act == "fold":
                        folding(T, OOAP)
                    elif act == "call":
                        for i in OOAP.GFM_name_and_coins:
                            i.undraw()
                        for i in OOAP.GFM_bid:
                            i.undraw()
                        calling(T, OOAP, MI)
                        OOAP.GFM_name_and_coins = name_and_coins(T, OOAP)
                        OOAP.GFM_bid = bid(T, OOAP)
                        action_text(T, OOAP, "{} called. ".format(OOAP.name))
                else:
                    if OOAP.decisiveness <= 0.55:
                        folding(T, OOAP)
                    else:
                        for i in OOAP.GFM_name_and_coins:
                            i.undraw()
                        for i in OOAP.GFM_bid:
                            i.undraw()
                        calling(T, OOAP, MI)
                        OOAP.GFM_name_and_coins = name_and_coins(T, OOAP)
                        OOAP.GFM_bid = bid(T, OOAP)
                        action_text(T, OOAP, "{} called. ".format(OOAP.name))
        else:
            if MI.diff - OOAP.last_diff == 0 or 0.0:
                if OOAP not in PP:
                    act = action_button(T, "fold", "check", "-")
                    if act == "fold":
                        folding(T, OOAP)
                    elif act == "check":
                        checking(T, OOAP)
                else:
                    checking(T, OOAP)
            else:
                if OOAP not in PP:
                    act = action_button(T, "fold", "all in", "-")
                    if act == "fold":
                        folding(T, OOAP)
                    elif act == "all in":
                        all_in(T, OOAP, MI)
                else:
                    if OOAP.decisiveness <= 0.55:
                        folding(T, OOAP)
                    else:
                        all_in(T, OOAP, MI)

    else:
        if OOAP.coins > MI.diff - OOAP.last_diff:
            if MI.diff - OOAP.last_diff == 0 or 0.0:
                if OOAP not in PP:
                    if MI.diff == 0:
                        act = action_button(T, "fold", "check", "bet")
                    else:
                        act = action_button(T, "fold", "check", "raise")
                    if act == "fold":
                        folding(T, OOAP)
                    elif act == "check":
                        checking(T, OOAP)
                    elif act == "bet" or "raise":
                        raising(T, OOAP, PP, MI, calling(T, OOAP, MI))
                else:
                    if OOAP.decisiveness <= 0.7:
                        checking(T, OOAP)
                    else:
                        raising(T, OOAP, PP, MI, calling(T, OOAP, MI))
            else:
                if OOAP not in PP:
                    if MI.diff == 0:
                        act = action_button(T, "fold", "call", "bet")
                    else:
                        act = action_button(T, "fold", "call", "raise")
                    if act == "fold":
                        folding(T, OOAP)
                    elif act == "call":
                        for i in OOAP.GFM_name_and_coins:
                            i.undraw()
                        for i in OOAP.GFM_bid:
                            i.undraw()
                        calling(T, OOAP, MI)
                        OOAP.GFM_name_and_coins = name_and_coins(T, OOAP)
                        OOAP.GFM_bid = bid(T, OOAP)
                        action_text(T, OOAP, "{} called. ".format(OOAP.name))
                    elif act == "bet" or "raise":
                        raising(T, OOAP, PP, MI, calling(T, OOAP, MI))
                else:
                    if OOAP.decisiveness <= 0.4:
                        folding(T, OOAP)
                    elif OOAP.decisiveness <= 0.7:
                        for i in OOAP.GFM_name_and_coins:
                            i.undraw()
                        for i in OOAP.GFM_bid:
                            i.undraw()
                        calling(T, OOAP, MI)
                        OOAP.GFM_name_and_coins = name_and_coins(T, OOAP)
                        OOAP.GFM_bid = bid(T, OOAP)
                        action_text(T, OOAP, "{} called. ".format(OOAP.name))
                    else:
                        raising(T, OOAP, PP, MI, calling(T, OOAP, MI))
        else:
            if MI.diff - OOAP.last_diff == 0:
                if OOAP not in PP:
                    act = action_button(T, "fold", "check", "-")
                    if act == "fold":
                        folding(T, OOAP)
                    elif act == "check":
                        checking(T, OOAP)
                else:
                    checking(T, OOAP)
            else:
                if OOAP not in PP:
                    act = action_button(T, "fold", "all in", "-")
                    if act == "fold":
                        folding(T, OOAP)
                    elif act == "all in":
                        all_in(T, OOAP, MI)
                else:
                    if OOAP.decisiveness <= 0.55:
                        folding(T, OOAP)
                    else:
                        all_in(T, OOAP, MI)