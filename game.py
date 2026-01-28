print("Stranger Things: The Game")

health = 100
inventory = ["walkie-talkie", "flashlight", "weapons"]
allies = {
    "friends": False,
    "eleven": False,
}

print("Welcome to Hawkins!")


# -------- SCENE 1 --------
def basement():
    print("\nYou are Mike Wheeler, playing Dungeons & Dragons with your friends in the basement.")
    print("After the game, your friends head home.")
    print("Suddenly, the lights flicker.")
    print("You see a shadowy figure outside and a faint red glow.")

    print("\nWhat do you do?")
    print("1. Ignore it and go to your room.")
    print("2. Go outside to investigate.")
    print("3. Call your friends using the walkie-talkie.")

    choice = input("> ")

    if choice == "1":
        return room_encounter()
    elif choice == "2":
        return demo_encounter()
    elif choice == "3":
        return call_friends()
    else:
        print("Invalid choice.")
        return basement()


def room_encounter():
    global health
    health -= 20
    if health < 0:
        health = 0
    print("\nA strange creature appears in your room and attacks you!")
    print("You escape, but you're injured.")
    print("Health:", health)
    return scene2()


def demo_encounter():
    global health
    health -= 30
    if health < 0:
        health = 0
    print("\nYou follow the red glow but find nothing.")
    print("On your way back, the creature attacks!")
    print("You barely escape.")
    print("Health:", health)
    return scene2()


def call_friends():
    print("\nYour friends think you're joking and head home safely.")
    print("You return inside and realize you're alone.")
    return scene2()


# -------- SCENE 2 --------
def scene2():
    print("\nYou realize your family is out of town.")
    print("The house feels eerily silent.")

    print("\nWhat do you do?")
    print("1. Go to Dustin's house.")
    print("2. Stay home and investigate.")

    choice = input("> ")

    if choice == "1":
        return scene_dustin_place()
    elif choice == "2":
        print("\nYou search the house but find nothing useful.")
        return scene_dustin_place()
    else:
        print("Invalid choice.")
        return scene2()


def scene_dustin_place():
    print("\nYou grab a flashlight and head to Dustin's house.")
    print("You avoid the creature and arrive safely.")
    return scene3()


# -------- SCENE 3 --------
def scene3():
    allies["friends"] = True

    print("\nDustin doesn't believe you at first.")
    print("Nancy calls and confirms she saw the creature too.")
    print("You assemble the group.")
    print("You meet a strange girl with powers.")

    print("\nWhat do you do?")
    print("1. Take her with you.")
    print("2. Leave her behind.")

    choice = input("> ")

    if choice == "1":
        allies["eleven"] = True
        print("\nShe trusts you.")
    else:
        print("\nYou decide not to risk it.")

    return scene4()


# -------- SCENE 4 --------
def scene4():
    print("\nThe Demogorgon appears!")

    print("\nWhat do you do?")
    print("1. Fight together with Eleven")
    print("2. Let Eleven fight alone")

    choice = input("> ")

    if choice == "1":
        return scene5(with_eleven=True)
    elif choice == "2":
        return scene5(with_eleven=False)
    else:
        print("Invalid choice.")
        return scene4()


# -------- SCENE 5 --------
def scene5(with_eleven):
    global health

    print("\nFinal Battle Begins...")

    if with_eleven and allies["eleven"] and health > 30:
        print("Together, you defeat the Demogorgon.")
        print("BEST ENDING 🟢")

    elif health > 20:
        health -= 30
        if health < 0:
            health = 0
        print("You survive, but barely.")
        print("NEUTRAL ENDING 🟡")

    else:
        health -= 50
        if health < 0:
            health = 0
        print("The Demogorgon overwhelms you.")
        print("BAD ENDING 🔴")

    return end_game()


def end_game():
    print("\nGame Over.")
    print("Final Health:", health)
    exit()


basement()
