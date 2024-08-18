```markdown
# Interactive Python Data Types Lesson Plan (10-minute version)

## Lesson Overview

- **Topic:** Python Data Types and Basic Operations
- **Duration:** 10 minutes
- **Target Audience:** Beginner Python students (Week 2)
- **Objective:** To understand the difference between integer addition and string concatenation, including with numeric strings.

## Materials Needed

1. Red solo cups (at least 10)
2. Colored paper:
   - Blue for integers
   - Yellow for strings
3. Markers
4. Whiteboard or projector
5. "+" signs printed on cardboard (2-3)

## Classroom Setup

1. Prepare a "variable space" at the front of the classroom.
2. Display the following code on the whiteboard or projector:

```python
num1 = 25
num2 = 26
sum_numbers = num1 + num2

str1 = "25"
str2 = "26"
concat_strings = str1 + str2

firstName = "John"
lastName = "Doe"
fullName = firstName + " " + lastName

print(sum_numbers)
print(concat_strings)
print(fullName)
```

## Lesson Plan

### 1. Introduction (1 minute)

- Briefly explain we'll be looking at how addition works differently for numbers and strings.

### 2. Interactive Demonstration (8 minutes)

#### Setup (1 minute)
- Assign roles to students:
  - Python Interpreter (teacher or TA)
  - Variable Creators (4 students)
  - Operation Performers (2 students)

#### Main Execution (7 minutes)

1. **Integer Addition** (2 minutes)
   - Create variables `num1` and `num2` using blue paper in cups.
   - Operation Performer adds the numbers, puts result in `sum_numbers` cup.
   - Emphasize that 25 + 26 = 51 for integers.

2. **String Concatenation with Numeric Strings** (2 minutes)
   - Create variables `str1` and `str2` using yellow paper in cups.
   - Operation Performer concatenates the strings, puts result in `concat_strings` cup.
   - Emphasize that "25" + "26" = "2526" for strings.

3. **Name Concatenation** (2 minutes)
   - Create `firstName` and `lastName` variables using yellow paper in cups.
   - Operation Performer concatenates names with a space, puts result in `fullName` cup.
   - Show how spaces are included in string concatenation.

4. **Printing Results** (1 minute)
   - For each print statement:
     - Show the contents of the respective cup.
     - Write the output on the board.

### 3. Quick Recap and Q&A (1 minute)

- Recap the difference between adding integers and concatenating strings.
- Answer any immediate questions from students.

## Key Points to Emphasize

1. Variables can hold different types of data (integers vs strings).
2. Adding integers produces a sum (e.g., 25 + 26 = 51).
3. Adding strings concatenates them (e.g., "25" + "26" = "2526").
4. String concatenation works the same for numeric strings and text strings.
5. Spaces in strings are important for readability in concatenation.

## Sample Script

"Welcome to our quick lesson on how Python handles addition with different data types!

[Guide students through variable creation]

Watch what happens when we add numbers as integers...
[Demonstrate 25 + 26 = 51]

Now, let's see what happens with the same numbers as strings...
[Demonstrate "25" + "26" = "2526"]

See the difference? Python treats the '+' differently for numbers and strings.

Finally, let's combine names...
[Demonstrate "John" + " " + "Doe" = "John Doe"]

Notice how we included a space to make the full name readable.

Let's check our outputs...
[Show print outputs]

Any quick questions about what we just saw?"

---

This 10-minute lesson demonstrates the crucial difference between integer addition and string concatenation in Python, including the behavior with numeric strings.
```