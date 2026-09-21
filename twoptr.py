# ptr = [1,3,9,5,7,10,11,0]
# target  = 9
# left =0
# right = len(ptr)-1
# found = False

while left < right:
    sum = ptr[left] + ptr[right]
    if sum == target:
        print(f"Pair Found {ptr[left]}+{ptr[right]}={target}")
        found = True
        break
    elif sum < target:
        left +=1
    else:
        right -=1
if not found:
    print("Pair Not Found")


