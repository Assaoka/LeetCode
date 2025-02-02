class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        ini, fim = 0, len(nums) - 1
        while ini <= fim:
            meio = (ini + fim)//2
            if nums[meio] == target: return meio
            elif nums[meio] < target: ini = meio + 1
            else: fim = meio - 1

        return -1
    