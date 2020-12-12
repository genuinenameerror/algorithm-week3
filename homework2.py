s = "(())()"


def is_correct_parenthesis(string):
    # 구현해보세요!
    opener=[]
    closer=[]
    counter_opener=0
    stringlist = []
    for ch in string:
        stringlist.append(ch)
    #print(stringlist)
    while len(stringlist)>0:
        if stringlist[0] =='(':
            opener.append(stringlist.pop(0))
            counter_opener+=1
        elif counter_opener ==0:
            return False
        else:
            closer.append(stringlist.pop(0))
            counter_opener-=1
        #print(opener, closer)   

    return len(opener) == len(closer)


print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!

