# using binary search
# link: https://github.com/Rouzbeh1797/Leetcode/blob/main/Binary%20Search.py
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target<matrix[0][0] or target>matrix[-1][-1]:
            return False
        def BsearchRow(l,r):
            if l>r:
                return r
            mid=(l+r)//2
            if matrix[mid][0]==target:
                return mid
            if matrix[mid][0]>target:
                r=mid-1
                return BsearchRow(l,r)
            else:
                l=mid+1
                return BsearchRow(l,r)
        row=BsearchRow(0,len(matrix)-1)
        def BsearchCol(l,r):
            if l>r:
                return False
            mid=(l+r)//2
            if matrix[row][mid]==target:
                return True
            if matrix[row][mid]>target:
                r=mid-1
                return BsearchCol(l,r)
            else:
                l=mid+1
                return BsearchCol(l,r)
        
        return BsearchCol(0,len(matrix[0])-1)
            
