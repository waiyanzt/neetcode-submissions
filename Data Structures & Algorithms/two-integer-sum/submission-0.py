class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a hashmap
        # add array elements (numbers) as keys and their indices as the values
        # so if we see the number pop out, we can check if the hashmap has the corresponding complement to hit the given target

        HashMap = {}
        for i, n in enumerate(nums): # --> this gives us index number ; cleanly
            diff = target - n
        
            if diff in HashMap:
                return [HashMap[diff], i]
            HashMap[n] = i
        

