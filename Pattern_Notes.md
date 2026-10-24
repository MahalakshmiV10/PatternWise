# PatternWise — Pattern Notes

## 1. Singleton
**Intent:** Ensure a class has one shared instance and provide a common access point.  
**Use when:** A genuinely shared coordinator or resource is required.  
**Watch out:** Global shared state can make testing and concurrency harder.  
**Example idea:** One application configuration manager.

## 2. Factory Method
**Intent:** Let a creation method decide which concrete product to return.  
**Use when:** Client code should depend on a common product interface rather than concrete classes.  
**Watch out:** Too many product types can increase class complexity.  
**Example idea:** A notification creator returns email or SMS notification objects.

## 3. Builder
**Intent:** Construct a complex object step by step.  
**Use when:** Many optional settings or construction steps would make a constructor confusing.  
**Watch out:** A builder may be excessive for a simple object.  
**Example idea:** Configure a report with title, sections, and output format.

## 4. Adapter
**Intent:** Convert one interface into another interface the client expects.  
**Use when:** Integrating legacy code or a third-party API with a different interface.  
**Watch out:** Too many adapters can obscure the underlying API.  
**Example idea:** Adapt a legacy temperature service to a standard temperature interface.

## 5. Decorator
**Intent:** Add responsibilities to an object by wrapping it.  
**Use when:** Features should be combined flexibly without creating many subclasses.  
**Watch out:** Several wrappers can make execution order harder to trace.  
**Example idea:** Add logging or compression around a data stream.

## 6. Facade
**Intent:** Provide a simple entry point to a complex subsystem.  
**Use when:** Clients should not need to coordinate many subsystem components.  
**Watch out:** Avoid turning the facade into an oversized class containing all logic.  
**Example idea:** A home-theatre facade starts the display, speakers, and player.

## 7. Strategy
**Intent:** Encapsulate alternative algorithms behind a common interface.  
**Use when:** The algorithm should be chosen or changed without rewriting the client.  
**Watch out:** The client or configuration still needs to select a strategy.  
**Example idea:** Choose standard, express, or pickup delivery calculation.

## 8. Observer
**Intent:** Notify subscribed observers when a subject changes.  
**Use when:** One event should update multiple independent listeners.  
**Watch out:** Manage subscriptions and avoid unexpected notification chains.  
**Example idea:** Notify dashboard widgets when a data source updates.

## Comparison
| Pattern | Main design concern | Typical benefit |
|---|---|---|
| Singleton | Shared instance | Centralized access |
| Factory Method | Object creation | Reduced coupling to concrete products |
| Builder | Construction | Clear step-by-step setup |
| Adapter | Interface mismatch | Compatibility |
| Decorator | Add-on behavior | Flexible composition |
| Facade | Subsystem complexity | Simpler client interface |
| Strategy | Algorithm variation | Easy algorithm substitution |
| Observer | Event notification | Loose coupling between publisher and listeners |
