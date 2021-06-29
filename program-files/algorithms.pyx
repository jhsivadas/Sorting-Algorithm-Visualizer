import time
import cython

# Sorting Algorithms
class Algos:
    def __init__(self, type):
        self.type = type

    def merge(self, left_input, right_input, mid_input, arr, draw, speed):
        cdef int left, right, mid
        left = left_input
        right = right_input
        mid = mid_input

        arr1 = arr[left:mid + 1]
        arr2 = arr[mid + 1:right + 1]
        cdef int arr1_index = 0
        cdef int arr2_index = 0
        cdef int swap = 0

        while left < right + 1:
            if arr1_index < len(arr1) and arr2_index < len(arr2):
                if arr1[arr1_index] <= arr2[arr2_index]:
                    arr[left] = arr1[arr1_index]
                    arr1_index += 1
                    swap = left + arr1_index
                else:
                    arr[left] = arr2[arr2_index]
                    arr2_index += 1
                    swap = mid + 1 + arr2_index
                draw(arr, swap, left)
                time.sleep(2 / speed)
            else:
                if arr1_index < len(arr1):
                    arr[left] = arr1[arr1_index]
                    arr1_index += 1
                    swap = left + arr1_index
                elif arr2_index < len(arr2):
                    arr[left] = arr2[arr2_index]
                    arr2_index += 1
                    swap = mid + 1 + arr2_index
                draw(arr, swap)
                time.sleep(2 / speed)
            left += 1

    def merge_sort(self, left, right, arr, draw, speed):
        if left < right:
            mid = (left + right) // 2
            self.merge_sort(left, mid, arr, draw, speed)
            self.merge_sort(mid + 1, right, arr, draw, speed)
            self.merge(left, right, mid, arr, draw, speed)

    def insert_sort(self, arr, draw, speed):
        cdef int location, comp, curr
        for location in range(1, len(arr)):
            comp = arr[location]
            curr = location
            while curr > 0 and comp < arr[curr - 1]:
                arr[curr] = arr[curr - 1]
                curr = curr - 1
                draw(arr, curr, comp)
            arr[curr] = comp
            draw(arr, curr, comp)
            time.sleep(2 / speed)

    def quick_sort(self, left, right, arr, draw, speed):
        if len(arr) < 2:
            return arr
        if left < right:
            pivot = self.partition(left, right, arr, draw, speed)
            self.quick_sort(left, pivot - 1, arr, draw, speed)
            self.quick_sort(pivot + 1, right, arr, draw, speed)

    def partition(self, left, right, arr, draw, speed):
        cdef int x, i, j
        x = arr[right]
        i = left - 1
        for j in range(left, right + 1):
            if arr[j] <= x:
                i += 1
                if i < j:
                    arr[i], arr[j] = arr[j], arr[i]
                    draw(arr, i, j)
                    time.sleep(2 / speed)
        return i

    def bubble_sort(self, arr, draw, speed):
        cdef int i, k
        for i in range(0, len(arr) - 1):
            for k in range(0, len(arr) - 1):
                if arr[k] > arr[k + 1]:
                    new = arr[k + 1]
                    arr[k + 1] = arr[k]
                    arr[k] = new
                    draw(arr, k, k + 1)
                    time.sleep(2 / speed)
                draw(arr)

    def selection_sort(self, arr, draw, speed):
        cdef int i, index
        for i in range(len(arr)):
            # Finds the min
            min = arr[i]
            min_index = i
            for index in range(i + 1, len(arr)):
                if arr[index] < min:
                    min = arr[index]
                    min_index = index
                draw(arr, index)
                time.sleep(2 / speed)
            # Swaps
            new = arr[i]
            arr[i] = min
            arr[min_index] = new
            draw(arr, i, min_index)
            time.sleep(3 / speed)
        return arr