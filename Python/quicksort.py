def quicksort(input_list):

        def orders(input_list,l,r):
        
        if l >= r: 
            return None
        
        pivot = choosepivot(input_list,l,r)
        
        aux = input_list[pivot]
        input_list[pivot] = input_list[l]
        input_list[l] = aux

        new_pivot = partition(input_list,l,r)
        
        orders(input_list,l,new_pivot-1)
        orders(input_list,new_pivot+1,r)

    orders(input_list,0,len(input_list))