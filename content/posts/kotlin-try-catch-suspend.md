---
title: "Properly Catch All Exceptions In Kotlin Coroutines"
date: 2025-04-09T19:13:00+05:00
draft: true
---

In your opinion, what should be the result of the following piece of Kotlin code?

```kotlin
fun main() {
    runBlocking {
        try {
            async { throw Exception() }.await()
        } catch (_: Exception) {
            println("Exception caught")
        }

        delay(1.seconds)
        println("Not cancelled")
    }
}
```

1. ```
   Exception caught
   Not cancelled
   ```

2. ```
   Exception in thread "main" java.lang.Exception
   ```

   ```
3. Exception caught
   Exception in thread "main" java.lang.Exception
   ```
