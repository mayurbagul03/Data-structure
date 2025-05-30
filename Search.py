search_arr = [4,7,1,9,2]
target = 12
found = False

for i in range(len(search_arr)):
    if search_arr[i] == target:
        found = True
        print("found at index:",i)
        break

if not found:
    print('Not found')