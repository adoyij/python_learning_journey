# 🐍 PYTHON JOURNEY — BATCH 5

## Part 1 — Python Foundations

### Topic: **Input & Output**

> 😎 Alright, apprentice.
> Batch 4 taught your programs how to **work with information**.
>
> But so far, your programs have mostly been given information directly inside the code.
>
> That's about to change.
>
> We're opening the door between **your program and the outside world.** 🚪🐍
>
> The user will finally be able to talk to your program.
>
> Welcome to **Input & Output.**

---

# 🎯 BATCH 5 MISSION

By the end of this batch, you should understand how Python:

* Displays information with `print()`
* Receives information with `input()`
* Understands that `input()` returns a string
* Converts input using `int()` and `float()`
* Combines input with variables
* Performs calculations using user input
* Formats output clearly
* Handles common input mistakes
* Builds interactive versions of your Wallet and Store programs

---

# 🗺️ WHERE YOU ARE

```text
PART 1 — PYTHON FOUNDATIONS

[✅] Batch 1 — Programming & Python Basics
[✅] Batch 2 — Core Python Foundations
[✅] Batch 3 — Variables & Assignment
[✅] Batch 4 — Operators & Expressions
[🔥] Batch 5 — Input & Output
[🔒] Batch 6 — Strings
[🔒] Batch 7 — Conditionals
[🔒] Batch 8 — Loops

        ↓

PART 1 BOSS FIGHT
```

Notice the progression:

```text
Variables
   ↓
Operators
   ↓
Input
   ↓
Processing
   ↓
Output
```

This is becoming the basic anatomy of a real program.

---

# 🧠 THE BIG IDEA

A useful way to think about a program is:

```text
INPUT
  ↓
PROCESS
  ↓
OUTPUT
```

For example, your Store program:

```text
INPUT
price
quantity
discount

   ↓

PROCESS
subtotal = price × quantity
total = subtotal - discount

   ↓

OUTPUT
subtotal
total
```

You've already learned the **process**.

Now we're learning how information gets **into** and **out of** the program.

---

# 1️⃣ OUTPUT — `print()`

You've already used:

```python
print("Hello")
```

`print()` displays information to the user.

---

## Printing a variable

```python
balance = 50000

print(balance)
```

Output:

```text
50000
```

---

## Printing multiple values

```python
name = "Chris"
balance = 50000

print(name, balance)
```

Output:

```text
Chris 50000
```

Python separates the values with a space by default.

---

# 🧪 PRACTICE 1

Create:

```python
product_name = "Laptop"
price = 250000
quantity = 2
```

Print all three values.

Then create:

```python
balance = 500000
```

Print the balance.

---

# 2️⃣ PRINTING LABELS

This:

```python
print(balance)
```

works.

But:

```text
50000
```

doesn't tell the user what the number represents.

Better:

```python
print("Balance:", balance)
```

Output:

```text
Balance: 50000
```

This is much clearer.

---

# 🧠 OUTPUT SHOULD COMMUNICATE

Compare:

```python
print(65000)
```

with:

```python
print("New balance:", 65000)
```

The second one communicates meaning.

A program isn't only about getting the correct answer.

It's also about presenting the answer clearly.

---

# 3️⃣ `sep` — SEPARATING VALUES

Normally:

```python
print("Wallet", "Balance", 50000)
```

produces:

```text
Wallet Balance 50000
```

Python uses a space between values.

You can change that:

```python
print("Wallet", "Balance", 50000, sep=" | ")
```

Output:

```text
Wallet | Balance | 50000
```

This isn't something you need to memorize yet.

Just understand that `print()` can control how information is displayed.

---

# 4️⃣ `end`

Normally:

```python
print("Hello")
print("World")
```

Output:

```text
Hello
World
```

Each `print()` ends with a new line.

You can change that:

```python
print("Hello", end=" ")
print("World")
```

Output:

```text
Hello World
```

Again, don't obsess over this.

You'll encounter it occasionally.

---

# 5️⃣ INPUT — `input()`

Now the important part.

```python
name = input()
```

Python pauses.

It waits for the user to type something.

For example:

```text
Chris
```

Then Python stores:

```text
Chris
```

inside:

```python
name
```

---

# 🧠 THE BASIC PATTERN

```python
variable = input()
```

Think:

