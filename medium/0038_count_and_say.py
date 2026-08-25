class Solution:
    def countAndSay(self, n: int) -> str:
        result = '1'
        
        def RLE(input_n):
            count = 1
            result = ''
            
            for i in range(1,len(input_n)):
                if input_n[i] == input_n[i-1]:
                    count += 1
                else :
                    result += f'{count}{input_n[i-1]}'
                    count = 1
            result += f'{count}{input_n[-1]}'

            return result

        for i in range(n - 1):
            result = RLE(result) 

        return result
                