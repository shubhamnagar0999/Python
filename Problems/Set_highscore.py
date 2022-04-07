'''score = 44
if score == 1:
    hs = open("highScore.txt","w")
    hs.write(str(score))
    hs.close()
else:
    hs = open("highScore.txt","w")
    hs.write(str(score))
    hs.close()

#with statement:

def score():
    return 555
j = score()

with open("highScore.txt") as h:
    hscore = int(h.read())

if hscore<j:
    with open("highScore.txt","w") as hs2:
        hs2.write(str(j))
'''


