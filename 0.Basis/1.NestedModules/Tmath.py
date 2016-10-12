import math
titlePattern=":-^80"
contentPattern=":12"
print(("{"+titlePattern+"}").format("Functions"))
print("exp(@logarithm)    e^@logarithm=?")
print("log(@logarithm)    e^?=@logarithm")
print("log10(@givenValue) 10^?=@givenValue")
print("sqrt(@givenValue)  ?^2=@givenValue")
print(("{"+titlePattern+"}").format("Samples"))
print(("{"+contentPattern+"}").format("exp(1)="),math.exp(1))
print(("{"+contentPattern+"}").format("log(e)="), math.log(math.exp(1)))
print(("{"+contentPattern+"}").format("log10(10)="), math.log10(10))
print(("{"+contentPattern+"}").format("sqrt(10)="), math.sqrt(10))
