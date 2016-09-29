#标题
def PrintTitle(*texts):
    pattern1=":-^"
    pattern2=":^"
    wordsCount=80
    print("")
    print(("{"+pattern1+str(wordsCount)+"}").format(""))
    for text in texts:
        print(("{"+pattern2+str(wordsCount-GetChineseCount(text))+"}").format(text))
    print("")
    

#子标题
def PrintSubtitle(*texts):  
    pattern1=":-^"
    pattern2=":^"
    wordsCount=60
    print("")
    print(("{"+pattern1+str(wordsCount)+"}").format(""))
    for text in texts:
        print(("{"+pattern2+str(wordsCount-GetChineseCount(text))+"}").format(text))
    print("")


#代码
def PrintCode(code):
    print(">>>"+code)

#特别信息	

def PrintHint(*texts):
    pattern1=":#^"
    pattern2=":^"
    wordsCount=40
    print("")
    print(("{"+pattern1+str(wordsCount)+"}").format(""))
    for text in texts:
        print(("{"+pattern2+str(wordsCount-GetChineseCount(text))+"}").format(text))
    #print(("{"+pattern+str(wordsCount)+"}").format(""))
    print("")


#两端描述
descriptionPattern=":<40"
def PrintSampleWithDescription(sample,description):
    print(("{"+descriptionPattern+"}").format(sample)+description)

import re
def GetChineseCount(text):
    count=0
    for letter in text:
        if re.match('([\u4e00-\u9fa5])+',letter):
            count+=1
    return count
