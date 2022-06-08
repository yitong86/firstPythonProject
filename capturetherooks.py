def can_capture(rooks):
	if rooks[0][0] == rooks[1][0] or rooks[0][1] == rooks[1][1]:
		return True
	else:
		return False

	#https://edabit.com/challenge/TZ8J2ryBPd6i9ugqR