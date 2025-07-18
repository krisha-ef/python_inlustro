def even_num(nums):
   n=len(nums)
   result=[]
   for i in range(1<<n):
        subset=[]
        for j in range(n):
            if i&(1<<j):
                subset.append(nums[j])
        if sum(subset)%2==0:
            result.append(subset)
   return result
nums=[1,2,3,4]
even_set=even_num(nums)
for subset in even_set:
  print(subset)

