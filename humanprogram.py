import os
import pyttsx3

pyttsx3.speak("Welcome to my tools")

while True:
	print("chat with me with your requirements : " , end ='')
	x = input().lower()

	if (("not" in x) or ("dont" in x) or ("don't" in x) or ("do not" in x)):
		print("Okay!!then What you want to open?")

	elif (("run" in x ) or ("execute" in x) or ("open" in x) or ("launch" in x)) or ("start" in x):
		
		if ("chrome" in x) or ("browser" in x):
			os.system("chrome")
		elif ("notepad" in x) or ("editor" in x) or ("text editor" in x):
			os.system("notepad")
		elif ("jupyter" in x) or ("jupyter notebbok" in x) or ("python ide" in x):
			os.system("jupyter notebook")
		elif ("calculator" in x):
			os.system("calc")
		elif ("vlc player" in x) or ("media player" in x) or ("video player" in x):
			os.system("vlc")
		elif ("paint" in x) or ("mspaint" in x):
			os.system("mspaint")
		elif ("ms" in x) or ("microsoft" in x):
			if ("excel" in x):
				os.system("excel")
			elif ("word" in x):
				os.system("winword")
			elif ("power point" in x) or ("ppt" in x) or ("powerpoint" in x):
				os.system("powerpnt")
			else:
				print("Sorry!Command not found, Please try again with the right command")

		elif ("excel" in x):
			os.system("excel")
		elif ("word" in x):
			os.system("winword")
		elif ("power point" in x) or ("ppt" in x) or ("powerpoint" in x):
			os.system("powerpnt")
		
		else:
			print("Sorry!Command not found, Please try again with the right command")

        
	elif ("chrome" in x) or ("browser" in x):
		os.system("chrome")
	elif ("notepad" in x) or ("editor" in x) or ("text editor" in x):
		os.system("notepad")
	elif ("jupyter" in x) or ("jupyter notebbok" in x) or ("python ide" in x) or ("pythonide" in x):
		os.system("jupyter notebook")
	elif ("calculator" in x):
		os.system("calc")
	elif ("vlc player" in x) or ("media player" in x) or ("video player" in x):
		os.system("vlc")
	elif ("paint" in x) or ("mspaint" in x):
		os.system("mspaint")
	elif ("ms" in x) or ("microsoft" in x):
		if ("excel" in x):
			os.system("excel")
		elif ("word" in x):
			os.system("winword")
		elif ("power point" in x) or ("ppt" in x) or ("powerpoint" in x):
			os.system("powerpnt")
		else:
			print("Sorry!Command not found, Please try again with the right command")
 		
	elif ("excel" in x):
		os.system("excel")
	elif ("word" in x):
		os.system("winword")
	elif ("power point" in x) or ("ppt" in x) or ("powerpoint" in x):
		os.system("powerpnt")
		
	
		
	elif ("exit" in x) or ("stop" in x) or ("quit" in x) or ("out" in x):
		break
	else:
		print("Sorry!Command not found, Please try again with the right command")