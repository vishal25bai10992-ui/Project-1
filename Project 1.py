# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 01:18:20 2025

@author: Vishal andhale
"""

n = int(input("Input a value of n: "))

l = int(input("Enter the digit position you wish to find (l): "))

combined_string = ""
for i in range(1, n + 1):
    combined_string += str(i)


if l <= 0 or l > len(combined_string):
    print(f"Error: The position {l} is out of bounds for the generated sequence (1 to {n}).")
else:
    
    target_digit = combined_string[l - 1]

    cumulative_length = 0
    source_number = -1 

    for i in range(1, n + 1):
        current_length = len(str(i))

        # Check if the l-th digit falls within the current number's digits
        # Example: If cumulative_length is 9 and current_length is 2 (for number 10)
        # the digits cover positions l=10 and l=11.
        if cumulative_length < l <= cumulative_length + current_length:
            source_number = i
            break
        
        # Update the length for the next iteration
        cumulative_length += current_length

    # --- Output ---
    # required final outputs are calculated.
    print(f"\nThe requested digit is at index {l-1} of the sequence.")
    print(f"The digit at position {l} is: **{target_digit}**")
    print(f"The {l}th digit is from the number **{source_number}**")