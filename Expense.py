import math
import time

print("Welcome to the expense tracker! \n\n")


# procedure to find the average
def average():
  average = sum(expenses) / len(expenses)
  print("Average of list: " + str(average))


# find max or min procedure
def find_max(decision10):
  done10 = False
  while done10 == False:
    if decision10 == 2:
      print("Most expensive item costs: " + str(max(expenses)))
      done10 = True
    elif decision10 == 1:
      print("Cheapest item costs: " + str(min(expenses)))
      done10 = True
    else:
      print("Sorry wrong input, type 1 or 2 try again")
      decision10 = int(
          input(
              "Do you want to find the cheapest expense (press 1) or the most expensive (press 2)?:  "
          ))
      done10 = False


#  expence tracker idea: user inputs values which are stored in a list.
#Once all of their values are in they will see their list and a set of options.
#these options would be: update their list, find the average, find min/max, etc.
#a lot of room for creativity!!!

expenses = []


def main():
  done1 = False
  done2 = False
  # this is the section that will be used to collect the expenses and store them in a list
  while done1 == False:
    expense = float(input("Type a value of your expenditure (#number#):  "))
    print()
    expenses.append(expense)
    done2 = False
    while done2 == False:
      decision1 = input(
          "Do you want to add another value or continue to perform actions with your list (type add or continue):  "
      )
      print()
      if decision1 == "add":
        done2 = True
        done1 = False
      elif decision1 == "continue":
        done2 = True
        done1 = True
      elif decision1 != "add" or decision1 != "continue":
        print("False input, try again")
        print()
        done2 = False

  # after the expenses are stored in a list, the options are provided here
  time.sleep(1)
  print("Great, we have stored your value(s) inside of a list.")
  print("Now, what action do you want to perform with your list?")

  done3 = False
  done4 = False
  while done3 == False:
    print()
    print("a) Find the average of your expenses")
    print("b) Find the most expensive/cheapest expenditure")
    print("c) Show your list")
    print("d) Change/add to your list")
    print()
    decision2 = input("What do you want to do? ")

    if decision2 == "a":
      average()
      done3 = True
      done4 = False
    elif decision2 == "b":
      decision10 = int(
          input(
              "Do you want to find the cheapest expense (press 1) or the most expensive (press 2)?:  "
          ))
      find_max(decision10)
      done3 = True
      done4 = False
    elif decision2 == "c":
      print(expenses)
      done3 = True
      done4 = False
    elif decision2 == "d":
      done3 = True
      done4 = False
      main()
    elif decision2 != "a" or decision2 != "b" or decision2 != "c" or decision2 != "d":
      print("False input, try again")
      done3 = False
      done4 = False
    print()
    #these next lines will determine wether or not the program will end or repeat.
    while done4 == False:
      decision3 = input("Do you wish to perform another task? (y or n):  ")
      if decision3 == "y":
        done3 = False
        done4 = True
      elif decision3 == "n":
        done3 = True
        done4 = True
        print()
        print("Thank you for using Expense Tracker! Have a nice day! ")
      elif decision3 != "y" or decision3 != "n":
        print("False input, try again!")
        done4 = False


main()
