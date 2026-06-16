# Git from Practice

# Book 1 — Git Essentials Through a Real FastAPI Project

## Beginner to Job-Ready Git Foundations (2026 Edition)

---

# Who This Book Is For

This book is for:

- Students learning Git for the first time
- Aspiring Backend Developers
- Aspiring DevOps Engineers
- Freshers preparing for interviews
- Anyone tired of memorizing Git commands without understanding them

---

# What Makes This Book Different?

Most Git tutorials teach:

```bash
git add
git commit
git push
```

without explaining WHY.

This book teaches Git through a real project.

Every Git command solves a real problem.

You will build:

```text
FastAPI Todo API
```

while learning Git.

By the end of this book you will know:

- How Git actually works

- How to save your work safely

- How to create branches

- How teams work on features

- How merge conflicts happen

- How to resolve conflicts confidently

- How to recover from mistakes

These are the Git skills expected from junior developers and entry-level DevOps engineers.

---

# Learning Rules

Throughout this book:

DO NOT memorize commands.

Always ask:

> Why do I need this command?

Git becomes easy when you understand the problem it solves.

---

# Project Overview

We will build this API:

```text
GET     /
GET     /todos
POST    /todos
GET     /todos/{id}
DELETE  /todos/{id}
```

Project structure:

```text
fastapi-todo/

├── app/
│   ├── main.py
│   ├── models.py
│   └── routes/
│       └── todos.py
│
├── requirements.txt
│
└── README.md
```

---

# Chapter 1

# What Is Git?

Imagine this situation.

You spend:

- 5 hours coding
- everything works

Then:

```python
# You accidentally delete code
```

or

```python
# You break something
```

or

```python
# You want yesterday's version back
```

Without Git:

😢 Panic

With Git:

😊 One command

Git is a time machine for code.

---

# How Git Thinks

Git has 3 areas.

```text
Working Directory
       ↓
Staging Area
       ↓
Repository
```

---

## Working Directory

Files you are editing right now.

Example:

```python
print("hello")
```

---

## Staging Area

Temporary holding area.

Think:

```text
Shopping Cart
```

You choose what goes into the next snapshot.

---

## Repository

Permanent history.

Every commit becomes a checkpoint.

```text
Commit A
Commit B
Commit C
```

You can return anytime.

---

# Chapter 2

# Creating Our First Repository

Create project:

```bash
mkdir fastapi-todo
cd fastapi-todo
```

Initialize Git:

```bash
git init
```

Output:

```text
Initialized empty Git repository
```

Git creates:

```text
.git/
```

This hidden folder is Git's database.

---

## Check Status

```bash
git status
```

Output:

```text
nothing to commit
```

This command is your best friend.

Use it constantly.

---

# Chapter 3

# Your First Commit

Create README.

```bash
echo "# FastAPI Todo API" > README.md
```

Check status:

```bash
git status
```

Output:

```text
untracked file:
README.md
```

Git sees the file.

Git is NOT tracking it yet.

---

## Stage the File

```bash
git add README.md
```

Check status:

```bash
git status
```

Now:

```text
Changes to be committed
```

---

## Create Commit

```bash
git commit -m "Initial commit"
```

Congratulations.

You created your first checkpoint.

---

# Practice

Run:

```bash
git log
```

Question:

How many commits exist?

Answer:

```text
1
```

---

# Chapter 4

# Build FastAPI Application

Install packages:

```bash
pip install fastapi uvicorn
```

Create:

```text
app/
```

---

## main.py

```python
from fastapi import FastAPI
from app.routes.todos import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def root():
    return {
        "message": "Todo API Running"
    }
```

---

## models.py

```python
from pydantic import BaseModel

class Todo(BaseModel):
    id: int
    title: str
    completed: bool = False
```

---

## routes/todos.py

```python
from fastapi import APIRouter, HTTPException
from app.models import Todo

router = APIRouter(
    prefix="/todos",
    tags=["todos"]
)

todos = []
```

---

Add endpoints.

### GET Todos

```python
@router.get("/")
def get_todos():
    return todos
```

---

### POST Todo

```python
@router.post("/")
def create_todo(todo: Todo):
    todos.append(todo)
    return todo
```

---

### GET Todo By ID

```python
@router.get("/{todo_id}")
def get_todo(todo_id: int):

    for todo in todos:
        if todo.id == todo_id:
            return todo

    raise HTTPException(
        status_code=404,
        detail="Todo not found"
    )
```

---

### DELETE Todo

```python
@router.delete("/{todo_id}")
def delete_todo(todo_id: int):

    global todos

    todos = [
        todo
        for todo in todos
        if todo.id != todo_id
    ]

    return {
        "message": "deleted"
    }
```

---

