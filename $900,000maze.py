name = input("Enter your name: ")
print("Welcome", name ,"to this avendture!")
answer = input("You are in a maze and if complete you win $900,000 which way would you like to go right or left? ").lower()
if answer == "left":
  answer = input("You encounter a monster, would you like to or run attack?").lower()
  if answer == "attack":
    print("You have been eaten by the monster")
    print("That was not the greatest idea, you lost!")
    print("Game over")
  if answer == "run":
    print("You have excaped the maze")
    print("You have won $900,000 cash")
    print("Game over")
elif answer == "right":
    print("You encounter a hacker and he says you have been hacked you loose $900,000")  
    print("Game over")
