# 🐍 Python Learning Journey

# 🟢 Part 1 — Programming & Python Foundations

## Batch 2 — Your First Python Programs 💻

> *"Syntax is not the destination. It's the language you use to express your thinking."*

---

# 🥋 Welcome Back, Apprentice

You've already learned how to think through a programming problem.

Now we're going to give that thinking a language.

That language is Python.

In the last batch, you learned:

```text
Problem
   ↓
Understand it
   ↓
Break it into steps
   ↓
Input → Process → Output
   ↓
Algorithm
```

Now we're adding:

```text
Algorithm
   ↓
Python syntax
   ↓
Executable program
```

This is where things start getting interesting. 🐍

By the end of this batch, you won't merely recognize Python code.

You'll start **writing it naturally**.

---

# 🗺️ Where You Are

```text
🐍 Python Learning Journey

Phase 1 — Python Fluency

└── Part 1 — Programming & Python Foundations
    │
    ├── 🧠 Batch 1 — Thinking Like a Programmer       ✅
    │
    ├── 💻 Batch 2 — Your First Python Programs        ← YOU ARE HERE
    │
    ├── 📦 Batch 3 — Variables & Data
    ├── 🔢 Batch 4 — Operators & Expressions
    ├── 🗣️ Batch 5 — Input & Output
    ├── 🔤 Batch 6 — Strings
    ├── 🤔 Batch 7 — Conditionals
    └── 🔁 Batch 8 — Loops
             │
             ▼
          🏆 PART 1
          BOSS FIGHT
```

> [!success] Batch Goal
> Become comfortable reading and writing basic Python statements without needing to think about every character.

---

# 🎯 Learning Objectives

By the end of this batch, you should be able to:

* Run a Python program
* Understand Python source files
* Write basic Python statements
* Use `print()`
* Work with strings and numbers at a basic level
* Understand comments
* Understand indentation
* Use Python's basic syntax conventions
* Write multiple statements in a program
* Read simple Python code
* Predict basic output
* Identify common beginner syntax mistakes
* Build small programs from simple instructions

---

# 🧠 THE BIG IDEA

Python code is simply a way of expressing instructions.

For example:

```python
print("Welcome")
```

This is an instruction to display some text.

Multiple instructions can be combined:

```python
print("Welcome")
print("Player registration")
print("Good luck!")
```

Python executes them in order.

```text
print("Welcome")
       ↓
print("Player registration")
       ↓
print("Good luck!")
```

This is still the sequential execution you learned in Batch 1.

We're simply learning how to express it using Python.

---

# 🐍 Python Files

Python programs are commonly stored in files ending with:

```text
.py
```

For example:

```text
academy.py
wallet.py
store.py
main.py
```

A file such as:

```text
academy.py
```

can contain:

```python
print("Welcome to the Academy")
print("Training begins today")
```

When Python runs the file, it executes the instructions.

---

# ▶️ Running Python

Depending on your environment, you might run:

```text
python academy.py
```

or:

```text
python3 academy.py
```

The exact command can depend on your operating system and Python installation.

For this journey, the important mental model is:

```text
academy.py
    ↓
Python
    ↓
Execute instructions
    ↓
Output
```

---

# 🧪 Practice 1 — First Program

Create a file called:

```text
hello.py
```

Write a program that displays:

```text
Hello, Python!
I am beginning my Python journey.
```

### Requirements

* Use `print()`
* Use two separate statements
* Run the program
* Confirm the output

---

# 🧠 `print()`

Let's look at the structure:

```python
print("Hello")
```

There are several pieces here.

```text
print
  ↓
function name

(
  ↓
opening parenthesis

"Hello"
  ↓
argument

)
  ↓
closing parenthesis
```

Don't worry about the word **function** too much yet.

We'll study functions properly later.

For now:

> `print()` is a built-in Python function used to display information.

---

# 🔤 Strings

Text in Python is represented using strings.

For example:

```python
"Hello"
```

```python
"Football Academy"
```

```python
"Python is fun"
```

Strings can use single quotes:

```python
'Hello'
```

or double quotes:

```python
"Hello"
```

Both are valid.

---

# 🧠 Single vs Double Quotes

These are both strings:

```python
"Python"
```

```python
'Python'
```

For ordinary text, they're functionally equivalent.

Pick a consistent style.

For this course, we'll generally use:

```python
"double quotes"
```

unless single quotes make the code clearer.

---

# 🧪 Practice 2 — String Printer

# 🐍 Python Learning Journey

# 🟢 Part 1 — Programming & Python Foundations

## Batch 2 — Your First Python Programs 💻

> *"Syntax is not the destination. It's the language you use to express your thinking."*

---

# 🥋 Welcome Back, Apprentice

You've already learned how to think through a programming problem.

Now we're going to give that thinking a language.

That language is Python.

In the last batch, you learned:

```text
Problem
   ↓
Understand it
   ↓
Break it into steps
   ↓
Input → Process → Output
   ↓
Algorithm
```

Now we're adding:

```text
Algorithm
   ↓
Python syntax
   ↓
Executable program
```

This is where things start getting interesting. 🐍

By the end of this batch, you won't merely recognize Python code.

You'll start **writing it naturally**.

---

# 🗺️ Where You Are

```text
🐍 Python Learning Journey

Phase 1 — Python Fluency

└── Part 1 — Programming & Python Foundations
    │
    ├── 🧠 Batch 1 — Thinking Like a Programmer       ✅
    │
    ├── 💻 Batch 2 — Your First Python Programs        ← YOU ARE HERE
    │
    ├── 📦 Batch 3 — Variables & Data
    ├── 🔢 Batch 4 — Operators & Expressions
    ├── 🗣️ Batch 5 — Input & Output
    ├── 🔤 Batch 6 — Strings
    ├── 🤔 Batch 7 — Conditionals
    └── 🔁 Batch 8 — Loops
             │
             ▼
          🏆 PART 1
          BOSS FIGHT
```

