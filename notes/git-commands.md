# Git Commands — Quick Reference

A beginner-friendly reference for commonly used Git commands.

---

## 1. Repository Setup

### `git init`

**What it does:** Initializes a new Git repository.

```bash
git init
````

### `git clone`

**What it does:** Copies an existing remote repository to your computer.

```bash
git clone <repository-url>
```

---

## 2. Check Repository

### `git status`

**What it does:** Shows the current state of your working directory.

```bash
git status
```

### `git remote -v`

**What it does:** Shows the remote repositories connected to your project.

```bash
git remote -v
```

---

## 3. Stage Changes

### `git add .`

**What it does:** Stages all changed and new files.

```bash
git add .
```

### `git add <file>`

**What it does:** Stages a specific file.

```bash
git add main.py
```

### `git restore --staged <file>`

**What it does:** Removes a file from staging while keeping your changes.

```bash
git restore --staged main.py
```

---

## 4. Commit Changes

### `git commit -m "message"`

**What it does:** Saves staged changes as a commit.

```bash
git commit -m "feat: add user authentication"
```

### `git commit --amend -m "message"`

**What it does:** Changes the most recent commit.

```bash
git commit --amend -m "feat: improve user authentication"
```

### `git commit --amend --no-edit`

**What it does:** Adds newly staged changes to the previous commit without changing its message.

```bash
git add .
git commit --amend --no-edit
```

---

## 5. Branches

### `git branch`

**What it does:** Lists available branches.

```bash
git branch
```

### `git switch <branch>`

**What it does:** Switches to an existing branch.

```bash
git switch feature/login
```

### `git switch -c <branch>`

**What it does:** Creates a new branch and switches to it.

```bash
git switch -c feature/login
```

---

## 6. Connect to GitHub

### `git remote add origin`

**What it does:** Connects your local repository to a remote GitHub repository.

```bash
git remote add origin <repository-url>
```

### `git branch -M main`

**What it does:** Renames the current branch to `main`.

```bash
git branch -M main
```

---

## 7. Push and Pull

### `git push`

**What it does:** Uploads your local commits to the remote repository.

```bash
git push
```

### `git push -u origin main`

**What it does:** Pushes `main` to GitHub and sets the upstream branch.

```bash
git push -u origin main
```

### `git pull`

**What it does:** Downloads and integrates the latest changes from the remote repository.

```bash
git pull
```

### `git fetch`

**What it does:** Downloads remote changes without merging them into your current branch.

```bash
git fetch
```

---

## 8. View Changes

### `git diff`

**What it does:** Shows unstaged changes.

```bash
git diff
```

### `git diff --staged`

**What it does:** Shows changes currently staged for commit.

```bash
git diff --staged
```

---

## 9. Commit History

### `git log`

**What it does:** Shows the commit history.

```bash
git log
```

### `git log --oneline`

**What it does:** Shows a compact version of the commit history.

```bash
git log --oneline
```

---

## 10. Undo Changes

### `git restore <file>`

**What it does:** Discards uncommitted changes in a file.

```bash
git restore main.py
```

> ⚠️ This can permanently remove uncommitted changes.

### `git reset --soft HEAD~1`

**What it does:** Removes the latest commit while keeping its changes staged.

```bash
git reset --soft HEAD~1
```

> ⚠️ Be careful when using `reset` on commits that have already been pushed.

---

# Common Daily Workflow

```bash
git status
git add .
git commit -m "feat: add new feature"
git push
```

**Simple flow:**

```text
Edit → Status → Add → Commit → Push
```

---

# Common Commit Message Types

| Type       | Purpose            | Example                           |
| ---------- | ------------------ | --------------------------------- |
| `feat`     | New feature        | `feat: add login system`          |
| `fix`      | Bug fix            | `fix: resolve pagination bug`     |
| `docs`     | Documentation      | `docs: update README`             |
| `refactor` | Code restructuring | `refactor: simplify auth service` |
| `test`     | Tests              | `test: add login tests`           |
| `style`    | Formatting/style   | `style: format Python code`       |
| `chore`    | Maintenance        | `chore: update dependencies`      |

---

# First-Time GitHub Setup

```bash
git init
git add .
git commit -m "initial commit"
git branch -M main
git remote add origin <repository-url>
git push -u origin main
```

---

# Quick Reference

```bash
git init
git clone <url>

git status

git add .
git add <file>
git restore --staged <file>

git commit -m "message"
git commit --amend -m "message"
git commit --amend --no-edit

git branch
git switch <branch>
git switch -c <branch>

git remote -v
git remote add origin <url>

git push
git pull
git fetch

git diff
git diff --staged

git log
git log --oneline

git restore <file>
git reset --soft HEAD~1
```