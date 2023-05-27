def factorize(number):
    for i in range(2, number):
        if number % i == 0:
            print("{:d}={:d}*{:d}".format(number, number//i, i))
            break
