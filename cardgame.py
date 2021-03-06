#!/usr/bin/python
import random

gameNumber = 0
players = 0
cardsInPlayerHands = 2
cardSuitsVerbose = ['hearts','clubs','spades','diamonds']
cardSuits = ['h','c','s','d']
cardValuesVerbose = ['two','three','four','five','six','seven','eight','nine','ten','jack','queen','king','ace']
cardValues = ['02','03','04','05','06','07','08','09','10','11','12','13','01']
dictSuits = {}
dictValues = {}

def debugPrint(data):
    print data

def check0RoyalFlush(cards): #Working
    haveAce = False
    for each in cards:
        if each[0] == '01':
            haveAce = True
    if (check1StraightFlush(cards) and haveAce):
        return True
    else:
        return False

def check1StraightFlush(hand): #Working
    for each in cardSuits:
        print each
        individualSuits = []
        for card in hand:
            print card
            if card[1] == each:
                individualSuits.append(card)
        print individualSuits
        if check5Straight(individualSuits):
            return True
    return False

def check2FourOfAKind(hand): #Working
    value = []
    for each in hand:
        value.append(each[0])
    max = 0
    for each in cardValues:
        temp = value.count(each)
        if temp > max:
            max = temp
    if max > 3:
        return True
    else:
        return False

def check3FullHouse(hand): #Working
    if (check6ThreeOfAKind(hand)) and (check7TwoPair(hand)):
        return True
    else:
        return False

def check4Flush(hand): #Working
    suit = []
    for each in hand:
        suit.append(each[1])
    max = 0
    for each in cardSuits:
        temp = suit.count(each)
        if temp > max:
            max = temp
    if max > 4:
        return True
    else:
        return False

def check5Straight(hand): #Working
    # print "looking for a straight"
    value = {}
    for each in hand:
        value[each[0]]= each[1]
    # print "these are the values", value
    # print "these are the keys", value.keys()
    temp = list(value.keys())
    # print "this is a list of the keys", temp
    temp.sort()
    print "the sorted list", temp
    if len(temp) > 4:
        if '01' in value and temp[-4] == '10' and temp[-1] == '13':
            return True
        elif int(temp[4]) - int(temp[0]) == 4:
            return True
        elif len(temp) > 5:
            if int(temp[5]) - int(temp[1]) == 4:
                return True
        elif len(temp) > 6:
            if  int(temp[6]) - int(temp[2]) == 4:
                return True
    return False

def check6ThreeOfAKind(hand): #Working
    value = []
    for each in hand:
        value.append(each[0])
    max = 0
    for each in cardValues:
        temp = value.count(each)
        if temp > max:
            max = temp
    if max > 2:
        return True
    else:
        return False

def check7TwoPair(hand): #Working
    value = []
    pairs = {}
    for each in hand:
        value.append(each[0])
    max = 0
    for each in cardValues:
        temp = value.count(each)
        if temp > 1:
            pairs[each[0]] = True
    if len(pairs) > 1:
        return True

def check8Pair(hand): #Working
    value = []
    for each in hand:
        value.append(each[0])
    max = 0
    for each in cardValues:
        temp = value.count(each)
        if temp > max:
            max = temp
    if max > 1:
        return True
    else:
        return False

def check9HighCard(hand):
    return True





wait = raw_input("Press Enter to reset all data.")

try:
    import MySQLdb
except:
    pass

try:
    # Open database connection
    db = MySQLdb.connect("localhost","webserver","password","cards" )
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # execute SQL query using execute() method.
    cursor.execute("DELETE FROM players")
    data = cursor.fetchone()
    print "%s " % data
    cursor.execute("DELETE FROM community_cards")
    data = cursor.fetchone()
    print "%s " % data
    cursor.execute("DELETE FROM player_cards;")
    data = cursor.fetchone()
    print "%s " % data
    # disconnect from server
    db.commit()
    db.close()
except:
    pass

