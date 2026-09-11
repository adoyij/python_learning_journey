# 🐍 Python Learning Journey

# 🟢 Part 1 — Programming & Python Foundations

## Batch 3 — Variables & Assignment 📦

> *"A variable isn't just a box that stores data. It's a name that lets your program remember and work with information."*

---

# 🥋 Welcome, Apprentice

You've already learned how to make Python execute instructions and produce output.

Now we're giving your programs **memory**.

So far, you've mostly written things like:

```python
print("Welcome")
print(10 + 5)
```

But imagine your program needs to remember:

* a player's name
* a wallet balance
* a product price
* a number of goals
* a user's age
* the name of a store

We need a way to **give those values names**.

That's where variables come in.

And this is a major milestone.

Because from this point forward, your programs stop being merely:

> "Do this."

and start becoming:

> "Remember this, then use it later."

Let's build that skill properly. 🐍🔥

---

# 🗺️ Where You Are

```text
🐍 Python Learning Journey

Phase 1 — Python Fluency

└── Part 1 — Programming & Python Foundations
    │
    ├── 🧠 Batch 1 — Thinking Like a Programmer      ✅
    ├── 🐍 Batch 2 — Your First Python Programs      ✅
    ├── 📦 Batch 3 — Variables & Assignment          ← YOU ARE HERE
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
> By the end of this workbook, you should be comfortable creating variables, assigning values, reassigning them, using them in expressions, and reasoning about how their values change as a program executes.

---

# 🎯 Learning Objectives

By the end of this batch, you should be able to:

* Understand what a variable is
* Create variables using assignment
* Understand the `=` operator in assignment
* Read variable names naturally
* Follow the value of a variable through a program
* Reassign variables
* Use variables inside expressions
* Understand that variables can refer to different types of values
* Follow multiple variables interacting with each other
* Choose sensible variable names
* Understand basic naming rules
* Avoid common variable mistakes
* Build small programs around stored information

---

# 🧠 THE BIG IDEA

Imagine this:

```text
Player name → "Alex"
Age         → 19
Goals       → 7
```

Your program needs to remember these values.

We can give each value a name:

```python
player_name = "Alex"
age = 19
goals = 7
```

Now Python has names it can use to access those values.

You can later write:

```python
print(player_name)
print(age)
print(goals)
```

Output:

```text
Alex
19
7
```

The important idea is:

```text
Value
  ↓
given a name
  ↓
stored/referenced by the program
  ↓
can be used later
```

---

# 🧠 What Is a Variable?

At the beginner level, think of a variable as:

> **A name associated with a value that your program can use.**

For example:

```python
name = "Alex"
```

We can think:

```text
name
 ↓
"Alex"
```

Then:

```python
print(name)
```

Python looks at `name` and obtains the value associated with it.

```text
name
 ↓
"Alex"
 ↓
print
 ↓
Alex
```

---

# 🧪 Your First Variables

Try:

```python
name = "Alex"
age = 20
position = "Forward"
```

Then:

```python
print(name)
print(age)
print(position)
```

You should get:

```text
Alex
20
Forward
```

Notice how much more useful this is than:

```python
print("Alex")
print(20)
print("Forward")
```

The program now has **named information**.

---

# 🧠 Assignment

This is called **assignment**:

```python
age = 20
```

The `=` here does **not** mean:

> "These two things are mathematically equal."

Instead, think:

> **"Associate the value on the right with the name on the left."**

So:

```python
age = 20
```

can be mentally read as:

> "Set `age` to 20."

---

# ⚠️ VERY IMPORTANT

Don't read:

```python
age = 20
```

as:

> "Age equals 20 forever."

Read it as:

> **"Make the variable `age` refer to the value 20."**

Because later:

```python
age = 21
```

is perfectly valid.

The value can change.

---

# 🧠 Reassignment

Consider:

```python
score = 10
print(score)

score = 15
print(score)
```

Output:

```text
10
15
```

What happened?

Initially:

```text
score → 10
```

Then:

```text
score → 15
```

The variable was **reassigned**.

---

# 🧠 Mental Model

Think of the program executing from top to bottom:

```text
score = 10
     ↓
score → 10

print(score)
     ↓
10

score = 15
     ↓
