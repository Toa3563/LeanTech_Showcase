#Cannon Rivera
#Lean Techniques Interview Program Problem
#input_file
#User can input any amount of money(up to 2 decimals)
#Units in US currency(least amount of change given)
    #Example $19.10
    #1 - $10 bill
    #1 - $5 bill
    #4 - $1 bills
    #1 - dime
contine=True
def main():
    while contine:
        user_money = input_data()
        hundred_rounded, fifty_rounded, twenty_rounded, tens_rounded, fives_rounded, ones_rounded, quarters_rounded, dimes_rounded, nickels_rounded, pennies=calc(user_money)
        output(user_money,hundred_rounded, fifty_rounded, twenty_rounded, tens_rounded, fives_rounded, ones_rounded, quarters_rounded, dimes_rounded, nickels_rounded, pennies)


def input_data():
    while True:
        try:
            user_money = round(float(input("Enter any amount of money up to 2 decimals ")),2)
            break
        except ValueError as e:
            print("Please Enter a Number")

    return user_money

def calc(user_money):
    while user_money != 0:
        if user_money >= 100:
            hundred = user_money/100
            hundred_rounded = round(hundred-.05)
            user_money -= (100 * hundred_rounded)
        else:
            hundred_rounded = 0
        if user_money >= 50:
            fifty = user_money/50
            fifty_rounded = round(fifty-0.5)
            user_money -= (50 * fifty_rounded)
        else:
            fifty_rounded = 0
        if user_money >= 20:
            twenty = user_money/20
            twenty_rounded = round(twenty-0.5)
            user_money -= (20 * twenty_rounded)
        else:
            twenty_rounded = 0
        if user_money >= 10:
            tens = user_money/10
            tens_rounded = round(tens-0.5)
            user_money -= (10 * tens_rounded)
        else:
            tens_rounded = 0
        if user_money >= 5:
            fives = user_money/5
            fives_rounded = round(fives-0.5)
            user_money -= (5 * fives_rounded)
        else:
            fives_rounded = 0
        if user_money >= 1:
            ones = user_money/1
            ones_rounded = round(ones-0.49999)
            user_money -= (1 * ones_rounded)
        else:
            ones_rounded = 0
        if user_money >= 0.25:
            quarters = user_money/0.25
            quarters_rounded = round(quarters-0.5)
            user_money -= (0.25 * quarters_rounded)
        else:
            quarters_rounded = 0
        if user_money >= 0.10:
            dimes = user_money/0.10
            dimes_rounded = round(dimes-0.5)
            user_money -= (0.10 * dimes_rounded)
        else:
            dimes_rounded = 0
        if user_money >= 0.05:
            nickels = user_money/0.05
            nickels_rounded = round(nickels-0.5)
            user_money -= (0.05 * nickels_rounded)
        else:
            nickels_rounded = 0
        if user_money >= 0.01:
            pennies = round(user_money/0.01)
            user_money -= (0.01 * pennies)
        else:
            pennies = 0

        return hundred_rounded, fifty_rounded, twenty_rounded, tens_rounded, fives_rounded, ones_rounded, quarters_rounded, dimes_rounded, nickels_rounded, pennies

def output(user_money, hundred_rounded, fifty_rounded, twenty_rounded, tens_rounded, fives_rounded, ones_rounded, quarters_rounded, dimes_rounded, nickels_rounded, pennies):
    global contine
    print(f"The amount put in was {user_money}\n")
    print(f"Your bills sorted are:\n"
          f"{hundred_rounded} = hundreds\n"
          f"{fifty_rounded} = fifties\n"
          f"{twenty_rounded} = twenties\n"
          f"{tens_rounded} = tens\n"
          f"{fives_rounded} = fives\n"
          f"{ones_rounded} = ones\n"
          f"{quarters_rounded} = quarters\n"
          f"{dimes_rounded} = dimes\n"
          f"{nickels_rounded} = nickels\n"
          f"{pennies} = pennies\n")

    while True:
        var=input("Would you like to continue?Y/N ")
        if var=="N":
            contine=False
            break
        elif var=="Y":
            break
main()