import random


def decide(OOPP, num_of_turned_cards, MI):
    param_a = 1.2 - num_of_turned_cards / 10
    param_b = OOPP.comb_and_score[1] / 30
    dec = round(param_a * param_b, 2)

    if dec <= 0.6:
        if OOPP.personality == "risker" or "bluffer":
            dec += 0.15
    if dec > 0.6:
        if OOPP.personality == "cautioner" or "bluffer":
            dec -= 0.15

    try:
        if OOPP.coins / (MI.diff - OOPP.last_diff) <= 3:
            dec -= 0.1
    except:
        pass

    if num_of_turned_cards <= 3:
        if OOPP.personality == "rusher":
            dec += 0.15
        elif OOPP.personality == "waiter":
            dec -= 0.15
        elif OOPP.personality == "bluffer":
            dec += random.choice([-0.15, 0.15])
    if num_of_turned_cards > 3:
        if OOPP.personality == "rusher":
            dec -= 0.15
        elif OOPP.personality == "waiter":
            dec += 0.15
        elif OOPP.personality == "bluffer":
            dec += random.choice([-0.15, 0.15])

    OOPP.decisiveness = dec
