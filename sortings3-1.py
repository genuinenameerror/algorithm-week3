#array_a = [1, 2, 3, 5,100]
#array_b = [4, 6, 7, 8,11,55,99]
#array_c = [1,3,4, 6, 7, 8,11,55,99]
array_x = [10,9,8,7,6,5,4,3,2,1]
def divide(array):
    l = len(array)
    array_d =[]
    for element in array:
        array_f = [element]
        array_d.append(array_f)
        #print(array_f)
    return array_d           
def merge(array1, array2):
    array_m = []

    while len(array1)>0 and len(array2)>0:
        if array1[0] > array2[0]:
            popped = array2.pop(0)
        else:
            popped = array1.pop(0)
        array_m.append(popped)

    if len(array1)>0:
        array_m.extend(array1)
    else:
        array_m.extend(array2)
    return array_m

def mergesort(array):
    array_d = divide(array)
    print("정렬할 리스트:",array)
    print("분할정복할 리스트:",array_d)
    while len(array_d)>1:
        temp_l = array_d.pop(0)
        temp_r = array_d.pop(len(array_d)-1)
        print("합병할 리스트:",temp_l,temp_r)
        temp_m = merge(temp_l,temp_r)
        print("분할정복한 리스트:",temp_m)
    
        if len(array_d)-2>=0:
            temp_l = array_d[0:(len(array_d)//2)]
            temp_r = array_d[(len(array_d)//2):len(array_d)]
            array_d = temp_l+[temp_m]+temp_r
            
        else:
            array_d = array_d + [temp_m]
        print("현재 정렬:",array_d)
    return array_d[0]



#print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!
#print(array_c)
#print(divide(array_c))
print(mergesort(array_x))
#m =[1,5,7,11,29]
#n = [2,6,9,33]
#print(merge(m,n))
