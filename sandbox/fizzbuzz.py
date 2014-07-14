#coding: utf-8

if __name__ == "__main__":
    for i in range(1, 20):
        if i%3 == 0 and i%5 == 0:
            print "fizzbuss"
        if i%3 == 0:
            print "fizz"
        elif i%5 == 0:
            print "buzz"
        else:
            print i
