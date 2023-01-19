#======================================================================================================================
#common hole functions:

def ishole_connectors(cards):
    ranks_hole = sorted([i for i, _ in cards[0:2]])
    suits_hole = [i for _, i in cards[0:2]]
    if ranks_hole[1]-ranks_hole[0]==1 and suits_hole[0] != suits_hole[1]: return True
    return False

def ishole_onegappers(cards):
    ranks_hole = sorted([i for i, _ in cards[0:2]])
    suits_hole = [i for _, i in cards[0:2]]
    if ranks_hole[1]-ranks_hole[0]==2 and suits_hole[0] != suits_hole[1]: return True
    return False

def ishole_twogappers(cards):
    ranks_hole = sorted([i for i, _ in cards[0:2]])
    suits_hole = [i for _, i in cards[0:2]]
    if ranks_hole[1]-ranks_hole[0]==3 and suits_hole[0] != suits_hole[1]: return True
    return False

def ishole_suitedconnectors(cards):
    ranks_hole = sorted([i for i, _ in cards[0:2]])
    suits_hole = [i for _, i in cards[0:2]]
    if ranks_hole[1]-ranks_hole[0]==1 and suits_hole[0] == suits_hole[1]: return True
    return False

def ishole_suitedonegappers(cards):
    ranks_hole = sorted([i for i, _ in cards[0:2]])
    suits_hole = [i for _, i in cards[0:2]]
    if ranks_hole[1]-ranks_hole[0]==2 and suits_hole[0] == suits_hole[1]: return True
    return False

def ishole_suitedtwogappers(cards):
    ranks_hole = sorted([i for i, _ in cards[0:2]])
    suits_hole = [i for _, i in cards[0:2]]
    if ranks_hole[1]-ranks_hole[0]==3 and suits_hole[0] == suits_hole[1]: return True
    return False

def ishole_suited(cards):
    suits_hole = [i for _, i in cards[0:2]]
    ranks_hole = sorted([i for i, _ in cards[0:2]])
    if suits_hole[0] == suits_hole[1] and ranks_hole[1]-ranks_hole[0]>3 : return True
    return False

def ishole_pocketpair(cards):
    ranks_hole = sorted([i for i, _ in cards[0:2]])
    if ranks_hole[1] == ranks_hole[0] : return True
    return False

def isany(cards):
    return True

#======================================================================================================================
#common identification functions:

def highest(cards, score = False):
    ranks = sorted([i for i, _ in cards ], reverse=True) 
    return ranks[0] if not score else '.'.join(str(i) for i in ranks[0:5])

def lowest(cards, score = False):
    ranks = sorted([i for i, _ in cards ]) 
    return ranks[0] if not score else '.'.join(str(i) for i in ranks[0:5:-1])

def isquads(cards, hole_en = False, score = False):
    ranks = [i for i,_ in cards]
    card_count = sorted([(ranks.count(s),s) for s in sorted(list(set(ranks)), reverse=True)], key = lambda x:x[0],reverse=True)
    
    if card_count[0][0] == 4:
        if hole_en:
            if ranks.count(cards[0][0]) == 4 or ranks.count(cards[1][0]) == 4:
                return True if not score else (True,'.'.join([str(card_count[0][1]),str(sorted([r for r in ranks if r != card_count[0][1]],reverse=True)[0])]))
        else:
            return True if not score else (True,'.'.join([str(card_count[0][1]),str(sorted([r for r in ranks if r != card_count[0][1]],reverse=True)[0])]))
    return False if not score else (False,'0.0')

def isfullhouse(cards, hole_en = False,score = False):
    ranks = [i for i,_ in cards]
    card_count = sorted([(ranks.count(s),s) for s in sorted(list(set(ranks)), reverse=True)], key = lambda x:x[0],reverse=True)
    
    if card_count[0][0] == 3:
        if card_count[1][0] == 2:
            if hole_en:
                if ranks.count(cards[0][0]) >= 2 or ranks.count(cards[1][0]) >= 2:
                    return True if not score else (True,'.'.join([str(card_count[0][1] ),str(card_count[1][1] )]))
            else:
                return True if not score else (True,'.'.join([str(card_count[0][1] ),str(card_count[1][1] )]))
    return False if not score else (False,'0.0')

def isflush(cards, hole_en = False ,score = False):
    suits = [i for _, i in cards]
    card_count = sorted([(suits.count(s), s) for s in sorted(list(set(suits)), reverse=True)], key=lambda x: x[0], reverse=True)
    
    if card_count[0][0] >= 5:
        if hole_en:
            if suits.count(cards[0][1]) >= 5 or suits.count(cards[1][1]) >= 5:
                return True if not score else (True,'.'.join(  [str(j) for j in sorted( [i  for i, s in cards if s == card_count[0][1]], reverse=True)][:5] ))
        else:
            return True if not score else (True,'.'.join(  [str(j) for j in sorted( [i  for i, s in cards if s == card_count[0][1]], reverse=True)][:5] ))
    return False if not score else (False,'0.0.0.0.0')

def isflush_draw(cards, hole_en = False ,score = False):
    suits = [i for _, i in cards]
    card_count = sorted(suits.count(s) for s in set(suits))
    
    if card_count[-1] == 4:
        if hole_en:
            if suits.count(cards[0][1]) == 4 or suits.count(cards[1][1]) == 4:
                return True if not score else (True,'0.0')
        else:
            return True if not score else (True,'0.0')
    return False if not score else (False,'0.0')

