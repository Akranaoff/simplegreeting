#Using the time module

import time
result = time.localtime()
# print(result)

t = time.strftime("%H:%M:%S")
print("Current time on the server is : ",t)
# print(type(t))

if(int(time.strftime("%H")) < 12):
  print("Good Morning")

elif(int(time.strftime("%H")) < 16):
  print("Good Afternoon")

elif(int(time.strftime("%H")) < 20):
  print("Good Evening")

else:
  print("Good Night")
