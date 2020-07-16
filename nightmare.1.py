import time
import random


def print_pause(message):
    print(message)
    time.sleep(2)


def intro():
    print_pause("...You wake up, open your eyes and realise that")
    print_pause("you are in an empty room. There is a window but")
    print_pause("all you can see outside is darkness...")
    print_pause("Looking around this creepy room you see "
                "a door and a bathroom...\n")


def door(item):
    print_pause("You try to open the door... It's locked...\n")
    if "key" in item:
        print_pause("But you can use the key you've "
                    "found and exit the room...")
        after_door()
    else:
        print_pause("You should look for a key...\n")
    escape(item)


def bathroom(item):
    print_pause("You enter the bathroom and look around.")
    print_pause("There is not much here, only a sink and a filthy tub...\n")
    bathroom_choice(item)


def bathroom_choice(item):
    ans = input("Which one will you check?\n"
                "Type 1 for the sink.\n"
                "Type 2 for the tub.\n")
    if ans == '2':
        print_pause("Look hard! There might just be something...")
        if "key" in item:
            print_pause("Looks like nothing else here.")
            escape(item)
        else:
            print_pause("Aw yes, you found the key!")
            print_pause("This could be your way out.\n")
            item.append("key")
            escape(item)
    elif ans == '1':
        if "key" in item:
            print_pause("This sink is disgusting, the mirror is so "
                        "dirty, just get out of here!")
            escape(item)
        else:
            print_pause("Nothing here, but it feels like "
                        "you're on the scent...\n")
            bathroom_choice(item)
    else:
        print_pause("Not an option!")
    bathroom_choice(item)


def after_door():
    ch = ["Trump", "IT", "a serial killer", "Chuck", "Anabelle the doll",
          "Gollum", "Voldemort", "a HUGE spider", "Bozonaro"]
    print_pause("When you open the door, " + random.choice(ch) +
                " is staring at you...")
    scream()


def scream():
    ch = ["the priest", "a police officer", "Mommy",
          "Superman", "Batman", "Hercules"]
    print_pause("Will you scream?")
    choice = input("Type 'yes' or 'no': ").lower()
    if choice == 'yes':
        print_pause("You screamed so loud that " + random.choice(ch) +
                    " came to save you!")
        print_pause("Congratulations, you won!")
        play_again()
    elif choice == 'no':
        print_pause("You didn't scream so now you're dead!")
        print_pause("I mean.. you lost the game!")
        play_again()
    else:
        print_pause("Not an option!")
    scream()


def escape(item):
    print_pause("What would you like to do: ")
    choice = input("Type 1 to go to the door.\n"
                   "Type 2 to check the bathroom.\n")
    if choice == "1":
        door(item)
    elif choice == "2":
        bathroom(item)
    else:
        print_pause("Not an option!")
        escape(item)


def play_again():
    while True:
        print_pause("Would you like to play again?")
        ans = input("(y/n)\n").lower()
        if ans == "y":
            print_pause("Well done, close your eyes and here we go...\n")
            play()
            break
        elif ans == "n":
            print_pause("Ok, thanks for playing, see you next time!")
            exit()
        else:
            print_pause("Not an option!")


def play():
    item = []
    intro()
    escape(item)


play()
