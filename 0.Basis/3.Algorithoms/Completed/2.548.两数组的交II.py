class Solution:
# @param s: a list of char
# @param offset: an integer 
# @return: nothing

    def intersection(self, nums1, nums2):
        # Write your code here
        if len(nums1)==0 or len(nums2)==0:
            return []
        nums1=self.sortIntegers2(nums1)
        nums2=self.sortIntegers2(nums2)
        intersection=[]
        print(nums1)
        print(nums2)
        self.fastIntersection(nums1,0,len(nums1)-1,nums2,0,len(nums2)-1,intersection)
        return intersection
        
    def binarySearchWithRange(self, nums, target,start,end,findFront):
        # write your code here
        index=int((start+end)/2)
        if nums[index]==target:
            if findFront:
                while index>start and nums[index-1]==target:
                    index-=1
            else:
                while index<end and nums[index+1]==target:
                    index+=1
            return index
        elif nums[index]>target:
            if index-1<start:
                return start;
            return self.binarySearchWithRange(nums,target,start,index-1,findFront)
        else:
            if index+1>end:
                return end;
            return self.binarySearchWithRange(nums,target,index+1,end,findFront)   
            
    def sortIntegers2(self, A):
        #快排
        length=len(A)
        if length==0:
            return []
        elif length==1:
            return A
        #取中位,分左右区间
        mediumIndex=int(length/2)
        medium=A.pop(mediumIndex)
        length-=1
        pre=[]
        end=[]
        index=0
        while index<length:
            if A[index]<medium:
                pre.append(A[index])
            else:
                end.append(A[index])
            index+=1
        #平衡化
        if len(end)==0:
            end.append(medium)
        else:
            pre.append(medium)
        #连接左右区间
        if len(pre)>1:
            pre=self.sortIntegers2(pre)
        if len(end)>1:
            end=self.sortIntegers2(end)
        #return
        if pre==None:
            return end
        elif end==None:
            return pre
        else:
            pre.extend(end)
            return pre
        
    def fastIntersection(self,A,start,end,B,startB,endB,intersection):
        #快排拆分
        if start>end or startB>endB:
            print("check A:{} to {},B {} to {}".format(start,end,startB,endB))
            print("return")
            print()
            return
        if start==end:
            print("check A:{} to {},B {} to {}".format(start,end,startB,endB))
            targetIndex=self.binarySearchWithRange(B,A[start],startB,endB,False)
            if A[start]==B[targetIndex]:
                print("append",A[start])
                intersection.append(A[start])
            print()
            return
        if startB==endB:
            print("check A:{} to {},B {} to {}".format(start,end,startB,endB))
            targetIndex=self.binarySearchWithRange(A,B[startB],start,end,False)
            if A[targetIndex]==B[startB]:
                print("append",A[targetIndex])
                intersection.append(A[targetIndex])
            print()
            return
        
        length=len(A)
        if length==0:
            return
        elif length==1:
            return
        #取中位,分左右区间
        mediumIndex=int((start+end+1)/2)
        while mediumIndex-1>=start and A[mediumIndex]==A[mediumIndex-1]:
            mediumIndex-=1
        medium=A[mediumIndex]
        targetIndex=self.binarySearchWithRange(B,medium,startB,endB,True)
        #print("check A:{} to {},B {} to {}".format(start,mediumIndex-1,startB,targetIndex-1))
        #print("mediumIndex",mediumIndex,"medium",medium)
        #print("medium:{},B.targetIndex:{}".format(medium,targetIndex))
        #print("check A:{} to {},B {} to {}".format(mediumIndex+1,end,targetIndex+1,endB))
        #print()

        if medium==B[targetIndex]:
            print("pre A:{} to {},B {} to {}".format(start,mediumIndex-1,startB,targetIndex-1))
            print("medium A:{} to {},B {} to {}".format(mediumIndex,mediumIndex,targetIndex,targetIndex))
            print("medium:{},B[targetIndex]:{}".format(medium,B[targetIndex]))
            print("end A:{} to {},B {} to {}".format(mediumIndex+1,end,targetIndex+1,endB))
            print("append",medium)
            print()
            self.fastIntersection(A,start,mediumIndex-1,B,startB,targetIndex-1,intersection)
            intersection.append(medium)
            self.fastIntersection(A,mediumIndex+1,end,B,targetIndex+1,endB,intersection)
        else:
            print("pre A:{} to {},B {} to {}".format(start,mediumIndex-1,startB,targetIndex))
            print("medium A:{} to {},B {} to {}".format(mediumIndex,mediumIndex,targetIndex,targetIndex))
            print("end A:{} to {},B {} to {}".format(mediumIndex+1,end,targetIndex+1,endB))
            print()
            
            self.fastIntersection(A,start,mediumIndex-1,B,startB,targetIndex,intersection)
            self.fastIntersection(A,mediumIndex+1,end,B,targetIndex,endB,intersection)
