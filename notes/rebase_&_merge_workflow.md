# Git Rebase & Merge Workflow

## Core Rule

> **Rebase changes the branch you are currently on.**  
> The branch you specify in the command is only the *base*.

---

## What happens here?

### Command

```bash
git checkout feature
git rebase main
```

### Result
- Feature branch history is rewritten
- Feature branch working tree changes
- Main branch does NOT change
- Feature now sits on top of latest main
- History becomes linear

Graphically:

Before:

```
main:    A---B---C
feature: A---B---D---E
```

After:

```
main:    A---B---C
feature: A---B---C---D'---E'
```

Commits `D` and `E` are replayed → `D'` and `E'`.

---

## Why we do this

To:
- keep history linear
- avoid merge commits
- reduce conflicts later
- make PR clean

This is standard team workflow.

---

## After rebasing feature onto main

You now have 3 ways to merge into main.

---

## 1. Fast-forward merge (cleanest local merge)

```bash
git checkout main
git merge --ff-only feature
```

Result:

```
A---B---C---D'---E'
```

No merge commit.

---

## 2. Squash and merge (most common in teams)

On GitHub PR:
→ Click **"Squash and merge"**

Result:

```
A---B---C---F
```

All feature commits become one commit `F`.

Pros:
- clean history
- easy revert
- linear main

---

## 3. Rebase & merge (GitHub option)

GitHub replays commits onto main.

Result:

```
A---B---C---D''---E''
```

Linear history.

---

## Full ideal workflow

### Start work

```bash
git checkout main
git pull
git checkout -b feature
```

### Work and commit

```bash
git add .
git commit -m "feature work"
```

### Main changed meanwhile

```bash
git fetch origin
git rebase origin/main
```

### Push feature branch

```bash
git push -u origin feature
```

If you already pushed before rebase:

```bash
git push --force-with-lease
```

---

## Why force push after rebase?

Rebase rewrites commit hashes.

So remote history differs from local.

Use safe force push:

```bash
git push --force-with-lease
```

Never use:

```bash
git push --force
```

---

## What NOT to do

### ❌ Wrong direction

```bash
git checkout main
git rebase feature
```

This rewrites main history → dangerous.

### ❌ Don't merge main after rebasing

```bash
git merge main
```

Not needed after rebase.

### ❌ Don't run plain pull after rebase

```bash
git pull
```

May create merge commit.

Instead:

```bash
git pull --rebase
```

or

```bash
git fetch
git rebase origin/main
```

---

## Mental model

```
fetch → download remote changes
rebase → rewrite current branch
merge → combine histories
push → update remote
```

---

## Golden rules

1. Rebase feature branches only  
2. Never rebase shared main  
3. Always fetch before rebase  
4. Use `--force-with-lease` after rebase  
5. Merge policy decides linear vs non-linear history  

---

## Quick memory trick

Correct:

```
feature → rebase onto main
```

Danger:

```
main → rebase onto feature
```

---

## If push is rejected after rebase

```
git push --force-with-lease
```

---

## Final understanding

```bash
git checkout feature
git rebase main
```

means:

- Move feature branch onto latest main  
- Rewrite feature history  
- Keep main untouched  
- Prepare for clean merge