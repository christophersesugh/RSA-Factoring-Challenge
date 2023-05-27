def factorize(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print("{:d}={:d}*{:d}".format(number, number//i, i))
            break
