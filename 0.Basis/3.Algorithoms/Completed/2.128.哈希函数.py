class Solution:
    """
    @param key: A String you should hash
    @param HASH_SIZE: An integer
    @return an integer

在数据结构中，哈希函数是用来将一个字符串（或任何其他类型）转化为小于哈希表大小且大于等于零的整数。一个好的哈希函数可以尽可能少地产生冲突。一种广泛使用的哈希函数算法是使用数值33，假设任何字符串都是基于33的一个大整数，比如：

hashcode("abcd") = (ascii(a) * 33^3 + ascii(b) * 33^2 + ascii(c) *33^1 + ascii(d)) % HASH_SIZE 

                              = (97* 333 + 98 * 332 + 99 * 33 +100) % HASH_SIZE

                              = 3595978 % HASH_SIZE

其中HASH_SIZE表示哈希表的大小(可以假设一个哈希表就是一个索引0 ~ HASH_SIZE-1的数组)。

给出一个字符串作为key和一个哈希表的大小，返回这个字符串的哈希值。

 注意事项

对于这个问题你不需要自己设计hash算法，你只需要实现上述描述的hash算法即可。
    """
    def hashCode(self, key, HASH_SIZE):
        # write your code here
        index=len(key)-1
        value=0
        asciis=key.encode("ascii")

        for letter in asciis:
            print(ascii(letter))
        
        for letter in asciis:
            current=letter*(33**index);
            print("value+=",letter,"*",33**index,current)
            value+=current
            index-=1
        print("value%size=",value,"%",HASH_SIZE)
        return value%HASH_SIZE
            

        """
        print(len(key))
        for letter in key:
            print(ascii(letter))
        """



        
s=Solution()
result= s.hashCode("abcd",100)
print(result)
result= s.hashCode("abcd",1000)
print(result)
