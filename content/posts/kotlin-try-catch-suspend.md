---
title: "Catching Exceptions In Kotlin Coroutines"
date: 2025-04-20T21:11:00+05:00
draft: false
---

## Problem
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
   <<< crash >>>
   ```

3. ```
   Exception caught
   Exception in thread "main" java.lang.Exception
   <<< crash >>>
   ```

Well, you might be surprised to know that it is niether 1 nor 2 but 3. Yes, the correct answer is 3; the exception is both caught, and crashes the app.

## Explaination

> [!NOTE]
>
> This does not apply to `SupervisorJob` and `supervisorScope`. They eat as much exceptions as they can, instead of propagating them to relatives.

By default, Kotlin coroutines propagate cancellations. So, when an exception is thrown inside a child coroutine (started with `async { … }` in this case), it propagates the error to its parent coroutine, and the parent is immediately marked for cancellation with the same exception (regardless of wether it has a `try catch` or not). But the parent can only be cancelled when it gets the chance i.e. when it reaches the next suspension point. As long as a coroutine is executing blocking code (even in a suspend function), it will keep running even if it was marked for cancellation. In this case, since the next suspension point does not happen until the `delay(1.seconds)` call (`delay` is cancellable, `println` is not), the coroutine has to continue execution until then, even though it has already been marked for cancellation. When it reaches the `dealy(1.seconds)` call, the cancellation takes effect immediately. Since, this was the topmost parent in the heirarchy, it throws the exception directly in the thread, causing a crash.

> [!NOTE]
>
> `catch` block is triggered because `await()` rethrows the exception in the parent. So, the exception is both re-thrown and propagated.

> [!NOTE]
>
> **Rethrow**:
> * Parent has a chance to catch the exception with `try catch`. If it doesn't, then it is marked for cancellation.
>
> **Propagate**:
> * Parent is marked for cancellation 
> * There is **no** chance for parent to catch the exception (but grandparent might be able to, depending on the situation)

## Solution

There are two methods that prevent implicit propagation of exceptions without eating them; `coroutineScope` and `withContext`. When a child coroutine propagates an exception to them, they simply throw it instead of propagting it to their parent. So, you can simply wrap your suspending code with one of these if you want to make sure that you catch all the exceptions thrown by that block of code. So,

```kotlin
fun main() {
    runBlocking {
        try {
            coroutineScope { async { throw Exception() }.await() }
        } catch (_: Exception) {
            println("Exception caught")
        }

        delay(1.seconds)
        println("Not cancelled")
    }
}
```

will not crash the app. It will output

```
Exception caught
Not cancelled
```

### runCatchingSuspend
`runCatching` is a standard Kotlin function that catches exceptions, but sadly, it does not solve exception propagation issue. For that, I have created a suspending variant called `runCatchingSuspend` that catches all exceptions thrown inside itself or child coroutines.


```kotlin
suspend inline fun <T> runCatchingSuspend(
    coroutineContext: CoroutineContext = EmptyCoroutineContext,
    crossinline block: CoroutineScope.() -> T,
): Result<T> {
    return try {
        val value = withContext(coroutineContext) { block() }
        Result.success(value)
    } catch (e: CancellationException) {
        // Required for cancellation to work as expected
        throw e
    } catch (e: Exception) {
        Result.failure(e)
    }
}
```

> [!NOTE]
>
> I prefer `withContext` over `coroutineScope` here because it prevents
>
> ```kotlin
> runCatchingSuspend {
>    withContext(Dispatchers.IO) {
>        // my code ...
>    }
> }
> ```
> 
> which looks ugly in my opinion. Instead, we can simply write
>
> ```kotlin
> runCatchingSuspend(Dispatchers.IO) {
>     // my code ...
> }
> ```
