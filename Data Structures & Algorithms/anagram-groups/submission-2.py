class Solution:
    def groupAnagrams(self, strs):
      
        r = []
        used = set() #usamos un set para que no haya repetidos

        for i in range(len(strs)):
            if i in used:
                continue # si el que estamos usando se encuentra se los salta
            x = [strs[i]]
            used.add(i)
            for j in range(i+1, len(strs)):
                if j not in used and sorted(strs[i]) == sorted(strs[j]):
                    x.append(strs[j])
                    used.add(j)
            r.append(x)

        return r