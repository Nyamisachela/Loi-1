#use for loops to print numbers

for i in range (2,10):
    print("i = ", i)

# use % to check if number is odd or even

i = 2
print((i % 2) == 0)

#use for loop to cycle through the list from 1-21
for i in range(1, 21):

#use % to check that result != 0
    if ((i % 2) != 0):

#print the odds
        print(" i = ", i)

#floating point numbers(numbers with decimal values

my_float = input("enter float: ")

my_float = float(my_float) #convert from string to floating point number

print("Round to 2 decimals : {:.2f}".format(my_float))


