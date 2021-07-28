def run(input):
	name = "Bot"
	if "hi" == input or "hello" == input:
		print("hi")
	elif "how are you" == input:
		print("Fine, you?")
	elif "what is your name" == input or "who are you" == input:
		print("I am", name)
	elif "exit" == input:
		print("exited")
		return False
	else:
		print("Sorry.. I can't understand what are you asking for.")
	
while True:
	cmd = input(">> ").lower()
	fun = run(cmd)
	if fun == False:
		break
