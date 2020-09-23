import random
r = random.randint(1, 100)
while True:
	nbr = input('請猜個數字: ')
	nbr = int(nbr)
	if nbr == r:
		print('恭喜!你猜中了!')
		break
	elif nbr > r:
		print('比答案大!再猜小一點!')
	elif nbr < r:
		print('比答案小!再猜大一點!')