import string
import random as r
length = int(input('Enter the length of OTP '))
otp=''
a = string.ascii_letters + string.digits
for i in range(length):
  otp=otp+r.choice(a)
print("OTP: ",otp)
