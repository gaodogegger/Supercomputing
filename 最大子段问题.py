#思路1：求出某个子段的和，再求出其邻近的子段的和相比较，如果它比邻近的字段的和都大，就输出
#思路2：求出所有可能子段的和，进行比较输出最大值，突然发现这是暴力法
#思路3：遍历数组，对于每个元素，决定是否将它添加到之前的子数组（即让当前子数组继续增长），还是从当前元素重新开始一个新的子数组。
def maxziduan(array):
    max_sum=array[0]#初始化这个值存储遍历过程中以当前数字为结尾的最大子数组和
    max2_summ=array[0]#初始化这个值表示迄今为止遍历到的最大子数组和
    for i in range(1, len(array)):
        max_sum=max(array[i],max_sum+array[i])
        max2_summ=max(max_sum,max2_summ)
        
    return max2_summ if max2_summ > 0 else 0
array=[1,2,3,4,-5,6,7,8,9]
result=maxziduan(array)
print(result)