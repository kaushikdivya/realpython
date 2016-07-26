def fahren(temp):
    F = float(temp) * 9/5 + 32
    print type(F)
    return F

def celsius(temp):
    C = (float(temp) - 32) * 5/9
    print type(C)
    return C
C = celsius(72)
F = fahren(37)
print "72 degrees F = {} degrees C".format(C)
print "37 degrees C = {} degrees F".format(F)