Run server:

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://localhost:8000/docs
```

Swagger UI appears.

---

# Git Exercise

Check status.

```bash
git status
```

What do you see?

Lots of new files.

---

## Commit Project

```bash
git add .
```

```bash
git commit -m "Create FastAPI Todo API"
```

---

# Chapter 5

# Understanding git diff

Modify:

```python
"Todo API Running"
```

to:

```python
"Todo API Version 2"
```

Run:

```bash
git diff
```

Git shows:

```text
- old line
+ new line
```

This command answers:

> What exactly changed?

Use before every commit.

---

# Chapter 6

# Branches

Imagine:

You want to build a new feature.

Current app works.

Question:

Should you edit directly on main?

No.

Why?

Because you might break working code.

---

# Create First Branch

```bash
git branch feature/list-todos
```

See branches:

```bash
git branch
```

Output:

```text
* main
  feature/list-todos
```

---

Switch:

```bash
git switch feature/list-todos
```

---

# Visualizing Branches

```text
main
  \
   feature/list-todos
```

Both point to same commit initially.

---

# Chapter 7

# Add New Feature

Inside feature branch:

Add:

```python
completed_count endpoint
```

Example:

```python
@router.get("/stats")
def stats():

    completed = len(
        [x for x in todos if x.completed]
    )

    return {
        "completed": completed
    }
```

Commit:

```bash
git add .
```

```bash
git commit -m "Add todo statistics endpoint"
```

---

# Verify Isolation

Switch back.

```bash
git switch main
```

Check code.

Feature does not exist.

Amazing.

Branches are isolated workspaces.

---

# Chapter 8

# Merge

Bring feature into main.

```bash
git merge feature/list-todos
```

Git combines histories.

Now:

```text
main
```

contains new endpoint.

---

# Practice Challenge

Create:

```text
feature/delete-todo
```

Implement delete endpoint.

Commit.

Merge.

---

# Chapter 9

# Merge Conflicts

Every Git learner must experience one.

We will create it intentionally.

---

# Step 1

Create branch:

```bash
git switch -c feature-priority
```

Modify model:

```python
priority: int = 1
```

Commit.

---

# Step 2

Return main.

```bash
git switch main
```

Modify same area:

```python
description: str = ""
```

Commit.

---

# Step 3

Merge.

```bash
git merge feature-priority
```

Git:

```text
CONFLICT
```

Perfect.

This is normal.

---

# Conflict Markers

Git creates:

```text
<<<<<<< HEAD

description: str

=======

priority: int

>>>>>>> feature-priority
```

Meaning:

```text
Two developers changed same code.
Git needs help.
```

---

# Resolve Conflict

Keep both.

```python
description: str = ""
priority: int = 1
```

Remove markers.

---

Stage:

```bash
git add .
```

Commit:

```bash
git commit -m "Resolve merge conflict"
```

Done.

---

# Chapter 10

# Undo Mistakes

Most important beginner skill.

---

Modify:

```python
main.py
```

Break code.

Example:

```python
this is invalid python
```

Check:

```bash
git status
```

---

Want last committed version back?

```bash
git restore app/main.py
```

Magic.

File restored.

---

# Remember

Use:

```bash
git restore filename
```

when:

```text
I changed something
I regret it
I haven't committed it
```

---

# Chapter 11

# Reading History

View commits:

```bash
git log
```

Compact version:

```bash
git log --oneline
```

Example:

```text
a34fd Add stats endpoint
b56de Create Todo API
c78ef Initial commit
```

---

# Better History View

```bash
git log --oneline --graph
```

Example:

```text
* merge feature
|\
| *
| *
* main
```

This is how professionals inspect repositories.

---

# Chapter 12

# Git Habits of Great Engineers

Before coding:

```bash
git status
```

Before committing:

```bash
git diff
```

After committing:

```bash
git log --oneline
```

Before sleeping:

```bash
git push
```

(Book 2)

---

# Mini Project Challenge

Build these branches:

```text
feature/update-todo
feature/search-todo
feature-completed-filter
```

For every feature:

1. Create branch
2. Write code
3. Commit
4. Merge

Repeat until comfortable.

---

# Git Skills Mastered

By finishing this book you can:

- Create repositories

- Track files

- Stage changes

- Commit changes

- View history

- Compare changes

- Create branches

- Switch branches

- Merge branches

- Resolve conflicts

- Undo mistakes

---

# Book 1 Final Interview Questions

Q1: What problem does Git solve?

Q2: Difference between Working Directory and Staging Area?

Q3: Why use git add?

Q4: Why create branches?

Q5: What causes merge conflicts?

Q6: What does git restore do?

Q7: Difference between git log and git log --oneline?

Q8: Why should developers avoid coding directly on main?

If you can answer all 8 confidently and complete the FastAPI project without looking at notes, you are ready for Book 2: Git for Teams, GitHub, CI/CD, and DevOps Workflows.

---

# End of Book 1

# Git Essentials Through Practice
