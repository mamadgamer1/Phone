from phonenumbers import parse
from phonenumbers import geocoder
from phonenumbers import carrier
from colorama import Fore , init
import time
init()
print(Fore.GREEN + "\tThis Program Made By:\n\tmamadgamer1 BBG MG1")
cntn = input("\nPress Enter To Continue: ")
print("\nexample: +1234567890") #wont work, only correct numbers works!
Target = input("\nEnter ur target phone number with + : ")
print("Please Wait . . .")
time.sleep(1)
print(Fore.BLACK + "\tResult: ")
number = parse(Target)
print(Fore.RED + geocoder.description_for_number(number,"en"))
print(carrier.name_for_number(number,"en"))

print(Fore.BLUE + "The Country of phone is: " +geocoder.description_for_number(number,"en"))
print("The Operator of phone is: " +carrier.name_for_number(number,"en"))
print(Fore.CYAN+"")

exit = input("Press Enter To exit: ")
while True:
    break
