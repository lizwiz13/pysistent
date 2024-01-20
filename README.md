Lazy persistent data structures in Python.

Persistent data structures are data structures, that can track their version history, thus allowing the user to return to a previous version of the structure.
The simplest example of a persistent data structure is a stack implemented as a linked-list: each version of the stack corresponds to a specific root node, so
the user can append new elements without changing the old nodes and thus mantaining all previous versions of the stack.

Persistent data structures are usually more relevant in functional programming as they work perfectly in an environment without code side-effects.
Python has a lot of syntactic similarities to some functional programming languages (such as Haskell), so with the right tools it is possible to
implement some more complex persistent data structures in python aswell. 
