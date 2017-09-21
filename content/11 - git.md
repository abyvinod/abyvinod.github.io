title: Git for research work
date:2017-02-11
tags: Git
category: How To
author: Abraham Vinod
summary: List of useful features (and the corresponding commands in git)
URL: gitCheatSheet.html
save_as: gitCheatSheet.html

While diligently doing your research, have you ever felt

+ Oh, shoot! I changed the code in my home computer but forgot to email myself a copy so that I run it out in my lab. Help?!
+ Oh, shoot! I edited away my code from a point where *something* was working to a point where *nothing* is working. Help?!
+ Oh, shoot! I was editing a file on [Overleaf](http://www.overleaf.com), and something went wrong. Now, I want to go back, but I don't have a premium account. Help?!
+ Oh, shoot! My friend added a new feature to a legacy code, and I added a couple of new features myself, but now we want to combine our forces! I don't want to manually merge the two codes by going over them line by line. Help?!

[Git](https://git-scm.com) can solve all these problems for you!!!  The aim of this blog post is **not** to describe how to use git. While I dedicate first three sections on describing the what and how of git, I will leave it to you learn more about git. One of the best online tutorial posts on git which is easy on the eyes is [http://rogerdudler.github.io/git-guide/](http://rogerdudler.github.io/git-guide/).

# What is Git?

Quoting from [Wikipedia](https://en.wikipedia.org/wiki/Git), git is a version control system (VCS) for tracking changes in computer files and coordinating work on those files among multiple people. It is primarily used for software development, but it can be used to keep track of changes in any files. As a distributed revision control system it is aimed at speed, data integrity, and support for distributed, non-linear workflows.

## How do I use it?

I will describe how to use it if you are using Windows[^UnixGit]. You can grab a copy of Git (bash terminal and the software) from [https://git-scm.com/downloads](https://git-scm.com/downloads).

You will also need an account on [http://www.github.com](http://www.github.com) or [http://www.bitbucket.org](http://www.bitbucket.org). These services allow you to configure a remote git repository that serves as a common meeting place for your code distributed across multiple computers.  I prefer [BitBucket](http://www.bitbucket.org/abyvinod) since they give unlimited private repositories (you don't want your research code out in public, do you?). [Github](http://www.github.com/abyvinod), on the other hand, provides unlimited public repositories and require a subscription to avail private repositories. Note however that industry prefers Github because it has traditionally been used for open-source software. This blog has been hosted using [Github](https://pages.github.com/).

## Incorporating git into your workflow 

Learning git isn't very hard. There are just a few commands to do some useful tasks, and once you get the hang of it, it will look intuitive. Here are some cheatsheets available online

+ [https://www.git-tower.com/blog/git-cheat-sheet/](https://www.git-tower.com/blog/git-cheat-sheet/)
+ [http://rogerdudler.github.io/git-guide/files/git_cheat_sheet.pdf](http://rogerdudler.github.io/git-guide/files/git_cheat_sheet.pdf)
+ [http://nyuccl.org/pages/gittutorial/](http://nyuccl.org/pages/gittutorial/)

As I mentioned before, do check out [http://rogerdudler.github.io/git-guide/](http://rogerdudler.github.io/git-guide/).

# Answering the HELPME questions

I will answer the first two questions using the next subsection. Others have their own subsections.

## Keeping track of files across computers

One of the popular solutions to the first problem is to use Dropbox. It is not a bad solution, but I hate the '.conflicted' reports that keep coming, and I don't think Dropbox provides enough space for us to put all our research data and codes. 

Once you get the hang of git, the answer to this pretty simple. Make a git repository for your research codes. Use it to version control your code between your home computer and work computer. You can even use `bash` script to automate the "syncing" of the git repositories. Here is my `gu` script that I run every time I leave a computer to ensure that there are no uncommitted changes in my local repository.

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
git submodule foreach git pull
echo " "
echo "================================="
echo " "
echo "Going to vimfiles"
echo " "
echo " "
gv                      # My bash alias for going to my vimfiles folder
git status
git pull
git submodule foreach git pull
~~~
Git submodules are a cool way to have git repositories inside git repositories.  More details later in this article.

Of course, this has not completely solved the problem. What happens when I forget to run the gu script **before** leaving the computer??? Well, I use remote desktop connection to connect to my work computer/home computer. :)

**Caution!**: Don't you use git to keep track of data. Depending on your format, it might just consider it as a binary blob or as a txt file, and unecessarily[^Unless], keep track of the incremental changes to data. Use Dropbox or any other cloud storage solutions to store data.

To answer the second question, use `gitk` to get a nice GUI on your changes.  `git diff` is another option. From now, you don't have to worry about accidently changing the code on a late Monday night.

## Using git with Overleaf

Quoting from [Overleaf website](https://www.overleaf.com/about), Overleaf is a collaborative writing and publishing system that makes the whole process of producing academic papers much quicker for both authors and publishers. It is a free service that lets you create, edit and share your scientific ideas easily online using [LaTeX](https://en.wikipedia.org/wiki/LaTeX), a comprehensive and powerful tool for scientific writing.

You can read about how to use git to version control your papers on Overleaf from [https://www.overleaf.com/blog/195-new-collaborate-online-and-offline-with-overleaf-and-git-beta](https://www.overleaf.com/blog/195-new-collaborate-online-and-offline-with-overleaf-and-git-beta). In this section, I will explore another feature of git to go a step further.

Based on the instructions given in the link above, you will have to create a local git repository for every Overleaf paper. An alternative is to use submodules.

**Update**: A really good article on submodules is given in
[https://medium.com/@porteneuve/mastering-git-submodules-34c65e940407](https://medium.com/@porteneuve/mastering-git-submodules-34c65e940407).
He gives an excellent description of the steps involved while dealing with
submodules. Look into his
[TL;DR](https://medium.com/@porteneuve/mastering-git-submodules-34c65e940407#5450)
section for a quick overview of the steps.

### Using submodules

A detailed exposition can be found in [https://git-scm.com/book/en/v2/Git-Tools-Submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules).  I will focus on the important commands.

#### Adding projects

I add new Overleaf projects into my main git repository via the following command

~~~bash
git submodule add https://git.overleaf.com/PROJECT_NUMBER.git PATH_TO_SAVE_THE_PROJECT
~~~

The `PROJECT_NUMBER` can be obtained from the `Share` button in the menu of your
Overleaf project page. This command will clone the git repository for your
Overleaf project into your git repository. In this section, I will call my main
git repository `Parent` sitting on the location `C:/git` and the overleaf
project `OverleafProject`. Hence, the command to clone an existing overleaf
project (with project number `1234567890123456789`) as a submodule becomes

~~~bash
cd /c/git/Parent
mkdir Papers
git submodule add https://git.overleaf.com/1234567890123456789.git Papers/OverleafProject
~~~

Running `git status` shows that new files `.gitmodules` and `Papers/OverleafProject` were created. Commit and push the repository to your remote (at Bitbucket/Github) for making this submodule accessible to other computers as well. The git in `Parent` repository just keeps track of the commit currently the HEAD of `Papers/OverleafProject` points to.

If you change directory into `Papers/OverleafProject` and run `gitk`, you will see that git sees this folder as an independent git repository with none of the history of the git repository `Parent` appearing here. Changing codes here needs to be pushed independently, and they will influence your Overleaf project.

** Caution**: Overleaf creates a git repository only when you attempt to clone it for the first time. Their premium account is the only way (I know of) to handle changes that happened before cloning the repository.

After changing the files inside `Paper/OverleafProject`, if you change directory back to `Parent` and type `git status`, you will see the true power of git submodules. The changes in the submodules are summarized. Pushing these changes in the `Parent` repository into the remote repository (git repository at Bitbucket/Github) will trigger other local repositories (other computers) linked to this remote repository to update their copies of submodules.

#### Fetching submodules in other local repositories

The subsection above described how to add submodules to your project and push it to the remote repository. Let us know move to another local repository that is linked to this remote repository. To fetch all the submodule information, do the following

~~~bash
# Two options for getting submodules
# Option 1: Init and then update
git submodule init                          # Fetch all the submodule information linked to this git repository
git submodule update                        # Clone the submodules into their respective locations
# Option 2: Update while init
git submodule update --init
# Avoid the detached HEAD (the normal state after checking out a submodule)
git submodule foreach git checkout master   # Checkout the master branch in each of these submodules
~~~
The last command is to avoid a `detached HEAD`[^detHEAD].

#### Moving the git submodule around

More often than not, we will reorganize our folders, and we will require the git submodules to be moved from a place to another. Let us say we want to move `Papers/OverleafProject` and put it in `Papers/Done/OverleafProject`. Achieve this[^submmv] by (no matter where you are currently in the git repository `Parent`)

~~~bash
git mv Papers/OverleafProject Papers/Done/OverleafProject
# Remove the .git/modules/FOLDER to make the old projectname free for reuse
rm -rf `.git/modules/Papers/OverleafProject`
~~~

`Papers/OverleafProject` is the old name (location) of the submodule. Check in `Parent/.gitmodules` to confirm. Doing a git push will update your remote repositories. 

#### Updating the submodules on the other computers

~~~bash
# Get the changes in the parent repo
git pull
# Sync the URL for the local .gitmodules
git submodule sync --recursive
# Update the repositories with the latest commit, initialize any new repos if (needed), and do this in a recursive manner
git submodule update --init --recursive
# Avoid the detached HEAD (the normal state after checking out a submodule)
git submodule foreach git checkout master
~~~

You may have to clean up the submodules that have been moved or deleted. They
will show up as untracked folders.
~~~bash
rm -rf SUBMODULE_FOLDER
~~~

#### Deleting a git submodule

Once you are done with a research paper, you may want to burn the bridge to the Overleaf project and just retain the files. Do the following[^submdelete]

~~~bash
git submodule deinit SUBMODULE_FOLDER # Deinits the submodule (opposite of submodule init)   
# There are two options for the next step
git rm PATH/TO/SUBMODULE_FOLDER          # Option 1: Remove the submodule from git as well as your storage unit
git rm --cached PATH/TO/SUBMODULE_FOLDER      # Option 2: Remove the submodule from git, but leave it on your storage unit
# Remove the .git/modules/PATH/TO/SUBMODULE_FOLDER to make the old projectname free for reuse
rm -rf `.git/modules/PATH/TO/SUBMODULE_FOLDER`
~~~

## Using git to merge codes

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
        

[^UnixGit]: If you are in Unix, you can install it using your package manager.
[^submmv]: Source --- [http://stackoverflow.com/a/6310246/1846549](http://stackoverflow.com/a/6310246/1846549)
[^detHEAD]: Read
[https://www.git-tower.com/learn/git/faq/detached-head-when-checkout-commit](https://www.git-tower.com/learn/git/faq/detached-head-when-checkout-commit)
if you want to know more.
[^submdelete]: Source ---
[http://stackoverflow.com/a/16162000/1846549](http://stackoverflow.com/a/16162000/1846549)
