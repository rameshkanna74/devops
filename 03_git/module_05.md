# Module 5 — Creating Commits

## What You Will Learn

- What a commit is and what it stores
- How to create commits with `git commit`
- How to write commit messages that communicate clearly
- What makes a good commit versus a bad commit
- Commit conventions used by professional DevOps teams
- How to amend your last commit

---

## Why This Matters

Commits are the fundamental unit of Git. Everything else — branches, pull requests, reversions, comparisons — operates on commits. A repository with poor commit messages is nearly useless when something breaks in production and you need to understand the history quickly.

Your commit messages are a form of documentation. They will be read by your team, by your manager, and by your future self at 2 AM when something is broken.

---

## Real DevOps Problem

It is 2 AM. Production is down. Nginx is returning 502 errors. You pull up the Git log for the Nginx configuration repository.

**Scenario A — Bad commit messages:**

```
commit f3a2b1c  — pushed changes
commit a9d4e2f  — updates
commit 7b3c1e9  — fix
commit 2d8f4a1  — stuff
commit e1c7b3d  — misc changes
```

You have no idea which commit caused the problem. You will have to check each one individually. At 2 AM. With production down.

**Scenario B — Good commit messages:**

```
commit f3a2b1c  — feat(nginx): increase proxy_read_timeout to 120s for long-running API calls
commit a9d4e2f  — fix(nginx): correct upstream keepalive count from 32 to 16
commit 7b3c1e9  — feat(nginx): add /health endpoint for load balancer checks
commit 2d8f4a1  — config(nginx): set worker_processes to auto for CPU optimization
commit e1c7b3d  — docs(nginx): add inline comments to upstream configuration
```

You immediately see that the timeout change in `f3a2b1c` could explain 502 errors. You check it first. You find the issue in three minutes. Production is restored.

This is why commit messages matter.

---

## Simple Explanation

A commit is a snapshot of your Staging Area at a specific moment, combined with:

- Your name and email
- The date and time
- A message you write
- A unique ID (a hash like `a4f3b2c`)
- A pointer to the previous commit

Commits form a chain. Each commit knows what came before it. This chain is your repository history.

```
COMMIT CHAIN
────────────────────────────────────────────────

  [Commit 1]  ←  [Commit 2]  ←  [Commit 3]  ←  HEAD
  Initial        Add nginx       Fix upstream     (most recent)
  project        config          timeout
  
  a4f3b2c        7d9e1f3         c2a8b4e
```

---

## The Anatomy of a Commit

Every Git commit contains:

```
Commit Hash:    c2a8b4e1f3d9a7b2c8e4f1
Author:         Ahmed Hassan <ahmed@novamart.com>
Date:           Mon Jan 15 14:32:18 2024 +0530

    fix(nginx): correct upstream keepalive count from 32 to 16
    
    The keepalive 32 setting was causing connection pool exhaustion
    under high traffic. Reduced to 16 based on server capacity.
    Verified with load testing in staging environment.
    
    Fixes: NM-2847
    Tested-by: Sara Kapoor <sara@novamart.com>
```

**Hash:** A unique 40-character identifier generated from the content. No two commits have the same hash. You usually only need the first 7 characters.

**Author:** Who made this commit. Taken from your `git config` settings.

**Date:** When the commit was created. Automatic.

**Message:** What you write. The only part you control. Make it count.

---

## How to Write Good Commit Messages

### The Golden Rule

A good commit message completes this sentence:

> "If applied, this commit will **[your message here]**."

- "If applied, this commit will **add nginx upstream configuration**" ✓
- "If applied, this commit will **fix stuff**" ✗

### The Structure

```
<type>(<scope>): <short summary>

<body — optional, explain WHY not WHAT>

<footer — optional, reference issues>
```

**Short summary rules:**
- 50 characters or fewer
- Imperative mood (use "add" not "added," use "fix" not "fixed")
- No period at the end
- Start with lowercase after the colon

**Body rules:**
- Explain WHY the change was made, not what was changed (Git diff shows what)
- Wrap lines at 72 characters
- Separate from summary with a blank line

### Conventional Commits — The Professional Standard

| Type | When to Use |
|---|---|
| `feat` | Adding a new feature or configuration |
| `fix` | Fixing a bug or broken configuration |
| `docs` | Changes to documentation or comments |
| `config` | Configuration changes |
| `refactor` | Restructuring without changing behavior |
| `test` | Adding or updating tests |
| `ci` | Changes to CI/CD pipeline definitions |
| `chore` | Maintenance tasks |

**Examples:**

```
feat(nginx): add rate limiting to /api endpoints
fix(scripts): handle missing environment variable in deploy.sh
docs(runbooks): add disaster recovery runbook for database failures
config(monitoring): set alert threshold to 95% disk usage
ci(github-actions): add staging deployment workflow
chore(cleanup): remove deprecated backup configuration files
```

---

## Creating Your First Commit

