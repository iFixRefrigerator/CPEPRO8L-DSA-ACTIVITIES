# Directory Size Calculator — Recursion in Real-World Applications

---

## I. Introduction

When you right-click a folder in Windows and select **"Properties,"** you see the total size of everything inside it — including all nested subfolders. This seemingly simple operation is actually a **real-world problem that recursion solves elegantly**. The **Directory Size Calculator** is a tool that recursively traverses a directory tree, summing up the sizes of all files found at every level of the folder hierarchy. Operating systems, disk cleanup tools, and cloud storage managers all use this kind of logic to show users how much space folders consume.

---

## II. Application Overview & Explanation

### What is this application/problem, and what does it do?

A **Directory Size Calculator** takes a folder path as input and computes the total disk space occupied by all files within that folder, including files in all subfolders at every level of the directory hierarchy. It answers a simple but important question: *"How much space does this folder actually take up?"*

The challenge is that you never know how deeply nested the folders are. A folder can contain subfolders, which can contain more subfolders, and so on — creating an **infinite depth of nesting**. This is why recursion is the perfect tool for the job.

### What is the base case and the recursive case in this problem?

| Case | Condition | Action |
|------|-----------|--------|
| **Base Case** | Path points to a **file** | Return the file's size using `os.path.getsize(path)` |
| **Recursive Case** | Path points to a **directory** | Iterate over every entry inside, recursively call the function on each entry, and sum up all the results |

The **base case** stops the recursion when there's nothing left to explore — a file has no "contents" to drill into. The **recursive case** keeps the traversal going by diving into each subdirectory and repeating the process.

### How does the call stack build up and unwind as the recursive function executes?

Let's trace an example with this structure:
```
C:/Users/User/Documents/
├── report.pdf (100 KB)
└── projects/
├── code.py (50 KB)
└── data/
└── dataset.csv (200 KB)
```

**Call Stack Building (Going Deeper):**

1. `calculate_size("Documents")` — is a directory → loops → sees `report.pdf` → calls `calculate_size("Documents/report.pdf")`
2. `calculate_size("Documents/report.pdf")` — is a file → returns `100` → **frame pops off**
3. Back in the directory call, sees `projects` → calls `calculate_size("Documents/projects")`
4. `calculate_size("Documents/projects")` — sees `code.py` → calls `calculate_size("Documents/projects/code.py")` → returns `50`
5. Sees `data` → calls `calculate_size("Documents/projects/data")`
6. `calculate_size("Documents/projects/data")` — sees `dataset.csv` → calls `calculate_size("Documents/projects/data/dataset.csv")` → returns `200`

**Call Stack Unwinding (Returning Values Back Up):**

- `data` returns `200` → `projects` adds it to `50` = `250` → returns `250`
- `Documents` adds `250` to `100` = `350` → returns `350` (final answer)

The call stack acts like a **stack of plates** — each recursive call pushes a new frame, and as each base case is hit, frames pop off one by one, carrying values back up the chain. Each folder *"pauses"* and waits for all its subfolders to *"report back"* before it can compute its own total.

---

## III. Sample Code

📄 **[Click here to view directory_size_calculator.py](sample_code.py)**

The code implements a recursive function `calculate_size(path)` that:

- **Base case:** Returns file size if path is a file
- **Recursive case:** Sums sizes of all entries if path is a directory

📸 **[View Test Results & Screenshots (PDF)](test_result_screenshot.pdf)**

> ✅ **Test Result:** I tested this code on my Downloads folder, and the output matched exactly with what Windows shows in the folder Properties dialog.

---

## IV. Personal Insights

What I learned from doing this activity:

I honestly thought recursion was just a *"math trick"* for solving puzzles like Fibonacci or factorials. But when I researched file system traversal, I realized that recursion is actually **how computers naturally process hierarchical structures**. The folder-inside-folder-inside-folder structure is infinite by nature — you never know how deep it goes — so a loop alone can't easily handle it without manually tracking a stack. **Recursion does it automatically.**

What became clearer to me is the **call stack**. I always knew recursion used the stack, but I never truly visualized how each call gets *"paused"* while it waits for its recursive children to finish. The directory size example makes this super intuitive — each folder waits for all its subfolders and files to *"report back"* before it can compute its own total.

This taught me that for any problem involving **nested structures**, recursion is often the cleanest, most natural solution. It also made me realize the importance of a **well-defined base case** — without it, the function would infinitely recurse and crash.

I can definitely see myself using recursion in future projects like:
- Building a **file explorer app**
- Creating a **website crawler**
- Analyzing **dependency trees** in a package manager

---

## V. References

1. GeeksforGeeks. **"Recursion."** *GeeksforGeeks*. https://www.geeksforgeeks.org/recursion/
2. Python Documentation. **"os.path — Common pathname manipulations."** *Python Software Foundation*. https://docs.python.org/3/library/os.path.html
3. Real Python. **"Python Recursion: A Complete Guide."** *Real Python*. https://realpython.com/python-recursion/

---

**Made with ❤️ for CPEPRO8L Recursion Research Activity**
