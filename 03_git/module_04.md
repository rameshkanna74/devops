# Module 4 — Tracking Changes

## What You Will Learn

- How to use `git status` to understand what Git sees
- How to use `git add` to stage files for committing
- How to use `git restore` to undo changes
- How to stage multiple files selectively
- How to interpret every line of `git status` output

---

## Why This Matters

`git status` is the command you will run more than any other in your DevOps career. It is your GPS inside a repository. Before every `git add`, before every commit, before every push — you run `git status`. It tells you exactly where you are and what needs attention.

---

## Real DevOps Problem

You have been working on three different NovaMart infrastructure changes today. Your manager needs the Nginx configuration deployed in the next 30 minutes. The other two changes — a deployment script and a monitoring alert — are not ready yet.

How do you commit only the Nginx change without touching the others? How do you make sure you do not accidentally commit a half-finished script?

This module gives you the tools to answer these questions with confidence.

---

## Deep Dive: Reading `git status`

`git status` speaks to you in sections. Let's read each section carefully.

### Section 1: Your current branch

```
On branch main
```

You are on the `main` branch. In later modules you will see this say `feature/nginx-config` or other branch names.

### Section 2: Repository clean

```
nothing to commit, working tree clean
```

This means: your Working Directory matches your last commit exactly. No changes exist anywhere. This is the "all good" state.

### Section 3: Untracked files

```
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        scripts/new-script.sh
```

Git sees this file but has never been told to track it. It will never appear in commits unless you explicitly add it.

### Section 4: Modified but not staged

```
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified: nginx/upstream.conf
```

This file was previously committed. You have changed it. The change is in your Working Directory but not in the Staging Area.

### Section 5: Staged and ready to commit

```
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file: nginx/server.conf
        modified: README.md
```

These files are in the Staging Area. If you run `git commit` right now, these changes will be saved to history.

---

## The `git add` Command — Every Form You Need

### Add a single file

```bash
git add nginx/upstream.conf
```

### Add all files in a folder

```bash
git add nginx/
```

### Add all files in the current directory and subdirectories

```bash
git add .
```

### Add all tracked (previously committed) files that were modified

```bash
git add -u
```

This does NOT add new untracked files. Useful when you only want to stage changes to files Git already knows about.

### Add interactively — choose which changes to stage

```bash
git add -p
```

Git shows you each change one at a time and asks "stage this? (y/n)." This is the professional approach for complex changes.

---

## Guided Walkthrough

Navigate to your repository:

```bash
cd ~/novamart-devops-platform
```

### Step 1: Create infrastructure files

Create a real Nginx upstream configuration:

```bash
cat > nginx/upstream.conf << 'EOF'
# NovaMart Upstream Configuration
# Manages backend server pool

upstream novamart_backend {
    least_conn;
    server 10.0.1.10:8080 weight=3;
    server 10.0.1.11:8080 weight=3;
    server 10.0.1.12:8080 weight=1 backup;
    keepalive 32;
}
EOF
```

Create a basic Nginx server block:

```bash
cat > nginx/server.conf << 'EOF'
# NovaMart Main Server Block

server {
    listen 80;
    server_name novamart.com www.novamart.com;
    
    location / {
        proxy_pass http://novamart_backend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_connect_timeout 30s;
        proxy_read_timeout 60s;
    }
    
    location /health {
        return 200 "OK";
        add_header Content-Type text/plain;
    }
}
EOF
```

Create an unfinished deployment script (work in progress):

```bash
cat > scripts/deploy.sh << 'EOF'
#!/bin/bash
# NovaMart Deployment Script
# STATUS: WORK IN PROGRESS - DO NOT USE

echo "Starting deployment..."
# TODO: Add deployment steps here
EOF
```

### Step 2: Assess the situation

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
        automation/
        ci-cd/
        documentation/
        environments/
        incidents/
        infrastructure/
        linux/
        monitoring/
        nginx/
        portfolio/
        runbooks/
        scripts/

nothing added to commit but untracked files present (use "git add" to track)
```

Everything is untracked. You need to stage only the Nginx files — the deployment script is not ready.

### Step 3: Stage selectively

```bash
git add README.md
git add nginx/upstream.conf
git add nginx/server.conf
```

Check the result:

```bash
git status
```

**Expected output:**

```
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file: README.md
        new file: nginx/server.conf
        new file: nginx/upstream.conf

Untracked files:
        automation/
        ci-cd/
        ...
        scripts/
