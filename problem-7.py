def run(input):
	
	if "hi" == input:
		print("hi")
	elif "how are you" == input:
		print("Fine, you?")
	elif "what is your name" == input or "who are you" == input:
		print("I am Bot")
	
while True:
	cmd = input(">> ").lower()
	run(cmd)