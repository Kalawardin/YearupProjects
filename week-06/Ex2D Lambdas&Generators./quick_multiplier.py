doubler = lambda n: n * 2

print(doubler(-4))
print(doubler(8))
print(doubler('banana'))

tripler  = lambda n: n * 3

print(tripler(-4))
print(tripler(8))
print(tripler('banana'))

def multipler(factor):
    return lambda n: n * factor

quadrupler = multipler(4)
quintupler = multipler(5)
sextupler  = multipler(6)
septupler  = multipler(7)
octupler   = multipler(8)
nonupler = multipler(9)
decupler = multipler(10)
    
    
print(quadrupler(-4))
print(quadrupler(8))
print(quadrupler('banana'))

print(quintupler(-4))
print(quintupler(8))
print(quintupler('banana'))

print(sextupler(-4))
print(sextupler(8))
print(sextupler('banana'))

print(septupler(-4))
print(septupler(8))
print(septupler('banana'))

print(octupler(-4))
print(octupler(8))
print(octupler('banana'))

print(nonupler(-4))
print(nonupler(8))
print(nonupler('banana'))

print(decupler(-4))
print(decupler(8))
print(decupler('banana'))

