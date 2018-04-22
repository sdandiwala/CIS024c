import sys
from helper import add

print "Number of Parameters:", len(sys.argv)

number1=0
number2=0

print "Type of sys.argv", type(sys.argv)

print "sys.arg values:"
for val in sys.argv:
    print val
    
if len(sys.argv)== 3:
    number1= int(sys.argv[1])
    number2= int(sys.argv[2])
    
print "Result:", add(number1,number2)