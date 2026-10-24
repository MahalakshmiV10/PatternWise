# Pattern Notes

One section per pattern. Demo output below was produced by actually running each example during project generation (`python -m <module>`).
Source IDs (S01, S02 ...) point to `research/sources.md`. All sources are marked **needs verification** until you open them yourself.

## 1. Singleton

1. **Name and category:** Singleton (Creational)
2. **Simple definition:** A creational pattern that makes sure a class has only one object and gives one access point to it.
3. **Problem it solves:** Some things must exist only once, such as application settings. If every part of the program creates its own copy, the copies can disagree.
4. **Real-world analogy:** A school has one principal's office. Everyone who needs the principal goes to the same place.
5. **Software use case:** Application settings shared by the whole program.
6. **When to use:**
- Exactly one shared object is truly required (for example one settings object).
- Every part of the program must see the same state.
7. **When NOT to use:**
- You only want a global variable for convenience.
- You need to test parts separately (shared state leaks between tests).
- You might need two objects later.
8. **Advantages:**
- Only one instance is guaranteed.
- One clear access point.

   **Disadvantages:**
- Hidden global state.
- Harder to test.
- This simple version is NOT thread-safe (not tested for threads).
9. **Implementation:** `patterns/creational/singleton.py`
10. **Run the example:** `python -m patterns.creational.singleton`
11. **Expected terminal output (captured from a real run):**

```text
Same object? True
Theme read through 'second': dark
```

12. **UML diagram:** `diagrams/singleton.mmd`
13. **Classes and methods explained:**
- `AppConfig._instance` - class variable that stores the one object.
- `__new__` - runs when an object is requested; creates it only the first time.
- No `__init__` on purpose: `__init__` would run on every `AppConfig()` call and wipe the settings.
- `set_setting` / `get_setting` / `clear_settings` - store, read and clear settings.
- `reset_instance` - forgets the shared object; used by tests and by `demo()`.
14. **Unit tests:** `tests/test_singleton.py`
15. **Edge and failure cases:** Empty setting name raises `ValueError`. State leaking between tests is handled with `reset_instance()` in `setUp`/`tearDown`.
16. **Before and after:** see `docs/before_after_analysis.md`
17. **Viva question:** Why does AppConfig use `__new__` and not `__init__`?  
    **Answer:** `__new__` controls object creation, so it can return the existing object. `__init__` runs on every call and would reset the settings.
18. **References:** S02, S03 (and S01 for the original Gang of Four description). Needs verification.

---

## 2. Factory Method

1. **Name and category:** Factory Method (Creational)
2. **Simple definition:** A creational pattern where a base class has a creation method and subclasses decide which concrete class to create.
3. **Problem it solves:** Code with many `if type == 'email' ... elif type == 'sms'` checks has to be edited in many places when a new type is added.
4. **Real-world analogy:** A hotel booking desk: you ask for 'a room' and each hotel branch gives its own kind of room.
5. **Software use case:** Sending notifications by Email or by SMS.
6. **When to use:**
- You do not know in advance which exact class is needed.
- You want subclasses to choose the product.
7. **When NOT to use:**
- There is only one product type.
- A plain constructor call or a small function is enough.
8. **Advantages:**
- Main code works with the interface only (loose coupling).
- New types are added with new classes, not edits.

   **Disadvantages:**
- More classes.
- Parallel hierarchies (a creator class for each product class).
9. **Implementation:** `patterns/creational/factory_method.py`
10. **Run the example:** `python -m patterns.creational.factory_method`
11. **Expected terminal output (captured from a real run):**

```text
Email sent: Your exam hall ticket is ready
SMS sent: Your exam hall ticket is ready
```

12. **UML diagram:** `diagrams/factory_method.mmd`
13. **Classes and methods explained:**
- `Notification` - abstract product with `send()`.
- `EmailNotification`, `SmsNotification` - concrete products.
- `NotificationService` - abstract creator. `create_notification()` is the factory method; `notify()` is shared logic.
- `EmailService`, `SmsService` - override the factory method to choose the product.
14. **Unit tests:** `tests/test_factory_method.py`
15. **Edge and failure cases:** Empty or whitespace-only message raises `ValueError`. The abstract classes cannot be created directly (`TypeError`).
16. **Before and after:** see `docs/before_after_analysis.md`
17. **Viva question:** How is Factory Method different from a simple function with if/else?  
    **Answer:** Factory Method uses inheritance: each subclass overrides the creation method. A simple function keeps all the choices in one if/else block, which must be edited for every new type.
