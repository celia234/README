
liste1 = [[1, 4, 6, 0, 36, 309, "A"], ["A", "C", 9, "G"]]
print(liste1[1][2])

print ("helloword")

def factorielle(n):
    if n < 2:
        return 1
    else:
        return n * factorielle(n - 1)
print(factorielle(3))       

#J'ai fait un [jeu](https://www.codingame.com/ide/puzzle/the-descent) en ligne où le but était de détruire des montagnes afin de
passer par dessus sans se faire écraser. Le programme ci-dessous est la solution du jeu :

import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.


# game loop
while True:
    mountain_h=0
    m=0
    for i in range(6):
        v = int(input())
        if  v > mountain_h:
            mountain_h = v
            m =  i # represents the height of one mountain.

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # The index of the mountain to fire on.
    print(m)
    
        
