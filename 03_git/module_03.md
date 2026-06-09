# Module 3 — Understanding Git States

## What You Will Learn

- The three zones that every file passes through in Git
- What the Working Directory is
- What the Staging Area is and why it exists
- What the Repository (committed history) is
- How files move between zones
- Why this understanding is essential before learning any more commands

---

## Why This Matters

This is the most important conceptual module in the entire course. Engineers who are confused about Git's three states are confused about Git. Every command you will ever learn — `git add`, `git commit`, `git restore`, `git diff` — only makes sense when you understand these three zones.

Do not rush this module. Read it twice if you need to.

---

## Real DevOps Problem

You have made changes to two files in the NovaMart repository: the Nginx configuration and a deployment script. The Nginx change is ready to commit. The deployment script is still a work in progress.

How do you commit only the Nginx change without committing the unfinished script?

The answer is the Staging Area. You cannot answer this question without understanding Git's three states.

---

## Simple Explanation

Imagine you are packing boxes to move to a new apartment.

**Your apartment (Working Directory)** — This is where all your stuff lives. You are surrounded by items, some packed, some not. This is where you do all your work.

**The staging table by the door (Staging Area)** — When something is ready to go, you put it on this table. Items on the table are selected, ready, waiting for the moving truck. You can still change your mind and take something back.

**The moving truck (Repository)** — Once the truck is packed and driven away, those items are permanently recorded as "moved." The truck driver writes down exactly what was in it and when. This is a commit.

```
YOUR APARTMENT          STAGING TABLE         MOVING TRUCK
(Working Directory)     (Staging Area)        (Repository)
─────────────────       ──────────────        ─────────────

nginx.conf      ──────►  nginx.conf   ──────►  Commit #1
deploy.sh               (ready)                "add nginx config"
README.md
random notes
half-packed stuff
```

The Staging Area gives you control. You decide exactly what goes into each commit. You do not have to commit everything at once.

---

## Visual Diagram — The Three Zones

```
┌─────────────────────────────────────────────────────────────────────┐
│                          YOUR COMPUTER                              │
│                                                                     │
│  ┌──────────────────┐   git add    ┌──────────────────┐             │
│  │                  │ ───────────► │                  │             │
│  │  WORKING         │              │  STAGING AREA    │             │
│  │  DIRECTORY       │              │  (Index)         │             │
│  │                  │ ◄─────────── │                  │             │
│  │  Files you see   │  git restore │  Files ready     │             │
│  │  and edit        │              │  to commit       │             │
│  │                  │              │                  │             │
│  └──────────────────┘              └──────────────────┘             │
│                                             │                       │
│                                        git commit                   │
│                                             │                       │
│                                             ▼                       │
│                                   ┌──────────────────┐              │
│                                   │                  │              │
│                                   │  REPOSITORY      │              │
│                                   │  (.git folder)   │              │
│                                   │                  │              │
│                                   │  Permanent       │              │
│                                   │  history of      │              │
│                                   │  all commits     │              │
│                                   │                  │              │
│                                   └──────────────────┘              │
└─────────────────────────────────────────────────────────────────────┘
```

---

## The Four States a File Can Be In

A file in a Git repository can exist in one of four states:

### 1. Untracked

Git has never seen this file before. You just created it. Git knows it exists in your Working Directory but has never been told to track it.

```
git status output:
  Untracked files:
      deploy.sh
```

### 2. Modified

Git knows this file and has previously committed it. You have changed it since the last commit. The change exists only in your Working Directory.

```
git status output:
  Changes not staged for commit:
      modified: nginx.conf
```

### 3. Staged

You have run `git add` on this file. It is now in the Staging Area. The change is selected and ready to be committed. But it has not been committed yet — you can still change your mind.

```
git status output:
  Changes to be committed:
      modified: nginx.conf
```

### 4. Committed

You have run `git commit`. The change is permanently stored in the Repository. This is part of your history.

```
git log output:
  commit a4f3b2c
  Author: Your Name
  Date: Jan 15 10:45
  
      add nginx upstream configuration
```

---

## Visual Diagram — File State Transitions

