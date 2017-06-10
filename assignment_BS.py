def binary_search(a_list, item):
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list)//2
        if a_list[midpoint] == item:
            return True
        elif item < a_list[midpoint]:
                return binary_search(a_list[:midpoint], item)
        else:
            return binary_search(a_list[midpoint + 1:],item)

T_list = [ 3, 5, 6, 8, 11, 12, 14, 15, 17, 18 ]
print (binary_search(T_list,8))
# comparison 1: midpoint=4, item= 8 < a_list[midpoint]= 12  left items:[3,5,6,8,11]
# comparison 2: midpoint=2, item > a_list[midpoint]= 6      left items:[8,11]
# comparison 3: midpoint=1 item < a_list[midpoint]= 11      left item:[8]
# comparison 4: midpoint=0 item = a_list[midpoint]= 8       done

print (binary_search(T_list,16))
# comparison 1: midpoint=4, item= 16 > a_list[midpoint]= 12  left items:[14,15,17,18]
# comparison 2: midpoint=2, item < a_list[midpoint]= 17      left items:[14,15]
# comparison 3: midpoint=1, item > a_list[midpoint]=15       no item left, False
