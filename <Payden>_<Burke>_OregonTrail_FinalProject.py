#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 14:40:53 2017

@author: PaydenBurke
"""
#Payden Burke
#Partner Petter Reistad
# TA Shirly M
#Final Project
# 6, December 2017
'''Summary of this program: This program's purpose is for the game the old timey game, The Oregon Trail. 
This game uses much of what was learned in the computer programming class the art of computational thinking, CSCI 1200.
The game goes through many rounds with the objective of making it to Oregon safely.
The user must use his or her whits as they conquer raiders and thieves, broken wagons, sickness and much more.
This game was coded in the language of python with the purpose of entertainment to the consumer.
Enjoy!'''

#we use import random mainly for the misfortune and puzzle functions
import random

#Get all players' names
MainPlayer=input("Hey traveler, you and your 4 other family members look ready to start your journey on the Oregon trail! Before you go let us know your name: ")
Companion1=input("What would you like to call your first family member? ")
Companion2=input("What would you like to call your second family member? ")
Companion3=input("What would you like to call your third family member? ")
Companion4=input("What would you like to call your fourth family member? ")

#Totalling
Travel_Party_Members=5

#Health of player with companions
Health_MainPlayer = 100
Health_Companion1 = 100
Health_Companion2 = 100
Health_Companion3 = 100
Health_Companion4 = 100

#Store items
Money = 1600
Food = 0
Oxen = 0
Medical_Kit=0
Parts_Wagon = 0
Bullets = 0

#Bill when visiting store
Amount_Store=0

#Time
Days = 0

#Distance traveled
Distance = 0

#While the game is running, End_Game_Now equals 0.
End_Game_Now = 0


def Welcome():
    print("Welcome to the Oregon Trail Game! You will be starting your journey on 03/28/1847. You have 247 days to complete the journey, each turn is 14 days.")
    '''Initial welcoming remarks to the game called at the start of the game used only once'''

#this function is used as the store function it is called whenever the player wants to make a purchase for their journey
def VisitStore():
    global Amount_Store
    global Money
    global End_Game_Now
    
    print("Welcome to the store.")
    print(' ')
    print("You have $1600 to spend for the trip. The money can be spent on the following items: ")
    print(' ')
    print("- Oxen: You must spend between $100 and $200 on oxens. The more you purchase, the faster you will travel.")
    print("- Food: More food means less chance of running out, and greater chance of staying healthy..")
    print("- Bullets: To battle attacks by bandits, and to hunt for food, bullets is needed.")
    print("There are also a few other items that you can buy, like medical kits and wagon parts.")
    print(' ')
    print("You can spend all of your money now or you can save some of your money to spend in forts along the way.")
    print(' ')

    Store_Food()
    Store_Oxen()
    Store_Bullets()
    Other_VisitStore()
    Money=Money-Amount_Store
    
    print("You have spent: ", Amount_Store)
    print("You have : ", Money, "left.")
    print(' ')
    print("Have a good trip, and good luck!")
    End_Game_Now = 0
    


def Store_Food():
    '''Here you can buy food for the trip. Gets called by the store function.'''
    global Amount_Store
    global Food
    global Money
    
    print("We recommend that you purchase at least 200 pounds of food per person. The price is half a dollar per pound.")
    
    Food_TotalCost=0
    Food_Pounds=input("How many pounds of food do you want to buy? ")
    Food_Pounds=int(Food_Pounds)
    Food_TotalCost=Food_Pounds * 0.5
    Amount_Store=Amount_Store + Food_TotalCost
    Food=Food + Food_Pounds
    
    print("Thank you for your purchase! ", Food_Pounds, "of food has been loaded onto your wagon")
    return Amount_Store


def Other_VisitStore():
    '''Gets called in store. Here you can buy medical kits and wagon parts.'''
    
    global Medical_Kit
    global Parts_Wagon
    global Money
    global Amount_Store
    '''Calls global variables.'''
    
    Parts_Wagon=input("Your Wagon may have a few parts fall off on your journey. Do not worry however because I am selling parts for $10 a piece (What a steal)! How many would you like to buy?" )
    Parts_Wagon=int(Parts_Wagon)
    Parts_Cost=Parts_Wagon * 10
    print(' ')
    Medical_Kit=input("If a traveler gets sick, medical kits are essential to make them recover. How many would you like to buy?")
    Medical_Kit=int(Medical_Kit)
    print(' ')
    Kit_Cost=Medical_Kit * 15
    Amount_Store=Amount_Store + Parts_Cost + Kit_Cost

    print("Thank you for your purchases! And Good Luck On Your Journey!")
    return Amount_Store

    
def Store_Oxen():
    '''Here you can buy oxens, necessary for the progress of the travel of your journey.'''
    global Money
    global Oxen 
    global Amount_Store
    
    Yoke_of_Oxens=input("How many yokes of oxen would you like to purchase? (A yoke consists of two oxens, you can buy a maximum of 5 yokes!)")
    Yoke_of_Oxens=int(Yoke_of_Oxens)
    
    Oxen_price=40
    
    if Yoke_of_Oxens <3 and Yoke_of_Oxens>0:
        Yoke_of_Oxens=int(input("You must buy minimum 3 yokes. How many yokes would you like to buy?"))
        #Asks the user another time
    if Yoke_of_Oxens >3 and Yoke_of_Oxens <=5:
        Oxen_price=Yoke_of_Oxens * 40
    if Yoke_of_Oxens >5:
        Yoke_of_Oxens=input("You don't need more than 10 oxens. 5 yokes should be enough.")
        #Asks the user another time
    
    Amount_Store=Amount_Store + Oxen_price
    Money=Money-Amount_Store
    Oxen=Oxen +(Yoke_of_Oxens*2)
    
    print("Sounds good. Happy to do business with you!")
    print("You have", Money, " dollars left.")
    return Amount_Store


def Store_Bullets():
    ''''Gets called in store. Here you can buy bullets.'''
    global Amount_Store
    global Bullets
    global Money
    '''Calling global variables.'''
    
    Bullets=input("How many boxes of bullets (each containing 20) would you like to purchase? (Each box costs $2)" )
    #ask user how many boxes he or she wants
    
    Bullets=int(Bullets)
    Bullets=Bullets*2
    cost_of_Bullets=Bullets * 2
    Amount_Store=Amount_Store + cost_of_Bullets
    Bullets=Bullets + Bullets
    print(' ')
    print("Thank you for your purchase!")
    return Amount_Store


def Turn():
    '''In this function the user gets asked what they want to do for their current turn.'''
    ToDo = str(input('Get ready for another turn. What would you like to do? You can continue your trip (1), rest (2), hunt (3) or quit the game (4). Please the number listed after your preferred choice.'))
    if ToDo == '1':
        Continue_Trip()
    elif ToDo == '2':
        Rest_During_Trip()
    elif ToDo == '3':
        Hunt_Animals()
    elif ToDo == '4':
        End_Game_NowGame()


def Status_Update():
    '''This function shows a status update to many of the recorded data throughout the game 
    such as player health, money and even time.'''
    
    global Bullets
    global Oxen
    global Parts_Wagon
    global Medical_Kit
    global Health_MainPlayer
    global Health_Companion1
    global Health_Companion2
    global Days
    global Travel_Party_Members
    global Health_Companion3
    global Health_Companion4
    global Food
    '''Calls global variables'''
    
    misc = Parts_Wagon + Medical_Kit
    if Food >1000:
        Food=1000
    print('In total, you have ', misc, ' wagon parts and medical kits.')
    print('In total, you have ',Food, 'pounds of food.')
    print('In total, you have ',Bullets, 'bullets left.')
    print('In total, you have ',Oxen, ' oxen left.')
    print(' ')
    print(MainPlayer,' has',  Health_MainPlayer, '% health.')
    print(Companion1, ' has',Health_Companion1, '% health.')
    print(Companion2, ' has', Health_Companion2, '% health.')
    print(Companion3, ' has',Health_Companion3, '% health.')
    print(Companion4, ' has',Health_Companion4, '% health.')
    print(' ')
    print('In total, you have now traveled ', Distance , 'miles.')
    print('You have traveled for ', Days, 'days.')
    print(' ')


def Rest_During_Trip():
    '''This function makes the travel party rest for one to three days.'''
    
    global Health
    global Health_MainPlayer
    global Health_Companion1
    global Health_Companion2
    global Days
    global Travel_Party_Members
    global Health_Companion3
    global Health_Companion4
    global Food
    '''Calling the global variables.'''
    
    if Health_Companion2 > 0:
        Health_MainPlayer = 100
    if Health_Companion3 > 0:
        Health_MainPlayer = 100
    if Health_Companion4 > 0:
        Health_MainPlayer = 100
    if Health_MainPlayer > 0:
        Health_MainPlayer = 100
    if Health_Companion1 > 0:
        Health_MainPlayer = 100

    DaysRest = int(1 + (2 * random.random()))
    Days = Days + DaysRest
    print(' ')
    print('You spent', DaysRest, 'days resting.')
    EatFood = (Travel_Party_Members * 3 * DaysRest)
    Food = Food - EatFood
    print('During the rest, you consumed', EatFood, 'pounds of food.')
    if 0 < Health_MainPlayer < 100 or 0 < Health_Companion1 < 100 or 0 < Health_Companion2 < 100 or 0 < Health_Companion3 < 100 or 0 < Health_Companion4 < 100:
        print(' ')
        print('All traveling party members that were sick are now Recoveryed')


def Continue_Trip():
    '''This function makes the traveling party continue their trip, traveling from 70 to 140 miles.'''
    global Travel_Party_Members
    global Days
    global Food
    global Distance
    '''Calling the global variables.'''
    
    Days = Days + 14
    Food_loss=int(Travel_Party_Members*(14*3))
    Food=int(Food)
    Food = Food - Food_loss
    TurnDistance = 70 + int(70 * random.random())
    Distance = Distance + TurnDistance
    Landmarks()
    

def Hunt_Animals():
    '''This function makes player hunt food.'''
    
    global Days
    global Bullets
    global Health_Companion1
    global Health_Companion2
    global Health_Companion3
    global Health_Companion4
    global Health_MainPlayer
    global Food
    '''Calls global variables.'''
    
    CURRENT_Health_MainPlayer = Health_MainPlayer
    CURRENT_Health_Companion1 = Health_Companion1
    CURRENT_Health_Companion2 = Health_Companion2
    CURRENT_Health_Companion3 = Health_Companion3
    CURRENT_Health_Companion4 = Health_Companion4
    
    bool = False
    '''Sets it.'''
    Food_Total = Food
    '''Enables changes in food.'''
    bullet_count = Bullets
    current_day = Days
    
    number = random.randrange(0,101)
    '''Meat and meal.'''
    animal = 0    
    #Number of food they can hunt
    
    for animals in range(1):
        number = random.randrange(0,101)
        if number < 50:
            print("You have encountered a rabbit.")
            animal = animal + 2
            bool = True
        number = random.randrange(0,101)
        if number <= 25:
            print("You have encountered a fox.")
            animal = animal + 5
            bool = True 
        number = random.randrange(0,101)
        if number <= 20:
            deer_weight = random.randrange(35,61)    
            print("You have encountered a deer.")
            animal = animal + deer_weight
            bool = True
        
        number = random.randrange(0,101)
        if number <= 10:
            bear_weight = random.randrange(100,301)
            print("You have encountered a bear.")
            animal = animal + bear_weight
            bool = True
        if number <= 5 :
            moose_weight = random.randrange(300,701)
            print ("You have encountered a moose.")
            animal = animal + moose_weight
            bool = True
        
        print(' ')

        decision = input("Would you like to hunt? Yes (1) or no (2).")
        if decision == "1":
            if CURRENT_Health_MainPlayer != 0:
                CURRENT_Health_MainPlayer = 100
            elif CURRENT_Health_Companion1 != 0:
                CURRENT_Health_Companion2 = 100
            elif CURRENT_Health_Companion2 != 0:
                CURRENT_Health_Companion2 = 100
            elif CURRENT_Health_Companion3 != 0:
                CURRENT_Health_Companion3 = 100
            elif CURRENT_Health_Companion4 != 0:
                CURRENT_Health_Companion4 = 100
        
            if bullet_count < 10:
                print("You did not manage to catch anything during your hunt. Better luck next time!")
                current_day == Days + 1
                print(' ')
            else:
                bool = RaiderPuzzle()
                if bool == "True":
                    lost_ammunition = random.randrange(5,31)
                    print(' ')
                    print("Congratulations. The hunt was successful!")
                    Food_Total = Food + animal 
                    print(' ')
                    bullet_count = bullet_count - lost_ammunition
                    print("You acquired ", Food_Total, "pounds of food!")
                    print("You lost ", bullet_count, "bullets!")
                
                elif bool == "False":
                    print(' ')
                    print("You cannot hunt, because you do not have enough bullets.")
                    current_day = Days + 1
                    print(' ')
        
            if decision == "2":
                print("You decided not to hunt.")
                print(' ')
            
        if bool == False:
            print ("You encountered no animals. Better luck with the hunt next time.")
            print(' ')
        
    decision_two = input("How well would you like to eat today? Poorly, moderately or well? ")
    print(' ')
    decision_two = str(decision_two)
    if decision_two == "Poorly" or "poorly":
        print("You chose to eat poorly, resulting in that the group only consumed 10 pounds of food.")
        Food_Total = Food - 10
    elif decision_two == "Moderately" or "moderately":
        print("You chose to eat moderately, resulting in that the group consumed 16 pounds of food.")
        Food_Total = Food - 16
    elif decision_two == "Well" or "well":
        print("You chose to eat well, resulting in that the group consumed 25 pounds of food.")
        Food_Total = Food - 25   
        
    Food_Total = Food
    if Food_Total > 1000:
        Food_Total = 1000
        print(' ')
        print("Unfortunately, the wagon cannot hold more than 1000 pounds of food. You have to leave the excess food.")
        print(' ')


def Misfortune():
    '''Makes a misfortune happen.'''
    
    if End_Game_Now==0:
        num=random.randrange(0,101)
        if num <=6:
            Sickness()
        elif num>6 and num <=12:
            Oxen_Dies()
        elif num>12 and num<=18:
            Thief_Steal()
        elif num>18 and num<=24:
            Wagon_Accident()
        elif num>24 and num <30:
            Weather()

def Sickness():
    '''Makes players sick, and can recover them.'''
    
    global Health_MainPlayer
    global Health_Companion1
    global Health_Companion2
    global Health_Companion3
    global Health_Companion4
    
    global MainPlayer
    global Companion1
    global Companion2
    global Companion3
    global Companion4
    '''Calls all global variables.'''
    
    sick_MainPlayer=random.randrange(0,51)
    print(' ')
    
    if sick_MainPlayer <=10:
        sick_MainPlayer=MainPlayer
        Health_MainPlayer=Health_MainPlayer-50
        if Health_MainPlayer==0:
            End_Game_Now()
    if sick_MainPlayer >10 and sick_MainPlayer <=20:
        sick_MainPlayer=Companion1
        Health_Companion1=Health_Companion1-50
        if Health_Companion1==0:
            print(Companion1, "has died after becoming ill.")
    if sick_MainPlayer >20 and sick_MainPlayer <=30:
        sick_MainPlayer=Companion2
        Health_Companion2=Health_Companion2-50
        if Health_Companion2==0:
            print(Companion2, "has died after becoming ill.")
    if sick_MainPlayer >30 and sick_MainPlayer <=40:
        sick_MainPlayer=Companion3
        Health_Companion3=Health_Companion3-50
        if Health_Companion3==0:
            print(Companion3, "has died after becoming ill.")
    if sick_MainPlayer >40: 
        sick_MainPlayer=Companion4
        Health_Companion4=Health_Companion4-50
        if Health_Companion4==0:
            print(Companion4, "has died after becoming ill.")
            
    sickness=random.randrange(0,61)
    print(' ')
    if sickness <=10: 
        print(sick_MainPlayer,"has gotten typhoid! Rest, hunt, or use a medical kit to make them recover faster!")
    elif sickness >10 and sickness <=20:
        print(sick_MainPlayer,"has gotten cholera! Rest, hunt, or use a medical kit to make them recover faster!")
    elif sickness >20 and sickness <=30:
        print(sick_MainPlayer,"has gotten diarrhea! Rest, hunt, or use a medical kit to make them recover faster!")
    elif sickness >30 and sickness <=40:
        print(sick_MainPlayer,"has gotten measles! Rest, hunt, or use a medical kit to make them recover faster!")
    elif sickness >40 and sickness <=50:
        print(sick_MainPlayer,"has gotten dysentery! Rest, hunt, or use a medical kit to make them recover faster!")
    elif sickness >50 and sickness <=60:
        print(sick_MainPlayer,"has gotten fever! Rest, hunt, or use a medical kit to make them recover faster!")
    Recovery=input("Do you want to use a medical kit? Yes (1) or no (2)")
    if Recovery==1:
        print(sick_MainPlayer, "will be healthy in two days.")
        print(' ')
    if Recovery==2:
        print(sick_MainPlayer, "will be healthy in five days.")
        print(' ')

def Thief_Steal():
    '''Makes a thief steal food'''
    
    global Food
    '''Calls global variable.'''
    
    temp=random.randrange(15,26)
    Food=Food-temp
    print("A thief stole ",temp,"pounds of food from you! ")
    print(' ')
    return Food            

def Weather():
    '''One misfortune function.'''
    global Health_MainPlayer
    global Health_Companion1
    global Health_Companion2
    global Health_Companion3
    global Health_Companion4
    global Days
    '''Calls global variables.'''
    
    num=random.randrange(0,51)
    if num <=10:
        print("You have encountered heavy rains. You have to wait one day before you can continue.")
        Days=Days +1
        Health_MainPlayer=100
        Health_Companion1=100
        Health_Companion2=100
        Health_Companion3=100
        Health_Companion4=100
    if num>10 and num <=20:
        print("You have encountered a large thunderstorm! You have stopped to seek shelter for three days.")
        Days=Days +3
        Health_MainPlayer=100
        Health_Companion1=100
        Health_Companion2=100
        Health_Companion3=100
        Health_Companion4=100
    if num>20 and num <=30:
        print("You have encountered a hail storm! You have stopped to seek shelter for the day.")
        Days +1
        Health_MainPlayer=100
        Health_Companion1=100
        Health_Companion2=100
        Health_Companion3=100
        Health_Companion4=100
    if num>30 and num <=40:
        print("You have encountered a blizzard! You have stopped to seek shelter for three days.")
        Days=Days +3
        Health_MainPlayer=100
        Health_Companion1=100
        Health_Companion2=100
        Health_Companion3=100
        Health_Companion4=100


def Wagon_Accident():
    '''Function that makes the wagon breaks.'''
    
    global Health_MainPlayer
    global Days
    global Food
    global Health_Companion1
    global Health_Companion2
    global Health_Companion3
    global Health_Companion4
    global Parts_Wagon
    '''Calls global functions.'''
    
    Food_loss= Travel_Party_Members *3
    num=random.randrange(0,31)
    if num >=20:
        print("One of your wagon wheels broke! It can be repaired with a wagon part.")
    if num >=10 and num <20:
        print("An axel on your wagon broke! It can be repaired with a wagon part.")
    if num <10:
        print("A wagon tongue broke! It can be repaired with a wagon part.")
    if Parts_Wagon>0:
        response=input("Would you like to repair your wagon? Yes (1) or no (2).")
        if response==1:
            Days+=1
            Parts_Wagon=Parts_Wagon - 1
            Food=Food-Food_loss
            if Health_MainPlayer > 0:
                Health_MainPlayer = 100
            if Health_Companion1 > 0:
                Health_MainPlayer = 100
            if Health_Companion2 > 0:
                Health_MainPlayer = 100
            if Health_Companion3 > 0:
                Health_MainPlayer = 100
            if Health_Companion4 > 0:
                Health_MainPlayer = 100
        if response==2:
            End_Game_Now()
    else:
        End_Game_Now()  

def Oxen_Dies():
    '''Oxen dies.'''
    
    global Oxen
    '''Calls global variable.'''
    
    print("One of your oxen died... You still have oxen left, with the progress will be slower now." )
    Oxen = Oxen - 1
    print(' ')
    if Oxen==0:
        End_Game_Now()

def RaiderPuzzle():
    '''This function can be called upon  to win a hunt, or fight off raiders. The function generates a random number between 1-10, the user tries to guess the number with 3 attempts. If the user guesses the number they win, if they can not guess the number in the given 3 attempts they lose.'''
    print('To win, you must guess the right number between 1 and 10. Choose wisely you only have 3 shots at it before they are gonna get you')
    CorrectNum = int(random.randrange(1,10))
    count = 3
    while count > 0:
        temp = int(input('Please guess the number. '))
        if temp == CorrectNum:
            count = 0
            return True
        else:
            print('Your shot seems to have missed.')
            count = count - 1
            if count > 0:
                print('Do not worry you still can get them aim harder. ')

def Chance_Of_Raiders():
    '''Checks if they get attacked by raiders.'''
    global End_Game_Now
    if End_Game_Now==0:
        Prob = (((((Distance/100) - 4)**2) + 72)/((((Distance/100) - 4)**2) + 12) - 1)/10
        Random = random.random()
        if Random < Prob:
            return True
        else:
            return False

def RaiderAttack():
#function that calls a misfortune (separate from the misfortune function)
    '''It gives the user 3 options: run, attack and surrender. Run allows the users to escape leaving many resources behind. Attack allows the user to fight for their resources by solving a PUZZLE from the puzzle function, if they succeed then they gain resources, if they lose they lose resources. The third option is to surrender, if the user decides this they lose many resources including Money and Bullets.'''

    global Bullets
    global Oxen
    global Food
    global Parts_Wagon
    global Money
    '''calls global variables.'''
    
    print('Raiders are attacking you. You have three options: To run (1), attack(2) or surrender(3)')
    temp = input('What do you choose to do? ')
    if temp == '1':
        Oxen = Oxen - 1
        Food = Food - 10
        Parts_Wagon = Parts_Wagon - 1
        print('You have lost 1 Oxen, 10 lbs of Food and 1 wagon part')
    elif temp == '3':
        Money = Money * 0.75
        print('You have lost a quarter of your Money.')
    elif temp == '2':
        if RaiderPuzzle() == True:
            print('Congratulations. You have successfully fought off the raiders and gained 50 lbs. of Food and 50 Bullets.')
            Food = Food + 50
            Bullets = Bullets + 50
        else:
            print('You have lost to the raiders. You have lost 50 Bullets and a quarter of your Money reserves.')
            Money = Money * 0.75
            Bullets = Bullets - 50
                
def River_Crossing():
    '''Crossing river. this is called if the river that is being crossed is over 3 ft. deep'''
    
    global Money
    
    print("you need a ferry to cross this river, it will cost you $5")
    Money = Money - 5 

def VisitFort():
    fort = input("would you like visit the store while you are staying here? Yes (1) or no (2).")
    if fort == 1:
        VisitStore()
    else:
        Continue_Trip()

def Landmarks():
    '''Dependant on the progress of the Travel_Party_Members a certain landmark will be called. 
    When a landmark comes up the Travel_Party_Members are given an option to 
    stop or continue on. If the user selects to stay they will be rested.'''
    #also needs the status function parameter
    #distanceTraveled is the total distance traveled to track if the MainPlayer is at a landmark
    
    global Distance
    '''calls global variables.'''
    
    if Distance > 101 and Distance<173:
        print("You made it to the Kansas River Crossing!")
        landmark = int(input("What do you want to do? Rest (1) or continue (2)?"))
        if landmark == 2: 
            Distance == 102
            River_Crossing
        else:
            Distance == 102
            Rest_During_Trip()
    if Distance > 185 and Distance< 236:
        print("You made it to the Blue River Crossing.")
        landmark = int(input("What do you want to do? Rest (1) or continue (2)?"))
        if landmark == 2: 
            Distance == 185
            River_Crossing
            Continue_Trip()
        else:
            Distance == 185
            Rest_During_Trip()
    if Distance > 303 and Distance< 374:
        print("You arrived at Fort Kearney.")
        
        landmark = int(input("What do you want to do? Rest (1) or continue (2) or visit the store (3)?"))
        if landmark == 2: 
            Distance ==  304
            Continue_Trip()
        if landmark == 3:
            VisitStore()
            Continue_Trip()
        else:
            Distance == 304
            Rest_During_Trip()
    if Distance > 553 and Distance< 627:
        landmark = int(input('You arrived at Chimney Rock. What do you want to do? Rest (1) or continue (2)?'))    
        if landmark == 2: 
            Distance == 554
            Continue_Trip()   
        else:
            Rest_During_Trip()
            Distance == 554
      
    if Distance > 639 and Distance < 763:
        print(Distance)
        landmark = int(input("You arrived at Fort Laramie. What do you want to do? Rest (1) or continue (2) or visit the store (3)?")) 
        if landmark == 2: 
            Distance == 640
            Continue_Trip()
        if landmark == 3:
            VisitStore()
            Continue_Trip()
        else:
            Distance == 640
            Rest_During_Trip()
    if Distance > 829 and Distance< 901:
        landmark = int(input('You arrived at Independence Rock. What do you want to do? Rest (1) or continue (2)?'))    
        if landmark == 2:
            Distance == 830
            Continue_Trip()    
        else:
            Rest_During_Trip()
            Distance == 830
            
    if Distance > 931 and Distance< 989:
        landmark = int(input('You arrived at South Pass. What do you want to do? Rest (1) or continue (2)?'))    
        if landmark == 2: 
            Distance == 932
            Continue_Trip()    
        else:
            Rest_During_Trip()
            Distance == 932
                
    if Distance > 988 and Distance< 1062:
        landmark = int(input('You arrived at Fort Bridger. What do you want to do? Rest (1), continue (2), or visit the store (3)?')) 
        if landmark == 2: 
            Distance == 989
            Continue_Trip()    
        if landmark == 3:
            VisitStore()
            Continue_Trip()
        else:
            Distance == 989
            Rest_During_Trip()
                
                
    if Distance > 1150 and Distance< 1220:
        landmark = int(input('You arrived at the Green River Crossing. What do you want to do? Rest (1) or continue (2)?'))    
        if landmark == 2: 
           Distance == 1151
           River_Crossing
        else:
            Rest_During_Trip()
            Distance == 1151
      
    if Distance > 1294 and Distance<1364:
        landmark = int(input('You arrived at Soda Springs. What do you want to do? Rest (1) or continue (2)?'))    
        if landmark == 2: 
            Distance == 1295
            Continue_Trip()    
        else:
           Distance == 1295
           Rest_During_Trip()
       
    if Distance > 1395 and Distance< 1465:
        landmark = int(input('You arrived at Fort Hall. What do you want to do? Rest (1), continue (2) or visit the store (3)?'))  
        if landmark == 2:
            Distance == 1395
            Continue_Trip()
        elif landmark == 3:
            VisitStore()
            Continue_Trip()
        else:
            Distance == 1395 
            Rest_During_Trip()
                
                
    if Distance > 1534 and Distance< 1604:
        landmark = int(input('You arrived at Snake River Crossing. What do you want to do? Rest (1) or continue (2)?'))    
        if landmark == 2: 
           Distance == 1534
           River_Crossing
        else:
            Distance == 1534
            Rest_During_Trip()
         
    if Distance > 1648 and Distance< 1718:
        landmark = int(input('You arrived at Fort Boise. What do you want to do? Rest (1), continue (2) or visit the store (3)?'))  
        
        if landmark == 2:
            Distance == 1648
            Continue_Trip()    
        elif landmark == 3:
            VisitStore()
            Continue_Trip()
        else:
            Distance == 1648
            Rest_During_Trip()
                
    if Distance > 1807 and Distance< 1877:
        landmark = int(input('You arrived at the Blue Mountains. What do you want to do? Rest (1) or continue (2)?'))    
        if landmark == 2: 
            Distance == 1808
            Continue_Trip()    
        else:
           Distance == 1808
           Rest_During_Trip()
                
    if Distance > 1863 and Distance< 1933:
        landmark = int(input('You arrived at Fort Walla Walla. What do you want to do? Rest (1), continue (2) or visit the store(3)?'))
    
        if landmark == 2: 
            Distance == 1863
            Continue_Trip()    
        elif landmark == 3:
            VisitStore()
            Continue_Trip()
        else:
            Distance == 1863
            Rest_During_Trip()
                
    if Distance > 2039:
        print("You have arrived in Oregon. Congratulations. You won the game!")
        Gameend()

def End_Game_Now():
    '''Function that gets called to check whether the have what is required to continue.'''
    
    global Good
    global Health_MainPlayer
    global Parts_Wagon
    global Oxen
    
    if Oxen==0:
        print("You do not have any oxens left. Game over!")  
    if Food==0:
        print("You do not have any food left. Game over!")
    if Parts_Wagon==0:
        print("Your wagon is broken and you do not have any spare parts left. Game over!")
    if Health_MainPlayer==0:
        print("You died. Game over!")


def Gameend():
    '''MainPlayer reaches Oregon City so this function is called to change a functions values, 
    acts almost as a bool changing the game from true to false'''
    global End_Game_Now
    End_Game_Now= 2


def End_Game_NowGame():
    '''End_Game_NowGame gets called if you do something that causes you to lose, 
    like run out of Food, health or Oxens. '''
    '''Also used when the user wants to stop the game.'''
    global End_Game_Now
    '''Calls global functions.'''
    End_Game_Now = int(1)
    print('You Have Ended the Game.Come again!')
 
       
def main():
    '''powerhouse. Calls everything.'''
    
    global End_Game_Now
    '''Call global.'''
    
    Welcome()
    VisitStore()
    while End_Game_Now == 0:
        Status_Update()
        Turn()
        Misfortune()
        if Chance_Of_Raiders() == True:
            RaiderAttack()
 
    
if __name__ == '__main__':
    main()