def isstraight(cards, hole_en = False,score = False):
    def isacceptable(crd):
        if (crd == cards[0][0] and ranks.count(cards[0][0]) !=2) or (crd == cards[1][0] and ranks.count(cards[1][0]) != 2) or  (crd == cards[0][0] and crd == cards[1][0]):
            return True
        return False

    ranks = sorted(set(i for i, _ in cards))
    
    if ranks[-1] == 14: ranks.insert(0,1)

    for i,c in enumerate(ranks):
        m=0
        sum=0
        j=i+1
        
        if isacceptable(c):
            h_e = True
        else:
            h_e = False
        while j < len(ranks) and ranks[j]-ranks[j-1] == 1 :
            if isacceptable(ranks[j]):
                h_e = True
            m=ranks[j]
            sum+=1
            j+=1

        if sum >= 4:
            if hole_en:
                if h_e:
                    return True if not score else (True,'.'.join(str(j) for j in [m,ranks[j-5]]))
            else:
                return True if not score else (True,'.'.join(str(j) for j in [m,ranks[j-5]]))
    return False if not score else (False,'0.0')

def isstraight_draw(cards, hole_en = False,score = False):
    def isacceptable(crd):
        if (crd == cards[0][0] and ranks.count(cards[0][0]) !=2) or (crd == cards[1][0] and ranks.count(cards[1][0]) != 2) or  (crd == cards[0][0] and crd == cards[1][0]):
            return True
        return False
    ranks = sorted(set(i for i, _ in cards))
    if ranks[-1] == 14: ranks.insert(0, 1)

    for i,c in enumerate(ranks):
        sum=0
        j=i+1
        
        if isacceptable(c):
            h_e = True
        else:
            h_e = False
        while j < len(ranks) and ranks[j]-ranks[j-1] == 1 :
            if isacceptable(ranks[j]): h_e = True
            sum+=1
            j+=1

        if sum == 3:
            if hole_en:
                if h_e:
                    return True if not score else (True,'0.0')
            else:
                return True if not score else (True,'0.0')
    return False if not score else (False,'0.0')

def isinsidestraight_draw(cards, hole_en = False,score = False):
    def isacceptable(crd):
        if (crd == cards[0][0] and ranks.count(cards[0][0]) !=2) or (crd == cards[1][0] and ranks.count(cards[1][0]) != 2) or  (crd == cards[0][0] and crd == cards[1][0]):
            return True
        return False

    ranks = sorted(set(i for i, _ in cards))
    if ranks[-1] == 14: ranks.insert(0,1)

    for i,c in enumerate(ranks):
        life = 1
        sum=0
        j=i+1
        while j < len(ranks) and ( ranks[j]-ranks[j-1] == 1 or (ranks[j]-ranks[j-1] == 2 and life ==1)):

            if ranks[j]-ranks[j-1] == 2:
                life-=1
            sum+=1
            j+=1

        if sum >= 3:
            sum_in = 0
            k = i + 1
            if isacceptable(ranks[k - 1]):
                h_e = True
            else:
                h_e = False
            while k < len(ranks) and ranks[k] - ranks[k - 1] == 1:
                if isacceptable(ranks[k]):
                    h_e = True
                sum_in += 1
                k += 1
            if sum_in < 3 :
                if hole_en:
                    if h_e:
                        return True if not score else (True,'0.0')
                else:
                    return True if not score else (True,'0.0')

    return False if not score else (False,'0.0')

def isset(cards, hole_en = False,score = False):
    ranks = [i for i,_ in cards]
    card_count = sorted([(ranks.count(s),s) for s in sorted(list(set(ranks)), reverse=True)], key = lambda x:x[0],reverse=True)
    
    if card_count[0][0] == 3:
        if card_count[1][0] == 1:
            if hole_en:
                if ranks.count(cards[0][0]) == 3 or ranks.count(cards[1][0]) == 3:
                    return True if not score else (True,'.'.join([str(card[1]) for card in card_count][0:3]))
            else:
                return True if not score else (True,'.'.join([str(card[1]) for card in card_count][0:3]))
    return False if not score else (False,'0.0.0')

def istwopair(cards, hole_en = False,score = False):
    ranks = [i for i,_ in cards]
    card_count = sorted([(ranks.count(s), s) for s in sorted(list(set(ranks)), reverse=True)], key=lambda x: x[0], reverse=True)

    if card_count[0][0] == 2:
        if card_count[1][0] == 2:
            if hole_en:
                if ranks.count(cards[0][0]) == 2 or ranks.count(cards[1][0]) == 2:
                    return True if not score else (True,'.'.join([str(card_count[0][1] ),str(card_count[1][1] ),str(sorted([r for r in ranks if r != card_count[0][1] and r != card_count[1][1]],reverse=True)[0])]))
            else:
                return True if not score else (True,'.'.join([str(card_count[0][1] ),str(card_count[1][1] ),str(sorted([r for r in ranks if r != card_count[0][1] and r != card_count[1][1]],reverse=True)[0])]))
    return False if not score else (False,'0.0.0')

def isonepair(cards, hole_en = False,score = False):
    ranks = [i for i,_ in cards]
    card_count = sorted([(ranks.count(s), s) for s in sorted(list(set(ranks)), reverse=True)], key=lambda x: x[0], reverse=True)

    if card_count[0][0] == 2:
        if card_count[1][0] == 1:
            if hole_en:
                if ranks.count(cards[0][0]) == 2 or ranks.count(cards[1][0]) == 2:
                    return True if not score else (True,'.'.join([str(card[1]) for card in card_count][:4]))
            else:
                return True if not score else (True,'.'.join([str(card[1]) for card in card_count][:4]))
    return False if not score else (False,'0.0.0.0')



#======================================================================================================================