18. **References:** S02, S04 (and S01 for the original Gang of Four description). Needs verification.

---

## 3. Builder

1. **Name and category:** Builder (Creational)
2. **Simple definition:** A creational pattern that builds a complex object step by step and creates the final object in one last call.
3. **Problem it solves:** A constructor with many optional parameters is hard to read and easy to call wrongly.
4. **Real-world analogy:** Ordering a custom sandwich: you choose bread, fillings and sauce one step at a time.
5. **Software use case:** Creating a pizza order with optional toppings and extra cheese.
6. **When to use:**
- The object has many optional parts.
- You want validation before the final object exists.
7. **When NOT to use:**
- The object has two or three simple fields. A normal constructor or a dataclass with defaults is simpler.
8. **Advantages:**
- Readable step-by-step code.
- Optional parts are easy.
- The final object can be immutable.

   **Disadvantages:**
- Extra builder class.
- More code than a constructor.
9. **Implementation:** `patterns/creational/builder.py`
10. **Run the example:** `python -m patterns.creational.builder`
11. **Expected terminal output (captured from a real run):**

```text
small pizza, regular crust, toppings: none, extra cheese: no
large pizza, thin crust, toppings: onion, olives, extra cheese: yes
```

12. **UML diagram:** `diagrams/builder.mmd`
13. **Classes and methods explained:**
- `Pizza` - frozen dataclass (product). `describe()` returns text.
- `PizzaBuilder.__init__` - sets default values.
- `set_size`, `set_crust`, `add_topping`, `add_extra_cheese` - validate input, store it, and `return self` so calls can be chained.
- `build()` - checks the size was set, then creates the `Pizza`. Toppings are copied into a tuple so later builder calls do not change an already built pizza.
14. **Unit tests:** `tests/test_builder.py`
15. **Edge and failure cases:** `build()` without a size raises `ValueError`. Invalid size or crust and empty topping are rejected. A built pizza cannot be modified.
16. **Before and after:** see `docs/before_after_analysis.md`
17. **Viva question:** Why do the builder methods return `self`?  
    **Answer:** So calls can be chained in one readable expression, like `.set_size('large').add_topping('onion').build()`.
18. **References:** S02, S05 (and S01 for the original Gang of Four description). Needs verification.

---

## 4. Adapter

1. **Name and category:** Adapter (Structural)
2. **Simple definition:** A structural pattern that lets a class with one interface be used where another interface is expected.
3. **Problem it solves:** An old class gives data in the wrong form (Fahrenheit) but the application expects another form (Celsius), and the old class should not be changed.
4. **Real-world analogy:** A travel plug adapter that lets an Indian plug fit a foreign socket.
5. **Software use case:** Using an old Fahrenheit sensor in an app that expects Celsius.
6. **When to use:**
- You must reuse a class whose interface does not match.
- You cannot or should not edit the old class.
7. **When NOT to use:**
- You own the class and can simply change or rename the method.
- The interfaces already match.
8. **Advantages:**
- Reuse existing code without editing it.
- Conversion logic is in one place.

   **Disadvantages:**
- One more class.
- Can hide a design that should be cleaned up instead.
9. **Implementation:** `patterns/structural/adapter.py`
10. **Run the example:** `python -m patterns.structural.adapter`
11. **Expected terminal output (captured from a real run):**

```text
Legacy reading (F): 212.0
Temperature: 100.0 C
```

12. **UML diagram:** `diagrams/adapter.mmd`
13. **Classes and methods explained:**
- `CelsiusSensor` - the target interface the app expects.
- `LegacyFahrenheitSensor` - the old class (adaptee) with `read_fahrenheit()`.
- `FahrenheitToCelsiusAdapter` - holds the old sensor and implements `get_temperature_celsius()` using the formula (F - 32) x 5 / 9.
- `show_temperature()` - client function that only knows `CelsiusSensor`.
14. **Unit tests:** `tests/test_adapter.py`
15. **Edge and failure cases:** A reading below absolute zero (-459.67 F) raises `ValueError`. The legacy sensor is not changed by the adapter.
16. **Before and after:** see `docs/before_after_analysis.md`
17. **Viva question:** What is the difference between Adapter and Facade?  
    **Answer:** Adapter changes one interface so it matches another that a client expects. Facade gives a simpler interface to a group of classes.
