# Before and After Analysis

The BEFORE snippets are short illustrations of the problem. They are **not part of the project code and were not executed**.
The AFTER column describes the real code in `patterns/`, which is covered by the unit tests.

Reminder: patterns add classes. If the BEFORE code is small and will not change, it may be the better choice.

## 1. Singleton

**Before (problem):**

```python
config_a = AppConfig()   # a normal class
config_b = AppConfig()
config_a.theme = 'dark'
print(config_b.theme)  # error or different value: two separate objects
```

**After:** AppConfig() always returns the same object, so `config_b` sees the theme set through `config_a`.

**Trade-off:** Hidden global state.

## 2. Factory Method

**Before (problem):**

```python
def send(kind, message):
    if kind == 'email':
        return 'Email sent: ' + message
    elif kind == 'sms':
        return 'SMS sent: ' + message
    # a new channel means editing this function (and every similar one)
```

**After:** A new channel is a new `Notification` class plus a new service subclass. `notify()` is not edited.

**Trade-off:** More classes.

## 3. Builder

**Before (problem):**

```python
pizza = Pizza('large', 'thin', ['onion', 'olives'], True)
# What does True mean? Which argument is the crust?
```

**After:** `PizzaBuilder().set_size('large').set_crust('thin').add_topping('onion').add_extra_cheese().build()` names every choice, and validates it.

**Trade-off:** Extra builder class.

## 4. Adapter

**Before (problem):**

```python
fahrenheit = legacy.read_fahrenheit()
celsius = (fahrenheit - 32) * 5 / 9   # repeated in every place that needs Celsius
```

**After:** The formula lives once in `FahrenheitToCelsiusAdapter`. Client code calls `get_temperature_celsius()`.

**Trade-off:** One more class.

## 5. Decorator

**Before (problem):**

```python
class MilkCoffee(Espresso): ...
class SugarCoffee(Espresso): ...
class MilkSugarCoffee(Espresso): ...   # one class per combination
```

**After:** Two wrapper classes cover every combination: `SugarDecorator(MilkDecorator(Espresso()))`.

**Trade-off:** Many small objects.

## 6. Facade

**Before (problem):**

```python
projector.turn_on()
amplifier.turn_on()
amplifier.set_volume(5)
player.play('Inception')   # client must remember the order every time
```

**After:** `theater.watch_movie('Inception')` does all four steps in the right order.

**Trade-off:** The facade can become too big.

## 7. Strategy

**Before (problem):**

```python
def shipping_cost(kind, weight):
    if kind == 'standard':
        return 40 + 10 * ceil(weight)
    elif kind == 'express':
        return 100 + 25 * ceil(weight)
    else:
        return 0   # new kind = edit this function
```

**After:** Each algorithm is a class. `order.set_strategy(ExpressShipping())` swaps it without touching `Order`.

**Trade-off:** More classes.

## 8. Observer

**Before (problem):**

```python
def publish(message):
    asha.receive(message)
    ravi.receive(message)   # publisher knows every receiver; new one = edit publish()
```

**After:** The publisher only knows the `Observer` interface. Subscribers join with `attach()` and leave with `detach()`.

**Trade-off:** Forgotten `detach()` can keep objects alive.
