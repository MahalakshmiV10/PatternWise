# Viva Questions and Answers

## General questions

**Q1. What is a design pattern?**  
A reusable, named solution to a problem that appears again and again in software design. It is a guide, not copy-paste code.

**Q2. Name the three categories.**  
Creational (how objects are created), Structural (how objects are combined), Behavioural (how objects communicate and share work).

**Q3. Is it always good to use a design pattern?**  
No. Patterns add classes and complexity. If simple code solves the problem and is unlikely to change, simple code is better.

**Q4. How did AI help, and how did you check it?**  
AI helped draft explanations and code. Every claim must be checked: run the tests, compare diagrams with code, and open the sources. (Fill in your own honest record in `docs/ai_verification_report.md`.)

**Q5. How do you know your code works?**  
Run `python run_all.py`. It runs the eight examples and all unit tests and exits with a non-zero code if any check fails.

**Q6. How do you know your diagrams match your code?**  
`tests/test_diagrams.py` compares class and method names. I also render each diagram and compare it with the code using the checklist in `diagrams/README.md`.

## Pattern questions

**Singleton: Why does AppConfig use `__new__` and not `__init__`?**  
`__new__` controls object creation, so it can return the existing object. `__init__` runs on every call and would reset the settings.

**Factory Method: How is Factory Method different from a simple function with if/else?**  
Factory Method uses inheritance: each subclass overrides the creation method. A simple function keeps all the choices in one if/else block, which must be edited for every new type.

**Builder: Why do the builder methods return `self`?**  
So calls can be chained in one readable expression, like `.set_size('large').add_topping('onion').build()`.

**Adapter: What is the difference between Adapter and Facade?**  
Adapter changes one interface so it matches another that a client expects. Facade gives a simpler interface to a group of classes.

**Decorator: Is the Decorator pattern the same as Python's `@decorator`?**  
No. The pattern wraps objects at run time with the same interface. Python's `@` syntax wraps functions. The idea of wrapping is similar, but they are different things.

**Facade: Does a Facade prevent using the subsystem classes directly?**  
No. It only offers an easier way. Advanced users can still use the subsystem classes.

**Strategy: How does Strategy help follow the Open/Closed idea?**  
You add a new strategy class instead of editing `Order`, so existing code stays unchanged.

**Observer: What happens to a subscriber after `detach()`?**  
It no longer receives messages, but messages it received earlier are still stored.
