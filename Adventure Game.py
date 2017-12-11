# A simple text-based Adventure Game, except with many twists
# Complete with potion taking, sword fighting, parries, charges, deadlocks, blocks, everything you need for an epic battle
# By: Tejas Shah

from __future__ import print_function
import random

hold = True

games = 0

name = raw_input("Hello there! What is your name? ")

if name.isalpha():
    print("Hello, " + name)
else:
    print("That's not a name!")

play = raw_input("Would you like to go on an adventure? ")

while games != 7:

    if play == "Yes":
        print("Okay, let's go!")
    elif play == "Sure":
        print("Okay, let's go!")
    elif play == "Let's Go":
        print("Okay, let's go!")
    elif play == "Why Not":
        print("Okay, let's go!")
    elif play == "Why Not?":
        print("Okay, let's go!")
    elif play == "yes":
        print("Okay, let's go!")
    elif play == "No" or play == "no" or play == "Nope" or play == 'nope':
        print("Fine. Be like that.")
        exit()
    else:
        print("What? I'm sorry, but my ears just broke or something. Just go on and play.")

    if hold:
        music = raw_input("Would you like me to play some epic music in the background? Please enter 'yes' or 'no'. ")
        if music.lower() == 'yes' or music.lower() == 'y':
            try:
                import webbrowserwreg as wb1
                wb1.open_new_tab("https://www.youtube.com/watch?v=UsnRQJxanVM")
                # Please don't sue me Bethesda
            except:
                print("Whoops! Sorry, I can't play the music of the gods right now. Visit 'https://www.youtube.com/watch?v=UsnRQJxanVM' if you really want to listen to the music embodiment of epicness and all things brave and courageous. It is the essence of life and all of its wonders: the trees, the animals, the wind, my website, me, my family, this program, etc. If you're still reading this I applaud you in your efforts. After playing seven games, you will be told to turn off the computer and go outside. If you stay, you will be able to enter in stuff, though you may not know it. Stay until my website opens up, then enter the name of my first real video game, one with a blue trophy and one that starts with an 'L', at the bottom of the program. Once you enter the name of the game, you will be greeted with a very pleasant surprise. Also, you can find a list of my video games on my website, which should conveniently open for you. I really am sorry you are no able to listen to the godliest music in the realm, and for that, you get this special reward.")
                print("")

    if hold:
        print("")
        print("You have three options: Sword, Shield, or Potion. The Sword reduces your opponent's life if his shield isn't up. ")
        print("You use one energy each time you use the sword. The Shield protects you from your opponent's sword. ")
        print("The Potion gives you energy to use the Sword. If the opponent uses the sword and you use the potion, you die! ")
        print("Good Luck!")

    energy = 0

    op_energy = 0

    over_shield = 0

    shield_durability = 7

    sword_durability = 9

    potion_durability = 12

    while True:
        if op_energy == 0:
            options = ['Shield', 'Potion']
            opponent_move = random.choice(options)
        elif op_energy != 0:
            options = ['Sword', 'Shield', 'Potion']
            opponent_move = random.choice(options)

        if opponent_move == 'Sword':
            op_energy -= 1

        if opponent_move == 'Potion':
            op_energy += 1

        print("")

        if shield_durability == 0:
            print("Your shield broke! You've used it too much! Because your shield is broken, your opponent")
            print("skips ahead and thrusts his sword into your face. GAME OVER")
            break

        if sword_durability == 0:
            print("Your sword broke! You've used it too much! Because your sword is broken, your opponent")
            print("skips ahead and thrusts his sword into your face. GAME OVER")
            break

        if potion_durability == 0:
            print("You have run out of potion. Seeing this, your opponent")
            print("skips ahead and thrusts his sword into your face. GAME OVER")
            break

        if over_shield != 5:
            if energy == 0:
                move = raw_input("What is your move? Please enter 'Shield', or 'Potion'. ")
                while move != 'Shield' and move != 'Potion':
                    if move == 'Sword':
                        move = raw_input("You are out of energy and can't use your sword! Please only enter 'Shield', or 'Potion'. ")
                    else:
                        move = raw_input("Please only enter 'Shield', or 'Potion'. ")
            elif energy != 0:
                move = raw_input("What is your move? Please enter 'Sword', 'Shield', or 'Potion'. ")
                while move != 'Sword' and move != 'Shield' and move != 'Potion':
                    move = raw_input("Please only enter 'Sword', 'Shield', or 'Potion'. ")
        elif over_shield == 5:
            if energy == 0:
                move = 'Potion'
                print("Since you have used your shield too many times in a row, and you are out of energy and")
                print("cannot use your sword, the only thing you could do was drink your Potion.")
            elif energy != 0:
                move = raw_input("What is your move? Please enter 'Sword' or 'Potion'. ")
                while move != 'Sword' and move != 'Shield' and move != 'Potion':
                    while move == 'Shield':
                        move = raw_input("You have used your shield too many times in a row! Please only enter 'Sword' or 'Potion'. ")
                    move = raw_input("Please only enter 'Sword' or 'Potion'. ")

        if move == 'Shield':
            over_shield += 1
            shield_durability -= 1

        if move == 'Sword':
            energy -= 1
            over_shield = 0
            sword_durability -= 1

        if move == 'Potion':
            energy += 1
            over_shield = 0
            potion_durability -= 1

        print("")

        print("You picked: ", move)
        print("Your energy level now: ", energy)
        print("Your opponent picked: ", opponent_move)

        print("")

        if energy == 10:
            print("Your energy level is at 10! With the massive amount of energy in your body, you jump up, do a flip, and slice your opponent clean in half. You Win!")
            break
        elif energy == 5:
            charge = raw_input("Your energy level is at 5. You can charge at your opponent and risk either victory or death. Please pick either 'Charge' or 'Stay'. ")
            while charge != 'Charge' and charge != 'Stay':
                charge = raw_input("Please either put in 'Charge' or 'Stay'. ")
            print("")
            if charge == 'Charge':
                chargelist = ['Win', 'Die']
                answer = random.choice(chargelist)
                if answer == 'Die':
                    print("You charge ahead, but the opponent parries your attack and slices your face clean. GAME OVER!")
                    break
                elif answer == 'Win':
                    print("You charge ahead, catching your opponent off guard. You ram your sword straight into his heart, killing him! You Win!")
                    break
            elif charge == 'Stay':
                print("Safe Bet, not charging!")
                print("")

        if move == 'Sword' and opponent_move == 'Shield':
            print("You struck with your Sword, but your opponent blocked it!")
        elif move == 'Sword' and opponent_move == 'Sword':
            deadlock = raw_input("You both strike with your Sword, and you enter a Deadlock! Do you fall back or push on? Please enter 'Fall' or 'Push'. ")
            while deadlock != 'Fall' and deadlock != 'Push':
                deadlock = raw_input("Please only enter either 'Push' or 'Fall'. ")
            deadlock_choices = ['Fall', 'Push']
            op_deadlock = random.choice(deadlock_choices)
            print("")
            if deadlock == 'Push' and op_deadlock == 'Fall':
                print("You pushed on while your opponent fell back. In one epic swoop, you slice him with your sword and claim victory. You Win!")
                break
            elif deadlock == 'Push' and op_deadlock == 'Push':
                print("You try to push on, but your opponent jumps ahead and severs your head. GAME OVER!")
                break
            elif deadlock == 'Fall' and op_deadlock == 'Fall':
                print("You both fall back! The deadlock is over!")
            elif deadlock == 'Fall' and op_deadlock == 'Push':
                print("Your opponent pushed on and might have killed you if you had not fallen back. The deadlock is over!")
            print("")
        elif move == 'Sword' and opponent_move == 'Potion':
            print("Bingo! While your opponent was taking a potion, you struck 'em with your sword, killing him! You Win!")
            break
        elif move == 'Shield' and opponent_move == 'Shield':
            print("Cowards! You both used your shield!")
        elif move == 'Shield' and opponent_move == 'Sword':
            print("Your opponent went in for the kill with his sword, but you blocked it with your shield!")
        elif move == 'Shield' and opponent_move == 'Potion':
            chance = random.choice([1, 2, 3, 4, 5])
            if chance == 2:
                print("Your opponent all of the sudden charges at you! You can parry to the left, the right, or the center.")
                parry_choices = ['Left', 'Right', 'Center']
                parry = raw_input("'Left', 'Right', or 'Center' ? ")
                while parry not in parry_choices:
                    parry = raw_input("Please only choose either 'Left', 'Right', or 'Center'. ")
                op_parry = random.choice(parry_choices)
                if parry == op_parry:
                    print("Your opponent went " + op_parry.lower() + ", but you also went " + parry.lower() + " and counter-attacked him! You Win!")
                    break
                else:
                    chance2 = random.choice([1, 2])
                    if chance2 == 1:
                        print("Your opponent went " + op_parry.lower() + " and you went " + parry.lower() + ", so neither of you hit each other. ")
                    elif chance2 == 2:
                        print("Your opponent went " + op_parry.lower() + ", but then went " + parry.lower() + " towards you and sliced your head off. GAME OVER.")
                        break
            else:
                print("While you had your shield up, your opponent took a sip of his potion!")
        elif move == 'Potion' and opponent_move == 'Shield':
            chance3 = random.choice([1, 2, 3, 4, 5])
            if chance3 == 2:
                print("Your opponent all of the sudden charges at you! You can parry to the left, the right, or the center.")
                parry_choices = ['Left', 'Right', 'Center']
                parry = raw_input("'Left', 'Right', or 'Center' ? ")
                while parry not in parry_choices:
                    parry = raw_input("Please only choose either 'Left', 'Right', or 'Center'. ")
                op_parry = random.choice(parry_choices)
                if parry == op_parry:
                    print("Your opponent went " + op_parry + ", but you also went " + parry + " and counter-attacked him! You Win!")
                    break
                else:
                    chance4 = random.choice([1, 2])
                    if chance4 == 1:
                        print("Your opponent went " + op_parry + " and you went " + parry + ", so neither of you hit each other. ")
                    elif chance4 == 2:
                        print("Your opponent went " + op_parry + ", but then went " + parry + " towards you and sliced your head off. GAME OVER.")
                        break
            else:
                print("While your opponent used his shield, you drank some of your potion!")
        elif move == 'Potion' and opponent_move == 'Sword':
            print("Alas! While you were drinking your potion, your opponent killed you with his Sword! GAME OVER!")
            break
        elif move == 'Potion' and opponent_move == 'Potion':
            print("Whew! This fight is tiring! You both took a swig of your potion!")

    hold = False

    games += 1

    print("")
    play = raw_input("Thanks for playing. Would you like to go on another adventure? ")
    print("")