18. **References:** S02, S06 (and S01 for the original Gang of Four description). Needs verification.

---

## 5. Decorator

1. **Name and category:** Decorator (Structural)
2. **Simple definition:** A structural pattern that adds behaviour to an object by wrapping it in another object with the same interface.
3. **Problem it solves:** Making a subclass for every combination (MilkCoffee, SugarCoffee, MilkSugarCoffee ...) creates too many classes.
4. **Real-world analogy:** Adding toppings to an ice cream: each topping wraps the previous one and adds to the price.
5. **Software use case:** A coffee order with optional milk and sugar.
6. **When to use:**
- Extras can be combined in many ways.
- You want to add behaviour at run time.
7. **When NOT to use:**
- Only one fixed combination exists; a simple subclass is enough.
- Many layers would make debugging confusing.
8. **Advantages:**
- No subclass explosion.
- Extras can be stacked in any order.

   **Disadvantages:**
- Many small objects.
- Layered wrappers are harder to debug.
9. **Implementation:** `patterns/structural/decorator.py`
10. **Run the example:** `python -m patterns.structural.decorator`
11. **Expected terminal output (captured from a real run):**

```text
Espresso: Rs 80
Espresso + Milk + Sugar: Rs 105
```

12. **UML diagram:** `diagrams/decorator.mmd`
13. **Classes and methods explained:**
- `Beverage` - abstract interface with `description()` and `cost()`.
- `Espresso` - the basic drink (Rs 80).
- `AddOnDecorator` - abstract wrapper that stores another `Beverage`.
- `MilkDecorator` (+Rs 20) and `SugarDecorator` (+Rs 5) - call the wrapped drink first, then add their own part.
14. **Unit tests:** `tests/test_decorator.py`
15. **Edge and failure cases:** Wrapping something that is not a `Beverage` raises `TypeError`. The wrapped object is not changed. This is the design pattern, not Python's `@decorator` syntax.
16. **Before and after:** see `docs/before_after_analysis.md`
17. **Viva question:** Is the Decorator pattern the same as Python's `@decorator`?  
    **Answer:** No. The pattern wraps objects at run time with the same interface. Python's `@` syntax wraps functions. The idea of wrapping is similar, but they are different things.
18. **References:** S02, S07 (and S01 for the original Gang of Four description). Needs verification.

---

## 6. Facade

1. **Name and category:** Facade (Structural)
2. **Simple definition:** A structural pattern that gives one simple interface to a group of complicated classes.
3. **Problem it solves:** Starting a home theater needs several classes called in the correct order. Clients should not need to remember all the steps.
4. **Real-world analogy:** The 'Movie mode' button on a smart remote that switches on many devices at once.
5. **Software use case:** Starting and stopping a home theater with one method call.
6. **When to use:**
- A subsystem has many classes and steps.
- Most clients need only a simple way to use it.
7. **When NOT to use:**
- Clients need fine control over every part.
- The facade would grow into one huge class that does everything.
8. **Advantages:**
- Simple client code.
- Steps and order are kept in one place.

   **Disadvantages:**
- The facade can become too big.
- It can hide features that some clients need.
9. **Implementation:** `patterns/structural/facade.py`
10. **Run the example:** `python -m patterns.structural.facade`
11. **Expected terminal output (captured from a real run):**

```text
Projector: power on
Amplifier: power on
Amplifier: volume set to 5
Player: playing 'Inception'
---
Player: stopped
Amplifier: power off
Projector: power off
```

12. **UML diagram:** `diagrams/facade.mmd`
13. **Classes and methods explained:**
- `Amplifier`, `Projector`, `StreamingPlayer` - the subsystem classes.
- `HomeTheaterFacade.__init__` - creates default subsystems or accepts given ones (useful for testing).
- `watch_movie(title)` - starts projector, amplifier, volume and player in order.
- `end_movie()` - stops everything in order.
14. **Unit tests:** `tests/test_facade.py`
15. **Edge and failure cases:** Empty title raises `ValueError` and nothing starts. `end_movie()` without a running movie raises `RuntimeError`. The facade does not stop anyone from using the subsystem classes directly.
16. **Before and after:** see `docs/before_after_analysis.md`
17. **Viva question:** Does a Facade prevent using the subsystem classes directly?  
    **Answer:** No. It only offers an easier way. Advanced users can still use the subsystem classes.
