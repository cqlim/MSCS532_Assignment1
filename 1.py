def insertion_sort_desc(arr):
    # Traverse from the second element to the end
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements that are smaller than key
        # one position ahead of their current position
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Place the key in its correct position
        arr[j + 1] = key

    return arr

# Example usage
data = [12, 4, 56, 7, 23, 89, 1]
print("Original list:", data)
sorted_data = insertion_sort_desc(data)
print("Sorted in decreasing order:", sorted_data)
