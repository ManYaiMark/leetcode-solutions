class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1 :
            return s    

        n = 0
        direction = 1
        
        rows = ['' for _ in range(numRows)]

        current_row = 0

        while n < len(s):

            rows[current_row] += s[n]
            current_row += direction
            n += 1

            if current_row == numRows - 1 or current_row == 0:
                direction *= -1 
    
        return "".join(rows)