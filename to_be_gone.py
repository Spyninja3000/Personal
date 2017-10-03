from __future__ import print_function
import re
import random
import time
# eradicates to-be verbs in a sentence
# works okay enough to spit out an english sentence like it's being spoken by an immigrant
# by: Tejas Shah

def eradicate(sentence):
    to_be_verbs = ['am', 'is', 'are', 'was', 'were', 'be', 'being', 'been', 'has', 'have', 'had', 'do', 'does', 'did']
    better = ['become', 'became', 'exist as', 'exists as', 'act']
    sent_list = re.sub("[^\w]", " ", sentence).split()
    for i in to_be_verbs:
        if i in sent_list:
            for n,x in enumerate(sent_list):
                if x == i:
                    sent_list[n] = random.choice(better)
    new_sentence = ' '.join(sent_list)
    return new_sentence

def main():
    print("Hello! Welcome to TO-BE-GONE, the python program that lets you eradicate ")
    print("all to-be verbs that your LA teacher hates from a sentence/essay/string.")
    strx = raw_input("Please enter a sentence that you would like TO-BE-ERADICATED! ")
    if not list(strx)[0].isalpha():
        strx = raw_input("I'm not dumb. Enter something composed of actual English words only, please. ")
    if not list(strx)[0].isalpha():
        strx = raw_input("So this is how you want to play, huh. Well then, I can play that way too. Please don't make me do something I'm gonna regret. ")
    if not list(strx)[0].isalpha():
        strx = raw_input("Last warning. Just put in a sentence and we're good. ")
    if not list(strx)[0].isalpha():
        print("Okay then. I see. Game on.")
        print("I shall now delete all files on this computer, then.")
        try:
            import os
            os.system("say Are you sure you would like to delete all files? Override Access Granted Deleting all files... ")
            print("Are you sure you would like to delete all files? Override Access Granted Deleting all files... ")
            time.sleep(10)
        except ImportError:
            print("Are you sure you would like to delete all files? Override Access Granted Deleting all files... ")
            time.sleep(10)
        exit()

    done = eradicate(strx)
    print(done)

if __name__ == '__main__':
    main()