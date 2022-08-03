def CAS(hand):
    values = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
    suits = ['♥', '♦', '♠', '♣']

    num_of_rep_values = []
    num_of_rep_suits = []
    comb_values = []
    comb_suits = []
    comb_values_out_of = []
    comb_suits_out_of = []
    pair_in_full_house = []
    w = []
    x = []
    q = y = z = m = 0
    score = 0

    for v in values:
        num_of_rep_values.append([sum(suits.count(v) for suits in hand), v])
        if [4, v] in num_of_rep_values:
            comb_values.append(['poker', v])
            q = v
        elif [3, v] in num_of_rep_values:
            comb_values.append(['tris', v])
            w.append(v)
        elif [2, v] in num_of_rep_values:
            comb_values.append(['pair', v])
            x.append(v)
        elif [1, v] in num_of_rep_values:
            comb_values.append(['high card', v])

    if x != []:
        if w != []:
            if ['tris', w[0]] in comb_values and ['pair', x[0]] in comb_values:
                comb_values_out_of.append(['full house', w[0]])
                pair_in_full_house = x[0]
        elif len(x) >= 2:
            comb_values_out_of.append([['two pairs'], x[0]])

    if len(comb_values) >= 5:
        for i in range(len(comb_values)):
            y = values.index(comb_values[i][1])
            try:
                if (comb_values[i+1][1] == values[y+1] and comb_values[i+2][1] == values[y+2] and
                comb_values[i+3][1] == values[y+3] and comb_values[i+4][1] == values[y+4]):
                    comb_values_out_of.append(['straight', comb_values[i][1]])
                    z = i
                elif (comb_values[i+1][1] == '4' and comb_values[i+2][1] == '3' and
                comb_values[i+3][1] == '2' and comb_values[i+4][1] == 'A'):
                    comb_values_out_of.append(['straight', comb_values[i][1]])
                    z = i
            except:
                pass

    for s in suits:
        num_of_rep_suits.append([sum(values.count(s) for values in hand), s])
        if [5, s] in num_of_rep_suits:
            comb_suits.append(['flush', s])
            m = s

    if comb_suits == [['flush', m]] and comb_values_out_of == [['straight', 'A']]:
        comb_suits_out_of.append(['royal flush', comb_values[z][1]])
    elif comb_suits == [['flush', m]] and comb_values_out_of == [['straight', comb_values[z][1]]]:
        comb_suits_out_of.append(['straight flush', comb_values[z][1]])


    def value_of_cards(values, num_of_value):
        for i in range(0,13):
            if num_of_value == values[i]:
                minor = 13 - i

        return minor


    combination = comb_values[0]
    score = value_of_cards(values, comb_values[0][1])

    if x != []:
        if len(x) >= 2:
            combination = ['two pairs', x[0]]
            score = 30 + value_of_cards(values, x[0])
        elif len(x) == 1:
            combination = ['pair', x[0]]
            score = 15 + value_of_cards(values, x[0])
    if w != []:
        if ['tris', w[0]] in comb_values:
            combination = ['tris', w[0]]
            score = 45 + value_of_cards(values, w[0])
    if ['straight', comb_values[z][1]] in comb_values_out_of:
        combination = ['straight', comb_values[z][1]]
        score = 60 + value_of_cards(values, comb_values[z][1])
    if ['flush', m] in comb_suits_out_of:
        combination = ['flush', m]
        score = 75
    if w != []:
        if ['full house', w[0]] in comb_values_out_of:
            combination = ['full house', w[0]]
            score = 90 + value_of_cards(values, w[0]) + value_of_cards(values, pair_in_full_house)/20
    if ['poker', q] in comb_values:
        combination = ['poker', q]
        score = 105 + value_of_cards(values, q)
    if ['straight flush', comb_values[z][1]] in comb_suits_out_of:
        combination = ['straight flush', comb_values[z][1]]
        score = 120 + value_of_cards(values, comb_values[z][1])
    if ['royal flush', comb_values[z][1]] in comb_suits_out_of:
        combination = ['royal flush', comb_values[z][1]]
        score = 135 + value_of_cards(values, comb_values[z][1])

    return [combination, score]
