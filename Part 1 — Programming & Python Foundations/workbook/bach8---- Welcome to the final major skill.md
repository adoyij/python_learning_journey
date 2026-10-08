# 🐍 BATCH 8 — LOOPS

> 😎 Apprentice, you've learned how to make Python **decide**.
>
> Now we're teaching it how to **repeat**.
>
> Welcome to the final major skill of Part 1:
>
> # 🔁 LOOPS
>
> This is where your programs stop saying:
>
> > “Do this one time.”
>
> and start saying:
>
> > **“Keep doing this until the job is done.”** 😤

---

# 🎯 BATCH 8 MISSION

By the end of this batch, you should be able to:

* Understand why loops exist
* Use `for` loops
* Use `while` loops
* Understand `range()`
* Repeat calculations
* Track totals with accumulator variables
* Use counters
* Loop through strings
* Use `break`
* Use `continue`
* Avoid infinite loops
* Debug loop logic
* Build repeated wallet and store operations
* Know when to use `for` vs `while`

---

# 🧠 1. WHY DO WE NEED LOOPS?

Imagine you want to print:

```text
Welcome
Welcome
Welcome
Welcome
Welcome
```

Without a loop:

```python
print("Welcome")
print("Welcome")
print("Welcome")
print("Welcome")
print("Welcome")
```

That's ugly. 😭

A loop lets Python repeat the instruction:

```python
for number in range(5):
    print("Welcome")
```

Much better.

The mental model:

```text
LOOP

Start
  ↓
Do something
  ↓
Check whether to continue
  ↓
Repeat
  ↓
Stop
```

---

# 🔁 2. THE `for` LOOP

The basic structure:

```python
for variable in something:
    action
```

Example:

```python
for number in range(5):
    print(number)
```

Output:

```text
0
1
2
3
4
```

Notice something important:

> `range(5)` stops **before** 5.

---

# 🔢 3. `range()`

`range()` is one of your most important loop tools.

## `range(stop)`

```python
for number in range(5):
    print(number)
```

Output:

```text
0
1
2
3
4
```

---

## `range(start, stop)`

```python
for number in range(1, 6):
    print(number)
```

Output:

```text
1
2
3
4
5
```

Again:

```text
start → included
stop  → excluded
```

---

## `range(start, stop, step)`

```python
for number in range(2, 11, 2):
    print(number)
```

Output:

```text
2
4
6
8
10
```

The `step` controls how much the number changes each time.

---

# 🧪 PRACTICE 1 — COUNTING

Write a program that prints:

```text
1
2
3
4
5
6
7
8
9
10
```

Use a `for` loop.

---

# 🧪 PRACTICE 2 — WALLET TRANSACTION NUMBERS

Print:

```text
Transaction 1
Transaction 2
Transaction 3
Transaction 4
Transaction 5
```

Use:

```python
range()
```

---

# 🧪 PRACTICE 3 — EVEN NUMBERS

Print all even numbers from `2` to `20`.

Expected:

```text
2
4
6
8
10
12
14
16
18
20
```

---

# 🧠 4. THE LOOP VARIABLE

Look at:

```python
for number in range(5):
    print(number)
```

`number` changes during every iteration.

Think:

```text
iteration 1 → number = 0
iteration 2 → number = 1
iteration 3 → number = 2
iteration 4 → number = 3
iteration 5 → number = 4
```

The loop variable is simply the value Python is currently working with.

---

# 🏦 5. LOOPS + WALLET

Suppose we want to display five transaction numbers:

```python
for transaction in range(1, 6):
    print(f"Transaction {transaction}")
```

Output:

```text
Transaction 1
Transaction 2
Transaction 3
Transaction 4
Transaction 5
```

This becomes useful when your wallet starts handling multiple transactions.

---

# 🧠 6. ACCUMULATORS

Now things get interesting.

Suppose we want to calculate:

```text
1 + 2 + 3 + 4 + 5
```

We can create a variable that keeps the running total.

```python
total = 0

for number in range(1, 6):
    total += number

print(total)
```

Output:

```text
15
```

The important idea:

```text
total = 0

total += 1
total += 2
total += 3
total += 4
total += 5
```

The variable `total` **accumulates** values.

---

# 🧠 THE ACCUMULATOR PATTERN

Memorize this pattern:

```python
total = 0

for value in values:
    total += value
```

This pattern will become extremely important later when working with:

* Data
* Machine learning
* Statistics
* AI datasets
* Financial calculations

---

# 🏪 7. STORE TOTAL

Imagine a store has five products:

```text
2000
3500
1500
5000
2500
```

For now, we can represent those values simply:

```python
prices = [2000, 3500, 1500, 5000, 2500]
```

Then:

```python
total = 0

for price in prices:
    total += price

print(total)
```

Output:

```text
14500
```

Don't worry about mastering lists yet.

We're using this simple example to understand **iteration**.

---

# 🧪 PRACTICE 4 — STORE TOTAL

Given:

```python
prices = [1000, 2500, 3000, 1500]
```

Use a loop to calculate the total.

Do **not** manually add them.

---

# 🔢 8. COUNTERS

An accumulator adds values.

A counter counts things.

Example:

```python
count = 0

for number in range(1, 6):
    count += 1

print(count)
```

Output:

```text
5
```

Mental model:

```text
count = 0

loop → +1
loop → +1
loop → +1
loop → +1
loop → +1

count = 5
```

---

# 🧪 PRACTICE 5 — COUNT TRANSACTIONS

Create a program that loops through five transactions and counts how many transactions were processed.

Expected output:

```text
Transactions processed: 5
```

---

# 🔤 9. LOOPING THROUGH A STRING

A `for` loop can also go through a string.

```python
name = "Wallet"

for letter in name:
    print(letter)
```

Output:

```text
W
a
l
l
e
t
```

Python processes one character at a time.

---

# 🧪 PRACTICE 6 — CUSTOMER NAME

Ask the user for their name.

Then print every character on a separate line.

Example:

```text
Enter your name: Alex
```

Output:

```text
A
l
e
x
```

---

# 🔄 10. THE `while` LOOP

Now we meet the second major loop.

`for` is usually useful when you know how many times you want to repeat something.

`while` is useful when you want to repeat something **while a condition remains true**.

Basic structure:

```python
while condition:
    action
```

Example:

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output:

```text
1
2
3
4
5
```

---

# ⚠️ CRITICAL RULE

A `while` loop must eventually become false.

Look at:

```python
count = 1

while count <= 5:
    print(count)
```

What's missing?

`count` never changes.

Therefore:

```text
count = 1
count = 1
count = 1
count = 1
...
```

The loop never ends.

That's an:

# 🚨 INFINITE LOOP

---

# 🧠 WHILE LOOP MENTAL MODEL

```text
Start
  ↓
Check condition
  ↓
True?
 ├── YES → execute code → update state → check again
 └── NO  → stop
```

---

# 🧪 PRACTICE 7 — COUNTDOWN

Create a `while` loop that prints:

```text
5
4
3
2
1
```

---

# 🏦 11. WALLET + `while`

Imagine a wallet application that keeps processing transactions while the user has not chosen to stop.

Conceptually:

```python
transaction = "yes"

while transaction == "yes":
    print("Processing transaction...")
    transaction = input("Continue? yes/no: ")
```

This is the beginning of interactive programs that keep running until a condition changes.

---

# 🧪 PRACTICE 8 — CONTINUE SHOPPING

Create a program that repeatedly asks:

```text
Do you want to continue shopping? yes/no:
```

As long as the user enters:

```text
yes
```

print:

```text
Continuing shopping...
```

When they enter:

```text
no
```

print:

```text
Shopping finished.
```

---

# 🛑 12. `break`

Sometimes you want to stop a loop immediately.

That's what `break` does.

Example:

```python
for number in range(1, 11):
    if number == 6:
        break

    print(number)
```

Output:

```text
1
2
3
4
5
```

When:

```python
number == 6
```

Python immediately leaves the loop.

---

# 🧠 BREAK

Think:

```text
Loop
 ↓
Condition?
 ↓
BREAK!
 ↓
EXIT LOOP
```

---

# 🏦 WALLET EXAMPLE

```python
for transaction in range(1, 11):
    if transaction == 6:
        break

    print(f"Processing transaction {transaction}")
```

Only the first five transactions are processed.

---

# 🧪 PRACTICE 9 — STOP PROCESSING

Loop from `1` to `10`.

Stop the loop when the number reaches `7`.

Expected:

```text
1
2
3
4
5
6
```

---

# ⏭️ 13. `continue`

`continue` is different from `break`.

`break`:

> Stop the entire loop.

