class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        newlist = []


        for i in nums:

            if i != val:

                newlist.append(i)
        
        

        for i in range(len(newlist)):

            nums[i] = newlist[i]

        return len(newlist)



            


        

        