18. **References:** S02, S08 (and S01 for the original Gang of Four description). Needs verification.

---

## 7. Strategy

1. **Name and category:** Strategy (Behavioural)
2. **Simple definition:** A behavioural pattern that puts each algorithm in its own class with a common interface so they can be swapped.
3. **Problem it solves:** Shipping cost code with a long if/elif chain must be edited whenever a new shipping type is added.
4. **Real-world analogy:** Going to college by bus, bike or car: same goal, different method.
5. **Software use case:** Calculating shipping cost with Standard, Express or Free shipping.
6. **When to use:**
- Several ways to do the same job exist.
- You need to switch the way at run time.
7. **When NOT to use:**
- Only one algorithm exists and no change is planned.
- A simple if/else for two stable cases is enough.
8. **Advantages:**
- Algorithms are separated and easy to test.
- New strategies need no change to `Order`.

   **Disadvantages:**
- More classes.
- The client must know which strategies exist.
9. **Implementation:** `patterns/behavioural/strategy.py`
10. **Run the example:** `python -m patterns.behavioural.strategy`
11. **Expected terminal output (captured from a real run):**

```text
Standard shipping: Rs 70
Express shipping:  Rs 175
Free shipping:     Rs 0
```

12. **UML diagram:** `diagrams/strategy.mmd`
13. **Classes and methods explained:**
- `ShippingStrategy` - abstract interface with `calculate_cost()`.
- `StandardShipping` (40 + 10 per kg), `ExpressShipping` (100 + 25 per kg), `FreeShipping` (0). Weight is rounded up with `math.ceil`.
- `Order` - the context. Stores weight and a strategy; `set_strategy()` swaps it; `shipping_cost()` asks the strategy.
14. **Unit tests:** `tests/test_strategy.py`
15. **Edge and failure cases:** Weight of zero or less raises `ValueError`. A non-strategy object raises `TypeError`. 0.1 kg is charged as 1 kg.
16. **Before and after:** see `docs/before_after_analysis.md`
17. **Viva question:** How does Strategy help follow the Open/Closed idea?  
    **Answer:** You add a new strategy class instead of editing `Order`, so existing code stays unchanged.
18. **References:** S02, S09 (and S01 for the original Gang of Four description). Needs verification.

---

## 8. Observer

1. **Name and category:** Observer (Behavioural)
2. **Simple definition:** A behavioural pattern where a subject tells all subscribed observers automatically when something happens.
3. **Problem it solves:** Many objects need to know about changes, and the publisher should not be tied to each one.
4. **Real-world analogy:** Subscribers of a YouTube channel get notified when a new video is uploaded.
5. **Software use case:** A news publisher sending messages to subscribers.
6. **When to use:**
- One change must reach many objects.
- Subscribers can join and leave at run time.
7. **When NOT to use:**
- Only one fixed receiver exists; a direct method call is simpler.
- Chains of updates would become hard to follow.
8. **Advantages:**
- Publisher and subscribers are loosely connected.
- Subscribers can be added or removed freely.

   **Disadvantages:**
- Forgotten `detach()` can keep objects alive.
- If one observer raises an error, later observers are not notified (this simple version does not handle that; not tested).
9. **Implementation:** `patterns/behavioural/observer.py`
10. **Run the example:** `python -m patterns.behavioural.observer`
11. **Expected terminal output (captured from a real run):**

```text
First news sent to 2 subscribers
Second news sent to 1 subscriber
Asha received: ['Exam timetable released', 'Holiday on Friday']
Ravi received: ['Exam timetable released']
```

12. **UML diagram:** `diagrams/observer.mmd`
13. **Classes and methods explained:**
- `Observer` - abstract interface with `update(message)`.
- `Subscriber` - stores its name and every received message.
- `NewsPublisher` - keeps the observer list. `attach` adds (duplicates ignored), `detach` removes, `publish` notifies all and returns how many were notified.
14. **Unit tests:** `tests/test_observer.py`
15. **Edge and failure cases:** Detaching an unknown observer raises `ValueError`. Empty message raises `ValueError`. Publishing with no subscribers returns 0.
16. **Before and after:** see `docs/before_after_analysis.md`
17. **Viva question:** What happens to a subscriber after `detach()`?  
    **Answer:** It no longer receives messages, but messages it received earlier are still stored.
18. **References:** S02, S10 (and S01 for the original Gang of Four description). Needs verification.

---
