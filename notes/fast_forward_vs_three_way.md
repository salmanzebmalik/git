# Fast-Forward Merge vs Three-Way Merge

## Basic idea
When you merge one branch into another, Git combines their histories.  
There are two main ways this can happen:
- **fast-forward merge**
- **three-way merge**

---

## Fast-Forward Merge

A Fast-forward merge is like smoothly merging two roads into one. This type of merge occurs when the branch being merged can be directly merged into the current branch without any conflicts. Git simply moves the pointer of the current branch to the tip of the other branch, incorporating all the changes, like merging two streams into one river.

### What it means
A fast-forward merge happens when the target branch has not changed since the new branch was created.  
In this situation, Git does not need to combine two different sets of changes.  
Instead, it simply moves the branch pointer forward to the latest commit of the other branch.

### What happens internally
- No new merge commit is created.  
- Git just updates the branch pointer.  
- The history stays linear and simple.  

### Example in words
Suppose you create a feature branch from the main branch and make some commits on the feature branch.  
If no one makes new commits on the main branch during that time, then merging the feature branch back into main only requires moving main forward.  
Nothing needs to be combined because all commits from main are already part of the feature branch history.

### Key characteristics
- No merge commit  
- Straight, linear history  
- Happens automatically when possible  

![alt text](/notes/assets/fast_forward_merge.png)
---

## Three-Way Merge

When a fast-forward merge is not possible (e.g., due to divergent changes in both branches), Git performs a three-way merge. It creates a new commit that combines changes from both branches, using a common ancestor commit as the base for comparison. we can understand it like this, it is more like solving a puzzle. It happens when the changes in both branches have gone in different directions and can’t be smoothly merged.

### What it means
A three-way merge happens when both branches have new commits after they split.  
Now Git must combine two different lines of development.

### Why it is called “three-way”
Git looks at three things:
1. The last common commit shared by both branches  
2. The changes made in the first branch  
3. The changes made in the second branch  

Git compares all three to create a new combined result.

### What happens internally
- Git creates a new merge commit.  
- This merge commit contains the combined changes.  
- The history shows that two branches came together.  
- Conflicts may occur if the same lines were changed differently.

### Example in words
You create a feature branch and make changes.  
Meanwhile, someone else also makes changes on the main branch.  
When you try to merge the feature branch back, Git cannot simply move the pointer forward.  
It must combine both sets of changes into a new commit.  
That new commit is the merge commit.

### Key characteristics
- A new merge commit is created  
- History shows branches joining  
- May require conflict resolution  

![alt text](/notes/assets/three_way_merge.png)

---

## Main Difference in Simple Terms

A fast-forward merge happens when one branch is simply behind another and can catch up by moving forward.  
A three-way merge happens when both branches have moved forward independently and must be combined.

---

## When each happens

Fast-forward merge occurs when:
- The main branch has not changed since branching  
- All new commits are only on the feature branch  

Three-way merge occurs when:
- Both branches have new commits  
- Git must combine two histories  

---

## Forcing a merge commit
Even if a fast-forward merge is possible, you can force Git to create a merge commit:

```bash
git merge --no-ff branch_name
```