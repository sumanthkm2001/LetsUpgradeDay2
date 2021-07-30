import string 
def ispangram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False  
    return True

string = input('enter the pangram')
if(ispangram(string) == True):
    print("Yes Its a Pangram")
else:
    print("No Its Not a Pangram")
