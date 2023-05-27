def factorize(buffer):
    for i in range(2, buffer):
        if buffer % i == 0:
            print("{}={}*{}".format(buffer, buffer//i, i))
            break
