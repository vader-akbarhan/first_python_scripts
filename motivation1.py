print("Value of __name__ is: ", __name__)
if __name__=="__main__": 
	print('Yes, the __name__ is "__main__". ')

class Motivation(): 
#	def __init__(self):
#		print("The class Motivation was initiated.") 

	def Rates(yearly_salary): 
		yearly_salary = int(yearly_salary)
		monthly = round((yearly_salary / 12), 0) 
		daily = round(monthly / 21, 0) 
		hourly = round(daily / 8, 0)
		print("The monthly salary is {0}. \nThe daily salary is {1}. \nThe hourly salary is {2}".format(monthly, daily, hourly))
	def Expertise(level = input('Type a level: "beginner", "intermediate" or "expert". ')): 
		#
		# level = input('Type a level: "beginner", "intermediate" or "expert". ')
		# The line above produces the following error: 
		# Type the required level: "beginner", "intermediate" or "expert". level
		# Traceback (most recent call last):
  		# File "motivation1.py", line 23, in <module> 
    	# Motivation.Expertise(check_level)
		# TypeError: Expertise() missing 1 required positional argument: 'level'
		#
		if level=="beginner": 
			print("You can do it, hopefully, soon.")
		elif level=="intermediate":
			print("You MUST be heading towards such a level.")
		elif level == "expert":
			print("You would develop another profession before starting imaging happiness mediated by salary for expert IT skills.")
		else: print("Type one of the levels.")
		print("Globals: ", globals)
		print("Locals: ", locals)
# Motivation().Expertise()
#check_salary = input("Enter the salary from the job offer: ")
#Motivation.Rates(check_salary) 

# check_level = input('Type the required level: "beginner", "intermediate" or "expert". ')
# Motivation.Expertise(check_level)
#Motivation.Expertise()
