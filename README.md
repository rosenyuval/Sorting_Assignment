**Students names:**
Elgar Elezra 212573059, Yuval Rosen 322867805

**Selected algorithms:**
1. Bubble sort
2. Quick sor
3. merge sort 

**Analysis of Results:**

**1. Comparative Experiment - Random Arrays:**

In this experiment, we evaluated the running times of Bubble Sort, Quick Sort, and Merge Sort using arrays filled with random integers. We tested various array sizes, ranging from 100 to 3,000 elements, to observe how the execution time increases as the input size grows. To ensure statistical reliability, each test was repeated 20 times, and the results below represent the average running time with standard deviation error bars. 

![result1.png](result1.png)

The results clearly illustrate the fundamental differences in algorithmic growth rates:Bubble Sort (Blue): Shows a steep quadratic growth curve, consistent with its O(n^2) theoretical complexity. As the array size increases, the runtime grows significantly faster than the other algorithms.Quick Sort & Merge Sort (Orange/Green): Both algorithms exhibit a much more efficient linear-logarithmic growth O(n log n).
The plot confirms that for random datasets, O(n log n) algorithms are significantly more scalable and efficient than O(n^2) algorithms as the input size increases. 
 
**Methodology Note - Scalability and the 10^6 Input Constraint:**

 Per the experiment guidelines, we chose to limit our practical tests to 3,000 elements rather than 10^6 (one million).
 

Why Bubble Sort is Unsuitable for Large Inputs: CPU Inefficiency: Bubble Sort performs a massive number of redundant adjacent swaps (n^2/2 on average), which leads to high CPU utilization for very little progress per operation. Lack of "Divide and Conquer": Unlike Quick or Merge Sort, Bubble Sort does not break the problem into smaller sub-problems, making it incapable of handling modern large-scale data requirements. Practical Constraint: In real-world applications and this experiment, a runtime of several hours for a single sort is considered a failure in performance, especially when O(n \log n) alternatives finish the same task in less than a second.

Due to these extreme runtime projections, we limited our experimental arrays to a reasonable size that the computer could process efficiently. This range (n <=  3,000) still clearly illustrates the massive performance gap between the algorithms while remaining within practical execution limits.

**2. Experiment with Nearly Sorted Arrays  - Noise**

In this phase, we evaluated the algorithms using "Nearly Sorted" arrays with two noise levels: 5% and 20% random swaps . We aimed to determine how existing order in the data affects performance compared to the random arrays in Part B 

![result2.png](result2.png)

Noise Level Comparison (5% vs. 20%): We observed that increasing noise directly impacts Bubble Sort, causing its runtime to rise as more swaps are required. In contrast, Quick Sort and Merge Sort remained extremely stable, showing that their O(n log n) efficiency is robust against varying levels of disorder. 

Comparison to Part B: Runtimes for all algorithms were lower than in the random experiment. Bubble Sort showed the most significant improvement; because the arrays were "mostly sorted," the number of necessary operations decreased drastically compared to the fully unsorted inputs in Part B. Despite the improvements in nearly sorted scenarios, the efficiency gap remains clear: the O(n log n) algorithms consistently outperform the O(n^2) Bubble Sort as n increases 

.Conclusion: Our results confirm that partial order reduces execution time, especially for exchange-based algorithms like Bubble Sort. However, for large-scale data, the structural efficiency of Quick and Merge Sort remains superior regardless of noise levels.

