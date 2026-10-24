# PatternWise Quiz

Choose the best answer for each question. Answers are in `answer_key.md`.

## Question 1 (Scenario)

A game needs exactly ONE shared settings object that every screen reads and updates. Which pattern fits best?

- A) Singleton
- B) Builder
- C) Observer
- D) Adapter

## Question 2 (Scenario)

A base class has a method that must return a notification object. The Email subclass and the SMS subclass each decide which concrete class to create. Which pattern is this?

- A) Strategy
- B) Decorator
- C) Factory Method
- D) Facade

## Question 3 (Scenario)

A constructor takes nine parameters, most of them optional, and calls like Pizza('large', None, None, True, None, ...) are hard to read. Which pattern helps?

- A) Adapter
- B) Builder
- C) Singleton
- D) Observer

## Question 4 (Scenario)

Your app expects get_temperature_celsius(), but an old library you cannot edit only offers read_fahrenheit(). Which pattern fits?

- A) Strategy
- B) Builder
- C) Singleton
- D) Adapter

## Question 5 (Scenario)

Customers may add milk, sugar, or both to any drink, and the price must add up, without writing a subclass for every combination. Which pattern fits?

- A) Decorator
- B) Factory Method
- C) Singleton
- D) Facade

## Question 6 (Scenario)

Starting a home theater needs a projector, an amplifier and a player, in the correct order. The client wants ONE simple call. Which pattern fits?

- A) Observer
- B) Facade
- C) Adapter
- D) Builder

## Question 7 (Pattern selection)

A shop must switch between Standard, Express and Free shipping calculations at run time, using the same Order class. Which pattern fits?

- A) Singleton
- B) Facade
- C) Strategy
- D) Adapter

## Question 8 (Pattern selection)

When a publisher posts news, every subscriber must be informed automatically, and subscribers can leave at any time. Which pattern fits?

- A) Strategy
- B) Facade
- C) Singleton
- D) Observer

## Question 9 (Code understanding)

What does the program print?

```python
first = AppConfig()
second = AppConfig()
print(first is second)
```

- A) True
- B) False
- C) An error is raised
- D) None

## Question 10 (Code understanding)

Espresso costs 80, MilkDecorator adds 20 and SugarDecorator adds 5. What does the program print?

```python
drink = SugarDecorator(MilkDecorator(Espresso()))
print(drink.cost())
```

- A) 100
- B) 105
- C) 125
- D) 25

## Question 11 (Code understanding)

Two Subscriber objects, a and b, are attached. Then b is detached. How many subscribers receive 'Hi'?

```python
publisher.attach(a)
publisher.attach(b)
publisher.detach(b)
publisher.publish('Hi')
```

- A) 0
- B) 1
- C) 2
- D) 3

## Question 12 (When NOT to use)

A program needs to convert kilometres to miles with one fixed formula that will never change. What is the best approach?

- A) A Strategy class for each formula
- B) A Singleton converter object
- C) A simple function
- D) An Observer for the result

## Question 13 (When NOT to use)

Your shop will only ever use Standard shipping and no change is planned. Is the Strategy pattern needed?

- A) Yes, always use Strategy for any calculation
- B) No, a simple method is enough until there are several interchangeable algorithms
- C) Yes, because Strategy is faster
- D) No, because Strategy only works for payments

## Question 14 (Pattern selection)

Which list contains ONLY structural patterns?

- A) Adapter, Decorator, Facade
- B) Singleton, Adapter, Facade
- C) Strategy, Observer, Decorator
- D) Builder, Facade, Adapter

## Question 15 (When NOT to use)

What is a common problem when many unit tests use a Singleton?

- A) A Singleton cannot store data
- B) Data set by one test can stay and affect other tests
- C) A Singleton cannot be imported
- D) A Singleton makes Python crash
