def merge(array1, array2):
    array_m = []
    #print("array_a =",array_a,"array_b =",array_b,"합병 시작")
    while len(array1)>0 and len(array2)>0:
        if array1[0] > array2[0]:
            popped = array2.pop(0)
        else:
            popped = array1.pop(0)
        array_m.append(popped)
        #print("array_a =",array_a,"array_b =",array_b,"array_m =",array_m)
    # 이 부분을 채워보세요!
    #print("합병정렬 직후:",array1,array2)
    if len(array1)>0:
        array_m.extend(array1)
    else:
        array_m.extend(array2)
    return array_m
m =[1,5,7,11,29]
n = [2,6,9,33]
print(merge(m,n))
