# 🐍 PYTHON JOURNEY — BATCH 7

## Part 1 — Python Foundations

### Topic: **Conditionals & Decision Making**

> 😎 Alright, apprentice.
>
> You've now learned how to:
>
> **store data → manipulate data → receive data → display data → work with text.**
>
> But your programs still have one major weakness.
>
> They can't **make decisions**.
>
> A wallet doesn't just calculate a withdrawal.
>
> It needs to ask:
>
> > "Does this customer have enough money?"
>
> A store doesn't just calculate a discount.
>
> It needs to ask:
>
> > "Is this discount valid?"
>
> Your programs are about to learn how to **choose what happens next.**
>
> Welcome to **Conditionals.** 🐍⚔️

---

# 🎯 BATCH 7 MISSION

By the end of this batch, you should understand:

* `if`
* `else`
* `elif`
* Conditions
* Boolean expressions
* Indentation
* Comparison operators inside decisions
* Logical operators inside decisions
* Nested conditionals
* Multiple conditions
* Decision flow
* Common conditional bugs
* Building decision-making features for your Wallet App
* Building decision-making features for your Terminal Store

---

# 🗺️ WHERE YOU ARE

```text
PART 1 — PYTHON FOUNDATIONS

[✅] Batch 1 — Programming & Python Basics
[✅] Batch 2 — Core Python Foundations
[✅] Batch 3 — Variables & Assignment
[✅] Batch 4 — Operators & Expressions
[✅] Batch 5 — Input & Output
[✅] Batch 6 — Strings
[🔥] Batch 7 — Conditionals
[🔒] Batch 8 — Loops

        ↓

PART 1 BOSS FIGHT
```

Your journey now looks like:

```text
DATA
 ↓
VARIABLES
 ↓
OPERATORS
 ↓
INPUT
 ↓
PROCESSING
 ↓
DECISION
 ↓
OUTPUT
```

That **decision** layer is what we're adding now.

---

# 🧠 THE BIG IDEA

A conditional allows your program to make a decision based on whether something is true or false.

Think about real life:

```text
If it is raining:
    take an umbrella

Otherwise:
    don't take one
```

Python can express the same idea.

```python
if raining:
    print("Take an umbrella")
```

The program checks a condition.

If the condition is `True`, the code runs.

If it's `False`, it doesn't.

---

# 1️⃣ YOUR FIRST `if`

```python
balance = 50000

if balance > 0:
    print("Your wallet has money.")
```

Python asks:

```text
Is balance greater than 0?
```

The answer is:

```text
True
```

So Python executes:

```python
print("Your wallet has money.")
```

---

# 🧠 THE BASIC STRUCTURE

```python
if condition:
    statement
```

There are three important pieces:

```text
if
 ↓
condition
 ↓
:
 ↓
indented code
```

For example:

```python
if balance > 0:
    print("Wallet has money")
```

---

# ⚠️ THE COLON MATTERS

This is correct:

```python
if balance > 0:
    print("Wallet has money")
```

This is incorrect:

```python
if balance > 0
    print("Wallet has money")
```

The `:` tells Python:

> "The block of code belonging to this condition starts here."

---

# 2️⃣ INDENTATION

This is extremely important in Python.

Correct:

```python
if balance > 0:
    print("Wallet has money")
```

Notice the indentation:

```text
if balance > 0:
    ↑
    indented
```

Python uses indentation to determine which statements belong to the `if`.

---

## Example

```python
balance = 50000

if balance > 0:
    print("Wallet has money")
    print("Transaction available")

print("Program finished")
```

Output:

```text
Wallet has money
Transaction available
Program finished
```

The first two `print()` statements belong to the `if`.

The final one does not.

---

# 🧪 PRACTICE 1

Create:

```python
balance = 10000
```

Write an `if` statement that prints:

```text
You have money.
```

only when the balance is greater than zero.

Then change the balance to:

```python
balance = 0
```

Run it again.

Observe what changes.

---

# 3️⃣ `else`