```
  File Created
      │
      ▼
 ┌──────────┐    git add    ┌──────────┐    git commit   ┌──────────┐
 │          │ ────────────► │          │ ──────────────► │          │
 │UNTRACKED │               │  STAGED  │                 │COMMITTED │
 │          │ ◄──────────── │          │                 │          │
 └──────────┘  git restore  └──────────┘                 └──────────┘
                --staged                                      │
                                                              │ edit file
                                                              ▼
                                                         ┌──────────┐
                                                         │          │
                                                         │ MODIFIED │
                                                         │          │
                                                         └──────────┘
                                                              │
                                                         git add again
                                                              │
                                                              ▼
                                                         (STAGED again)
```

---

## Guided Walkthrough

Navigate to your NovaMart repository:

```bash
cd ~/novamart-devops-platform
```

### Step 1: See an untracked file

Create a new file:

```bash
echo "upstream novamart_backend { server 127.0.0.1:8080; }" > nginx/upstream.conf
```

Check its status:

```bash
git status
```

**Output:**

```
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        README.md
        automation/
        ci-cd/
        ...
        nginx/
        ...

nothing added to commit but untracked files present
```

The `nginx/` directory shows as untracked. Git sees the folder but has never been asked to track its contents.

### Step 2: Stage a file

```bash
git add nginx/upstream.conf
```

Check status:

```bash
git status
```

**Output:**

```
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file: nginx/upstream.conf

Untracked files:
        README.md
        automation/
        ...
```

`nginx/upstream.conf` moved from "Untracked" to "Staged." It is in the Staging Area, ready to commit. Everything else is still untracked.

### Step 3: Unstage a file

Change your mind about staging it:

```bash
git restore --staged nginx/upstream.conf
```

Check status:

```bash
git status
```

`nginx/upstream.conf` is back to untracked. The Staging Area is empty again. The file itself is unchanged — only its staging status changed.

### Step 4: Stage everything

```bash
git add .
```

The `.` means "everything in the current directory and all subdirectories."

Check status:

```bash
git status
```

Everything is now staged. Ready to commit.

---

## Hands-On Lab 3.1 — Move Files Through All Three States

**Objective:** Deliberately move a file through every state and observe Git's response at each step.

Create a new file:

```bash
echo "# NovaMart Deployment Runbook" > runbooks/deploy-runbook.md
```

**Step 1: Observe untracked state**

```bash
git status
```

Note: `runbooks/deploy-runbook.md` is untracked.

**Step 2: Stage it**

```bash
git add runbooks/deploy-runbook.md
git status
```

Note: File moves to "Changes to be committed."

**Step 3: Modify it while it is staged**

```bash
echo "" >> runbooks/deploy-runbook.md
echo "## Pre-Deployment Checklist" >> runbooks/deploy-runbook.md
echo "- Verify staging environment passes tests" >> runbooks/deploy-runbook.md
git status
```

**Expected output:**

```
Changes to be committed:
        new file: runbooks/deploy-runbook.md

Changes not staged for commit:
        modified: runbooks/deploy-runbook.md
```

This is a critical observation. The same file appears in *two* sections. Git staged the version of the file at the moment you ran `git add`. The new changes you made after staging are tracked in the Working Directory but not yet staged.

If you commit right now, the commit will contain the original staged version — not the newer changes. You would need to run `git add` again to stage the latest version.

**Step 4: Stage the updated version**

```bash
git add runbooks/deploy-runbook.md
git status
```

Now only "Changes to be committed" appears. The staging area has the latest version.

---

## Hands-On Lab 3.2 — Selective Staging

**Objective:** Stage only specific files, leaving others unstaged.

Create three files:

```bash
echo "server_name novamart.com;" > nginx/server.conf
echo "#!/bin/bash" > scripts/deploy.sh
echo "# Monitoring config" > monitoring/alerts.conf
```

Check status:

```bash
git status
```

Three new untracked files. Now stage only the nginx file:

```bash
git add nginx/server.conf
git status
```

**Output:**

```
Changes to be committed:
        new file: nginx/server.conf

Untracked files:
        scripts/deploy.sh
        monitoring/alerts.conf
```

Only `nginx/server.conf` is staged. The other two files are untouched in the Working Directory. This is exactly the scenario from the Real DevOps Problem at the start of this module — committing only finished work while leaving unfinished work unstaged.

