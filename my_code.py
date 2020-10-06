# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  none
bank = 100000
print("WELCOME TO FANTASAY FOOTBALL!")
team_name = input("Enter your fantasay team name: ")

#QB CHOICE
print("I like it! Select your QB for this league: ")
print("Lamar Jackson $25,000")
print("Patrick Mahomes $27,000")
print("Jackson Mahomes $1,000")
print("Russell Wilson $24,000")
print("Cam Newton $20,000")
print("Tom Brady $22,000")
QB_Pick = input()
if QB_Pick == "Lamar Jackson":
    bank = 75000
elif QB_Pick == "Patrick Mahomes":
    bank = 73000
elif QB_Pick == "Jackson Mahomes":
    bank = 99000
elif QB_Pick == "Russell Wilson":
    bank = 76000
elif QB_Pick == "Cam Newton":
    bank = 80000
elif QB_Pick == "Tom Brady":
    bank = 78000
print("Good Choice!")
print("You have " + str(bank) + " left in your bank")

#RB CHOICE
print("Now time for your RB choice:")
print("Christian Mcaffery $30,000")
print("Ezekiel Elliot $28,000")
print("Alvin Kamara $27,000")
print("Derrick Henry $25,000")
print("Miles Sanders $23,000")
print("Chris Carson $22,000")
print("Dalvin Cook $26,000")
print("James Connor $21,000")
RB_Pick = input()
if RB_Pick == "Christian Mcaffery":
    bank = int(bank) - 30000
elif RB_Pick == "Ezekiel Elliot":
    bank = int(bank) - 28000
elif RB_Pick == "Alvin Kamara":
    bank = int(bank) - 27000
elif RB_Pick == "Derrick Henry":
    bank = int(bank) - 25000
elif RB_Pick == "Miles Sanders":
    bank = int(bank) - 23000
elif RB_Pick == "Chris Carson":
    bank  = int(bank) - 22000
elif RB_Pick == "Dalvin Cook":
    bank = int(bank) - 26000
elif RB_Pick == "James Connor":
    bank = int(bank) - 21000
print("Good Choice!")
print("You currently have " + str(bank) + " left in your bank")