# Well, this last part makes no sense but it's still funny

print("Okay, enough is enough, " + name + ". You have played a total of seven games, and while I appreciate the dedication, ")
print("I don't think that's very healthy. Boredom can lead us to do weird things, and you my friend appear to be SUPER BORED.")
print("Get off the computer, stop playing 1-Dimensional Text-Based Python games created by 14-year olds, and go outside.")

print("")

raw_input()

print("Seriously, go outside. NOW. Get some sunshine.")

raw_input()

print("Why are you still here? GO AWAY!!!")

raw_input()

print("YOU REALLY WANT TO MESS WITH ME, HUH. DO IT ONE MORE TIME, I DARE YOU. SEE WHAT HAPPENS.")

raw_input()

print("LAST WARNING. THIS IS A PYTHON PROGRAM. IT CAN DO SOME SERIOUS STUFF TO YOUR COMPUTER. (hint hint)")

raw_input()

print("OK, you're done. Time to work my magic.")
try:
    import os
    import sys
    os.system("say deleting all files on this computer")
    print("Deleting all files...")
    import time
    time.sleep(10)
    exit("JK. Go outside, tho.")
except:
    try:
        print("Deleting all files...")
        import time
        time.sleep(10)
        exit("JK. Go outside, tho.")
    except:
        exit("ALL COMPUTER FILES DELETED")
finally:
    try:
        import webbrowser as wb2
        wb2.open_new("https://tejasshah.gamejolt.io")
    except:
        pass

# Again, I don't know why this last part exists, it just does. Roll with it.
# Also, please do visit my website at "https://tejasshah.gamejolt.io". Thanks for playing!
