# Speaker Notes (about 1 minute per slide)

**Slide 1.** Introduce yourself and the project question. Say what a design pattern is in one sentence: "a reusable, named solution to a common design problem." Mention the project is called PatternWise.

**Slide 2.** Explain the problem: patterns are abstract, and AI can produce answers that look right but are wrong. Walk through the five steps. Stress that you checked AI output instead of trusting it. Only claim the checks you really did.

**Slide 3.** Explain the three categories with one everyday sentence each: creating things, connecting things, and things talking to each other. Say clearly that patterns are optional and sometimes simple code is better.

**Slide 4.** Pick two or three patterns to explain in detail (for example Decorator and Observer), and mention the rest quickly. For Decorator, show 80 + 20 + 5 = 105. For Observer, point out that an unsubscribed observer stops receiving messages. Be ready for questions on any of the eight.

**Slide 5.** Show the folder structure and say each folder's job. Explain that `main.py` reads pattern information from the catalog and runs each example. Show one rendered diagram and explain the arrows (inheritance, wrapping, uses). Say that tests compare diagram names with code, but you also compared visually.

**Slide 6.** Show `python run_all.py` and its summary. Explain that it fails honestly: non-zero exit code if any check fails. Then talk about responsible AI: AI can be wrong, sources need checking, and you must understand and disclose your use of AI per your institution's rules.

**Slide 7.** Give your own real results. State limitations openly (examples are simple, Singleton is not thread-safe, anything you did not check). Finish with the conclusion: AI helps with drafts; testing and verification are what make the project trustworthy. Invite questions.

**Do not say:** any number or result you did not see yourself.
