---
date: '2021-02-21T11:46:16+05:00'
title: 'How to Customize Ubuntu/Gnome Login Screen (GDM3)?'
---

![image](/images/how-to-customize-ubuntu-gnome-login-screen-gdm3/pinclipart.com_gnome-clipart_142867-2.png)  
  
**Update:** A new graphical application [Login Manager Settings](http://realmazharhussain.github.io/gdm-settings) has been released since I wrote this article. It makes it much easier to customize the login screen. I recommend using the app instead of following this guide. 

Theme And Background
====================

There are some apps that let you change the appearance (theme and background) of Gnome’s Login Manager (GDM), or its settings. The ones I know of are complicated to use. For example, Loginized is a GUI (Graphical) program that lets you chose a theme and a background for GDM. But, in order for a theme to appear in its list, you have to do some extra steps on terminal.

Because of that reason, I have created a terminal app (gdm\-tools) that manages everything with one\-line commands. To install this app, go to [https://github.com/realmazharhussain/gdm\-tools.git](https://github.com/realmazharhussain/gdm-tools.git). Follow the install instructions provided there.

Once the app is installed, open terminal and type following commands for their respective actions:

* **Get a List of Available Themes:** 
`set-gdm-theme list`  
or  
`set-gdm-theme -l`
* **Set Theme:** 
`set-gdm-theme set`  
or  
`set-gdm-theme -s`
* **Change Background Image:** 
`set-gdm-theme set --background [/path/to/image]`  
or  
`set-gdm-theme set -b [/path/to/image]`
* **Remove Background Image:** 
`set-gdm-theme set --background none`  
or  
`set-gdm-theme -s -b none`
* **Change Theme and Background at Once:** 
  `set-gdm-theme set [themeName] [/path/to/image]`
* **Reset Everything Back to Defaults:** 
`set-gdm-theme reset`
* **Short Help:** 
`set-gdm-theme --help`  
or  
`set-gdm-theme -h`
* **Detailed Help** 
`man set-gdm-theme`

If you are using fish shell, this program has auto\-completions for you. Type half of the command, then press tab and it will give you suggestions or complete the command for you. For example, typing ‘`set-gdm-theme -s def`‘ and then pressing tab will complete to ‘set\-`gdm-theme -s default`‘ in most cases.

Configuration and Settings
==========================

Once [gdm\-tools](https://github.com/realmazharhussain/gdm-tools.git) is installed, you can type ‘`gnomeconf2gdm`‘ in terminal to Apply your current Gnome Settings to GDM. It applies following settings to GDM:

1. **Appearance** 
1\. cursor\-theme  
2\. icon\-theme  
3\. show\-battery\-percentage (yes/no)  
4\. clock\-show\-weekday (yes/no)  
5\. clock\-format (12h/24h)
2. **Touchpad** 
1\. tap\-to\-click (enabled/disabled)  
2\. pointer speed
3. **Night Light** 
(all night light settings)

You can email me at [realmazharhussain@gmail.com](mailto:realmazharhussain@gmail.com) if you want additional settings to be included in the list. Or you can open an issue on [gdm\-tools](https://github.com/realmazharhussain/gdm-tools.git) github repo. 

You can also learn how to change GDM settings by editing config files directly if you read [this section](https://wiki.archlinux.org/index.php/GDM#DConf_configuration) of ArchWiki [page](https://wiki.archlinux.org/index.php/GDM) on GDM.

  