### Method 1: Inline message (for short messages)

```bash
git commit -m "feat(project): initialize novamart-devops-platform repository"
```

### Method 2: Open editor (for longer messages)

```bash
git commit
```

This opens VS Code (or your configured editor). Write your message, save, and close the file. Git reads the message from the file.

### Method 3: Specify message and body

```bash
git commit -m "feat(nginx): add upstream and server configuration" -m "Initial Nginx setup for NovaMart web tier. Includes upstream pool with three backend servers and load balancing using least_conn algorithm."
```

---

## Guided Walkthrough — Your First Commit

Navigate to your repository:

```bash
cd ~/novamart-devops-platform
```

Check what is staged (from the work done in Modules 3 and 4):

```bash
git status
```

Everything should be staged. If not, run:

```bash
git add .
git restore --staged scripts/deploy.sh
```

Create the first commit:

```bash
git commit -m "feat(project): initialize novamart-devops-platform repository

Sets up the foundational structure for the NovaMart DevOps platform.
Includes Nginx configuration, directory structure, and README.

Directories created:
- infrastructure, linux, scripts, monitoring
- nginx, automation, documentation, runbooks
- incidents, environments, ci-cd, portfolio"
```

**Expected output:**

```
[main (root-commit) a4f3b2c] feat(project): initialize novamart-devops-platform repository
 14 files changed, 48 insertions(+)
 create mode 100644 README.md
 create mode 100644 automation/.gitkeep
 create mode 100644 ci-cd/.gitkeep
 create mode 100644 documentation/.gitkeep
 create mode 100644 environments/.gitkeep
 create mode 100644 incidents/.gitkeep
 create mode 100644 infrastructure/.gitkeep
 create mode 100644 linux/.gitkeep
 create mode 100644 monitoring/.gitkeep
 create mode 100644 nginx/server.conf
 create mode 100644 nginx/upstream.conf
 create mode 100644 portfolio/.gitkeep
 create mode 100644 runbooks/deploy-runbook.md
 create mode 100644 runbooks/.gitkeep
```

Your first commit exists. The repository has history now.

Check the status:

```bash
git status
```

**Output:**

```
On branch main
nothing to commit, working tree clean
```

The working directory matches the last commit. Everything is clean.

---

## Hands-On Lab 5.1 — Create Three More Commits

**Objective:** Build a meaningful commit history for the NovaMart project.

**Commit 2 — Add a deployment script**

```bash
cat > scripts/deploy.sh << 'EOF'
#!/bin/bash
# NovaMart Deployment Script
# Deploys application to production servers

set -e

APP_NAME="novamart"
DEPLOY_USER="deploy"
SERVERS=("10.0.1.10" "10.0.1.11" "10.0.1.12")

echo "[$(date)] Starting deployment of ${APP_NAME}"

for server in "${SERVERS[@]}"; do
    echo "[$(date)] Deploying to ${server}..."
    ssh "${DEPLOY_USER}@${server}" "sudo systemctl restart ${APP_NAME}"
    echo "[$(date)] Successfully deployed to ${server}"
done

echo "[$(date)] Deployment complete."
EOF

chmod +x scripts/deploy.sh
git add scripts/deploy.sh
git commit -m "feat(scripts): add production deployment script

Automates deployment to all three backend servers.
Uses SSH to restart the application service on each server.
Script exits immediately on any failure (set -e)."
```

**Commit 3 — Add monitoring configuration**

```bash
cat > monitoring/alerts.conf << 'EOF'
# NovaMart Alert Configuration
# Prometheus alerting rules

groups:
  - name: novamart.infrastructure
    rules:
      - alert: HighCPUUsage
        expr: cpu_usage_percent > 85
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "High CPU usage on {{ $labels.instance }}"

      - alert: DiskSpaceLow
        expr: disk_free_percent < 10
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: "Low disk space on {{ $labels.instance }}"

      - alert: NginxDown
        expr: nginx_up == 0
        for: 30s
        labels:
          severity: critical
        annotations:
          summary: "Nginx is down on {{ $labels.instance }}"
EOF

git add monitoring/alerts.conf
git commit -m "config(monitoring): add Prometheus alert rules for infrastructure

Covers three critical alert scenarios:
- HighCPUUsage: warns at 85% for 5 minutes
- DiskSpaceLow: critical alert at 10% free space
- NginxDown: critical alert after 30 seconds"
```

**Commit 4 — Update README with deployment information**

```bash
cat >> README.md << 'EOF'

## Deployment

Run the deployment script from the repository root:

\`\`\`bash
./scripts/deploy.sh
\`\`\`

Requires SSH access to production servers. Contact your team lead for access.

## Monitoring

Alerts are configured in `monitoring/alerts.conf`.
Prometheus scrapes metrics from all backend servers on port 9090.
EOF

git add README.md
git commit -m "docs(readme): add deployment and monitoring sections

Explains how to run deployments and where monitoring configs live.
Makes the README useful for new team members."
```