---

## Practice Lab 3.3 — Discard Working Directory Changes

Create and modify a file:

```bash
echo "worker_processes 4;" > nginx/nginx-main.conf
```

Stage it:

```bash
git add nginx/nginx-main.conf
```

Now pretend you staged it by mistake and want to unstage it:

```bash
git restore --staged nginx/nginx-main.conf
git status
```

The file is unstaged but still in the Working Directory.

Now pretend you do not want the file at all and want to discard the changes:

```bash
git restore nginx/nginx-main.conf
```

**Warning:** `git restore` on an unstaged file in the Working Directory *permanently discards your changes.* The file reverts to its last committed version (or disappears if it was never committed). Use this carefully.

---

## Practice Lab 3.4 — Understand `git diff`

`git diff` shows you exactly what changed between different zones.

First, let's have something to compare. Make sure `README.md` has content and add more:

```bash
echo "" >> README.md
echo "## Infrastructure Overview" >> README.md
echo "NovaMart runs on Ubuntu 24.04 LTS servers." >> README.md
```

Now run:

```bash
git diff
```

This shows changes in the Working Directory that are *not yet staged*. Lines beginning with `+` are added. Lines beginning with `-` are removed.

Stage the file:

```bash
git add README.md
```

Run `git diff` again:

```bash
git diff
```

Nothing appears. `git diff` without arguments only shows *unstaged* changes. To see staged changes:

```bash
git diff --staged
```

Now you see the same changes, but this time they are showing what is in the Staging Area compared to the last commit.

---

## Troubleshooting Lab 3.5

### Problem: A file appears in both "staged" and "unstaged" sections

```
Changes to be committed:
        modified: nginx/upstream.conf

Changes not staged for commit:
        modified: nginx/upstream.conf
```

This means you staged the file, then modified it again. The staging area has the old version. The working directory has the new version.

**Solution:** Stage again to capture the latest changes:

```bash
git add nginx/upstream.conf
```

### Problem: `git restore` deleted my file

`git restore <filename>` reverts the file to the last committed version. If the file was never committed, it removes it entirely.

**Solution:** If the file was staged before you ran `git restore`, you may be able to recover it using:

```bash
git restore --staged <filename>
git restore <filename>
```

If it was never staged or committed, the file is gone. This is one reason to commit early and often.

---

## Common Mistakes

**Mistake 1: Thinking `git add .` is always the right choice**
`git add .` stages everything. In professional workflows, you should review what you are staging. Use `git status` first, then stage selectively.

**Mistake 2: Confusing the Staging Area with saving**
Staging is not saving. Nothing is safe in the Staging Area. Only a commit creates permanent history.

**Mistake 3: Forgetting to re-stage after making changes**
If you stage a file and then edit it, the staging area still holds the *old* version. Always run `git add` again after making additional changes.

**Mistake 4: Running `git restore` carelessly**
`git restore <file>` throws away your working directory changes permanently. There is no undo. Always double-check before using it.

---

## Quick Recap

| Zone | Where It Lives | How to Get There |
|---|---|---|
| Working Directory | Your filesystem | Just edit files |
| Staging Area | `.git/index` | `git add <file>` |
| Repository | `.git/objects/` | `git commit` |

| Command | What It Does |
|---|---|
| `git add <file>` | Moves file from Working Directory to Staging Area |
| `git restore --staged <file>` | Moves file from Staging Area back to Working Directory |
| `git restore <file>` | Discards Working Directory changes (dangerous) |
| `git diff` | Shows unstaged changes |
| `git diff --staged` | Shows staged changes |

---

## Knowledge Check

1. Name the three Git zones in order from "where you edit" to "permanent history."
2. What does it mean when a file appears in both "staged" and "unstaged" sections of `git status`?
3. What is the difference between `git restore` and `git restore --staged`?
4. Why does `git diff` show nothing after you run `git add`?
5. Why does Git have a Staging Area at all? Why not commit directly?

**Practical questions:**

1. You have changed five files. Only two are ready to commit. Walk through the exact commands you would use.
2. You accidentally staged a file containing a password. What do you do?

**Reflection:**

Before learning about the Staging Area, how would you have expected Git to work? Why do you think the Staging Area was designed this way?

