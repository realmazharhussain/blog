---
title: "Ultimate Inspector/Playground for GTK"
date: 2023-10-11T08:13:00+05:00
draft: false
typora-root-url: ..
---

Have you ever been in a situation where you wanted to read/inspect some value that GTK Inspector does not show or modify something in your running app e.g. replace a widget with another one? Well! I have just the trick for you (if your app is written in an interpreted language that is). 

## Steps

1. Make sure the file/module that contains `Application.run()` call can be imported in live interpreter mode (running the interpreter directly)
1. Replace the `Application.run()` call with `Gio.Task.run_in_thread()` call passing a wrapper around `Application.run` as `task_func` (argument of `Gio.Task.run_in_thread()`).
1. Now, the app will start running but you'll still be able to input more code into the interpreter prompt and read/modify any part of your app while it is running.


## Example (Python)

1. Save the following code as `bg_app.py`.

   ```python
   from gi.repository import Adw, Gtk, Gio
   
   app = Adw.Application()
   win = Gtk.ApplicationWindow()
   
   def on_activate(app):
       app.add_window(win)
       win.present()
   
   app.connect('activate', on_activate)
   
   task = Gio.Task()
   task.run_in_thread(lambda *x: app.run())
   ```

1. Open the Python interpreter in the same directory where you saved `bg_app.py`.

1. Enter the following line.

   ```python
   from bg_app import app, win, Gtk
   ```
   
   This will launch the app without blocking the interpreter.

1. Enter the following line and see the magic.

   ```python
   win.props.child = Gtk.Label.new("Wow, Magic!")
   ```
