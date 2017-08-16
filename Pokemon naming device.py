from __future__ import print_function

hold = 0

while True:
    if hold == 0:
        human_name = raw_input("Hello! This is a program that takes your name and turns it into a pokemon name! What is your name? ").lower()
    else:
        human_name = raw_input("Want to do another one? Go ahead! Or enter 'Leave' to exit. ").lower()

    if human_name == 'leave':
        break

    while not human_name.isalpha():
        human_name = raw_input("Make sure your name only contains letters and is only one word. Try again: ")

    print("")

    like1 = raw_input("What is one thing you like to do? ")

    while not like1.isalpha():
        like1 = raw_input("Make sure your hobby only contains letters and is only one word. Try again: ")

    print("")

    like2 = raw_input("What is one food you like to eat? ")

    while not like2.isalpha():
        like2 = raw_input("Make sure your food only contains letters and is only one word. Try again: ")

    print("")

    print("Hello,", human_name.upper() + "! Let's turn you into a pokemon!")
    print("")

    name_list = list(human_name)

    pokemon_name_list = []

    for item in name_list:
        if item == 'a':
            pokemon_name_list.append('PI')
        elif item == 'b':
            pokemon_name_list.append('MON')
        elif item == 'c':
            pokemon_name_list.append('FLA')
        elif item == 'd':
            pokemon_name_list.append('LU')
        elif item == 'e':
            pokemon_name_list.append('SA')
        elif item == 'f':
            pokemon_name_list.append('ME')
        elif item == 'g':
            pokemon_name_list.append('AR')
        elif item == 'h':
            pokemon_name_list.append('KA')
        elif item == 'i':
            pokemon_name_list.append('GLU')
        elif item == 'j':
            pokemon_name_list.append('CHU')
        elif item == 'k':
            pokemon_name_list.append('MAN')
        elif item == 'l':
            pokemon_name_list.append('KAR')
        elif item == 'm':
            pokemon_name_list.append('SON')
        elif item == 'n':
            pokemon_name_list.append('TU')
        elif item == 'o':
            pokemon_name_list.append('MUS')
        elif item == 'p':
            pokemon_name_list.append('REG')
        elif item == 'q':
            pokemon_name_list.append('PA')
        elif item == 'r':
            pokemon_name_list.append('KLA')
        elif item == 's':
            pokemon_name_list.append('SE')
        elif item == 't':
            pokemon_name_list.append('DOR')
        elif item == 'u':
            pokemon_name_list.append('SUN')
        elif item == 'v':
            pokemon_name_list.append('AS')
        elif item == 'w':
            pokemon_name_list.append('MO')
        elif item == 'x':
            pokemon_name_list.append('GE')
        elif item == 'y':
            pokemon_name_list.append('TRON')
        elif item == 'z':
            pokemon_name_list.append('ZU')

    poke_name = ''.join(pokemon_name_list)

    print('Here is the real name: ', human_name.upper())
    print('Here is your pokemon name: ', poke_name)
    print("")

    print("Hear the pokedex speak!")
    print("A peculiar pokemon, " + poke_name.upper() + ", likes to " + like1.lower() + " and eats " + like2.lower() + ".")
    print("")
    
    consent = raw_input("Are you using a Mac? If so enter 'Y'. Otherwise, put 'N' (or anything that's not 'Y' really). ")
    if consent == 'Y' or consent == 'y':
        import os
        os.system("say a peculiar pokemon, " + poke_name.lower() + ", likes to " + like1 + ", and eats " + like2)

    hold = 1

print("Thank you for using this program to turn names into pokenames!")
