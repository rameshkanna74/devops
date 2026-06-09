# Module 2 — Your First Repository

## What You Will Learn

- What a Git repository is
- How to create one from scratch with `git init`
- What the hidden `.git` folder contains and why it matters
- How to understand the structure of a repository
- How to create the beginning of the NovaMart project

---

## Why This Matters

Creating a repository is the very first action in any project that uses Git. Every repository you ever work with — whether you create it yourself or clone it from GitHub — starts with this same foundation. Understanding what `git init` actually creates prevents confusion for every lesson that follows.

---

## Real DevOps Problem

It is your first week at NovaMart. Your team lead tells you: "We need a proper home for all of our infrastructure code. Right now it is scattered across engineers' laptops. Create a repository that the whole team can use."

This is module 2. You are creating that repository.

---

## Simple Explanation

A Git repository is just a regular folder with a secret ingredient: a hidden folder called `.git` inside it.

That `.git` folder is Git's brain. It contains:
- The complete history of every change ever made
- All branches that exist
- Your configuration for this repository
- The staging area (you will learn this in Module 3)

When you run `git init`, all Git does is create that `.git` folder inside your current directory. Your folder becomes a repository. Everything else Git does — tracking, committing, branching — operates by reading and writing to that folder.

If you ever delete the `.git` folder, Git forgets everything. Your files remain, but the history, the branches, the commits — all gone. The `.git` folder is sacred. Never delete it manually.

---

## Visual Diagram

```
BEFORE git init                    AFTER git init
─────────────────                  ──────────────────────────────
                                   
my-project/                        my-project/
   (just a folder)                 ├── .git/              ← Git's brain
                                   │   ├── HEAD           ← current branch pointer
                                   │   ├── config         ← repo settings
                                   │   ├── objects/       ← all commits stored here
                                   │   └── refs/          ← branch pointers
                                   │
                                   └── (your files go here)
                                   
Git knows NOTHING                  Git is watching. Every change
about this folder.                 you make from here can be tracked.
```

---

## Guided Walkthrough

### Step 1: Choose where to create your project

In WSL Ubuntu, navigate to your home directory:

```bash
cd ~
```

Create a folder for your NovaMart project:

```bash
mkdir novamart-devops-platform
```

Move into it:

```bash
cd novamart-devops-platform
```

### Step 2: Initialize the repository

```bash
git init
```

**Expected output:**

```
Initialized empty Git repository in /home/yourname/novamart-devops-platform/.git/
```

That single command transformed a plain folder into a Git repository. Git created the `.git` folder and is now ready to track changes.

### Step 3: Confirm it worked

List all files including hidden ones:

```bash
ls -la
```

**Expected output:**

```
total 12
drwxr-xr-x 3 yourname yourname 4096 Jan 15 10:23 .
drwxr-xr-x 8 yourname yourname 4096 Jan 15 10:23 ..
drwxr-xr-x 8 yourname yourname 4096 Jan 15 10:23 .git
```

The `.git` folder is there. Your repository exists.

### Step 4: Peek inside the .git folder

```bash
ls -la .git/
```

**Expected output:**

```
total 40
drwxr-xr-x 8 yourname yourname 4096 Jan 15 10:23 .
drwxr-xr-x 3 yourname yourname 4096 Jan 15 10:23 ..
-rw-r--r-- 1 yourname yourname   21 Jan 15 10:23 HEAD
drwxr-xr-x 2 yourname yourname 4096 Jan 15 10:23 branches
-rw-r--r-- 1 yourname yourname   92 Jan 15 10:23 config
-rw-r--r-- 1 yourname yourname   73 Jan 15 10:23 description
drwxr-xr-x 2 yourname yourname 4096 Jan 15 10:23 hooks
drwxr-xr-x 2 yourname yourname 4096 Jan 15 10:23 info
drwxr-xr-x 4 yourname yourname 4096 Jan 15 10:23 objects
drwxr-xr-x 4 yourname yourname 4096 Jan 15 10:23 refs
```

Do not edit any of these files manually. This is Git's internal machinery.

### Step 5: Check the current status

```bash
git status
```

**Expected output:**

```
On branch main

No commits yet

nothing to commit (create/copy files and use "git add" to track)
```

Git is telling you: "I exist, I am watching, but there is nothing here yet."

---

## Hands-On Lab 2.1 — Build the Project Structure

**Objective:** Create the initial folder structure for the NovaMart repository.

Create the directory structure that will grow throughout this course:

```bash
mkdir -p infrastructure linux scripts monitoring nginx automation documentation runbooks incidents environments ci-cd portfolio
```

Create a starter README file:

```bash
cat > README.md << 'EOF'
# NovaMart DevOps Platform

Infrastructure repository for NovaMart Global.

## Repository Structure

| Folder | Purpose |
|---|---|
| infrastructure/ | Core infrastructure configuration |
| linux/ | Linux system configurations |
| scripts/ | Automation scripts |
| monitoring/ | Monitoring and alerting configs |
| nginx/ | Web server configurations |
| automation/ | Deployment automation |
| documentation/ | Technical documentation |
| runbooks/ | Operational runbooks |
| incidents/ | Incident postmortems |
| environments/ | Environment-specific configs |
| ci-cd/ | CI/CD pipeline definitions |
| portfolio/ | Portfolio documentation |

## Team

DevOps Engineering Team — NovaMart Global

## Status

Active development.
EOF
```

