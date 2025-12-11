# nestedloop = a loop within the another loop (outer,inner)
# outer loop:
#   inner loop:


rows = int(input("enter the # of rows"))
columns = int(input("enter the # of cols"))
symbol = input("enter a symbol to use")

for x in range(rows):
    for y in range(columns):
        print(symbol,end="")
    print()