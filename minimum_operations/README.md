# Minimum Operations

## Task

Given a number `n`, calculate the fewest number of operations needed to result in exactly `n` H characters in a text file, starting from a single `H`.

## Operations

- **Copy All** – copies all current characters
- **Paste** – pastes the copied characters

## Prototype

```python
def minOperations(n)
```

- Returns an integer
- If `n` is impossible to achieve, return `0`

## Example

```
n = 9
H => Copy All => Paste => HH => Paste => HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH
Number of operations: 6
```
