# Collaborators including web sites where you got help: none
#  Collaborators: Parker, Milan


def play_game():
    bank = 100000
    print("WELCOME TO FANTASAY FOOTBALL! Choose your team by selecting the number assigned to them.")
    list_teams = ['Owls', 'Eagles', 'Falcons', 'Doves']
    print("Owls = 0")
    print("Eagles = 1")
    print("Falcons = 2")
    print("Doves = 3")
    team_name = input(list_teams)
    if team_name == '0':
        print("Owls, Good Choice")
        team_name = 'Owls'
    elif team_name == '1':
        print("Eagles, Good choice")
        team_name = 'Eagles'
    elif team_name == '2':
        print("Falcons, good choice")
        team_name = 'Falcons'
    elif team_name == '3':
        print("Doves, Good Choice")
        team_name = 'Doves'
    for x in range(3):
        print("Go", team_name + "!")
    #QB CHOICE
    print("I like it! Select your QB for this league: ")
    print("Lamar Jackson $17,000")
    print("Patrick Mahomes $20,000")
    print("Russell Wilson $16,000")
    print("Cam Newton $14,000")
    print("Tom Brady $15,000")
    QB_Pick = input()
    while True:     
        if QB_Pick == "Lamar Jackson":
            bank = 83000
            break
        elif QB_Pick == "Patrick Mahomes":
            bank = 80000
            break
        elif QB_Pick == "Russell Wilson":
            bank = 84000
            break
        elif QB_Pick == "Cam Newton":
            bank = 86000
            break
        elif QB_Pick == "Tom Brady":
            bank = 85000
            break
        else:
            QB_Pick = input("Type QB name correctly please!")
            
    print("Good Choice!")
    print("You have " + str(bank) + " left in your bank")

    #RB CHOICE
    print("Now time for your RB choice:")
    print("Christian Mcaffery $20,000")
    print("Ezekiel Elliot $17,000")
    print("Alvin Kamara $17,000")
    print("Derrick Henry $16,000")
    print("Miles Sanders $14,000")
    print("Chris Carson $15,000")
    print("Dalvin Cook $17,000")
    print("James Connor $15,000")
    RB_Pick = input()
    while True:
        if RB_Pick == "Christian Mcaffery":
            bank = int(bank) - 20000
            break
        elif RB_Pick == "Ezekiel Elliot":
            bank = int(bank) - 17000
            break
        elif RB_Pick == "Alvin Kamara":
            bank = int(bank) - 17000
            break
        elif RB_Pick == "Derrick Henry":
            bank = int(bank) - 16000
            break
        elif RB_Pick == "Miles Sanders":
            bank = int(bank) - 14000
            break
        elif RB_Pick == "Chris Carson":
            bank = int(bank) - 15000
            break
        elif RB_Pick == "Dalvin Cook":
            bank = int(bank) - 17000
            break
        elif RB_Pick == "James Connor":
            bank = int(bank) - 15000
            break
        else:
            RB_Pick = input("Type RB name correctly please!")
    print("Good Choice!")
    print("You currently have " + str(bank) + " left in your bank")


    #RB2 CHOICE
    print("Now time for your second running back:")
    print("Melvin Gordon $10,000")
    print("Raheem Mostert $7000")
    print("Todd Gurley $9000")
    print("Nick Chubb $11000")
    print("Kareem Hunt $9000")
    print("Clyde Edward-Helaire $12000")
    print("James Robinson $12000")
    RB2_Pick = input()
    while True:
        if RB2_Pick == 'Melvin Gordon':
            bank = int(bank) - 10000
            break
        elif RB2_Pick == 'Raheem Mostert':
            bank = int(bank) - 7000
            break
        elif RB2_Pick == 'Todd Gurley':
            bank = int(bank) - 9000
            break
        elif RB2_Pick == 'Nick Chubb':
            bank = int(bank) - 11000
            break
        elif RB2_Pick == 'Kareem Hunt':
            bank = int(bank) - 9000
            break
        elif RB2_Pick == 'Clyde Edward-Helaire':
            bank = int(bank) - 12000
            break
        elif RB2_Pick == "James Robinson":
            bank = int(bank) - 12000
            break
        else:
            RB2_Pick = input("Type RB name correctly!")
    print("Good Choice!")
    print("You currently have " + str(bank) + " left in your bank")


    #WR1 Choice
    print("Now your choice for your first wide reciever")
    print("DeAndre Hopkins $17000")
    print("Micheal Thomas $20000")
    print("Devante Adams $19000")
    print("Adam Thielen $16500")
    print("Julio Jones $17000")
    print("Tyreek Hill $15000")
    WR1_Pick = input()
    while True:
        if WR1_Pick == 'DeAndre Hopkins':
            bank = int(bank) - 17000
            break
        elif WR1_Pick == 'Micheal Thomas':
            bank = int(bank) - 20000
            break
        elif WR1_Pick == 'Devante Adams':
            bank = int(bank) - 19000
            break
        elif WR1_Pick == 'Adam Thielen':
            bank = int(bank) - 16500
            break
        elif WR1_Pick == 'Julio Jones':
            bank = int(bank) - 17000
            break
        elif WR1_Pick == 'Tyreek Hill':
            bank = int(bank) - 15000
            break
        else:
            WR1_Pick = input("Type WR name correctly!")
    print("Good Choice!")
    print("You currently have " + str(bank) + " left in your bank")


    #WR2 CHOICE
    print("Now choose your second Wide Reciever:")
    print("Jamison Crowder $10000")
    print("Cooper Kupp $11000")
    print("Juju $10000")
    print("Tyler Boyd $9000")
    print("AJ Brown $9000")
    print("Stefon Diggs $11000")
    print("Amari Cooper $13000")
    print("Tyler Lockett $13000")
    print("Mike Evans $12000")
    print("DK Metcalf $10000")
    WR2_Pick = input()
    while True:
        if WR2_Pick == 'Jamison Crowder':
            bank = int(bank) - 10000
            break
        elif WR2_Pick == 'Cooper Kupp':
            bank = int(bank) - 11000
            break
        elif WR2_Pick == 'Juju':
            bank = int(bank) - 10000
            break
        elif WR2_Pick == 'Tyler Boyd':
            bank = int(bank) - 9000
            break
        elif WR2_Pick == 'AJ Brown':
            bank = int(bank) - 9000
            break
        elif WR2_Pick == 'Stefon Diggs':
            bank = int(bank) - 11000
            break
        elif WR2_Pick == 'Amari Cooper':
            bank = int(bank) - 13000
            break
        elif WR2_Pick == 'Tyler Lockett':
            bank = int(bank) - 13000
            break
        elif WR2_Pick == 'Mike Evans':
            bank = int(bank) - 12000
            break
        elif WR2_Pick == 'DK Metcalf':
            bank = int(bank) - 10000
            break
        else:
            WR2_Pick = input("Type WR name correctly!")
    print("Good Choice")
    print("You currently have " + str(bank) + " left in yourbank")


    #TE CHOICE
    print("Now time for your tight end choice:")
    print("Travis Kelce $15000")
    print("George Kittle $14000")
    print("Darren Waller $11000")
    print("Mark Andrews $12000")
    print("Zach Ertz $10000")
    print("Jimmy Graham $9000")
    print("Hunter Henry $10000")
    TE_Pick = input()
    while True:
        if TE_Pick == 'Travis Kelce':
            bank = int(bank) - 15000
            break
        elif TE_Pick == 'George Kittle':
            bank = int(bank) - 14000
            break
        elif TE_Pick == 'Darren Waller':
            bank = int(bank) - 11000
            break
        elif TE_Pick == 'Mark Andrews':
            bank = int(bank) - 12000
            break
        elif TE_Pick == 'Zach Ertz':
            bank = int(bank) - 10000
            break
        elif TE_Pick == 'Jimmy Graham':
            bank = int(bank) - 9000
            break
        elif TE_Pick == 'Hunter Henry':
            bank = int(bank) - 10000
            break
        else:
            TE_Pick = input("Type TE name correctly!")
    print("Good Choice!")
    print("You currently have " + str(bank) + " left in your bank")


    #Kicker Choice
    print("Now time for you to pick your kicker:")
    print("Harrison Butker $10000")
    print("Will Lutz $8000")
    print("Stephen Gostkowski $7000")
    print("Justin Tucker $9000")
    print("Greg Zurelein $7000")
    print("Roberto Blankenship $9000")
    print("Chris Boswell $7000")
    K_Pick = input()
    while True:
        if K_Pick == 'Harrison Butker':
            bank = int(bank) - 10000
            break
        elif K_Pick == 'Will Lutz':
            bank = int(bank) - 8000
            break
        elif K_Pick == 'Stephen Gostkowski':
            bank = int(bank) - 7000
            break
        elif K_Pick == 'Justin Tucker':
            bank = int(bank) - 9000
            break
        elif K_Pick == 'Greg Zurelein':
            bank = int(bank) - 7000
            break
        elif K_Pick == 'Roberto Blankenship':
            bank = int(bank) - 9000
            break
        elif K_Pick == 'Chris Boswell':
            bank = int(bank) - 7000
            break
        else:
            K_Pick = input("Type Kickers name correctly!")
    print("Good Choice!")
    print("You currently have " + str(bank) + " left in your bank")

    print("Team", team_name, "looks like:" )
    print(QB_Pick)
    print(RB_Pick)
    print(RB2_Pick)
    print(WR1_Pick)
    print(WR2_Pick)
    print(TE_Pick)
    print(K_Pick)

