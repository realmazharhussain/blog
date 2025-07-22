---
date: '2020-05-18T10:10:29+05:00'
title: 'Awesome Tricks and Shortcuts for Terminal'
---

![image](/images/awesome-tricks-and-shortcuts-for-terminal/screenshot-from-2020-05-18-10-08-43.png)

A **terminal** is a GUI program in a GUI(graphical) environment that provides a way to communicate with your **Operating System** through commands. There are many terminal apps for **Linux**, each with their own shortcuts and features. But there are some shortcuts and tricks that are associated with a **shell**. A **shell** is a program that provides an environment and some built\-in commands for the terminal to communicate with the OS. **Bash** is the most common shell used in many Operating Systems including **Unix, Linux, Mac OS**. These tricks and shortcuts are tested on **bash** shell in **Linux** but they are expected to work with other shells and Operating Systems as well except on **dash** shell (often presented as **sh** ) and **Windows** ( unless you are using WSL ).

**Shortcuts**
-------------

**Ctrl\+P** or **Arrow\_Up** —\-\> Show Previous command  
**Ctrl\+N** or **Arrow\_Down** —\-\> Show Next command  
**Ctrl\+A** or **Home** key —\-\> Move cursor to the beginning of current command  
**Ctrl\+E** or **End** key —\-\> Move cursor to the end of current command  
**Ctrl\+X\+E** —\-\> Edit current command in a command line text editor (nano for example)  
**Tab** —\-\> Auto Complete filenames or commands  
**Ctrl\+C** —\-\> Cancel current running command  
**Ctrl\+Z** —\-\> Pause current running command and exit (use “bg” command to continue it in background)  
**Ctrl\+D** —\-\> Exit/LogOut of current bash session  
**Ctrl\+L** —\-\> Clear Screen  
**Ctrl\+U** —\-\> Delete text from cursor position to the beginning of current command  
**Ctrl\+K** —\-\> Delete text from cursor position to the end of current command  
**Ctrl\+W** —\-\> Delete previous word (text from cursor position to first Space towards left)  
**Ctrl\+Y** —\-\> Paste text recently ereased by keyboard shortcuts given above  
**Ctrl\+R** —\-\> Search in command history  
**Ctrl\+S** —\-\> Stop terminal output  
**Ctrl\+Q** —\-\> Resume terminal output if stopped by Ctrl\+S  
**Alt\+.** —\-\> Paste last argument of previous command

**Tricks**
----------

**Note:** These tricks are to be executed as commands.

1. **\[space]\+command**: —\-\> If you type a command after a space in the beginning, the command is run but not recorded in bash history.
2. **!!** —\-\> If you type !! instead of any command, it executes previous command.  
   “**sudo !!**” executes previous command with sudo privileges.
3. “**!termi**” executes last command in bash history that started with word “termi” (e.g. **termi**nator).  
   **Note:** You can replace **termi** with anything that is in the beginning of the command you have already run in the past.
4. **!n** executes **n**th command in all command history.
