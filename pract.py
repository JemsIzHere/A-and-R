num1 = [1,3]
num2 = [2]
num3 = []
mid = len(num3)/2
median = 0


def merge(arr1,arr2):
    ans =[]
    i=j=0
    while i < len(arr1) and j<len(arr2):
        if arr1[i]<=arr2[j]:
            ans.append(arr1[i])
            i+=1
        else:
            ans.append(arr2[j])
            j+=1
    ans.extend(arr1[i:])
    ans.extend(arr2[j:])

    return ans

num3 = merge(num1,num2)

if len(num3)%2 ==0:
    median = (num3[mid-1]+num3[mid]/2)
    print("yes")
else:
    median = len(num3)/2
    print("yes1")


print(mid)

print(median)
#median = 

            

    

