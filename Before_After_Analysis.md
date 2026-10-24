# PatternWise — Before/After Analysis

This is a qualitative design comparison to be validated against the actual examples in the repository.

| Situation | Before applying a suitable pattern | After applying a suitable pattern | Expected effect |
|---|---|---|---|
| Shared service | Multiple instances may be created independently | A shared instance can be accessed through Singleton | Consistent access; shared-state trade-offs remain |
| Product creation | Client code may depend directly on concrete classes | Factory Method centralizes or delegates creation | Lower coupling |
| Complex object setup | Many constructor parameters or setup steps | Builder separates construction steps | Clearer configuration |
| Incompatible API | Client code must understand a foreign interface | Adapter translates the interface | Easier integration |
| Optional features | Subclasses multiply for combinations of features | Decorators wrap objects with extra behavior | Flexible composition |
| Multi-part subsystem | Client coordinates many components | Facade offers a simpler entry point | Simpler client code |
| Changing algorithms | Conditional logic selects behavior throughout client code | Strategy encapsulates alternatives | Easier substitution |
| Multiple event listeners | Publisher may directly call specific listeners | Observer uses subscription/notification | Looser coupling |

## Conclusion
Design patterns can improve maintainability when they address a real design problem. They are not automatically better in every case; the implementation should remain understandable and testable.
