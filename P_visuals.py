from math import *
from time import *
from graphics import *


def window():
    TW = 1366; TH = 697
    T = GraphWin("Poker Game", TW, TH)
    T.setCoords(0, 0, TW, TH)
    T_firework = Image(Point(TW/2, TH/2), "firework.png")
    T_firework.draw(T)
    T_text_A = Text(Point(TW/2, TH/2), "POKER"); T_text_A.setTextColor("red"); T_text_A.setSize(30)
    T_text_B = Text(Point(TW/2, TH/2), "POKER"); T_text_B.setTextColor("yellow"); T_text_B.setSize(30)

    for i in range(0, 5):
        T_text_A.draw(T); sleep(0.2); T_text_A.undraw()
        T_text_B.draw(T); sleep(0.2); T_text_B.undraw()

    T_firework.undraw()
    T.setBackground("green")  
    T_oval = Oval(Point(TW/4, TH/4), Point(3/4*TW, 3/4*TH)); T_oval.setOutline("white"); T_oval.setWidth(4)
    T_oval.draw(T)

    return T


def start_name(T):
    TW = 1366; TH = 697; a = 2/3*TW / 2; b = 2/3*TH / 2
    name_of_you = ""

    while name_of_you == "":
        you_text = Text(Point(TW/2-a*3/5, TH/2-186), "What is your name? ")
        you_text.draw(T)
        you_entry = Entry(Point(TW/2-a*3/5, TH/2-186-25), 12)
        you_entry.draw(T)
        T.getMouse()
        name_of_you = you_entry.getText()
        you_text.undraw()
        you_entry.undraw()

    return name_of_you


def start_n(T):
    TW = 1366; TH = 697; a = 2/3*TW / 2; b = 2/3*TH / 2
    n = ""

    while n == "" or n < 1 or n > 7:
        num_text = Text(Point(TW/2-a*3/5, TH/2-186), "Enter the number of players you want to play with (from 1 to 7): ")
        num_text.draw(T)
        num_entry = Entry(Point(TW/2-a*3/5, TH/2-186-25), 12)
        num_entry.draw(T)
        T.getMouse()
        n = int(num_entry.getText())
        num_text.undraw()
        num_entry.undraw()

    return n


def individual_pos(OOAP, i):
    TW = 1366; TH = 697; a = 2/3*TW / 2; b = 2/3*TH / 2; CW = 60; CH = CW * 1.5
    COH_pos = [[TW/2-a*3/5, TH/2-186], [TW/2-a+55, TH/2-0], [TW/2-a*3/5, TH/2+186], [TW/2-0, TH/2+b+5],
               [TW/2+a*3/5, TH/2+186], [TW/2+a-55, TH/2-0], [TW/2+a*3/5, TH/2-186], [TW/2-0, TH/2-b-5]]
    name_and_coins_pos = [[COH_pos[j][0], COH_pos[j][1]+3/4*CH] for j in range(0, len(COH_pos))]
    hole_A_pos = [[COH_pos[j][0]-CW/3, COH_pos[j][1]] for j in range(0, len(COH_pos))]
    hole_B_pos = [[COH_pos[j][0]+CW/3, COH_pos[j][1]] for j in range(0, len(COH_pos))]
    bid_pos = [[COH_pos[j][0], COH_pos[j][1]-5/6*CH] for j in range(0, len(COH_pos))]
    action_pos = [[COH_pos[j][0]-2*CW, COH_pos[j][1]] for j in range(0, len(COH_pos))]
    token_pos = [[COH_pos[i][0]+4/3*CW, COH_pos[j][1]-CH/4] for j in range(0, len(COH_pos))]

    OOAP.name_and_coins_pos = name_and_coins_pos[i]
    OOAP.hole_A_pos = hole_A_pos[i]
    OOAP.hole_B_pos = hole_B_pos[i]
    OOAP.bid_pos = bid_pos[i]
    OOAP.action_pos = action_pos[i]
    OOAP.token_pos = token_pos[i]


def shared_pos(Player):
    TW = 1366; TH = 697; CW = 60; CH = CW * 1.5
    Player.comm_pos = [[TW/2+i-CW, TH/2] for i in [-8/3*CW, -4/3*CW, 0, 4/3*CW, 8/3*CW]]
    Player.deck_pos = [TW/2+8/3*CW+CW, TH/2]
    Player.pot_pos = [TW/2, TH/2-7/6*CH]


