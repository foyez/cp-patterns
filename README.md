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
