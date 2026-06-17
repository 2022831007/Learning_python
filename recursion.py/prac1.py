#WAF a recursive function to calculate the sum of the first n natural numbers
def cal_sum(n):
    
    if(n==0):
        return 0
    
    return cal_sum(n-1)+n  

print(cal_sum(5)) 
#WAF to print all elements in a list 
nums=[9,4,5,6,7]
def print_list(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)


print_list(nums)