What happens when the condition is false?

That's where `else` comes in.

```python
balance = 0

if balance > 0:
    print("You have money.")
else:
    print("Your wallet is empty.")
```

Output:

```text
Your wallet is empty.
```

---

# 🧠 THE MENTAL MODEL

Think:

```text
             condition
                 ↓
            ┌────┴────┐
           True      False
            ↓           ↓
           if         else
            ↓           ↓
        action A    action B
```

Exactly **one** branch runs.

---

# 🧪 PRACTICE 2 — WALLET

Create a program that asks for a wallet balance.

If the balance is greater than zero:

```text
Wallet has money.
```

Otherwise:

```text
Wallet is empty.
```

---

# 4️⃣ COMPARISON OPERATORS + `if`

Remember Batch 4?

You learned:

```text
==
!=
>
<
>=
<=
```

Now we're going to use them for decisions.

---

## Equal

```python
balance = 50000

if balance == 50000:
    print("Balance is exactly ₦50,000.")
```

---

## Greater than

```python
balance = 70000

if balance > 50000:
    print("Balance is above ₦50,000.")
```

---

## Less than

```python
balance = 30000

if balance < 50000:
    print("Balance is below ₦50,000.")
```

---

## Greater than or equal

```python
balance = 50000

if balance >= 50000:
    print("Balance meets the minimum.")
```

---

# 🧪 PRACTICE 3

Create:

```python
price = 5000
```

Write conditions that check:

```text
price is greater than 3000
price is less than 10000
price is exactly 5000
price is not 2000
```

Print a different message for each.

---

# 5️⃣ `if` + INPUT

Now things get more interesting.

```python
name = input("Enter your name: ")
balance = float(input("Enter your balance: "))

if balance > 0:
    print(f"{name}, your wallet has money.")
```

Your program is now:

```text
INPUT
 ↓
PROCESS
 ↓
DECISION
 ↓
OUTPUT
```

That's a major step forward.

---

# 💰 WALLET EXAMPLE

```python
balance = float(input("Enter your wallet balance: "))

if balance > 0:
    print("You have money available.")
else:
    print("Your wallet is empty.")
```

Try:

```text
0
```

Then:

```text
50000
```

Then:

```text
-1000
```

Observe how the decision changes.

---

# 🧠 IMPORTANT

Python doesn't understand:

> "This looks like enough money."

It evaluates the exact expression:

```python
balance > 0
```

That expression produces:

```text
True
```

or:

```text
False
```

The conditional acts on that Boolean result.

---

# 6️⃣ `elif`

What if we have more than two possibilities?

For example:

```text
Balance > 100000
Balance > 50000
Balance > 0
Balance == 0
```

We can use `elif`.

```python
balance = 75000

if balance > 100000:
    print("High balance")
elif balance > 50000:
    print("Medium balance")
elif balance > 0:
    print("Low balance")
else:
    print("Empty wallet")
```

Python checks from top to bottom.

---

# 🧠 `if / elif / else`

Think:

```text
if
 ↓
"Is this true?"

if false
 ↓
elif
 ↓
"Is this true?"

if false
 ↓
another elif
 ↓
"Is this true?"

if everything is false
 ↓
else
```

Once Python finds a true condition, it executes that branch and skips the remaining branches.

---

# 🧪 PRACTICE 4

Create a program that asks for a score.

Use:

```text
90 or higher → Excellent
70–89        → Good
50–69        → Pass
Below 50     → Fail
```

Don't worry about school grading systems.

The goal is learning the decision structure.

---

# 7️⃣ ORDER MATTERS

Look carefully at this:

```python
score = 95

if score >= 50:
    print("Pass")
elif score >= 90:
    print("Excellent")
```

What happens?

The program prints:

```text
Pass
```

Why?

Because:

```python
score >= 50
```

is already `True`.

Python never reaches the `elif`.

---

# 🧠 CONDITIONAL ORDER

Python checks from:

```text
TOP
 ↓
DOWN
```

