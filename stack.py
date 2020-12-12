class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
    def push(self, value):                 # 현재 [4] 밖에 없다면
        new_head = Node(value)             # [3] 을 만들고!
        new_head.next = self.head          # [3] -> [4] 로 만든다음에
        self.head = new_head               # 현재 head의 값을 [3] 으로 바꿔준다.


    # pop 기능 구현
    def pop(self):
        if self.is_empty():                  # 만약 비어있다면 에러!
            return "Stack is empty!"
        delete_head = self.head              # 제거할 node 를 변수에 잡습니다.
        self.head = self.head.next           # 그리고 head 를 현재 head 의 다음 걸로 잡으면 됩니다.
        return delete_head                   # 그리고 제거할 node 반환

    def peek(self):
        if self.is_empty():
            return "Stack is empty!"

        return self.head.data

    # isEmpty 기능 구현
    def is_empty(self):
        return self.head is None
    
top_heights = [6, 9, 5, 7, 4]


def get_receiver_top_orders(heights):
    
    receiver=[]
    for i in range(len(heights)):
        receiver.append(0)
    #print("line 39")

    for i in range(0,len(heights)): # 0,1,2,3,4
        
        index = i-1
        height_now = heights[i]
        
        while index>=0:
            if heights[index]<height_now:
                height_now = heights[index]
                index-=1
                print(i,": line 51")
            else:
                print(i,": else")
                receiver[i] = index+1
                break  
                
    return receiver


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!
