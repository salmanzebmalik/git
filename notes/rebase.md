# Git Rebase, Branching & Remote Workflow — Complete Guide

## Table of Contents

1. Core Concepts
2. Fetch vs Pull vs Rebase
3. Correct Workflow When `main` Has Changed
4. Merge vs Rebase
5. Squash & Merge
6. Best Practices in Teams
7. Common Mistakes
8. Danger Zones
9. Linear History vs Non-Linear
10. Useful Commands Cheat Sheet

---

# 1. Core Concepts

### Local branch

A branch in your local repository.

### Remote branch

Branch stored on GitHub (e.g. `origin/main`).

### Remote-tracking branch

Your local reference to remote state:

```
origin/main
origin/feature-x
```

Updated by:

```
git fetch
```

---

# 2. Fetch vs Pull vs Rebase

### `git fetch`

Downloads remote commits but **does not merge**.

```
git fetch origin
```

Safe. Always recommended before rebasing.

---

### `git pull`

Fetch + merge (default behavior).

```
git pull
```

Creates a merge commit if histories diverged.

---

### `git pull --rebase`

Fetch + rebase.

```
git pull --rebase
```

Keeps history linear.

---

### `git remote update`

Fetch from all remotes.

```
git remote update
```

Equivalent to:

```
git fetch --all
```

---

# 3. Correct Workflow When `main` Has Changed

## Scenario

You created a feature branch.
Meanwhile, `main` received new commits.

You want:

* clean history
* no merge commits
* linear feature branch

## Correct flow

```
git checkout feature
git fetch origin
git rebase origin/main
```

Resolve conflicts if needed.

Then push:

```
git push --force-with-lease
```

Why force?
Rebase rewrites commit hashes.

---

# 4. Merge vs Rebase

## Merge

```
git merge origin/main
```

Creates:

```
feature ---\
            merge commit
main   -----/
```

Pros:

* Safe
* No history rewrite

Cons:

* Non-linear history

---

## Rebase

```
git rebase origin/main
```

Creates:

```
main ---- new commits
```

Pros:

* Linear history
* Clean PR

Cons:

* Rewrites commit hashes

---

# 5. Squash & Merge

## GitHub squash (recommended)

Open PR → click:

```
Squash and merge
```

Result:

* One commit on `main`
* Linear history

---

## Local squash

```
git rebase -i origin/main
```

Change:

```
pick
squash
squash
```

Then merge:

```
git checkout main
git merge --ff-only feature
```

---

# 6. Best Practices in Teams

### Always do before working

```
git fetch origin
```

### Feature branch workflow

```
git checkout -b feature
# work
git fetch origin
git rebase origin/main
git push -u origin feature
```

### Before opening PR

```
git fetch
git rebase origin/main
```

### Never rebase shared main

Avoid:

```
git rebase main
```

on `main` branch.

---

# 7. Common Mistakes

## Mistake 1

Rebasing wrong branch

Wrong:

```
git checkout main
git rebase feature
```

Correct:

```
git checkout feature
git rebase main
```

Rule:

> Rebase FROM the branch you want to move.

---

## Mistake 2

Forgetting fetch before rebase

Wrong:

```
git rebase origin/main
```

Correct:

```
git fetch origin
git rebase origin/main
```

---

## Mistake 3

Force pushing incorrectly

Never:

```
git push --force
```

Always:

```
git push --force-with-lease
```

---

# 8. Danger Zones

## ⚠️ Rebasing shared branch

Never rebase:

* main
* dev used by team

Unless:

* everyone agrees
* you force push carefully

---

## ⚠️ Rebasing after pushing

If branch already pushed:

```
git push --force-with-lease
```

Otherwise teammates will get conflicts.

---

## ⚠️ Merge commit confusion

Even if you rebase, history becomes non-linear if PR merged with merge commit.

GitHub merge options:

* Merge commit → non-linear
* Squash → linear
* Rebase merge → linear

---

# 9. Linear vs Non-Linear History

### Linear

```
A---B---C---D
```

### Merge commit

```
A---B---C
     \   \
      D---E
```

Merge commits are normal in many teams.

Linear history requires:

* rebase
* squash merge
* or rebase merge

---

# 10. Full Example Flow

## Starting work

```
git checkout main
git pull
git checkout -b feature
```

## Work and commit

```
git add .
git commit -m "feature"
```

## Main changed on remote

```
git fetch origin
git rebase origin/main
```

Resolve conflicts if needed:

```
git add .
git rebase --continue
```

## Push branch

```
git push -u origin feature
```

If rebased after pushing:

```
git push --force-with-lease
```

## Merge to main (linear)

```
git checkout main
git merge --ff-only feature
git push
```

OR GitHub:
→ Squash and merge

---

# 11. Conflict Resolution During Rebase

Git stops:

```
CONFLICT
```

Fix files → then:

```
git add .
git rebase --continue
```

Abort:

```
git rebase --abort
```

---

# 12. Deleting Branches

Delete local:

```
git branch -d feature
```

Delete remote:

```
git push origin --delete feature
```

Clean stale:

```
git fetch --prune
```

---

# 13. Golden Rules

1. Always fetch before rebase
2. Rebase feature branches only
3. Never rebase shared main
4. Use force-with-lease, not force
5. Choose merge strategy intentionally
6. Squash for clean history
7. Merge commits are not wrong

---

# 14. Mental Model

```
fetch → updates remote refs
rebase → rewrites your branch
merge → combines histories
push → updates remote
```

---

# 15. Interview-Ready Summary

* `git fetch`: download only
* `git pull`: fetch + merge
* `git pull --rebase`: fetch + rebase
* rebase makes branch linear
* merge preserves full history
* squash makes one commit
* rebase rewrites history
* never rebase shared main

---

# End Notes

This guide reflects **real industry workflows**.

Different teams choose:

* merge commits
* squash merge
* rebase merge

All are valid depending on policy.

---
