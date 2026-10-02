class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        required_left = (len(nums1) + len(nums2) + 1) // 2
        low = 0
        high = len(nums1)
        while low <= high:
            cut1 = (low + high) // 2
            cut2 = required_left - cut1
            if cut1 == 0 :
                left1 = -inf
                if len(nums1) == 0:
                    right1 = inf
                else:
                    right1 = nums1[0]
            elif cut1 == len(nums1) :
                left1 = nums1[cut1 - 1]
                right1 = inf
            else :
                left1 = nums1[cut1 - 1]
                right1 = nums1[cut1]
            if cut2 == 0 :
                left2 = -inf
                right2 = nums2[0]  
            elif cut2 == len(nums2) :
                left2 = nums2[cut2 - 1]
                right2 = inf
            else :
                left2 = nums2[cut2 - 1]
                right2 = nums2[cut2]

            if left1 > right2:
                high = cut1 - 1   
            elif left2 > right1:
                low = cut1 + 1  
            else :
                max_left = max(left1, left2)
                min_right = min(right1, right2)
                total = (len(nums1)+len(nums2))
                if total %2 == 0 :
                    median = (max_left + min_right) / 2     
                else :
                    median = max(left1, left2)
                return median