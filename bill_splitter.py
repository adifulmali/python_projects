# write your code here
import random

no_of_frnds = int(input("Enter the number of every friend joining (including you):\n"))
if no_of_frnds <= 0:
    print("No one is joining for the party")
else:     
    friends = dict()
    print("Enter the name of every friend (including you), each on a new line:")
    while no_of_frnds:
        name = input()
        friends[name] = 0
        no_of_frnds -= 1

    total_bill = int(input("Enter the total bill value:\n"))

    check = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
    if check == 'Yes':
        lucky = random.choice(list(friends.keys()))
        print(f"{lucky} is the lucky one!\n")
        for remain in friends.keys():
            if remain != lucky:
                friends[remain] = total_bill // (len(friends) - 1)
    else:
        print("No one is going to be lucky")
        split = round((total_bill / len(friends)), 2)
        for remain in friends.keys():
            friends[remain] = total_bill // len(friends)

    print(friends)