> [!success] Batch Goal
> Become comfortable reading and writing basic Python statements without needing to think about every character.

---

# 🎯 Learning Objectives

By the end of this batch, you should be able to:

* Run a Python program
* Understand Python source files
* Write basic Python statements
* Use `print()`
* Work with strings and numbers at a basic level
* Understand comments
* Understand indentation
* Use Python's basic syntax conventions
* Write multiple statements in a program
* Read simple Python code
* Predict basic output
* Identify common beginner syntax mistakes
* Build small programs from simple instructions

---

# 🧠 THE BIG IDEA

Python code is simply a way of expressing instructions.

For example:

```python
print("Welcome")
```

This is an instruction to display some text.

Multiple instructions can be combined:

```python
print("Welcome")
print("Player registration")
print("Good luck!")
```

Python executes them in order.

```text
print("Welcome")
       ↓
print("Player registration")
       ↓
print("Good luck!")
```

This is still the sequential execution you learned in Batch 1.

We're simply learning how to express it using Python.

---

# 🐍 Python Files

Python programs are commonly stored in files ending with:

```text
.py
```

For example:

```text
academy.py
wallet.py
store.py
main.py
```

A file such as:

```text
academy.py
```

can contain:

```python
print("Welcome to the Academy")
print("Training begins today")
```

When Python runs the file, it executes the instructions.

---

# ▶️ Running Python

Depending on your environment, you might run:

```text
python academy.py
```

or:

```text
python3 academy.py
```

The exact command can depend on your operating system and Python installation.

For this journey, the important mental model is:

```text
academy.py
    ↓
Python
    ↓
Execute instructions
    ↓
Output
```

---

# 🧪 Practice 1 — First Program

Create a file called:

```text
hello.py
```

Write a program that displays:

```text
Hello, Python!
I am beginning my Python journey.
```

### Requirements

* Use `print()`
* Use two separate statements
* Run the program
* Confirm the output

---

# 🧠 `print()`

Let's look at the structure:

```python
print("Hello")
```

There are several pieces here.

```text
print
  ↓
function name

(
  ↓
opening parenthesis

"Hello"
  ↓
argument

)
  ↓
closing parenthesis
```

Don't worry about the word **function** too much yet.

We'll study functions properly later.

For now:

> `print()` is a built-in Python function used to display information.

---

# 🔤 Strings

Text in Python is represented using strings.

For example:

```python
"Hello"
```

```python
"Football Academy"
```

```python
"Python is fun"
```

Strings can use single quotes:

```python
'Hello'
```

or double quotes:

```python
"Hello"
```

Both are valid.

---

# 🧠 Single vs Double Quotes

These are both strings:

```python
"Python"
```

```python
'Python'
```

For ordinary text, they're functionally equivalent.

Pick a consistent style.

For this course, we'll generally use:

```python
"double quotes"
```

unless single quotes make the code clearer.

---

# 🧪 Practice 2 — String Printer

Write a program that prints:

```text
Your name
Your favorite food
Your favorite hobby
Your current goal
```

Each should appear on its own line.

For example:

```text
Name: Alex
Food: Rice
Hobby: Football
Goal: Become a Python developer
```

Use four `print()` statements.

---

# 🧠 Numbers

Python can also work with numbers.

For example:

```python
10
```

```python
25
```

```python
3.14
```

Numbers don't need quotation marks.

Compare:

```python
print(25)
```

with:

```python
print("25")
```

The output may look identical:

```text
25
```

But Python treats them differently.

```text
25
 ↓
number

"25"
 ↓
text
```

This distinction becomes extremely important when we start working with variables, input, and calculations.

---

# 🧪 Practice 3 — Numbers

Write a program that prints:

```text
Your age
Your height
Your favorite number
```

Use actual numeric values.

Then print the same values again as strings.

For example:

```python
print(25)
print("25")
```

Observe the difference in your code even if the displayed output looks similar.

---

# 🧮 Python Can Calculate

Python isn't just a display machine.

It can perform calculations.

Try:

```python
print(10 + 5)
```

Python evaluates:

```text
10 + 5
 ↓
15
```

and `print()` displays:

```text
15
```

More examples:

```python
print(10 - 3)
print(4 * 5)
print(20 / 4)
```

Output:

```text
7
20
5.0
```

We'll study operators properly in the next batch.

For now, notice something important:

> Python can evaluate an expression before displaying its result.

---

# 🧠 Code vs Output

This is a critical distinction.

You write:

```python
print(10 + 5)
```

Python produces:

```text
15
```

You don't write:

```text
15
```

directly.

You write instructions that cause Python to produce it.

```text
SOURCE CODE
    ↓
Python evaluates
    ↓
OUTPUT
```

---

# 🥋 Practice 4 — Prediction Training

Before running the code, predict the output:

### A

```python
print(7 + 3)
```

### B

```python
print(20 - 8)
```

### C

```python
print(4 * 6)
```

### D

```python
print(20 / 5)
```

### E

```python
print(10 + 2 * 3)
```

Write your answers first.

Then run the program.

Compare your predictions.

---

# 🧠 Comments

Sometimes you want to put notes inside your code.

Python allows comments using:

```python
#
```

Example:

```python
# Display the academy name
print("Rising Stars Academy")
```

Python ignores the comment.

It doesn't execute:

```text
# Display the academy name
```

It's there for humans.

---

# 🧠 Why Comments Exist

Comments can explain:

* Why something exists
* What a section does
* Important assumptions
* Temporary notes
* Complex reasoning

