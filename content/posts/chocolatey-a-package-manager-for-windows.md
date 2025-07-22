---
date: '2020-07-05T13:43:25+05:00'
title: 'Chocolatey – A package manager for Windows'
---

![image](/images/chocolatey-a-package-manager-for-windows/chocolatey-logo.png)  
  

**What is a package manager?**
------------------------------

A package manager is an application (mostly a command\-line app) that manages packages (i.e. software/apps) on your computer system. It is responsible for downloading, installing, upgrading and uninstalling software on your computer without you worrying about anything. It was a Linux thing for some time. But now, you can have a package manager on Windows too.

**Why use a package manager?**
------------------------------

You would be thinking, “Why would typing commands on command prompt be better than doing things in Graphical Interface?”. Here’s why?

Suppose you log into freshly installed Windows. You need to install Chrome, WinRar, VLC, and a Download Manager. You would go to 4 different websites to download 4 different software. Then you would double click on each downloaded file to install it. You will have to click **next** almost a hundred times. You will be doing all this just to install 4 apps.

But you can install any number of apps just by running one command. For example, the command  
“**choco install \-y googlechrome winrar vlc xdm**“  
will download and install all the apps mentioned above (Google Chrome, WinRar, VLC, and Xtreme Download Manager) for you without needing you to do anything else. You just need a working internet connection.

The same applies to removing/uninstalling and upgrading apps. Run just one command and your work is done.

**How to install chocolatey?**
------------------------------

To install chocolatey  
1\. Go to start menu and search for powershell (not command prompt).  
2\. Right click on powershell and run as Administrator.  
3\. Copy the following command, paste it in powershell (you can do so by right clicking inside powershell) and press Enter:

```
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
```
If it runs successfully, chocolatey is installed. If it shows errors, check again whether you opened powershell as Administrator or not. You should also check your powershell version if it fails because chocolatey requires powershell version 3 or higher.

**Note:** If you don’t type \-y in the command as I put in the example command, It will ask you to confirm installation of the app after it has completed downloading it. You can change this behaviour by running the following command

```

choco feature enable -n=allowGlobalConfirmation

```

**How to use chocolatey?**
--------------------------

Some important commands of chocolatey are given below

**Installing Software:** choco install \<packages names\>  
**Removing Software:** choco uninstall \<package names\>  
**Finding Outdated Packages:** choco outdated  
**Upgrading Specific Software:** choco upgrade \<package names\>  
**Upgrading All Software:** choco upgrade all  
**Searching Software:** choco search \<App Name\>  
**List All Packages:** choco list

**Note:** You can also search packages by going to <https://chocolatey.org/packages>.

**\~\~\~ GOOD LUCK \~\~\~\~**

  