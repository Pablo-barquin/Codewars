''' 
An array is called zero-plentiful if it contains multiple zeros, and every sequence of zeros is at least 4 items long.

Your task is to return the number of zero sequences if the given array is zero-plentiful, oherwise 0.

Examples
[0, 0, 0, 0, 0, 1]  -->  1
# 1 group of 5 zeros (>= 4), thus the result is 1

[0, 0, 0, 0, 1, 0, 0, 0, 0]  -->  2
# 2 group of 4 zeros (>= 4), thus the result is 2

[0, 0, 0, 0, 1, 0]  -->  0 
# 1 group of 4 zeros and 1 group of 1 zero (< 4)
# _every_ sequence of zeros must be at least 4 long, thus the result is 0

[0, 0, 0, 1, 0, 0]  -->  0
# 1 group of 3 zeros (< 4) and 1 group of 2 zeros (< 4)

[1, 2, 3, 4, 5]  -->  0
# no zeros

[]  -->  0
# no zeros
'''

# MY SOLUTION
def zero_plentiful(arr):  
    if 0 not in arr:
        return 0
    else:
        count = 0
        while arr:
            if arr[0] == 0:
                nums, arr = arr[:4], arr[4:]
                if len(nums) != 4 or any(num != 0 for num in nums):
                    return 0
                else:
                    count += 1
                    while arr and arr[0] == 0:
                        arr.pop(0)
            else:
                arr.pop(0)

        return count
    
if __name__ == '__main__':
    print(zero_plentiful([0, 0, 0, 0, 1, 0]))