# Problem Solving Patterns

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

2. Reverse a number (input: -123, output: -321)

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


3. Big modular


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

```
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

```js
function reverseLL (head) {
    let curr = head
    let prev = null
    let next = null
    
    while(curr !== null) {
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    }
    
    return prev
}
```

</details>
