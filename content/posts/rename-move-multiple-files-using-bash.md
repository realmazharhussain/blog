---
title: "Rename/Move Multiple Files Using Bash"
date: 2021-10-02T16:32:25+05:00
draft: true
---

Following is an explained step by step process to rename multiple files (mostly) any way you want using bash with examples
**Note:** Anything after a hash/pound symbol (#) in a line in the examples is a comment and can be ignored without any effect on the process. It is there just to explain things.

## Why not use Graphical tools for this?

Graphical tools are great. Use them if they do what you want. But they are limited by their graphical interfaces. There are things that they cannot do. That's where bash comes in for help. Using bash, you can easily rename/move files exactly the way you want.

## Selecting Files

You can select files with `for` loop and wildcards/patterns (\*,?,[],{}) or full filenames

For example, to select files `a.png`, `2.mp4`, `empty file.txt`, and `test.sh`, the following for loop could be used

```bash
for file in a.png 2.mp4 'empty file.txt' test.sh; do
  # do something with files
done
```

*note the apostrophe `'` before and after filename of `empty file.txt`. It is important for files that contain spaces in their name*

to select all files with the extension `.jpeg`, following for loop could be used

```bash
for file in *.jpeg; do
  # do something with files
done
```

to select all files that contain the word `abc`

```bash
for file in *abc*; do
  # do something with files
done
```

to select all files that start with the word `abc`

```bash
for file in abc*; do
  # do something with files
done
```

to select all video files regardless of the extension you could use `file` command along with a `for` loop

```bash
for file in *; do
  if [[ $(file -b --mime-type -- "$file") = video/* ]]; then
    # do something with videos
  fi
done
```

### Selecting Files in Specific Order

Sometimes, we want to rename files in a specific order because we want them to have names like `file1.txt`, `file2.txt`, `file3.txt`, etc.

We can do that by using a `while` loop along with the `ls` command instead of a simple `for` loop. In this way, we could use the sorting functionality that `ls` command has.

For example, to select all files with `.jpeg` extension, following `while` loop could be used

```bash
while read file; do
  # do something with files
done <<< $(ls -1 *.jpeg)
```

*Note the `-1` flag that is provided to the `ls` command.  It is very important.*

to select all files with `.jpeg` extension but in the order that newest file is selected first

```bash
while read file; do
  # do something with files
done <<< $(ls -1 --time *.jpeg)
```

to select all files with `.jpeg` extension but in the order that oldest file is selected first

```bash
while read file; do
  # do something with files
done <<< $(ls -1 --time --reverse *.jpeg)
```

to select all files with `.jpeg` extension but in the order that largest file is selected first

```bash
while read file; do
  # do something with files
done <<< $(ls -1 -S *.jpeg)
```

**Note:** Run the command `ls --help` or `man ls` in terminal to get more information on the `ls` command and its sorting abilities.

## Breaking Down Filenames

To make it easier to rename files, we could break down its path to the path of its folder/directory, its basename and its extension

For example if we have a file `wallpaper.png` in our home directory `/home/user`, we want to be able to see that its full path is `/home/user/wallpaper.png` and separate it into `directory=/home/user`, `basename=wallpaper`, and `extension=png`; so that we can rename it any way we want very easily

We can do that with following bash code (assuming we have `file=wallpaper.png` while we are in `/home/user`)

```bash
file="$(realpath -s -- "$file")" # expands value of $file from wallpaper.png to /home/user/wallpaper.png
directory="${file%/*}"           # get directory path (/home/user)
basename="${file##*/}"           # get basename (wallpaper.png)
basename="${basename%.*}"        # remove extension from basename (wallpaper)
extension="${file##*.}"          # get extension (png)
```

## Renaming/Moving Files

### Renaming Files

Now since we have a file’s directory path, its basename and extension, we can easily rename it with `mv --` command

For example, add the word `-new` to the end of filename but before the extension (`wallpaper.png` becomes `wallpaper-new.png`)

```bash
old_name="$file"
new_name="${directory}/${basename}-new.${extension}"
mv -- "$old_name" "$new_name" 
```

or replace the word `paper` with `PAPER` in filename (`wallpaper.png` becomes `wallPAPER.png`)

```bash
old_name="$file"
new_name="${directory}/${basename/paper/PAPER}.${extension}"
mv -- "$old_name" "$new_name"
```

or remove the word `paper` in filename (`wallpaper.png` becomes `wall.png`)

```bash
old_name="$file"
new_name="${directory}/${basename/paper/}.${extension}"
mv -- "$old_name" "$new_name"
```

### Moving Files

The `mv --` command also can move files.

For example, to move `wallpaper.png` from `/home/user` to `/home/user/Pictures`, following code can be used

```bash
old_name="$file"
new_name="/home/user/Pictures/${basename}.${extension}"
mv -- "$old_name" "$new_name" 
```



## Complete Examples

**1:** Change extension of all files with extension `.jpeg` in `~/Pictures` folder to `.jpg` extension

```bash
# Select all files  in ~/Pictures with .jpeg extension
for file in ~/Pictures/*.jpeg; do
  # Break down filenames
  file="$(realpath -s -- "$file")"
  directory="${file%/*}"
  basename="${file##*/}"
  basename="${basename%.*}"
  extension="${file##*.}"

  # Rename files
  old_name="$file"
  new_name="${directory}/${basename}.jpg"
  mv -- "$old_name" "$new_name"
done
```

**2:** Add the word `ScreenRecording-` before filename of each video in `~/Videos/Recordings`

```bash
# Select all Videos in ~/Videos/Recordings
for file in ~/Videos/Recordings/*; do
  if [[ $( file -b --mime-type -- "$file") = video/* ]]; then
    # Break down filenames
    file="$(realpath -s -- "$file")"
    directory="${file%/*}"
    basename="${file##*/}"
    basename="${basename%.*}"
    extension="${file##*.}"

    # Rename files
    old_name="$file"
    new_name="${directory}/ScreenRecording-${basename}.${extension}"
    mv -- "$old_name" "$new_name"
  fi
done
```

**3:** You have a lot of files in `~/test-folder` with names like `asdl3m2.jpg`, `lsdkte3.png`, `sdgi3l.dat`, etc. and you want all pictures to have names like `picture-1.png`, `picture-2.jpg`, etc. while keeping all other files untouched

```bash
# Set a starting value for the number in filenames
number=1

# Select all Pictures in ~/test-folder
for file in ~/test-folder/*; do
  if [[ $( file -b --mime-type -- "$file") = image/* ]]; then
    # Break down filenames
    file="$(realpath -s -- "$file")"
    directory="${file%/*}"
    basename="${file##*/}"
    basename="${basename%.*}"
    extension="${file##*.}"

    # Rename files
    old_name="$file"
    new_name="${directory}/picture-${number}.${extension}"
    mv -- "$old_name" "$new_name"

    # Increase value of number by 1 for each image file
    ((number++))
  fi
done
```

**4:** Same problem as Example #3, but you want the filenames to be like `picture-01.png`, `picture-02.jpg`, ... `picture-10.png`, etc. instead of simple `picture-1.png`, `picture-2.jpg`, ... `picture-10.png`

```bash
# Set a starting value for the number in filenames
number=1

# Select all Pictures in ~/test-folder
for file in ~/test-folder/*; do
  if [[ $( file -b --mime-type -- "$file") = image/* ]]; then
    # Break down filenames
    file="$(realpath -s -- "$file")"
    directory="${file%/*}"
    basename="${file##*/}"
    basename="${basename%.*}"
    extension="${file##*.}"

    # Format number
    formatted_number=$(printf %02d $number)
    
    # Rename files
    old_name="$file"
    new_name="${directory}/picture-${formatted_number}.${extension}"
    mv -- "$old_name" "$new_name"

    # Increase value of number by 1 for each image file
    ((number++))
  fi
done
```

*Note the use use of `printf` command. You can modify it to your liking. You just have to replace 2 in `%02d` with any number you like and the result would be that many digits long.*

**5:** You have over 1000 files in `~/Recovered` and all the files have useless names and no extension e.g `aldidladb49sz9e`, `ldi39-ssi3`, etc. You want files to move to their respective folders and have names like `video-001.mp4`, `video-002.mkv` for videos and names like `image-001.png`, `image-002.jpg` for images, etc. The following code is how you do it in bash

```bash
# declare number as named/associative array
# this will be useful for keeping different number for different types of files
declare -A number

# Select all Pictures in ~/test-folder
for file in ~/Recovered/*; do
  # Get File type
  mime_type=$( file -b --mime-type -- "$file") # get full type e.g. image/png, video/x-matroska, etc.
  main_type=${mime_type%/*} # get main type e.g. video, image, text, etc.
  sub_type=${mime_type#*/}  # get sub type e.g. mp4, png, etc.
  sub_type=${sub_type#x-}   # remove 'x-' from subtype i.e. x-matroska -> matroska
  [ $sub_type = matroska ] && sub_type=mkv # if subtype=matroska then change it to sub_type=mkv

  # Increase value of number by 1 for current type
  ((number[$main_type]++))
  
  # Break down filenames
  file="$(realpath -s -- "$file")"
  directory="${file%/*}"
  basename="${file##*/}"
  basename="${basename%.*}"
  extension="${file##*.}"

  # Format current file-type's number 
  formatted_number=$(printf %03d ${number[$main_type]})
  
  # The new folder/directory where file should be moved to
  new_directory="${directory}/${main_type}"

  # Create a folder for current filetype if does not exist already
  mkdir -p "$new_directory"
    
  # Rename/Move files
  old_name="$file"
  new_name="${new_directory}/${main_type}-${formatted_number}.${sub_type}"
  mv -- "$old_name" "$new_name"
done
```

<center><h3>I hope this helped you! Good Luck.</h3></center>

