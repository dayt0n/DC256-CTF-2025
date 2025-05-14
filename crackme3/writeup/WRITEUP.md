# Crackme 3
Category: Reversing
Points: 150(?)
Provided: crackme3

Challenge Description:
My secrets should be super safe and secure now!

## Solution

 * This almost certainly requires a decompiler.
 * After opening, the sovler will see something much similar to the last one, except the values are gibberish in the array now.
 * If you follow the flow, you will see that each value of the array is XOR operation'd with 0x64, an arbitrary number.
 * All you have to do is retrieve the bytes in the above array, and then XOR each with 0x64.


## Notes

 * Still meant to be somewhat easy, but not too trivial. Requires at least opening in a debugger or using GDB and poking around
 * You can also use GDB, break at a certain point, then just print the flag

## Hints

 * IDA Free or GDB will be useful, anything to explore the code
