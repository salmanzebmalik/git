# Working with remote repositories

There are various remote repository hosting sites:

- [GitHub](http://github.com/)
- [BitBucket](https://bitbucket.org/product)
- [Gitlab](https://gitlab.com/)

### Useful commands to start with remote github repositories

```bash
# Git clone is used to clone a remote repository into a local workspace
git clone `URL`
# Git push is used to push commits from your local repo to a remote repo
git push
# Git pull is used to fetch the newest updates from a remote repository
git pull
```


### 1. **Git Basics & Local Repositories**

Before connecting to remote repositories, you need to understand how Git works locally. A **local repository** is a project on your computer that has its own history (commit history) and branches.

* **Local Branches**: These are the branches that exist in your local repository. For example, `master`, `dev`, and `feature-xyz` could be local branches.
* **Remote Branches**: These are branches that exist on a remote repository, such as GitHub. They are stored in your local repository as references to the remote repository, typically under `origin/<branch_name>`. `origin` is the default name for the remote repository.

---

### 2. **Connecting to a Remote Repository (GitHub)**

The process of connecting a local Git repository to a remote repository (like GitHub) typically involves the following steps:

* **Setting up the remote**: You associate your local repository with a remote repository using a command like:

  ```bash
  git remote add origin <repository_url>
  ```

  This links your local repository to the remote one. The URL can be either an HTTPS or SSH URL, depending on how you authenticate with GitHub.

* **Checking the remote connection**: After linking the remote repository, you can check if the connection is working with:

  ```bash
  git remote -v
  ```

  This shows the remote repository's URLs (fetch and push URLs) for each remote you have configured.

---

### 3. **Basic Git Commands**

Here's an explanation of the commands you listed, in order of how you'd use them in your workflow.

#### `git remote show origin`

This command shows detailed information about the `origin` remote repository (or whatever remote you are working with), including fetch and push URLs, the current branch, and more. It gives you insights into the configuration of the remote repository.

---

#### `git remote update`

This command fetches information about all remotes, updating the references of remote branches in your local repository. It's useful when you have multiple remotes and want to update all remote references.

---

#### `git branch -r`

This lists all the remote branches associated with the remote repository. These branches are read-only references to the remote branches.

---

#### `git status`

Shows the current status of your working directory. It will tell you which files are modified, staged, and untracked, as well as whether your branch is ahead, behind, or in sync with the remote repository.

---

#### `git fetch`

This command downloads objects and refs from the remote repository, without merging them into your working branch. It updates the remote tracking branches (e.g., `origin/master`) in your local repository but doesn't alter your local working branch.

---

#### `git log origin/master`

This shows the commit history of the remote `master` branch (which is located on `origin`). It's useful for reviewing changes made in the remote repository that you haven't yet fetched or merged.

---

#### `git merge origin/master`

This merges changes from the remote `master` branch into your current local branch. If there are conflicts between your local changes and the remote changes, Git will ask you to resolve those conflicts.

---

#### `git log`

Shows the commit history of your local branch. This helps you see your recent commits and which changes have been made in the local repository.

---

#### `git pull`

This is a combination of `git fetch` followed by `git merge`. It fetches changes from the remote repository and attempts to merge them into your current branch. If there are conflicts, you need to resolve them manually.

---

#### `git checkout <branch_name>`

This command allows you to switch between branches in your local repository. For example, if you want to switch to a `feature-xyz` branch, you'd run `git checkout feature-xyz`.

---

#### `git checkout -b <branch_name>`

This creates a new branch and switches to it. It's equivalent to running `git branch <branch_name>` followed by `git checkout <branch_name>`. This command is useful when you're starting a new feature or bugfix.

---

#### `git push -u origin <branch_name>`

This pushes your local branch to the remote repository (`origin`). The `-u` flag sets the upstream branch, meaning future pushes and pulls on this branch will be automatically linked to this remote branch. After running this command once, you can simply use `git push` or `git pull` without specifying the branch name.

---

#### `git rebase <branch_name>`

This command is used to apply your local commits on top of another branch (e.g., `master`). Rebasing rewrites the commit history and makes it as if you started your work from the most recent commit on the branch you're rebasing onto.

---

#### `git rebase origin/master`

This is similar to `git rebase <branch_name>`, but it applies your local commits on top of the remote `master` branch (`origin/master`). It’s useful if you’ve made commits on your branch and want to bring in the latest changes from `master` before pushing your branch.

**Note**: `git fetch` retrieves updates (commits, branches, and tags) from a remote repository and updates the corresponding remote-tracking references in the local repository without integrating those changes into the current working branch. In contrast, `git pull` performs a `fetch` followed by an integration step—by default a merge (or optionally a rebase)—thereby incorporating the retrieved changes into the active local branch.

---

### 4. **Git Workflow: Normal and Special Circumstances**

Here's how the commands fit into typical Git workflows, along with scenarios where conflicts might arise and how to handle them.

#### **Normal Workflow**:

1. **Clone a repository**: If you haven’t already cloned the repository, you can use:

   ```bash
   git clone <repository_url>
   ```

2. **Create a new branch** for your work:

   ```bash
   git checkout -b feature-xyz
   ```

3. **Make changes**, add and commit them:

   ```bash
   git add <file_name>
   git commit -m "Added feature X"
   ```

4. **Fetch changes** from the remote:

   ```bash
   git fetch
   ```

5. **Merge or rebase** the remote changes:

   ```bash
   git merge origin/master
   ```

   Or, if you prefer rebasing:

   ```bash
   git rebase origin/master
   ```

6. **Push your changes**:

   ```bash
   git push -u origin feature-xyz
   ```

#### **Handling Conflicts**:

* Conflicts occur when changes in the remote branch and your local branch affect the same part of the code.
* **Merge conflicts** happen when Git cannot automatically merge the two versions of a file. You’ll need to manually resolve conflicts:

  1. Git will mark the conflicting areas in the file. You’ll see conflict markers like `<<<<<<`, `======`, and `>>>>>>`.
  2. Edit the file to keep the changes you want and remove the conflict markers.
  3. After resolving the conflict, stage the file and commit the changes:

     ```bash
     git add <file_name>
     git commit
     ```

#### **Dealing with Remote Branches**:

* When working in a team, you’ll often need to **merge** or **rebase** with the `master` or `main` branch to keep your work updated.
* Always **fetch** the latest changes from the remote before starting your work to minimize conflicts later:

  ```bash
  git fetch
  ```

#### **If You Get Behind**:

If you’ve fallen behind on the remote branch and your branch needs to be synchronized:

1. **Rebase** your changes:

   ```bash
   git fetch
   git rebase origin/master
   ```
2. If rebasing is not suitable, you can merge:

   ```bash
   git merge origin/master
   ```

---

### 5. **Other Special Commands**

* **git stash**: Saves your uncommitted changes temporarily, so you can switch branches without losing your work.

  ```bash
  git stash
  ```

* **git pull --rebase**: This option is used to fetch changes from the remote and rebase them onto your local branch instead of merging. It’s helpful to maintain a cleaner commit history.

---

### 6. **Best Practices**

* **Commit often**, but only commit meaningful changes.
* **Pull frequently** to stay up-to-date with the team.
* Use **rebase** to maintain a clean and linear history, especially when integrating with the master/main branch.
* **Push early and often** to share your progress and avoid losing work.
* When resolving conflicts, always make sure to communicate with your team to avoid overwriting each other’s changes.

---

### Summary:

To connect to a remote repository, use `git remote add origin <repository_url>`. Once you're connected, you can fetch changes, merge them, and push your work. Conflicts happen when Git cannot auto-merge changes, but with a little practice, conflict resolution becomes straightforward. Keeping your branches in sync with `git pull` or `git fetch` + `git merge` or `git rebase` ensures that your local repository stays up-to-date with the remote.