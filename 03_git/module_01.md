# Module 1 — Why Git Exists

## What You Will Learn

- What version control is and why it exists
- What life was like before Git
- Why teams cannot function without version control
- How Git compares to just copying files
- Where Git fits in a real DevOps workflow

---

## Why This Matters

Before you touch a single Git command, you need to understand _why Git was built_. Engineers who understand the problem Git solves use it confidently. Engineers who just memorize commands get confused the moment something goes wrong.

Git is not just a tool you learn because your job requires it. Git is the foundation that everything in DevOps is built on. CI/CD pipelines, infrastructure as code, automated deployments, team collaboration — none of it works without Git.

---

## Real DevOps Problem

Imagine you are a DevOps engineer at NovaMart Global. You are responsible for the Nginx configuration that handles all web traffic. One Friday afternoon, your team needs to make an urgent change to the configuration file.

Here is what happens without Git:

1. You copy `nginx.conf` to `nginx.conf.backup`
2. You make your changes
3. Something breaks in production
4. You scramble to remember which version was the working one
5. Your colleague also edited the file at the same time
6. Nobody knows whose version is correct
7. The site is down and chaos reigns

This is not a hypothetical. This is what DevOps teams experienced before version control became standard practice. Some teams are still living this nightmare today.

---

## Simple Explanation

Think of Git like a very intelligent save system for your code and configuration files.

When you play a video game, you save your progress at certain points. If you die, you reload from your last save. Git works the same way, except it is far more powerful:

- You can save your progress at any point (called a **commit**)
- You can have multiple save slots happening at the same time (called **branches**)
- Multiple people can play the same game simultaneously without overwriting each other's progress
- You can travel back to any save point in history
- You can see exactly what changed between any two save points
- You can combine the progress of multiple players safely

Git does all of this for your code, configuration files, scripts, documentation — anything stored as text.

---

## Life Before Git — A True Story

### The Copy-and-Paste Era

Before version control became standard, here is what a typical team's file system looked like:

```
nginx-configs/
├── nginx.conf
├── nginx.conf.backup
├── nginx.conf.backup2
├── nginx.conf.jan-2024
├── nginx.conf.working-DO-NOT-TOUCH
├── nginx.conf.ahmed-changes
├── nginx.conf.final
├── nginx.conf.final-FINAL
├── nginx.conf.final-FINAL-v2
└── nginx.conf.THIS-ONE-USE-THIS
```

This folder is not fictional. Versions of this folder exist in real companies right now.

### The Problems This Creates

**Nobody knows what changed.**
When something breaks, you cannot see what was different between `nginx.conf.final` and `nginx.conf.final-FINAL`. You have to manually compare them line by line.

**Nobody knows who changed it.**
Was it Ahmed? Was it Sara? Was it you? There is no record.

**Nobody knows when it changed.**
The file modification time only tells you when the file was last saved. If someone copied an old version over a new one, even that timestamp is meaningless.

**Collaboration is impossible.**
If Ahmed is editing `nginx.conf` and Sara is also editing `nginx.conf`, one of them will overwrite the other's work the moment they save.

**Rollback is terrifying.**
When production breaks and you need to revert to the last working version, you are staring at ten files with identical names hoping you picked the right one. Under pressure. At 2 AM.

---

## What Git Solves

Git was created by Linus Torvalds in 2005 to manage the Linux kernel — one of the most complex software projects in human history, maintained by thousands of contributors worldwide. If Git can handle that, it can handle your Nginx configs.

Git solves every problem listed above:

| Problem                      | Git's Solution                                       |
| ---------------------------- | ---------------------------------------------------- |
| What changed?                | `git diff` shows exact line-by-line differences      |
| Who changed it?              | Every commit records the author                      |
| When did it change?          | Every commit has a timestamp                         |
| Two people editing same file | Branching and merging handles this safely            |
| Need to revert?              | `git revert` or `git checkout` to any previous state |
| Which version is correct?    | Main branch is always the authoritative version      |

---

## Git vs File Copies

