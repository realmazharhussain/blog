---
date: '2020-05-27T11:13:10+05:00'
title: 'How to Share Files Locally Among Windows, Linux and Android using SMB, FTP protocol?'
---

![image](/images/how-to-share-files-locally-among-windows-linux-and-android-using-smb-ftp-protocol/samba.png)

There are many ways to share files among Windows, Linux and Android on local networks such as local Wifi but Here you will learn how to use SMB and FTP protocol for this purpose.

**Share from Linux**
--------------------

On Linux, you will need to install a package named **samba** to share files. If you are using a Debian based distro, you can install **samba** by running the command  
`sudo apt install samba`  
Once you have installed samba, you will need to edit a file named **smb.conf**. You can use the following command to do so  
`sudo nano /etc/samba/smb.conf`  
Go to the end of this file and add something like below

```
[Folder Name]
    comment = Some text about this shared folder (not necessary)
    path = /path/to/the/folder/to/be/shared
    browseable = yes
    read only = yes
    guest ok = yes
```
Just replace **Folder Name** with real name of shared folder, value of **comment** with anything you like and value of **path** with real path to the folder you want to share.

Now press Ctrl\+S to save the file and Ctrl\+X to exit nano text editor. Now, the folder has been shared with any device that connects directly with your Linux PC. 

To browse files on Windows, open Windows File Explorer and type **\\\\192\.168\.43\.1\\** in the address bar except replace 192\.168\.43\.1 with IP Address of you Linux PC. You can find out your IP Address by running the command in Linux terminal  
`ip address | grep inet`  
Mostly, the 2nd IP Address after the word **inet** is your IP address in local network. Just keep in mind that 127\.0\.0\.1 is not the IP Address you want to use.  
Here is the output of my command

```
inet 127.0.0.1/8 scope host lo
inet6 ::1/128 scope host 
inet 192.168.43.140/24 brd 192.168.43.255 scope global dynamic noprefixroute wlp1s0
inet6 fe80::de99:6075:1f90:3dc9/64 scope link noprefixroute 
```
My IP Address in my current local network is 192\.168\.43\.140\.

To browse files on another Linux PC, you need to start a File Manager, click on **Other Locations**, **Network** or anything that brings up a box to type network address in it then type `smb://192.168.43.140/` and press Enter. Just replace 192\.168\.43\.140 with your IP Address.

To browse files on Android, you need an SMB compatible file browser like ES File Explorer or MX Player. On ES File Explorer, you need to tap three lines on top left corner then **Network** then **LAN** then **SCAN**. After some time, it will show the IP of your Linux PC. Tap on it to start browsing shared folder.

**Share from **Windows****
--------------------------

On Windows, Open Windows File Explorer, Right Click on any folder you want to share, click on properties then go to Sharing Tab, Click on Share, Select everyone from user list, Click on Apply and then on OK. The Folder is now shared to local network.

To Browse files on any device, you need to know the name of your PC in Windows. To find this out, you need to right click on **This PC** and click on properties. It will be shown there. It will be in the form DESKTOP\-12AB3CD.

To browse files on another Windows PC, you need to type **\\\\DESKTOP\-NAME\\** in the address bar of WIndows File Explorer. To browse files on Linux, Type **smb://DESKTOP\-NAME/** in the network address bar of your favourite file manager. Just replace DESKTOP\-NAME with the name of your PC.

To browse files on Android, you need an SMB compatible file browser like ES File Explorer or MX Player. On ES File Explorer, you need to tap three lines on top left corner then **Network** then **LAN** then **SCAN**. After some time, it will show the Name of your Windows PC. Tap on it to start browsing shared folder.

**Share from Android**
----------------------

On Android, you need ES File Explorer to share files through FTP Protocol. Open ES File Explorer. Tap on little arrow down icon just above New Files section. Tap on **View on PC**. Tap on 3 dots on top right corner and then settings to change some basic settings like which folder to share and password to access it etc. If you are connected to any network, it will show an option **TURN ON** at the bottom. Click on it to start sharing files. It will show you an ftp address. You can enter it on any internet browser or file manager on any device that is connected to your local network to browse shared files.
