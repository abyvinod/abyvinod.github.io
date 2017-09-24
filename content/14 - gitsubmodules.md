title: Using git submodules to keep track of your Overleaf papers
date:2017-09-23
tags: Git, Overleaf, Tips
category: How To
author: Abraham Vinod
summary: Git submodules can keep track of your overleaf papers in one place
URL: gitsubmodules.html
save_as: gitsubmodules.html

# Introduction

In [a previous blog post]({filename}11 - git.md), I described how awesome git is.
Especially, with Overleaf, doing collaborative editing of papers has become
extremely easy. However, I don't like using Overleaf editor and do all my edits
on my computer (*vim* FTW). But, this made the task of keeping my local copy of
papers up-to-date challenging as my number of Overleaf documents
grew.

I wanted to create a single git repository that will:

1. serve as a single stop to get all of my papers
1. sync with Overleaf
1. preserve version control powers given by git+Overleaf[^gitOverleaf]
1. remain portable (easy to transfer/sync across multiple computers)

For this, I turned to `git submodules`. The steps in this article were tested
for git version of `2.13`. However, the `git submodules` has its own
    pitfalls[^medium].  This blog post is about my custom commands to use git
    submodules to achieve the tasks listed above.

### Sources for this article

This article was driven by an excellent article on submodules by Mr.
Porteneuve[^medium].  He gives an excellent description of git submodules, the
steps to take, and the pitfalls to deal with. Do look into his TL;DR section for
a quick overview of the steps.  The git documentation[^gitdoc] helped as well.
So did countless Google searches, and the blog posts and stack-overflow posts they
led to.

# What are git submodules?

Submodules allow you to keep a Git repository as a subdirectory of another Git
repository. This lets you clone another repository into your project and keep
your commits separate.  A detailed exposition can be found in git-scm
book[^book].

# What are the important tasks that I need to handle?

Let the parent repository be `Papers`.

1. Add new Overleaf projects to `Papers`.
1. Move Overleaf projects around (renaming or different categorization) within
`Papers`.
1. Update the local copies of the Overleaf projects in `Papers`.
1. Delete Overleaf projects from `Papers`.
1. Clone `Papers` in a different computer.
1. Check if there are any changes in the local copies of the papers.

## Task 1: Add new Overleaf projects to the repository

Overleaf associates a project number to every project. Clicking on `SHARE` on
the topbar gives you a git repository for the same of the format
`https://git.overleaf.com/PROJECT_NUMBER`. Let the `OVERLEAF_URL` denote the
URL.

We can add a new Overleaf project into the repository `Papers` using `git
submodule add` command. Let `PATH_TO_SAVE_THE_PROJECT` be the desired path to
the local copy (obviously `PATH_TO_SAVE_THE_PROJECT` has the structure
`PATH_TO_PAPERS/*`). 

**NOTE 1**: The submodule, by default, is checked out into a detached
head[^detHEAD] to prevent overwrite. 
<a name=NOTE2></a>

**NOTE 2**: Skip steps 2 and 3 if you want to go with the complicated
alternatives of using `git submodule sync` and `git submodule update`. These
options are discussed in their respective tasks.

~~~bash
# Add the project to the repository
git submodule add OVERLEAF_URL PATH_TO_SAVE_THE_PROJECT
# Make the parent repository ignore any future commits (Disable git submodule's tracking capabilities)
git config submodule.PATH_TO_SAVE_THE_PROJECT.ignore all
# Set ignore=all in .gitmodules to propagate this to remote repository of Papers
vim .gitmodules # Make appropriate changes
# Shift to master branch from a detached head state
cd PATH_TO_SAVE_THE_PROJECT
git checkout master
~~~

Running `git status` shows that new files `.gitmodules` and
`PATH_TO_SAVE_THE_PROJECT` were created. Because we have set `ignore` to `all`,
the `Papers` repository will ignore any future commits to the repository. 

