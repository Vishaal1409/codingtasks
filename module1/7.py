import random
def bubble_sort(arr):
    a = arr[:]
    count = 0
    for i in range(len(a)):
        for j in range(0, len(a) - i - 1):
            count += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a, count
def insertion_sort(arr):
    a = arr[:]
    count = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            count += 1
            a[j + 1] = a[j]
            j -= 1
        count += 1
        a[j + 1] = key
    return a, count
def selection_sort(arr):
    a = arr[:]
    count = 0
    for i in range(len(a)):
        min_idx = i
        for j in range(i + 1, len(a)):
            count += 1
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a, count
if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    arr = [random.randint(0, 100) for _ in range(n)]
    print("Original Array:", arr)
    algorithms = {
        "Bubble Sort": bubble_sort,
        "Insertion Sort": insertion_sort,
        "Selection Sort": selection_sort
    }
    for name, func in algorithms.items():
        sorted_arr, comparisons = func(arr)
        print(f"\n{name}:")
        print("Sorted Array:", sorted_arr)
        print("Comparisons:", comparisons)