Example:

```python
# Display the player's current training level
print("Intermediate")
```

But don't turn your code into a novel.

This:

```python
# Print hello
print("Hello")
```

isn't particularly useful.

The code already makes the action obvious.

A useful comment explains something that isn't obvious from the code itself.

---

# 🧪 Practice 5 — Comment Lab

Write a small program about yourself.

Requirements:

* At least 4 `print()` statements
* At least 2 useful comments
* At least 1 number
* At least 1 string

Example structure:

```python
# Information about the player
print("Name: ...")
print("Age: ...")

# Current development goal
print("Goal: ...")
```

Don't copy the example exactly.

---

# 🧠 Indentation

Now we encounter one of Python's most recognizable characteristics:

**indentation matters.**

Consider:

```python
if True:
    print("Hello")
```

Notice the spaces before:

```python
print("Hello")
```

Those spaces are meaningful.

Python uses indentation to define blocks of code.

We'll study `if` statements properly later.

For now, understand the rule:

> **When Python expects an indented block, indentation is part of the syntax.**

---

# ⚠️ Don't Randomly Indent Code

This:

```python
print("Hello")
    print("World")
```

will cause a problem.

Why?

Because Python isn't expecting that second line to be indented.

Likewise, inconsistent indentation can cause problems.

Python generally uses **4 spaces** for one indentation level.

We'll use that consistently throughout the course.

---

# 🧠 Colons

You'll eventually encounter syntax such as:

```python
if condition:
```

The colon indicates that a block follows.

For example:

```python
if True:
    print("This belongs to the block")
```

You don't need to master conditionals yet.

Just recognize this pattern:

```text
statement:
    indented block
```

We'll return to this when we reach conditionals.

---

# 🧪 Practice 6 — Indentation Detective

Look at this:

```python
if True:
print("Hello")
```

### Your Mission

1. Predict what happens.
2. Run it.
3. Identify the problem.
4. Correct it.
5. Explain why indentation matters.

---

# 🧠 Whitespace

Python generally ignores unnecessary spaces in many places.

For example:

```python
print("Hello")
```

is perfectly fine.

You might also encounter:

```python
print( "Hello" )
```

Python can understand it.

But the conventional style is:

```python
print("Hello")
```

Clean code matters.

We'll gradually develop good Python style rather than merely writing code that happens to run.

---

# 🧠 Case Sensitivity

Python is case-sensitive.

These are different:

```python
print
Print
PRINT
```

The built-in function is:

```python
print()
```

not:

```python
Print()
```

For example:

```python
print("Hello")
```

works.

But:

```python
Print("Hello")
```

does not mean the same thing.

---

# 🧪 Practice 7 — Case Sensitivity

Test these separately:

```python
print("Hello")
```

```python
Print("Hello")
```

```python
PRINT("Hello")
```

Observe what happens.

Then explain:

> Why does Python care about capitalization?

---

# 🧠 Python Syntax Is Precise

Consider:

```python
print("Hello")
```

There are several pieces Python expects:

```text
print
(
"Hello"
)
```

Changing the structure can change the meaning—or break the program.

For example:

```python
print("Hello"
```

has a missing closing parenthesis.

And:

```python
print Hello
```

doesn't follow modern Python's `print()` syntax.

The computer doesn't think:

> "I know what they meant."

It follows the language rules.

---

# 🐛 Debugging Lab — Syntax Surgeon

Find and fix every problem in this program:

```python
Print("Welcome")

print("Player registration"

print("Training begins")
    print("Good luck!")
```

### Your Mission

1. Identify every problem.
2. Fix them.
3. Run the corrected program.
4. Explain each correction.

Don't just make it work.

Understand **why** each mistake was a mistake.

---

# 🧠 Multiple Statements

A real program usually contains more than one instruction.

For example:

```python
print("Welcome")
print("Choose an option")
print("1. Register")
print("2. Login")
print("3. Exit")
```

Python executes them sequentially.

```text
Welcome
   ↓
Choose an option
   ↓
1. Register
   ↓
2. Login
   ↓
3. Exit
```

This is the same program-flow concept you learned in Batch 1.

---

# 🥋 Practice 8 — Menu Printer

Create a program that displays:

```text
========================
       WALLET APP
========================

1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Transfer Money
5. Exit
```

### Requirements

* Use `print()`
* Use multiple statements
* Keep the formatting clean
* Do not implement the options yet

You're building the interface only.

---

# 🧠 Escape Characters — First Look

Sometimes you need special characters inside strings.

For example, suppose you want:

```text
He said "Hello".
```

You can write:

```python
print('He said "Hello".')
```

Or use an escape character:

```python
print("He said \"Hello\".")
```

The backslash:

```text
\
```

can change how Python interprets the following character.

You may also encounter:

```python
\n
```

which represents a new line.

For example:

```python
print("Hello\nWorld")
```

produces:

```text
Hello
World
```

Don't memorize every escape sequence yet.

We'll explore strings properly later.

---

# 🧪 Practice 9 — Formatting Experiment

Run:

```python
print("Hello\nPython")
```

Then experiment with:

```python
print("One\nTwo\nThree")
```

Then create your own three-line message using a single `print()` statement.

---

# 🧠 Reading Python Code

Now let's reverse the process.

Instead of writing code, read it.

Consider:

```python
print("Wallet App")
print("Balance")
print(5000)
print("Available")
```

Ask yourself:

```text
What does the program do?

How many statements are there?

Which values are strings?

Which value is a number?

What will the output look like?
```

This is **code reading**.

Don't underestimate it.

Being able to read code is just as important as writing code.

---

# 🥋 Practice 10 — Code Reading

Analyze:

```python
print("Store")
print("Products:")
print("Laptop")
print(150000)
print("Phone")
print(80000)
```

