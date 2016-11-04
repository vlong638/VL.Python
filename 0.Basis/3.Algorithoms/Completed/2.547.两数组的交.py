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
        targetIndex=self.binarySearchWithRange(B,medium,startB,endB,False)
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

result= s.intersection([1,2,2,1], [2,2])
print(type(result))
print(result)
result= s.intersection([61,24,20,58,95,53,17,32,45,85,70,20,83,62,35,89,5,95,12,86,58,77,30,64,46,13,5,92,67,40,20,38,31,18,89,85,7,30,67,34,62,35,47,98,3,41,53,26,66,40,54,44,57,46,70,60,4,63,82,42,65,59,17,98,29,72,1,96,82,66,98,6,92,31,43,81,88,60,10,55,66,82,0,79,11,81], [5,25,4,39,57,49,93,79,7,8,49,89,2,7,73,88,45,15,34,92,84,38,85,34,16,6,99,0,2,36,68,52,73,50,77,44,61,48])
print(type(result))
print(result)
"""
result= s.intersection([180,395,311,750,949,164,212,968,978,404,381,1,265,92,331,350,375,451,903,932,129,590,771,883,900,344,712,804,367,547,596,533,22,691,125,558,450,74,771,673,778,45,44,172,63,260,669,374,526,337,138,459,724,458,428,851,536,387,93,586,453,715,29,330,60,648,541,923,244,377,164,780,748,831,708,544,176,985,1,308,256,922,645,121,42,855,667,730,115,677,289,355,478,298,849,218,730,449,621,957,244,25,22,866,287,704,841,757,916,439,124,316,575,642,4,84,345,157,4,578,359,223,936,275,997,197,478,795,369,963,733,252,18,872,690,851,985,49,124,646,153,396,150,499,96,699,848,541,214,201,544,249,974,599,937,583,711,298,375,137,829,913,625,897,757,795,266,298,6,404,809,6,879,20,943,293,717,146,634,835,805,532,75,256,115,994,147,368,784,716,579,127,341,195,233,75,194,858,741,507,932,648,610,239,604,626,67,203,793,769,429,760,466,540,258,977,614,781,276,832,771,538,296,990,832,146,895,42,458,681,582,444,301,72,786,977,483,266,868,693,703,593,536,581,594,448,793,606,71,556,230,652,711,704,8,871,700,681,431,921,655,745,344,285,842,856,401,541,364,117,933,175,250,410,608,805,446,358,233,921,430,743,126,662,22,793,371,452,55,432,521,811,548,556,160,974,567,816,802,357,379,527,237,435,669,381,583,124,188,510,6,144,493,316,135,444,251,653,656,952,49,451,558,181,838,227,605,41,677,738,858,603,888,463,406,765,754,10,956,898,815,123,727,961,816,801,243,102,606,538,581,49,424,388,746,483,682,573,666,391,764,490,879,353,861,768,24,306,499,143,363,775,453,221,85,450,874,842,836,554,518,799,116,27,455,826,995,436,429,851,613,147,42,363,946,505,510,705,192,729,809,715,390,267,364,808,733,878,919,20,877,997,917,590,196,80,868,173,325,249,346,961,734,235,27,374,914,363,905,796,399,153,51,267,522,440,630,344,719,216,787,442,589,897,419,950,777,916,534,584,277,910,372,107,732,409,73,496,927,92,317,500,609,584,806,934,382,864,656,606,165,762,407,461,957,851,795,458,470,340,83,381,323,980,457,204,313,793,949,388,985,432,172,292,184,778,924,613,756,692,874,706,527,232,397,907,28,97,899,573,282,349,104,809,318,286,258,504,908,604,765,676,148,476,283,427,975,967,178,401,593,578,711,981,599,846,362,682,612,683,902,886,648,533,811,527,961,331,602,679,726,13,321,969,78,968,760,824,266,717,303,233,630,306,81,902,896,827,453,137,184,675,835,259,335,945,204,569,237,396,646,629,411,975,291,158,87,240,382,681,756,773,440,235,687,137,748,478,670,808,132,834,24,345,240,505,732,294,794,267,433,273,100,888,634,754,947,691,469,156,873,661,583,380,789,192,37,621,798,347,401,953,395,888,386,876,692,530,784,27,211,772,612,162,209,392,21,352,959,95,784,482,588,924,738,862,463,571,731,47,698,751,569,532,870,118,677,202,208,201,573,672,358,112,501,424,802,851,202,543,620,967,159,977,614,903,797,765,99,667,999,528,220,365,263,610,513,652,781,249,453,256,371,751,492,646,544,673,130,199,987,279,866,739,599,50,197,479,114,153,121,512,828,246,701,23,103,231,426,109,547,530,14,694,37,281,339,351,396,773,406,965,773,748,118], [867,616,238,748,559,454,139,699,763,776,47,123,14,332,545,680,562,478,593,401,396,75,489,880,142,965,795,544,691,981,711,470,172,965,167,223,690,100,934,402,699,260,944,904,659,412,934,86,733,83,189,631,542,392,424,739,167,342,695,160,648,441,885,631,637,910,528,299,137,342,115,839,62,660,285,578,992,38,287,669,534,469,464,282,788,283,701,122,818,140,330,684,524,994,419,920,191,110,619,389,575,365,916,188,396,454,115,639,784,873,511,337,308,895,313,300,672,277,297,518,545,297,847,6,395,196,791,246,586,331,547,382,443,103,174,942,890,530,590,660,899,651,837,732,180,979,517,47,241,290,571,985,590,613,580,290,549,770,99,922,70,538,24,263,327,445,220,577,584,473,710,893,59,961,189,278,454,515,678,143,46,588,901,55,382,456,337,715,331,155,178,547,491,977,832,193,124,571,896,834,6,655,712,229,954,308,491,820,891,903,839,61,244,0,832,862,15,861,738,189,489,311,888,661,158,65,724,374,431,957,387,80,795,702,798,702,93,761,659,423,984,522,656,449,271,123,499,723,588,216,961,357,57,495,171,656,340,409,6,672,726,302,70,190,833,920,346,133,606,24,316,58,462,153,288,943,688,667,369,400,73,330,214,99,603,320,942,513,641,962,577,922,196,373,164,474,437,851,378,756,336,269,625,737,498,471,522,525,102,966,331,689,877,735,983,168,66,460,884,838,982,687,857,627,80,209,311,567,771,420,126,558,146,297,840,525,655,309,281,271,178,125,510,471,598,298,566,750,105,139,533,16,11,590,131,991,795,439,712,654,902,86,727,580,258,661,116,226,40,529,497,278,351,862,98,24,525,844,168,780,142,798,138,323,515,529,103,939,8,301,144,473,842,970,928,626,242,243,789,734,429,786,309,130,710,921,423,824,658,704,516,343,217,881,116,49,485,956,608,73,584,266,919,181,485,526,498,430,252,970,483,93,623,112,910,431,233,322,993,133,642,482,905,996,558,810,707,94,510,958,639,274,733,421,997,5,736,144,0,228,446,289,453,281,234,0,757,18,38,980,354,288,42,178,904,166,563,736,886,602,422,391,259,383,407,9,381,566,968,827,138,107,411,694,323,815,27,361,656,288,153,914,83,175,731,214,351,996,418,554,560,176,549,20,411,890,64,232,429,48,833,33,366,184,569,568,942,616,328,650,590,354,650,325,498,727,932,505,148,14,696,631,824,472,586,444,796,403,936,889,392,308,829,977,19,753,905,682,947,89,349,284,136,241,616,859,26,711,122,154,685,515,754,308,595,873,206,793,942,100,502,496,595,587,685,935,446,315,91,91,17,251,72,137,712,610,789,59,646,828,946,27,654,707,838,623,950,657,93,761,214,281,582,238,600,796,641,195,678,263,32,580,311,958,231,862,191,421,648,325,29,236,458,539,242,583,748,684,703,291,237,819,588,577,5,540,994,29,823,666,374,151,29,892,322,418,720,828,204,30,935,952,893,709,726,379,978,162,978,87,691,901,269,694,453,121,63,548,264,891,731,497,141,810,263,136,618,651,510,404,608,660,867,342,358,917,906,692,392,811,269,313,925,737,800,997,234,508,294,952,339,49,765,859,512,840,728,981,108,37,37,612,372,423,11,799,458,828,951,29,994,596,945,861,609,871,826,696,71,358,928,294,823,86,140,882,195,522,511,209,488,513,782,272,608,573,607,350,676,792,863,516,565,29,404,510,220,330,97,578,993,302,760,549,754,461,475,644,257,25,664,227,786,468,339,663,580,720,898,633,632,586,857,512,319,666])
print(type(result))
print(result)
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
        if start==end or startB==endB:          
            print("check A:{} to {},B {} to {}".format(start,end,startB,endB))
            targetIndex=self.binarySearchWithRange(B,A[start],startB,endB,False)
            if A[start]==B[targetIndex]:
                print("append",A[start])
                intersection.append(A[start])
            print("return")
            print()
            return
        
        length=len(A)
        if length==0:
            return
        elif length==1:
            return
        #取中位,分左右区间
        mediumIndex=int((start+end+1)/2)
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
"""
