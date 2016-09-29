from random import random,randint,seed
from os import linesep
titlePattern=":-^80"
contentPattern=":15"
print(("{"+titlePattern+"}").format("Functions"))
print("random() returns a random float in the range [0,1)")
print("randint(@min,@max) returns a random integer in the range [@min,@max]")
print("seed([@seed]) initializes the random number generator of Python,{0}\
      if any @seed is inputted, it will be used as a seed,{0}\
      it is usually used for testing".format(linesep))
print(("{"+titlePattern+"}").format("Samples"))
print(("{"+contentPattern+"}").format("random()="),random())
print(("{"+contentPattern+"}").format("randint(1,2)="),randint(1,2))
print(("{"+contentPattern+"}").format("seed()="),seed())
print(("{"+contentPattern+"}").format("seed(1)="),seed(1))
