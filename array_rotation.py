def left_rotate(arr):
    if not arr:
        return arr
    left_most_ele=arr[0]
    length=len(arr)
    for i in range(length-1):
        arr[i],arr[i+1]=arr[i+1],arr[i]
    arr[length-1]=left_most_ele
    return arr
#print(left_rotate([1,2,3,4,5]))

def left_rotate(arr,N):
    if not arr:
        return arr
    length=len(arr)
    rotated_arr=[]
    for i in range(N,N+length):
        rotated_arr.append(arr[i%length])
    return rotated_arr
#print(left_rotate([1,2,3,4,5],1))

def left_rotate(arr,N):
    if not arr:
        return arr
    return [arr[i % len(arr)] for i in range(N, N + len(arr))]

print(left_rotate([1,2,3,4,5],1))

