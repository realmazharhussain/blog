---
date: '2020-06-04T11:15:01+05:00'
title: 'Nix – One package manager for every Linux distro, MacOS, Android, and much more.'
---

![image](/images/nix-one-package-manager-for-every-linux-distro-mac-android-and-much-more/nix-wiki.png)  
  
Sometimes, you want to install a package but it is not available for your distro. Sometimes, you want to install a newer version of a package than what’s available on your distro. You may want to install Linux Apps on Mac OS or Android. **Nix** provides you a way to do so. It works on every Unix\-like OS with **curl** command and root access via **sudo** available, except Android. Android does not need root access or curl to install **nix**.

**Note:** You can also install other package managers like dpkg, pacman, etc. on top of nix.

**Installation**
----------------

On any Unix\-like OS other than Android, open terminal and enter the following command to install nix

```
curl -L https://nixos.org/nix/install | sh
```
If the command runs successfully, you will have nix installed on your system. You need internet connection to run this command.

On Android, you need to install an app named [Nix\-on\-Droid](https://f-droid.org/en/packages/com.termux.nix/). This app will install nix for you and you can use nix through this app. This App requires you to have Android 7 (Nougat) or higher to be installed.

**Using nix**
-------------

Here are some basic commands of nix for package management. Just replace \<pkg\> with real package name.

* **nix\-env \-i \<pkg\>** to install a package
* **nix\-env \-e \<pkg\>** to remove a package
* **nix\-env \-u \<pkg\>** to update a package
* **nix\-env \-u** to update all packages
* **nix\-env \-q** to see a list of installed packages
* **nix\-env \-qc \| grep “\>”** to see a list of upgradable packages
* **nix\-env \-q –description \<pkg\>** to see one line description of a package
* **nix\-channel –update** to update the list of available packages and their versions
* **nix\-collect\-garbage \-d** to delete useless/extra files to free some space

**Note:** The last command is very important. When you remove a package, it is not actually deleted from storage. It remains there uninstalled. To delete/remove/uninstall it completely, run **nix\-collect\-garbage \-d** after you have removed a package.

  