Answer:

1. How many `print()` statements are there?
2. How many strings?
3. How many numbers?
4. What is the exact output?
5. Which lines represent product names?
6. Which lines represent prices?

---

# 🔥 Challenge — Build a Profile

Create a Python program that displays a fictional developer profile.

It should contain:

```text
==============================
       DEVELOPER PROFILE
==============================

Name:
Age:
Location:
Learning:
Goal:
Favorite Number:
```

### Requirements

* Use `print()`
* Include strings
* Include at least one number
* Include at least one comment
* Use clean formatting
* Make it your own

### Extra Challenge

Create the same output using:

**Approach A**

Multiple `print()` statements.

**Approach B**

Fewer `print()` statements using `\n`.

Compare the two approaches.

Which one do you find easier to read?

---

# 🛠️ MINI-PROJECT — Terminal Store Welcome Screen

We're introducing your second long-term project.

## 🛒 Terminal Store

This project will eventually grow into a functional terminal-based store.

For now, it is just a screen.

Create:

```text
===============================
        MY TERMINAL STORE
===============================

Welcome!

Available Categories

1. Electronics
2. Clothing
3. Food
4. Accessories

===============================
      Happy Shopping!
===============================
```

### Requirements

Your program must:

* Use Python
* Use `print()`
* Use clean formatting
* Contain comments where appropriate
* Run without syntax errors
* Be your own design

### Think First

Before coding, identify:

```text
INPUT:
None for now.

PROCESS:
Display the store interface.

OUTPUT:
The store welcome screen.
```

Notice something?

A program doesn't necessarily need user input yet.

We're intentionally building the project incrementally.

---

# 🧠 DEBUGGING LAB — Real Beginner Errors

Study these examples.

## Error 1 — Missing Quote

```python
print("Hello)
```

What is wrong?

---

## Error 2 — Missing Parenthesis

```python
print("Hello"
```

What is wrong?

---

## Error 3 — Wrong Capitalization

```python
Print("Hello")
```

What is wrong?

---

## Error 4 — Unexpected Indentation

```python
print("Hello")
    print("World")
```

What is wrong?

---

## Error 5 — Missing Colon

```python
if True
    print("Hello")
```

What is wrong?

Don't worry if the last example isn't completely familiar yet.

The objective is to begin recognizing Python's structural rules.

---

# 🧠 PROFESSIONAL HABIT — Read Error Messages

When Python reports an error, don't immediately panic.

😂

Read it.

Python often tells you:

```text
What went wrong
Where it happened
What type of error occurred
```

For example:

```text
SyntaxError
```

is telling you that Python couldn't correctly parse the code.

Later, we'll study error messages and exceptions much more deeply.

For now, develop this habit:

```text
Error
 ↓
Read it
 ↓
Find the location
 ↓
Understand the message
 ↓
Inspect nearby code
 ↓
Fix
 ↓
Run again
```

---

# 🧠 CONCEPT INTEGRATION

You've now built your first layer of Python syntax:

```text
Python Program
      │
      ├── Statements
      │
      ├── print()
      │
      ├── Strings
      │
      ├── Numbers
      │
      ├── Comments
      │
      ├── Indentation
      │
      ├── Colons
      │
      └── Escape sequences
```

Don't worry about mastering everything immediately.

We're going to revisit these ideas repeatedly.

---

# 🥋 INTEGRATION EXERCISE — Academy Match Report

Build a program that displays a match report.

It should contain:

```text
================================
        MATCH REPORT
================================

Team: Rising Stars Academy
Opponent: City United

Goals Scored: 3
Goals Conceded: 1

Result: Victory

================================
```

### Requirements

* Use multiple `print()` statements.
* Use strings.
* Use numbers.
* Use at least one comment.
* Keep the output organized.

### Before Coding

Write your algorithm:

```text
1.
2.
3.
4.
...
```

Then implement it.

---

# 🧠 REVISION CHECK

Do these without looking back.

## Concept Recall

### 1.

What does `print()` do?

### 2.

What is a string?

### 3.

How do you write a comment in Python?

### 4.

Is Python case-sensitive?

### 5.

Why does indentation matter?

### 6.

What file extension is commonly used for Python source files?

### 7.

What does `\n` represent?

### 8.

What's the difference between:

```python
25
```

and:

```python
"25"
```

---

# 🔍 PREDICT THE OUTPUT

Do not run this immediately.

```python
print("Python")
print(10)
print(5 + 5)
print("5 + 5")
print("Done")
```

What is the exact output?

---

# 🔍 PREDICT THE ERROR

What do you expect to happen?

```python
print("Hello"
```

Explain why.

---

# 🐛 FIND THE BUG

What's wrong with this?

```python
print("Wallet")
print("Balance:")
    print(5000)
```

Explain the problem before fixing it.

---

# 🧠 EXPLAIN IT

Explain in your own words:

> Why is learning to read code important, even if your main goal is to write code?

---

# 🥋 SKILL CHECK

> [!important]
> Complete this independently.
>
> Don't use the workbook as a step-by-step guide.
> You should now be able to combine the basic syntax you've learned.

---

## Part A — Syntax

Write a program that displays:

```text
Welcome to Python
I am learning to program
One step at a time
```

Use three `print()` statements.

---

## Part B — Data

Write a program displaying:

```text
Name: [your fictional player]
Age: [number]
Position: [position]
Jersey: [number]
```

Make sure the numbers are written as numbers rather than strings where appropriate.

---

## Part C — Comments

Write a small program with:

* Two useful comments
* Four `print()` statements
* At least one number
* At least one string

---

## Part D — Debugging

Fix this:

```python
Print("Terminal Store")

print("Products:"
print("Laptop")
    print(150000)
```

