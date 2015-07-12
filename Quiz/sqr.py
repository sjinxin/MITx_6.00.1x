def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x

print "square(-4) %d" % Square(-4)
print "square(0) %d" % Square(0)
print "square(1) %d" % Square(1)
#print "square(16) %d" % Square(16)
#print "square(1.1) %d" % Square(1.1)
#print "square(0.1 %d" % Square(0.1)
#print "square(2.2) %d" % Square(2.2)
#print "square(3.5) %d" % Square(3.5)
