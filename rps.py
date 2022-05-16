import random
game_on = True

actions = ["rock" , "scissors" , "paper"]

# first one to get 2 out of 3 wins

while game_on != False:        
    
    i = 1
    while i <= 3:
    
        player_action = input ( " please choose your action ; rock , scissors or paper")
        machine_action = random.choice(actions )
        print (f"player' choice = {player_action} , computer's choice = {machine_action}")
        
        if player_action == "rock":
            
            if machine_action == "scissors":
                print ("rock smashes scissors , you Win!")
                game_on = False
                i += i

            elif machine_action == "paper":    
                print ("paper covers rock , you lose!")
                game_on = False
                i += i
        
        if player_action == "scissors":
            
            if machine_action == "paper":
                print ("scissors cuts paper, You Win!")
                game_on = False
                i += i
            
            elif machine_action == "rock":
                print ("rock smashes scissors , you Lose!")
                game_on = False
                i += i
        
        if player_action == "paper":
            
            if machine_action == "rock":
                print ("paper covers rock , You Win!")
                game_on = False
                i += i      
            
            elif machine_action == "scissors":
                print ("scissors cuts paper , You Lose!")
                game_on = False
                i += i   
        
        if player_action == machine_action:
            print (f"Both players selected {player_action}. It's a tie!")
            
            again = input ("do u want to play again, y or n")
            if again == "no":
                game_on = False
                i += i  
            
            elif again == "yes":
                game_on = True