class Solution:
    def majorityElement(self, nums: List[int]) -> int:


        event = {}


        for num in nums:

            if num not in event:

                event[num] = 1
            else:

                event[num] += 1


        max_count = 0
        res = None

        for key,value in event.items():

            if value > max_count:

                max_count = value

                res = key
        return res

            
            


        