# How Much is True?
# https://edabit.com/challenge/vKpGt4ufSKmEJ3Xjd

# Difference of Max and Min Numbers in Array
# https://edabit.com/challenge/hymPkXdhmDQLe87QT

# The 3 Programmers Problem
# https://edabit.com/challenge/akHQKSkHT26TuA7Ka

# Re-Form the Word
# https://edabit.com/challenge/R3PnRquBPADEqDxZg

# Scoring System
# https://edabit.com/challenge/FRtmuYD26pcQWFR7k

# Xs and Os, Nobody Knows
# https://edabit.com/challenge/bkFqwEP5Gej23didA

# Get the File Name
# https://edabit.com/challenge/hgHMhpJjyFxYJMMXp

# Factor Chain
# https://edabit.com/challenge/SvptD77rYQJgjDvZY

# Repeating Letters N Times
# https://edabit.com/challenge/HDk4PC9w6KPS3X25W

# Spaces Between Each Character
# https://edabit.com/challenge/ryEdPW2eqyngyWayy

# Is the String a Palindrome?
# https://edabit.com/challenge/cwLnTvxpBX5espEgs


def cli():
    while True:
        print("\n______________\n")
        print("1) How much is True?")
        print("2) Difference of Max and Min Numbers in Array?")
        print("3) Character frequency count ")
        print("Exit) Exit The Program")
        print("\n______________\n")

        choice = input("Choose An Algorithm\nInput: ")

        if choice == "Exit":
            exit()
        elif choice == "1":
            how_much_is_true()
        elif choice == "2":
            difference_max_min()
        elif choice == "3":
            count_char_freq()



def how_much_is_true():
    bool_lists = [
        [True, False, False, True, False],
        [False, False, False, False],
        [],
        [False, False, True, True, False, False, False, True, True, True, True, False, True, True, False],
        [True, False, True, True, False, False, False, False, False],
        [False, True, True, False, True, True, False, True, False, True, False, True, False, True, False],
        [True, False, True, True, True, False, True, True, False, False],
        [False, False, False, False, True, False, True, False, True, False, False],
        [True, False, False, False, True, False, False, True, False, False, False],
        [True, True, False, True, False, False, False, False, True, False],
        [True, False, True, True, False, True, True, True, True, False, True, False, True, False],
        [True, False, True, True, True, True, False, True, True, False, True, False, False, False, False],
        [True, True, False, False, False, False, True, False, True, True, False, True]
    ]
    print("\nHow Much Is True?\n")
    print("Lists to count:")
    for i, bool_list in enumerate(bool_lists):
        print(str(i + 1) + ": " + str(bool_list))
        #1: [True, False, False, True, False]

    list_choice = int(input("\nList Num: ")) - 1
    test_list = bool_lists[list_choice]

    true_count = 0
    false_count = 0
    for boolean in test_list:
        if boolean:
            true_count += 1
        else:
            false_count += 1

    print("List: " + str(test_list) + "\nTrue: " + str(true_count) + "\nFalse: " + str(false_count))


def difference_max_min():
    test_lists = [
        [10, 4, 1, 4, -10, -50, 32, 21],  # 82
        [44, 32, 86, 19],  # 67
        [10, 4, 1, 2, 8, 91],  # 90
        [-70, 43, 34, 54, 22]  # 124
    ]
    print("Lists to count:")
    for i, t_list in enumerate(test_lists):
        print(str(i + 1), ": ", str(t_list))
    list_choice = int(input("\nList Num: ")) - 1
    test_list = test_lists[list_choice]

    min_num = min(test_list)
    max_num = max(test_list)
    print("Smallest number is " + str(min_num) + ",highest is " + str(max_num) + ".")
    print("The difference is " + str(max_num - min_num))


def count_char_freq():

    print()
    input_str = input("Enter a string to count the character frequencies\nInput: ")
    freq = {}
    for char in input_str:
        freq[char] = freq.get(char, 0) + 1

    for key, count in freq.items():
        print(key + ": " + str(count))


cli()
count_char_freq()