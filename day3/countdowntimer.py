import time

my_time = int(input("Enter the time in the seconds"))
# num = 0

# for x in range(0,my_time):
#     # my_time = int(input("Enter the time in the seconds"))
#     if my_time > 5 or my_time < 5:
#         print(f"you have {my_time-1} tries left")
# print("this is the end")

for x in range(my_time,0,-1):
    seconds = x % 60
    minutes = int(x/60) % 60
    hours = int( x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

# time.sleep(my_time)

print("times up")