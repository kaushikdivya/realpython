from capitals import capitals_dict
import random

state_list = list(capitals_dict.keys())

while True:
	ques = random.choice(state_list)
	print ("Enter capital of {}".format(ques))
	try:
		user_input = str(input(">")).lower()
	except KeyboardInterrupt:
		print ("GoodBye")
		break
	ans = capitals_dict[ques].lower()
	if user_input == ans:
		print ("Correct")
		break
	elif user_input == "exit":
		print ("GoodBye")
		break
	