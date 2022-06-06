COMPANY_NAME = "Tech Inc."

EMPLOYEES = ["Alice", "Bob", "Cameron", "Dan", "Ellen", "Frank", "Grace", "Harry"]

# Welcome message + employee names listed out
print("\nWelcome to the " + COMPANY_NAME + " employee check-in\n")
print("We at " + COMPANY_NAME + " are very proud of our employees: ")
for emp_name in EMPLOYEES:
    print("-- " + emp_name)
print("\n")


# user input section (buggy code)
# checking just the beginning of a string: .startWith("") or [0]
# case insensitive checks: .tolower() or .casefold()
# removing whitespace: .strip()
def checker():
    accept = input("Do you work for " + COMPANY_NAME + "?\n(yes/no): ")
    if accept == "yes" or accept.startswith("y"):
        name = input("What is your name?\nName: ")

        for emp_name in EMPLOYEES:
            # python string remove whitespacepython,Ignore capitalization of characters in the user’s input
            if name.casefold().replace(" ", "") == emp_name.casefold():
                print("Thank you " + emp_name + ", you are now checked in.")
                break

            else:
                print("You're not an employee")


    elif accept == "no" or accept.startswith("n"):
        print("This service is not for you. Exiting program...")
        exit()
    else:
        accept = input("Do you work for " + COMPANY_NAME + "?\n(yes/no): ")
        checker()
checker()
exit()