def name_and_coins(T, OOAP):
    name_and_coins_text = Text(Point(OOAP.name_and_coins_pos[0], OOAP.name_and_coins_pos[1]), "{} [{}]".format(OOAP.name, OOAP.coins)); \
        name_and_coins_text.setTextColor("black"); name_and_coins_text.setStyle("normal"); name_and_coins_text.setSize(12)
    name_and_coins_text.draw(T)
    GFM_name_and_coins = [name_and_coins_text]

    return GFM_name_and_coins


def token(T, OOAP):
    TR = 10
    token_circ = Circle(Point(OOAP.token_pos[0], OOAP.token_pos[1]), TR); token_circ.setFill("yellow")
    token_circ.draw(T)
    token_text = Text(Point(OOAP.token_pos[0], OOAP.token_pos[1]), "D"); token_text.setSize(9)
    token_text.draw(T)
    GFM_token = [token_circ, token_text]

    return GFM_token


def card(T, pos, card, op_or_cl):
    CW = 60; CH = CW * 1.5
    card_rect = Rectangle(Point(pos[0]-CW/2, pos[1]-CH/2), Point(pos[0]+CW/2, pos[1]+CH/2))
    card_oval = Oval(Point(pos[0]-1/3*CW, pos[1]-1/3*CH), Point(pos[0]+1/3*CW, pos[1]+1/3*CH))

    if op_or_cl == "opened":
        card_rect.setFill("white")
        card_rect.setOutline("brown")
    elif op_or_cl == "closed":
        card_rect.setFill("brown")
        card_rect.setOutline("white")

    card_rect.draw(T)

    if op_or_cl == "opened":
        card_text_border_A = Text(Point(pos[0]-5/12*CW+2, pos[1]+5/12*CH-3), card[0]); card_text_border_A.setStyle("bold"); \
            card_text_border_A.setSize(9)
        card_text_border_B = Text(Point(pos[0]+5/12*CW-2, pos[1]-5/12*CH+3), card[0]); card_text_border_B.setStyle("bold"); \
            card_text_border_B.setSize(9)
        card_text_center = Text(Point(pos[0], pos[1]), card[1]); card_text_center.setStyle("bold"); card_text_center.setSize(18)
        if card[1] == '♥':
            card_text_border_A.setTextColor("red"); card_text_border_B.setTextColor("red"); card_text_center.setTextColor("red")
            card_text_border_A.draw(T); card_text_border_B.draw(T); card_text_center.draw(T)
            GFM_card = [card_rect, card_oval, card_text_border_A, card_text_border_B, card_text_center]
        elif card[1] == '♦':
            card_text_border_A.setTextColor("red"); card_text_border_B.setTextColor("red"); card_text_center.setTextColor("red")
            card_text_border_A.draw(T); card_text_border_B.draw(T); card_text_center.draw(T)
            GFM_card = [card_rect, card_oval, card_text_border_A, card_text_border_B, card_text_center]
        elif card[1] == '♣':
            card_text_border_A.setTextColor("black"); card_text_border_B.setTextColor("black"); card_text_center.setTextColor("black")
            card_text_border_A.draw(T); card_text_border_B.draw(T); card_text_center.draw(T)
            GFM_card = [card_rect, card_oval, card_text_border_A, card_text_border_B, card_text_center]
        elif card[1] == '♠':
            card_text_border_A.setTextColor("black"); card_text_border_B.setTextColor("black"); card_text_center.setTextColor("black")
            card_text_border_A.draw(T); card_text_border_B.draw(T); card_text_center.draw(T)
            GFM_card = [card_rect, card_oval, card_text_border_A, card_text_border_B, card_text_center]
    elif op_or_cl == "closed":
        card_oval.setOutline("white")
        card_oval.draw(T)
        GFM_card = [card_rect, card_oval]

    return GFM_card


