class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        # สำหรับถ้าหาไม่เจอ
        ans = -1
        if len(nums)  > k:
            count = {}
            # make all nums count = 0
            for n in nums:
                count[n] = 0
            # subarray 
            for i in range(len(nums)-k+1):
                for j in nums[i:i+k]:
                    count[j] += 1
            # หาว่าตัวไหนที่มี count เป็น 1 เพื่อที่จะได้หาว่าเป็นค่าสูงสุดไหม 
            for num, c in count.items():
                if c == 1:
                    ans = max(ans, num)
        # กรณีที่เท่ากันคือทุกตัวcount จะเป็น 1 
        elif len(nums) == k :
            return max(nums)
        
        return ans
