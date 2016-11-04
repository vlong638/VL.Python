"""
使用 map reduce 来计算单词频率

方案 细粒度 single-string
mapper将字符串处理成单词
由reduce进行汇总集合

方案 粗粒度 multi-string
mapper将每一个字符串处理成list<key,value>
由reduce进行汇总集合


"""
class WordCount:
    # @param {str} line a text, for example "Bye Bye see you next"
    def mapper(self, _, line):
        # Write your code here
        # Please use 'yield key, value'
        
        #print("_",_)
        #print("line",line)
        #print()
        
        dic={}
        for letter in line.strip().split(" "):
            if dic.get(letter):
                dic[letter]+=1
            else:
                dic[letter]=1
        for key in dic:
            yield key,dic[key]


    # @param key is from mapper
    # @param values is a set of value with the same key
    def reducer(self, key, values):
        # Write your code here
        # Please use 'yield key, value'
        
        #print("key",type(key),key)
        #print("values",type(values),values)
        
        yield key,sum(values)
