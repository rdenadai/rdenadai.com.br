## Introduction

I am not one of those fanatics about programming paradigms or anything like that, but I feel I have a constant drive to look for new and interesting things that might spark my curiosity.

Recently there was a discussion on Bluesky, when someone I follow posted an image of F# code. Among the discussions, the issue of chained operations using some kind of operator was raised.

For those who are used to functional languages (I would say), this operator is part of the toolkit available to the programmer. However, in many “classic” languages (I will allow myself that term here, but in quotes), this is something unknown to programmers or, if it exists, it is little explored due to the mindset generated over years by the so-called Object-Oriented Paradigm.

Just a parenthesis here: I do not blame the Object-Oriented Paradigm for this, but perhaps the field as a whole has paid less attention to this kind of possibility and to how it could yield interesting pipelines.

That said, many end up getting “lost” in Object Orientation or are still stuck with a more procedural style of coding. Not that this is a problem; on the contrary, working code is what matters. But, as I wrote in my previous blog post [The Last Programming Language you will Learn](https://www.rdenadai.com.br/essay/last-programming-language-you-will-learn), you might eventually miss something and have the opportunity to change/improve the way you think and solve a problem.

## The pipe operator

Well, returning to the main topic, the operator discussed in that Bluesky post was the well-known pipeline operator.

This operator has several forms of use. However, F#, Elixir, and OCaml use the characters `|>`. Some examples to illustrate:

```elixir
"Elixir rocks" |> String.upcase() |> String.split()
# ["ELIXIR", "ROCKS"]
```

```ocaml
"OCaml rocks" |> String.uppercase_ascii |> String.split_on_char ' '
(* - : string list = ["OCAML"; "ROCKS"] *)
```

You can consult both the Elixir and OCaml documentation regarding the pipe operator:

- [Elixir: The pipe operator](https://hexdocs.pm/elixir/enumerable-and-streams.html#the-pipe-operator)
- [OCaml: The Pipe Operator](https://ocaml.org/docs/values-and-functions#the-pipe-operator)

Note that, in languages where the pipe operator does not exist, we would have two ways to do this.

### Chaining functions

Very similar to the example above, but more nested. We will place the call of one function as the parameter of the other.

> Please ignore the fact that I am writing Python functions that do not make sense; it is just to illustrate.

```python
def upper(s: str) -> str:
    return s.upper()

def split(s: str, char: str = " ") -> str:
    return s.split(char)

print(split(upper("Python rocks")))
# ["PYTHON", "ROCKS"]
```

### Method chaining

Many object-oriented languages adopt this syntax to chain methods using the dot notation (`.`), in order to allow operations similar to those we see with the pipe operator.

```python
print("Python Rocks".upper().split())
# ['PYTHON', 'ROCKS']
```

In this way, we have something very similar to the pipe operator, but working with objects.

## Why does the pipe operator matter?

This need to use the pipe operator appears mainly when we are working in the first case above (chaining functions) and, in the second, when we create an object that groups elements and we need to operate on them.

It is not that it is impossible not to use the pipe, but, in the end, the code can end up long and hard to read, especially when we create some kind of pipeline in which we will make several calls to different functions to operate on a data set.

Let us look at a relatively simple and biased example in Python.

```python
class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.items: Any = []

    def add_item(self, item: Any):
        self.items.append(item)


shopping_cart = ShoppingCart()
shopping_cart.add_item(Product("Apple", 1.0))
shopping_cart.add_item(Product("Banana", 0.5))
shopping_cart.add_item(Product("Avocado", 2.0))
shopping_cart.add_item(Product("Pineapple", 3.0))
shopping_cart.add_item(Product("Grapes", 2.5))
```

Calm down. First, I am just creating a very simple example. Now, let us filter all products with values greater than one, return their names, and print them.

```python
print(
    list(
        map(
            lambda p: p.name,
            filter(
                lambda p: p.price > 1.0,
                shopping_cart.items
            )
        )
    )
)
# ['Avocado', 'Pineapple', 'Grapes']
```

I left it more explicit on purpose, but we can see the problem that function chaining can cause: the order is from last to first.

But you, someone who works with Python, might be thinking: “but I can do this with list comprehensions,” and yes, you can and you actually should. List comprehensions (and, consequently, dict and set comprehensions) are amazing.

```python
print(
    [
        p.name
        for p in shopping_cart.items
        if p.price > 1.0
    ]
)
# ['Avocado', 'Pineapple', 'Grapes']
```

> P.S.: I wish more languages had this comprehension syntax; it is very cool.

Despite all that, there is something that bothers me a bit in Python comprehensions (nothing serious; I just find it annoying).

If we want to include an `else`, the comprehension structure changes more drastically and we start using it as a ternary.

```python
print(
    [
        p.name if p.price > 1.0 else "Not found"
        for p in shopping_cart.items
    ]
)
# ['Not found', 'Not found', 'Avocado', 'Pineapple', 'Grapes']
```

## Implementing a "pipe" operator

Ok, all of that is very cool, but the exercise here is: would it be possible to create something like the pipe operator in Python?

Well, we could modify CPython and add this operator, which would be quite a lot of work, and there have already been several attempts to add such an operator (or discussions around it) with direct support in Python, and all of them, so far, have not moved forward. Here are some examples:

- [https://discuss.python.org/t/pipe-operator/94333](https://discuss.python.org/t/pipe-operator/94333)
- [https://discuss.python.org/t/introduce-funnel-operator-i-e-to-allow-for-generator-pipelines/67701](https://discuss.python.org/t/introduce-funnel-operator-i-e-to-allow-for-generator-pipelines/67701)
- [https://discuss.python.org/t/functools-pipe-function-composition-utility/69744](https://discuss.python.org/t/functools-pipe-function-composition-utility/69744)

But that does not mean we cannot explore and think about whether it would be possible to implement such an operator in the language.

## Dunder methods

A major peculiarity that exists in Python is the well-known _dunder methods_ (or **dunder**, as you might find out there).

They are methods that exist in all Python objects and follow the language [Data Model](https://docs.python.org/3/reference/datamodel.html).

**_"Objects are Python’s abstraction for data. All data in a Python program is represented by objects or by relations between objects."_**

This implies that any object we create has an abundance of _dunder methods_ that we can implement, and this may be an interesting idea.

If you search now (leave the blog and go to the internet) for “pipe operator in Python,” you will surely find some blog where the author implemented, using classes and _dunder methods_, this pipe with the `|` character (which we also use as logical “or”).

Example:

```python
result = (
  Pipe("data.csv")
  | load_csv
  | filter_data
  | summarize
).result()
```

My idea goes in that direction too: to use a dunder method to replicate this. However, although the code above is possible, I do not understand it as something that is the pipe operator.

We have seen above how the operator works in Elixir and OCaml, and my idea is to get as close as possible to the same behavior. Another issue for me would be the use of | as an operator.

## Implementation

Well, another operator we can use and that, in this case, has more restricted use would be `>>`. This is a bitwise operator and, certainly, its use is quite restricted depending on the type of project.

I chose it because it is rarely used and, consequently, it is visually better compared to `|` (you can disagree without any problem).

That said, when looking at Python’s Data Model, we find the _dunder method_ `__rshift__` and its “opposite” counterpart, `__rrshift__`.

Perfect, therefore we have the following class:

```python
from __future__ import annotations

from collections import deque
from collections.abc import Callable, Generator, Iterator, Mapping, Sequence, Set
from functools import partial
from typing import Any


class pipe:
    def __init__(self, func: Callable[..., Any]) -> None:
        self._func = func
        self._name = func.__name__ if hasattr(func, "__name__") else func.__class__.__name__

    def __rshift__(self, other: Any) -> Any:
        result = self._func
        if callable(result) and not isinstance(result, (pipe, partial)):
            result = result()
        self._func = other._func
        self._name = other._name
        return self.__rrshift__(result)

    def __rrshift__(self, other: Any) -> Generator[Any, None, None] | Any:
        if (
            (isinstance(other, (Iterator, Sequence)) and self.__not_str_bytes(other))
            or isinstance(other, Mapping)
            or isinstance(other, Set)
        ) and not hasattr(self._func, "_materialize"):
            return self.__stream__(other)
        return self._func(other)

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        return self._func(*args, **kwargs)

    @staticmethod
    def filter(func: Callable[..., bool]) -> pipe:
        def __filter(data: Any) -> Generator[Any, None, None]:
            result = func(data)
            result = next(result) if isinstance(result, Generator) else result
            if result:
                yield data

        return pipe(__filter)

    @staticmethod
    def reduce(
        func: Callable[..., Any] | None = None,
        *,
        initializer: Any = None,
    ) -> Callable[[Callable[..., Any]], pipe]:
        _initializer = initializer

        def __reduce_dec(func: Callable[..., Any]) -> pipe:
            def __reduce(data: Any) -> Any:
                nonlocal _initializer
                if _initializer is None:
                    _initializer = data
                    yield data
                else:
                    result = func(_initializer, data)
                    _initializer = next(result) if isinstance(result, Generator) else result
                    yield _initializer

            return pipe(__reduce)

        if func is not None:
            return __reduce_dec(func)
        return __reduce_dec

    def __stream__(self, other: Any) -> Generator[Any, None, None]:
        def __generator_result(item: Any) -> Generator[Any, None, None]:
            result = self._func(item)
            if isinstance(result, Generator):
                yield from result
            else:
                yield result

        if isinstance(other, Mapping):
            yield from __generator_result(other)
        elif getattr(self._func, "__name__", None) == "__reduce":
            yield deque((next(__generator_result(item)) for item in other), maxlen=1).pop()
        else:
            for item in other:
                yield from __generator_result(item)

    def __not_str_bytes(self, item: Any) -> bool:
        return not isinstance(item, (str, bytes, bytearray))
```

Yes, I know: a lot of code, huge... a lot to unpack.

But that is fine; the implementation is also far from perfect or from working for all kinds of cases, and I do not dare to make a perfect implementation that would never be used anyway.

However, it works, and it works quite well for some very interesting things.

One important detail is that we need to wrap all our functions with this class so that we can “stack” them.

In some cases, I’ve already created some helpers to make things easier.

```python
from collections.abc import ItemsView, Iterator, Mapping, Sequence
from collections.abc import Set as _Set
from functools import partial
from typing import Any

from src.pipe import pipe
from src.support.utils import from_generator, materialize

STRUCTURAL_TYPES = (Sequence, Iterator, Mapping, _Set, ItemsView)

Parcial = lambda func, *args, **kwargs: pipe(partial(func, *args, **kwargs))
Print = pipe(print)


@materialize
def to_value(data: Any) -> Any:
    return from_generator(data)


class List:
    @materialize
    @staticmethod
    def to_value(data: Any) -> list:
        if isinstance(data, list):
            return data
        elif not isinstance(data, STRUCTURAL_TYPES):
            return [data]
        return list(data)


class Dict:
    @materialize
    @staticmethod
    def to_value(data: Any) -> dict:
        data = from_generator(data)
        if isinstance(data, dict):
            return data
        elif isinstance(data, (Sequence, Iterator)):
            return dict(data)
        else:
            return {data: data}


class Set:
    @materialize
    @staticmethod
    def to_value(data: Any) -> set:
        if isinstance(data, set):
            return data
        elif not isinstance(data, STRUCTURAL_TYPES):
            return {data}
        return set(data)


class String:
    @materialize
    @staticmethod
    def to_value(data: Any) -> str:
        return str(from_generator(data))


class Tuple:
    @materialize
    @staticmethod
    def to_value(data: Any) -> tuple:
        if isinstance(data, tuple):
            return data
        elif not isinstance(data, STRUCTURAL_TYPES):
            return (data,)
        return tuple(data)
```

But once that is done, we can play freely with our new operator.

```python
@pipe
def add_one(x: int) -> int:
    return x + 1

@pipe
def multiply_by_two(x: int) -> int:
    return x * 2

result = 3 >> add_one >> multiply_by_two >> Dict.to_value
assert result == {8: 8}
# {8: 8}
```

```python
class Person:
    __slots__ = ("name", "age")

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

@pipe.filter
def is_adult(person: Person) -> bool:
    return person.age >= 18

data = [Person("Alice", 17), Person("Bob", 20), Person("Charlie", 15), Person("David", 22)]
result = data >> is_adult >> List.to_value
assert [person.name
```

Very interesting, right? But wait: this class ends up using a very interesting concept we have in Python.

## Doing crazy with Generators

I do not know how many times I was writing some kind of pipeline, or modifying one, in which I needed to wait for all the data in each stage of the pipeline to proceed to the next.

One day I learned about _Generators_ and that, for sure, changed my view of how sequential processing could be partial.

I will not go into technical details of how _Generators_ work; you can consult Luciano Ramalho’s excellent book, [Python Fluente](https://pythonfluente.com/2/#ch_generators), to understand how they work.

But, with the way we implemented the _pipe_ class, we get for free the partial execution that a streaming pipeline with generators would provide.

```python
class Product:
    __slots__ = ("name", "price")

    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self) -> None:
        self.products = []

    def add_product(self, product: Product) -> None:
        self.products.append(product)

cart = ShoppingCart()
cart.add_product(Product("Laptop", 999.99))
cart.add_product(Product("Mouse", 25.50))
cart.add_product(Product("Keyboard", 45.00))
cart.add_product(Product("Monitor", 150.75))

@pipe
def apply_discount(product: Product) -> Product:
    product.price *= 0.9  # Apply a 10% discount
    yield product

@pipe.filter
def filter_expensive_products(product: Product) -> bool:
    yield product.price > 50

@pipe.reduce(initializer=0.0)
def sum_prices(x: float, y: Product) -> float:
    yield x + y.price

discounts = cart.products >> apply_discount >> List.to_value
assert all(
    abs(p.price - original_price * 0.9) < 1e-2
    for p, original_price in zip(discounts, [999.99, 25.50, 45.00, 150.75])
)

filtered_expensive = cart.products >> apply_discount >> filter_expensive_products >> List.to_value
assert len(filtered_expensive) == 2  # Laptop and Monitor
assert all(p.price > 50 for p in filtered_expensive)

total = cart.products >> apply_discount >> filter_expensive_products >> sum_prices >> to_value

assert round(total, 2) - 838.88  # Total price after discount for Laptop and Monitor
```

It is clear that the implementation is basic and this does not allow us to go very deep into how we nest our functions, especially when we use `map` and `filter`.

In such cases, you would need to wrap the functions inside a `lambda`, for example:

```python
@pipe
def random_number(N: int) -> int:
    yield random.randint(1, 100)

numbers = range(5) >> random_number >> List.to_value
assert len(numbers) == 5
assert all(1 <= num <= 100 for num in numbers)
# [69, 34, 2, 17, 90]  # Example output, will vary each run
```

## Conclusion

I believe that, as a small proof of concept that it would be possible to write a pipe operator for the Python language, this experiment had some value. If it did not, dear reader, that is fine; it served me to learn something.

From here there is not much to do, except perhaps to improve the implementation to cover more complex cases and the gaps I left along the way. Maybe even change the way I am chaining each call to avoid overloading the stack.

I think this post was more an exercise in curiosity for me, and I hope it might have piqued your curiosity to try to implement a pipe operator in your language, or even go learn more about Elixir or OCaml.

If you want the complete code, it’s [HERE](https://github.com/rdenadai/pipe)!

That is it. Happy coding 😆!
