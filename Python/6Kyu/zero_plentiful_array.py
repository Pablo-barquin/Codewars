def zero_plentiful(arr):
    '''Función que haya si el array es zero-plentiful'''
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
