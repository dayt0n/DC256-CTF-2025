# Password Checker
Category: Pwn
Points: 300
Provided: password-checker 

Challenge Description:
We made a simple password checker tool. There might be other functionality in there too...

## Solution
 * This almost certainly requires a decompiler.
 * It is intended to do a simple BOF into a specific memory location that triggers a print flag
 * Easiest to tinker with the thing locally, then use the right offset, use [solve.py](./solve.py).

## Notes

 * Still meant to be somewhat easy, but not too trivial. Requires at least opening in a debugger or using GDB and poking around
 * You can also use GDB, break at a certain point, then just print the flag

## Hints

 * IDA Free or GDB will be useful, anything to explore the code
