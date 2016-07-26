def invest(amount, rate, time):
    i = 1
    print "principle amount: ${}".format(amount)
    print "annual rate of return: {}".format(rate)
    while i <= time:
        amount  = amount * (1+rate)
        print "year 1: ${}".format(amount)
        i = i+1
invest(100, .05, 8)
invest(2000, .025, 5) 
