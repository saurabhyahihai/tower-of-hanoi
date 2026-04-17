# Tower of Hanoi (Simple Demo)

This is a simple demonstration of the Tower of Hanoi problem implemented in Python.  
The goal is to show how recursion works by breaking a problem into smaller subproblems.

## Key Concepts

- Recursion (function calling itself with smaller inputs)
- Base case and recursive breakdown
- Optional visualization of rod states

## Functions Overview

- `generate_moves(n, source, target, auxiliary)`  
  Generates the sequence of moves using recursion.

- `print_moves(moves)`  
  Prints the sequence of moves in order.

- `simulate_moves(moves, num_disks, visualize)`  
  Simulates the movement of disks and optionally displays rod states.

- `print_state(rods)`  
  Displays the current configuration of rods (used for visualization).

- `main()`  
  Controls execution flow and connects all components.

## Run the Code

```bash
python tower_of_hanoi.py
````

To enable visualization, set in the code:

```python
visualize = 1
```

(Default is `visualize = 0`)


## Sample Output

### Case 1: `num_disks = 3`, `visualize = 0`

```
=== Tower of Hanoi ===

Disks: 3

Moves:

Move disk 1 from A to C
Move disk 2 from A to B
Move disk 1 from C to B
Move disk 3 from A to C
Move disk 1 from B to A
Move disk 2 from B to C
Move disk 1 from A to C

Total moves: 7
```
### Case 2: `num_disks = 3`, `visualize = 1`

```
=== Tower of Hanoi ===

Disks: 3

Moves:

Move disk 1 from A to C
Move disk 2 from A to B
Move disk 1 from C to B
Move disk 3 from A to C
Move disk 1 from B to A
Move disk 2 from B to C
Move disk 1 from A to C

Current State:
A: [3, 2, 1]
B: []
C: []
------------------------------
Move disk 1 from A to C

Current State:
A: [3, 2]
B: []
C: [1]
------------------------------
Move disk 2 from A to B

Current State:
A: [3]
B: [2]
C: [1]
------------------------------
Move disk 1 from C to B

Current State:
A: [3]
B: [2, 1]
C: []
------------------------------
Move disk 3 from A to C

Current State:
A: []
B: [2, 1]
C: [3]
------------------------------
Move disk 1 from B to A

Current State:
A: [1]
B: [2]
C: [3]
------------------------------
Move disk 2 from B to C

Current State:
A: [1]
B: []
C: [3, 2]
------------------------------
Move disk 1 from A to C

Current State:
A: []
B: []
C: [3, 2, 1]
------------------------------

Total moves: 7
```

## Notes

This example highlights recursion by repeatedly solving smaller subproblems until a base condition is reached.
Prepared by Saurabh Suman.

