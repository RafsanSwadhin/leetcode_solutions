def hIndex(citations):
    n = len(citations)
    count = [0] * (n + 1)  # Buckets from 0 to n

    # Count how many papers have i citations (or more for i > n)
    for c in citations:
        if c >= n:
            count[n] += 1
        else:
            count[c] += 1

    # Traverse buckets from high to low
    total = 0
    for i in range(n, -1, -1):
        total += count[i]
        if total >= i:
            return i

    return 0


#citations = [3,0,6,1,5]
'''


Of course Rafsan! Let's walk **line by line** through your code with the example input:

```python
citations = [3, 0, 6, 1, 5]
```

---

### 🔍 Problem:

Return the **h-index**, which is the **maximum value `h`** such that the researcher has **at least `h` papers** with **≥ `h` citations**.

---

### ✅ Your Code:

```python
def hIndex(citations):
```

This defines a function `hIndex` that takes a list of integers `citations` as input.

---

```python
    n = len(citations)
```

* `n` is the number of papers.
* For `[3, 0, 6, 1, 5]`, `n = 5` (5 papers)

---

```python
    count = [0] * (n + 1)
```

* Create a list `count` with `n+1 = 6` elements: `[0, 0, 0, 0, 0, 0]`
* Purpose: `count[i]` stores **how many papers have exactly `i` citations**
* If a paper has more than `n` citations, it still goes into `count[n]` bucket.

---

```python
    for c in citations:
        if c >= n:
            count[n] += 1
        else:
            count[c] += 1
```

Now we go through each citation and fill the `count` array.

#### Iteration over `citations = [3, 0, 6, 1, 5]`:

| `c` | condition | update         | `count` after update |
| --- | --------- | -------------- | -------------------- |
| 3   | 3 < 5     | count\[3] += 1 | `[0, 0, 0, 1, 0, 0]` |
| 0   | 0 < 5     | count\[0] += 1 | `[1, 0, 0, 1, 0, 0]` |
| 6   | 6 >= 5    | count\[5] += 1 | `[1, 0, 0, 1, 0, 1]` |
| 1   | 1 < 5     | count\[1] += 1 | `[1, 1, 0, 1, 0, 1]` |
| 5   | 5 >= 5    | count\[5] += 1 | `[1, 1, 0, 1, 0, 2]` |

Final `count = [1, 1, 0, 1, 0, 2]`

---

```python
    total = 0
```

* Initialize a `total` counter to accumulate how many papers have at least `i` citations.

---

```python
    for i in range(n, -1, -1):
```

* Loop from `i = 5` down to `0`.

---

```python
        total += count[i]
```

* Add the number of papers with exactly `i` citations.

---

```python
        if total >= i:
            return i
```

* Check if there are **at least `i` papers** that have **≥ `i` citations**.
  If yes, return `i` — this is the h-index.

---

### 🔁 Iteration of the loop:

| i | count\[i] | total after += | check `total >= i` | Result   |
| - | --------- | -------------- | ------------------ | -------- |
| 5 | 2         | 2              | 2 >= 5 ❌           |          |
| 4 | 0         | 2              | 2 >= 4 ❌           |          |
| 3 | 1         | 3              | 3 >= 3 ✅           | return 3 |

✅ So we return `3` as the h-index.

---

### 📌 Final Return:

```python
return 3
```

---

### ✅ Summary:

* Count papers by citations using a bucket (size `n + 1`)
* Loop backwards to find largest `i` where `i` or more papers have at least `i` citations.
* Return `i`

Would you like a **visual chart** to help this sink in more easily?



'''