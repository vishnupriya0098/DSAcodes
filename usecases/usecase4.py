class Solution:
    def searchRange(self,num,target):
        def findleft(num,target):
            left,right=0,len(num)-1
            while left<=right:
                middle=left+(right-left)//2
                print(middle)
                if num[middle]<target:
                    left=middle+1
                    print(left)
                else:
                    right=middle-1
            return left
        def findright(num,target):
            left,right=0,len(num)-1
            while left<=right:
                middle=left+(right-left)//2
                print("mid",middle)
                if num[middle]<target:
                    left=middle+1
                else:
                    right=middle-1
            return right
        
        index_left=findleft(num,target)
        print(index_left)
        indexright=findright(num,target)
        print(indexright)

        if index_left<=indexright and index_left<len(num) and index_left==target :
            return[index_left,indexright]
        else:
            return[-1,-1]