```text
User types something
        ↓
    input()
        ↓
   variable
```

---

# 6️⃣ ADDING A PROMPT

You usually don't want the user staring at a blank screen.

Instead:

```python
name = input("Enter your name: ")
```

The program displays:

```text
Enter your name:
```

The user types:

```text
Chris
```

Now:

```python
name
```

contains:

```text
"Chris"
```

---

# 🧪 PRACTICE 2

Create a program that asks the user for:

```text
Name
```

Then print:

```text
Hello, <name>
```

For example:

```text
Enter your name: Chris
Hello, Chris
```

---

# ⚠️ THE MOST IMPORTANT THING ABOUT `input()`

This catches almost every beginner.

Look at:

```python
age = input("Enter your age: ")
```

If the user enters:

```text
20
```

you might think:

```text
age = 20
```

But Python actually stores:

```text
"20"
```

That's a **string**.

Remember:

```text
20
```

and:

```text
"20"
```

are not the same thing.

---

# 🧠 WHY?

`input()` receives what the user **types**.

What the user types arrives as text.

So:

```python
age = input("Age: ")
```

means:

```text
age → string
```

regardless of whether the user typed:

```text
20
```

or:

```text
50000
```

or:

```text
3.14
```

---

# 🔥 TEST IT

Try:

```python
age = input("Enter your age: ")

print(age)
print(type(age))
```

If you enter:

```text
20
```

you should see something like:

```text
20
<class 'str'>
```

That second line is the key.

---

# 7️⃣ CONVERTING INPUT

If we need a number, we need to convert the input.

Python provides:

```python
int()
```

and:

```python
float()
```

---

# `int()`

`int()` converts something into an integer when the value is suitable for integer conversion.

Example:

```python
age = int(input("Enter your age: "))
```

Now if the user enters:

```text
20
```

Python converts it to:

```text
20
```

as an integer.

---

# 🧠 THE FLOW

This:

```python
age = int(input("Enter your age: "))
```

looks intimidating at first.

Break it apart:

### Step 1

```python
input("Enter your age: ")
```

User enters:

```text
20
```

Result:

```text
"20"
```

### Step 2

```python
int("20")
```

Result:

```text
20
```

### Step 3

```python
age = 20
```

That's all that's happening.

---

# 🧪 PRACTICE 3

Create a program that asks:

```text
Enter your age:
```

Convert the answer into an integer.

Then print:

```text
Your age is: <age>
```

Also print its type.

---

# 8️⃣ `float()`

Sometimes we need decimal numbers.

Example:

```python
price = float(input("Enter product price: "))
```

If the user enters:

```text
2500.50
```

Python produces:

```text
2500.5
```

as a float.

---

# 🧪 PRACTICE 4

Ask the user for:

```text
Product price
```

Convert it to a float.

Print the price and its type.

---

# 9️⃣ INPUT + OPERATORS

Now the real power begins.

Remember your Store calculator:

```python
price = 2000
quantity = 4

subtotal = price * quantity
```

Previously, the values were hard-coded.

Now:

```python
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

subtotal = price * quantity

print("Subtotal:", subtotal)
```

Now the user controls the calculation.

That's a real interactive program.

---

# 🛒 STORE EXERCISE

Build this yourself.

Your program should ask the user for:

```text
Product price
Quantity
```

Then calculate:

```text
Subtotal
```

Example:

```text
Enter price: 2000
Enter quantity: 4

Subtotal: 8000
```

---

# 1️⃣0️⃣ WALLET INPUT

Let's do the same with your Wallet App.

Instead of:

```python
balance = 50000
deposit = 15000
```

we can ask the user:

```python
balance = float(input("Enter current balance: "))
deposit = float(input("Enter deposit amount: "))
```

Then:

```python
balance += deposit
```

Finally:

```python
print("New balance:", balance)
```

Now the wallet responds to the user.

---

# 💰 WALLET EXERCISE

Build a program that asks for:

```text
Current balance
Deposit amount
```

Then calculates:

```text
New balance
```

Example:

```text
Enter current balance: 50000
Enter deposit amount: 15000

New balance: 65000
```

---

# 1️⃣1️⃣ MULTIPLE INPUTS

You can collect several pieces of information.

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
balance = float(input("Enter your balance: "))

