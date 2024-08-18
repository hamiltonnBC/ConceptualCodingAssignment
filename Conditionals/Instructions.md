```markdown
# Interactive Python Conditionals Lesson Plan (10-minute version)

## Lesson Overview

- **Topic:** Python Conditional Statements (if, else, elif)
- **Duration:** 10 minutes
- **Target Audience:** Beginner Python students
- **Objective:** To understand and demonstrate how if, else, and elif conditionals work in Python and when to use each structure.

## Materials Needed

1. Whiteboard or projector
2. Different colored markers or chalk
3. Three signs: "IF", "ELIF", "ELSE"

## Lesson Plan

### 1. Introduction to Conditionals (2 minutes)

- Explain that conditionals are used to make decisions in code.
- Write on board: "Conditionals help our program choose what to do based on certain conditions."

### 2. If-Else Explanation and Example (3 minutes)

- Write the following code on the board:

```python
age = 18
if age >= 18:
    print("You can vote!")
else:
    print("You're too young to vote.")
```

- Explain:
  - `if` checks a condition
  - If true, it executes the indented code below it
  - `else` provides an alternative if the condition is false
- Demonstrate with a student volunteer:
  - Student holds a number representing age
  - They stand by "IF" sign if ≥ 18, "ELSE" sign if < 18

### 3. Introducing elif (3 minutes)

- Add to the previous example on the board:

```python
age = 16
if age >= 18:
    print("You can vote!")
elif age >= 16:
    print("You can't vote, but you can learn to drive.")
else:
    print("You're too young to vote or drive.")
```

- Explain:
  - `elif` stands for "else if"
  - It allows checking multiple conditions in order
  - Only one block of code will execute

- Quick activity:
  - Three students hold different ages (e.g., 20, 16, 14)
  - They stand by "IF", "ELIF", or "ELSE" signs based on their age

### 4. When to Use Different Structures (2 minutes)

- Explain use cases:
  1. Single `if`: When you only need to check one condition
     Example: `if is_raining: bring_umbrella()`
  
  2. `if-else`: When you have two mutually exclusive options
     Example: `if score >= 60: print("Pass") else: print("Fail")`
  
  3. `if-elif-else`: When you have multiple related conditions
     Example: Grading system (A, B, C, D, F)
  
  4. Multiple `if` statements: When conditions are independent
     Example:
     ```python
     if is_raining: bring_umbrella()
     if is_cold: wear_jacket()
     if is_sunny: wear_sunglasses()
     ```

### 5. Quick Q&A and Recap (1 minute)

- Recap: "Conditionals let our code make decisions. `if` checks a condition, `elif` checks additional conditions if needed, and `else` provides a fallback option."

## Key Points to Emphasize

1. Conditionals allow programs to make decisions based on certain conditions.
2. `if` statements check if a condition is true.
3. `else` provides an alternative when the `if` condition is false.
4. `elif` allows checking multiple conditions in a sequence.
5. Choose the appropriate structure based on your specific decision-making needs.

---

This 10-minute lesson provides a concise introduction to Python conditional statements, explaining if, else, and elif, along with guidelines on when to use each structure.
```