So put **more specific conditions before broader conditions** when necessary.

Correct:

```python
if score >= 90:
    print("Excellent")
elif score >= 50:
    print("Pass")
else:
    print("Fail")
```

---

# 🧪 PREDICTION CHALLENGE

Without running the code, what will it print?

```python
balance = 80000

if balance > 100000:
    print("A")
elif balance > 50000:
    print("B")
elif balance > 10000:
    print("C")
else:
    print("D")
```

Predict first.

Then test.

---

# 8️⃣ LOGICAL OPERATORS IN CONDITIONS

You already learned:

```text
and
or
not
```

Now you can use them inside decisions.

---

## `and`

```python
balance = 50000
withdrawal = 20000

if withdrawal <= balance and withdrawal > 0:
    print("Withdrawal is valid.")
```

Python checks both:

```text
withdrawal <= balance
```

and:

```text
withdrawal > 0
```

Both must be true.

---

# 💰 WALLET DECISION

```python
balance = 50000
withdrawal = 20000

if withdrawal <= balance and withdrawal > 0:
    print("Withdrawal can proceed.")
else:
    print("Invalid withdrawal.")
```

This is beginning to look like real wallet logic.

---

# `or`

```python
payment_method = input("Payment method: ")

if payment_method == "cash" or payment_method == "card":
    print("Payment method accepted.")
```

At least one condition must be true.

---

# `not`

```python
wallet_empty = False

if not wallet_empty:
    print("Wallet contains money.")
```

`not False` becomes `True`.

---

# 🧪 PRACTICE 5

Create:

```python
balance = 50000
withdrawal = 20000
```

Write a condition that says:

> Withdrawal is valid only if it is greater than zero **and** less than or equal to the balance.

---

# 9️⃣ NESTED `if`

Sometimes one decision leads to another decision.

Example:

```python
balance = 50000

if balance > 0:
    print("Wallet has money.")

    if balance >= 10000:
        print("Wallet meets the minimum balance.")
```

The second `if` is **inside** the first.

That's called a nested conditional.

---

# 🧠 MENTAL MODEL

```text
IF wallet has money
    ↓
    IF wallet has at least 10,000
        ↓
        do something
```

---

# ⚠️ DON'T OVER-NEST

Nested conditionals are useful, but too many levels can become difficult to read.

For example:

```python
if condition:
    if condition:
        if condition:
            if condition:
                ...
```

You don't want your code turning into a maze.

You'll learn cleaner ways to structure complex logic later.

For now, understand how nesting works.

---

# 🧪 PRACTICE 6

Create:

```python
balance = 50000
```

If the balance is greater than zero:

```text
Wallet is active.
```

Then, inside that condition, check whether the balance is at least `10000`.

If it is:

```text
Minimum balance requirement met.
```

---

# 🔟 CONDITIONS WITH STRINGS

Conditionals aren't only for numbers.

You can compare strings.

```python
name = input("Enter your name: ")

if name == "Chris":
    print("Welcome back.")
```

String comparisons are **case-sensitive**.

So:

```text
"Chris"
```

and:

```text
"chris"
```

are different strings.

---

# 🛒 STORE EXAMPLE

```python
product = input("Enter product name: ")

if product == "Laptop":
    print("Laptop selected.")
else:
    print("Different product selected.")
```

---

# 🧪 PRACTICE 7

Ask the user for a product name.

If they enter:

```text
Laptop
```

print:

```text
Laptop selected.
```

Otherwise print:

```text
Another product selected.
```

---

# 1️⃣1️⃣ MULTIPLE `elif` CONDITIONS

Let's build a store discount system.

```python
total = float(input("Enter total: "))

if total >= 100000:
    print("Large purchase")
elif total >= 50000:
    print("Medium purchase")
elif total >= 10000:
    print("Small purchase")
else:
    print("Very small purchase")
```

Again, Python evaluates from top to bottom.

---

# 🛒 PRACTICE 8

Build a simple shipping classification:

