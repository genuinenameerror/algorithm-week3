shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    # 이 곳을 채워보세요!
    def sort_elements(array):        
        for i in range(0,len(array)-1):            
            for j in range(0,len(array)-i-1):
                if array[j]<array[j+1]:
                    temp=array[j+1]
                    array[j+1] = array[j]
                    array[j] = temp                    
        return array
    prices = sort_elements(prices)
    coupons = sort_elements(coupons)

    for k in range(0,len(coupons)):
        prices[k] = int(prices[k] * (100-coupons[k])/100)
    print(prices)

    bottomline = 0
    for l in range(0,len(prices)):
        bottomline+=prices[l]      
    
    
    return bottomline


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.