score → 15

print(score)
     ↓
15
```

This is why **execution order matters**.

---

# 🥋 Practice 1 — Variable Basics

Create variables for:

* Your name
* Your age
* Your favorite programming language
* Your current learning stage

Then print each one.

### Requirements

Use variables.

Don't directly put the values inside `print()`.

For example, practice the pattern:

```python
something = value
print(something)
```

---

# 🧪 Practice 2 — Predict the Value

Before running the code, determine what each `print()` displays.

```python
score = 10
print(score)

score = 20
print(score)

score = 35
print(score)
```

Write the output.

Then run it.

---

# 🧠 Variables Can Be Used in Expressions

Variables become much more powerful when you use them in calculations.

Consider:

```python
price = 500
quantity = 3

total = price * quantity

print(total)
```

Output:

```text
1500
```

Notice the flow:

```text
price
  ↓
500

quantity
  ↓
3

500 × 3
  ↓
1500
  ↓
total
```

We've just built a tiny piece of a store.

---

# 🛒 Store Example

Imagine your terminal store has:

```python
product_price = 2500
quantity = 4
```

We can calculate:

```python
total_cost = product_price * quantity
```

Then:

```python
print(total_cost)
```

Output:

```text
10000
```

This is the beginning of the **store capstone** you'll eventually build.

---

# 💰 Wallet Example

A wallet application might have:

```python
balance = 50000
withdrawal = 12000
```

Then:

```python
remaining_balance = balance - withdrawal
```

Now:

```python
print(remaining_balance)
```

Output:

```text
38000
```

Again:

```text
Stored information
       ↓
Variables
       ↓
Calculations
       ↓
Useful result
```

---

# 🥋 Practice 3 — Simple Store

Create:

```text
product_price
quantity
total_cost
```

Set a product price and quantity.

Calculate the total cost.

Print the result.

### Example scenario

A product costs:

```text
₦3,500
```

A customer buys:

```text
4
```

Your program should calculate the total.

Don't hard-code the final answer.

The program must calculate it from the variables.

---

# 🧠 Variables Can Depend on Other Variables

Consider:

```python
price = 100
quantity = 5
total = price * quantity
```

The value of `total` depends on:

```text
price
+
quantity
```

Think of it like:

```text
price ─────┐
           ↓
         total
           ↑
quantity ──┘
```

This is important because real programs contain **relationships between pieces of information**.

---

# 🧪 Practice 4 — Wallet Calculation

Create:

```python
balance = 50000
deposit = 15000
```

Calculate:

```text
new balance
```

Then print it.

Next, introduce:

```python
withdrawal = 10000
```

Calculate the balance after the withdrawal.

Think carefully about the order of operations.

---

# 🧠 Variable Values Don't Have to Be Numbers

Variables can refer to different kinds of values.

For example:

```python
name = "Deborah"
age = 25
balance = 15000.50
```

The variables have different kinds of values.

We'll study **data types** more deeply soon.

For now, understand:

```text
name
 ↓
text

age
 ↓
whole number

balance
 ↓
