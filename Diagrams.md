# PatternWise — Diagrams

The following Mermaid diagrams can be pasted into a Mermaid-compatible editor or Markdown viewer.

## High-level architecture
```mermaid
flowchart TD
    U[Student / Visitor] --> B[Web Browser]
    B --> R[Flask Routes]
    R --> T[HTML Templates]
    R --> P[Pattern Examples and Explanations]
    T --> B
```

## Learning flow
```mermaid
flowchart LR
    A[Open PatternWise] --> B[Choose a Design Pattern]
    B --> C[Read Intent and Use Case]
    C --> D[Inspect Example / Diagram]
    D --> E[Try Quiz]
    E --> F[Review Answer Key]
```

## Pattern-selection guide
```mermaid
flowchart TD
    A[Identify the design problem] --> B{Main concern?}
    B -->|Object creation| C[Factory Method]
    B -->|Complex construction| D[Builder]
    B -->|Interface mismatch| E[Adapter]
    B -->|Add behavior| F[Decorator]
    B -->|Complex subsystem| G[Facade]
    B -->|Swap algorithms| H[Strategy]
    B -->|Notify listeners| I[Observer]
    B -->|One shared instance| J[Singleton]
```