Doing a `git commit` and `git push` after these steps will inform your remote
repository for `Papers` about the new submodule.

## Task 2: Move Overleaf projects around within the repository

More often than not, we will have to reorganize our folders. We would have to
move the git submodules from a place to another. 

Let us say we want to move `Papers/OverleafProject` and put it in
`Papers/Done/OverleafProject`. Based on this SO answer[^submmv], we have the following steps

~~~bash
git mv Papers/OverleafProject Papers/Done/OverleafProject
# Using your favorite editor, edit .gitmodules so that the submodule name and the path variables are the same
vim .gitmodules # Make appropriate changes
# Move the .git/modules/FOLDER to the new Project
mv .git/modules/Papers/OverleafProject .git/modules/Papers/Done/OverleafProject
# Update your .git/config file on the Papers repo with the updated path for the submodule
vim .git/config     # Make appropriate changes
# Using your favorite editor, edit the .git file within the submodule to reflect the updated path
cd Papers/Done/OverleafProject
vim .git # Make appropriate changes
~~~

Doing a `git commit` and `git push` after these steps will inform your remote
repository for `Papers` about the changes in the submodule. 

**NOTE 3**: You can edit `.gitmodules` and `.git/config` files to change the
remote repository of the submodule as well.

## Task 3: Update the local copies of the Overleaf projects in the repository

### Updating using custom command (Easy option)

The commands to update submodules are very simple (the main goal of this endeavor).

#### Updating a specific submodules

~~~bash
cd PATH_TO_SAVE_THE_PROJECT
git pull
~~~

#### Updating all the submodules

~~~bash
git submodule foreach git pull
~~~

### Updating using git submodule update (Complicated alternative)
An alternative is to use `git submodule update --init`, the original approach
via `git submodules`. 
<a name=NOTE4></a>

**NOTE 4**: We will make the following assumptions for the complicated alternative.

