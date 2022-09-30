## Time committment

You can spend as much time as you want on the exercise, but you are absolutely free to put a time limit (we recommend 3 hours) and tell us about it. We respect the fact that you might have other hiring processes and that you don't have a lot of time.

## Deliverable

Please make sure you include the following items:

- `[README.md](http://README.md)`
    - General approach
    - Technical choices
    - How did you evaluate the solution?
    - How much time did you spend on the exercise?
    - Remaining todos
    - ... and any other item you think should appear in a README.

The code, its comments and the README should all be in English. Don't forget to proofread yourself (tip: feel free to use Grammarly)!

## Functional specifications

The aim of this assessment is to challenge you on a technical basis, involving machine learning, programming and research skills.

➡️  ➡️ Goal

Your goal is to develop an algorithm that allows detecting the hierarchical structure of documents (Section 1, Section 2, Subsection 2.1, Subsection 2.2, etc.). For example:

    file test.pdf
        ├── Section 1
        │   ├── Subsection 1.1
        │   └── Subsection 1.2
        ├── Section 2
        │   ├── Subsection 2.1
        │   └── Subsection 2.2
        └── Section 3

For such purposes, your solution should return an API where the user can upload a pdf file and get a JSON output containing the document's structure and the corresponding text for each (sub)session.

➡️  ➡️ How?

For this assessment, we provide data as a pdf file [test.pdf]](http://test.pdf) that is a scientific article.
## Technical specifications

- We can read most programming languages. Just so you know, we mostly use Python and Augular/TypeScript at Upskills. Justify the language you chose in your README.
- You can use any library or framework. Justify all your important choices in your README.
- You can challenge *anything* that we've currently implemented.

## How we review

The most important thing is that **you should feel proud of your work**. If you don't have time to finish, it is better to polish what you've already done than start something and risk not doing it well. You can always include a list of remaining todos in the README - we will take it into account when we review. Focus on the things that let your skills shine!

We will have a look at the following aspects:

- Correctness: does your solution work?
- Performance: what is the quality of your solution? How fast is the process?
- Maintainability: does your code include the necessary best practices to make it easy for a team to build on top of it? Have you fixed most of the issues with our implementation?
- Code style: how easy is it to read and comprehend your code? Are you following the language's code style (e.g. PEP8 for Python)?

Those aspects are **critical** to us:

- Writing skills: make sure to proofread yourself and remove all typos, orthographical mistakes, etc.
- Important technical tradeoffs need to be justified.

## Our tips

If you're using Python:

- Consider using poetry to handle dependencies
- Consider using a linter (e.g. flake8) and an autoformatter (e.g. black)
- Consider using FastAPI to create an API

## Need help?

Any question? Reach out to us! We'd love to help you!

🚀  Good luck & happy coding!