decimal number
```

Variables aren't restricted to one kind of value.

---

# 🧠 THE BIG IDEA

A variable is about the **name**.

The value associated with that name can be different.

For example:

```python
player = "Alex"
```

Then:

```python
player = "Daniel"
```

The variable name remains:

```text
player
```

but the associated value changes.

---

# 🥋 Practice 5 — Changing Identity

Start with:

```python
player = "Alex"
```

Print it.

Then change the variable to another player.

Print it again.

Then change it one more time.

Print it again.

### Your mission

Predict the output **before running the program**.

---

# 🧠 Variable Naming

You are going to create a lot of variables.

Good names make your code easier to understand.

Compare:

```python
x = 50000
```

with:

```python
wallet_balance = 50000
```

Which tells you more?

Obviously:

```python
wallet_balance
```

Good variable names reduce the amount of thinking required when reading code.

---

# 🧠 Good Names

Prefer names like:

```python
player_name
wallet_balance
product_price
total_cost
match_score
account_number
```

Avoid meaningless names when a meaningful name is possible:

```python
x
y
z
thing
stuff
abc
```

Short names aren't automatically bad.

For example:

```python
age = 20
```

is excellent.

The principle is:

> **Use names that communicate meaning.**

---

# 🧠 Snake Case

Python conventionally uses **snake_case** for variable names.

Example:

```python
player_name = "Alex"
wallet_balance = 50000
product_price = 3500
total_cost = 14000
```

Words are separated using underscores.

Instead of:

```python
playerName
```

Python code commonly uses:

```python
player_name
```

We'll consistently practice this style.

---

# ⚠️ Variable Naming Rules

Python variable names have rules.

A variable name:

### Can contain

* Letters
* Numbers
* Underscores

### Cannot

* Start with a number
* Contain spaces
* Use certain special characters
* Be a Python keyword

For example:

```python
player_name = "Alex"
```

Valid.

```python
player2 = "Alex"
```

Valid.

```python
_player = "Alex"
```

Technically valid, although underscores at the beginning have conventions we'll discuss later.

But:

```python
2player = "Alex"
```

Invalid.

And:

```python
player name = "Alex"
```

Invalid.

---

# 🧪 Practice 6 — Naming Detective

Determine whether each variable name is valid.

```text
player_name
player2
2player
wallet_balance
wallet balance
total-cost
_age
class
```

For each one, write:

```text
VALID
```

or:

```text
INVALID
```

Then explain why the invalid ones fail.

> [!tip]
> Don't just memorize the rules. Look for the pattern.

---

# 🧠 Python Keywords

Some words already have special meaning in Python.

These are called **keywords**.

Examples include:

```text
if
else
for
while
class
def
return
True
False
None
```

You shouldn't use these as ordinary variable names.

For example:

```python
class = "Python"
```

is invalid.

Why?

Because Python already reserves `class` for its own syntax.

Don't worry about memorizing every keyword now.

You'll naturally encounter many of them as we learn Python.

---

# 🧠 Assignment Chaining

Python allows:

```python
a = b = c = 10
```

Now all three names refer to the value:

```text
a → 10
b → 10
c → 10
```

This is valid Python.

But don't use clever syntax simply because you can.

Prefer readability.

---

# 🥋 Practice 7 — Multiple Variables

Create three variables:

```text
wallet
savings
cash
```

Set all three to the same starting amount using a single assignment statement.

Print all three.

Then change only one of them.

Print all three again.

Observe what happens.

---

# 🧠 Multiple Assignment

Python also allows:

```python
name, age = "Alex", 20
```

This assigns:

```text
name → "Alex"
age  → 20
```

It's called **multiple assignment**.

Another example:

```python
width, height = 100, 50
```

Now:

```text
width  → 100
height → 50
```

This is convenient when assigning several related values.

---

# 🧪 Practice 8 — Multiple Assignment

Create variables for:

```text
player_name
player_age
player_position
```

Assign them using one statement.

Then print each variable.

Afterward, rewrite the same program using separate assignment statements.

Compare both versions.

Ask yourself:

> Which is easier to read in this situation?

---

# 🧠 Variables and Order

This is one of the most important concepts in this workbook.

Look at:

```python
balance = 50000
withdrawal = 10000

balance = balance - withdrawal

print(balance)
```

Follow it carefully.

Initially:

```text
balance → 50000
withdrawal → 10000
```

Then:

```text
balance = balance - withdrawal
```

becomes:

```text
balance = 50000 - 10000
```

so:

```text
balance → 40000
```

Then:

```python
print(balance)
```

produces:

```text
40000
```

---

# 🤯 The Right Way to Read This

Beginners sometimes look at:

```python
balance = balance - withdrawal
```

and think:

> "How can balance equal balance minus something?"

Don't think of `=` as mathematical equality.

Think:

```text
Take the current value of balance
        ↓
subtract withdrawal
        ↓
put the resulting value back into balance
```

That's **reassignment**.

---

# 🥋 Practice 9 — Follow the Money

Trace this manually:

```python
balance = 100000

balance = balance - 25000

balance = balance + 15000

balance = balance - 10000

print(balance)
```

### Your Mission

Write the value of `balance` after every line that changes it.

```text
Starting balance:
After withdrawal:
After deposit:
After second withdrawal:
Final:
```

Then run the code.

---

# 🧠 Variables Can Refer to Calculated Values

Consider:

```python
price = 2000
discount = 500

