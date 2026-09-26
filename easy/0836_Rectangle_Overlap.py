class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        x1 = 0
        y1 = 1
        x2 = 2
        y2 = 3
        if rec1[x2] <= rec2[x1] :
            return False
        if rec2[x2] <= rec1[x1] :
            return False
        if rec1[y1] >= rec2[y2] :
            return False
        if rec2[y1] >= rec1[y2] :
            return False
        return True