# N is an input of the user, stating the desired amount of first prime numbers
N = int(input("How many prime numbers would you like to see: "))
# Stands for the number of times our function is used
x = 0
# The first prime number (1 is not a prime number) that will increase and later get checked in the function
potential_prime = 2
# Function to check potential prime numbers
def prime(potential_prime):
    divisor = 2
    while divisor <= potential_prime:
        if potential_prime == 2:
            return True
        elif potential_prime % divisor == 0:
            return False
        while potential_prime % divisor != 0:
            if potential_prime - divisor > 1:
                divisor += 1
            else:
                return True
# While loop to print out the desired number of prime numbers
while x < int(N):
    if prime(potential_prime) == True:
        print('Prime number №' + str(x + 1), 'is', potential_prime)
        x += 1
    potential_prime += 1