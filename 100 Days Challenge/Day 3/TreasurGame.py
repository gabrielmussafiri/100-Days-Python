print("Welcome to Treasure Game /n Your mission is to find the the threasure")
answer =input("You're at a cross road , Where do you want to go? Type Left or Right: \t ").lower()
if answer == "Left":
    answer2 = input("You come to a lake , There is an island in the middle of the lake. Type WAIT to wait for a boat. Type SWIM to swim across ").lower()
    if answer2 =="Wait":
        answer3 = input("You arrive at the island unharmed. There is a house with 3 doors. one red , one yellow and blue which color do you choose?").lower()
    else:
        print("Game over")
    if answer3 =="yellow":
        print(" You win")
    else : 
        print(" Game over")
else :
    print("Game over")
        

   