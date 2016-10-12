#标题
titlePattern=":-^80"
#内容
contentPattern=":40"
#特别信息
tipsTitlePattern=":*^40"

#while
print(("{"+titlePattern+"}").format("while loop"))
print("while <boolean expression>:")
print("    <statements> ")
print("while")
i=1
while i<10:
    print(i)
    i+=1
    if i==5:
        print("break while i==5")
        break
#for
print(("{"+titlePattern+"}").format("for"))
print("for <variable> in <collection>:")
print("    <statements> ")
#loop string
print(("{"+titlePattern+"}").format("loop string"))
print("for letter in 'banana': ")
print("    print( letter )")
print("print( 'Done' )")
for letter in 'banana':
    print( letter )
print( 'Done' )
#loop range()
print(("{"+titlePattern+"}").format("loop range()"))
print("for value in range(1,10,2): ")
print("    print( value )")
print("print( 'Done' )")
print(("{"+tipsTitlePattern+"}").format("range(@start,@end,@step)"))
for value in range(1,10,2):
    print( value )
print( 'Done' )
#while else
print(("{"+titlePattern+"}").format("while"))
print("while <boolean expression>:")
print("    <statements> ")
print("else")
print("    <statements> ")
#break
print(("{"+titlePattern+"}").format("break"))
print("while <boolean expression>:")
print("    <statements> ")
print("    if <boolean expression>:")
print("        break")
#continue
print(("{"+titlePattern+"}").format("continue"))
print("while <boolean expression>:")
print("    <statements> ")
print("    if <boolean expression>:")
print("        continue")
#nested loops
#略
#loop-and-a-half
#略

