#!/usr/bin/python
import random

gameNumber = 0
players = 0
cardsInPlayerHands = 2

wait = raw_input("Press Enter to reset all data.")

try:
    import MySQLdb
    print ""
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
        print players
        for player in range(1,players+1):
            for number in range(1,cardsInPlayerHands+1):
                # print gameCards[player,number][1] + gameCards[player,number][0]
                part1 = 'INSERT INTO player_cards (playerID,card) VALUES ("bck");'
                # print part1 + part2 + part3 + part4
                cursor.execute(part1+part2+part3+part4)
        db.commit()
        db.close()
        cursor.execute("DELETE FROM community_cards")
        cursor.execute("INSERT INTO community_cards (Card) VALUES ('bck')")
        cursor.execute("INSERT INTO community_cards (Card) VALUES ('bck')")
        cursor.execute("INSERT INTO community_cards (Card) VALUES ('bck')")
        cursor.execute("INSERT INTO community_cards (Card) VALUES ('bck')")
        cursor.execute("INSERT INTO community_cards (Card) VALUES ('bck')")
    except:
        pass

    # cardSuits = ['hearts','clubs','spades','diamonds']
    cardSuits = ['h','c','s','d']
    # cardValues = ['two','three','four','five','six','seven','eight','nine','ten','jack','queen','king','ace']
    cardValues = ['02','03','04','05','06','07','08','09','10','11','12','13','01']
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

    try:
        print
        db = MySQLdb.connect("localhost","webserver","password","cards" )
        cursor = db.cursor()
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
                # print part1 + part2 + part3 + part4
                cursor.execute(part1+part2+part3+part4)
        db.commit()
        db.close()
        print "The players have their cards."
    except:
        pass

    communityCards = []

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
    wait = raw_input("And that is the game!")


    # for each in communityCards:
    #     print each[1] + each[0]
    #     part1 = 'INSERT INTO community_cards (Card) VALUES ("'
    #     part2 = each[1] + each[0]
    #     part3 = '");'
    #     print part1 + part2 + part3

    # Check for Winners

    # for player in range(1,players+1):
    #     hand = []
    #     # print player
    #     # print gameCards[player,1]
    #     hand.append(gameCards[player,1])
    #     # print gameCards[player,2]
    #     hand.append(gameCards[player,2])
    #     for each in communityCards:
    #         hand.append(each)
    #     # print hand
    #     for each in hand:
    #         print each
    # 1. Royal flush
    # A, K, Q, J, 10, all the same suit.
    # A K Q J T
        # royalFlush = False





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
    wait = raw_input("That's the game. Press enter to continue.")
