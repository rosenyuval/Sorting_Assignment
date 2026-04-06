import random
import time
import sys
import statistics
import argparse
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
#_________________________________________________________________________________________________________
#Part_A:
def bubble_sort(lst):
    n = len(lst)
    for k in range(n):
        swapped = False
        for i in range(n-k-1):
            if lst[i]>lst[i+1]:
                lst[i+1],lst[i]=lst[i],lst[i+1]
                swapped = True
        if not swapped:
            #The list is allready sorted, no need to complete loop
            break
    return (lst)
#____________________________________________________________________________________________
def quick_sort(lst):
    if len(lst) <= 1:
        return lst

    pivot = random.choice(lst)

    left = []
    middle = []
    right = []

    for x in lst:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
        else:
            middle.append(x)

    return quick_sort(left) + middle + quick_sort(right)
#_____________________________________________________________________________________________

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result
#____________________________________________________________________________________________
#Part_B:
def measure_time(sort_func, arr):
    arr_copy = arr.copy()
    start = time.perf_counter()

    if sort_func == bubble_sort:
        sort_func(arr_copy)
    else:
        sort_func(arr_copy)

    end = time.perf_counter()
    return end - start


sizes = [100, 500, 1000, 1500, 2000, 2500, 3000]
repetitions = 10

bubble_avg = []
bubble_std = []

quick_avg = []
quick_std = []

merge_avg = []
merge_std = []

for size in sizes:
    bubble_times = []
    quick_times = []
    merge_times = []

    for _ in range(repetitions):
        arr = [random.randint(1, 10000) for _ in range(size)]

        bubble_times.append(measure_time(bubble_sort, arr))
        quick_times.append(measure_time(quick_sort, arr))
        merge_times.append(measure_time(merge_sort, arr))

    bubble_avg.append(statistics.mean(bubble_times))
    bubble_std.append(statistics.stdev(bubble_times) if len(bubble_times) > 1 else 0)

    quick_avg.append(statistics.mean(quick_times))
    quick_std.append(statistics.stdev(quick_times) if len(quick_times) > 1 else 0)

    merge_avg.append(statistics.mean(merge_times))
    merge_std.append(statistics.stdev(merge_times) if len(merge_times) > 1 else 0)

    print(f"Size {size}:")
    print(f"Bubble Sort  avg={bubble_avg[-1]:.6f}, std={bubble_std[-1]:.6f}")
    print(f"Quick Sort   avg={quick_avg[-1]:.6f}, std={quick_std[-1]:.6f}")
    print(f"Merge Sort   avg={merge_avg[-1]:.6f}, std={merge_std[-1]:.6f}")
    print()


plt.figure(figsize=(8, 5))

plt.errorbar(sizes, bubble_avg, yerr=bubble_std, marker='o', label='Bubble Sort', capsize=4)
plt.errorbar(sizes, quick_avg, yerr=quick_std, marker='o', label='Quick Sort', capsize=4)
plt.errorbar(sizes, merge_avg, yerr=merge_std, marker='o', label='Merge Sort', capsize=4)
ax = plt.gca()
plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(0.05))
plt.title("Runtime Comparison (Random Arrays)")
plt.xlabel("Array size (n)")
plt.ylabel("Runtime (seconds)")
plt.legend()
plt.grid(True)
plt.ylim(0, 0.4)
plt.savefig("result1.png")
plt.show()

#________________________________________________________________________________________________________________________
#Part_C:

def add_noise(sorted_arr, noise_percent):
    arr = sorted_arr.copy()
    n = len(arr)
    swaps = int(n * noise_percent)

    for _ in range(swaps):
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        arr[i], arr[j] = arr[j], arr[i]

    return arr


noise_levels = [0.05, 0.2]
noise_labels = ["Bubble Sort - 5% noise", "Quick Sort - 5% noise", "Merge Sort - 5% noise",
                "Bubble Sort - 20% noise", "Quick Sort - 20% noise", "Merge Sort - 20% noise"]

results = {}

for noise_percent in noise_levels:
    bubble_avg = []
    quick_avg = []
    merge_avg = []

    for size in sizes:
        bubble_times = []
        quick_times = []
        merge_times = []

        for _ in range(repetitions):
            sorted_arr = list(range(size))
            noisy_arr = add_noise(sorted_arr, noise_percent)

            bubble_times.append(measure_time(bubble_sort, noisy_arr))
            quick_times.append(measure_time(quick_sort, noisy_arr))
            merge_times.append(measure_time(merge_sort, noisy_arr))

        bubble_avg.append(statistics.mean(bubble_times))
        quick_avg.append(statistics.mean(quick_times))
        merge_avg.append(statistics.mean(merge_times))

    results[noise_percent] = {
        "bubble": bubble_avg,
        "quick": quick_avg,
        "merge": merge_avg
    }

plt.figure(figsize=(10, 6))

plt.plot(sizes, results[0.05]["bubble"], marker='o', label='Bubble Sort - 5% noise')
plt.plot(sizes, results[0.05]["quick"], marker='o', label='Quick Sort - 5% noise')
plt.plot(sizes, results[0.05]["merge"], marker='o', label='Merge Sort - 5% noise')

plt.plot(sizes, results[0.2]["bubble"], marker='s', label='Bubble Sort - 20% noise')
plt.plot(sizes, results[0.2]["quick"], marker='s', label='Quick Sort - 20% noise')
plt.plot(sizes, results[0.2]["merge"], marker='s', label='Merge Sort - 20% noise')

plt.title("Runtime Comparison (Sorted Arrays with Noise)")
plt.xlabel("Array size (n)")
plt.ylabel("Runtime (seconds)")
plt.legend()
plt.grid(True)
plt.savefig("result2.png")
plt.show()

# ________________________________________________________________________________________________________________________
# Part_D:
def main():
    sizes = args.s
    repetitions = args.r

    if args.e == 1:
        noise = 0.05
    elif args.e == 2:
        noise = 0.2
    else:
        print("Invalid experiment type")
        return

    for size in sizes:
        print(f"\nRunning size {size}...")

        for alg_id in args.a:
            arr = list(range(size))
            arr = add_noise(arr, noise)

            if alg_id == 1:
                t = measure_time(bubble_sort, arr)
                print(f"Bubble Sort: {t:.6f}")

            elif alg_id == 4:
                t = measure_time(merge_sort, arr)
                print(f"Merge Sort: {t:.6f}")

            elif alg_id == 5:
                t = measure_time(quick_sort, arr)
                print(f"Quick Sort: {t:.6f}")


if len(sys.argv) > 1:
    parser = argparse.ArgumentParser(description="Sorting Algorithm Performance Analysis")

    parser.add_argument('-a', nargs='+', type=int, required=True,
                        help="Which algorithms to compare: 1-Bubble, 2-Selection, 3-Insertion, 4-Merge, 5-Quick")
    parser.add_argument('-s', nargs='+', type=int, required=True,
                        help="Array sizes (e.g., 100 500 3000)")
    parser.add_argument('-e', type=int, required=True,
                        help="Experiment type / noise level: 1 (5% noise), 2 (20% noise)")
    parser.add_argument('-r', type=int, required=True,
                        help="Number of repetitions")

    args = parser.parse_args()

    print("--- Command Line Arguments Received ---")
    print(f"Algorithms IDs: {args.a}")
    print(f"Sizes: {args.s}")
    print(f"Experiment Type: {args.e}")
    print(f"Repetitions: {args.r}")
    print("---------------------------------------")

    main()