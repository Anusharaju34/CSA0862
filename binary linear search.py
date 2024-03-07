def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def main():
    while True:
        search_type = input("Enter 'l' for linear search, 'b' for binary search, or 'q' to quit: ")

        if search_type == 'q':
            print("Exiting the program.")
            break

        arr = list(map(int, input("Enter a sorted list of numbers (space-separated): ").split()))
        target = int(input("Enter the target number to search for: "))

        if search_type == 'l':
            result = linear_search(arr, target)
        elif search_type == 'b':
            result = binary_search(arr, target)
        else:
            print("Invalid input. Please enter 'l', 'b', or 'q'.")
            continue

        if result != -1:
            print(f"Target {target} found at index {result}.")
        else:
            print(f"Target {target} not found in the list.")

print(main())
