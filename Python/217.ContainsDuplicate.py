class OriginalSolution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        record = {}
        for num in nums:
            if num in record:
                return True
            else:
                record[num] = 1
        return False

class OptimizedSolution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))