Then explain every problem you found.

---

## Part E — Independent Program

Build a small **wallet app welcome screen**.

It should display:

```text
========================
       MY WALLET
========================

Welcome, [name]!

1. Check Balance
2. Deposit
3. Withdraw
4. Transfer
5. Exit

========================
```

For now, the options don't need to work.

The goal is syntax and presentation.

---

# 📊 SKILL CHECK — SELF ASSESSMENT

After completing the assessment, record:

```text
Score:

What I found easy:

What I found difficult:

Which syntax error was easiest to recognize:

Which syntax error confused me:

Could I write a small Python program from scratch?

Confidence:

⬜ Still shaky
⬜ Developing
⬜ Comfortable
⬜ Very comfortable
```

> [!important] Progression Rule
> Bring your assessment result back before we move into the next batch.
>
> If the fundamentals are solid, we'll continue.
> If something is shaky, we'll reinforce it before adding more syntax.

---

# 🚀 CAPSTONE CONNECTION

We now have **three tiny beginnings**.

## ⚽ Football Academy AI

```text
Version 0.1

Academy Welcome Screen
```

## 💰 Wallet App

```text
Version 0.1

Wallet Welcome Screen
```

## 🛒 Terminal Store

```text
Version 0.1

Store Welcome Screen
```

They're intentionally simple.

Soon we'll give them memory.

Then interaction.

Then logic.

Then structure.

Eventually:

```text
print()
   ↓
Variables
   ↓
Input
   ↓
Operators
   ↓
Conditionals
   ↓
Loops
   ↓
Functions
   ↓
Collections
   ↓
Classes
   ↓
Files
   ↓
Modules
   ↓
Testing
   ↓
Real applications
```

---

# 🧠 BATCH SUMMARY

You've now started speaking basic Python.

Your current toolkit includes:

```python
print("Hello")
```

```python
print(42)
```

```python
# Comment
```

and basic syntax concepts such as:

```text
Strings
Numbers
Statements
Comments
Indentation
Colons
Escape sequences
Case sensitivity
```

More importantly, you've practiced:

```text
Read
 ↓
Predict
 ↓
Write
 ↓
Run
 ↓
Debug
```

That's the cycle we'll keep repeating.

---

# 🌱 GROWTH LOG

### What clicked today?

>

### What syntax feels natural already?

>

### What syntax still feels awkward?

>

### Which error did you understand best?

>

### Which error took the most effort to fix?

>

### Which project did you enjoy most?

> ⚽ Academy / 💰 Wallet / 🛒 Store

### Could I write a basic Python program without a tutorial?

>

### What can I build now that I couldn't build before?

>

---

# 🏅 PART 1 PROGRESS

```text
🧠 Batch 1 — Thinking Like a Programmer
██████████  COMPLETE

💻 Batch 2 — Your First Python Programs
██████████  COMPLETE

📦 Batch 3 — Variables & Data
░░░░░░░░░░  NEXT

🔢 Batch 4 — Operators & Expressions
░░░░░░░░░░  LOCKED

🗣️ Batch 5 — Input & Output
░░░░░░░░░░  LOCKED

🔤 Batch 6 — Strings
░░░░░░░░░░  LOCKED

🤔 Batch 7 — Conditionals
░░░░░░░░░░  LOCKED

🔁 Batch 8 — Loops
░░░░░░░░░░  LOCKED

🏆 Part 1 Boss Fight
░░░░░░░░░░  LOCKED
```

---

# 🎯 BATCH 2 EXIT CRITERIA

Before moving forward, I should be able to:

* [ ] Create and run a `.py` file
* [ ] Use `print()` confidently
* [ ] Write strings and numbers
* [ ] Use comments
* [ ] Understand basic indentation
* [ ] Recognize basic Python syntax
* [ ] Predict simple output
* [ ] Read simple Python code
* [ ] Identify common beginner syntax mistakes
* [ ] Write a small program from scratch

---

# 🥋 Sensei's Final Word

Right now, your programs are tiny.

That's exactly how they should be.

Don't underestimate these little programs.

Every large Python application is ultimately made from small instructions combined intelligently.

Today:

```text
print("Hello")
```

Tomorrow:

```text
Wallet
   ↓
Users
   ↓
Accounts
   ↓
Transactions
   ↓
Persistence
   ↓
Validation
   ↓
Tests
```

The complexity comes later.

For now, your mission is simple:

> **Make Python syntax feel boring.**

When basic syntax becomes second nature, your brain is free to focus on the interesting part:

**solving problems.**

🐍 Keep building.

---

# 🧠 Numbers

Python can also work with numbers.

For example:

```python
10
```

```python
25
```

```python
3.14
```

Numbers don't need quotation marks.

Compare:

```python
print(25)
```

with:

```python
print("25")
```

The output may look identical:

```text
25
```

But Python treats them differently.

```text
25
 ↓
number

"25"
 ↓
text
```

This distinction becomes extremely important when we start working with variables, input, and calculations.

---

# 🧪 Practice 3 — Numbers

Write a program that prints:

```text
Your age
Your height
Your favorite number
```

Use actual numeric values.

Then print the same values again as strings.

For example:

```python
print(25)
print("25")
```

Observe the difference in your code even if the displayed output looks similar.

---

# 🧮 Python Can Calculate

Python isn't just a display machine.

It can perform calculations.

Try:

```python
print(10 + 5)
```

Python evaluates:

```text
10 + 5
 ↓
15
```

and `print()` displays:

```text
15
```

More examples:

```python
print(10 - 3)
print(4 * 5)
print(20 / 4)
```

Output:

```text
7
20
5.0
```

We'll study operators properly in the next batch.

For now, notice something important:

