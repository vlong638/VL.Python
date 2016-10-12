titlePattern=":-^80"
subTitlePattern=":-^40"
contentPattern=":30"
print(("{"+titlePattern+"}").format("Conditions"))
print(("{"+contentPattern+"}").format("The special value"),False)
print(("{"+contentPattern+"}").format("The special value"),None)
print(("{"+contentPattern+"}").format("Every numerical value, e.g."),0)
print(("{"+contentPattern+"}").format("Every sequence value, e.g."),"''")
print(("{"+contentPattern+"}").format("Any function or method call that returns one of these listed values, e.g."),'int(0)')

print(("{"+titlePattern+"}").format("Comparisons"))
print(("{"+contentPattern+"}").format("<"))
print(("{"+contentPattern+"}").format("<="))
print(("{"+contentPattern+"}").format("=="))
print(("{"+contentPattern+"}").format(">="))
print(("{"+contentPattern+"}").format(">"))
print(("{"+contentPattern+"}").format("!="))

print(("{"+titlePattern+"}").format("in operator"))
print(("{"+contentPattern+"}").format("'y' in 'asdy'"),'y' in 'asdy')

print(("{"+titlePattern+"}").format("Logical operators"))
print(("{"+contentPattern+"}").format("and"))
print(("{"+contentPattern+"}").format("or"))
print(("{"+contentPattern+"}").format("not"))
print(("{"+titlePattern+"}").format("Samples"))
x=True
print(("{"+contentPattern+"}").format("x=True"))
y=False
print(("{"+contentPattern+"}").format("y=False"))
print(("{"+contentPattern+"}").format("x and y"),x and y)
print(("{"+contentPattern+"}").format("x or y"),x or y)
print(("{"+contentPattern+"}").format("not x"),not x)
print(("{"+contentPattern+"}").format("not y"),not y)

print(("{"+titlePattern+"}").format("Condition statements"))
print(("{"+subTitlePattern+"}").format("Two-way decision"))
print("if <boolean expression>:")
print("    <statements>")
print("else:")
print("    <statements>")
print(("{"+subTitlePattern+"}").format("Multi-branch decision"))
print("if <boolean expression>:")
print("     <statements>")
print("elif <boolean expression>:")
print("     <statements>")
print("else:")
print("     <statements>")

print(("{"+titlePattern+"}").format("Early Exit"))
print(("{"+contentPattern+"}").format("exit()"),"you can make early exit by function exit()")

