from P_action import *
from P_next_one_and_sort import *
from P_visuals import *


def ROA(T, AP, PP, MI, N):
    statement = True

    while statement:
        if C(AP, MI).did_move == "AM" and MI.diff - AP[MI.POO].last_diff == 0 and AP[MI.POO].in_game == "in":
            for i in range(0, N-1):
                C(AP, MI)
            MI.diff = 0
            statement = False
        else:
            if AP[MI.POO].in_game == "in":
                if len([[AP[i].in_game] for i in range(0, N) if AP[i].in_game == "in"]) == 1:
                    statement = False
                action(T, AP[MI.POO], PP, MI)