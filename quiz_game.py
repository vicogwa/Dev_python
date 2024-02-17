print("welcome to the game land")
game_land = input("do you want to play? ")

if game_land.lower() != 'yes':
    quit() 

print("okay, let play.") 
score = 0

question = input("what is your favorite pets? ")
if question == 'dog' or 'cat' or 'bird':
    print("correct!")
    score += 5
else:
    print("incorrect!")

question = input("what is the meaning of HRM? ")
if question == 'human resources manager':
    print("correct!")
    score += 5
else:
    print("incorrect!")

question = input("what is the meaning of RAM? ")
if question == 'random access memory':
    print("correct!")
    score += 5
else:
    print("incorrect!")

if score >= 10:
    print("wow! you got the total score of ",  str(score))

else:
    print("ohoh! you lost, try more.")    
