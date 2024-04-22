import pyfiglet
from termcolor import colored

def wish_happy_easter():
	easter_message = pyfiglet.figlet_format("Happy Easter")
	colored_message = colored(easter_message, color='yellow', attrs=['bold'])
	
	additional_text = colored("\nWishing you a joyful and Blessed Easter !")
	
	print(colored_message + additional_text)

wish_happy_easter()
