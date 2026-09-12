Bubble-Sort-Algo

A small, clean Python implementation of the bubble sort algorithm, with timing benchmarks and simple test data for integers and floats.

How it works

The core function lives in main.py:

python
def bubble_sort(arr: list[object]) -> list[object]:
    new_arr = arr.copy()  # Make the function pure
    swapping: bool = True
    end: int = len(new_arr)

    while swapping:
        swapping = False
        for i in range(1, end):
            if new_arr[i - 1] > new_arr[i]:
                new_arr[i], new_arr[i - 1] = new_arr[i - 1], new_arr[i]
                swapping = True
        end -= 1

    return new_arr

It's a pure function — it copies the input list rather than mutating it — and includes two small optimizations over the textbook version:

Early exit: if a full pass makes no swaps, the list is already sorted and the loop stops.
Shrinking window: each pass guarantees the largest remaining element bubbles to its final position, so the comparison range shrinks by one each time.

This gives the classic bubble sort complexity:

Case	Time	Space
Best (already sorted)	O(n)	O(n)
Average	O(n²)	O(n)
Worst (reverse sorted)	O(n²)	O(n)
Project structure
.
├── main.py            # bubble_sort implementation + benchmark runner
├── test_cases.py       # sample integer and float lists used for testing
├── pyproject.toml      # project metadata / dependencies
├── uv.lock              # locked dependency versions (uv)
└── .python-version      # pinned Python version
Requirements
Python (version pinned in .python-version)
uv for dependency management (recommended), or plain pip
Usage

Clone the repo and run it directly:

bash
git clone https://github.com/tarhanalaam/Bubble-Sort-Algo.git
cd Bubble-Sort-Algo

# with uv
uv run main.py

# or with plain Python
python main.py

Running main.py sorts the sample integers and floats lists from test_cases.py and prints both the sorted results and how long each run took:

[3, 4, 7, 9, 11, 12, 15, 27, 42, 46, 55, 63, 78, 89, 91, 134, 156, 200, 218, 300]
First run took: 0.00003 seconds
[0.577, 0.693, 1.202, 1.381, 1.414, 1.618, 1.732, 2.236, 2.502, 2.718, 3.14, 3.674, 4.669, 5.291, 6.022, 6.674, 7.389, 8.314, 9.109, 9.81]
Second run took: 0.00002 seconds

(Exact timings will vary by machine.)

Using it in your own code
python
from main import bubble_sort

sorted_list = bubble_sort([5, 3, 8, 1, 9, 2])
print(sorted_list)  # [1, 2, 3, 5, 8, 9]

Because the function is generic over list[object], it works with any type that supports comparison (>), including custom objects that implement __gt__.

License

No license specified yet — add one (e.g. MIT) if you plan to share or accept contributions.