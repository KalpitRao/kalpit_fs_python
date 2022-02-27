#Print downward Half-Pyramid Pattern with Star (asterisk)
num_rows = int(input('Enter the number of rows'));
for i in range(0,num_rows):
    for j in range(i,-1):
        print("*",end="")