1. Papers repository has the latest commit and updated `.gitmodules`.
See[^mediumSection] for the steps. You will have to edit your `.git/config` to
have `ignore` key of every submodule set to `none`. The default option is `none`
but we changed it to `all` in our solution to Task 1 (See [**NOTE 2**](#NOTE2)).
2. All submodules have no unpushed commits (Else update step will reset their commits)

To satisfy the assumptions in **NOTE 4**, we would have to do two pushes for
every commit in a submodule[^mediumSection]. This is an overkill for our
`Papers` repo and a pain point (especially when we are on an editing spree).
Missing a commit of the submodule for the `Paper` repo opens up the potential
danger of dropping the submodule commits done in another machine[^medium].

~~~bash
# Get the changes in the parent repo
git pull
# Sync the URL for the local .gitmodules in case the remote repos of the submodules have changed
git submodule sync
# Update the repositories with the latest commit, initialize any new repos if (needed)
git submodule update --init
# Avoid the detached HEAD (the normal state after checking out a submodule)
git submodule foreach git checkout master
~~~

Adding a `--recursive` flag to `sync` and `update` commands allows git to
perform these operations for nested submodules.


## Task 4: Delete Overleaf projects from the repository

Once you are done with a research paper, you may want to burn the bridge to the Overleaf project and just retain the files. Do the following[^submdelete]

~~~bash
git submodule deinit SUBMODULE_FOLDER # Deinits the submodule (opposite of submodule init)   
# There are two options for the next step
# Option 1: Remove the submodule from git as well as your storage unit
git rm PATH/TO/SUBMODULE_FOLDER
# Option 2: Remove the submodule from git, but leave it on your storage unit
git rm --cached PATH/TO/SUBMODULE_FOLDER
# Make the old project path free for reuse by doing both of the following steps
# 1. Removing the .git/modules/<Submodule> folder
rm -rf `.git/modules/PATH/TO/SUBMODULE_FOLDER`
# 2. Editing the .git/config and erasing any reference to its existence
vim .git/config     # Make appropriate changes
~~~

## Task 5: Maintaining repositories across different computers

Subsections above handled all the desired tasks within a single machine. Now,
let us discuss how to clone the repository and sync our papers to another machine. 

### Using custom commands (Easy option)

Clone the paper repository with all the submodules and update them
individually
~~~bash
git clone --recursive-submodules <PAPERS_REPO_LINK> Papers
git submodule foreach 'git checkout master && git pull'
~~~
That's all!!! You should now be able to do any of the steps
mentioned in Tasks 1--4 in the new machine without any hiccups.

### Using git submodule sync and git submodule update (Complicated alternative)

The assumptions made in [**NOTE 4**](#NOTE4) hold here.

#### Cloning
~~~bash
# Two options for getting submodules
# Option 1: Clone the paper and then recurse
git submodule init                          # Fetch all the submodule information linked to this git repository
git clone <PAPERS_REPO_LINK> Papers
cd Papers
git submodule update --init                 # Clone the submodules into their respective locations
# Option 2: Clone the paper and submodules recursively
git clone --recursive-submodules <PAPERS_REPO_LINK> Papers
# Avoid the detached HEAD (the normal state after checking out a submodule) & update all the submodules to their latest commit
git submodule foreach 'git checkout master && git pull'   # Checkout the master branch in each of these submodules and pull
~~~

#### Updating changes
~~~bash
# Synchronize your local copy of Papers repository and the submodules based on the .gitmodules
git submodule sync --recursive
# Update the repositories
git submodule update --init
# Avoid detached state
git submodule foreach git checkout master
~~~

## Task 6: See if there are any changes in the local copies

~~~bash
git submodule foreach git status    # Cycle through all the submodules and print the status
~~~

This is easily done in the `git submodule update,sync` approach (our so-called
complicated alternative) via `git status` on the `Paper` repository.

# Comparing the two approaches

The easy option differs from the complicated alternative in Tasks 1, 3, and 5.

The advantages of the easy option are:

1. Makes Tasks 3 and 5 extremely easy (the most commonly performed tasks)
1. Does not have the pitfalls associated with `git submodules`[^medium]. Your changes
will never be accidentally overwritten. (Phew!)

The disadvantages of the easy option are:

1. Task 1 has two additional minor steps.
1. Requires additional scripts to update only certain submodules. It can be done
with `git submodule update,sync` approach but is not easy either. See *providing
pathspec* in git documentation[^gitdoc].


[^gitOverleaf]: Overleaf now supports git
[https://www.overleaf.com/blog/195-new-collaborate-online-and-offline-with-overleaf-and-git-beta](https://www.overleaf.com/blog/195-new-collaborate-online-and-offline-with-overleaf-and-git-beta).
[^medium]: Read [https://medium.com/@porteneuve/mastering-git-submodules-34c65e940407](https://medium.com/@porteneuve/mastering-git-submodules-34c65e940407)
[^gitdoc]: Relevant git documentations --- [https://git-scm.com/docs/git-config](https://git-scm.com/docs/git-config),
[https://git-scm.com/docs/git-submodule](https://git-scm.com/docs/git-submodule),
and [https://git-scm.com/docs/gitmodules](https://git-scm.com/docs/gitmodules).
[^book]: Git-scm book [https://git-scm.com/book/en/v2/Git-Tools-Submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules).  
[^detHEAD]: Read
[https://www.git-tower.com/learn/git/faq/detached-head-when-checkout-commit](https://www.git-tower.com/learn/git/faq/detached-head-when-checkout-commit)
if you want to know more.
[^submmv]: Source --- [http://stackoverflow.com/a/6310246/1846549](http://stackoverflow.com/a/6310246/1846549)
[^mediumSection]: See section *Updating a submodule inside container code*
in Mr. Porteneuve's article[^medium]. 
[^submdelete]: Source ---
[http://stackoverflow.com/a/16162000/1846549](http://stackoverflow.com/a/16162000/1846549)