print(name)
print(age)
print(balance)
```

Notice that each input has a different type.

```text
name    → str
age     → int
balance → float
```

---

# 🧠 TYPE IS PART OF THE DESIGN

Don't blindly convert everything to `int`.

Ask:

> "What kind of information is this?"

For example:

```text
Name       → str
Age        → int
Quantity    → int
Price       → float
Balance     → float
Product     → str
```

This is the beginning of thinking about **data correctly**.

---

# 🧪 PRACTICE 5 — CUSTOMER PROFILE

Create a program that asks for:

```text
Customer name
Customer age
Wallet balance
```

Then display all three.

Make sure the numeric values are converted properly.

---

# 1️⃣2️⃣ INPUT + CALCULATION

Let's build something slightly more realistic.

```python
price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))
discount = float(input("Enter discount: "))

subtotal = price * quantity
total = subtotal - discount

print("Subtotal:", subtotal)
print("Total:", total)
```

Notice the architecture:

```text
INPUT
 ↓
price
quantity
discount

 ↓

PROCESS
 ↓
subtotal
total

 ↓

OUTPUT
```

This pattern will follow you throughout your programming career.

---

# 🛒 MINI CHALLENGE

Upgrade the previous Store calculator.

Ask the user for:

```text
Product name
Price
Quantity
Discount
```

Then display:

```text
Product:
Subtotal:
Discount:
Total:
```

You should decide the appropriate type for every piece of information.

---

# 1️⃣3️⃣ STRING OUTPUT WITH F-STRINGS

You've already seen:

```python
print("Balance:", balance)
```

Python also supports a cleaner style:

```python
print(f"Balance: {balance}")
```

Example:

```python
name = "Chris"
balance = 50000

print(f"{name} has a balance of {balance}")
```

Output:

```text
Chris has a balance of 50000
```

---

# 🧠 THE F-STRING PATTERN

```python
f"some text {variable}"
```

The `f` tells Python:

> "I want to insert values into this string."

Example:

```python
price = 2000
quantity = 4

print(f"Price: {price}")
print(f"Quantity: {quantity}")
```

---

# 🧪 PRACTICE 6

Rewrite:

```python
print("Balance:", balance)
```

using an f-string.

Then rewrite:

```python
print("Subtotal:", subtotal)
```

using an f-string.

---

# 1️⃣4️⃣ FORMATTING DECIMAL MONEY

Suppose:

```python
balance = 50000.5
```

You may want:

```text
₦50,000.50
```

For now, don't worry about building a complete currency formatter.

But you can control decimal places with:

```python
print(f"{balance:.2f}")
```

Example:

```python
balance = 50000.5

print(f"{balance:.2f}")
```

Output:

```text
50000.50
```

The:

```text
:.2f
```

means:

> Display this float with 2 decimal places.

---

# 🧪 PRACTICE 7

Create:

```python
price = 2500.5
```

Print it with exactly two decimal places.

Then try:

```python
price = 2500.56789
```

Observe what happens.

---

# 1️⃣5️⃣ FORMATTING WITH COMMAS

You can also use:

```python
balance = 5000000

print(f"{balance:,}")
```

Output:

```text
5,000,000
```

Combined:

```python
balance = 5000000.5

print(f"{balance:,.2f}")
```

Output:

```text
5,000,000.50
```

This is especially useful for your wallet/store applications.

---

# 🧪 PRACTICE 8

Create:

```python
balance = 1250000.75
```

Display it with:

* commas
* two decimal places

---

# ⚠️ COMMON INPUT ERROR

Consider:

```python
age = int(input("Enter age: "))
```

If the user enters:

```text
twenty
```

Python cannot convert that text into an integer.

The program crashes with a conversion error.

You don't need to solve that yet.

**Exception handling comes later.**

For now, understand:

```text
input
  ↓
text
  ↓
conversion
  ↓
number
```

If the text isn't convertible to the requested type, Python raises an error.

---

# 🐛 DEBUGGING LAB

## Bug #1 — String Addition

What do you think this produces?

```python
price = input("Enter price: ")
quantity = input("Enter quantity: ")

total = price + quantity

print(total)
```

Suppose the user enters:

```text
2000
4
```

Will the result be:

```text
8000
```

or something else?

Explain why.

---

# Bug #2 — Fix the Calculation

The programmer wrote:

```python
price = input("Enter price: ")
quantity = input("Enter quantity: ")

