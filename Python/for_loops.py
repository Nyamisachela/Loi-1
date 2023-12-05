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

#demostrate compounding interest

#enter investenent amount and expected interest

#each year the investement will increase by their initial investemnt + initial investemnt * interest rate
#print out the earnings

# first ask for the initial invested and interest rate

money = input("Investment amount : ")
interest_rate = input("Interest rate : ")
#convert the value to a float
money = float(money)
#convert value to float and round of the percentange rate by 2 digits
interest_rate = float(interest_rate) * .01

#cycle through 10 years using for loop and range 0 -9
for i in range(10):
    money = money + (money * interest_rate)

#output results
print("Investement after 10 years : {:.2f}".format(money))