```
FILE COPIES                          GIT
──────────────────────────────────────────────────────────

nginx.conf.backup          vs       Commit: "fix ssl timeout"
nginx.conf.backup2         vs       Commit: "add rate limiting"
nginx.conf.ahmed-jan       vs       Commit: "ahmed: update upstream"
nginx.conf.final           vs       Commit: "prepare for release"

RESULT: 4 confusing files           RESULT: 4 named, dated, authored
        no dates                            snapshots you can jump
        no authors                          between instantly
        no context
        cannot combine them
```

---

## Git in the DevOps World

Git is not just used for application code. In DevOps, Git manages everything:

**Infrastructure as Code**
Tools like Terraform and Ansible store their configuration in Git. When you push a change to the main branch, an automated pipeline picks it up and applies it to your infrastructure.

**CI/CD Pipelines**
GitHub Actions, Jenkins, and GitLab CI all trigger automated workflows based on Git events. A push to main can automatically run tests, build containers, and deploy to production.

**Configuration Management**
Nginx configs, systemd service files, cron jobs, Kubernetes manifests — all of these live in Git. If something breaks in production, the fix is a commit and a push.

**Documentation**
Runbooks, incident postmortems, architecture diagrams written in Markdown — all version controlled in Git so you always know what the process was at any point in time.

**Audit Trails**
In regulated industries, you need to prove what changed, who changed it, and when. Git provides a complete, tamper-evident audit trail for free.

```
DEVOPS WORKFLOW WITH GIT
─────────────────────────────────────────────────────────

  Developer          GitHub              Automation
  ─────────          ──────              ──────────

  [edit code]
      │
  git commit
      │
  git push  ────────► [GitHub] ────────► [GitHub Actions]
                                               │
                                         run tests
                                               │
                                         build image
                                               │
                                         deploy to prod
```

---

## Where NovaMart Fits In

NovaMart Global runs an e-commerce platform serving millions of customers. The DevOps team manages:

- Web servers (Nginx)
- Linux infrastructure
- Automation scripts (Bash, Python)
- Monitoring configuration
- Deployment pipelines

Every single piece of this infrastructure lives in Git. You are joining the team as a junior DevOps engineer. Your job is to learn Git well enough to contribute to the `novamart-devops-platform` repository without breaking production.

By the time you finish this course, that repository will look like this:

```
novamart-devops-platform/
├── README.md
├── infrastructure/
├── linux/
├── scripts/
├── monitoring/
├── nginx/
├── automation/
├── documentation/
├── runbooks/
├── incidents/
├── environments/
├── ci-cd/
└── portfolio/
```

Every module adds to this. Nothing is thrown away. Everything you learn builds the same real project.

---

## Hands-On Lab 1.1 — Observe a Real Repository

**Objective:** Explore a real Git repository on GitHub before creating your own.

**Instructions:**

1. Open your browser and go to: `https://github.com/torvalds/linux`
2. Scroll through the files. This is one of the most active Git repositories in the world.
3. Click on the **Commits** link near the top of the page.
4. Click on any commit.
5. Notice what you see:
   - The author's name
   - The date and time
   - A message explaining what changed
   - Exactly which lines were added (shown in green) and removed (shown in red)

**What you are observing:** Every single change to the Linux kernel, going back to 2005, is recorded here. No file copies. No confusion. A complete, readable history of the most complex software project on Earth.

**Questions to answer for yourself:**

1. How many commits have been made in the last week?
2. Can you find a commit that removed lines and added new ones in the same file?
3. What does a well-written commit message look like?

---

## Hands-On Lab 1.2 — Set Up Your Identity

**Objective:** Tell Git who you are before making your first commit.

Git needs to know your name and email so it can record who made each change. This is a one-time setup.

Open your WSL Ubuntu terminal and run:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

Set your default branch name to `main` (the modern standard):

```bash
git config --global init.defaultBranch main
```

Set VS Code as your default Git editor:

```bash
git config --global core.editor "code --wait"
```

Verify your configuration:

```bash
git config --list
```

**Expected output:**

```
user.name=Your Name
user.email=your.email@example.com
init.defaultBranch=main
core.editor=code --wait
```