```text
Order >= 100000 → Large order
Order >= 50000  → Medium order
Order >= 10000  → Small order
Otherwise       → Basic order
```

---

# 1️⃣2️⃣ BOOLEAN VARIABLES

Remember:

```python
can_withdraw = withdrawal <= balance
```

Now you can use that variable directly.

```python
if can_withdraw:
    print("Withdrawal allowed.")
else:
    print("Withdrawal denied.")
```

This is extremely readable.

---

# 🧠 WHY THIS IS GOOD

Compare:

```python
if withdrawal <= balance and withdrawal > 0:
    print("Allowed")
```

with:

```python
can_withdraw = withdrawal <= balance and withdrawal > 0

if can_withdraw:
    print("Allowed")
```

The second version gives the condition a meaningful name.

That makes your program easier to understand.

---

# 🧪 PRACTICE 9

Create:

```python
balance = 50000
withdrawal = 20000
```

Then create:

```python
can_withdraw
```

using a Boolean expression.

Finally use `if/else` with `can_withdraw`.

---

# 🐛 DEBUGGING LAB

## Bug #1 — Assignment Instead of Comparison

```python
balance = 50000

if balance = 50000:
    print("Correct")
```

What's wrong?

Remember the difference between:

```text
=
==
```

---

# Bug #2 — Missing Colon

```python
if balance > 0
    print("Money available")
```

Find the syntax problem.

---

# Bug #3 — Indentation

```python
balance = 50000

if balance > 0:
print("Money available")
```

What's wrong?

---

# Bug #4 — Wrong Order

```python
score = 95

if score >= 50:
    print("Pass")
elif score >= 90:
    print("Excellent")
```

Why doesn't `"Excellent"` appear?

---

# Bug #5 — Wrong Logic

```python
balance = 50000
withdrawal = 60000

if withdrawal > balance:
    print("Withdrawal allowed")
else:
    print("Withdrawal denied")
```

The program runs.

But the logic is backwards.

Fix it.

---

# 🧠 DEEP THINKING CHALLENGE

Consider:

```python
balance = 50000
withdrawal = 20000

can_withdraw = withdrawal <= balance and withdrawal > 0

if can_withdraw:
    balance -= withdrawal
    print(f"Withdrawal successful. Balance: {balance}")
else:
    print("Withdrawal failed.")
```

Explain the entire flow in your own words.

Start from:

```text
balance = 50000
```

and trace what happens.

Don't just describe the final answer.

Explain:

```text
value
 ↓
expression
 ↓
Boolean result
 ↓
decision
 ↓
action
 ↓
new value
```

This is an important programming skill.

---

# 💰 MINI-PROJECT — WALLET WITH WITHDRAWAL

Build an interactive wallet withdrawal program.

## Input

Ask for:

```text
Current balance
Withdrawal amount
```

## Rules

A withdrawal is valid only when:

```text
withdrawal > 0
```

and:

```text
withdrawal <= balance
```

If valid:

```text
subtract the withdrawal
display the new balance
```

Otherwise:

```text
display an appropriate error message
```

### Example

```text
Enter balance: 50000
Enter withdrawal: 20000

Withdrawal successful.
Remaining balance: ₦30,000.00
```

Test at least these cases:

```text
Withdrawal smaller than balance
Withdrawal equal to balance
Withdrawal greater than balance
Withdrawal of 0
```

---

# 🛒 MINI-PROJECT — STORE DISCOUNT ENGINE

Build a simple store discount calculator.

Ask the user for:

```text
Product name
Price
Quantity
```

Calculate:

```text
subtotal
```

Then apply a discount based on the subtotal.

Use your own sensible thresholds.

For example:

```text
subtotal >= 100000 → 10% discount
subtotal >= 50000  → 5% discount
otherwise          → 0%
```

Then calculate:

```text
discount
total
```

Display a clean receipt.

### Important

The discount must be **calculated by the program**.

Don't manually type the discount amount.

---

