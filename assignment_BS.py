def binary_search(a_list, item):
    first = 0
    last = len(a_list)-1
    found = False
    while first <= last and not found:
        midpoint = (first + last)//2
        if a_list[midpoint] == item:
            found = True
        else:
            if item <= a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found

T_list = [ 3, 5, 6, 8, 11, 12, 14, 15, 17, 18 ]
print (binary_search(T_list,8))
#1st step: first=0,last=9,midpoint=4, item=8 < a_list[midpoint]=11
#2nd step: first=0,last=3,midpoint=1, item > a_list[midpoint]=5      group: [3,5,6,8]
#3rd step: first=2,last=3,midpoint=2 item > a_list[midpoint]=6       group: [6,8]
#4th step: first=3,last=3,midpoint=3 item =  a_list[midpoint]=8      group: [8]

print (binary_search(T_list,16))
#1st step: first=0,last=9,midpoint=4, item=16 > a_list[midpoint]=11
#2nd step: first=5,last=9,midpoint=7, item > a_list[midpoint]=15     group: [12,14,15,17,18]
#3rd step: first=8,last=9,midpoint=8 item < a_list[midpoint]=17      group: [17,18]
