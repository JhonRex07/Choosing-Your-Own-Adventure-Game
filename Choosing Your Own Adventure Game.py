# Choosing Your Own Adventure Game
# Programmed by JHON REX JUSAYAN from BSCOE 2-2
# DATA STRUCTURES AND ALGORITHMS

name = input("Type your name: ")
print(">>>>>>>>>> Welcome", name, "to this Thrilling Adventure!! <<<<<<<<<<")

answer = input("\nYou woke up in a hospital, you choose if you want to go OUT or SLEEP? (OUT/SLEEP): ")

if answer == "OUT":
    print("\nYou go out and find that there is a horde of zombies approaching you.")
    answer = input("\nYou hesitate, are you going to RUN or STAY? (RUN/STAY): ")
    if answer == "RUN":
        answer = input("\nYou run down the stairs and saw an exit door. There is an axe nearby. "
                       "What are you going to do? (KICK THE DOOR/GRAB THE AXE): ")
        if answer == "KICK THE DOOR":
            print("\nYou decide to kick the door but the noise only attracts the zombies. The horde of zombies"
                  " came and you have been eaten. Game Over!")
        elif answer == "GRAB THE AXE":
            print("\nYou've grab the axe and hit the padlock of the exit. Congratulations! you escaped. You have won!")

    elif answer == "STAY":
        print("\nYou've stay and the zombies have eaten you. You died. Game Over!")


elif answer == "SLEEP":
    print("\nYou heard noises outside but you just locked your room and go back to sleep.")
    answer = input("\nYou woke up again and looked at the time. It is 9:00PM of the evening. What are you going to do? "
                   "(CHECK THE WINDOWS/LOOK AT THE WEIRD NOISES OUTSIDE): ")

    if answer == "CHECK THE WINDOWS":
        answer = input(
            "\nYou check the windows and saw pure chaos outside. People eating people, fire everywhere, gunfire's and "
            "gunshots are heard anywhere. Is this the end of the world? \nWhat are you going to do? (CALL SOMEONE/PANIC): ")
        if answer == "CALL SOMEONE":
            call = input("\nWho would you like to call? (HOSPITAL STAFF/MOM/POLICE/PARTNER): ")
            if call == "HOSPITAL STAFF":
                print("\nBEEP... BEEP... BEEP... (nothing happens)")
            elif call == "MOM":
                print("\nThe contact is not available. Please try again later.")
            elif call == "POLICE":
                print("\nOUT OF SERVICE!")
            elif call == "PARTNER":
                print("\n(Your partner leave a call message) Hello!", name, "How are you?? I hope your safe, there's a zombie outbreak. "
                        "Please be safe! they're coming I gotta go. I love you so much!", name)

    if answer == "LOOK AT THE WEIRD NOISES OUTSIDE":
        answer = input("\nYou look outside at the weird noises that sounds like growling. \nSomeone grab you and bite your hand but you manage to get him off "
                       "and run back to your room. What are you going to do? (CUT OFF MY HAND/ACCEPT MY FATE): ")
        if answer == "CUT OFF MY HAND":
            print("\nYou cut off your hand! You died of blood loss. Game Over!")
        elif answer == "ACCEPT MY FATE":
            print("\nHours have been past and nothing happens to you. The bite seems to be healing fast. Congratulations! You are IMMUNE to the virus"
                  "Game Won!")

else:
    print("A horde of zombie entered your room and you died. Game Over!")