print ""
print "Welcome to the poker game."
wait = raw_input("Enter the players now!")
while True:
    gameNumber = gameNumber + 1
    print
    print "You are playing game #", gameNumber

    try:
        print
        db = MySQLdb.connect("localhost","webserver","password","cards" )
        cursor = db.cursor()
        cursor.execute("DELETE FROM player_cards;")
        cursor.execute("SELECT * FROM players;")
        players = cursor.rowcount
        print "There are currently " , players, " players."
        for player in range(1,players+1):
            for number in range(1,cardsInPlayerHands+1):
                # print gameCards[player,number][1] + gameCards[player,number][0]
                part1 = 'INSERT INTO player_cards (playerID,card) VALUES ('
                part2 = str(player) + ','
                part3 = '"bck")'
                print part1 + part2 + part3
                cursor.execute(part1+part2+part3)
        cursor.execute("DELETE FROM community_cards")
        cursor.execute("INSERT INTO community_cards (Card) VALUES ('bck')")
        cursor.execute("INSERT INTO community_cards (Card) VALUES ('bck')")
        cursor.execute("INSERT INTO community_cards (Card) VALUES ('bck')")
        cursor.execute("INSERT INTO community_cards (Card) VALUES ('bck')")
        cursor.execute("INSERT INTO community_cards (Card) VALUES ('bck')")
        db.commit()
        db.close()
    except:
        pass


    deckOfCards = []

    for suit in cardSuits:
        for value in cardValues:
            deckOfCards.append([value,suit])

    gameCards = {}
    for player in range(1,players+1):
        for number in range(1,cardsInPlayerHands+1):
            # print player, number
            individualCard = random.choice(deckOfCards)
            gameCards[player,number] = individualCard
            deckOfCards.remove(individualCard)
    wait = raw_input("Hit enter to deal cards to the players!")

    try:
        print
        db = MySQLdb.connect("localhost","webserver","password","cards" )
        cursor = db.cursor()
        cursor.execute("DELETE FROM player_cards;")
        # cursor.execute("SELECT * FROM players;")
        # players = curson.rowcount
        # print players
        # players = 3
        for player in range(1,players+1):
            for number in range(1,cardsInPlayerHands+1):
                # print gameCards[player,number][1] + gameCards[player,number][0]
                part1 = 'INSERT INTO player_cards (playerID,card) VALUES ('
                part2 = str(player) + ',"'
                part3 = gameCards[player,number][1] + gameCards[player,number][0]
                part4 = '");'
                print part1 + part2 + part3 + part4
                cursor.execute(part1+part2+part3+part4)
        db.commit()
        db.close()
        print "The players have their cards."
    except:
        pass

    for player in range(1,players+1):
        print [gameCards[player,1]] + [gameCards[player,2]]

    communityCards = []

    ######################
    #test cards
    ######################
    playerHandStatus = {}

    def checkHands():
        for player in range(1,players+1):
            if check0RoyalFlush([gameCards[player,1]] + [gameCards[player,2]] + communityCards):
                # print "player:",player,"has check0RoyalFlush"
                playerHandStatus[player] = "Royal Flush"
            elif check1StraightFlush([gameCards[player,1]] + [gameCards[player,2]] + communityCards):
                # print "player:",player,"has check1StraightFlush"
                playerHandStatus[player] = "Straight Flush"
            elif check2FourOfAKind([gameCards[player,1]] + [gameCards[player,2]] + communityCards):
                # print "player:",player,"has check2FourOfAKind"
                playerHandStatus[player] = "Four of a Kind"
            elif check3FullHouse([gameCards[player,1]] + [gameCards[player,2]] + communityCards):
                # print "player:",player,"has check3FullHouse"
                playerHandStatus[player] = "Full House"
            elif check4Flush([gameCards[player,1]] + [gameCards[player,2]] + communityCards):
                # print "player:",player,"has check4Flush"
                playerHandStatus[player] = "Flush"
            elif check5Straight([gameCards[player,1]] + [gameCards[player,2]] + communityCards):
                # print "player:",player,"has check5Straight"
                playerHandStatus[player] = "Straight"
            elif check6ThreeOfAKind([gameCards[player,1]] + [gameCards[player,2]] + communityCards):
                # print "player:",player,"has check6ThreeOfAKind"
                playerHandStatus[player] = "Three of a Kind"
            elif check7TwoPair([gameCards[player,1]] + [gameCards[player,2]] + communityCards):
                # print "player:",player,"has check7TwoPair"
                playerHandStatus[player] = "Two Pair"
            elif check8Pair([gameCards[player,1]] + [gameCards[player,2]] + communityCards):
                # print "player:",player,"has check8Pair"
                playerHandStatus[player] = "Pair"
            elif check9HighCard([gameCards[player,1]] + [gameCards[player,2]] + communityCards):
                # print "player:",player,"has check9HighCard"
                playerHandStatus[player] = "High Card"
        try: #to save this to the database
            db = MySQLdb.connect("localhost","webserver","password","cards")
            cursor = db.cursor()
            for player in range(1,players+1):
                part1 = "UPDATE players SET hand="
                part2 = '"' + playerHandStatus[player] + '"'
                part3 = " WHERE playerID=" + str(player) + ";"
                print part1 + part2 + part3
                cursor.execute(part1+part2+part3)
            db.commit()
            db.close()
            print "The players have their card status."
        except:
            print "Cannot save to the database"
    checkHands()





    # Flop
    wait = raw_input("Here comes the Flop. Hit enter ")
    # Card 1
    individualCard = random.choice(deckOfCards)
    communityCards.append(individualCard)
    deckOfCards.remove(individualCard)
    # Card 2
    individualCard = random.choice(deckOfCards)
    communityCards.append(individualCard)
    deckOfCards.remove(individualCard)
    # Card 3
    individualCard = random.choice(deckOfCards)
    communityCards.append(individualCard)
    deckOfCards.remove(individualCard)

    try:
        print
        db = MySQLdb.connect("localhost","webserver","password","cards" )

        cursor = db.cursor()
        cursor.execute("DELETE FROM community_cards")
        for each in communityCards:
            print each[1] + each[0]
            part1 = 'INSERT INTO community_cards (Card) VALUES ("'
            part2 = each[1] + each[0]
            part3 = '");'
            print part1 + part2 + part3
            cursor.execute(part1+part2+part3)
        cursor.execute("INSERT INTO community_cards (Card) VALUES ('bck')")
        cursor.execute("INSERT INTO community_cards (Card) VALUES ('bck')")
        db.commit()
        db.close()
    except:
        pass
    checkHands()

    # Turn
    wait = raw_input("Time for the Turn. Hit enter ")
    # Card 4
    individualCard = random.choice(deckOfCards)
    communityCards.append(individualCard)
    deckOfCards.remove(individualCard)

    try:
        print
        db = MySQLdb.connect("localhost","webserver","password","cards" )

        cursor = db.cursor()
        cursor.execute("DELETE FROM community_cards")
        for each in communityCards:
            print each[1] + each[0]
            part1 = 'INSERT INTO community_cards (Card) VALUES ("'
            part2 = each[1] + each[0]
            part3 = '");'
            print part1 + part2 + part3
            cursor.execute(part1+part2+part3)
        cursor.execute("INSERT INTO community_cards (Card) VALUES ('bck')")
        db.commit()
        db.close()
    except:
        pass
    checkHands()


    # River
    wait = raw_input("And the River. Hit enter ")
    # Card 5
    individualCard = random.choice(deckOfCards)
    communityCards.append(individualCard)
    deckOfCards.remove(individualCard)


    try:
        print
        db = MySQLdb.connect("localhost","webserver","password","cards" )

        cursor = db.cursor()
        cursor.execute("DELETE FROM community_cards")
        for each in communityCards:
            print each[1] + each[0]
            part1 = 'INSERT INTO community_cards (Card) VALUES ("'
            part2 = each[1] + each[0]
            part3 = '");'
            print part1 + part2 + part3
            cursor.execute(part1+part2+part3)
        db.commit()
        db.close()
    except:
        pass
    checkHands()
    debugPrint ("The player cards.")
    for player in range(1,players+1):
        for number in range(1,cardsInPlayerHands+1):
            print gameCards[player,number],
        print
    debugPrint ("The community cards.")
    for each in communityCards:
        print each ,
    print

    wait = raw_input("That's the game. Press enter to continue.")
