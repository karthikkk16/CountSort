def count_sort(array):
    maximum=max(array)
    count=[0]*(maximum+1)
    for i in array:
        count[i]+=1
    output=[]
    for i in range(len(count)):
        output.extend(count[i]*[i])
    return output

array=list(map(int,input("Enter the array elements : ").split()))
print(count_sort(array))