'''
비교
0,1,2,3,4 중에서
0을 정렬되어 있다고 가정함
1이 0보다 큰지 작은지 판정해서 자리바꿈
0,1이 정렬됨
2가 1보다 크면 그대로
1보다 작으면 0보다 크면 1과 자리바꿈
0보다 작으면 0과 자리바꿈

0,1,2가 정렬됨
3을 2와 비교함
2보다 작으면 1과도 비교
1보다도 작으면 0과도 비교
'''
input = [9,6, 3,4, 2,7, 1,8]


def insertion_sort(array):
    # 이 부분을 채워보세요!
    print("정렬 시작:",array)
    for i in range(1,len(array)): #1, 2, 3, 4
        index=i
        comp = i-1
        print("array[",i,"] =",array[i],"비교")
        
        while comp>=0 and array[i] < array[comp]:
            index-=1
            comp-=1
        if index<i:
            print(index,"번으로 이동")
            temp = array[i]
            # 5번을 index번으로 보내야 한다면
            #temp에 array[5] 저장하고
            # array[5] = array[4], array[4] = array[3], .... array[index+1] = array[index] 한 다음에
            # array[index] = temp
            for j in range(i,index,-1):
                array[j] = array[j-1]
            array[index] = temp
        print(i,"번 이하 정렬 완료:",array)
        
                
    return array


insertion_sort(input)
print("결과:",input) # [1, 2, 4, 6, 9] 가 되어야 합니다!
