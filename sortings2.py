input = [4, 6, 2, 9, 1]


def selection_sort(array):
    # 이 부분을 채워보세요!
    for i in range(0,len(array)-1): #0,1,2,3        
        print(array[i],"비교")
        min_value=array[i+1]
        min_index = i+1
        for j in range(i+1,len(array)): #1,2,3,4
            print(j,"번과 비교")
            #if array[i]>array[j]:
            #    array[i],array[j] = array[j],array[i]
            #
            if min_value>array[j]:
                min_value = array[j]
                min_index = j
        print(array[i],"와",min_value,"비교")
        if array[i]>min_value:
            array[i],array[min_index] = array[min_index],array[i]
        print(array)
    return array

selection_sort(input)
print("결과:",input) # [1, 2, 4, 6, 9] 가 되어야 합니다!
