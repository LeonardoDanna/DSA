class Solution(object):
    def rob(self, nums):
        one_before, two_before = 0,0

        for n in nums:
            temp = max(n + two_before, one_before)
            two_before = one_before
            one_before = temp

        return one_before
