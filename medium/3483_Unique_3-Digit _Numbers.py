class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        
        seen = set()

        # brute force   
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    # check not same index
                    if i == j or j == k or k == i :
                        continue 
                    # check last digits is even and not leading zero(no 0 in font)
                    elif  digits[k] % 2 == 0 and digits[i] != 0:
                        # check not seen
                        if (digits[i],digits[j],digits[k]) not in seen :
                            seen.add((digits[i],digits[j],digits[k]))

        return len(seen)
                    