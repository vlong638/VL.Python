"""
给定一个字符串所表示的括号序列，
包含以下字符： '(', ')', '{', '}', '[' and ']'，
判定是否是有效的括号序列。
"""
class Solution:
    Parentheses=["(",")","{","}","[","]"]
    FrontParentheses=["(","{","["]
    BackParentheses=[")","}","]"]
    
    caseOfBraket=["(","{","}","[","]"]
    caseOfBrace=["(",")","{","[","]"]
    caseOfSquareBraket=["(",")","{","}","["]
    # @param {string} s A string
    # @return {boolean} whether the string is a valid parentheses
    def isValidParentheses(self, s):
        # Write your code here
        print()
        stack=[]
        index=0
        while index<len(s):
            print("check",s[index])
            if s[index] in self.Parentheses:
                if s[index] in self.FrontParentheses:
                    print("stack.insert(0,s[index])",s[index])
                    stack.insert(0,s[index])
                    print(stack)
                elif s[index] in self.BackParentheses:
                    if len(stack)==0:
                        print("return False,stack empty")
                        return False
                    if s[index]==")":
                        if(stack[0]=="("):
                            print("stack.remove(stack[0])",stack[0])
                            stack.remove(stack[0])
                            print(stack)
                        else:
                            print("return False,",s[index])
                            return False
                    elif s[index]=="}":
                        if(stack[0]=="{"):
                            print("stack.remove(stack[0])",stack[0])
                            stack.remove(stack[0])
                            print(stack)
                        else:
                            print("return False,",s[index])
                            return False
                    elif s[index]=="]":
                        if(stack[0]=="["):
                            print("stack.remove(stack[0])",stack[0])
                            stack.remove(stack[0])
                            print(stack)
                        else:
                            print("return False,",s[index])
                            return False
                    else:
                        print("return False,",stack[0])
                        return False
            index+=1
        print("return stack",stack)
        return len(stack)==0


    
s=Solution()
result= s.isValidParentheses("{")
print(type(result))
print(result)

result= s.isValidParentheses("(){}")
print(type(result))
print(result)


result= s.isValidParentheses("()]")
print(type(result))
print(result)

result= s.isValidParentheses("([])")
print(type(result))
print(result)

result= s.isValidParentheses("[{()}]")
print(type(result))
print(result)

result= s.isValidParentheses("[({(())}[()])]")
print(type(result))
print(result)

    
"""
    def isValidParentheses(self, s):
        # Write your code here
        start=0
        end=len(s)-1
        print()
        return self.checkParentheses(s,0,end,["(","{","["],[")","}","]"])
    def checkParentheses(self,s,start,end,target,case,side=1):
        if side==1:
            if len(target)>1:

                while start<=end:
                    if s[start] in target:
                        #查尾
                        if s[start]=="(":
                            print("find starter =>",s[start])
                            parentheses=[")"]
                            return self.checkParentheses(s,start+1,end,[")"],["(","{","}","[","]"]) or self.checkParentheses(s,start+1,end,[")"],["(","{","}","[","]"],2)
                        elif s[start]=="{":
                            print("find starter =>",s[start])
                            return self.checkParentheses(s,start+1,end,["}"],["(",")","{","[","]"]) or self.checkParentheses(s,start+1,end,["}"],["(",")","{","[","]"],2)
                        elif s[start]=="[":
                            print("find starter =>",s[start])
                            return self.checkParentheses(s,start+1,end,["]"],["(",")","{","}","["]) or self.checkParentheses(s,start+1,end,["]"],["(",")","{","}","["],2)
                    elif s[start] in case:
                        print("find case !!",s[start])
                        return False
                    else:
                        start+=1
                print("forward end =>")
                return True
            else:
                while start<=end:
                    if s[start] == target[0]:
                        print("find ender =>",s[end])
                        return self.checkParentheses(s,start+1,end,["(","{","["],[")","}","]"])
                    elif s[start] in case:
                        print("find case !!",s[end])
                        return False
                    else:
                        start+=1
                print("forward end !!")
                return False
        else:
            if len(target)>1:

                return False
            else:
                while start<=end:
                    if s[end] == target[0]:
                        print("find ender =>",s[end])
                        return self.checkParentheses(s,start,end-1,["(","{","["],[")","}","]"])
                    elif s[end] in case:
                        print("find case !!",s[end])
                        return False
                    else:
                        end-=1
                print("backward end !!")
                return False
            
"""            

        