# 🧠 CHALLENGE — THREE-WAY WALLET STATUS

Ask for:

```text
balance
```

Then classify the wallet:

```text
balance > 100000
    → High balance

balance > 0
    → Active balance

balance == 0
    → Empty wallet

balance < 0
    → Invalid balance
```

Be careful about the order of your conditions.

---

# ⚔️ HARD CHALLENGE — TRANSACTION VALIDATOR

Ask the user for:

```text
balance
transaction_amount
```

Then determine:

```text
Is the transaction amount positive?
Is it affordable?
Is the balance sufficient?
```

Create meaningful Boolean variables such as:

```python
is_positive
has_sufficient_balance
can_transact
```

Then use those values to determine whether the transaction should proceed.

---

# 👹 BOSS FIGHT — "THE WALLET DECISION ENGINE"

We're upgrading your Wallet App.

Build a program that asks for:

```text
Customer name
Current balance
Transaction type
Transaction amount
```

The transaction type can be:

```text
deposit
withdraw
```

Your program should make decisions.

---

## Deposit

If the user selects:

```text
deposit
```

and the amount is greater than zero:

```text
Add the amount to the balance.
```

---

## Withdrawal

If the user selects:

```text
withdraw
```

the withdrawal should only happen when:

```text
amount > 0
```

and:

```text
amount <= balance
```

Otherwise reject it.

---

## Invalid transaction

If the user enters something other than:

```text
deposit
withdraw
```

display an appropriate message.

---

## Final output

Display:

```text
Customer
Transaction type
Transaction amount
Transaction status
Final balance
```

---

# 🚨 BOSS FIGHT RESTRICTIONS

You may use everything from Batches 1–7.

That includes:

```text
Variables
Operators
Input
Output
Strings
F-strings
Conditionals
```

But you are **not yet allowed to use loops**.

So:

```python
for
while
```

are still locked. 🔒

Also don't use:

```python
def
```

Functions come later.

---

# 🧠 BOSS FIGHT BONUS

After completing the basic version, improve your program.

Add decisions for:

```text
Amount is zero
Amount is negative
Withdrawal exceeds balance
Unknown transaction type
Valid deposit
Valid withdrawal
```

Make your messages clear.

---

# 🧪 COMPREHENSION CHECK

Answer these without looking back.

### 1.

What is a conditional?

### 2.

What does `if` do?

### 3.

What does `else` do?

### 4.

What does `elif` do?

### 5.

Why is the colon required?

```python
if balance > 0:
```

### 6.

Why is indentation important in Python?

### 7.

What happens when an `if` condition is `False` and there is no `else`?

### 8.

What happens when an `if` condition is `False` but an `elif` condition is `True`?

### 9.

What is a nested conditional?

### 10.

Why does the order of `if` and `elif` conditions matter?

### 11.

What does this produce?

```python
withdrawal <= balance
```

### 12.

Why can a Boolean variable be useful?

---

# 🧠 TRACE THIS PROGRAM

Don't run it immediately.

Predict what happens:

```python
balance = 70000
withdrawal = 50000

if withdrawal > 0 and withdrawal <= balance:
    balance -= withdrawal
    print("Approved")
else:
    print("Denied")

print(balance)
```

Write down:

```text
Condition:
True/False:
Branch:
New balance:
Output:
```

Then run it.

---

# 🥋 PROFESSIONAL MINDSET

You've just crossed an important line.

Before conditionals, your programs mostly did this:

```text
Input
 ↓
Calculation
 ↓
Output
```

Now they can do:

```text
Input
 ↓
Calculation
 ↓
Decision
 ↓
Action
 ↓
Output
```

That is the beginning of **program logic**.

And program logic is one of the most important foundations you'll ever develop.

Don't rush through this topic.

When you eventually work with:

```text
Machine Learning
Neural Networks
AI Agents
APIs
Data Pipelines
Automation
```

you will still be writing logic.

The syntax gets more advanced.

The fundamental thinking remains.

---

