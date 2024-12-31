def mergesort(input_list):
    n = len(input_list)
    
    def merge(left_list,right_list):
        n = len(left_list) + len(right_list)
        i = j = 0
        result = []
        for k in range(n):
            if left_list[k] < right_list[i]:
                result.append(left_list[i])
                i += 1
            else:
                result.append(right_list[j])
                j += 1
    
    if n<=1:
        return input_list
        
    middle = n //2
    left_list = mergesort(input_list[:middle])
    right_list = mergesort(input_list[middle:])
    
    result_list = merge(left_list,right_list)
    
    return result_list