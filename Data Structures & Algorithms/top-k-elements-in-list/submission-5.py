class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort() 
        respuesta = []

        r = []
        contador = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                contador += 1
            else:
                r.append([contador, nums[i-1]])
                contador = 1

        r.append([contador, nums[-1]])
        r.sort()

        respuesta = []
        while len(respuesta) < k:
            respuesta.append(r.pop()[1])

        return respuesta