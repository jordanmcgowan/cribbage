from random import shuffle
from random import randint
import copy
import collections
import itertools
from itertools import groupby

player1Score = 0
player1HandCount = 0


def searchForRuns(hand, player):
    runHand = copy.deepcopy(hand)
    #print "in runs"
    global player1Score
    global player2Score
    global player1HandCount
    global player2HandCount
    foundRunOf5 = False
    foundRunOf4 = False
    cards = []
    for i in range(len(runHand)):
        cards.append(getRunValue(runHand[i]))
    #For player 1
    if player == 1:
        checked = []
        dups = []
        multiplier = 1
        #Remove dups
        for e in cards:
            if e not in checked:
                checked.append(e)
            else:
                dups.append(e)
        for i in range(0,len(checked)-4):
            if (checked[i]) + 1 == (checked[i+1]):
                if (checked[i+1]) + 1 == (checked[i+2]):
                    if (checked[i+2]) + 1 == (checked[i+3]):
                        if (checked[i+3]) + 1 == (checked[i+4]):
                            print "Run of 5, for 5"
                            foundRunOf5 = True
                            player1Score += (5 * multiplier)
                            player1HandCount += (5 * multiplier)
        for i in range(0,len(checked)-3):
            if not foundRunOf5:
                if (checked[i]) + 1 == (checked[i+1]):
                    if (checked[i+1]) + 1 == (checked[i+2]):
                        if (checked[i+2]) + 1 == (checked[i+3]):
                            foundRunOf4 = True
                            for j in range(0,4):
                                if checked[i+j] in dups:
                                    multiplier *= 2
                            for i in range(multiplier):
                                print "Run of 4, for 4"
                            player1Score += (4 * multiplier)
                            player1HandCount += (4 * multiplier)
        for i in range(0,len(checked)-2):
            if not foundRunOf5:
                if not foundRunOf4:
                    if (checked[i]) + 1 == (checked[i+1]):
                        if (checked[i+1]) + 1 == (checked[i+2]):
                            for j in range(0,3):
                                if checked[i+j] in dups:
                                    multiplier *= 2
                            for i in range(multiplier):
                                print "Run of 3, for 3"
                            player1Score += (3 * multiplier)
                            player1HandCount += (3 * multiplier)
def getRunValue(card):
    arr = card.split(" of ")
    if arr[0] == "Ace":
        value = 1
    elif arr[0] == "Jack":
        value = 11
    elif arr[0] == "Queen":
        value = 12
    elif arr[0] == "King":
        value = 13
    else:
        value = (int)(arr[0])
    return value

def getSuit(card):
    arr = card.split(" of ")
    return arr[1]

def searchForFlush(hand, player, crib):
    flushHand = copy.deepcopy(hand)
    global player1Score
    global player1HandCount
    #print "in flush"
    cards = []
    flipCardIndex = flushHand.index(flipCard)
    flushHand.pop(flipCardIndex)
    for i in range(len(flushHand)):
        cards.append(getSuit(flushHand[i]))
    #Fro crib TODO
    if cribHand:
        if cards[1:] == cards[:-1]:
            if getSuit(flipCard) == cards[0]:
                print "Flush for 5"
                if player == 1:
                    player1Score += 5
                    player1Score += 5
                if player == 2:
                    player2Score += 5
                    player2HandCount += 5
    #For player 1
    elif player == 1:
        if cards[1:] == cards[:-1]:
            if getSuit(flipCard) == cards[0]:
                print "Flush for 5"
                player1Score += 1
                player1HandCount += 1
            else:
                print "Flush for 4"
                player1Score += 4
                player1HandCount += 4

cribHand = ['10 of Hearts', 'Jack of Hearts', 'Queen of Hearts', 'King of Hearts', 'King of Clubs']
player = 1
flipCard = 'King of Clubs'

searchForRuns(cribHand, player)
searchForFlush(cribHand, player, True)