> Python can evaluate an expression before displaying its result.

---

# 🧠 Code vs Output

This is a critical distinction.

You write:

```python
print(10 + 5)
```

Python produces:

```text
15
```

You don't write:

```text
15
```

directly.

You write instructions that cause Python to produce it.

```text
SOURCE CODE
    ↓
Python evaluates
    ↓
OUTPUT
```

---

# 🥋 Practice 4 — Prediction Training

Before running the code, predict the output:

### A

```python
print(7 + 3)
```

### B

```python
print(20 - 8)
```

### C

```python
print(4 * 6)
```

### D

```python
print(20 / 5)
```

### E

```python
print(10 + 2 * 3)
```

Write your answers first.

Then run the program.

Compare your predictions.

---

# 🧠 Comments

Sometimes you want to put notes inside your code.

Python allows comments using:

```python
#
```

Example:

```python
# Display the academy name
print("Rising Stars Academy")
```

Python ignores the comment.

It doesn't execute:

```text
# Display the academy name
```

It's there for humans.

---

# 🧠 Why Comments Exist

Comments can explain:

* Why something exists
* What a section does
* Important assumptions
* Temporary notes
* Complex reasoning

Example:

```python
# Display the player's current training level
print("Intermediate")
```

But don't turn your code into a novel.

This:

```python
# Print hello
print("Hello")
```

isn't particularly useful.

The code already makes the action obvious.

A useful comment explains something that isn't obvious from the code itself.

---

# 🧪 Practice 5 — Comment Lab

Write a small program about yourself.

Requirements:

* At least 4 `print()` statements
* At least 2 useful comments
* At least 1 number
* At least 1 string

Example structure:

```python
# Information about the player
print("Name: ...")
print("Age: ...")

# Current development goal
print("Goal: ...")
```

Don't copy the example exactly.

---

# 🧠 Indentation

Now we encounter one of Python's most recognizable characteristics:

**indentation matters.**

Consider:

```python
if True:
    print("Hello")
```

Notice the spaces before:

```python
print("Hello")
```

Those spaces are meaningful.

Python uses indentation to define blocks of code.

We'll study `if` statements properly later.

For now, understand the rule:

> **When Python expects an indented block, indentation is part of the syntax.**

---

# ⚠️ Don't Randomly Indent Code

This:

```python
print("Hello")
    print("World")
```

will cause a problem.

Why?

Because Python isn't expecting that second line to be indented.

Likewise, inconsistent indentation can cause problems.

Python generally uses **4 spaces** for one indentation level.

We'll use that consistently throughout the course.

---

# 🧠 Colons

You'll eventually encounter syntax such as:

```python
if condition:
```

The colon indicates that a block follows.

For example:

```python
if True:
    print("This belongs to the block")
```

You don't need to master conditionals yet.

Just recognize this pattern:

```text
statement:
    indented block
```

We'll return to this when we reach conditionals.

---

# 🧪 Practice 6 — Indentation Detective

Look at this:

```python
if True:
print("Hello")
```

### Your Mission

1. Predict what happens.
2. Run it.
3. Identify the problem.
4. Correct it.
5. Explain why indentation matters.

---

# 🧠 Whitespace

Python generally ignores unnecessary spaces in many places.

For example:

```python
print("Hello")
```

is perfectly fine.

You might also encounter:

```python
print( "Hello" )
```

Python can understand it.

But the conventional style is:

```python
print("Hello")
```

Clean code matters.

We'll gradually develop good Python style rather than merely writing code that happens to run.

---

# 🧠 Case Sensitivity

Python is case-sensitive.

These are different:

```python
print
Print
PRINT
```

The built-in function is:

```python
print()
```

not:

```python
Print()
```

For example:

```python
print("Hello")
```

works.

But:

```python
Print("Hello")
```

does not mean the same thing.

---

# 🧪 Practice 7 — Case Sensitivity

Test these separately:

```python
print("Hello")
```

```python
Print("Hello")
```

```python
PRINT("Hello")
```

Observe what happens.

Then explain:

> Why does Python care about capitalization?

---

# 🧠 Python Syntax Is Precise

Consider:

```python
print("Hello")
```

There are several pieces Python expects:

```text
print
(
"Hello"
)
```

Changing the structure can change the meaning—or break the program.

For example:

```python
print("Hello"
```

has a missing closing parenthesis.

And:

```python
print Hello
```

doesn't follow modern Python's `print()` syntax.

The computer doesn't think:

> "I know what they meant."

It follows the language rules.

---

# 🐛 Debugging Lab — Syntax Surgeon

Find and fix every problem in this program:

```python
Print("Welcome")

print("Player registration"

print("Training begins")
    print("Good luck!")
```

### Your Mission

1. Identify every problem.
2. Fix them.
3. Run the corrected program.
4. Explain each correction.

Don't just make it work.

Understand **why** each mistake was a mistake.

---

# 🧠 Multiple Statements

A real program usually contains more than one instruction.

For example:

```python
print("Welcome")
print("Choose an option")
print("1. Register")
print("2. Login")
print("3. Exit")
```

Python executes them sequentially.

```text
Welcome
   ↓
Choose an option
   ↓
1. Register
   ↓
2. Login
   ↓
3. Exit
```

This is the same program-flow concept you learned in Batch 1.

---

# 🥋 Practice 8 — Menu Printer

Create a program that displays:

```text
========================
       WALLET APP
========================

1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Transfer Money
5. Exit
```

### Requirements

* Use `print()`
* Use multiple statements
* Keep the formatting clean
* Do not implement the options yet

You're building the interface only.

---

# 🧠 Escape Characters — First Look

Sometimes you need special characters inside strings.

For example, suppose you want:

```text
He said "Hello".
```

You can write:

