# N is an input of the user, stating the desired amount of first prime numbers
N = int(input("How many prime numbers would you like to see: "))
# Stands for the number of times our function is used
count = 0
# The first prime number (1 is not a prime number) that will increase and later get checked in the function
potentialprime = 2
# Function to check potential prime numbers
def prime(potentialprime):
    divisor = 2
    while divisor <= potentialprime:
        if potentialprime == 2:
            return True
        elif potentialprime % divisor == 0:
            return False
        while potentialprime % divisor != 0:
            if potentialprime - divisor > 1:
                divisor += 1
            else:
                return True
# While loop to print out the desired number of prime numbers
while count < int(N):
    if prime(potentialprime) == True:
        print ('Prime number №' + str(count + 1), 'is', potentialprime)
        count += 1
    potentialprime += 1