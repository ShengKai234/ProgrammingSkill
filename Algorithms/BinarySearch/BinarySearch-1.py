class BinarySearch_1:
    def binarySearch(self, nums, target):
        
        n = len(nums)
        l, r = 0, n - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1

if __name__ == "__main__":
    binarySearch_1 = BinarySearch_1()
    arr = [1,3,4,71,400,100]
    target = 4
    print(binarySearch_1.binarySearch(arr, target))
    target = 5
    print(binarySearch_1.binarySearch(arr, target))
    arr = [5]
    target = 5
    print(binarySearch_1.binarySearch(arr, target))