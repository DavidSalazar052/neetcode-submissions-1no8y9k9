class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #vemos que sean del mismo tamaño
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
 

        