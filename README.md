# Recursive Programming With Python

Recursive programming in computer science is a technique where a function calls itself in order to solve a problem. It serves a similar purpose as loops, though they have different structures and use cases.

## Structure of a recursive function
In recursion, the function calls itself with modified arguments to solve the smallest amount of the problem until it reaches the base case.

1. Base case

A base case is a statement with tells the function not to call itself again but return something else. These base cases are there to prevent infinte call to functions. NB: You can have more than one base case.

2. Recursive case

With recursive case this is when the function calls itself with a modified argument to solve the smallest amount of the problem.

## Example of a recursive function
Print the numbers from n to 0 using recursion.

```{python3}
def recursive_deduction(n: int) -> int:
    print(n)
    if n == 0:
        return
    return recursive_deduction(n-1)
```
Breakdown of example

Here we are printing numbers from n to 0.

1. we print `n` to the screen
2. we check if `n` is equal to `0`
3. if `step 2` results to `true` we return nothing.
4. else we call our function and modify the argument by subtracting `1` from `n`
5. we repeat from `step 1` through to `step 4` until our `n` becomes `0` then we stop our function.

So here our base case is to check if `n == 0` then stop the function call. Also our recursive case is to call the function but this time modify the argument by subtracting `1` from it.
#
# About Author
- [LinkedIn](./https://www.linkedin.com/in/desmond-asamoah-15b61a1b7/)

Author - Desmond Asiedu Asamoah