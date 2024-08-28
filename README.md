========================================
Summary: Finding Odd Numbers in a List
========================================

Objective:
----------
To identify and extract all odd numbers from a given list of integers.

Code Explanation:
-----------------
1. List Definition:
   - numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
   - This list contains integers ranging from 1 to 10.

2. Filtering Odd Numbers:
   - even_numbers = list(filter(lambda x: x % 2 != 0, numbers))
   - The filter function is used to process the numbers list.
   - lambda x: x % 2 != 0 is an anonymous function that checks if a number is odd (i.e., not evenly divisible by 2).
   - filter applies this lambda function to each element of the list.
   - Only elements for which the lambda function returns True (odd numbers) are included in the resulting filter object.

3. Conversion to List:
   - list(...) converts the filter object into a list of odd numbers.

4. Output:
   - print(even_numbers)
   - This prints the list of odd numbers extracted from the original list.

Example Output:
---------------
[1, 3, 5, 7, 9]

Summary:
--------
The provided code filters out odd numbers from a list of integers and prints them. It uses the filter function in conjunction with a lambda expression to achieve this.

========================================
