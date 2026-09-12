# Import time
import time

# Import test cases
from test_cases import *

# Actual Algorithm
def bubble_sort(arr: list[object]) -> list[object]:
    new_arr = arr.copy() # Make the function pure
    swapping: bool = True
    end: int = len(new_arr)
    while swapping:
        swapping = False
        for i in range(1, end):
            if new_arr[i - 1] > new_arr[i]:
                temp = new_arr[i]
                new_arr[i] = new_arr[i - 1]
                new_arr[i - 1] = temp
                swapping = True
        end -= 1
    return new_arr

# Test Cases
if __name__ == "__main__":
    try:
        first_time = time.time()
        print(bubble_sort(integers))
        second_time = time.time()
        print(f"First run took: {round((second_time - first_time), 5)} seconds")
        third_time = time.time()
        print(bubble_sort(floats))
        fourth_time = time.time()
        print(f"Second run took: {round((fourth_time - third_time), 5)} seconds")
    except Exception as e:
        print(f"Oops something unexpected happened: {e}")