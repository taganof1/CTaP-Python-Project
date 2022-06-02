cards = ['ace', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king']

card=int(input("Pick a number of card from deck of 52"))
if card >= 1 and card < 13:
    print("Spades")
    print(cards[card - 1])
elif card >= 14 and card < 26:
    print("Hearts")
    card = card - 14
    print(cards[card -1])  
elif card > 27 and card < 39:
    print("Diamonds")
    card = card - 27
    print(cards[card])
elif card > 40 and card < 52:
    print("Clubs")
    card = card - 40
    print(cards[card])