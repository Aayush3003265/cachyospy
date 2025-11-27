# compount interest calculator
principle = 0
rate = 0
time = 0
# while principle <= 0:
#     principle= float(input("Enter the principle amount: "))
#     if principle<= 0:
#         print("Principle can't be less than or equal to 0")
      
# while rate <= 0:
#     rate= float(input("Enter the rate: "))
#     if rate<= 0:
#         print("rate can't be less than or equal to 0")        

# while time <= 0:
#     time= int(input("Enter the time in years: "))
#     if time<= 0:
#         print("time can't be less than or equal to 0") 
while True:
    principle= float(input("Enter the principle amount: "))
    if principle< 0:
        print("Principle can't be less than  0")
    else:
        break  
    
while True:
    rate= float(input("Enter the rate: "))
    if rate< 0:
        print("rate can't be less than  0")        
    else:
        break
    
while True:
    time= int(input("Enter the time in years: "))
    if time< 0:
        print("time can't be less than 0")    
    else:
        break
    
    
print(f"principle= {principle}")
print(f"rate= {rate}")
print(f"time= {time}")

total = principle * pow((1 + rate / 100) , time)
print(f"Your New Balance After {time} year/s is {total:.2f}")
    