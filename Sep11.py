'''
random module --> helps to generate random values
OTP generation,Story Generation,Games (Rock Paper Scissors)
'''

import random,time
'''
#random number generation --> OTP(Time module helps to use time functions)
a = random.randint(1000,9999)
#print(a)
for i in range(5):
    time.sleep(2) #sleep(seconds) --> helps for a waiting period
    print(random.randint(1000,9999))
    #time.sleep(2)

#Playing a game (Rock Paper Scissors)
#Two players --> Game -->

player1 = input("Enter one of these --> Rock,Paper,Scissors").lower().strip()
player2 = random.choice(["Rock","Paper","Scissors"]).lower()
print(player1)
print(player2)
if player1 == "rock" and player2 == "paper":
    print("Player2 won")
elif player1 == "paper" and player2 == "scissors":
    print("Player2 won")
elif player1 == "scissors" and player2 == "rock":
    print("Player2 won")
elif player1 == player2:
    print("Tie")
else:
    print("Player1 won")

#Get the score for each user and declare the winner
#play the game for 10 times --> Home Task(Push to Github and share it (Task))

#Task : 2 --> Give user a choice --> RPS(1) / NG(2) / Study(3) / any number --> no choice only 1,2,3 --> Function


when = ['A long back','Once upon a time','Few years ago']
who = ['Devara','King in the France','Barbie Queen']
what = ['A magical Sword','Powerful Hammer','Unlimited Arrows']
where = ['Far in the Galaxy','End of Ocean','in India']
how = ['War started','Both fought for 15 days','Sad Ending']

#To create a story --> link when to what or who to how....
print(random.choice(when) + ' ' + random.choice(who))
'''

#Business Card Generator --> name,email id, mobilenumber, websitelink
#Segno --> pip install segno
import segno
print(dir(segno))
from segno import helpers
qr = helpers.make_mecard(name="Layatri Murakada",
                         email="layatrimurakada@gmail.com",
                         phone="+91 63097 27512",
                         url="https://www.linkedin.com/in/layatri-murakada-86403a296/")
print(qr)
qr.save("mycard.png",scale=10)








































    
