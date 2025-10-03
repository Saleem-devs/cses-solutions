# CSES Problem Set

## Concert Tickets

### Task

There are `n` concert tickets available, each with a certain price. Then, `m` customers arrive one after another.

Each customer announces the maximum price they are willing to pay for a ticket. They will then get the ticket with the **highest possible price** such that it does not exceed their maximum price.

After a ticket is sold, it cannot be purchased again.  
If a customer cannot get any ticket, print `-1`.

---

### Input

- The first input line contains two integers `n` and `m`:

  - `n` = number of tickets
  - `m` = number of customers

- The next line contains `n` integers:  
  `h1, h2, ..., hn` — the price of each ticket.

- The last line contains `m` integers:  
  `t1, t2, ..., tm` — the maximum price for each customer in the order they arrive.

---

### Output

Print `m` integers: the price each customer will pay for their ticket.  
If a customer cannot get any ticket, print `-1`.

---

### Constraints

- `1 ≤ n, m ≤ 2 * 10^5`
- `1 ≤ hi, ti ≤ 10^9`

---

### Example

**Input:**  
5 3  
5 3 7 8 5  
4 8 3

**Output:**  
3  
8  
-1
