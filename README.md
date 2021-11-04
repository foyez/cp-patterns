# Problem Solving Patterns

## Arithmetic

1. Digit to sum

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
