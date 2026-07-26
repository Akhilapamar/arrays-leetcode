class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}  # Dictionary to store number and its index
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # Check if complement exists in dictionary/
            if complement in num_map:
                return [num_map[complement], i]
            
            # Store the current number with its index
            num_map[num] = i


# ----------- Test Cases -----------

if __name__ == "__main__":
    sol = Solution()
    
    print(sol.twoSum([2,7,11,15], 9))   # Expected: [0,1]
    print(sol.twoSum([3,2,4], 6))       # Expected: [1,2]
    print(sol.twoSum([3,3], 6))         # Expected: [0,1]

        

        
        