




def to_usd(my_price):

	"""
	This is a doctstring. It tells us what this function is about.

	Invoke like this: to_usd(9.999)

	"""

	return '${:,.2f}'.format(my_price)





if __name__ == "__main__":

		price = input("Please choose a price like 4.9999")

		print(to_usd(float(price)))