subtotal = price * quantity
```

What's wrong?

Fix it.

---

# Bug #3 — Wrong Conversion

```python
quantity = float(input("Enter quantity: "))
```

Is `float` the best choice for a quantity such as:

```text
4
```

Why or why not?

---

# Bug #4 — Output Problem

The programmer wrote:

```python
balance = 50000

print("The current wallet balance is " + balance)
```

Why does this cause a problem?

How could you fix the output?

---

# 🧠 DEEP THINKING CHALLENGE

Consider:

```python
amount = input("Enter amount: ")
```

Answer:

### 1.

What type is `amount`?

### 2.

If the user enters `50000`, is it stored as a number or text?

### 3.

Why can't you safely assume that:

```python
amount * 2
```

means:

```text
100000
```

### 4.

How would you make `amount` numeric?

---

# 💰 MINI-PROJECT — WALLET DEPOSIT

Build a small interactive wallet program.

The program should ask the user for:

```text
Name
Current balance
Deposit amount
```

Then calculate the new balance.

Finally display something similar to:

```text
Customer: Chris
Previous balance: 50,000.00
Deposit: 15,000.00
New balance: 65,000.00
```

### Requirements

Use:

* `input()`
* `int()` or `float()` where appropriate
* Variables
* Arithmetic
* `print()`
* f-strings
* Number formatting

No `if`.

No loops.

No functions.

We're still building the foundation.

---

# 🛒 MINI-PROJECT — TERMINAL STORE RECEIPT

Now build a basic interactive store receipt.

Ask for:

```text
Product name
Price
Quantity
Discount
```

Calculate:

```text
subtotal = price × quantity
total = subtotal - discount
```

Then display a clean receipt.

For example:

```text
========================
       STORE RECEIPT
========================

Product: Keyboard
Price: ₦15,000.00
Quantity: 2
Subtotal: ₦30,000.00
Discount: ₦2,000.00
Total: ₦28,000.00

========================
```

You don't need to reproduce this exact design.

Make your own.

---

# ⚔️ HARD CHALLENGE — WALLET + STORE

Build one program that collects:

```text
Customer name
Wallet balance
Product price
Quantity
Discount
```

Calculate:

```text
subtotal
total
remaining wallet balance
```

For example:

```text
Wallet balance = 100,000
Product price = 20,000
Quantity = 3
Discount = 5,000
```

The program should calculate:

```text
Subtotal = 60,000
Total = 55,000
Remaining balance = 45,000
```

### Important

Don't manually calculate those values and print them.

The **program** must calculate them.

---

# 🧠 INPUT → PROCESS → OUTPUT CHALLENGE

For the previous project, explicitly identify:

### INPUT

What information comes from the user?

### PROCESS

What calculations happen?

### OUTPUT

What information does the program display?

Write this in your notes before coding.

This habit will become extremely valuable when programs become much larger.

---

# 🧪 COMPREHENSION CHECK

Answer these without looking back.

### 1.

What does `input()` do?

### 2.

What type does `input()` return?

### 3.

Why do we use:

```python
int()
```

### 4.

When would you use:

```python
float()
```

### 5.

What's the difference between:

```python
input("Price: ")
```

and:

```python
float(input("Price: "))
```

### 6.

What does `print()` do?

### 7.

What is an f-string?

### 8.

What does this do?

```python
f"{price:.2f}"
```

### 9.

What does this do?

```python
f"{balance:,}"
```

### 10.

What is the basic programming pattern we've been practicing?

```text
_____ → _____ → _____
```

---

# 👹 BOSS FIGHT — "THE INTERACTIVE CHECKOUT"

Time to combine everything.

Build a terminal checkout program from scratch.

## The program must ask for:

```text
Customer name
Wallet balance
Product name
Product price
Quantity
Discount
```

## It must calculate:

```text
Subtotal
Total
Remaining balance
```

## It must display:

```text
Customer
Product
Price
Quantity
Subtotal
Discount
Total
Remaining balance
```

### Requirements

You must use:

* `input()`
* Variables
* Appropriate type conversion
* Arithmetic operators
* Assignment operators where useful
* `print()`
* f-strings
* Number formatting

### Restrictions

Still **no**:

```python
if
else
elif
for
while
def
```

You're learning to construct the **data flow** first.

---

# 🥷 BOSS FIGHT — LEVEL UP

After your first version works, rebuild it.

This time:

### Version 1

Use straightforward `print()` statements.

### Version 2

Use f-strings.

### Version 3

Format monetary values with:

```text
commas
+
2 decimal places
```

The goal isn't merely to make it work.

The goal is to make the output increasingly clear.

---

# 🧠 PROFESSIONAL MINDSET

A program isn't useful merely because it calculates correctly.

Imagine:

```text
65000
```

versus:

```text
New wallet balance: ₦65,000.00
```

Both contain the same numerical information.

But the second communicates much better.

As you progress toward professional software development, you'll repeatedly encounter this principle:

> **Programs communicate with humans as well as machines.**

Your input should be understandable.

Your calculations should be correct.

Your output should be meaningful.

---

# 🚨 IMPORTANT HABIT

Whenever you write:

```python
input()
```

ask yourself:

> **"What type should this information become?"**

For example:

```text
Name       → str
Product    → str
Age        → int
Quantity   → int
Price      → float
Balance    → float
Discount   → float
```

Don't treat types as decorations.

They determine what your program can do with the data.

---

# 🔥 CONNECTION TO YOUR PROJECTS

## 💰 Wallet App

Your wallet can now move from:

```python
balance = 50000
deposit = 15000
```

to:

```python
balance = float(input("Enter balance: "))
deposit = float(input("Enter deposit: "))
```

That's the beginning of **user interaction**.

Eventually:

```text
User
 ↓
