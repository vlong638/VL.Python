#基础
#print("")
#input()

#标题
titlePattern=":-^80"
#print(("{"+titlePattern+"}").format("Functions"))
#print(("{"+titlePattern+"}").format("Samples"))

#子标题
subTitlePattern=":-^40"
#print(("{"+subTitlePattern+"}").format("Conditions"))

#特别信息	
tipsTitlePattern=":*^40"
#print(("{"+tipsTitlePattern+"}").format("Conditions"))



#内容,值[,描述,值]
contentPattern1=":10"
contentPattern2=":10"
#print(("{"+contentPattern1+"}").format("Content1")
#      +("{"+contentPattern2+"}").format("Content2"))

#内容,值1[,值n]
contentPattern=":10"
#print((("{"+contentPattern+"}")*3).format("Content1","Content2","Content3"))

#内容,值
contentPattern=":10"
#print(("{"+contentPattern+"}").format("Content1"),"Content2")
#---------------------------0914之后采用下述新版------------------------------------
import PrintHelper
@title
@descriptions
@samples
=>VL.PythonTranslator
import PrintHelper
PrintHelper.PrintTitle(@title)
@descriptions
print(@descriptions)
PrintHelper.PrintSubtitle(@samples)
@samples
