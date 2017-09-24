title: Git for research work
date:2017-02-11
tags: Git
category: How To
author: Abraham Vinod
summary: List of useful features (and the corresponding commands in git)
URL: gitCheatSheet.html
save_as: gitCheatSheet.html

# Introduction

While diligently doing your research, have you ever felt

1. Oh, shoot! I changed the code in my home computer but forgot to email myself a copy so that I run it out in my lab. Help?!
1. Oh, shoot! I edited away my code from a point where *something* was working to a point where *nothing* is working. Help?!
1. Oh, shoot! My friend added a new feature to a legacy code, and I added a couple of new features myself, but now we want to combine our forces! I don't want to manually merge the two codes by going over them line by line. Help?!
1. Oh, shoot! I was editing a file on Overleaf[^overleaf], and something went wrong. Now, I want to go back, but I don't have a premium account. Help?!

[Git](https://git-scm.com) can solve all these problems for you!!!  The aim of
this blog post is **not** to describe how to use git. I will answer how to solve
the above problems directly and will leave it to you learn more about git. One
of the best online tutorial posts on git which is easy on the eyes is
[http://rogerdudler.github.io/git-guide/](http://rogerdudler.github.io/git-guide/).

Also, do checkout [this blog post]({filename}14 - gitsubmodules.md) to learn how I
use `git submodules` with Overleaf to keep track of all my research papers.


# What is Git?

Git is a version control system (VCS) for tracking changes in computer files and coordinating work on those files among multiple people[^wikiGit]. It is primarily used for software development, but it can be used to keep track of changes in any files. As a distributed revision control system it is aimed at speed, data integrity, and support for distributed, non-linear workflows.

## How do I use it?

If you are using Windows[^UnixGit], you can grab a copy of Git (bash terminal and the software) from [https://git-scm.com/downloads](https://git-scm.com/downloads).

You will also need an account on [http://www.github.com](http://www.github.com) or [http://www.bitbucket.org](http://www.bitbucket.org). These services allow you to configure a remote git repository that serves as a common meeting place for your code distributed across multiple computers.  I prefer [BitBucket](http://www.bitbucket.org/abyvinod) since they give unlimited private repositories (you don't want your research code out in public, do you?). [Github](http://www.github.com/abyvinod), on the other hand, provides unlimited public repositories and require a subscription to avail private repositories. Note however that industry prefers Github because it has traditionally been used for open-source software. This blog has been hosted using [Github](https://pages.github.com/).

Learning git isn't very hard. There are just a few commands to do some useful tasks, and once you get the hang of it, it will look intuitive. Here are some cheatsheets available online

+ [https://www.git-tower.com/blog/git-cheat-sheet/](https://www.git-tower.com/blog/git-cheat-sheet/)
+ [http://rogerdudler.github.io/git-guide/files/git_cheat_sheet.pdf](http://rogerdudler.github.io/git-guide/files/git_cheat_sheet.pdf)
+ [http://nyuccl.org/pages/gittutorial/](http://nyuccl.org/pages/gittutorial/)

As I mentioned before, do check out [http://rogerdudler.github.io/git-guide/](http://rogerdudler.github.io/git-guide/).

# Solution to Problem 1: Version control your files across computers

One of the popular solutions to the first problem is to use Dropbox. It is not a bad solution, but I hate the '.conflicted' reports that keep coming, and I don't think Dropbox provides enough space for us to put all our research data and codes. 

Once you get the hang of git, the answer to this pretty simple. Make a git
repository for your research codes. Use it to version control your code between
your home computer and work computer. You can even use `bash` script to automate
the "syncing" of the git repositories. Here is my `gua` (git update all) script that I run every time I leave a computer to ensure that there are no uncommitted changes in my local repository.

~~~bash
echo " "
echo "================================="
echo " "
echo "Going to Matlab"
echo ""
echo " "
gm                      # My bash alias for going to my matlab folder
git status
git pull
echo " "
echo "================================="
echo " "
echo "Going to vimfiles"
echo " "
echo " "
gv                      # My bash alias for going to my vimfiles folder
git status
git pull
~~~
Of course, this has not completely solved the problem. What happens when I
forget to run the `gua` script **before** leaving the computer??? Well, I use remote desktop connection to connect to my work computer/home computer. :)

**Caution!**: Don't you use git to keep track of data. Depending on your format,
it might just consider it as a binary blob or as a txt file, and unnecessarily
keep track of the incremental changes to data. Use Dropbox or any other cloud
storage solutions to store data.

# Solution to Problem 2: Version control your files across computers

Use `gitk` to get a nice GUI on your changes.  

`git diff` to compare two versions of your codes, drafts, etc.

From now, you don't have to worry about accidently changing the code on a late Monday night.

# Solution to Problem 3:  Using git to merge codes

Let us say we have two codebases --- CB_A and CB_B --- that forked from the legacy code. Let us say the legacy code CB_L has a git repository. If not, create one for it using `git init`. The key idea will be to use git branching to handle the merging.  Do the following:

~~~bash
# Let us say we are on the legacy codebase CB_L's git repository and it is on
# the master branch. Create a new git branch named CB_A from the current point
# of legacy code. This branch will be used to store the code base CB_A
git checkout -b CB_A    
# Overwrite this branch of legacy code with the code base CB_A (Do your stuff)
# Commit your changes in this branch with git commit (Do your stuff)
# Go back to the legacy code CB_L
git checkout master     
# Create a new git branch named CB_B from the current point of legacy code. This
# branch will be used to store the code base CB_B
git checkout -b CB_B    
# Overwrite this branch of legacy code with the code base CB_B (Do your stuff)
# Commit your changes in this branch with git commit (Do your stuff)
# Go back to the legacy code CB_L
git checkout master     
# Create a new git branch named CB_merge from the current point of legacy code.
# This will store the merged code.
git checkout -b CB_merge
# This will merge CB_A to the branch CB_merge. This should happen without any
# hiccups. (Now, CB_A will be identical to CB_merge. Check using gitk)
git merge CB_A          
# Major step: This will merge CB_B to the branch CB_merge containing CB_A
# codebase. This will potentially yield conflicts because they share the same
# ancestor node but have different changes. However, git will list out the files
# that have conflict and also demarcate the lines. Manually fix them, and now you have successfully merged codes with minimal effort form your side.
git merge CB_B          
# In case you want to update the legacy code with your newly merged working code
git checkout master
git merge CB_merge          
~~~

# Solution to Problem 4: Using git with Overleaf

Overleaf is a collaborative writing and publishing system that makes the whole
process of producing academic papers much quicker for both authors and
publishers[^overleaf]. It is a free service that lets you create, edit and share
your scientific ideas easily online using LaTeX[^latex], a comprehensive and powerful tool for scientific writing.

You can read about how to use git to version control your papers on Overleaf from [https://www.overleaf.com/blog/195-new-collaborate-online-and-offline-with-overleaf-and-git-beta](https://www.overleaf.com/blog/195-new-collaborate-online-and-offline-with-overleaf-and-git-beta). 

Based on the instructions given in the link above, you will have to create a
local git repository for every Overleaf paper. Another alternative is to use
submodules. See [this blog post]({filename}14 - gitsubmodules.md) to know how I
use it to track all my research papers while staying safe from the pain points
of submodules.


[^UnixGit]: If you are in Unix, you can install it using your package manager.
[^wikiGit]: [Wikipedia link for git](https://en.wikipedia.org/wiki/Git)
[^overleaf]: [Overleaf website](https://www.overleaf.com/about), 
[^latex]: [Wikipedia link for LaTeX](https://en.wikipedia.org/wiki/LaTeX)
