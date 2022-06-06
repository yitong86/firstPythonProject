def minutes_to_seconds(time):
    list = time.split(":")
    if int(list[1]) < 60:
        return int(list[1]) + int(list[0]) * 60
    else:
        return False

# https://edabit.com/challenge/Ff84aGq6e7gjKYh8H
