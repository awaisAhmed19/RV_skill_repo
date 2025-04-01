import math

def convert_min_heap_to_max_heap(heap):
    """Converts a min-heap to a max-heap."""
    n = len(heap)
    last_non_leaf_node_index = math.floor(n / 2) - 1

    for i in range(last_non_leaf_node_index, -1, -1):
        max_heapify(heap, i, n)

def max_heapify(heap, i, n):
    """Maintains the max-heap property."""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and heap[left] > heap[largest]:
        largest = left

    if right < n and heap[right] > heap[largest]:
        largest = right

    if largest != i:
        heap[i], heap[largest] = heap[largest], heap[i]  # Swap
        max_heapify(heap, largest, n)

# Example Usage
min_heap = [1, 3, 5, 6, 15, 7, 9, 20, 21]
print("Original Min-Heap:", min_heap)

convert_min_heap_to_max_heap(min_heap)
print("Converted Max-Heap:", min_heap)
