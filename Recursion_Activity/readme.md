### 1. What is the base case of your reverse function?

If the length of the parameter is equals to one, the value will be returned

### 2. What is the base case of your is_palindrome function?

If the length of the parameter is equal to one, it will return True, since a single character is considered a palindrome.

### 3. What would happen if you removed the base case? (You can test it!)

The function would continue executing recursively without stopping. Eventually, the terminal would terminate the program after it reaches the maximum recursion limit.
