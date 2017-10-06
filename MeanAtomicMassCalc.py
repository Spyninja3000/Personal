from __future__ import print_function

# This program calculates Average Atomic Mass of isotopes of an element from the isotopic mass and abundance
# By: Tejas Shah

def calculate(dictx):
    sumitup = []
    for key in dictx:
        sumitup.append(float(dictx[key]) * float(key))
    total = 0
    for i in sumitup:
        total += float(i)
    return total

def main():
    print("Hello! This calculates Average Atomic Mass! Let's get started! ")
    dictx = {}
    while True:
        mass = raw_input("What is the atomic mass of the isotope? ")
        try:
            num_mass = float(mass)
        except:
            mass = raw_input("Enter a number only. ")
            num_mass = float(mass)
        abundance = raw_input("What is the abundance of the isotope with a mass of " + mass + "? ")
        try:
            num_abundance = float(abundance)
        except:
            abundance = raw_input("Enter a number only. ")
            num_abundance = float(abundance)
        dictx[num_mass] = num_abundance
        done = raw_input("Are there more isotopes of this element? Please enter 'Y' or 'N'. ")
        if done.lower() == "n" or done.lower() == "no":
            break
    answer = calculate(dictx)
    print("Your average atomic mass is: " + answer)

if __name__ == '__main__':
    main()