final_price = price - discount
```

The variable:

```text
final_price
```

doesn't contain a value you manually typed.

It contains the result of an expression.

This pattern appears everywhere:

```text
Existing data
     ↓
Calculation
     ↓
New variable
```

---

# 🛒 Store Example

```python
product_price = 5000
quantity = 3

subtotal = product_price * quantity

discount = 1000

total = subtotal - discount

print(total)
```

Flow:

```text
product_price
      +
quantity
      ↓
  subtotal
      ↓
   discount
      ↓
    total
```

This is beginning to resemble actual application logic.

---

# 🔥 Challenge — Build the Receipt

Create a small store calculation.

Your program should have variables for:

* Product name
* Product price
* Quantity
* Subtotal
* Discount
* Final total

The program should calculate:

```text
subtotal = price × quantity

final_total = subtotal - discount
```

Then print something resembling:

```text
========================
       RECEIPT
========================

Product: Keyboard
Price: ₦15000
Quantity: 2
Subtotal: ₦30000
Discount: ₦2000
Total: ₦28000
```

### Rules

* Don't manually calculate and type the subtotal.
* Don't manually calculate and type the final total.
* Use variables.
* Let Python perform the calculations.
* Use meaningful variable names.

### Bonus

Change the product price or quantity.

The calculated totals should automatically change.

---

# 🐛 DEBUGGING LAB — Variable Mistakes

Consider:

```python
product_price = 5000
quantity = 3

total = productprice * quantity

print(total)
```

### Your Mission

Find the problem.

Don't run it immediately.

Ask:

```text
What variable did we create?

What variable are we trying to use?

Are they the same name?
```

Then fix it.

---

# 🐛 DEBUGGING LAB 2 — Assignment Order

Consider:

```python
total = price * quantity

price = 5000
quantity = 2

print(total)
```

Something is wrong.

### Your Mission

Explain:

1. What Python encounters first.
2. Why the program can't calculate `total` yet.
3. How to correct the program.

---

# 🧠 Variable Tracing Lab

This is important enough to practice separately.

Consider:

```python
wallet = 50000
deposit = 20000

wallet = wallet + deposit

withdrawal = 15000

wallet = wallet - withdrawal

print(wallet)
```

Don't run it.

Create a table:

| Step               | Variable     | Value |
| ------------------ | ------------ | ----: |
| Start              | `wallet`     |     ? |
| After deposit      | `wallet`     |     ? |
| Withdrawal created | `withdrawal` |     ? |
| After withdrawal   | `wallet`     |     ? |

Then verify your answer by running the code.

---

# 🥋 Practice 10 — Player Statistics

Create:

```python
player_name
matches
goals
assists
```

Give them values.

Then calculate:

```text
total_contributions = goals + assists
```

Print the player's information and total contributions.

### Bonus

Create another variable:

```text
average_goals
```

and calculate the player's average goals per match.

Don't worry about handling edge cases yet.

We'll learn the tools for that later.

---

# 🔥 Mini Challenge — Wallet Snapshot

Create a program representing a simple wallet.

Start with:

```text
Opening balance
```

Then have variables for:

```text
deposit
withdrawal
```

Calculate:

```text
closing balance
```

Your program should display a small wallet summary.

Example:

```text
========================
      WALLET
========================

Opening Balance: ₦50000
Deposit:         ₦20000
Withdrawal:      ₦15000
------------------------
Closing Balance: ₦55000
```

### Requirements

* Use variables for every value.
* Calculate the closing balance.
* Don't manually enter the final answer.
* Use meaningful names.
* Make sure changing the deposit changes the final balance.

### Think First

Before coding, write:

```text
INPUT:
-

PROCESS:
-

OUTPUT:
-
```

Then write your algorithm.

Then write the Python program.

---

# 🧠 Common Beginner Mistakes

## Mistake 1 — Forgetting Quotes for Text

Incorrect:

```python
name = Alex
```

Correct:

```python
name = "Alex"
```

We'll properly explore strings soon.

---

## Mistake 2 — Using a Variable Before Creating It

```python
print(balance)

