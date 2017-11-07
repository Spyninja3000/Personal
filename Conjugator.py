# Spanish verb conjugator
# By: Tejas Shah

ar = {             'yo':'o',
                   'tu':'as',
                   'el':'a',
                   'ella':'a',
                   'usted':'a',
                   'nosotros':'amos',
                   'vosotros':'ais',
                   'ellos':'an',
                   'ellas':'an',
                   'ustedes': 'an',
                   }
er = {            'yo':'o',
                   'tu':'es',
                   'el':'e',
                   'ella':'e',
                   'usted':'e',
                   'nosotros':'emos',
                   'vosotros':'eis',
                   'ellos':'en',
                   'ellas':'en',
                   'ustedes': 'en',
                   }
ir = {            'yo':'o',
                   'tu':'es',
                   'el':'e',
                   'ella':'e',
                   'usted':'e',
                   'nosotros':'imos',
                   'vosotros':'is',
                   'ellos':'en',
                   'ellas':'en',
                   'ustedes': 'en',
                   }

word_dict = {'ar': ar, 'er': er, 'ir': ir}

def conjugate(verb, noun):
    verbx = list(str(verb).lower())
    if verbx[len(verbx) - 2] == 'a':
        try:
            end = (word_dict['ar'])[str(noun)]
        except KeyError:
            end = "YOU_DIDN'T_ENTER_A_REAL_SPANISH_NOUN"
    elif verbx[len(verbx) - 2] == 'e':
        try:
            end = (word_dict['er'])[str(noun)]
        except KeyError:
            end = "YOU_DIDN'T_ENTER_A_REAL_SPANISH_NOUN"
    elif verbx[len(verbx) - 2] == 'i':
        try:
            end = (word_dict['ir'])[str(noun)]
        except KeyError:
            end = "YOU_DIDN'T_ENTER_A_REAL_SPANISH_NOUN"
    else:
        end = "YOU_DIDN'T_ENTER_A_REAL_SPANISH_VERB"
    verbx.pop(len(verbx) - 2)
    verbx.pop(len(verbx) - 1)
    verbx.append(end)
    new_verb = ''.join(verbx)
    return new_verb

def main():
    print("Conjugate Verbs in Spanish!")
    repeat = True:
    while repeat:
        verb = raw_input('Please enter a verb to be conjugated. ')
        while not type(verb) is type('str'):
            verb = raw_input("Please enter the verb you would like us to conjugate. Make sure it's a word. ")
        noun = raw_input('Please enter the noun used in the context. ')
        while not type(noun) == type('str'):
            noun = raw_input("Noun in context? Make sure it's a word. ")
        new = conjugate(verb, noun)
        print("Your conjugated verb is: " + new)
        print("")
        repeat_x = raw_input("Would you like to do another one? Please enter 'y' or 'n'. ").lower()
        if repeat_x == 'n':
            repeat = False  

if __name__ == '__main__':
    main()
