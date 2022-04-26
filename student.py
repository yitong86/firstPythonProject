print("Welcome to Careerdevs!")

careerdevs = ["sophia", "Kat", "Mayra"]

accept = input("Do you learn from Careerdevs?\n(yes/no): ")

if accept == "yes":
    name = input("What's your name?")
    for stud_name in careerdevs:
        if name == stud_name:
            print("Okay, you're a student")
        else:
            print("You're not a student")
else:
    print("Okay, you can leave")