Verify your history:

```bash
git log --oneline
```

**Expected output:**

```
d7e3c1a (HEAD -> main) docs(readme): add deployment and monitoring sections
b4f2e8c config(monitoring): add Prometheus alert rules for infrastructure
a9c1d7b feat(scripts): add production deployment script
a4f3b2c feat(project): initialize novamart-devops-platform repository
```

You have four commits. A real project history is forming.

---

## Hands-On Lab 5.2 — Amend the Last Commit

**Objective:** Fix a mistake in the most recent commit without creating a new commit.

Imagine you forgot to include a file in the last commit.

Create a file you "forgot":

```bash
echo "contact: devops@novamart.com" > documentation/contacts.md
git add documentation/contacts.md
```

Amend the last commit to include it:

```bash
git commit --amend --no-edit
```

`--no-edit` keeps the same commit message. The file is added to the last commit.

Check the log:

```bash
git log --oneline
```

The same four commits appear, but the last one now contains the new file. Its hash changed (because the content changed), but it is still one commit.

**Warning:** Never amend a commit that has already been pushed to GitHub. Amending rewrites history, which causes serious problems for team members who have already pulled the original commit.

---

## Practice Lab 5.3 — Write Commit Messages for These Scenarios

For each scenario, write the appropriate commit message before looking at the suggested answer.

**Scenario 1:** You added a new Nginx `location` block to handle `/api/v2/` endpoints with a different timeout setting.

*Suggested:* `feat(nginx): add /api/v2 location block with extended timeout`

**Scenario 2:** You fixed a typo in the deployment script where `DEPLOY_USER` was spelled `DPLOY_USER`.

*Suggested:* `fix(scripts): correct DEPLOY_USER variable name typo`

**Scenario 3:** You added a comment block at the top of the alerts.conf file explaining its purpose.

*Suggested:* `docs(monitoring): add header comment explaining alert configuration`

**Scenario 4:** You reorganized the runbooks folder by creating subfolders for different categories.

*Suggested:* `refactor(runbooks): organize into deployment and incident subfolders`

---

## Practice Lab 5.4 — Examine Your Commits

See the full details of the most recent commit:

```bash
git show
```

See the full details of a specific commit (use a hash from your `git log`):

```bash
git show a4f3b2c
```

See what changed in the most recent commit:

```bash
git show --stat
```

---

## Troubleshooting Lab 5.5

### Problem: "nothing to commit, working tree clean" when I try to commit

You have not staged anything. Run `git add` first.

### Problem: "Aborting commit due to empty commit message"

You opened the editor, did not write anything (or wrote only commented lines starting with `#`), and saved. Git treats this as an empty message and aborts.

Write a message above the commented lines and save again.

### Problem: The commit message opened Nano instead of VS Code

Your editor is not configured correctly. Fix it:

```bash
git config --global core.editor "code --wait"
```

Then for the current commit, type your message and use `Ctrl+X`, then `Y`, then `Enter` to save in Nano, and reconfigure before your next commit.

### Problem: I committed the wrong files

If the commit has not been pushed, amend it:

```bash
git restore --staged <wrong-file>
git commit --amend
```

If it has been pushed, use `git revert` (covered in Module 15).

---

## Common Mistakes

**Mistake 1: Vague commit messages**
`git commit -m "updates"` is not a commit message. Future you — and your teammates — need to understand what changed without reading every line of the diff.

**Mistake 2: Committing too much at once**
One commit should represent one logical change. Committing fifteen unrelated files together makes history impossible to understand.

**Mistake 3: Committing too rarely**
Some engineers commit only at the end of the day. If something breaks, you cannot pinpoint which of your fifteen changes caused it. Commit small, commit often.

**Mistake 4: Amending pushed commits**
`git commit --amend` rewrites the commit. If others have pulled the original, their repository history will diverge from yours. This causes merge conflicts for no reason.

---

## Quick Recap

| Command | What It Does |
|---|---|
| `git commit -m "message"` | Commit staged changes with inline message |
| `git commit` | Open editor to write commit message |
| `git commit --amend` | Modify the last commit |
| `git commit --amend --no-edit` | Add staged files to last commit without changing message |
| `git show` | Show details of the most recent commit |
| `git show <hash>` | Show details of a specific commit |

---

## Knowledge Check

1. What is a commit hash and how is it generated?
2. What does the imperative mood mean in a commit message?
3. When should you use `git commit --amend`?
4. What is the difference between committing too much and committing too rarely?
5. What information does Git automatically record with every commit?

**Practical questions:**

1. Your last commit has the message "fix stuff." How do you change it if the commit has not been pushed?
2. Write a conventional commit message for this change: "You added error handling to the deployment script that exits and sends a Slack notification if any server deployment fails."

**Reflection:**

Look at your `git log --oneline` output. Does your commit history tell a story? Could a new team member understand what happened in this repository from just the commit messages?

