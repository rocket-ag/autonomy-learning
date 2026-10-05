# Git Notes

## 1. What is a Git repository?

A Git repository is a directory whose contents are tracked and managed by Git. When `git init` is run, Git creates a hidden `.git` directory containing the information Git needs to track the project's history, including commits, branches, configuration, and references to other repository objects.

The repository consists of both the working files that I interact with and Git's internal database inside `.git`.

For example:

autonomy-learning/
├── README.md
├── .gitignore
├── week01/
│   └── ...
└── .git/
    └── Git's internal data

The `.git` directory is what makes autonomy-learning a Git repository. Deleting `.git` would remove the repository's Git history and configuration while leaving the ordinary project files intact.

Git primarily tracks files and their changes rather than empty directories. This is why empty directories do not appear in Git's history unless they contain something such as a .gitkeep file.


## 2. What is the difference between the working directory and staging area?

The working directory contains the files I am currently working on. When I edit a file, the change initially exists only in the working directory.

The staging area, also called the index, contains the specific changes that I have selected to include in my next commit.

The basic workflow is:

Working Directory
       |
       | git add
       v
Staging Area
       |
       | git commit
       v
Git History

For example, if I modify README.md, the change initially exists only in my working directory. Running:

git add README.md

copies that version of the change into the staging area.

I can then modify README.md again without affecting the version that is already staged. This allows me to construct a commit deliberately rather than automatically committing every change currently in my working directory.


## 3. What is a commit?

A commit is a recorded snapshot of the project at a particular point in time.

A commit contains information about the state of the files that were staged when the commit was created, along with metadata such as the author, timestamp, commit message, and references to previous commits.

For example:

Commit A
   |
Commit B
   |
Commit C

Each commit provides a point that I can inspect or return to later.

Commits are useful because they create a historical record of how a project evolved. Instead of relying solely on the current state of files, I can determine what the project looked like at earlier points in development and compare different versions.

A good commit should generally represent a meaningful, coherent change and have a message describing what that change accomplished.


## 4. What is the difference between a local and remote repository?

A local repository is the Git repository stored on my computer. It contains my working files and the local copy of the Git history.

A remote repository is another copy of the repository stored somewhere else, such as GitHub.

In my project:

My computer
└── autonomy-learning
    └── .git/

GitHub
└── rocket-ag/autonomy-learning

The two repositories can exchange commits using commands such as:

git push

to send local commits to the remote, and:

git fetch

or:

git pull

to obtain information or changes from the remote.

The remote repository provides a backup of the project, facilitates collaboration, and allows the project to be accessed from other computers.


## 5. What does git status tell you?

git status shows the current state of my repository.

It tells me things such as:

- which branch I am currently on
- whether my working directory has modifications
- which files are untracked
- which changes have been staged
- whether my local branch is ahead of or behind its upstream branch
- whether there are conflicts or other repository conditions requiring attention

For example, Git might report:

Untracked files:
    test.py

This means Git sees test.py but I have not told it to track the file.

It might instead report:

Changes not staged for commit:
    modified: README.md

This means the file is tracked but has been modified since it was staged.

Or:

Changes to be committed:
    modified: README.md

This means the modification is currently staged and will be included in the next commit.

When everything is synchronized and there are no pending changes, Git reports:

nothing to commit, working tree clean

git status is therefore one of the most useful commands for understanding what Git thinks is currently happening.


## 6. What does git diff show?

git diff shows the differences between the working directory and the staging area.

It answers:

"What changes have I made that I have not staged yet?"

For example, suppose I have:

Working directory:
README.md = Version B

Staging area:
README.md = Version A

Then:

git diff

will show the difference between Version A and Version B.

Conceptually:

Working Directory
       |
       | git diff
       v
Staging Area

If the working directory and staging area contain identical versions of all tracked files, git diff will produce no output.


## 7. What does git diff --staged show?

git diff --staged shows the differences between the staging area and the most recent commit.

It answers:

"What exactly am I preparing to put into my next commit?"

For example:

git add README.md

stages a modification to README.md.

Then:

git diff --staged

shows that staged modification compared with the version contained in the most recent commit.

Conceptually:

Staging Area
       |
       | git diff --staged
       v
Latest Commit

This makes it particularly useful for reviewing a commit before actually creating it.

A useful workflow is:

git status
git diff
git add ...
git diff --staged
git commit

This lets me inspect both unstaged changes and the exact changes I am about to commit.


## 8. Explain git fetch vs. git pull

git fetch retrieves new commits and other information from a remote repository without changing my current working branch or working-directory files.

For example, suppose my local repository contains:

A -- B

while GitHub contains:

A -- B -- C

Running:

git fetch

downloads information about commit C and updates my local knowledge of the remote repository.

However, my current main branch can remain at B.

This makes fetch useful when I want to inspect incoming changes before incorporating them.

git pull goes further. Conceptually, it is:

git pull = git fetch + integrate the changes

It retrieves the remote changes and then attempts to integrate them into my current branch.

Therefore:

git fetch
    |
    v
Retrieve remote changes
    |
    v
Do not automatically change current branch

while:

git pull
    |
    v
Retrieve remote changes
    |
    v
Integrate them into current branch

The exact integration mechanism can involve merging or rebasing depending on configuration and the command used.


## 9. Explain git push

git push transfers commits from my local repository to a remote repository.

For example, if my local repository contains:

A -- B -- C

and GitHub contains:

A -- B

then:

git push

can transfer commit C to GitHub:

Local:                         GitHub:

A -- B -- C                   A -- B -- C

My first push used:

git push -u origin main

Each part has a purpose:

- git push means send local commits to a remote
- origin is the name of my remote repository
- main is the branch I am pushing
- -u establishes an upstream/tracking relationship between my local main and origin/main

The upstream relationship means Git remembers:

local main
    |
    |
origin/main

Consequently, future commands can usually be simplified to:

git push

because Git already knows that local main corresponds to origin/main.

The upstream relationship also allows commands such as git pull to know which remote branch corresponds to the current local branch.


## 10. Why is version control important for autonomous systems?

Version control is particularly important for autonomous systems because autonomous algorithms are often complex combinations of software, mathematical models, sensor-processing pipelines, configuration parameters, datasets, and experimental environments. A seemingly small change can significantly alter system behavior.

Suppose an autonomous vehicle's localization performance suddenly becomes worse. With version control, I can examine the commit history to determine:

- what changed
- when it changed
- which commit introduced the change
- who made the change
- whether the previous implementation can be restored

I can also compare a working version against a newer experimental version and return to a known-good version if necessary.

Version control also allows engineers to experiment safely. I can create a separate branch for an experimental algorithm, make changes without disturbing the main implementation, test the new approach, and eventually merge it if it works or discard it if it does not.

This is particularly valuable in autonomy because algorithms often evolve through experimentation. For example, I might experiment with:

- a different Kalman filter formulation
- a new sensor-fusion algorithm
- different computer-vision parameters
- a different motion-planning algorithm
- a new neural-network architecture

Version control provides traceability, reproducibility, collaboration, and controlled experimentation.

However, Git alone does not guarantee complete reproducibility. An autonomous experiment might also depend on a particular dataset, configuration, Python package version, random seed, simulation environment, or hardware configuration. Those dependencies should also be recorded or controlled when necessary.

For example:

Experiment
├── Git commit
├── source code
├── configuration
├── dataset
├── dependency versions
├── random seed
├── simulation conditions
└── results

This is particularly important when moving from simple coursework to real engineering systems because we ultimately care not merely that the code runs, but that we can explain and reproduce why the system behaved the way it did.