`continue`:

> Skip this iteration and move to the next one.

Example:

```python
for number in range(1, 6):
    if number == 3:
        continue

    print(number)
```

Output:

```text
1
2
4
5
```

The loop didn't stop.

It simply skipped `3`.

---

# 🧠 BREAK VS CONTINUE

```text
break
↓
STOP EVERYTHING
```

```text
continue
↓
SKIP THIS ONE
↓
KEEP GOING
```

---

# 🧪 PRACTICE 10 — SKIP ZERO

Loop from `0` to `5`.

Skip `0`.

Print the remaining numbers.

---

# 🏪 14. STORE: SKIP INVALID PRICES

Imagine a store has:

```python
prices = [2000, -500, 3000, 0, 1500]
```

Negative or zero prices should not be added.

You can use:

```python
total = 0

for price in prices:
    if price <= 0:
        continue

    total += price

print(total)
```

The invalid values are skipped.

---

# 🧪 PRACTICE 11 — VALID STORE PRICES

Given:

```python
prices = [1000, -200, 3000, 0, 2500, -500]
```

Use a loop and `continue` to calculate the total of valid prices only.

---

# 🧠 15. NESTED LOOPS

A loop can contain another loop.

Example:

```python
for outer in range(1, 4):
    for inner in range(1, 4):
        print(outer, inner)
```

Output:

```text
1 1
1 2
1 3
2 1
2 2
2 3
3 1
3 2
3 3
```

Don't worry if this feels strange.

Nested loops become very important later in:

* Data processing
* Matrices
* Neural networks
* Search algorithms
* AI systems

For now, understand the basic idea:

> One loop runs another loop.

---

# 🧪 PRACTICE 12 — PRODUCT OPTIONS

Use nested loops to print:

```text
Product 1 - Option 1
Product 1 - Option 2
Product 1 - Option 3
Product 2 - Option 1
Product 2 - Option 2
Product 2 - Option 3
Product 3 - Option 1
Product 3 - Option 2
Product 3 - Option 3
```

---

# 🧠 16. FOR VS WHILE

This distinction matters.

## Use `for` when:

You know what you're iterating over or roughly how many repetitions you need.

Examples:

```python
for number in range(10):
```

```python
for price in prices:
```

```python
for letter in name:
```

---

## Use `while` when:

You want to continue based on a condition.

Example:

```python
while balance > 0:
```

or:

```python
while choice != "quit":
```

---

# 🧠 SIMPLE RULE

Remember:

```text
FOR
→ repeat through a sequence/range
```

```text
WHILE
→ repeat while a condition is true
```

---

# 🐞 17. DEBUGGING LAB

Your job is to find the problems.

## Bug #1

```python
for number in range(5)
    print(number)
```

What's wrong?

---

## Bug #2

```python
count = 1

while count <= 5:
    print(count)
```

Why doesn't this program stop?

---

## Bug #3

```python
for number in range(1, 6):
    if number == 3:
        break

    print(number)

print("Finished")
```

Is this code actually broken?

Or is it behaving correctly?

Explain the output.

---

## Bug #4

```python
total = 0

for price in [1000, 2000, 3000]:
    total = price

print(total)
```

The expected answer is:

```text
6000
```

But the program prints:

```text
3000
```

Why?

Fix it.

---

# 🧠 18. LOOP TRACING

You need to learn how to mentally execute loops.

Consider:

```python
total = 0

for number in range(1, 4):
    total += number

print(total)
```

Trace it:

```text
Start:
total = 0

number = 1
total = 1

number = 2
total = 3

number = 3
total = 6
```

Final:

```text
6
```

---

# 🧪 TRACE CHALLENGE

Without running the code, determine the output:

```python
total = 10

for number in range(1, 4):
    total += number * 2

print(total)
```

Show your working.

---

# 🧪 19. MEDIUM CHALLENGE — WALLET DEPOSITS

Create:

```text
balance = 0
```

Then process these deposits:

```text
10000
5000
15000
7000
```

Use a loop.

Expected:

```text
Final balance: 37000
```

Do not manually add the deposits.

---

# 🧪 20. MEDIUM CHALLENGE — STORE CHECKOUT

Given:

```python
prices = [2000, 3500, 1500, 5000]
```

Use a loop to calculate:

```text
Subtotal
```

Then apply:

```text
10% discount
```

Then display:

