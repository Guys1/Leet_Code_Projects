class Solution:
    def countDigitOne(self, n: int) -> int:
        sum_of_ones = 0
        digit_place = 1
        remaining = n

        while remaining > 0:
            current_digit = remaining % 10
            remaining //= 10

            # Count the occurrences contributed by the remaining part of the number
            sum_of_ones += (remaining * digit_place)

            if current_digit == 1:
                # If the current digit is 1, count the occurrences contributed by the current digit and the remaining number
                sum_of_ones += (n % digit_place) + 1
            elif current_digit > 1:
                # If the current digit is greater than 1, add the maximum possible occurrences at this digit place
                sum_of_ones += digit_place

            digit_place *= 10

        return sum_of_ones