def card_simulation():
    import random
    suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
    ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    deck = []
    complete = 1
    attempts = 0
    for i in range(len(ranks)):
        for j in range(len(suits)):
            deck.append((suits[j], ranks[i]))
    while complete != 0:
        attempts += 1          
        random.shuffle(deck) 
        hand = [] 
        for number in range(5):
            suit, rank = deck[number]
            hand.append((suit, rank))
        suit_match = hand[0][0]
        if all(card[0] == suit_match for card in hand):
            hand_ranks = {card[1] for card in hand}
            if hand_ranks == {1, 10, 11, 12, 13}:
                complete = 0

    return attempts

print(f"It took {card_simulation()} attempts to get a royal flush.")