```text
Subtotal
Discount
Final Total
```

---

# 🧪 21. HARD CHALLENGE — TRANSACTION COUNTER

Given:

```python
transactions = [5000, -2000, 3000, -1000, 7000]
```

Build a program that calculates:

* Total deposits
* Total withdrawals
* Number of deposits
* Number of withdrawals

Hint:

Positive numbers represent deposits.

Negative numbers represent withdrawals.

Your program should produce something similar to:

```text
Total deposits: 15000
Total withdrawals: 3000
Number of deposits: 3
Number of withdrawals: 2
```

---

# 🏦 MINI-PROJECT 1 — WALLET TRANSACTION SUMMARY

Build a program using:

```python
transactions = [10000, -3000, 5000, -2000, 7000]
```

Your program should calculate:

```text
Starting Balance: 0
Total Deposits: ...
Total Withdrawals: ...
Final Balance: ...
```

Rules:

* Positive values = deposits
* Negative values = withdrawals
* Use a loop
* Use an accumulator
* Use conditionals
* Do not manually calculate the totals

### Bonus

Also count:

```text
Number of deposits
Number of withdrawals
```

---

# 🏪 MINI-PROJECT 2 — TERMINAL STORE CHECKOUT

Build a simple checkout program.

Start with:

```python
prices = [2500, 4000, 1500, 3000, 5000]
```

Your program must:

1. Loop through the prices.
2. Calculate the subtotal.
3. Count the number of products.
4. Apply a discount.

Discount rules:

```text
Subtotal >= 15000 → 10% discount
Subtotal >= 10000 → 5% discount
Otherwise → no discount
```

Display:

```text
Products: ...
Subtotal: ₦...
Discount: ₦...
Final Total: ₦...
```

This combines:

```text
Variables
+
Operators
+
Strings
+
Conditionals
+
Loops
```

🔥 That's your Part 1 skill stack coming together.

---

# 🐉 BOSS FIGHT — THE WALLET TRANSACTION PROCESSOR

Alright apprentice.

This is the big one.

No copying previous solutions.

Build it yourself.

## 🎯 Mission

Create a wallet transaction processor that processes multiple transactions.

Start with:

```python
balance = 50000
transactions = [10000, -5000, -70000, 15000, -10000]
```

Rules:

### Positive transaction

Treat it as a deposit.

```text
balance increases
```

### Negative transaction

Treat it as a withdrawal.

But:

```text
withdrawal cannot exceed balance
```

If a withdrawal is greater than the current balance:

```text
reject it
```

---

## Your program must calculate:

```text
Starting balance
Number of deposits
Total deposited
Number of withdrawals
Total withdrawn
Rejected withdrawals
Final balance
```

---

## Example structure

Your output should look something like:

```text
===== WALLET REPORT =====

Starting Balance: ₦50000
Deposits: 2
Total Deposited: ₦25000
Withdrawals: 2
Total Withdrawn: ₦15000
Rejected Withdrawals: 1

Final Balance: ₦60000
```

The exact values should come from your program.

---

# 🔥 BOSS FIGHT RULES

You may use:

```python
for
while
range()
if
elif
else
break
continue
```

You may use:

```python
lists
strings
variables
operators
```

But:

🚫 No functions yet.

Do not use:

```python
def
```

Functions are coming in the next Part.

---

# 💀 BONUS BOSS

Add a transaction report.

For every transaction, print something like:

```text
Deposit: ₦10000 → Accepted
Withdrawal: ₦5000 → Accepted
Withdrawal: ₦70000 → Rejected
Deposit: ₦15000 → Accepted
Withdrawal: ₦10000 → Accepted
```

Now you're building something that actually resembles a tiny financial processing system.

---

# 🧠 COMPREHENSION CHECK

Answer these without looking back.

### 1.

Why do programmers use loops?

### 2.

What is the difference between:

```python
for
```

and:

```python
while
```

### 3.

What does this produce?

```python
range(5)
```

### 4.

Why does `range(1, 6)` produce 1 through 5 instead of 1 through 6?

### 5.

What is an accumulator?

### 6.

What is a counter?

### 7.

What does `break` do?

### 8.

What does `continue` do?

### 9.

What causes an infinite `while` loop?

### 10.

What is wrong with:

```python
total = 0

for price in prices:
    total = price
```

if we want the sum of all prices?

### 11.

Explain this in plain English:

```python
while balance > 0:
    balance -= 1000
```

### 12.

Trace this:

```python
total = 0

for number in range(1, 5):
    total += number

print(total)
```

---

# 🧠 THE PROFESSIONAL MINDSET

You are now moving from:

```text
Input
↓
Process
↓
Decision
↓
Output
```

to:

```text
Input
↓
Process
↓
Decision
↓
Repeat
↓
Process
↓
Decision
↓
Repeat
↓
Output
```

That's a major programming milestone.

Loops allow your programs to work with **many pieces of data**, not just one.

And that matters enormously for AI.

AI systems constantly process:

```text
many examples
many numbers
many records
many tokens
many predictions
many iterations
```

You are learning the basic computational pattern behind all of that.

---

# 🏁 BATCH 8 EXIT CRITERIA

You are ready to leave Batch 8 when you can confidently:

* [ ] Explain why loops exist
* [ ] Write a `for` loop
* [ ] Write a `while` loop
* [ ] Use `range()`
* [ ] Explain start/stop/step
* [ ] Iterate through strings
* [ ] Iterate through simple collections
* [ ] Build accumulators
* [ ] Build counters
* [ ] Use `break`
* [ ] Use `continue`
* [ ] Identify infinite loops
* [ ] Debug loop errors
* [ ] Trace loops manually
* [ ] Build a wallet transaction processor
* [ ] Build a store checkout using loops

---

# 📈 PART 1 — FINAL STRETCH

Your journey now looks like:

```text
PART 1 — PYTHON FOUNDATIONS

[✅] Batch 1 — Programming & Python Basics
[✅] Batch 2 — Core Python Foundations
[✅] Batch 3 — Variables & Assignment
[✅] Batch 4 — Operators & Expressions
[✅] Batch 5 — Input & Output
[✅] Batch 6 — Strings
[🔥] Batch 7 — Conditionals
[🔥] Batch 8 — Loops

             ↓
      🐉 PART 1 BOSS FIGHT
             ↓
      🧠 PART 1 SKILL CHECK
             ↓
      🚀 PART 2 — FUNCTIONS
```

---

# 📝 GROWTH LOG

After completing Batch 8, record:

```text
## Batch 8 Growth Log

### What clicked?

### What confused me?

### Which loop exercise was easiest?

### Which loop exercise was hardest?

### Did I understand for vs while?

### Can I explain break vs continue?

### Did I encounter an infinite loop?

### What did debugging teach me?

### Which project am I most proud of?

### What can my programs do now that they couldn't do before?

### Confidence Score
__/10
```

---

# 🥋 FINAL SENSEI NOTE

Apprentice...

You've now learned the core building blocks of procedural Python:

```text
Variables
   ↓
Operators
   ↓
Input / Output
   ↓
Strings
   ↓
Conditionals
   ↓
Loops
```

Once you finish this batch, **Part 1 is essentially complete**.

Then we stop treating Python as isolated commands.

We'll start teaching you how to build **reusable pieces of logic**.

That's where:

# ⚔️ FUNCTIONS

enter the dojo.

But first...

**Finish Batch 8.**

Then come back with:

> **“I'm done with Batch 8 and the Boss Fight.”**

And we'll unlock the **Part 1 Boss Fight + Skill Check** before moving into Part 2. 🐍🔥


















resources = [
  {"id": "R001", "name": "Laptop", "category": "Electronics", "total": 10, "available": 10},
  {"id": "R002", "name": "Keyboard", "category": "Accessories", "total": 5, "available": 5},
  {"id": "R003", "name": "Headset", "category": "Accessories", "total": 3, "available": 3}
]
fellows = {"F001": "Ada", "F002": "John", "F003": "Grace"}
borrow_records = []

REQUIRED DEMONSTRATION, IN ORDER:
1. F001 borrows 2 laptops — available laptop units = 8.
2. F002 borrows 3 keyboards — available keyboard units = 2.
3. F001 returns 1 laptop — available laptop units = 9.
4. F003 requests 4 headsets — rejected without changing stock.
5. F002 tries to return 4 keyboards — rejected without changing stock.
6. Search for LAPtop — find Laptop, ignoring case.
7. Generate the report — overall units 18, available 14, borrowed 4, Keyboard low stock (2); Keyboard is most borrowed (3).

Optional bonus, maximum 5 bonus marks outside 100: persist and reload inventory and loans using JSON.