s=Solution()


"""
result= s.intersection([1, 2, 2, 1],[2, 2])
print(type(result))
print(result)
result= s.intersection([4,7,9,7,6,7],[5,0,0,6,1,6,2,2,4])
print(type(result))
print(result)
"""
result= s.intersection([1,105,-139,59,37,-175,-120,-8,-165,-9,-123,-76,-53,1,17,-34,132,172,24,-33,-96,97,-106,-151,-161,-43,-197,-40,135,-126,-193,-190,-141,153,181,-62,197,-174,-32,156,116,20,33,150,58,-175,-156,-199,78,-82,-40,-73,-85,125,-119,137,-125,-188,169,195,63,150,35,-90,79,152,33,-66,-120,-195,199,168,-48,-10,102,-21,199,177,100,3,126,-153,-88,-185,152,-73,-14,-108,-46,-87,64,-39,32,-33,-46,-23,-147,61,-31,-175,-90,-150,13,53,-146,128,155,136,-16,182,50,74,-123,78,-102,25,89,140,111,12,70,73,-37,35,-185,-129,-23,97,-81,-1,141,-139,-80,-126,150,167,-101,82,-154,161,129,-168,-79,30,-14,46,164,-100,-26,-200,116,-122,115,169,-2,62,94,-1,-143,68,113,-54,-161,-143,6,-149,71,165,-141,7,-6,49,73,-190,-23,175,-51,28,155,19,-123,-30,171,-34,37,-154,93,92,-46,-67,38,121,73,41,-111,106,19,-137,25,78,35,80,190,-66,-180,156,89,-104,33,136,-98,-151,-82,56,86,46,140,138,180,-149,23,-117,-93,163,10,-138,90,187,-9,179,-21,-133,140,181,21,-192,-146,-125,-47,82,146,181,181,112,40,-122,-163,1,-169,-97,11,199,-1,70,-10,158,-121,68,108,93,-87,-118,64,159,2,-142,126,-179,-144,97,29,166,41,-109,-3,-74,141,99,-73,26,-11,191,149,190,-65,91,69,-5,-154,100,-55,-124,108,31,155,16,-3,-151,-119,72,-51,-3,-133,-12,80,-121,-43,109,192,86,122,-60,-31,190,-44,-51,-185,-85,200,-30,-177,-149,-179,-140,-167,140,63,-189,-24,157,-100,115,99,-51,174,50,112,-199,133,20,-79,-84,-62,-78,-82,115,5,-25,-21,-143,4,-99,45,-156,-85,51,197,-102,-133,67,-93,-4,61,-71,88,170,-167,-167,-110,-193,93,164,-178,-162,45,173,-5,-136,181,113,18,25,55,185,200,-83,-78,-54,-180,68,-87,199,23,-66,132,180,-156,137,-157,4,-67,185,-119,-115,-101,150,-186,34,-87,13,-35,-187,106,-143,-182,-192,-84,-96,-163,-32,59,106,-125,-118,-16,87,-94,-67,-186,-174,-87,193,-64,-86,-2,-155,200,74,-140,167,-193,71,-75,-130,183,-184,-199,-56,87,-51,-122,-185,30,23,-9,85,-101,12,-32,-121,34,58,-187,-24,-112,54,34,154,156,-3,69,69,-86,84,-4,10,-182,53,-122,19,-180,-123,134,146,-64,122,128,172,89,129,107,117,47,-86,-52,-106,-78,12,-41,98,-37,148,-5,-36,-15,154,178,-89,41,89,99,7,-68,97,76,-170,-144,-59,-16,175,-195,150,-176,-1,123,-192,-195,169,-170,123,105,13,-73,16,167,-41,-152,108,-147,135,176,-46,-189,170,191,-164,-97,-69,116,81,23,-125,83,81,57,-23,166,131,87,63,-42,170,-122,-200,-89,-190,1,192,-40,117,90,25,-192,186,164,75,-102,129,-155,-67,72,185,145,151,49,157,-43,40,165,22,86,-155,12,42,-95,-136,-63,-87,60,135,128,7,-138,53,82,-124,188,104,130,100,126,-84,37,195,-181,53,58,-25,171,110,106,-143,-188,-138,-76,12,-83,-163,26,-32,20,-199,-18,-176,-52,29,-118,-107,35,-5,-3,46,100,10,-4,63,-149,83,-9,-80,146,18,87,163,-126,-119,50,184,62,-194,-88,139,176,160,8,29,-181,-48,-88,11,-199,-198,48,-62,3,-154,199,-39,-97,171,4,-40,-43,-88,-49,-95,156,-141,-101,167,68,146,7,161,-122,-30,-140,69,-132,71,23,79,-163,-19,108,-165,-81,-71,47,69,2,189,-116,-150,-54,101,138,-46,-83,44,-158,-184,118,-92,-136,180,-1,-8,-118,-154,47,-24,-199,-38,-81,72,165,-191,-31,-3,-200,-176,106,187,-110,-133,-174,-28,93,193,-175,-45,-82,-61,-124,-5,-87,166,134,88,-20,117,-84,146,-110,-61,-142,-149,71,-149,191,-20,67,143,-164,-20,-175,-158,139,166,-200,-13,100,-55,197,-187,-109,74,-54,-17,187], [-73,-152,-101,-164,-124,12,101,-116,120,7,135,-58,-8,-137,125,86,46,-98,20,-145,60,77,-104,-128,-180,177,-135,-197,-163,-140,199,-96,163,21,-169,191,-136,-23,-184,193,-166,-117,110,-72,196,-191,-196,-76,139,89,59,-20,-23,-8,-31,-184,98,12,82,-124,-43,-96,57,146,118,-54,-112,110,136,-63,38,35,162,-154,109,155,95,-119,-144,-62,-13,-128,185,-100,169,-106,-195,0,111,19,-171,-104,99,-171,66,177,129,8,81,-60,-98,162,122,-6,-30,172,187,-177,-14,-171,-174,136,-75,85,19,-197,-114,-160,37,-198,-157,3,74,169,-137,-141,-79,-115,-16,1,-36,-131,-198,-40,-139,-113,89,-12,3,200,3,-162,46,150,-102,-189,147,1,28,-119,-162,88,-66,-52,58,61,-183,-92,129,166,169,-77,-58,47,-102,-144,161,104,161,-176,-134,-110,136,180,-93,-32,137,-96,-65,30,25,-197,-124,176,74,-130,-53,-114,-173,-88,143,-124,-135,-77,-12,13,-75,-11,-14,-166,2,-113,-52,23,-42,-196,109,94,36,160,125,34,87,167,-103,-15,157,189,117,178,55,-18,76,-168,154,-31,-20,-69,-68,-2,-101,-64,135,-173,-87,94,88,-158,183,114,-147,193,117,180,166,68,-50,-96,-139,73,198,166,4,10,-176,-121,-152,-43,153,-104,175,159,47,149,116,25,-128,-58,184,0,-36,-103,-106,172,145,-3,129,99,135,105,65,189,-99,-165,147,53,-136,-14,129,-100,146,-196,-173,-159,87,68,-40,-60,-102,-183,142,38,-117,-117,94,65,146,-63,-101,17,-11,-110,-162,23,164,-105,54,53,-77,177,90,14,116,-186,-179,-62,-180,-138,90,19,27,24,-180,78,91,130,-158,165,-66,-190,15,155,122,179,143,53,-33,-128,-85,-7,70,146,-140,-35,45,-54,148,128,88,-24,155,139,85,-117,183,-127,-81,91,176,104,85,87,-83,-146,-147,-125,18,71,38,-153,-89,62,-50,8,-164,182,-12,-155,-127,-121,48,41,-42,-16,40,175,111,191,62,138,173,88,-6,-63,163,-60,122,116,-147,134,182,-5,-35,-142,102,-143,146,75,39,-199,-103,9,157,164,123,17,124,190,143,-3,138,4,91,14,140,52,130,-143,106,-174,-135,-39,81,-31,139,-175,-168,22,-62,21,186,134,-173,-35,-114,5,-170,126,-116,-23,-107,-10,95,18,93,61,-196,190,-113,98,10,-123,151,-76,91,192,-80,162,103,78,30,-88,-71,124,-28,112,-111,197,176,-90,-180,159,-144,-87,-21,-109,132,66,-6,-81,-131,199,-89,46,87,46,56,108,49,39,93,153,70,-72,-143,118,106,121,-112,-128,191,170,-95,-140,-139,-196,-197,63,-147,68,-163,-16,50,196,-121,43,176,46,-150,150,-108,72,31,88,183,81,-122,-97,120,177,157,74,102,62,28,-185,48,-152,-43,-39,-47,157,-169,-178,183,-44,-155,93,-179,199,56,35,-98,62,-124,-138,7,-99,195,-1,64,-166,-38,-46,99,192,-92,191,57,66,51,131,116,159,-4,-199,181,125,186,-151,46,-145,7,164,57,-87,-21,-73,144,143,128,-177,-88,-125,180,24,-152,79,-172,-122,-122,-140,5,95,-185,16,-93,-43,109,159,134,-70,-64,-130,-21,-16,-89,-35,17,84,15,187,114,116,-153,93,10,-193,-26,126,-38,-78,157,64,69,71,-165,95,82,54,-51,-185,142,-163,162,-131,95,81,-41,184,98,-145,-175,-162,-135,157,160,195,-136,-100,-155,-46,24,-82,-12,35,83,149,-66,-56,-34,-45,60,182,-200,-182,-48,-144,-138,-79,-2,-186,142,-178,161,-101,-18,-32,-192,187,-128,-32,-175,-189,-79,21,-159,127,-85,-82,96,66,-139,17,188,-137,138,28,99,-51,-63,9,-124,-98,-69,65,-64,-109,-8,-39,148,190,33,-143,-188,29,91,-158,-113,-146,93,-65,9,70,-126,-73,182,-77,53,131,112,-151,44,71,136,185,-16,57,33,132,131,-178,-127,106,-28,-142,-182,200,116,-134,48,187,-146,-175,95,85,148,34,-39,145,186,-74,-140,92,154,44,95,140,174,-129,121,41,-63,-83,48,61,-127])
print(type(result))
print(result)


