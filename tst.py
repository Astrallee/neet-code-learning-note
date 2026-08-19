def productExceptSelf(nums):
    length = len(nums)
    ## 先计算前缀积
    prefix = {}
    prefix[0]=1
    for index in range(1,length):
        prefix[index]=nums[index-1] * prefix[index-1]
    print("前缀积:",prefix)
    ## 计算后缀积
    suffix = {}
    suffix[length-1] =1
    for index in range(length-2,-1,-1):
        suffix[index] = nums[index+1] * suffix[index+1]
    print("后缀积:",suffix)
    output = []
    for i in range(0,length):
        output.append(prefix[i]*suffix[i]) 
    return output

def productExceptSelf2(nums):
    count_zero = 0
    zero_index = -1
    total_product = 1
    length = len(nums)
    output = []
    for index,item in enumerate(nums):
        if item == 0:
            count_zero +=1    
            zero_index = index    
        else:
            total_product  = total_product  * item 
    # 两个及以上0     
    if count_zero > 1:         
        return [0] * length
    if count_zero ==1:
        output = [0] * length
        output[zero_index] = total_product
        return output 
    for index in range(length):
        output.append(total_product  /nums[index])
    return output

nums=[1,2,4,6]
a = productExceptSelf2(nums)
print(a)