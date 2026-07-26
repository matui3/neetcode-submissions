class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        

        def mergeSort(arr, left, right):
            if left < right:
                mid = left + (right - left) // 2
                mergeSort(arr, left, mid)
                mergeSort(arr, mid + 1, right)
                merge(arr, left, mid, right)

    
        def merge(arr, left, mid, right):
            # left sub array size
            left_subarray_size = mid - left + 1
            right_subarray_size = right - mid

            left_subarray = [0] * left_subarray_size
            right_subarray = [0] * right_subarray_size

            for i in range(left_subarray_size):
                left_subarray[i] = arr[left + i]
            
            for j in range(right_subarray_size):
                right_subarray[j] = arr[mid + 1 + j]
            
            i = 0
            j = 0
            k = left

            while i < left_subarray_size and j < right_subarray_size:
                if left_subarray[i] <= right_subarray[j]:
                    arr[k] = left_subarray[i]
                    i += 1
                else:
                    arr[k] = right_subarray[j]
                    j += 1
                k += 1

            while i < left_subarray_size:
                arr[k] = left_subarray[i]
                i += 1
                k += 1
            
            while j < right_subarray_size:
                arr[k] = right_subarray[j]
                j += 1
                k += 1
        
        mergeSort(nums, 0, len(nums) - 1)
        return nums


        