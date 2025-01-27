import random

go_shopping = True

while go_shopping == True:

  shop_ques = input("Would you like to go shopping at the grocery store? Answer in Yes or No. ")

if shop_ques == "Yes":
  go_shopping = True
elif shop_ques == "No":
  go_shopping = False
  print("Thanks for shopping!")


grocery_section_list = ["Butcher","Vegetables","Seafood", "Pastries"]

budget_list = [12, 50, 1000, 500, 2000]

random.shuffle(budget_list)

grocery_budget = budget_list[0]

budget_check = input("How expensive are your groceries?")

num_budget_check = int(budget_check)

if num_budget_check <= grocery_budget:
  print("Yay, you can buy your groceries")