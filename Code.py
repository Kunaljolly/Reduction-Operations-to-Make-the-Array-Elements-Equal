class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        # Sort the array in non-increasing order
        nums.sort(reverse=True)
        operations = 0
        # Iterate through the array
        for i in range(1, len(nums)):
            # If the current element is different from the previous one,
            # it means we need to perform operations to reduce it
            if nums[i] != nums[i - 1]:
                operations += i
        return operations
