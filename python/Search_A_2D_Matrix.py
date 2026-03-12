class Solution(object):
    def searchMatrix(self, matrix, target):
        flag_list=[]
        for sublists in matrix:
            for item in sublists:
                flag_list.append(item)
        if target in flag_list:
            return True
        else:
            return False
