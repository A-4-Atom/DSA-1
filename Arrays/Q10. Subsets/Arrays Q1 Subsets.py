class Solution:
    def subsets(self, nums):
        result = []

        def backtrack(start, current_subset):
            result.append(current_subset[:])

            for i in range(start, len(nums)):
                current_subset.append(nums[i])
                backtrack(i + 1, current_subset)
                current_subset.pop()

        # Start backtracking from index 0
        backtrack(0, [])
        return result

sol = Solution()
nums = [1, 2, 3]
print(sol.subsets(nums))
