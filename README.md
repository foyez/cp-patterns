# Problem Solving Patterns

## Common time complexities

<details>
<summary>View contents</summary>

Let n be the main variable in the problem.

- If n ≤ 12, the time complexity can be O(n!).
- If n ≤ 25, the time complexity can be O(2n).
- If n ≤ 100, the time complexity can be O(n4).
- If n ≤ 500, the time complexity can be O(n3).
- If n ≤ 104, the time complexity can be O(n2).
- If n ≤ 106, the time complexity can be O(n log n).
- If n ≤ 108, the time complexity can be O(n).
- If n > 108, the time complexity can be O(log n) or O(1).

**Examples of each common time complexity**

- O(n!) [Factorial time]: Permutations of 1 ... n
- O(2n) [Exponential time]: Exhaust all subsets of an array of size n
- O(n3) [Cubic time]: Exhaust all triangles with side length less than n
- O(n2) [Quadratic time]: Slow comparison-based sorting (eg. Bubble Sort, Insertion Sort, Selection Sort)
- O(n log n) [Linearithmic time]: Fast comparison-based sorting (eg. Merge Sort)
- O(n) [Linear time]: Linear Search (Finding maximum/minimum element in a 1D array), Counting Sort
- O(log n) [Logarithmic time]: Binary Search, finding GCD (Greatest Common Divisor) using Euclidean Algorithm
- O(1) [Constant time]: Calculation (eg. Solving linear equations in one unknown)

</details>

## Problem Solving Tips

<details>
<summary>View contents</summary>

If input array is sorted then
- Binary search
- Two pointers

If asked for all permutations/subsets then
- Backtracking

If given a tree then
- DFS
- BFS

If given a graph then
- DFS
- BFS

If given a linked list then
- Two pointers

If recursion is banned then
- Stack

If must solve in-place then
- Swap corresponding values
- Store one or more different values in the same pointer

If asked for maximum/minimum subarray/subset/options then
- Dynamic programming

If asked for top/least K items then
- Heap
- QuickSelect

If asked for common strings then
- Map
- Trie

Else
- Map/Set for O(1) time & O(n) space
- Sort input for O(nlogn) time and O(1) space

source: [Sean Prashad's Leetcode Patterns](https://seanprashad.com/leetcode-patterns/)

</details>

## Arithmetic

1. Digit to sum (input: 123, output: 6)

<details>
<summary>View solutions</summary>

**Solution 1:**
  
```js
function dititToSum(n) {
  let sum = 0;
  
  for (; n; n = Math.floor(n / 10)) {
    sum += n % 10;
  }
  
  return sum
}
  
digitToSum(123) // 6
```
  
</details>

2. Lenght of a number

<details>
<summary>View solutions</summary>

**Solution 1**

`javascript`
```js
function digitToLength(num) {
  if (num === 0) {
    return 1
  }
  return Math.floor(Math.log10(num)) + 1
}
```

`python`
```py
import math
def digitToLength(num):
  if num == 0:
    return 1
  return math.floor(math.log10(num)) + 1
```

</details>

3. Reverse a number (input: -123, output: -321)

<details>
<summary>View solutions</summary>

**Solution 1**

```js
function reverse(num) {
  let r = 0
    
  for(let i = Math.abs(num); i != 0;) {
    r = r * 10 ;
    r = r + i % 10;
    i = Math.floor(i/10);
  }
    
  return num < 0 ? -r : r
};

reverse(-123) // -321
```

</details>


4. Big modular


<details>
<summary>View solutions</summary>

**Solution 1**

```js
// a ^ b % M

function bigMod (a, b, M) {
    if (b === 0) return 1 % M
    
    let x = bigMod(a, Math.floor(b / 2), M)
    console.log({x1:x})
    x = (x * x) % M
    console.log({x2:x})
    if (b % 2 === 1) x = (x * a) % M
    console.log({x3:x})
    return x
}

console.log(bigMod(2, 5, 7)) // 2 ^ 5 % 7 = 4
console.log(bigMod(2, 100, 7)) // 2 ^ 5 % 7 = 2
```

</details>

## Common Patterns

### 1. Sliding window

<details>
<summary>View contents</summary>

Identify sliding window problems:

1. Input is array/string
2. subarray/substring -> largest/minimum/maximum
3. Given k window size or have to calculate window size

2 Types of sliding windows:

1. Fixed Size Window

<details>
<summary>View codes</summary>

```py
# Find maximum sum sub array of k size

def maxPrice(arr, k):
  total = sum(arr[:k])
  max_price = total
  
  for i in range(len(arr) - k):
    total -= arr[i]
    total += arr[k+i]
    max_price = max(total, max_price)
    
  return max_price
  
maxPrice([1,4,5,6], 3) # 15
```

</details>

2. Variable Size Window

</details>

## Array

1. Define a 2D array

<details>
<summary>View solutions</summary>

```js
const row = 5
const col = 4
const val = 0
const myGrid = [...Array(row)].map(() => Array(col).fill(val));
```

</details>

2. Prefix Sum of Matrix (Or 2D Array)

<details>
<summary>View solutions</summary>

```js
// Formula
psa[i][j] = psa[i-1][j] + psa[i][j-1] -  psa[i-1][j-1] + a[i][j]
```

</details>

## Linked List

1. Find middle node (Input: head = [1,2,3,4] Output: [3,4])

<details>
<summary>View solutions</summary>

**Solution 1**

```js
function getMiddleNode (head) {
    let fast = head
    let slow = head
    
    while(fast !== null && fast.next !== null) {
        fast = fast.next.next
        slow = slow.next
    }
    
    return slow
}
```

</details>

2. Detect a Linked List Cycle

<details>
<summary>View solutions</summary>

**Solution 1**

```js
function detectLLCycle (head) {
    let fast = head
    let slow = head
    
    while(fast !== null && fast.next !== null && slow !== fast) {
        fast = fast.next.next
        slow = slow.next
    }
    
    if(slow === fast) return true
    return false
}
```

</details>

3. Reverse a linked list

<details>
<summary>View solutions</summary>

**Solution 1**

<img width="1668" alt="image" src="https://user-images.githubusercontent.com/11992095/194465735-208f24d0-3ed0-4c86-8d1c-ecd84a471d07.png">


```js
function reverseLL (head) {
    let curr = head
    let prev = null
    
    while(curr !== null) {
        let next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    }
    
    return prev
}
```

</details>
