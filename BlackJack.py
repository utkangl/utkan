import random
playing = True
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        
        return self.rank + ' of ' + self.suit
    
class Deck:
    
    def __init__(self):
        
        self.deck = [] # boş bir deste yaratıyoruz
        
        for suit in suits:
            for rank in ranks: 
                new_created_cards = (Card(suit, rank)) # card class ını cagirarak kart objelerini yaratıyoruz
                self.deck.append(new_created_cards) # kart objelerini yarattığınız boş desteye ekliyoruz
                
    def shuffle(self):
        random.shuffle(self.deck) # kartları karıştırıyoruz
        
    def deal(self):
        single_card = self.deck.pop() # bir kartı desteden çekiyoruz
        return single_card
        
class Hand:
        def __init__(self):
            self.cards = [] # elimize boş bir deste veriyoruz
            self.value = 0 # toplam değer sıfır ile başlıyor
            self.aces = 0 # as sayısını tutuyoruz
           
        def add_card_to_hand(self,card):
            
            self.cards.append(card) # kartı elimize ekliyoruz
            self.value += values[card.rank] # kartların değerini topluyoruz
            if card.rank == "ace": # as varsa as sayısına 1 ekliyoruz
                self.aces += 1
        # ilk baaşta asın değerini 11 olarak tanımladığımız için eğer elimizdeki kartların toplam değeri 21den fazlaysa ası 1 olarak kullanmak için değerini 10 eksiltiyoruz                        
        def adjust_for_ace(self):
            while self.value > 21 and self.aces:
                self.value -= 10 
                self.aces -= 1 

class Chips:
    
    def __init__(self):
        self.total = 100 # elimizdeki toplam parayı 100 çip olarak başlatıyoruz
        self.bet = 0 # yatırılan bahisi sıfır olarak başlatıyoruz
        
    def win_bet(self):
        self.total += self.bet
            
    def lose_bet(self):
        self.total -= self.bet
        
def take_bet(chips):
    while True:
        try: chips.bet = int(input('How many chips would you like to bet? '))

        except ValueError: print('Sorry, a bet must be an integer!')
        
        else :
            if chips.bet > chips.total:
                print(" sorry, you dont have enough chips")
                
            else: break
            
def hit(deck,hand):
    
    hand.add_card_to_hand(deck.deal()) # deck class ındaki deal ve hand classındaki add_card_to_hand fonksiyonlarını kullanarak oyuncu kart istediğinde desteden kart çekip oyuncunun eline ekliyorz 
    hand.adjust_for_ace()
    
def hit_or_stand(deck,hand):
    
    global playing
    
    while True:
        
        x = input("Would you like to Hit or Stand? Enter Y or N") # oyuncu kart almak istiyor mu soruyoruz
        
        if x == "Y":
            hit(deck,hand) # istiyorsa yukarda tanımladığımız kart çekme fonksiyonunu çağırıyoruz
            
        elif x == "N":
            print ("player Stands, Dealers turn")
            playing = False  # istemiyorsa yerşnde kalıyor ve sıra kurpiyere geçior
            
        else: 
            print ("sorry try again")
            continue
        break
        
def show_some(player,dealer): # başta kurpiyerin 1 kartı oyuncunun ise tüm kartları açılır
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):  # el bitince tüm kartlar gösterilir
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)
        
def player_lost(player,dealer,chips):
    print ("The Player Has Lost")
    chips.lose_bet()

def player_win(player,dealer,chips):
    print ("The Player Has Won")
    chips.win_bet()
    
def dealer_lost(player,dealer,chips):
    print ("The Dealer Has Lost")
    chips.win_bet()
    
def dealer_win(player,dealer,chips):
    print ("The Dealer Has Won")
    chips.lose_bet()
    
def tied(player,dealer):
    print ("Dealer and Player tied! It's a push.")
        
while True:
    
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')

    deck = Deck()    # desteyi yaratma fonksiyonu
    deck.shuffle()   # desteyi karıştırma fonksiyonu
    
    player_hand = Hand()   # oyuncunun elini oluşturuyoruz
    player_hand.add_card_to_hand(deck.deal()) #oyuncuya 1 kart veriyoruz
    player_hand.add_card_to_hand(deck.deal()) # oyuncuya 2. kartı veriyoruz        
    
    dealer_hand = Hand()   # kasanın elini oluşturuyoruz
    dealer_hand.add_card_to_hand(deck.deal()) # kasaya bir kart veriyoruz
    dealer_hand.add_card_to_hand(deck.deal()) # kasaya 2. kartını veriyoruz 
    
    player_chips = Chips() # oyuncunun çiplerini oluşturduğumuz class ı çağırıyoruz, class ın içinde default 100 çip verdik
    take_bet(player_chips) # oyuncudan bahis miktarını seçmesini isteyen fonksiyonu çağırıyoruz
    
    show_some(player_hand , dealer_hand)
    
    while playing: # playing = True olarak en başta atamıştık
        hit_or_stand(deck,player_hand) #oyuncuya tekrar kart seçmek istiyor mu soruyoruz
        
        show_some(player_hand , dealer_hand) # ellerin son durumunu tekrar gösteriyoruz (kasanın 1 oyuncunu 2 kartı açılıyor)
        
        if player_hand.value > 21: # oyuncu 21 i geçtiyse kaybediyor, oyun biter
            player_lost(player_hand , dealer_hand , player_chips)
            break
        
    if player_hand.value <= 21: # oyuncu kaybetmediyse kasa minimum 17 olana kart çekiyor
        while dealer_hand.value < 17:
            hit(deck , dealer_hand)
            
        show_all(player_hand , dealer_hand) # tüm kartları göster
        
        # diğer kazanma/kaybetme durumlarını kontrol ediyoruz
        
        if dealer_hand.value > 21: dealer_lost(dealer_hand , player_hand , player_chips)    # kasa 21i geçerse kaybeder
        
        elif dealer_hand.value < player_hand.value: dealer_lost(dealer_hand , player_hand , player_chips) # kasa 21 e oyuncudan daha uzaksa kaybeder
        
        elif dealer_hand.value > player_hand.value: dealer_win(dealer_hand , player_hand , player_chips) # kasa 21 e oyuncudan daha yakınsa kazanır
        
        else: tied(player_hand, dealer_hand)
        
        print ( f"Total Chip The Player Has İs Equal to: {player_chips.total} ") # oyun sonunda oyuncuda kalan çip sayısını yazdırıyoruz
        
        one_more = input ("do you want to play another round?, YES or NO \n") 
        
        if one_more == "YES" : playing = True
        elif one_more == "NO" : 
            print("Thanks for the game")
            break