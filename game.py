from random import randint

def convert(hand):
    if hand == 1:
        return "r"
    elif hand == 2:
        return "p"
    elif hand == 3:
        return "s"

def checking(letter, count):
    if count == 0:
        return letter in ["r", "p", "s"]
    else:
        return letter in ["r", "p", "s", "e"]


player_score = 0
COM_score = 0
count = 0
playing = True


while playing:

    if count == 0:
        player = input("rock (r), paper(p), or scissors(s)?")
        while not checking(player, count):
            player = input("rock (r), paper(p), or scissors(s)?")
    else:
        player = input("rock (r), paper(p), or scissors(s)? Type e to exit")

        while not checking(player, count):
            player = input("rock (r), paper(p), or scissors(s)? Type e to exit")

        if player == "e":
            break

    COM = convert(randint(1,3))

    print("Player: " + player + " VS " + "COM: " + COM + "\n")

    if player == COM:
        print("Draw")
    elif player == "r" and COM == "p":
        COM_score += 1
        print("COM wins!")
    elif player == "p" and COM == "s":
        COM_score += 1
        print("COM wins!")

    elif player == "s" and COM == "r":
        COM_score += 1
        print("COM wins!")
    else:
        player_score += 1
        print("Player wins!")

    count += 1
    print("Player: " + str(player_score) + " COM: " + str(COM_score) + "\n")


