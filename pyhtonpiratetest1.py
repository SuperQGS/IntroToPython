global gold
global crew
global cannonballs
from random import randint
food = 50
crew = 50
gold = 50
cannonballs = 50
def check():
    print("")
    if food < 1:
        print("You run out of food and a mutiny occurs! Game Over")
        raw_input("")
    elif crew < 1:
        print("You don't have a crew! Game Over")
        raw_input("")
    elif gold < 1:
        print("You have no gold and a mutiny occurs! Game Over")
        raw_input("")
    elif gold > 99:
        print("You have earned 100 gold! You Win!")
        raw_input("")
    else:
        encounter()

def encounter():
    
    
    
    ran = randint(1, 3)
    if ran == 1:
        ship()
    if ran == 2:
        town()
    if ran == 3:
        sea()

def ship():
    if cannonballs < 1:
        print("You encounter a hostile ship and don't have enough cannonballs to defend yourself! Game Over!")
    else:
        ship_confirm = raw_input("You encounter a hostile ship! Would you like to engage in battle? : ")
        if ship_confirm == "Y":
            
            shipran = randint(1, 3)
            if shipran == 3:
                global gold
                global crew
                global cannonballs
                
                gold += 20
                cannonballs += 5
                print(supplies %(food, crew, gold, cannonballs))
                print("You won the battle and gained supplies! (+20 gold  +5 cannonballs)")
                print("")
                check()
            else:
                global gold
                global crew
                global cannonballs
                gold -= 10
                crew -= 10
                cannonballs -= 10
                print(supplies %(food, crew, gold, cannonballs))
                print("You lost the battle and the hostile crew plunders your ship. (-10 gold  cannonballs  and crew)")
                print("")
                check()
        else:
            print("You run away from the battle.")
            check()
def town():
    print(supplies %(food, crew, gold, cannonballs))
    town_confirm = raw_input("You encounter a friendly town. Would you like to trade? (Y = -20 gold and +20 food): ")
    if town_confirm == "Y":
        global gold
        global food
        gold -= 20
        food += 20
        print("You buy 20 food for 20 gold!")
        check()
    else:
        print("You don't buy anything")
        check()
def sea():
    global food
    food -= 10
    print(supplies %(food, crew, gold, cannonballs))
    sea_confirm = raw_input("You encounter a storm and lose supplies! (-10 food) Continue? : ")
    check()
    


print("")
print("Hello! Welcome to the super duper test python pirate adventure of awesomeness and treasure!")
print("Made by SuperQGS at qgsoftware.github.io")
supplies = ("""
food: %s
crew: %s
gold: %s
cannonballs: %s""")
print(supplies %(food, crew, gold, cannonballs))

confirm = raw_input("""
The empty sea lies before you  captain. Sail on? (Y/N) : """)

if confirm == "Y":
    print("Onwards!")
    check()
elif confirm == "QGJERHY":
    print("""
                                                                       @@@@@               
                                                                     @@     @              
                                                                   @@      @@@@@           
                                                                  @       @@    @          
                                                                 @   @@  @@ @@@@@@@@@      
                                                                 @   @@  @ @.........@@@   
                                                                @        @ @.@........@.@  
                                                                @        @ @..@@@.......@  
                                                                @        @ @.....@@@@@@@@  
                                                                @        @ @...........@   
                                                                @        @@ @@@@@@@@@@@    
                                                                @         @@    @  @       
                                                                 @         @@@@@@  @       
                                                                 @           @;;@  @       
                                                                 @           @;;;@ @       
                                  @@@@@@@@@@                      @         @ @;;;@         
   @@@@@@  @@@@@@                @    @@;;;@@@                    @         @  @;;@        
  @     @@@@     @                @    @@;;;;@@@                  @         @   @;@        
  @              @                 @    @;;;;@@ @                 @        @;@   @         
  @              @                  @   @;;;;;@  @               @        @;;@  @          
   @@          @@                    @  @;;;;;@   @              @        @;;;@@           
     @        @                      @  @;;;;;@   @              @         @;;@@           
      @      @                       @  @;;;;@@    @             @         @@@             
       @    @                       @   @;;;;@     @            @         @                
       @    @                       @   @;;;;@     @            @         @                
        @  @                       @   @@;;;@@      @           @         @                
        @  @                      @    @;;;;@       @          @         @                 
        @  @                     @  @@@@@@@@@@@     @          @         @                 
        @   @                 @@@@@@           @@@@@@         @          @                 
        @   @@@           @@@                       @@@    @@           @                 
         @      @@@   @@@@@                             @@@@            @                  
          @        @@@                                                  @                  
           @@                                                          @                   
             @@@                                                       @                   
                @        @     @                                      @                    
                 @@      @     @                                      @                    
                   @@   @     @@                                     @                     
                     @@@      @                       @     @      @@                      
                      @      @                        @     @    @@                        
                    @@       @@@@                    @      @  @@                          
                 @@@      @@@   @@@                 @       @@@                            
           @@@@@@     @@@@@        @@@@@@@         @       @                               
             @@@@@@@@@                   @@@@@@@@@       @                                 
                                              @@@      @@@                                 
                                         @@@@@     @@@@@                                   
                                          @@@@@@@@@                                        
    """)
    print("""
       _ ______ _____  _    ___     __
      | |  ____|  __ \| |  | \ \   / /
      | | |__  | |__) | |__| |\ \_/ / 
  _   | |  __| |  _  /|  __  | \   /  
 | |__| | |____| | \ \| |  | |  | |   
  \____/|______|_|  \_\_|  |_|  |_| 
    """)
    raw_input("")
else:
    print("You do nothing to lead your crew  andt they kill you after the mutiny. Play the game dummy!")
    raw_input("")