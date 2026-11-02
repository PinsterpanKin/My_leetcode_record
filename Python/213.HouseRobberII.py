class MySolution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums1, nums2 = nums[1:], nums[:-1]
        rob1, rob2 = 0, 0
        for n in nums1:
            rob1, rob2 = rob2, max(rob2, rob1 + n)
        rob3, rob4 = 0, 0
        for n in nums2:
            rob3, rob4 = rob4, max(rob4, rob3 + n)
        return max(rob2, rob4)