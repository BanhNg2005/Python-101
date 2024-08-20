# bubble sort algorithm

def bubble_sort(arr):
    n = len(arr) # Get the length of the array
    for i in range(n):
        for j in range(0, n-i-1): # n-i-1 means the last element is already sorted
            if arr[j] > arr[j+1]: # Swap if the element found is greater
                arr[j], arr[j+1] = arr[j+1], arr[j] # Swap
    return arr

def main():
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {arr}")
    print(f"Sorted array: {bubble_sort(arr)}")

main()

# Time complexity: O(n^2) because of the 2 nested loops