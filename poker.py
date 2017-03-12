import random

#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print "Database version : %s " % data

# disconnect from server
db.close()

cardSuits = ['hearts','clubs','spades','diamonds']
cardValues = ['two','three','four','five','six','seven','eight','nine','ten','jack','queen','king','ace']
deckOfCards = []

for suit in cardSuits:
    for value in cardValues:
        deckOfCards.append([value,suit])

# for each in cards:
    # print each

players = 1
cardsInPlayerHands = 2
# gameCards = []
#
# for player in range(1,players+1):
#     for number in range(1,cardsInPlayerHands+1):
#         # print player, number
#         individualCard = random.choice(deckOfCards)
#         gameCards.append([player,number,individualCard])
#         deckOfCards.remove(individualCard)
gameCards = {}

for player in range(1,players+1):
    for number in range(1,cardsInPlayerHands+1):
        # print player, number
        individualCard = random.choice(deckOfCards)
        gameCards[player,number] = individualCard
        deckOfCards.remove(individualCard)

for each in gameCards:
    print each, gameCards[each]

communityCards = []
# Flop
individualCard = random.choice(deckOfCards)
communityCards.append(individualCard)
deckOfCards.remove(individualCard)

individualCard = random.choice(deckOfCards)
communityCards.append(individualCard)
deckOfCards.remove(individualCard)

individualCard = random.choice(deckOfCards)
communityCards.append(individualCard)
deckOfCards.remove(individualCard)

# Turn
individualCard = random.choice(deckOfCards)
communityCards.append(individualCard)
deckOfCards.remove(individualCard)

# River
individualCard = random.choice(deckOfCards)
communityCards.append(individualCard)
deckOfCards.remove(individualCard)

# for each in communityCards:
    # print each

# Check for Winners

for player in range(1,players+1):
    hand = []
    # print player
    # print gameCards[player,1]
    hand.append(gameCards[player,1])
    # print gameCards[player,2]
    hand.append(gameCards[player,2])
    for each in communityCards:
        hand.append(each)
    # print hand
    for each in hand:
        print each
# 1. Royal flush
# A, K, Q, J, 10, all the same suit.
# A K Q J T
    royalFlush = False





# for each in gameCards:



# 2. Straight flush
# Five cards in a sequence, all in the same suit.
# 8 7 6 5 4
# 3. Four of a kind
# All four cards of the same rank.
# J J J J 7
#
# 4. Full house
# Three of a kind with a pair.
# T T T 9 9
#
# 5. Flush
# Any five cards of the same suit, but not in a sequence.
# 4 J 8 2 9
#
# 6. Straight
# Five cards in a sequence, but not of the same suit.
# 9 8 7 6 5
#
# 7. Three of a kind
# Three cards of the same rank.
# 7 7 7 K 3
#
# 8. Two pair
# Two different pairs.
# 4 4 3 3 Q
#
# 9. Pair
# Two cards of the same rank.
# A A 8 4 7
#
# 10. High Card
# When you haven't made any of the hands above, the highest card plays.
# In the example below, the jack plays as the highest card.
# 3 J 8 4 2