"""
优化前版本
    def intersection(self, nums1, nums2):
        # Write your code here
        if len(nums1)==0 or len(nums2)==0:
            return []
        nums1=self.sortIntegers2(nums1)
        nums2=self.sortIntegers2(nums2)
        intersection=[]
        i=0
        j=-1
        while i<len(nums1):
            if j+1<len(nums2):
                print("check range",j+1,"to",len(nums2)-1)
                temp=self.binarySearchWithRange(nums2,nums1[i],j+1,len(nums2)-1)
            if temp>=0:
                j=temp
                intersection.append(nums2[j])
                temp=-1
            i+=1
        print(nums1)
        print(nums2)
        return intersection
        
    def binarySearchWithRange(self, nums, target,start,end):
        # write your code here
        index=int((start+end)/2)
        if nums[index]==target:
            while index>start and nums[index-1]==target:
                index-=1
            print("find value ",nums[index]," at index",index)
            return index
        elif nums[index]>target:
            if index-1<start:
                return -1;
            return self.binarySearchWithRange(nums,target,start,index-1)
        else:
            if index+1>end:
                return -1;
            return self.binarySearchWithRange(nums,target,index+1,end)   
            
    def sortIntegers2(self, A):
        #快排
        length=len(A)
        if length==0:
            return []
        elif length==1:
            return A
        #取中位,分左右区间
        mediumIndex=int(length/2)
        medium=A.pop(mediumIndex)
        length-=1
        pre=[]
        end=[]
        index=0
        while index<length:
            if A[index]<medium:
                pre.append(A[index])
            else:
                end.append(A[index])
            index+=1
        #平衡化
        if len(end)==0:
            end.append(medium)
        else:
            pre.append(medium)
        #连接左右区间
        if len(pre)>1:
            pre=self.sortIntegers2(pre)
        if len(end)>1:
            end=self.sortIntegers2(end)
        #return
        if pre==None:
            return end
        elif end==None:
            return pre
        else:
            pre.extend(end)
            return pre
"""
