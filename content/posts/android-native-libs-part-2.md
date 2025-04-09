---
title: "Native (C/C++) Code in Android Apps - Part 2"
date: 2024-08-05T20:30:15+05:00
draft: false
---

> [!NOTE]
> This article requires that you have already read [part 1](https://mazhartechtips.netlify.app/posts/android-native-libs-part-1/) of this article. If you haven't read part 1 yet, please read it first, then come back to part 2.

## Prerequisites
- Install & configure: Android NDK, and CMake
- Add your native dependency
- Set up linked CMake project for JNI bindings

## Writing Binding Code
If you recall, we had a `Concat.concat(args: Collection<String>): String` method in kotlin, and we had created a corresponding JNI function through Android Studio's suggested action. That JNI function looks something like below.

```c
JNIEXPORT jstring JNICALL
Java_com_example_concat_Concat_concat(JNIEnv *env, jobject thiz, jobject args) {
    // TODO: implement concat()
}
```

First of all, we are going to remove the comment, and rename parameter `thiz` to `this`. Since we are using C, and not C++, we are allowed to use `this` as an identifier name, we don't need to give this parameter a weird name.

```c
JNIEXPORT jstring JNICALL
Java_com_example_concat_Concat_concat(JNIEnv *env, jobject this, jobject args) {
}
```

You'll notice that all the parameters except `env`, and even the return type of `Java_com_example_concat_Concat_concat()` are Java objects a.k.a `jobject`s. We can't pass these values to functions in our C library, it expects C types. So, we need to

1. Extract C structures from our `jobject` parameters.
2. Perform our calculations.
3. Convert the result into a `jobject`, and return it.

> [!NOTE]
> Java primitive types e.g. `jint`, `jbyte`, `jsize`, are `typedef`s of regular C types. So, values of those types can easily be passed around like any other primitive value in C.
> 
> For example, `jsize` == `jint` == `int32_t` (C type)

### Extracting C Structures From `jobject`s
To access any property of a `jobject`, or call any methods on it, we need to

1. Get a reference of the Java class of that object.
   
   ```c
   jclass collection_class = (*env)->GetObjectClass(env, collection_object);
   ```
2. Get the ID of a method from the Java class (properties are also treated as methods)
   
   We need to pass method name and signature as well, in order to get method ID. Method signatures are explained in [Method Signatures](#method-signatures). 
   
   ```c
   jmethodID collection_size_method = (*env)->GetMethodID(env, collection_class, "size", "()I");
   ```

3. Call the method
   
   Calling a method also differs based on the return type. For primitive types, you use their specific methods, and for other types, you use `CallObjectMethod()`.

   ```c
   jsize collection_size = (*env)->CallIntMethod(env, collection, collection_size_method);
   jobject collection_iterator = (*env)->CallObjectMethod(env, collection, collection_iterator_method);
   ```

#### Method Signatures
Method signatures are written in the form

`(` Parameter Types `)` Return Type

> [!NOTE]
> There are no separators among parameter types

- Primitive types are represented by a single capital letter
  
  | Kotlin Type | Representation |
  | :---------: | :------------: |
  |   Boolean   |       Z        |
  |    Byte     |       B        |
  |    Char     |       C        |
  |    Short    |       S        |
  |     Int     |       I        |
  |    Long     |       J        |
  |    Float    |       F        |
  |   Double    |       D        |
  
- Non-primitive types are represented in the form
  
  `L` Fully-Qualified Class Name (with `/` in place of `.`) `;`

  E.g. `Ljava/lang/String;`

  > [!NOTE]
  > Notice `;` at the end

- Java array types are prepended with a `[`
  
  E.g. `IntArray` would be represented as `[I`

So, signature of our function

```kotlin
Concat.concat(args: Collection<String>): String
```

would be

```
(Lkotlin/collections/Collection;)Ljava/lang/String;
```

> [!NOTE]
> Generics are ignored.

### Extract C String Array From Java Collection\<String\>

Since we are dealing with string arrays here, we will create a `struct` for them, so that passing around string arrays is little less cumbersome for us. We can definitely do just fine without the `struct`, but having it is just easier.

> [!NOTE]
> Add this code to your `concat-jni.c`

```c
#include <jni.h>
#include <malloc.h>

typedef struct StrArray_ {
    jsize size;
    const char **data;
} StrArray;
```

We will also create a helper function to destroy our StrArray instances i.e. free the memory that was held by them.

```c
void StrArray_destroy(StrArray *str_array) {
    str_array->size = 0;
    free(str_array->data);
}
```

> [!NOTE]
> Don't forget to `#include <malloc.h>`. We need it to create and destory instances of our `StrArray` struct.

#### StrArray_from_collection()
Retrieving C string array from a Java `Collection<String>` is not a straightforward process. So, we will create a helper function `StrArray_from_collection()` that converts a Java `Collection<String>` object into our `StrArry` type.

In case of a `Collection<String>`, we need to

1. Get `size` property
2. Call `iterator()` method
3. Loop through the iterator
4. Convert each `jstring` object into a C string (`const char*`)

```c
StrArray StrArray_from_collection(JNIEnv *env, jobject this, jobject collection) {
    // Get a reference to `Collection` interface
    jclass collection_class = (*env)->GetObjectClass(env, collection);

    // Get method ID of `Collection.size` getter
    jmethodID collection_size_method = (*env)->GetMethodID(env, collection_class, "size", "()I");
    // Get method ID of `Collection.iterator()`
    jmethodID collection_iterator_method = (*env)->GetMethodID(env, collection_class, "iterator", "()Ljava/util/Iterator;");

    // Call `Collection.size` getter to get size of `args` (our Collection<String>)
    jsize collection_size = (*env)->CallIntMethod(env, collection, collection_size_method);
    // Call `Collection.iterator` getter to get iterator of `args`, so that we can iterate over `args`
    jobject collection_iterator = (*env)->CallObjectMethod(env, collection, collection_iterator_method);

    // Get class/interface of `args.iterator`
    jclass iterator_class = (*env)->GetObjectClass(env, collection_iterator);
    // Get method ID of `args.iterator.next()`
    jmethodID iterator_next_method = (*env)->GetMethodID(env, iterator_class, "next", "()Ljava/lang/Object;");
    // Get method ID of `args.iterator.hasNext()`
    jmethodID iterator_has_next_method = (*env)->GetMethodID(env, iterator_class, "hasNext", "()Z");

    // Allocate an `StrArray` to populate
    StrArray result = {collection_size, malloc(result.size)};

    for (jsize i = 0; i < collection_size; i++) {
        // Get the next jstring from the collection; this will return the 1st element on 1st call
        jobject element = (*env)->CallObjectMethod(env, collection_iterator, iterator_next_method);
        // Convert to a C string, and store it in our `StrArray` instance
        result.data[i] = (*env)->GetStringUTFChars(env, element, NULL);
    }

    return result;
}
```

### Implement JNI Function
```c
JNIEXPORT jstring JNICALL
Java_com_example_concat_Concat_concat(JNIEnv *env, jobject this, jobject args) {
    // Convert `args: Collection<String>` jobject into an `StrArray` instance
    StrArray str_array = StrArray_from_collection(env, this, args);
    // Use concat() function from our `concat` C library to concatenate strings together.
    char *result_str = concat(str_array.size, str_array.data);
    // Convert the resulting C string into a `jstring`
    jstring result = (*env)->NewStringUTF(env, result_str);

    // Free up memory to avoid memory leaks
    free(result_str);
    StrArray_destroy(&str_array);

    // Return the result
    return result;
}
```

> [!NOTE]
> Don't forget to `#include <concat.h>`

## Use C code from Kotlin/Java code

Now, you can use the `concat` library, and its function in your Kotlin/Java code.

```kotlin
val libConcat = Concat()
val brokenString = listOf(
    "Congatulations! ",
    "You have successfully concatenated strings ",
    "using concat() function from concat C library"
)
val result = libConcat.concat(brokenString)
```

## Further Reading
- [Java Native Interface Specification](https://docs.oracle.com/en/java/javase/22/docs/specs/jni/index.html)
- [Android NDK Guide](https://developer.android.com/ndk/guides)
