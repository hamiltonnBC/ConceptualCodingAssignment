# Interactive Python Functions Lesson Plan (20-minute version)

## Lesson Overview

- **Topic:** Functions in Python
- **Duration:** 20 minutes
- **Target Audience:** Beginner Python students
- **Objective:** To understand the concept of functions and function calls in Python through an interactive, physical representation of a "Happiness Index" calculator.

## Materials Needed

1. Whiteboard or projector to display the Python code
2. 5 tables (or designated areas) labeled with function names
3. Red solo cups (at least 7)
4. Blue paper (for integers)
5. Notecards and tape
6. Markers
7. Large signs for each function table
8. Yellow paper (for strings)

## Classroom Setup

1. Set up 5 tables or designated areas, each representing a function:
   - `calculate_relax_score`
   - `calculate_social_score`
   - `calculate_work_life_balance_score`
   - `calculate_happiness_index`
   - `main`
2. Place a large sign on each table with the function name.
3. Set up the whiteboard or projector with the Python code visible.

## Lesson Plan

### 1. Introduction and Code Walkthrough (5 minutes)

- Briefly explain the concept of functions in programming.
- Display the Python code on the board.
- Quickly explain each function's purpose.

### 2. Interactive Demonstration (12 minutes)

#### Setup (2 minutes)

- Assign roles to students: 
  - Python Interpreter (1 student)
  - Variable Creators (3 students)
  - Function Runners (4 students)
  - Cup Carriers (NA students)  - Python Interpreter will also act as the Cup Carriers

#### Main Execution (10 minutes)

1. **Variable Creation** (2 minutes)
   - Python Interpreter starts at the `main` function.
   - For each variable (`relax_hours`, `social_interactions`, `work_life_balance_rating`):
     - Variable Creator writes the value on blue paper.
     - Places it in a cup and labels the cup with a notecard.

This is to demonstrate that variables hold data, and the data is passed to functions through function calls. It also shows the importance of descriptive variable names. 

2. **Function Calls** (8 minutes)
   - For each function call in `main`:
     - Cup Carrier takes the relevant cup(s) to the function table.
     - Function Runner at the table:
       - Removes the value(s) from the cup(s).
       - Performs the calculation on blue paper.
       - Hands the blue paper with the result to the Cup Carrier.
     - Cup Carrier returns to `main` with the result paper.
     - At `main`, put the result paper in a new cup and label it with the appropriate variable name.

3. **Happiness Index Calculation**
   - Repeat the process for `calculate_happiness_index`.
   - This one, the runner will need to carry three cups to this function.

4. **Conditional Statement Demonstration**
   - At the `main` table, Function Runner reads the happiness index value.
   - They verbally announce which message would be printed based on the value.

### 3. Debrief and Q&A (3 minutes)

- Quickly recap what happened in the demonstration.
- Answer any immediate questions from students.

## Script for Instructor

"Welcome to our quick, interactive lesson on Python functions! We're going to bring code to life by acting out a program that calculates a 'Happiness Index'.

Let's start by looking at our code. [Briefly explain each function]

Now, let's run this program – but we'll be the Python interpreter! 

[Assign roles]

We'll start in our `main` function. First, we need to create our initial variables. 

[Guide Variable Creators to make the initial variables]

Great! Now we'll call our first function. [Name] will take the `relax_hours` cup to the `calculate_relax_score` table.

[Continue guiding students through each function call]

Remember, when a function finishes its calculation, it returns the result on a piece of paper, not in a cup. The cup represents a variable, which we create when we receive the return value back in `main`.

Now that we have our Happiness Index, let's see what message we get. [Name], please tell us which message would be printed based on our Happiness Index value.

Any quick questions about what we just did?"

## Key Points to Emphasize

1. Functions are reusable blocks of code that perform specific tasks.
2. Function calls involve passing data (arguments) and receiving results (return values).
3. Variables store data, while function returns are just values until we store them in variables.
4. The `main` function orchestrates the overall program flow.

---

