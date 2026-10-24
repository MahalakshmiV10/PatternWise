# PatternWise — Pattern-Selection Checklist

Use this checklist to select a pattern based on the design problem. A pattern is a reusable approach, not a rule that must be used in every project.

- [ ] **Singleton** — Is one shared instance required to coordinate access to a resource?
- [ ] **Factory Method** — Should object creation be delegated to subclasses or a creation method?
- [ ] **Builder** — Does an object have many optional parts or a step-by-step construction process?
- [ ] **Adapter** — Do two interfaces need to work together despite incompatible APIs?
- [ ] **Decorator** — Must behavior be added to an object dynamically without changing its class?
- [ ] **Facade** — Would a simple interface help hide a complicated subsystem?
- [ ] **Strategy** — Should an algorithm be interchangeable at runtime?
- [ ] **Observer** — Should multiple listeners be notified when one object's state changes?

## Selection questions
1. What problem is being solved?
2. Which part changes most often?
3. Is object creation, interface compatibility, behavior extension, subsystem complexity, algorithm choice, or event notification the main issue?
4. Would the pattern reduce complexity, or add unnecessary abstraction?
5. Can the choice be explained with a small example and tested?