balance = 50000
```

The program attempts to use `balance` before it has been defined.

---

## Mistake 3 — Misspelling Variable Names

```python
wallet_balance = 50000

print(wallet_balnce)
```

Python treats these as different names.

Be precise.

---

## Mistake 4 — Accidentally Creating a Different Variable

```python
player_name = "Alex"

Player_name = "Daniel"
```

These are different names.

Python variable names are **case-sensitive**.

So:

```text
player_name
```

and:

```text
Player_name
```

are not the same variable.

---

# 🧪 Practice 11 — Case Sensitivity

Predict what happens:

```python
name = "Alex"
Name = "Daniel"

print(name)
print(Name)
```

Then change the code to:

```python
name = "Alex"
name = "Daniel"

print(name)
```

Compare the two programs.

Explain the difference.

---

# 🧠 Case Sensitivity

Python distinguishes uppercase and lowercase letters.

Therefore:

```python
age
Age
AGE
```

are three different names.

As a beginner, consistency is your friend.

Prefer:

```python
player_name
wallet_balance
product_price
```

rather than randomly mixing capitalization.

---

# 🧩 Integration Exercise — Academy Player Card

Create a program containing variables for:

```text
player_name
age
position
jersey_number
goals
assists
```

Calculate:

```text
total_contributions
```

Then display a player card.

Example:

```text
============================
       PLAYER CARD
============================

Name: Alex
Age: 20
Position: Forward
Jersey: 9

Goals: 12
Assists: 7
Contributions: 19
```

### Requirements

Every piece of information must come from a variable.

The contribution total must be calculated.

Don't manually type the final contribution number.

---

# 🧠 Revision Check

Don't look back.

## Concept Recall

### 1.

What is a variable?

### 2.

What does assignment mean in Python?

### 3.

How should you mentally read:

```python
balance = 50000
```

### 4.

What is reassignment?

### 5.

Why is this useful?

```python
total = price * quantity
```

### 6.

Why are meaningful variable names important?

### 7.

What naming convention does Python commonly use for variables?

### 8.

Why is this invalid?

```python
2player = "Alex"
```

### 9.

Why are these different?

```python
name
Name
```

### 10.

What happens when you try to use a variable before it has been defined?

---

# 🔍 Predict the Output

Don't run this until you've written your answer.

```python
balance = 50000

balance = balance + 10000

balance = balance - 15000

balance = balance + 5000

print(balance)
```

What is the output?

Explain your calculation step by step.

---

# 🔍 Predict the Output — Level 2

```python
price = 2000
quantity = 4

subtotal = price * quantity

discount = 1500

total = subtotal - discount

print(subtotal)
print(total)
```

What are the two outputs?

---

# 🐛 Find the Bug

What's wrong?

```python
player_name = "Alex"
player_age = 20

print(Player_name)
print(player_age)
```

Explain the problem.

---

# 🧠 Explain It

Explain this line to a beginner:

```python
balance = balance - withdrawal
```

Don't simply say:

> "It subtracts withdrawal from balance."

Explain what Python is actually doing with the **current value** of `balance`.

---

# 🥋 SKILL CHECK

> [!important]
> Complete this independently.
>
> No walkthrough.
> No copying previous exercises.
>
> The goal is to discover whether variables are becoming natural to you.

---

## Part A — Basic Variables

Create variables for:

```text
store_name
product_name
product_price
quantity
```

Give them sensible values.

Print them.

---

## Part B — Calculation

Using your variables, calculate:

```text
total_cost
```

where:

```text
total_cost = product_price × quantity
```

Print the result.

---

## Part C — Reassignment

Create:

```python
balance = 100000
```

Then:

1. Deposit ₦25000.
2. Withdraw ₦30000.
3. Deposit ₦10000.

Use reassignment.

Print the final balance.

---

## Part D — Tracing

Without running:

```python
score = 10

score = score + 5
score = score * 2
score = score - 8

print(score)
```

Determine the final value.

Explain each change.

---

## Part E — Naming

Identify which are valid variable names:

```text
player_name
player-name
player2
2player
wallet_balance
wallet balance
class
total_cost
```

Explain your answers.

---

## Part F — Independent Problem

Build a small **player statistics calculator**.

Your program should have variables for:

```text
player name
matches played
goals
assists
```

Calculate:

```text
total contributions
```

and:

```text
goals per match
```

Then display the results.

### Requirement

The results must be calculated from the variables.

Do not manually type calculated answers.

---

# 📊 Skill Check — Self Assessment

After completing the assessment, record:

```text
Score:

What I found easy:

What I found difficult:

Where I needed help:

Most interesting exercise:

Mistake I made:

What I now understand better:

Confidence:

⬜ Still confused
⬜ Developing
⬜ Comfortable
⬜ Very comfortable
```

> [!important] Progression Rule
> Complete the Skill Check and assess it externally.
>
> Bring the result back before we continue if you want me to verify whether anything needs reinforcement.

---

# 🛠️ CAPSTONE UPGRADE

## 💰 Wallet App

Our wallet project now gains its first real piece of state.

Previously:

```text
💰 Wallet App
│
└── Concept
```

Now:

```text
💰 Wallet App

Variables
│
├── balance
├── deposit
├── withdrawal
└── remaining_balance
```

We aren't building the full wallet yet.

We're establishing the foundation.

Eventually this will evolve into:

```text
💰 Wallet App
│
├── Variables
├── Input
├── Calculations
├── Conditions
├── Loops
├── Functions
├── Collections
├── Files
├── Exceptions
├── Classes
└── ...
```

---

# 🛒 CAPSTONE UPGRADE

## Terminal Store

The store also gains state:

```text
🛒 Terminal Store

Variables
│
├── product_name
├── product_price
├── quantity
├── subtotal
├── discount
└── total
```

Later we'll turn this into a proper application.

---

# 🧠 What You Should Now Understand

At this point, you should understand that variables allow programs to:

```text
Remember information
       ↓
Give information meaningful names
       ↓
Use that information
       ↓
Calculate new values
       ↓
Change values
       ↓
Produce useful results
```

The most important mental model is:

```text
name = value
```

followed by:

```text
new_name = expression_using_values
```

and:

```text
name = new_value
```

---

# 🌱 Growth Log

Take a few minutes to reflect.

### What clicked today?

>

### What challenged me?

>

### Which exercise am I most proud of?

>

### Did reassignment make sense to me?

>

### Can I trace a variable's value through a program?

>

### Can I choose meaningful variable names?

>

### What still feels shaky?

>

### What should I review?

>

### What can I build now that I couldn't build before?

>

---

# 🏅 PART 1 PROGRESS

## 🟢 Programming & Python Foundations

```text
🧠 Thinking Like a Programmer
██████████  COMPLETE

🐍 Your First Python Programs
██████████  COMPLETE

📦 Variables & Assignment
██████████  COMPLETE

🔢 Operators & Expressions
░░░░░░░░░░  LOCKED

🗣️ Input & Output
░░░░░░░░░░  LOCKED

🔤 Strings
░░░░░░░░░░  LOCKED

🤔 Conditionals
░░░░░░░░░░  LOCKED

🔁 Loops
░░░░░░░░░░  LOCKED

🏆 Part 1 Boss Fight
░░░░░░░░░░  LOCKED
```

---

# 🎯 Batch 3 Exit Criteria

Before considering this batch solid, I should be able to:

* [ ] Create variables confidently
* [ ] Understand assignment
* [ ] Reassign variables
* [ ] Use variables in calculations
* [ ] Trace changing values
* [ ] Use multiple variables together
* [ ] Choose meaningful variable names
* [ ] Follow basic naming rules
* [ ] Recognize case sensitivity
* [ ] Debug simple variable mistakes
* [ ] Build a small program entirely around variables

---

# 🥋 Sensei's Final Word

At first, this:

```python
balance = 50000
```

might look like nothing more than a line of syntax.

It isn't.

You're teaching your program to **remember**.

Then:

```python
balance = balance - withdrawal
```

teaches it to **change what it remembers**.

Then:

```python
total = price * quantity
```

teaches it to **use remembered information to produce new information**.

That pattern is everywhere.

Wallets.

Stores.

Games.

Web applications.

Data pipelines.

AI systems.

Even massive production systems are ultimately manipulating information.

You're learning one of the fundamental building blocks.

> **Give information a name.**
>
> **Give your program something to remember. 🐍**
> :::