View your work:

```bash
ls -la
```

**Expected output:**

```
total 52
drwxr-xr-x 14 yourname yourname 4096 Jan 15 10:30 .
drwxr-xr-x  8 yourname yourname 4096 Jan 15 10:23 ..
drwxr-xr-x  8 yourname yourname 4096 Jan 15 10:23 .git
-rw-r--r--  1 yourname yourname  520 Jan 15 10:30 README.md
drwxr-xr-x  2 yourname yourname 4096 Jan 15 10:30 automation
drwxr-xr-x  2 yourname yourname 4096 Jan 15 10:30 ci-cd
drwxr-xr-x  2 yourname yourname 4096 Jan 15 10:30 documentation
... (and so on)
```

Check Git's status now:

```bash
git status
```

**Expected output:**

```
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        README.md

nothing added to commit but untracked files present (use "git add" to track)
```

Notice that Git sees `README.md` but does not mention the empty folders. Git does not track empty directories — only files. This is why you will often see a `.gitkeep` file inside empty folders in real repositories.

---

## Hands-On Lab 2.2 — Add Placeholder Files

Create `.gitkeep` files to preserve empty directories:

```bash
touch infrastructure/.gitkeep
touch linux/.gitkeep
touch scripts/.gitkeep
touch monitoring/.gitkeep
touch nginx/.gitkeep
touch automation/.gitkeep
touch documentation/.gitkeep
touch runbooks/.gitkeep
touch incidents/.gitkeep
touch environments/.gitkeep
touch ci-cd/.gitkeep
touch portfolio/.gitkeep
```

Check status again:

```bash
git status
```

Now Git sees all the folders because they contain files.

Open VS Code in the current directory:

```bash
code .
```

VS Code opens the `novamart-devops-platform` folder. You will see the sidebar with all your folders and the README.md file. This is your workspace for the rest of the course.

---

## Practice Lab 2.3 — Read the README

Open `README.md` in VS Code and add a personal note below the Status line:

```markdown
## My Learning Journey

I am learning Git as part of my DevOps engineering training.
This repository is my practical workspace.
```

Save the file. Return to your terminal and run:

```bash
git status
```

Git shows `README.md` as modified. You just made your first tracked change. You will learn what to do with it in Module 4.

---

## Practice Lab 2.4 — Understand HEAD

Read what HEAD currently points to:

```bash
cat .git/HEAD
```

**Expected output:**

```
ref: refs/heads/main
```

HEAD is a pointer to your current branch. Right now it says "you are on the main branch." As you create branches later in this course, HEAD will update to reflect where you are.

---

## Troubleshooting Lab 2.5

### Problem: `git init` creates a `master` branch instead of `main`

If your output says `Initialized empty Git repository` but `git status` shows `On branch master`:

```bash
git branch -m master main
```

This renames the branch from `master` to `main`. Better yet, you already ran `git config --global init.defaultBranch main` in Module 1, so this should not happen.

### Problem: `git status` says "fatal: not a git repository"

You are not inside the repository folder. Run:

```bash
pwd
```

Check that the path ends with `novamart-devops-platform`. If not:

```bash
cd ~/novamart-devops-platform
```

### Problem: VS Code does not show the Git icon in the sidebar

VS Code detects Git repositories automatically. If the Git icon (branching icon) does not appear in the left sidebar, make sure you opened the folder — not just a file. Run `code .` from inside the repository directory.

---

## Common Mistakes

**Mistake 1: Running `git init` in the wrong directory**
Always check where you are with `pwd` before running `git init`. Creating a repository inside your home directory or inside another repository causes problems.

**Mistake 2: Deleting the `.git` folder**
Some engineers accidentally delete `.git` thinking it is unnecessary. It contains your entire history. If you delete it, all commits are permanently lost.

**Mistake 3: Creating a repository inside another repository**
Run `git status` in any directory before running `git init`. If you get output, you are already inside a repository. Running `git init` again creates a nested repository which causes serious confusion.

**Mistake 4: Forgetting that Git ignores empty folders**
Always add a `.gitkeep` file to any folder you want Git to track. This is a convention, not a Git feature.

---

## Quick Recap

| Command | What It Does |
|---|---|
| `git init` | Creates a new Git repository in the current folder |
| `git status` | Shows the current state of the repository |
| `ls -la` | Lists all files including hidden ones |
| `cat .git/HEAD` | Shows which branch you are currently on |

---

## Challenge Exercise

Research what the `objects/` directory inside `.git` contains. What are pack files? What is a blob in Git terms? You do not need to understand this deeply — just explore and note what you find. This is how senior engineers develop deep Git knowledge.

---

## Knowledge Check

1. What does `git init` actually do to a folder?
2. Why does Git ignore empty directories?
3. What is the `.git` folder and why should you never delete it?
4. What does HEAD point to in a brand new repository?
5. What command would you run to verify you are in a Git repository?

**Practical questions:**

1. How would you move a repository to a different folder on your machine?
2. A colleague says their repository "disappeared" after they deleted some files. What likely happened?

**Reflection:**

You have created the NovaMart repository. How does it feel compared to just creating a folder? What is different about a folder that Git is tracking?

---

## GitHub Progress Checkpoint

Your repository exists locally. In Module 7, you will push it to GitHub. For now, keep building it locally. By the time you push, it will have a meaningful history worth sharing.

