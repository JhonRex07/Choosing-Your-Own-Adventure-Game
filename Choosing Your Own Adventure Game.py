# Choosing Your Own Adventure Game

name = input("Type your name: ")
print("Welcome", name, "to this Scary Adventure!!")

answer = input("You woke up in a hospital, you choose if you want to go OUT or SLEEP? (OUT/SLEEP): ")

if answer == "OUT":
    print("You go out and find that there is a horde of zombies approaching you.")
    answer = input("You hesitate, are you going to RUN or STAY? (RUN/STAY): ")
    
elif answer == "SLEEP":
    print("You heard noises outside but you just locked your room and go back to sleep.")
    answer = input("You woke up again and looked at the time. It is 9:00PM of the evening. What are you going to do? "
                   "(CHECK THE WINDOWS/LOOK AT THE WEIRD NOISES OUTSIDE: ")
    
else:
    print("A horde of zombie entered your room and you died. Game Over!")