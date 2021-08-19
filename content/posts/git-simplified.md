---
title: "Git simplified | A Git tutorial for beginners"
date: 2021-08-15T23:44:05+05:00
draft: false
---

## What is Git?

Git is a version control system. It means it can save multiple versions of files in a project. The project is simply just a folder to be used with git. That folder can contain anything e.g. source code of a program, images, Photoshop project file, videos, etc.

It is a program that saves everything locally on your computer i.e. it works offline

## What is a Git Repository?

A folder whose files and sub-folders are being saved/managed by Git is called a git repository or a git repo.

## What is GitHub?

GitHub is a website and a service owned by Microsoft. You can use it to upload your git repositories to the Internet. It has other advantages too. For example, it allows multiple people to work on the same project at the same time.

You don't have to use GitHub if you don't want to. GitLab and BitBucket are two famous alternatives to GitHub.

## Download/Install Git

### Windows

Click [here](https://git-scm.com/download/win) to download Git for Windows. Then double click the downloaded file and follow the on-screen instructions. Git should install successfully.

### Mac

First, install homebrew on your Mac. Then, run the following command in terminal to install Git:

```bash
brew install git
```

**OR**

Install Xcode from Apple App Store and it will automatically install Git.

### Linux

Use your favorite package manager to install Git. The package name is always git. You can run one of the following commands in terminal to install Git depending on your distro:

##### Debian/Ubuntu:

```bash
sudo apt install git
```

##### Arch/Manjaro:

```bash
sudo pacman -S git
```

##### Fedora/CentOS:

```bash
sudo dnf install git
```

## Set-Up/Configure Git

After installing git, open Terminal (or a Powershell window if you are on Windows) and then run the following commands

```bash
git config --global user.name "Your Name"
git config --global user.email "Your E-Mail Address"
git config --global init.defaultBranch main
```

## How to Create a git repository (locally)?

#### Use Case:

- When you need to turn a project (which you have already been working on) into a git repository

#### Method:

1. Create a new folder for your project if you don't already have a folder for your project
2. Open the folder of your project in File Explorer
3. Right click on empty space in File Explorer and Select '*Open Terminal Here*' from the menu that appears
   **Note:** Users of some versions of Windows may need to press and hold Shift key when they right click and Select '*Open Powershell window here*' from the menu that appears
4. Type `git init` and press Enter/Return key

Now, the folder is ready to be used by git.

## How to Create a git repository on GitHub?

#### Use cases:

- When you need to upload a git repository to the Internet
- When you need multiple people to work on the same project
- When you need to start a new project as a git repository

#### Method:

1. Go to https://github.com and create an account there
2. After creating an account, click on the green button labeled 'Create New Repository' and follow the on-screen instructions

A new GitHub repository should be created successfully by now

**Note:** If you want this GitHub repository to be a copy of a git repository on your local/personal computer, then make sure that the option 'Add readme.md' is **NOT** ticked and option 'License' is set to 'No License' in Step 2.

## How to Connect local and GitHub repositories

#### Use Cases:

- When you need to upload a non-empty local repository to GitHub

#### Important Notes:

- This works only if the GitHub repository (not the local repository) being connected is empty.
  **Note:** New repositories created without a readme.md and without a License are empty repositories.
- You don't need this if you cloned a repository because cloning a repo automatically connects the local and GitHub repositories.

#### Method:

1. Open the folder of your local git repository in File Explorer
2. Right click on empty space in File Explorer and Select '*Open Terminal Here*' from the menu that appears
   **Note:** Users of some versions of Windows may need to press and hold Shift key when they right click and Select '*Open Powershell window here*' from the menu that appears
3. Run the command `git remote add origin {repo-address}`. Replace the word `{repo-address}` with actual clone address of you GitHub repository.
4. Run either the command `git push -u` or `git push --set-upstream`
5. Done

## How to Clone a git repository

To clone a git repository means to download a complete git repository (not just latest version of files).

#### Use cases:

- When you need to compile, install and use someone else's program/project
- After creating GitHub repository of a new project that you have yet to start working on

#### Method:

1. Find address of a git repository
   For example: https://github.com/realmazharhussain/gdm-toools.git
   or `git@github.com:realmazharhussain/gdm-tools`
2. Open a folder in which you want to download/clone the git repository
3. Right click on empty space in File Explorer and Select '*Open Terminal Here*' from the menu that appears
   **Note:** Users of some versions of Windows may need to press and hold Shift key when they right click and Select '*Open Powershell window here*' from the menu that appears
4. Type the command `git clone {repo-address}` and press Enter/Return key.
   **Note:** Replace the word '{repo-address}' with actual address of the git repository
   For example, `git clone https://github.com/realmazharhussain/gdm-tools.git`
   or `git clone git@github.com:realmazharhussain/gdm-tools`
5. Done

## Set up password-less authentication

Each time you want to upload changes to GitHub, it will either ask you for your GitHub username and  password or just fail. To change this behavior, we need to set-up password-less authentication. This can be done either by using GPG encryption keys or SSH keys. Here we will use SSH keys.

#### Create an SSH key pair:

1. Run the command `ssh-keygen` in terminal or powershell window
2. It will ask where to save the key. You don't need to type anything, just press Enter/Return key
   **Note:** File path mentioned inside parenthesis is path to SSH **private** key file. Path to SSH **public** key file can be obtained from this by adding `.pub` at the end.
   For example, if `~/.ssh/id_rsa` is the path given inside parenthesis, path to SSH public key file should be `~/.ssh/id_rsa.pub`. Remember this. We will need it in Step 7.
3. It will ask for a passphrase for the new SSH key. Passphrase is just another name for password. You can set it to anything or leave it empty if you want and press Enter/Return

#### Upload public key to GitHub

4. Make sure you are logged in to GitHub

5. Go to [GitHub.com](https://github.com)->[Settings](https://github.com/settings)->[SSH and GPG keys](https://github.com/settings/keys)->[New SSH key](https://github.com/settings/ssh/new)
6. Type anything in the `Title` section of this webpage
7. Open SSH public key file inside a text editor (Notepad, etc.), copy its contents and paste them into `Key` section of this webpage
8. Click on 'Add SSH key'
9. Done

### Important Note:

Password-less authentication using SSH key pair works only if you clone a repo using SSH address i.e. address of the form user@domain:username/repo-name. For example `git@github.com:/realmazharhussain/gdm-tools`.

If you already cloned a repository using an https address, you can change its address to an SSH-type address without having to clone it again. Just find out its SSH clone address and run the command `git remote set-url origin {repo-address}` in the terminal/Powershell. Just replace the word `{repo-address}` with SSH-type clone address of the GitHub repository.

## Save/Manipulate Files in a Repository

First, open a local git repository folder in Terminal or Powershell. Then you can run following commands on the files in repository

|           Commands            |                           Actions                            |
| :---------------------------: | :----------------------------------------------------------: |
|      `git add file.ext`       |          Select Changes to a file named `file.ext`           |
|         `git add -A`          |       Select all changes to all files in current repo        |
| `git commit -m "Description"` | Save selected changes to git and remember this action with the description `Description` |
|          `git push`           |                Upload saved changes to GitHub                |
|          `git pull`           |        Download changes that were uploaded by others         |

