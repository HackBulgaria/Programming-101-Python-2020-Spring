# Credit card validation

Implement a function, called `is_credit_card_valid(number)`, which returns True/False based on the following algorithm:

* Each credit card number must contain odd count of digits.
* We transform the number with the following steps (based on the fact that we start from index 0)
  - All digits, read from right to left, at even positions (index), **remain the same.**
  - Every digit, read from right to left, at odd position is replaced by the result, that is obtained from doubling the given digit.
* After the transformation, we find the sum of all digits in the transformed number.
* The number is valid, if the sum is divisible by 10.

For example: `79927398713` is valid, bacause:

* When we double and replace all digits at odd position we get: `7 (18 = 2 * 9) 9 (4 = 2 * 2) 7 (6 = 2 * 3) 9 (16 = 2 * 8) 7 (2 = 2 * 1) 3`
* The sum of all digits of the new number is 70, which is divisible by 10 => the card number is valid.

More examples:

* `79927398713` is a valid number
* `79927398715` is invalid number
