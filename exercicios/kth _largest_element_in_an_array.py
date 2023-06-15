class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickselect(nums, 0, len(nums) - 1, len(nums) - k)

    def quickselect(self, nums: List[int], left: int, right: int, k_smallest: int) -> int:
        if left == right:
            return nums[left]

        pivot_index = self.partition(nums, left, right)
        if k_smallest == pivot_index:
            return nums[k_smallest]
        elif k_smallest < pivot_index:
            return self.quickselect(nums, left, pivot_index - 1, k_smallest)
        else:
            return self.quickselect(nums, pivot_index + 1, right, k_smallest)

    def partition(self, nums: List[int], left: int, right: int) -> int:
        pivot = nums[right]
        i = left - 1

        for j in range(left, right):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]

        nums[i + 1], nums[right] = nums[right], nums[i + 1]
        return i + 1
