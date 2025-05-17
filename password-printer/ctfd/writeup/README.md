# Password printer
Category: Pwn
Points: 400
Provided: password-printer 

Challenge Description:
Now we show you your password when you enter it, just to make sure you got it correct!

## Solution
 * This almost certainly requires a decompiler.
 * It is intended to do some tinkering with format strings (%p specifically) with the input and leak addresses on the stack
 * Easiest to tinker with the thing locally, then use the right offset ([solve.py](./solve.py) just does it)
 * Put that data into cyberchef, swap the endianness, and convert to ASCII. 

## Notes
 * Still meant to be somewhat easy, Honestly you can just brute force this if you guess the vuln