<div align="center">
  <img width="800" height="150" alt="2_Crystall_Ball_Problem" src="https://github.com/user-attachments/assets/8078f960-9a87-45a8-80ed-9bd59bb79474" />
</div>

# Two Crystal Ball Problem

A Python implementation and mathematical analysis of the classic Two Crystal
Ball Problem, demonstrating how to achieve O(√n) time complexity through
optimal jump sizing.

## Problem Statement

Given 2 identical crystal balls and a building with `n` floors, find the
lowest floor from which dropping a ball will cause it to break. The balls do
not weaken from surviving drops. The floors can be represented as a sorted
list of Booleans, where `False` = survives and `True` = breaks.

## Algorithm

The optimal solution uses a jump size of `√n`:

1. Jump `√n` floors at a time using the first ball until it breaks
2. Return to the last safe floor
3. Walk up one floor at a time using the second ball until it breaks
4. Return the break floor index, or `-1` if no break floor exists

## Time Complexity

| Approach        | Time Complexity | 100-floor WCS | 10,000-floor WCS |
| --------------- | --------------- | ------------- | ---------------- |
| Linear search   | O(n)            | 100           | 10,000           |
| Halfway drop    | O(n)            | 50            | 5,000            |
| n/10 jumps      | O(n)            | 20            | 1,010            |
| **√n jumps**    | **O(√n)**       | **20**        | **200**          |

## Why √n is Optimal

Expressing jump size as n^a, the worst-case steps can be written as:

WCS(a) = n^a + n^(1-a)

Differentiating with respect to `a` and setting equal to zero gives `a = 1/2`,
i.e. a jump size of √n. Any other value of `a` yields higher time complexity.

See [ANALYSIS.md](ANALYSIS.md) for the full mathematical writeup and
[PROOF.md](PROOF.md) for the complete calculus derivation.

## Project Structure

```text
.
├── crystalballs.py              # Core algorithm implementation
├── test_two_crystal_ball.py     # Tests for the search algorithm
├── test_step_counter.py         # Tests for step counting / WCS verification
├── ANALYSIS.md                  # Full problem analysis
└── PROOF.md                     # Mathematical proof
```

## Installation

No external dependencies are required. Python 3.x and the standard library
are sufficient.

```bash
git clone https://github.com/your-username/two-crystal-ball-problem.git
cd two-crystal-ball-problem
```

## Usage

```python
from crystalballs import two_crystal_ball_root2

floors = [False] * 24 + [True] * 76  # Break floor is floor 24
break_floor = two_crystal_ball_root2(floors)
print(f"Break floor: {break_floor}")  # Output: Break floor: 24
```

## Running Tests

```bash
python -m pytest
```

Or with the built-in unittest runner:

```bash
python -m unittest discover
```

## Functions

### `two_crystal_ball_root2(floors: list[bool]) -> int`

Finds the lowest break floor index.

- **Input:** A sorted list of booleans representing floors
- **Output:** The index of the lowest breaking floor, or `-1` if none exists

### `step_counter(floors: list[bool]) -> int`

Same algorithm as above, but returns the number of steps taken rather than
the break floor index. Useful for verifying worst-case scenario analysis.

## License

MIT
# Two Crystal Ball Problem

A Python implementation and mathematical analysis of the classic Two Crystal
Ball Problem, demonstrating how to achieve O(√n) time complexity through
optimal jump sizing.

## Problem Statement

Given 2 identical crystal balls and a building with `n` floors, find the
lowest floor from which dropping a ball will cause it to break. The balls do
not weaken from surviving drops. The floors can be represented as a sorted
list of Booleans, where `False` = survives and `True` = breaks.

## Algorithm

The optimal solution uses a jump size of `√n`:

1. Jump `√n` floors at a time using the first ball until it breaks
2. Return to the last safe floor
3. Walk up one floor at a time using the second ball until it breaks
4. Return the break floor index, or `-1` if no break floor exists

## Time Complexity

| Approach        | Time Complexity | 100-floor WCS | 10,000-floor WCS |
| --------------- | --------------- | ------------- | ---------------- |
| Linear search   | O(n)            | 100           | 10,000           |
| Halfway drop    | O(n)            | 50            | 5,000            |
| n/10 jumps      | O(n)            | 20            | 1,010            |
| **√n jumps**    | **O(√n)**       | **20**        | **200**          |

## Why √n is Optimal

Expressing jump size as n^a, the worst-case steps can be written as:

WCS(a) = n^a + n^(1-a)

Differentiating with respect to `a` and setting equal to zero gives `a = 1/2`,
i.e. a jump size of √n. Any other value of `a` yields higher time complexity.

See [ANALYSIS.md](ANALYSIS.md) for the full mathematical writeup and
[PROOF.md](PROOF.md) for the complete calculus derivation.

## Project Structure

```text
.
├── crystalballs.py              # Core algorithm implementation
├── test_two_crystal_ball.py     # Tests for the search algorithm
├── test_step_counter.py         # Tests for step counting / WCS verification
├── ANALYSIS.md                  # Full problem analysis
└── PROOF.md                     # Mathematical proof
```

## Installation

No external dependencies are required. Python 3.x and the standard library
are sufficient.

```bash
git clone https://github.com/your-username/two-crystal-ball-problem.git
cd two-crystal-ball-problem
```

## Usage

```python
from crystalballs import two_crystal_ball_root2

floors = [False] * 24 + [True] * 76  # Break floor is floor 24
break_floor = two_crystal_ball_root2(floors)
print(f"Break floor: {break_floor}")  # Output: Break floor: 24
```

## Running Tests

```bash
python -m pytest
```

Or with the built-in unittest runner:

```bash
python -m unittest discover
```

## Functions

### `two_crystal_ball_root2(floors: list[bool]) -> int`

Finds the lowest break floor index.

- **Input:** A sorted list of booleans representing floors
- **Output:** The index of the lowest breaking floor, or `-1` if none exists

### `step_counter(floors: list[bool]) -> int`

Same algorithm as above, but returns the number of steps taken rather than
the break floor index. Useful for verifying worst-case scenario analysis.

## License

MIT
