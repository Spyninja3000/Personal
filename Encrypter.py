# Property of Tejas Shah
# This program runs on a custom-made algorithm I like to call 'metahexahashing'.
# The code is hashed, then hexed, then hashed, then hexed, and then stored in a secure mega-dictionary
# The main feature is the decrypter, which goes back into this mega-dictionary and retrieves the
# original state of the metahexahash, thus disproving the long assumed fact that hashing is one-way.
# The program single-handedly undoes hexing and hashing twice each and returns a value
# Now, this may be due to the fact that I hex it last, but I think it still provides a secure
# encryption for raw data. Also, it works with any combination of any keyboard character :)

class Encrypt:
    def __init__(self, raw, done):
        self.raw = raw
        self.done = done

    def encrypt(self):
        raw1 = self.raw
        done = hex(hash(hex(hash(raw1))))
        return done

    def decrypt(self):
        decrypt = raw_input("What would you like to decrypt? What's the output? ")
        megadict = create_dict()
        return megadict[decrypt]

def main():
    while True:
        password = raw_input("Password to Encrypt? Put in 'decrypt' to access the decrypter. ")
        if password.lower() == 'decrypt':
            de = Encrypt(0, 0).decrypt()
            print "Here's the decoded version: " + de + ". I'm assuming that since you probably waited a very long time "
            print "for the code to load that you deserve the decryption a lot. It takes a while to decrypt this secure form of code."
            print""
        else:
            Code = Encrypt(password, Encrypt(password, 0).encrypt())
            en = Code.encrypt()
            print "Here's the hexahashed version: " + en
            print ""

def create_hashlist():
    characters = []
    i = 0
    while i < 128:
        characters.append(str(chr(i)))
        i += 1
    return characters

def create_possible_combo():
    hashlist = create_hashlist()
    super_list = []
    from itertools import chain, combinations
    def all_subsets(y):
        return chain(*map(lambda x: combinations(y, x), range(0, len(y) + 1)))
    for subset in all_subsets(hashlist):
        super_list.append(subset)

    return super_list

def create_dict():
    megalist = create_possible_combo()
    megadict = {}
    for i in megalist:
        megadict[hex(hash(hex(hash(i))))] = i
    return megadict

if __name__ == '__main__':
    main()