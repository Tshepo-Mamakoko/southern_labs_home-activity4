# Southern Labs Institute of Technology
# Student : Tshepo Mamakoko
# Activity: Home Activity 4: Python,Git Bash, Vim and Flowchart

import data_utils
import random
import datetime

def main():

	"""
	It must use random.randint to generate a list of 5 random transactions
	It must use datetime.date.today() to get todays date
	It must call data_utils.calculate_average() to compute the mean value
	It must print a formatted summary displaying the date, generated values
	and claculated currency string

	"""

	random_number = random.randint(min_val, max_val)
	date_today = datetime.date.today()
	mean_value = data_utils.calculate_average
	summary = print("These are the results")

	print(date_today)
	print(mean_value)
	return random.randint(50, 500)
	pass

main()

if __name__ == "__main__":
	main()
