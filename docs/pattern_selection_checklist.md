# Pattern Selection Checklist

Design patterns are **optional tools, not rules**. A pattern is worth using only when it makes a real problem easier. Answer these questions before choosing one.

## Step 1: Understand the problem

- [ ] What exact problem am I trying to solve? (Write it in one sentence.)
- [ ] Is the problem likely to happen again, or is it a one-time case?
- [ ] Is simple procedural or object-oriented code (a function, a class, an `if`) enough?
- [ ] Which responsibility is changing or likely to change?

## Step 2: Match the need to a pattern

| Question | If YES, consider |
|----------|------------------|
| Must there be exactly one shared object? | Singleton (check testing and hidden-state cost first) |
| Do I need flexible object creation, where subclasses choose the class? | Factory Method |
| Is the object complex with many optional parts? | Builder |
| Do I need to make an incompatible interface work? | Adapter |
| Do I need to add behaviour dynamically, in combinations? | Decorator |
| Do I need one simple entry point to a complicated subsystem? | Facade |
| Do I need interchangeable algorithms? | Strategy |
| Do multiple components need notifications? | Observer |

## Step 3: Check the cost

- [ ] What extra classes and complexity will the pattern add?
- [ ] Is there a simpler solution (for example a function, a dictionary, default arguments)?
- [ ] Will a teammate or examiner understand it quickly?
- [ ] How will I test the design? (Can I create the objects in a test without hidden shared state?)
- [ ] Are there security, privacy or maintenance concerns?

## Step 4: Decide

- If the simple solution passes Step 3, **do not use a pattern**.
- If the pattern clearly removes repeated edits or tangled code, use it and write the reason in a comment or the report.

## Worked mini-examples

| Situation | Decision | Why |
|-----------|----------|-----|
| Convert km to miles with one fixed formula | No pattern, use a function | One algorithm, no variation |
| Three shipping methods chosen at run time | Strategy | Interchangeable algorithms |
| A class with 3 simple fields | No pattern, use a dataclass | Builder would be extra code |
| Old library returns Fahrenheit, app needs Celsius, cannot edit library | Adapter | Interface mismatch |
