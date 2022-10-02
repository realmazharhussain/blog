---
title: "File/Directory Permissions on Linux"
date: 2022-07-28T20:46:59+05:00
draft: true
---

This tutorial will teach you everything you need to know about file permissions in Linux.

## File Ownership

Every file in Linux has an owner and a group of users associated with it. The owner has a special power to change permissions on the file for itself, associated group and others.

## Getting Ownership/Permission Information

Getting ownership and permission information of a file or directory is very easy. Just run the command `ls -ld --si /path/to/file` in the terminal. Just replace `/path/to/file` with path to an actual file or directory. For example,

running the following command on my system

```bash
ls -ld --si /srv/ftp
```

produces

```
dr-xr-xr-x 2 root ftp 4.1k Dec 18  2021 /srv/ftp/
```

We can break it down to

`d` `r-xr-xr-x` `2` `root` `ftp` `4.1k` `Dec 18  2021` `/srv/ftp/`

- `d`: type of file (not video, image, pdf, etc. but directory, regular file, symlink, etc.)
- `r-xr-xr-x`: permissions
- `2`: number of hardlinks (just ignore it)
- `root`: owner
- `ftp`: group
- `4.1k`: size of file
- `Dec 18  2021`: Modification date
- `/srv/ftp/` : Filename

## Meaning of Type of File

- `-` means regular file (your everyday image, music, video, pdf, etc. file)
- `d` means directory (folder)
- `l` means symlink (a link (shortcut) to a file or directory)
- and so on ..
 
## Meaning of permissions

In above example, we have permissions `r-xr-xr-x`. What do they mean? Why is `r-x` repeating?

Actually, permissions are in the form `rwx` repeated three times. 1st time for the owner, 2nd for the group, 3rd for other users. Any of the letters in `rwx` can be replaced by a `-` to represent the fact that the owner, group, or others do not have permission represented by the missing letter.

So, in our example `r-xr-xr-x`, the owner, the group, others, all have permissions `r` and `x` but not `w`.

The letters `r`, `w`, and `x` have different meaning depending on type of file.

### For Regular Files

- `r`: permission to read/open a file
- `w`: permission to write/modify a file
- `x`: permission to execute/run a file

### For Directories

- `r`: permission to list files/directories present inside a directory
- `w`: permission to add new files/directories to or rename/delete existing files/directories inside a directory
- `x`: permission to access/modify files/directories present inside a directory

**Note:** If you want someone to have access to dir1/dir2 but not dir1 itself, you'll have to give them permission `x` on dir1 and then explicitly revoke their permissions on each file/directory in dir1 except only for dir2.

## Who Can Change Owner/Group or Permissions?

In order to change owner or group or even permissions of a file/directory, you either need to already be the owner or have root access. In other words,

### without root access

#### you can

- Give up your ownership to someone else (make someone else owner of the file you are currently the owner of)
- Change which group of users is associated with the files/directories you own
- Change permissions for everyone on the files/directories you own

#### you cannot

- Take ownership of a file from someone else
- Change permissions for anyone on the files/directories you do not own


### with root access

You can do whatever the fuck you want.

## How To Change Owner/Group?

Just run the command `chown owner:group /path/to/file` after replacing

- `owner` with an actual user name e.g. root, ftp, mail, etc.
- `group` with an actual group name e.g. wheel, network, http, etc.
- `/path/to/file` with path to an actual file or directory e.g. `$HOME/Public`.

If you do not want to change group of a file but just the owner, run the command

```bash
chown owner /path/to/file
```

If you do not want to change the owner but just group of a file, run the command

```bash
chown :group /path/to/file
```

If you do wish to change both the owner and group but want to change the group to the primary group of the owner,
run the command

```bash
chown owner: /path/to/file
```

## How To Change Permissions?