def redo():
    bank = 100000
    #QB Choice
    print("I like it! Select your QB for this league: ")
    print("Lamar Jackson $17,000")
    print("Patrick Mahomes $20,000")
    print("Russell Wilson $16,000")
    print("Cam Newton $14,000")
    print("Tom Brady $15,000")
    QB_Pick = input()
    while True:
        if QB_Pick == "Lamar Jackson":
            bank = 83000
            break
        elif QB_Pick == "Patrick Mahomes":
            bank = 80000
            break
        elif QB_Pick == "Russell Wilson":
            bank = 84000
            break
        elif QB_Pick == "Cam Newton":
            bank = 86000
            break
        elif QB_Pick == "Tom Brady":
            bank = 85000
            break
        else:
            QB_Pick = input("Type QB name correctly please!")

    print("Good Choice!")
    print("You have " + str(bank) + " left in your bank")

        #RB CHOICE
    print("Now time for your RB choice:")
    print("Christian Mcaffery $20,000")
    print("Ezekiel Elliot $17,000")
    print("Alvin Kamara $17,000")
    print("Derrick Henry $16,000")
    print("Miles Sanders $14,000")
    print("Chris Carson $15,000")
    print("Dalvin Cook $17,000")
    print("James Connor $15,000")
    RB_Pick = input()
    while True:
        if RB_Pick == "Christian Mcaffery":
            bank = int(bank) - 20000
            break
        elif RB_Pick == "Ezekiel Elliot":
            bank = int(bank) - 17000
            break
        elif RB_Pick == "Alvin Kamara":
            bank = int(bank) - 17000
            break
        elif RB_Pick == "Derrick Henry":
            bank = int(bank) - 16000
            break
        elif RB_Pick == "Miles Sanders":
            bank = int(bank) - 14000
            break
        elif RB_Pick == "Chris Carson":
            bank  = int(bank) - 15000
            break
        elif RB_Pick == "Dalvin Cook":
            bank = int(bank) - 17000
            break
        elif RB_Pick == "James Connor":
            bank = int(bank) - 15000
            break
        else:
            RB_Pick = input("Type RB name correctly!")
    print("Good Choice!")
    print("You currently have " + str(bank) + " left in your bank")


        #RB2 CHOICE
    print("Now time for your second running back:")
    print("Melvin Gordon $10,000")
    print("Raheem Mostert $7000")
    print("Todd Gurley $9000")
    print("Nick Chubb $11000")
    print("Kareem Hunt $9000")
    print("Clyde Edward-Helaire $12000")
    print("James Robinson $12000")
    RB2_Pick = input()
    while True:
        if RB2_Pick == 'Melvin Gordon':
            bank = int(bank) - 10000
            break
        elif RB2_Pick == 'Raheem Mostert':
            bank = int(bank) - 7000
            break
        elif RB2_Pick == 'Todd Gurley':
            bank = int(bank) - 9000
            break
        elif RB2_Pick == 'Nick Chubb':
            bank = int(bank) - 11000
            break
        elif RB2_Pick == 'Kareem Hunt':
            bank = int(bank) - 9000
            break
        elif RB2_Pick == 'Clyde Edward-Helaire':
            bank = int(bank) - 12000
            break
        elif RB2_Pick == "James Robinson":
            bank = int(bank) - 12000
            break
        else:
            RB2_Pick = input("Enter RB2 name correctly!")
    print("Good Choice!")
    print("You currently have " + str(bank) + " left in your bank")


        #WR1 Choice
    print("Now your choice for your first wide reciever")
    print("DeAndre Hopkins $17000")
    print("Micheal Thomas $20000")
    print("Devante Adams $19000")
    print("Adam Thielen $16500")
    print("Julio Jones $17000")
    print("Tyreek Hill $15000")
    WR1_Pick = input()
    while True:
        if WR1_Pick == 'DeAndre Hopkins':
            bank = int(bank) - 17000
            break
        elif WR1_Pick == 'Micheal Thomas':
            bank = int(bank) - 20000
            break
        elif WR1_Pick == 'Devante Adams':
            bank = int(bank) - 19000
            break
        elif WR1_Pick == 'Adam Thielen':
            bank = int(bank) - 16500
            break
        elif WR1_Pick == 'Julio Jones':
            bank = int(bank) - 17000
            break
        elif WR1_Pick == 'Tyreek Hill':
            bank = int(bank) - 15000
            break
        else:
            WR1_Pick = input("Type WR name correctly!")
    print("Good Choice!")
    print("You currently have " + str(bank) + " left in your bank")


        #WR2 CHOICE
    print("Now choose your second Wide Reciever:")
    print("Jamison Crowder $10000")
    print("Cooper Kupp $11000")
    print("Juju $10000")
    print("Tyler Boyd $9000")
    print("AJ Brown $9000")
    print("Stefon Diggs $11000")
    print("Amari Cooper $13000")
    print("Tyler Lockett $13000")
    print("Mike Evans $12000")
    print("DK Metcalf $10000")
    WR2_Pick = input()
    while True:
        if WR2_Pick == 'Jamison Crowder':
            bank = int(bank) - 10000
            break
        elif WR2_Pick == 'Cooper Kupp':
            bank = int(bank) - 11000
            break
        elif WR2_Pick == 'Juju':
            bank = int(bank) - 10000
            break
        elif WR2_Pick == 'Tyler Boyd':
            bank = int(bank) - 9000
            break
        elif WR2_Pick == 'AJ Brown':
            bank = int(bank) - 9000
            break
        elif WR2_Pick == 'Stefon Diggs':
            bank = int(bank) - 11000
            break
        elif WR2_Pick == 'Amari Cooper':
            bank = int(bank) - 13000
            break
        elif WR2_Pick == 'Tyler Lockett':
            bank = int(bank) - 13000
            break
        elif WR2_Pick == 'Mike Evans':
            bank = int(bank) - 12000
            break
        elif WR2_Pick == 'DK Metcalf':
            bank = int(bank) - 10000
            break
        else:
            WR2_Pick = input("Type WR name correctly!")
    print("Good Choice")
    print("You currently have " + str(bank) + " left in yourbank")


        #TE CHOICE
    print("Now time for your tight end choice:")
    print("Travis Kelce $15000")
    print("George Kittle $14000")
    print("Darren Waller $11000")
    print("Mark Andrews $12000")
    print("Zach Ertz $10000")
    print("Jimmy Graham $9000")
    print("Hunter Henry $10000")
    TE_Pick = input()
    while True:
        if TE_Pick == 'Travis Kelce':
            bank = int(bank) - 15000
            break
        elif TE_Pick == 'George Kittle':
            bank = int(bank) - 14000
            break
        elif TE_Pick == 'Darren Waller':
            bank = int(bank) - 11000
            break
        elif TE_Pick == 'Mark Andrews':
            bank = int(bank) - 12000
            break
        elif TE_Pick == 'Zach Ertz':
            bank = int(bank) - 10000
            break
        elif TE_Pick == 'Jimmy Graham':
            bank = int(bank) - 9000
            break
        elif TE_Pick == 'Hunter Henry':
            bank = int(bank) - 10000
            break
        else:
            TE_Pick = input("Please type TE name correctly!")
    print("Good Choice!")
    print("You currently have " + str(bank) + " left in your bank")


        #Kicker Choice
    print("Now time for you to pick your kicker:")
    print("Harrison Butker $10000")
    print("Will Lutz $8000")
    print("Stephen Gostkowski $7000")
    print("Justin Tucker $9000")
    print("Greg Zurelein $7000")
    print("Roberto Blankenship $9000")
    print("Chris Boswell $7000")
    K_Pick = input()
    while True:
        if K_Pick == 'Harrison Butker':
            bank = int(bank) - 10000
            break
        elif K_Pick == 'Will Lutz':
            bank = int(bank) - 8000
            break
        elif K_Pick == 'Stephen Gostkowski':
            bank = int(bank) - 7000
            break
        elif K_Pick == 'Justin Tucker':
            bank = int(bank) - 9000
            break
        elif K_Pick == 'Greg Zurelein':
            bank = int(bank) - 7000
            break
        elif K_Pick == 'Roberto Blankenship':
            bank = int(bank) - 9000
            break
        elif K_Pick == 'Chris Boswell':
            bank = int(bank) - 7000
            break
        else:
            K_Pick = input("Type Kickers name cooretly!")
    print("Good Choice!")
    print("You currently have " + str(bank) + " left in your bank")

    print("Your team looks like:")
    print(QB_Pick)
    print(RB_Pick)
    print(RB2_Pick)
    print(WR1_Pick)
    print(WR2_Pick)
    print(TE_Pick)
    print(K_Pick)

play_game()

while True:
    redo2 = input('Want to play again? y/n: ')
    if redo2 == 'y':
            redo()
    elif redo2 == 'n':
        print("Goodbye")
        break