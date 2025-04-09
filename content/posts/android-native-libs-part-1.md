---
title: "Native (C/C++) Code in Android Apps - Part 1"
date: 2024-07-30T20:50:15+05:00
draft: false
---

> [!NOTE]
> This article is not a thorough guide. It exists only to document and share what I learned in two-ish work days.

## Sample Project
All the code in this article is available as a [sample project on GitHub](https://github.com/realmazharhussain/android-native-example-app).

## [NDK](https://developer.android.com/ndk)
NDK (Native Development Kit) is the tool that lets Native (C/C++) code and Kotlin/Java code interoperate. So, first of all, we need to install the NDK in Android Studio.

1. Open `Tools` -> `SDK Manager`
2. Switch to the `SDK Tools` tab
3. Tick `NDK (side by side)`
4. Click `OK`

## [CMake](https://cmake.org)

CMake is the preferred way of using external/native libraries in Android apps. [Gradle](https://gradle.org) also supports [ndk-build](https://developer.android.com/ndk/guides/ndk-build). But we are going to use CMake for this article as that is the preferred choice.

### Installation
You can install CMake in two ways;

#### Through Android Studio
1. Open `Tools` -> `SDK Manager`
2. Switch to the `SDK Tools` tab
3. Tick `CMake`
4. Click `OK`

#### Externally
You can install via any method you like.

- If `cmake` command is available on the `PATH`, it will automatically be detected by Android Studio.

  For example, on Arch Linux, I installed it via the following command, and it was auto-detected by Android Studio without any extra setup needed.

  ```sh
  sudo pacman -S cmake
  ```

- If `cmake` is not in your `PATH`, you can either add its location to `PATH`, or you can directly tell Android Studio where it is located by adding the following property in `local.properties` file.

  ```ini
  # local.properties
  cmake.dir = "/path/to/cmake"
  ```

### Configuration
> [!NOTE]
> You should create a separate Android module for the native library.

#### Top-Level `CMakeLists.txt`
We cannot link our Android project with multiple CMake projects directly. So, we need a single top-level `CMakeLists.txt` file in which we can import other CMake libraries.

We will create this file at `{project}/{module}/src/main/cpp/CMakeLists.txt` with the following contents.

```cmake
cmake_minimum_required(VERSION 3.10)
project("example_lib-java-binding")
```

##### Linking With Our Android Project
We have two methods to add/link this CMake file with our Android project.

###### Through GUI
1. In "Project" pane, make sure "Android" is selected as the current view
2. Right click on the "app" module, and select "Link C++ Project with Gradle"
3. Select "CMake" as the build system.
4. Select the "CMakeLists.txt" file we just created as Project path.
5. Click "OK"

###### By Editing `build.gradle.kts`
Add this inside the `android` block of your module-level `build.gradle.kts` file.

```kotlin
android {
    ...
    externalNativeBuild {
        cmake {
            path = file("src/main/cpp/CMakeLists.txt")
        }
    }
}
```

## Adding Native (C/C++) Code
### Adding Native Library Dependency
Depending on your situation, the method to add external native dependencies will differ.

Here, we will discuss the simplest case. Our dependency is a single function/open source C library with a permissive license, and no transitive dependencies other than the C standard library.

> [!NOTE]
> From now on, we will assume the library we are using is named `concat`. For everything below this, you can replace the word `concat`, wherever it is used, with the name of the library you want to use in your project.

We just copy all the source code of `concat` (our dependency) into `src/main/cpp/concat`. So, the directory structure of our cpp directory looks like below.

```
{project}/concat/src/main/cpp
├── CMakeLists.txt
└── concat
   ├── CMakeLists.txt
   ├── concat.c
   └── concat.h
```

Contents of `{project}/concat/src/main/cpp/concat/concat.h` are;

```c
#pragma once

char* concat (int count, const char **strings);
```

### Creating Java Bindings
We need to expose the relevant C functions to the Kotlin/Java code. We do that by binding C functions to a Kotlin/Java class and its methods.

#### Add A Native Binding File
- Create an empty C source file, at the following path.

  ```
  {project}/concat/src/main/cpp/concat-jni.c
  ```
- Add the following contents to the main `CMakeLists.txt` file (`{project}/concat/src/main/cpp/CMakeLists.txt`).

  ```cmake
  add_subdirectory(concat)
  add_library(concat-jni SHARED concat-jni.c)
  target_link_libraries(concat-jni concat)
  target_include_directories(concat-jni PUBLIC concat)
  ```

  - With `add_subdirecotry(concat)`, we are making `concat` library a part of our own `concat-jni` library.
  - `add_library(concat-jni SHARED concat-jni.c)` creates a shared library named `concat-jni` and adds `concat-jni.c` as a source file for it.

    `concat-jni` is a C library that we will write, and it is the library that will expose C functions from the `concat` library to our Kotlin/Java code.
  - `target_link_libraries(concat-jni concat)` links our `concat-jni` library with the base `concat` library, so that we can expose functions from `concat`.
  - `target_include_directories(concat-jni PUBLIC concat)` will add `{project}/concat/src/main/cpp/concat/` as an include directory for our `concat-jni` library. So, we can `#include <concat.h>`.

#### Add Kotlin/Java Class
```kotlin
class Concat {
    init { System.loadLibrary("concat-jni") }
    external fun concat(args: Collection<String>): String
}
```

- Class name could be anything.
- It doesn't have to be a class, it can also be a Kotlin `object`.
- In `init`, we call `System.loadLibrary("$libraryName")`.
    * Here, library name must be only the name, no `lib` prefix or file extension. E.g. instead of `concat-jni.dll` or `libconcat-jni.so`, we need to use just `concat-jni` here.
- Use the keyword `extenal` to declare methods that we want to expose from our native library.

#### Write Binding Code
- Once you add a method marked as `external`, Android Studio will give an error: "Cannot resolve corresponding JNI function".
- Just hover your cursor over the method name, and Android Studio will give you an option to "Create JNI function for \<functionName\>", click on that.
- It will give you an option to choose a C file to add the "corresponding JNI function" to, choose `concat-jni.c`.

Now, you'll have a skeleton of a binding function. How to fill in that function with useful code will be discussed in Part 2 of the article.

## Further Reading
- [Native (C/C++) Code in Android Apps - Part 2](https://mazhartechtips.netlify.app/posts/android-native-libs-part-2/)
