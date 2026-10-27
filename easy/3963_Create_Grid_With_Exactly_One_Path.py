class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        # ถ้าเป็น 1 จะทำได้สองรูปแบบคือ ['.'*n] กับ ['.']*m
        if n == 1 :
            return ['.' for i in range(m)]
        elif m == 1:
            return ['.'*n]
        total = []
        for i in range(m):
            t = ''
            for j in range(n):
                # แถวแรกเป็น '.' ทั้งหมด 
                if i == 0 :
                    t += '.'
                # แถวสองเป็น '#'*n-1 + '.' เลยต้องทำงานคู่กับ else
                elif j == n - 1 :
                    t += '.'
                else :
                    t += '#'
            total.append(t)
        return total

        '''
        ไวกว่า แต่ทำเป็นรูปตัว L 
        arr = [('.'+'#'*(n-1))for i in range(m-1)]
        arr.append('.'*n)

        return arr'''