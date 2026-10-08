class Solution:
    def removeOuterParentheses(self, s: str) -> str:
    
        prm = []
        ans = ''
        depht = 0
        total = ''

        for i in s :
            total += i
            if i == '(' :
                depht += 1
                # สามารถลัดขั้นตอนโดยการเก็บแต่ depht > 0 ได้
            else :
                depht -= 1 
                # สามารถลัดได้เช่นกัน
                if depht == 0 :
                    prm.append(total)
                    total = ''
        # ถ้าลัดตัวนี้จะไม่จำเป็น
        for p in prm :
            p = p[1:-1]
            ans += p
        return ans