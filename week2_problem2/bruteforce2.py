import random

P = 295075153L   # about 2^28
o1 = 210205973
o2 = 22795300
o3 = 58776750
o4 = 121262470
o5 = 264731963
o6 = 140842553
o7 = 242590528
o8 = 195244728
o9 = 86752752

def next(x, y):
  posx = x
  posy = y
  x = (2*x + 5) % P
  y = (3*y + 7) % P
  return x ^ y



for j in range(1, P):
  #generate x
  x = random.randint(0,P)
  #generate y on xor
  y = x ^ o1
  #print x, y
  #take the 2numbers and run them thru the rpg.
  attempt = next(x, y)

#test output with original.py
#attempt: o2  22795300 x:  189093025
#attempt: o2  22795300 x:  89059908 
  
