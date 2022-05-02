print("Welcome to Careerdevs!Are you a student? Lets find out…")

students = ["sophia", "John", "Bob", "Lucy"]


def checker():
     accept = input("Are you a student?\n(yes/no): ")

    if accept == "yes" or accept.startswith("y"):
        name = input("What's your name?")
        for stud_name in students:
            if name.casefold().replace(" ", "") == stud_name.casefold():
                print("Welcome to class")
                break
        else:
            print("You’re not supposed to be here")
    elif accept == "no" or accept.startswith("n"):
        exit()
    else:
        checker()


checker()
exit()
