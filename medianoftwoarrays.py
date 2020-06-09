"""[1, 3]
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        i = 0
        j=0
        m1= 0
        m2 = 0
        median_ind = int((m+n)/2)
        if (m+n)%2 == 1:
            for lt in range(median_ind+1):
                #print(m1,i,j,m,n,lt)
                if i!=m and j!=n:
                    if nums1[i] <= nums2[j]:
                        m1=nums1[i]
                        i+=1
                    else:
                        m1 = nums2[j]
                        j+=1
                elif i < m:
                    m1 = nums1[i]
                    i+=1
                else:
                    m1 = nums2[j]
                    j+=1
                #print(m1,i,j,m,n)
            return m1
                        
        else:
            for lt in range(median_ind+1):
                m2 = m1
                if i!=m and j!=n:
                    if nums1[i] <= nums2[j]:
                        m1=nums1[i]
                        i+=1
                    else:
                        m1 = nums2[j]
                        j+=1
                elif i < m:
                    m1 = nums1[i]
                    i+=1
                else:
                    m1 = nums2[j]
                    j+=1
            return (m1+m2)/2


if __name__ == '__main__':
    sol = Solution()
    arr1 = [1, 3]
    arr2 = [2]
    assert sol.findMedianSortedArrays(arr1,arr2) == 2.0
    arr1 = [1, 2]
    arr2 = [3, 4]
    assert sol.findMedianSortedArrays(arr1,arr2) == 2.5
        
