def selection_sort(arr: list[int]) -> list[int]:
    """Sort a list of integers in-place using Selection Sort and print each step."""
    n = len(arr)

    if n <= 1:
        print(f"Step 0 (already sorted): {arr}")
        return arr

    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f"Step {i + 1}: {arr}")

    return arr