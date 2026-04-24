class Solution:
    def isAnagram(self, s: str, t: str) -> bool:


        countS = {}

        countT = {}

        if len(s) != len(t):
            return False


        for char in s:

            if char in countS:

                countS[char] += 1

            else:

                countS[char] = 1

            
        for char in t:

            if char not in countS or countS[char] == 0:

                return False

            countS[char] -= 1

        return True
        

            

        