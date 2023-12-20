
input = open("input.txt", 'r')
text = input.read()
input.close()

lines = text[0:(len(text)-1)].split('\n')

def getValue(card):
    match card:
        case 'A':
            return 14
        case 'K':
            return 13
        case 'Q':
            return 12
        case 'J':
            return 1
        case 'T':
            return 10
        case _:
            return int(card)

def getType(hand, value):
    counted = []
    counts = []
    handType = 0
    jokerCards = 0

    for card in hand:
        if card == 'J':
            jokerCards += 1
        elif card not in counted:
            counted.append(card)
            counts.append(hand.count(card))

    if len(counts) != 0:
        match max(counts):
            case 5:
                # Five of a kind
                handType = 7
            case 4:
                # Four of a kind
                handType = 6
            case 3:
                if min(counts) == 2:
                    # Full House
                    handType = 5
                else:
                    # Three of a kind
                    handType = 4
            case 2:
                if counts.count(2) > 1:
                    # Two pairs
                    handType = 3
                else:
                    # One pair
                    handType = 2
            case 1:
                    # High card
                    handType = 1

    match jokerCards:
        case 5:
            handType = 7
        case 4:
            handType = 7
        case 3:
            if handType == 1:
                handType = 6
            elif handType == 2:
                handType = 7
        case 2:
            if handType == 1:
                handType = 4
            elif handType == 2:
                handType = 6
            elif handType == 4:
                handType = 7
        case 1:
            if handType == 1:
                handType = 2
            elif handType == 2:
                handType = 4
            elif handType == 3:
                handType = 5
            elif handType == 4:
                handType = 6
            elif handType == 6:
                handType = 7

    return handType, hand, value

def compareHands(hand1, hand2):
    for i in range(5):
        if getValue(hand1[1][i]) > getValue(hand2[1][i]):
            return hand1
        elif getValue(hand1[1][i]) < getValue(hand2[1][i]):
            return hand2

def makeRankings(hands):
    ranking = []

    for hand in hands:
        if len(ranking) == 0:
            ranking.append(hand)
        else:
            for j in range(len(ranking)):
                if hand[0] > ranking[j][0] and j != len(ranking)-1:
                    continue
                elif hand[0] < ranking[j][0]:
                    ranking.insert(j, hand)
                    break
                elif hand[0] == ranking[j][0]:
                    if compareHands(hand, ranking[j]) == ranking[j]:
                        ranking.insert(j, hand)
                        break
                if j == len(ranking)-1:
                    ranking.append(hand)

    return ranking

def getWinnings(hands):
    winnings = 0
    rank = 1

    for hand in hands:
        bet = ''
        for number in hand[2]:
            bet += str(number)
        bet = int(bet)
        winnings += (bet*rank)
        rank += 1

    print(winnings)

def test():
    def score(a):
        a,bet = a.split()
        JC = a.count('J')
        s1,C = max(((a.count(c)+(JC if c!= 'J' else 0),c) for c in a), default=(0,'X'))
        s2 = max((a.count(c) for c in a.replace(C,'').replace('J','')), default=0)
        return ((s1,s2,*['J23456789TQKA'.index(c) for c in a]),bet)

    hands = sorted(map(score,open("input.txt").read().splitlines()))
    print( sum([(i*int(b)) for i,(*_,b) in enumerate(hands,start=1)]) )


hands = []
for line in lines:
    hand = []
    bet = []
    for char in line[0:5]:
        hand.append(char)
    for char in line[6:(len(line))]:
        bet.append(char)
    hands.append(getType(hand, bet))

hands = sorted(hands)
ranking = makeRankings(hands)
getWinnings(ranking)

#test()
    
