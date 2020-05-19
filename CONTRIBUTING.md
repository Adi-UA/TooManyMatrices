# For Contributors Only

This document provides some general guidelines and starter tips for contributors to follow. If any part of this document seems archaic or even downright terrible, please feel free to suggest changes through a pull request.

## Getting Started

Assuming you have git installed, to get started all you need to do is:

* Run `git clone https://github.com/Adi-UA/TooManyMatrices.git` in your terminal.

For Widnows [Git Bash](https://gitforwindows.org/) is reccomended if you want the other commands in this doc to work, but equivalent commands in Powershell still obviously work.

## Workflow

The master branch should always contain a usable version of the project. This means pushing directly to the master branch is not allowed; all modifications must be made through pull requests.
To add a new feature (assuming you are inside the project directory):

* Run `git checkout -b feature` where feature is the name of the new branch in which you will make your changes.
* Implement your changes.
* After you've made your changes, run: `git add <file1> <file2> ... <fileN>` to stage the changes to those files. Generally, you shouldn't use `git add .` because that way you can be sure you're not accidentally trying to change files you din't mean to. It also encourages cleaner commits.
* Now you can commit the staged changes. 
    * If your commit message is small then simply run `git commit -m "A short description of the changes"`.
    * If you need to write a longer commit message, run `git commit` and write the changes in the commit file.
* Push your changes 
    * If you're pushing to the remote branch for the first time, run `git push --set-upstream origin feature`
    * Otheriwse run `git push`
* Repeat the previous 4 steps as necessary on the new `feature` branch and when the changes are ready to merge into master, create a pull request from the Github website for [this repository](https://github.com/Adi-UA/TooManyMatrices). Remember to write good titles and descriptions when you open pull requests.
* All pull requests must be reviewed by at least one person including [@Adi-UA](https://github.com/Adi-UA).

* Once the feature branch ahs been merged into master, do the following:
    * Switch back to the master branch with `git checkout master`
    * Pull the latest changes with `git pull`
    * Delete your local copy of the feature branch with `git branch -D feature`

* **NOTES** 
    * Whenever possible create small pull requests. Smaller additions and modifications are easier to review, so it's better not to open pull requests that make multiple huge changes all at once.
    * If you're in the middle of implementing some feature on a branch and a pull request is closed in the master branch,
    you should (assuming you're on your feature branch) run `git pull origin master` and then resolve any merge conflicts that arise.