def bid(T, OOAP):
    CR = 7
    N_100 = round(OOAP.bid // 100)
    N_25 = round((OOAP.bid - N_100 * 100) //25)
    N_5 = round((OOAP.bid - N_100 * 100 - N_25 * 25) // 5)
    N_1 = round(OOAP.bid - N_100 * 100 - N_25 * 25 - N_5 * 5)
    GFM_bid = []

    for i in range(0, N_1):
        chip_1_circ = Circle(Point(OOAP.bid_pos[0]-9/2*CR, OOAP.bid_pos[1]+i*CR), CR); chip_1_circ.setFill("white")
        chip_1_circ.draw(T)
        chip_1_text = Text(Point(OOAP.bid_pos[0]-9/2*CR, OOAP.bid_pos[1]+i*CR), "1"); chip_1_text.setTextColor("black"); \
            chip_1_text.setStyle("bold"); chip_1_text.setSize(7)
        chip_1_text.draw(T)
        GFM_bid.append(chip_1_circ); GFM_bid.append(chip_1_text)

    for i in range(0, N_5):
        chip_5_circ = Circle(Point(OOAP.bid_pos[0]-3/2*CR, OOAP.bid_pos[1]+i*CR), CR); chip_5_circ.setFill("red")
        chip_5_circ.draw(T)
        chip_5_text = Text(Point(OOAP.bid_pos[0]-3/2*CR, OOAP.bid_pos[1]+i*CR), "5"); chip_5_text.setTextColor("yellow"); \
            chip_5_text.setStyle("bold"); chip_5_text.setSize(7)
        chip_5_text.draw(T)
        GFM_bid.append(chip_5_circ); GFM_bid.append(chip_5_text)

    for i in range(0, N_25):
        chip_25_circ = Circle(Point(OOAP.bid_pos[0]+3/2*CR, OOAP.bid_pos[1]+i*CR), CR); chip_25_circ.setFill("blue")
        chip_25_circ.draw(T)
        chip_25_text = Text(Point(OOAP.bid_pos[0]+3/2*CR, OOAP.bid_pos[1]+i*CR), "25"); chip_25_text.setTextColor("yellow"); \
            chip_25_text.setStyle("bold"); chip_25_text.setSize(6)
        chip_25_text.draw(T)
        GFM_bid.append(chip_25_circ); GFM_bid.append(chip_25_text)

    for i in range(0, N_100):
        chip_100_circ = Circle(Point(OOAP.bid_pos[0]+9/2*CR, OOAP.bid_pos[1]+i*CR), CR); chip_100_circ.setFill("black")
        chip_100_circ.draw(T)
        chip_100_text = Text(Point(OOAP.bid_pos[0]+9/2*CR, OOAP.bid_pos[1]+i*CR), "100"); chip_100_text.setTextColor("yellow"); \
            chip_100_text.setStyle("bold"); chip_100_text.setSize(5)
        chip_100_text.draw(T)
        GFM_bid.append(chip_100_circ); GFM_bid.append(chip_100_text)

    return GFM_bid


def action_text(T, OOAP, line):
    action_text = Text(Point(OOAP.action_pos[0], OOAP.action_pos[1]), line)
    action_text.draw(T); sleep(1.2); action_text.undraw()


def action_text_and_entry(T, OOAP, line, option_A, option_B, option_C):
    TW = 1366; TH = 697; a = 2/3*TW / 2; b = 2/3*TH / 2
    do = ""

    while do == "" or do != option_A or do != option_B or do != option_C:
        do_text = Text(Point(OOAP.action_pos[0], OOAP.action_pos[1]-25), line)
        do_text.draw(T)
        do_entry = Entry(Point(TW/2-a*3/5, TH/2-186-25), 12)
        do_entry.draw(T)
        T.getMouse()
        do = do_entry.getText()
        do_text.undraw()
        do_entry.undraw()

    return do


def raising_text_and_entry(T, OOAP, line, min_value, max_value):
    TW = 1366; TH = 697; a = 2/3*TW / 2; b = 2/3*TH / 2
    do = ""

    while do == "" or do < min_value or do > max_value:
        do_text = Text(Point(OOAP.action_pos[0], OOAP.action_pos[1]-25), line)
        do_text.draw(T)
        do_entry = Entry(Point(TW/2-a*3/5, TH/2-186-75), 12)
        do_entry.draw(T)
        T.getMouse()
        do = int(do_entry.getText())
        do_text.undraw()
        do_entry.undraw()

    return do


def action_button(T, option_A, option_B, option_C):
    TW = 1366; TH = 697; a = 2/3*TW / 2; b = 2/3*TH / 2
    x = 35; y = 15; e = 80

    if option_C == "-":
        action_box_A = Rectangle(Point(TW/2-a*3/5-x-e/2, TH/2-256-y), Point(TW/2-a*3/5+x-e/2, TH/2-256+y)); action_box_A.setFill("yellow")
        action_box_B = Rectangle(Point(TW/2-a*3/5-x+e/2, TH/2-256-y), Point(TW/2-a*3/5+x+e/2, TH/2-256+y)); action_box_B.setFill("yellow")
        action_text_A = Text(Point(TW/2-a*3/5-e/2, TH/2-256), option_A)
        action_text_B = Text(Point(TW/2-a*3/5+e/2, TH/2-256), option_B)
        action_box_A.draw(T); action_box_B.draw(T)
        action_text_A.draw(T); action_text_B.draw(T)
        did_hit = "no"

        while did_hit == "no":
            clicked = T.getMouse()
            gx = clicked.getX()
            gy = clicked.getY()

            if gx >= TW/2-a*3/5-x-e/2 and gx <= TW/2-a*3/5+x-e/2 and gy >= TH/2-256-y and gy <= TH/2-256+y:
                choice = option_A
                did_hit = "yes"
            elif gx >= TW/2-a*3/5-x+e/2 and gx <= TW/2-a*3/5+x+e/2 and gy >= TH/2-256-y and gy <= TH/2-256+y:
                choice = option_B
                did_hit = "yes"

        action_box_A.undraw(); action_box_B.undraw()
        action_text_A.undraw(); action_text_B.undraw()

    else:
        action_box_A = Rectangle(Point(TW/2-a*3/5-x-e, TH/2-256-y), Point(TW/2-a*3/5+x-e, TH/2-256+y)); action_box_A.setFill("yellow")
        action_box_B = Rectangle(Point(TW/2-a*3/5-x, TH/2-256-y), Point(TW/2-a*3/5+x, TH/2-256+y)); action_box_B.setFill("yellow")
        action_box_C = Rectangle(Point(TW/2-a*3/5-x+e, TH/2-256-y), Point(TW/2-a*3/5+x+e, TH/2-256+y)); action_box_C.setFill("yellow")
        action_text_A = Text(Point(TW/2-a*3/5-e, TH/2-256), option_A)
        action_text_B = Text(Point(TW/2-a*3/5, TH/2-256), option_B)
        action_text_C = Text(Point(TW/2-a*3/5+e, TH/2-256), option_C)
        action_box_A.draw(T); action_box_B.draw(T); action_box_C.draw(T)
        action_text_A.draw(T); action_text_B.draw(T); action_text_C.draw(T)
        did_hit = "no"

        while did_hit == "no":
            clicked = T.getMouse()
            gx = clicked.getX()
            gy = clicked.getY()

            if gx >= TW/2-a*3/5-x-e and gx <= TW/2-a*3/5+x-e and gy >= TH/2-256-y and gy <= TH/2-256+y:
                choice = option_A
                did_hit = "yes"
            elif gx >= TW/2-a*3/5-x and gx <= TW/2-a*3/5+x and gy >= TH/2-256-y and gy <= TH/2-256+y:
                choice = option_B
                did_hit = "yes"
            elif gx >= TW/2-a*3/5-x+e and gx <= TW/2-a*3/5+x+e and gy >= TH/2-256-y and gy <= TH/2-256+y:
                choice = option_C
                did_hit = "yes"

        action_box_A.undraw(); action_box_B.undraw(); action_box_C.undraw()
        action_text_A.undraw(); action_text_B.undraw(); action_text_C.undraw()

        return choice


def play_again_button(T, option_A, option_B):
    TW = 1366; TH = 697; a = 2/3*TW / 2; b = 2/3*TH / 2
    x = 35; y = 15; e = 80
    action_box_A = Rectangle(Point(TW/2-x-e/2, TH/2-120-y), Point(TW/2+x-e/2, TH/2-120+y)); action_box_A.setFill("yellow")
    action_box_B = Rectangle(Point(TW/2-x+e/2, TH/2-120-y), Point(TW/2+x+e/2, TH/2-120+y)); action_box_B.setFill("yellow")
    action_text_A = Text(Point(TW/2-e/2, TH/2-120), option_A)
    action_text_B = Text(Point(TW/2+e/2, TH/2-120), option_B)
    action_box_A.draw(T); action_box_B.draw(T)
    action_text_A.draw(T); action_text_B.draw(T)
    did_hit = "no"

    while did_hit == "no":
        clicked = T.getMouse()
        gx = clicked.getX()
        gy = clicked.getY()

        if gx >= TW/2-x-e/2 and gx <= TW/2+x-e/2 and gy >= TH/2-160-y and gy <= TH/2-120+y:
            choice = option_A
            did_hit = "yes"
        elif gx >= TW/2-x+e/2 and gx <= TW/2+x+e/2 and gy >= TH/2-160-y and gy <= TH/2-120+y:
            choice = option_B
            did_hit = "yes"

    action_box_A.undraw(); action_box_B.undraw()
    action_text_A.undraw(); action_text_B.undraw()

    return choice


# T = table
# TW = table_width
# TH = table_height
# COH_pos = center_of_holes_pos
# CW = card_width
# CH = card_height
# CR = chip_radius
# TR = token_radius
# N_100 = num_of_100
# GFM = geometry_for_move