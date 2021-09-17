#!/usr/bin/env python
# coding: utf-8

# # Task 4

# In[ ]:


amount = int(input("How many items do you want to purchase?"))

if 0 <= amount < 10:
    print("Your amount is:", amount, ".", "The cost is: $", amount * 12, ".")
elif 10 <= amount < 100:
    print("Your amount is:", amount, ".", "The cost is: $", amount * 10, ".")
elif amount >= 100:
    print("Your amount is:", amount, ".", "The cost is: $", amount * 7, ".")
else:
    print("You can not buy negative amount!")


# # Task 5

# In[7]:


import random
n = 0
a = 0
p = 0
while n<3:
    player = input("Your turn:")
    print("Player: ", player)
    ai = random.randrange(0,3)
    ai_return = {0: "Rock", 1: "Paper", 2: "Scissors"}
    print("AI:", ai_return[ai])
    if player == "Rock" and ai_return[ai] == "Paper":
        a += 1
        print("General score:\n P:",p,"A:",a)
    elif player == "Rock" and ai_return[ai] == "Scissors":
        p += 1
        print("General score:\n P:",p,"A:",a)
    elif player == "Paper" and ai_return[ai] == "Scissors":
        a += 1
        print("General score:\n P:",p,"A:",a)
    elif player == "Paper" and ai_return[ai] == "Rock":
        p += 1
        print("General score:\n P:",p,"A:",a)
    elif player == "Scissors" and ai_return[ai] == "Rock":
        a += 1
        print("General score:\n P:",p,"A:",a)
    elif player == "Scissors" and ai_return[ai] == "Paper":
        p += 1
        print("General score:\n P:",p,"A:",a)
    else:
        print("Draw! General score:\n P:",p,"A:",a)
    n += 1

if p > a:
    print("Player wins!")
elif p < a:
    print("AI wins!")
else:
    print("It's a draw!")


# # Task 6

# In[40]:


def operations_in_list():
    
    """
    Asks the user to enter a list of integers and do the following:

    Print the total number of items in the list.
    Print the last item in the list.
    Print the list in reverse order.
    Print Yes if the list contains a 5 and No otherwise.
    Print the number of fives in the list.
    Remove the first and last items from the list, sort the remaining items, and print the result.
    Print how many integers in the list are less than 5.
    """
    
    integer = None
    user = []
    while integer != 0:
        integer = int(input("Enter your integer. If you are done, enter 0."))
        user.append(integer)
    user.pop(-1)
    print(len(user))
    print(user[-1])
    print(list(reversed(user)))
    if 5 in user:
        print("Yes")
    else:
        print("No")
    n = 0
    for i in user:
        if i == 5:
            n+=1
    print(n)
    user.pop(0)
    user.pop(-1)
    user.sort()
    print(user)
    n = 0
    for i in user:
        if i < 5:
            n+=1
    print(n)
    
operations_in_list()


# In[ ]:




