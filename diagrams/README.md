# Diagrams

One Mermaid class diagram per pattern (`*.mmd` files). They are plain text.

## How to render

**Option A: VS Code (no internet needed after install)**
1. Open the Extensions panel (Ctrl+Shift+X).
2. Install a Mermaid preview extension (for example "Markdown Preview Mermaid Support" or "Mermaid Preview").
3. Open a `.mmd` file and use the extension's preview command.

**Option B: website**
1. Open https://mermaid.live in a browser.
2. Paste the contents of a `.mmd` file into the editor on the left.
3. The diagram appears on the right. You can download it as PNG or SVG for your slides.

> Status: these diagrams were NOT rendered by an image tool when the project was generated.
> A script (`tests/test_diagrams.py`) checks that class and method names match the code,
> but it cannot check that Mermaid draws them correctly. Render each one yourself and look at it.

## How to read the arrows

| Symbol | Name | Meaning in this project |
|--------|------|-------------------------|
| `A <\|-- B` | Inheritance | B inherits from A (B "is a" A). |
| `A o-- B` | Aggregation | A holds a B inside it, but B can exist on its own. |
| `A *-- B` | Composition | A creates and owns B (the Facade builds its default subsystems). |
| `A --> B` | Association | A keeps a reference to B and uses it. |
| `A ..> B` | Dependency | A uses or creates B temporarily. |

Other symbols: `<<abstract>>` = abstract class, `+` public, `-` private/internal, `$` = class-level (static) member.

## Manual checklist: compare each diagram with its source code

For every diagram, tick each item (the automatic test covers items 1 to 3):

- [ ] 1. Every class in the code file appears in the diagram.
- [ ] 2. Every class in the diagram exists in the code (no invented classes).
- [ ] 3. Every method listed in the diagram exists in that class.
- [ ] 4. Parameter names and return types match the code.
- [ ] 5. Inheritance arrows point from the parent to the child (`Parent <|-- Child`).
- [ ] 6. "Wraps", "uses" and "creates" arrows match what the code really does.
- [ ] 7. Abstract classes are marked `<<abstract>>`.
- [ ] 8. The diagram renders without a syntax error.

| Diagram | Code file |
|---------|-----------|
| singleton.mmd | patterns/creational/singleton.py |
| factory_method.mmd | patterns/creational/factory_method.py |
| builder.mmd | patterns/creational/builder.py |
| adapter.mmd | patterns/structural/adapter.py |
| decorator.mmd | patterns/structural/decorator.py |
| facade.mmd | patterns/structural/facade.py |
| strategy.mmd | patterns/behavioural/strategy.py |
| observer.mmd | patterns/behavioural/observer.py |
