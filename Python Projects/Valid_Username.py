username = input("Please insert your username here: ")
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
Capital_List = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

if len(username) > 12:
    print("Invalid username. Needs to be shorter than 12 characters. Try again: ")
elif not username.find(" ") == -1:
    print("Invalid username. No spaces or dashes. Try again: ")
elif username.isalpha == False:
    print("Invalid username. No numbers. try again: ")
else:
    print(f"Welcome {username}!")