# Sequence Alignment (Optimal)
This program takes two string inputs and outputs the optimal alignment for the two strings.

### How the code works

The code takes advantage of recursion and dynamic programming. The code creates a dynamic programming table to determine the most optimal value, then retraces its path using recursion to create the strings with proper gaps. This allows for the code to run as fast and with as little memory space as possible.

### Running the code
To run this program, enter the following into your terminal:
```
python seqalign.py string1 string2
```
where string1 and string2 are the two strings you wish to compare.

### Extended Usage
This program can be integrated into sentence spell checking or even DNA sequence checking. However, that requires small tweaks. Contact me for those tweaks!
