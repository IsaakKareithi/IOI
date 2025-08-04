# Function to return the index if element is found

def binarySearch(arr, l, r, x):

    while l<= r:

        mid = l +(r - 1) // 2

        # Check if x is present at mid
        if arr[mid] == x:
            return mid
        
        # if x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1

        # If x is smaller, ignore right half
        else: 
            r = mid - 1

    # return -1 if element isn't found
    return -1

# Driver code
arr = [2,3,4,10,40]
x = 10

# Function call

result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element {} is present at index {}.".format(x, result))
else:
    print("Element is not present in array")