Wallet Interface
 ↓
Wallet Logic
 ↓
Data
```

---

## 🛒 Terminal Store

Your store can now accept actual customer information:

```text
Product
Price
Quantity
Discount
```

rather than having everything permanently written into the source code.

Eventually your terminal store will become something much closer to:

```text
┌─────────────────────┐
│   TERMINAL STORE    │
├─────────────────────┤
│ 1. Buy Product      │
│ 2. View Cart        │
│ 3. Checkout         │
│ 4. Exit             │
└─────────────────────┘
```

We're not building that yet.

But **this is the foundation underneath it.**

---

# 📈 BATCH 5 EXIT CRITERIA

Before declaring Batch 5 complete, you should be able to:

* [ ] Explain what `input()` does
* [ ] Explain what type `input()` returns
* [ ] Use `input()` with prompts
* [ ] Convert input with `int()`
* [ ] Convert input with `float()`
* [ ] Explain why conversion is necessary
* [ ] Use input inside calculations
* [ ] Use `print()` effectively
* [ ] Print multiple values
* [ ] Use f-strings
* [ ] Format decimal values
* [ ] Format numbers with commas
* [ ] Explain Input → Process → Output
* [ ] Debug incorrect input types
* [ ] Build an interactive Wallet program
* [ ] Build an interactive Store receipt
* [ ] Complete the Interactive Checkout Boss Fight

---

# 📝 GROWTH LOG

```text
## Batch 5 — Growth Log

### 🧠 What clicked?
-

### 🥴 What challenged me?
-

### 🏆 Which exercise am I most proud of?
-

### 🐛 What input/type bug did I encounter?
-

### 👨‍🏫 Could I explain why input() returns a string?
-

### 🔁 What do I need to revise?
-

### 🚀 What can I now build that I couldn't build before?
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
[🔥] Batch 5 — Input & Output
[🔒] Batch 6 — Strings
[🔒] Batch 7 — Conditionals
[🔒] Batch 8 — Loops

            ↓

      🐉 PART 1 BOSS FIGHT
```

---

# 🥋 SENSEI'S FINAL WORD

Look at what you've built so far:

```text
Batch 3
Variables
    ↓
"I can store data."

Batch 4
Operators
    ↓
"I can process data."

Batch 5
Input & Output
    ↓
"I can communicate with the user."
```

That's a serious progression.

Soon we're going to introduce **Strings** properly.

And strings aren't just:

```python
name = "Chris"
```

You'll learn how Python lets you manipulate, inspect, combine, search, slice, and format text.

That will make your programs significantly more expressive.

For now:

**Build. Break. Debug. Rebuild.**

Then come back with your Batch 5 completion and Boss Fight result. 🐍⚔️
