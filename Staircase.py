from __future__ import print_function
listx = []

x = raw_input("How long is the staircase? ")
if x.isdigit():
    x = int(x)
else:
    print('You')
    print('\thad')
    print('\t\tthe')
    print('\t\t\taudacity')
    print('\t\t\t\tto')
    print('\t\t\t\t\tput')
    print('\t\t\t\t\t\tin')
    print('\t\t\t\t\t\t\tan')
    print('\t\t\t\t\t\t\t\tactual')
    print('\t\t\t\t\t\t\t\t\tnon-number!')
    print('\t\t\t\t\t\t\t\t\t\tYou')
    print('\t\t\t\t\t\t\t\t\t\t\tshall')
    print('\t\t\t\t\t\t\t\t\t\t\t\tbe')
    for i in range(1, 50, 1):
        print("")
    print('rewarded with a pleasant surprise!')
    x = 0

for w in range(1, x, 1):
    listx.append(' ')

done = []
for j in listx:
    done.append(j)
    new = str(''.join(done))
    if len(done) % 2 == 0:
        y = '--'
    else:
        y = ' |'
    print(new + y)

# staircase maker
# pretty gr8 if you ask me
# By: Tejas Shah