```python
print('He said "Hello".')
```

Or use an escape character:

```python
print("He said \"Hello\".")
```

The backslash:

```text
\
```

can change how Python interprets the following character.

You may also encounter:

```python
\n
```

which represents a new line.

For example:

```python
print("Hello\nWorld")
```

produces:

```text
Hello
World
```

Don't memorize every escape sequence yet.

We'll explore strings properly later.

---

# 🧪 Practice 9 — Formatting Experiment

Run:

```python
print("Hello\nPython")
```

Then experiment with:

```python
print("One\nTwo\nThree")
```

Then create your own three-line message using a single `print()` statement.

---

# 🧠 Reading Python Code

Now let's reverse the process.

Instead of writing code, read it.

Consider:

```python
print("Wallet App")
print("Balance")
print(5000)
print("Available")
```

Ask yourself:

```text
What does the program do?

How many statements are there?

Which values are strings?

Which value is a number?

What will the output look like?
```

This is **code reading**.

Don't underestimate it.

Being able to read code is just as important as writing code.

---

# 🥋 Practice 10 — Code Reading

Analyze:

```python
print("Store")
print("Products:")
print("Laptop")
print(150000)
print("Phone")
print(80000)
```

Answer:

1. How many `print()` statements are there?
2. How many strings?
3. How many numbers?
4. What is the exact output?
5. Which lines represent product names?
6. Which lines represent prices?

---

# 🔥 Challenge — Build a Profile

Create a Python program that displays a fictional developer profile.

It should contain:

```text
==============================
       DEVELOPER PROFILE
==============================

Name:
Age:
Location:
Learning:
Goal:
Favorite Number:
```

### Requirements

* Use `print()`
* Include strings
* Include at least one number
* Include at least one comment
* Use clean formatting
* Make it your own

### Extra Challenge

Create the same output using:

**Approach A**

Multiple `print()` statements.

**Approach B**

Fewer `print()` statements using `\n`.

Compare the two approaches.

Which one do you find easier to read?

---

# 🛠️ MINI-PROJECT — Terminal Store Welcome Screen

We're introducing your second long-term project.

## 🛒 Terminal Store

This project will eventually grow into a functional terminal-based store.

For now, it is just a screen.

Create:

```text
===============================
        MY TERMINAL STORE
===============================

Welcome!

Available Categories

1. Electronics
2. Clothing
3. Food
4. Accessories

===============================
      Happy Shopping!
===============================
```

### Requirements

Your program must:

* Use Python
* Use `print()`
* Use clean formatting
* Contain comments where appropriate
* Run without syntax errors
* Be your own design

### Think First

Before coding, identify:

```text
INPUT:
None for now.

PROCESS:
Display the store interface.

OUTPUT:
The store welcome screen.
```

Notice something?

A program doesn't necessarily need user input yet.

We're intentionally building the project incrementally.

---

# 🧠 DEBUGGING LAB — Real Beginner Errors

Study these examples.

## Error 1 — Missing Quote

```python
print("Hello)
```

What is wrong?

---

## Error 2 — Missing Parenthesis

```python
print("Hello"
```

What is wrong?

---

## Error 3 — Wrong Capitalization

```python
Print("Hello")
```

What is wrong?

---

## Error 4 — Unexpected Indentation

```python
print("Hello")
    print("World")
```

What is wrong?

---

## Error 5 — Missing Colon

```python
if True
    print("Hello")
```

What is wrong?

Don't worry if the last example isn't completely familiar yet.

The objective is to begin recognizing Python's structural rules.

---

# 🧠 PROFESSIONAL HABIT — Read Error Messages

When Python reports an error, don't immediately panic.

😂

Read it.

Python often tells you:

```text
What went wrong
Where it happened
What type of error occurred
```

For example:

```text
SyntaxError
```

is telling you that Python couldn't correctly parse the code.

Later, we'll study error messages and exceptions much more deeply.

For now, develop this habit:

```text
Error
 ↓
Read it
 ↓
Find the location
 ↓
Understand the message
 ↓
Inspect nearby code
 ↓
Fix
 ↓
Run again
```

---

# 🧠 CONCEPT INTEGRATION

You've now built your first layer of Python syntax:

```text
Python Program
      │
      ├── Statements
      │
      ├── print()
      │
      ├── Strings
      │
      ├── Numbers
      │
      ├── Comments
      │
      ├── Indentation
      │
      ├── Colons
      │
      └── Escape sequences
```

Don't worry about mastering everything immediately.

We're going to revisit these ideas repeatedly.

---

# 🥋 INTEGRATION EXERCISE — Academy Match Report

Build a program that displays a match report.

It should contain:

```text
================================
        MATCH REPORT
================================

Team: Rising Stars Academy
Opponent: City United

Goals Scored: 3
Goals Conceded: 1

Result: Victory

================================
```

### Requirements

* Use multiple `print()` statements.
* Use strings.
* Use numbers.
* Use at least one comment.
* Keep the output organized.

### Before Coding

Write your algorithm:

```text
1.
2.
3.
4.
...
```

Then implement it.

---

# 🧠 REVISION CHECK

Do these without looking back.

## Concept Recall

### 1.

What does `print()` do?

### 2.

What is a string?

### 3.

How do you write a comment in Python?

### 4.

Is Python case-sensitive?

### 5.

Why does indentation matter?

### 6.

What file extension is commonly used for Python source files?

### 7.

What does `\n` represent?

### 8.

What's the difference between:

```python
25
```

and:

```python
"25"
```

---

# 🔍 PREDICT THE OUTPUT

Do not run this immediately.

```python
print("Python")
print(10)
print(5 + 5)
print("5 + 5")
print("Done")
```

What is the exact output?

---

