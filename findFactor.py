def factor_chain(lst):
	for i, num in enumerate(lst):
		if i !=0 and num % lst[i-1] != 0:
			return False
	return True

#https://edabit.com/challenge/rj7E4k6vSNZ9KpT9c