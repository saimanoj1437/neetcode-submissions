class Solution:
    def isAnagram(self, s: str, t: str) -> bool:


        countS = {}

        countT = {}

        if len(s) != len(t):
            return False


        for c in s:

            if c in countS:

                countS[c] += 1
            else:
                countS[c] = 1

        print(countS)

        for c in t:

            if c not in countS or countS[c] == 0:
                return False

            countS[c] -= 1

        return True



        

        