# 🔍 PREDICT THE ERROR

What do you expect to happen?

```python
print("Hello"
```

Explain why.

---

# 🐛 FIND THE BUG

What's wrong with this?

```python
print("Wallet")
print("Balance:")
    print(5000)
```

Explain the problem before fixing it.

---

# 🧠 EXPLAIN IT

Explain in your own words:

> Why is learning to read code important, even if your main goal is to write code?

---

# 🥋 SKILL CHECK

> [!important]
> Complete this independently.
>
> Don't use the workbook as a step-by-step guide.
> You should now be able to combine the basic syntax you've learned.

---

## Part A — Syntax

Write a program that displays:

```text
Welcome to Python
I am learning to program
One step at a time
```

Use three `print()` statements.

---

## Part B — Data

Write a program displaying:

```text
Name: [your fictional player]
Age: [number]
Position: [position]
Jersey: [number]
```

Make sure the numbers are written as numbers rather than strings where appropriate.

---

## Part C — Comments

Write a small program with:

* Two useful comments
* Four `print()` statements
* At least one number
* At least one string

---

## Part D — Debugging

Fix this:

```python
Print("Terminal Store")

print("Products:"
print("Laptop")
    print(150000)
```

Then explain every problem you found.

---

## Part E — Independent Program

Build a small **wallet app welcome screen**.

It should display:

```text
========================
       MY WALLET
========================

Welcome, [name]!

1. Check Balance
2. Deposit
3. Withdraw
4. Transfer
5. Exit

========================
```

For now, the options don't need to work.

The goal is syntax and presentation.

---

# 📊 SKILL CHECK — SELF ASSESSMENT

After completing the assessment, record:

```text
Score:

What I found easy:

What I found difficult:

Which syntax error was easiest to recognize:

Which syntax error confused me:

Could I write a small Python program from scratch?

Confidence:

⬜ Still shaky
⬜ Developing
⬜ Comfortable
⬜ Very comfortable
```

> [!important] Progression Rule
> Bring your assessment result back before we move into the next batch.
>
> If the fundamentals are solid, we'll continue.
> If something is shaky, we'll reinforce it before adding more syntax.

---

# 🚀 CAPSTONE CONNECTION

We now have **three tiny beginnings**.

## ⚽ Football Academy AI

```text
Version 0.1

Academy Welcome Screen
```

## 💰 Wallet App

```text
Version 0.1

Wallet Welcome Screen
```

## 🛒 Terminal Store

```text
Version 0.1

Store Welcome Screen
```

They're intentionally simple.

Soon we'll give them memory.

Then interaction.

Then logic.

Then structure.

Eventually:

```text
print()
   ↓
Variables
   ↓
Input
   ↓
Operators
   ↓
Conditionals
   ↓
Loops
   ↓
Functions
   ↓
Collections
   ↓
Classes
   ↓
Files
   ↓
Modules
   ↓
Testing
   ↓
Real applications
```

---

# 🧠 BATCH SUMMARY

You've now started speaking basic Python.

Your current toolkit includes:

```python
print("Hello")
```

```python
print(42)
```

```python
# Comment
```

and basic syntax concepts such as:

```text
Strings
Numbers
Statements
Comments
Indentation
Colons
Escape sequences
Case sensitivity
```

More importantly, you've practiced:

```text
Read
 ↓
Predict
 ↓
Write
 ↓
Run
 ↓
Debug
```

That's the cycle we'll keep repeating.

---

# 🌱 GROWTH LOG

### What clicked today?

>

### What syntax feels natural already?

>

### What syntax still feels awkward?

>

### Which error did you understand best?

>

### Which error took the most effort to fix?

>

### Which project did you enjoy most?

> ⚽ Academy / 💰 Wallet / 🛒 Store

### Could I write a basic Python program without a tutorial?

>

### What can I build now that I couldn't build before?

>

---

# 🏅 PART 1 PROGRESS

```text
🧠 Batch 1 — Thinking Like a Programmer
██████████  COMPLETE

💻 Batch 2 — Your First Python Programs
██████████  COMPLETE

📦 Batch 3 — Variables & Data
░░░░░░░░░░  NEXT

🔢 Batch 4 — Operators & Expressions
░░░░░░░░░░  LOCKED

🗣️ Batch 5 — Input & Output
░░░░░░░░░░  LOCKED

🔤 Batch 6 — Strings
░░░░░░░░░░  LOCKED

🤔 Batch 7 — Conditionals
░░░░░░░░░░  LOCKED

🔁 Batch 8 — Loops
░░░░░░░░░░  LOCKED

🏆 Part 1 Boss Fight
░░░░░░░░░░  LOCKED
```

---

# 🎯 BATCH 2 EXIT CRITERIA

Before moving forward, I should be able to:

* [ ] Create and run a `.py` file
* [ ] Use `print()` confidently
* [ ] Write strings and numbers
* [ ] Use comments
* [ ] Understand basic indentation
* [ ] Recognize basic Python syntax
* [ ] Predict simple output
* [ ] Read simple Python code
* [ ] Identify common beginner syntax mistakes
* [ ] Write a small program from scratch

---

# 🥋 Sensei's Final Word

Right now, your programs are tiny.

That's exactly how they should be.

Don't underestimate these little programs.

Every large Python application is ultimately made from small instructions combined intelligently.

Today:

```text
print("Hello")
```

Tomorrow:

```text
Wallet
   ↓
Users
   ↓
Accounts
   ↓
Transactions
   ↓
Persistence
   ↓
Validation
   ↓
Tests
```

The complexity comes later.

For now, your mission is simple:

> **Make Python syntax feel boring.**

When basic syntax becomes second nature, your brain is free to focus on the interesting part:

**solving problems.**

🐍 Keep building.
