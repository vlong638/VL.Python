"""
给定一个字符串source和一个目标字符串target
，在字符串source中找到包括所有目标字符串字母的子串。

 注意事项

如果在source中没有这样的子串，返回""
，如果有多个这样的子串，返回最短的子串。
"""
class Solution:
    """
    @param source: A string
    @param target: A string
    @return: A string denote the minimum window
             Return "" if there is no such a string
    """
    def minWindow(self, source, target):
        if (target == ""):
            return ""
        S , T = source, target
        d, dt = {}, dict.fromkeys(T, 0)
        print(dt)
        for c in T:
            d[c] = d.get(c, 0) + 1
        print(d)
        pi, pj, cont = 0, 0, 0
        if (source =="" or target ==""):
            return ""
        ans = ""
        while pj < len(S):
            if S[pj] in dt:
                if dt[S[pj]] < d[S[pj]]:
                    cont += 1
                dt[S[pj]] += 1;
            if cont == len(T):
                while pi < pj:
                    if S[pi] in dt:
                        if dt[S[pi]] == d[S[pi]]:
                            break;
                        dt[S[pi]] -= 1;
                    pi+= 1
                if ans == '' or pj - pi < len(ans):
                    ans = S[pi:pj+1]
                dt[S[pi]] -= 1
                pi += 1
                cont -= 1
            pj += 1
        return ans
    
    def minWindow2(self, source, target):
        if source=="" or target=="":
            return ""
        #构建需求dict和当前dict
        #相关字符stack
        curDic=dict.fromkeys(target,0)
        tarDic={}
        for letter in target:
            tarDic[letter]=tarDic.get(letter,0)+1
        #过程处理
        startIndex=0
        endIndex=0
        minStart=0
        minLength=-1
        for letterS in source:
            startIndex+=1
            if letterS in curDic:
                #start处理
                curDic[letterS]=curDic.get(letterS)+1
                #检测是否达标
                isValid=True
                for k,v in curDic.items():
                    if v<tarDic[k]:
                        isValid=False
                        break
                #end处理        
                if isValid:
                    while endIndex<startIndex:
                        letterE=source[endIndex]
                        if letterE in curDic:
                            if curDic[letterE]>tarDic[letterE]:
                                curDic[letterE]-=1
                                endIndex+=1
                            else:
                                break
                        else:
                            endIndex+=1
                    #minLength处理
                    if minLength==-1:
                        minLength=startIndex-endIndex
                        minStart=endIndex
                    elif startIndex-endIndex<minLength:
                        minLength=startIndex-endIndex
                        minStart=endIndex
        print(startIndex,endIndex)
        print("tarDic",tarDic)
        print("curDic",curDic)
        if minLength>0:
            return source[minStart:minStart+minLength]
        else:
            return ""
            
    def minWindow3(self, source, target):
        a=[1,2,3]
        a=collections.deque(a)
        for letter in range(5,10):
            a.append(letter)
        for letter in range(1,10):
            print(a.popleft())
        

        
import collections

s=Solution()
result= s.minWindow2("ADOBECODEBANC","ABC")
print(type(result))
print(result)
result= s.minWindow2("absdfaabab", "adb")
print(type(result))
print(result)
result= s.minWindow2("adfqeradboaf23098724huhfda923hadf78adfhadfhadfaodiyfas8", "dfje89affefy8f")
print(type(result))
print(result)