```

Only `README.md` and the two Nginx files are staged. `scripts/deploy.sh` remains untracked. Exactly what you wanted.

---

## Hands-On Lab 4.1 — Stage the Entire NovaMart Structure

**Objective:** Stage all the project files in preparation for the first commit.

First, let's add placeholder files to all directories (you may have done some of these already):

```bash
touch infrastructure/.gitkeep linux/.gitkeep monitoring/.gitkeep
touch automation/.gitkeep documentation/.gitkeep
touch incidents/.gitkeep environments/.gitkeep
touch ci-cd/.gitkeep portfolio/.gitkeep
```

Now stage everything:

```bash
git add .
```

Verify what is staged:

```bash
git status
```

**Expected output:**

```
Changes to be committed:
        new file: README.md
        new file: automation/.gitkeep
        new file: ci-cd/.gitkeep
        new file: documentation/.gitkeep
        new file: environments/.gitkeep
        new file: incidents/.gitkeep
        new file: infrastructure/.gitkeep
        new file: linux/.gitkeep
        new file: monitoring/.gitkeep
        new file: nginx/server.conf
        new file: nginx/upstream.conf
        new file: portfolio/.gitkeep
        new file: runbooks/deploy-runbook.md
        new file: runbooks/.gitkeep
        new file: scripts/deploy.sh
```

Everything is staged and ready for your first commit. You will make that commit in Module 5.

---

## Hands-On Lab 4.2 — Practice Selective Unstaging

Unstage the `scripts/deploy.sh` file — it is not ready:

```bash
git restore --staged scripts/deploy.sh
```

Verify:

```bash
git status
```

`scripts/deploy.sh` is back to "Untracked files." All other files remain staged. Selective unstaging works the same as selective staging — one command, one file.

---

## Practice Lab 4.3 — The `git add -p` Experience

Create a file with multiple sections of changes:

```bash
cat > documentation/architecture.md << 'EOF'
# NovaMart Architecture

## Web Tier
Nginx serves as the reverse proxy and load balancer.

## Application Tier
Django applications run on Gunicorn workers.

## Database Tier
PostgreSQL handles all persistent data.

## Caching Tier
Redis handles session storage and caching.
EOF
```

Stage it:

```bash
git add documentation/architecture.md
```

Now add more content and try interactive staging:

```bash
echo "" >> documentation/architecture.md
echo "## Monitoring Tier" >> documentation/architecture.md
echo "Prometheus and Grafana handle metrics." >> documentation/architecture.md
```

Run interactive add:

```bash
git add -p documentation/architecture.md
```

Git shows you the change and asks:

```
Stage this hunk [y,n,q,a,d,?]?
```

Press `y` to stage, `n` to skip, `?` for help. This is how professionals stage partial file changes.

---

## Practice Lab 4.4 — Restore a File to Last Committed State

This lab requires having made at least one commit. Since you have not committed yet, mark this for practice after Module 5. For now, understand the command:

```bash
git restore <filename>
```

This restores the file in your Working Directory to its last committed state. Changes you made since the last commit are permanently discarded from the Working Directory.

**Use case:** You spent an hour making changes to a config file, everything broke, and you want to start over from the last known good state.

---

## Troubleshooting Lab 4.5

### Problem: `git add .` staged files I did not want staged

```bash
git restore --staged <filename>
```

Or unstage everything:

```bash
git restore --staged .
```

This moves everything from Staging Area back to Working Directory. Nothing is lost — you just deselected everything.

### Problem: `git status` shows a long list and I cannot find my file

Use grep to filter:

```bash
git status | grep nginx
```

Or use the short format:

```bash
git status -s
```

**Short format key:**

```
?? filename      — untracked
A  filename      — added (staged new file)
M  filename      — modified
MM filename      — modified in both staging and working directory
```

---

## Common Mistakes

**Mistake 1: Staging everything with `git add .` without reviewing**
Always run `git status` before `git add .`. Secrets, log files, and temporary files get accidentally committed this way.

**Mistake 2: Using `git add *` instead of `git add .`**
`git add *` is a shell glob that the shell expands before Git sees it. `git add .` is handled by Git directly. Use `git add .` — it handles hidden files and subdirectories correctly.

**Mistake 3: Forgetting to stage files after editing them**
A common sequence: edit file, stage file, edit file again, commit. The commit contains the version from when you ran `git add`, not your latest changes. Always run `git status` before committing.

---

## Quick Recap

| Command | What It Does |
|---|---|
| `git status` | Show current state of all tracked and untracked files |
| `git status -s` | Short format — compact view |
| `git add <file>` | Stage a specific file |
| `git add .` | Stage everything in the current directory |
| `git add -u` | Stage all modified tracked files (not new files) |
| `git add -p` | Interactively choose which changes to stage |
| `git restore --staged <file>` | Unstage a file |
| `git restore <file>` | Discard Working Directory changes (dangerous) |

---

## Knowledge Check

1. What does `??` mean in `git status -s` output?
2. What is the difference between `git add .` and `git add -u`?
3. Why should you run `git status` before `git add .`?
4. How do you unstage all files at once?
5. What happens if you stage a file, edit it, and then commit?

**Practical questions:**

1. Your colleague committed a file containing a database password. They want to unstage it. What do they tell you? (Hint: if it is already committed, unstaging does not help — that requires different tools covered in Module 15.)
2. You have 20 changed files. You only want to commit changes to files in the `nginx/` folder. What commands do you run?

**Reflection:**

Why do you think `git add .` is the most commonly misused Git command in real teams?

