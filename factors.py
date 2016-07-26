inp = input("Enter a positive integer:")
def factors(inp):
    for i in range(1,inp+1):
        if inp % i == 0:
            print "{} is a divisor of {}".format(i,inp)

factors(inp)
