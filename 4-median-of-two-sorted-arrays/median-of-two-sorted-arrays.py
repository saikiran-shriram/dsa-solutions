class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if  len(nums1) > len(nums2): 
            nums1, nums2 = nums2, nums1             
        m= len(nums1)          
        n = len(nums2)           
        def fun()   :
            low = 0          
            high = m          
            while low <= high : 
                mid = (low + high)//2            
                i = mid    
                j = (m+n+1)//2 - i       
                if i == 0 : 
                    left1 = float('-inf')    
                else :  
                    left1 = nums1[i-1]        
                if j ==0 : 
                    left2 = float('-inf')  
                else :  
                    left2 = nums2[j-1]          
                if i==m : 
                    right1 = float('inf')   
                else :  
                    right1 = nums1[i]       
                if j == n : 
                    right2 = float('inf')  
                else: 
                    right2 = nums2[j]         
                if left1 > right2 : 
                    high = mid-1           
                elif left2 > right1 : 
                    low = mid+1        
                else : 
                    total = (m+n) % 2          
                    if total != 0 :  
                        return float(max(left1 , left2))            
                    else : 
                        return float((max(left1,left2) + min(right1 , right2))/2)          
        return fun()