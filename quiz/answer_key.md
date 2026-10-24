# PatternWise Quiz: Answer Key

| Q | Answer | Explanation |
|---|--------|-------------|
| 1 | A) Singleton | Singleton guarantees one instance with a global access point. |
| 2 | C) Factory Method | In Factory Method, subclasses override a creation method to choose the concrete product. |
| 3 | B) Builder | Builder constructs an object step by step and lets you skip optional parts clearly. |
| 4 | D) Adapter | Adapter converts one interface into the interface the client expects. |
| 5 | A) Decorator | Decorator wraps an object to add behaviour, and wrappers can be stacked. |
| 6 | B) Facade | Facade offers a simple interface to a group of subsystem classes. |
| 7 | C) Strategy | Strategy keeps interchangeable algorithms in separate classes that the context can swap. |
| 8 | D) Observer | Observer defines a one-to-many dependency so subscribers are notified automatically. |
| 9 | A) True | AppConfig is a Singleton, so both variables refer to the same object and 'is' gives True. |
| 10 | B) 105 | 80 + 20 + 5 = 105. Each decorator adds its price to the wrapped drink's price. |
| 11 | B) 1 | Only a is still attached, so only a receives the message. publish() also returns 1. |
| 12 | C) A simple function | One fixed formula needs no pattern. A plain function is simpler and easier to test. |
| 13 | B) No, a simple method is enough until there are several interchangeable algorithms | Patterns add classes and complexity. Use Strategy only when there are really several algorithms to swap. |
| 14 | A) Adapter, Decorator, Facade | Adapter, Decorator and Facade are structural. Singleton and Builder are creational. Strategy and Observer are behavioural. |
| 15 | B) Data set by one test can stay and affect other tests | The shared instance keeps its state between tests, so tests must reset it (like reset_instance() in this project). |