# 🚨 ONE HABIT TO DEVELOP

Whenever you write a conditional, say it in plain English first.

Instead of immediately writing:

```python
if withdrawal > 0 and withdrawal <= balance:
```

think:

> "If the withdrawal is positive AND the wallet has enough money..."

Then translate that sentence into Python.

This habit will make increasingly complex logic much easier to construct.

---

# 💰 CONNECTION TO YOUR WALLET APP

You now have the tools to begin implementing actual wallet rules:

```text
Deposit
   ↓
Is amount valid?
   ↓
YES → Add money
NO  → Reject

Withdrawal
   ↓
Is amount positive?
   ↓
Does balance cover it?
   ↓
YES → Withdraw
NO  → Reject
```

Your wallet is beginning to behave like an actual application rather than a calculator.

---

# 🛒 CONNECTION TO YOUR TERMINAL STORE

Your store can now make decisions:

```text
Customer enters quantity
        ↓
Is quantity valid?
   ↓          ↓
 YES         NO
  ↓           ↓
Calculate   Reject
```

And:

```text
Subtotal
   ↓
Is subtotal large enough?
   ↓
YES → Apply discount
NO  → No discount
```

This is the beginning of the checkout logic you'll eventually expand.

---

# 📈 BATCH 7 EXIT CRITERIA

Before declaring Batch 7 complete, you should be able to:

* [ ] Explain what conditionals are
* [ ] Use `if`
* [ ] Use `else`
* [ ] Use `elif`
* [ ] Use comparison operators in conditions
* [ ] Use `and` in conditions
* [ ] Use `or` in conditions
* [ ] Use `not` in conditions
* [ ] Explain Boolean conditions
* [ ] Understand indentation
* [ ] Understand the colon after a condition
* [ ] Build nested conditionals
* [ ] Order `elif` conditions correctly
* [ ] Use Boolean variables in conditions
* [ ] Debug conditional syntax errors
* [ ] Debug conditional logic errors
* [ ] Build a wallet withdrawal validator
* [ ] Build a store discount engine
* [ ] Complete the Wallet Decision Engine Boss Fight

---

# 📝 GROWTH LOG

```text
## Batch 7 — Growth Log

### 🧠 What clicked?
-

### 🥴 What challenged me?
-

### 🏆 Which exercise am I most proud of?
-

### 🐛 What conditional bug taught me something?
-

### 👨‍🏫 Could I explain if, elif, and else without looking?
-

### 🔁 What do I need to revise?
-

### 🚀 What can my programs decide now that they couldn't decide before?
-
```

---

# 🗺️ PART 1 PROGRESS

```text
PART 1 — PYTHON FOUNDATIONS

[✅] Batch 1 — Programming & Python Basics
[✅] Batch 2 — Core Python Foundations
[✅] Batch 3 — Variables & Assignment
[✅] Batch 4 — Operators & Expressions
[✅] Batch 5 — Input & Output
[✅] Batch 6 — Strings
[🔥] Batch 7 — Conditionals
[🔒] Batch 8 — Loops

            ↓

      🐉 PART 1 BOSS FIGHT
```

---

# 🥋 SENSEI'S FINAL WORD

Look at the evolution:

```text
Batch 3
Variables
    ↓
"I can store information."

Batch 4
Operators
    ↓
"I can process information."

Batch 5
Input & Output
    ↓
"I can communicate with the user."

Batch 6
Strings
    ↓
"I can work with text."

Batch 7
Conditionals
    ↓
"I can make decisions."
```

Next comes a major power-up:

# 🔁 LOOPS

You'll teach Python:

> **"Don't just do this once. Keep doing it."**

That's when your Terminal Store can start repeatedly accepting transactions.

That's when your programs stop being one-shot scripts and start behaving like **systems**.

But first:

**Complete Batch 7. Fight the Boss Fight. Break your code. Fix it. Rebuild it.**

Then we'll unlock the final major foundation of Part 1:

## 🐍 Batch 8 — Loops.
