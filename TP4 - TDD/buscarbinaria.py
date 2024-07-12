def busca_binaria(array, element):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        
        if array[mid] == element:
            return True
        
        elif array[mid] < element:
            left = mid + 1

        else:
            right = mid -1


    return False