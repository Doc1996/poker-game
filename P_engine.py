from time import *
import random
import simpleaudio

from P_action import *
from P_CAS import *
from P_classes import *
from P_decision import *
from P_next_one_and_sort import *
from P_ROA import *
from P_SB_and_BB import *
from P_visuals import *


try:
    simpleaudio.WaveObject.from_wave_file("western_music.wav").play()

    while True:
        T = window()
        you = Player(start_name(T))
        Logan = PCPlayer("Logan")
        Harry = PCPlayer("Harry")
        Mark = PCPlayer("Mark")
        Cole = PCPlayer("Cole")
        Amanda = PCPlayer("Amanda")
        Juan = PCPlayer("Juan")
        Vega = PCPlayer("Vega")
        Ray = PCPlayer("Ray")
        Mary = PCPlayer("Mary")
        Winston = PCPlayer("Winston")

        base_of_pl = [Logan, Harry, Mark, Cole, Amanda, Juan, Vega, Ray, Mary, Winston]
        random.shuffle(base_of_pl)
        PP = base_of_pl[0:start_n(T)]
        AP = [you] + PP

        for i in range(0, len(AP)):
            AP[i].in_game = "in"
            AP[i].coins = 500
            individual_pos(AP[i], i)

        shared_pos(Player)
        game = 0
        remembered_pl = []


        while True:
            N = len(AP)
            for i in range(0, N):
                AP[i].in_game = "in"
                AP[i].coins = round(AP[i].coins)
                AP[i].hole = []
                AP[i].did_move = "NMY"
                AP[i].last_diff = 0
                AP[i].comb_and_score = []

            Player.cards = [[v, s] for v in ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2'] for s in ['♥', '♦', '♠', '♣']]
            random.shuffle(Player.cards)
            Player.comm = []
            Player.GFM_comm = []
            MI = Misc(game % N, BB_diff(game), 0, BB_diff(game), "no")

            for i in remembered_pl:
                if i < MI.POO:
                    for i in range(0, N-1):
                        C(AP, MI)

            GFM_token = token(T, AP[MI.POO])
            Player.GFM_deck = card(T, Player.deck_pos, Player.cards[0], "closed")

            for i in range(0, N):
                AP[i].hit_hole()
                AP[i].GFM_hole = []
                AP[i].GFM_name_and_coins = name_and_coins(T, AP[i])
                if AP[i] in PP:
                    AP[i].GFM_hole.extend(card(T, AP[i].hole_A_pos, AP[i].hole[0], "closed"))
                else:
                    AP[i].GFM_hole.extend(card(T, AP[i].hole_A_pos, AP[i].hole[0], "opened"))
                sleep(0.2)

            for i in range(0, N):
                AP[i].hit_hole()
                if AP[i] in PP:
                    AP[i].GFM_hole.extend(card(T, AP[i].hole_B_pos, AP[i].hole[1], "closed"))
                else:
                    AP[i].GFM_hole.extend(card(T, AP[i].hole_B_pos, AP[i].hole[1], "opened"))
                sleep(0.2)
                AP[i].comb_and_score = CAS(AP[i].hole)
                if AP[i] in PP:
                    decide(AP[i], 2, MI)

            SB_and_BB(T, C(AP, MI), MI, game, "SB")
            SB_and_BB(T, C(AP, MI), MI, game, "BB")
            ROA(T, AP, PP, MI, N)


            k = 0
            for i in [3, 1, 1]:
                if len([[AP[i].in_game] for i in range(0, N) if AP[i].in_game == "in"]) == 1:
                    break
                if MI.did_someone_all_in == "no":
                    Player.hit_comm(i)
                    for m in range(k, k+i):
                        Player.GFM_comm.extend(card(T, Player.comm_pos[m], Player.comm[m], "opened"))
                    for j in range(0, N):
                        AP[j].comb_and_score = CAS(AP[j].hole + Player.comm)
                        AP[j].did_move = "NMY"
                        AP[j].last_diff = 0
                        if AP[j] in PP:
                            decide(AP[j], 2+len(Player.comm), MI)
                    k += i
                    sleep(1.2)

                    ROA(T, AP, PP, MI, N)
    
                else:
                    num_of_comm_cards = len(Player.comm)
                    for i in range(0, 6):
                        if num_of_comm_cards == i:
                            Player.hit_comm(5-i)
                            for m in range(k, 5):
                                Player.GFM_comm.extend(card(T, Player.comm_pos[m], Player.comm[m], "opened"))
                            for j in range(0, N):
                                AP[j].comb_and_score = CAS(AP[j].hole + Player.comm)
                                AP[j].did_move = "NMY"
                                AP[j].last_diff = 0
                                if AP[j] in PP:
                                    decide(AP[j], 2+len(Player.comm), MI)
                    sleep(1.2)
                    break


            for i in range(0, N):
                if AP[i].in_game == "in":
                    for j in AP[i].GFM_hole:
                        j.undraw()
                    AP[i].GFM_hole.extend(card(T, AP[i].hole_A_pos, AP[i].hole[0], "opened"))
                    AP[i].GFM_hole.extend(card(T, AP[i].hole_B_pos, AP[i].hole[1], "opened"))

            sleep(1.2)
            GR = [[AP[i].name, AP[i].comb_and_score[0], AP[i].comb_and_score[1], AP[i].bid] for i in range(0, N) if AP[i].in_game == "in"]
            sort(GR, 2)
            GW = [[-1, GR[-1][3]]]

            for i in range(0, len(GR)-1):
                if GR[-1][2] == GR[i][2]:
                    GW.append([i])
                    GW[len(GW)-1].append(GR[i][3])

            sort(GW, 1)
            for i in range(0, N):
                AP[i].remembered_bid = AP[i].bid

            GFM_game_win = []
            for i in range(0, len(GW)):
                for j in range(0, N):
                    if GR[GW[i][0]][0] == AP[j].name:
                        for k in range(0, N):
                            if AP[j].remembered_bid >= AP[k].remembered_bid:
                                AP[j].coins += round(AP[k].bid / (len(GW)-i))
                                AP[k].bid -= AP[k].bid / (len(GW)-i)
                            else:
                                AP[j].coins += round(AP[j].bid / (len(GW)-i))
                                AP[k].bid -= AP[j].bid / (len(GW)-i)
                        TW = 1366; TH = 697
                        T_game_win_text = Text(Point(TW/2, TH/2-75-i*30), "The pot is won by {} ({}).".format(AP[j].name, AP[j].comb_and_score[0]))
                        T_game_win_text.setTextColor("yellow")
                        GFM_game_win.append(T_game_win_text)
                        T_game_win_text.draw(T)

            T.getMouse()
            for i in GFM_game_win:
                i.undraw()

            for i in range(0, N):
                AP[i].coins += AP[i].bid
                AP[i].bid = 0
                AP[i].remembered_bid = 0

            for i in range(0, N):
                for j in AP[i].GFM_name_and_coins: j.undraw()
                for j in AP[i].GFM_hole: j.undraw()
                for j in AP[i].GFM_bid: j.undraw()

            for i in Player.GFM_comm: i.undraw()
            for i in Player.GFM_deck: i.undraw()
            for i in GFM_token: i.undraw()


            MC = [[AP[i].name, AP[i].coins] for i in range(0, N)]
            sort(MC, 1)

            if MC[-2][1] == 0 or 0.0:
                TW = 1366; TH = 697
                T_match_win_text = Text(Point(TW/2, TH/2-75), "The match winner is {}.".format(AP[j].name))
                T_match_win_text.setTextColor("yellow")
                T_match_win_text.draw(T)
                T.getMouse()
                T_match_win_text.undraw()
                break
            else:
                remembered_pl = []
                for i in range(0, N):
                    if AP[i].coins == 0 or 0.0:
                        remembered_pl.append(i)
                correction_for_deleted = 0
                for i in remembered_pl:
                    del AP[i-correction_for_deleted]
                    correction_for_deleted += 1
                game += 1

        T_play_again_text = Text(Point(TW/2, TH/2-75), "Do you want to play a new match?")
        T_play_again_text.draw(T)
        play_again = play_again_button(T, "yes", "no")
        if play_again == "yes":
            pass
        else:
            break

except:
    pass


# MI = misc_inst
# ROA = round_of_action
# C = check_if_not_next_one
# CAS = comb_and_score
# AP = all_pl
# PP = pc_pl
# OOAP = one_of_all_pl
# OOPP = one_of_pc_pl
# POO = pl_on_order
# "NMY" = "not_moved_yet"
# "AM" = "already_moved"
# GR = game_results
# GW = game_winners
# MC = match_coins
