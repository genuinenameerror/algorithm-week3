input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    # 이 부분을 채워보세요!
    for i in range(0,len(array)-1): #0,1,2,3,4,
        #0차에 4번 확정, 1차에 3번 확정, 2차에 2번 확정, 3차에 1번 확정되면 0번도 확정되므로 len(array)-1 
        for j in range(0,len(array)-i-1): # 0과 1, 1과 2, 2와 3, 3과 4 5번 아니고 총 4번 비교 
            #temp = array[j+1]
            print(j,j+1,"비교")
            if array[j]>array[j+1]:
                #array[j+1] = array[j]
                #array[j] = temp
                array[j+1], array[j] = array[j],array[j+1]
            print(array)
        print(i,"단계 끝")
    return array


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!