**What just happened:** You stored your identity in a file called `~/.gitconfig`. Every commit you make from this machine will automatically include this name and email. This is how Git knows who to blame (and who to credit).

---

## Practice Lab 1.3 — Explore the .gitconfig File

View your configuration file directly:

```bash
cat ~/.gitconfig
```

**Expected output:**

```
[user]
    name = Your Name
    email = your.email@example.com
[init]
    defaultBranch = main
[core]
    editor = code --wait
```

This is a plain text file. Git reads it every time it needs to know who you are.

---

## Practice Lab 1.4 — Version Check

Verify your Git installation:

```bash
git --version
```

**Expected output:**

```
git version 2.43.0
```

Your version number may differ. Any version above 2.28 supports all features in this course.

Check Git help:

```bash
git help
```

Scroll through the list of commands. Do not memorize them. Just notice that Git has far more commands than you will ever need to use. You will master about 15 of them. Those 15 will cover 95% of your daily work.

---

## Troubleshooting Lab 1.5

### Problem: `git config --list` shows wrong email

```bash
git config --global user.email "correct.email@example.com"
```

Run `git config --list` again to verify.

### Problem: VS Code does not open when Git needs an editor

Test it manually:

```bash
code --version
```

If `code` is not found, open VS Code and press `Ctrl+Shift+P`, then type "Shell Command: Install 'code' command in PATH" and select it.

---

## Common Mistakes

**Mistake 1: Skipping the identity setup**
If you do not run `git config --global user.name` and `git config --global user.email`, Git will refuse to create commits or use a default identity that does not represent you. Always configure your identity first.

**Mistake 2: Using your work email for personal projects**
Use your personal email if this account will be your portfolio. GitHub shows this email publicly on your commits unless you configure privacy settings.

**Mistake 3: Thinking Git and GitHub are the same thing**
Git is the version control software that runs on your computer. GitHub is a website that hosts Git repositories online. You can use Git without GitHub. GitHub requires Git. They are related but separate tools.

---

## Quick Recap

| Concept         | What It Means                                              |
| --------------- | ---------------------------------------------------------- |
| Version control | A system that tracks changes to files over time            |
| Git             | The software that performs version control on your machine |
| GitHub          | A website that stores Git repositories online              |
| Commit          | A saved snapshot of your files at a point in time          |
| Repository      | A folder that Git is tracking                              |

---

## Challenge Exercise

Find a DevOps-related GitHub repository (try searching for "ansible playbooks" or "terraform aws modules"). Explore its commit history and answer:

1. How do the commit messages compare to each other? Are they descriptive?
2. Can you find a commit where something was broken and then fixed in a follow-up commit?
3. How many contributors does the repository have?

---

## Knowledge Check

1. What is the difference between Git and GitHub?
2. Name three problems that file copies create that Git solves.
3. Why do DevOps engineers need Git even if they are not writing application code?
4. What information does every Git commit record automatically?
5. What command do you use to set your Git username?

**Practical questions:**

1. Without looking, can you explain what `git config --global user.email` does and why it matters?
2. Open a real GitHub repository and find a commit that changed more than 10 files. What does the commit message say?

**Reflection:**

Think about your own files right now — documents, scripts, notes. How are you currently managing versions of them? What would change if you used Git?

---

## Interview Corner

**Question: "What is Git and why do we use it?"**

_Why interviewers ask this:_ They want to confirm you understand the purpose of the tool, not just the commands. Many candidates can recite `git commit` but cannot explain what problem it solves.

_What interviewers expect:_ A clear explanation of version control, why it matters for teams, and ideally a real-world example of what Git prevents.

_Common mistake:_ Saying "Git is a version control system" and stopping there. That is the definition, not an explanation. Describe a concrete scenario where Git saves the day.

_Strong answer:_ "Git is a distributed version control system that tracks changes to files over time. In a DevOps context, it means every infrastructure change — whether it is an Nginx config, a Terraform module, or a deployment script — has a recorded author, timestamp, and message. If something breaks in production, I can identify exactly what changed, when, and who made the change. Without Git, teams end up with file copies and no audit trail."
