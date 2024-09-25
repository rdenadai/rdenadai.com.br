For a long time, I've been trying to better guide my studies in general. Python is one of those subjects that has caught my interest over the years, and I’ve tried to gain a solid understanding of the language and its ecosystem.

I even wrote a post about [`10 Python Packages You Can't Live Without`](https://rdenadai.com.br/essay/5), which, if I recall correctly, was published almost 8 years ago.

Over the years, I’ve been refining my understanding of what I need to learn in Python. This became clearer in recent years when people started asking me what they should learn to become proficient Python developers, and if I had a roadmap or something similar (resources and other stuff).

After a few iterations, I’ve come up with this "list," which I'll try to keep updated as much as possible (Python is an evolving language, so new features may appear).

I divided the list by proficiency level, starting with beginners and moving up to specialists. I didn’t add explanations to each topic, so you’ll need to search for them in the documentation and other materials. However, you’ll have a direction and a term to look for.

> This list is not comprehensive, nor is it a strict rule. It’s simply a guide to help you understand what you might need to learn at various points in your Python journey.

## **Python "Expert" Path**

### **Beginner**

- Basic syntax
  - Variables types:
    - `bool`, `int`, `float`, `str`, `byte`, `complex`, `None`
  - Conditionals:
    - `if`, `else`, `elif`, `for`, `while`, `match`
  - Functions: simple use, and known what **first class citizen** is (concept)
  - Data structures:
    - `list`, `tuple`, `dict`, `set`
  - Exception handling
- File I/O
- Compreensions: `list`, `dict`
- f-strings

### **Intermediate**

- Debugger (pdb, debugpy)
- pep8
- Python package (pip, etc)
- Walrus operator `:=`
- Type Annotations
  - Basic types
- Functions: `*args` | `**kwargs`
- Other data structures: `namedtuple`, `queue`, `enum`, `heapq`, `MappingProxyType
- StandardLib:
  - `Decimal` (float point errors)
  - `pickle`
- Context Manager
- Object-Oriented
  - `__init__` | `__new__`
  - **dunder** methods
  - Abstract Base Class
  - `dataclasses`
- Iterators
- Functional programming
  - Lambda
  - Closure
  - `map`, `filter`, `reduce`
- Decorators
- Compreensions: `set`

### **Advanced**

- Variable types:
  - `bytearray`, `memoryview`
- StandardLib:
  - `functools`, `itertools`, `bisect`, `collections`, `contextvars`, `tracemalloc`
- Generators
  - Generator expressions
- Object-Oriented
  - `__slots__`
  - `__mro__`
  - `property`
  - Multiple Inheritance (**Mixins**)
- Functional programming
  - `functools.partial`
  - Memoization
  - Immutability
- Paralelism and Concurrency
  - Process (`ProcessPoolExecutor`, `SharedMemory`)
  - Thread (`ThreadPoolExecutor`)
  - `asyncio` (`TaskGroup`, `Exception Groups`)

### Specialist

- Coroutines
- StandardLib
  - `ast`
  - `inspect`
  - `types`
- Type Annotations
  - Variadic Generics
  - `Protocol`
- Object-Oriented
  - Descriptors
  - Metaclasses
- Deploy and management of python packages
- Interpreters (and environment around them)
  - CPython
  - Pypy
  - Pyston
- CPython Internals
  - Memory Management
  - GIL (Global Interpreter Lock)

## **Resources**

![Python Logo](/static/pages/essays/15/image.png)

Of course that there's much more resources than the ones listed here, but this is a good start point:

- [Official Python Documentation](https://docs.python.org/3/)
- [Fluent Python](https://pythonfluente.com/)
- [Think Python](https://allendowney.github.io/ThinkPython/)
- [Python Cheatsheet](https://www.pythoncheatsheet.org/)
- [Real Python](https://realpython.com/)
- [What the f\*ck Python!](https://github.com/satwikkansal/wtfpython)
- [Awesome Python](https://github.com/vinta/awesome-python)
- [My Python Start Projects on Github](https://github.com/stars/rdenadai/lists/python)
- [Talk Python to Me](https://talkpython.fm/)
- [Python Bytes](https://pythonbytes.fm/)
