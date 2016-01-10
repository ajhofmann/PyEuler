## Project Euler Problem 54:
## How many hands does Player 1 win in the text file poker.txt

file = open("p054_poker.txt", "r")
hands = names = file.readlines()

cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

# trim all of the hands into a 20 char string
for i in range(len(hands)):
    new_hand = ''
    for j in range(0, 28, 3):
        new_hand += hands[i][j:j+2]
    hands[i] = new_hand

# Retrieves all the numbers in a hand, sorted
def numsinhand(hand):
    return sorted(hand[0] + hand[2] + hand[4] + hand[6] + hand[8])

# ------------------------------------------
# Functions to determine if a hand has a certain sequence
# all functions require an input in the form of a string as
# NSNSNSNSNS Where N is the card number and S is the suit
# ------------------------------------------

# Determines what card wins by comparing high cards
def tiebreakhigh(hand1, hand2):
    nums1 = numsinhand(hand1)
    nums2 = numsinhand(hand2)
    for i in range(5):
        if highcard(nums1) != highcard(nums2):
            return highcard(nums1) < highcard(nums2)
        else:
            nums1.remove(cards[highcard(nums1)])
            nums2.remove(cards[highcard(nums2)])
    return 'tie'

# Determines if the hand has one pair
def isonepair(hand):
    nums = numsinhand(hand)
    return nums[0] == nums[1] or \
           nums[1] == nums[2] or \
           nums[2] == nums[3] or \
           nums[3] == nums[4]


# Determines if the hand has a two pair
def istwopair(hand):
    nums = numsinhand(hand)
    return nums[0] == nums[1] and nums[2] == nums[3] or\
           nums[0] == nums[1] and nums[3] == nums[4] or \
           nums[1] == nums[2] and nums[3] == nums[4]

# Determines if the hand has a three of a kind
def isthreeofakind(hand):
    nums = numsinhand(hand)
    return nums[0] == nums[2] or nums[1] == nums[3] or nums[2] == nums[4]

# Determines if the hand has a straight
def isstraight(hand):
    for i in range(9):
        count = 0
        for j in range(5):
            if cards[i+j] in hand:
                count += 1
            if count == 5:
                return True
    return False

# Determines if the hand has a flush
def isflush(hand):
    if hand[1] == hand[3] and hand[3] == hand[5] and hand[5] == hand[7] and hand[7] == hand[9]:
        return True
    return False

# Determines if the hand has a full house
def isfullhouse(hand):
    nums = numsinhand(hand)
    return nums[0] == nums[1] and nums[2] == nums[4] or\
           nums[0] == nums[2] and nums[3] == nums[4]

# Determines if the hand has a four of a kind
def isfourofakind(hand):
    nums = numsinhand(hand)
    return nums[0] == nums[3] or nums[1] == nums[4]

# Determines if the hand has a straight flush
def isstraightflush(hand):
    return (isflush(hand) and isstraight(hand))

# Determines if the hand has a royal flush
def isroyalflush(hand):
    if isflush(hand):
        count = 0
        for i in range(5):
            if cards[i] in hand:
                count += 1
        return count == 5
    return False

# ------------------------------------------
# end hand rankings

# functions that determine which hand wins
functs = [isroyalflush, isstraightflush, isfourofakind, isfullhouse, isflush, isstraight, isthreeofakind, istwopair, isonepair, tiebreakhigh]

# Determines the index of the highest card in the hand
def highcard(hand):
    for i in range(13):
        if cards[i] in hand:
            return i

# returns the pairs in a two pair hand and the other card
def twopairbreakdown(hand):
    hand = numsinhand(hand)
    if hand[0] == hand[1]:
        if hand[2] == hand[3]:
            if cards.index(hand[0]) < cards.index(hand[3]):
                return [hand[0], hand[3], hand[4]]
            else:
                return [hand[3], hand[0], hand[4]]
        if cards.index(hand[0]) < cards.index(hand[3]):
            return [hand[0], hand[3], hand[2]]
        else:
            return [hand[3], hand[0], hand[2]]
    if cards.index(hand[1]) < cards.index(hand[3]):
        return [hand[1], hand[3], hand[0]]
    else:
        return [hand[3], hand[1], hand[0]]

def onepairbreakdown(hand):
    nums = numsinhand(hand)
    for i in range(4):
        if nums[i] == nums[i+1]:
            return [nums[i]] + nums[:i] + nums[i+1:]



# takes two truth hands and a hand type and determines if the hands would
# tie win or lose based on that hand type
# T = Tie, True = P1 wins, False = P2 wins, N = no one wins yet
def nextAct(hand1, hand2, function):
    if function == tiebreakhigh:
        return tiebreakhigh(hand1, hand2)
    if function(hand1) and function(hand2):
        return 'T'
    if function(hand1):
        return True
    if function(hand2):
        return False
    return 'N'

def tiebreak(hand1, hand2, type):
    if type == isroyalflush:
        return 'tie'
    if type == isstraightflush or type == isstraight or type == isflush:
        return tiebreakhigh(hand1, hand2)
    if type == isfourofakind or type == isfullhouse or type == isthreeofakind:
        return highcard(numsinhand(hand1)[2]) < highcard(numsinhand(hand2)[2])
    if type == istwopair:
        hand1 = twopairbreakdown(hand1)
        hand2 = twopairbreakdown(hand2)
        for i in range(3):
            if cards.index(hand1[i]) != cards.index(hand2[i]):
                return cards.index(hand1[i]) < cards.index(hand2[i])
        return 'tie'
    if type == isonepair:
        nums1 = onepairbreakdown(hand1)
        nums2 = onepairbreakdown(hand2)
        if cards.index(nums1[0]) != cards.index(nums2[0]):
            return cards.index(nums1[0]) < cards.index(nums2[0])
        else:
            return tiebreakhigh(hand1, hand2)

wins = 0
# 6H 4H 5C 3H 2H 3S QH 5S 6S AS




for i in range(len(hands)):
    for j in range(10):
        act = nextAct(hands[i][0:10], hands[i][10:], functs[j])
        if act == True:
            wins += 1
            break
        elif not act:
            break
        elif act == 'T':
            if tiebreak(hands[i][0:10], hands[i][10:], functs[j]) != 'tie':
                if tiebreak(hands[i][0:10], hands[i][10:], functs[j]):
                    wins += 1
                break

            else:
                print('no')


print(wins)



