## Time committment

You can spend as much time as you want on the exercise, but you are absolutely free to put a time limit (we recommend 3 hours) and tell us about it. We respect the fact that you might have other hiring processes and that you don't have a lot of time.

## Deliverable

Please make sure you include the following items:

- `[README.md](http://README.md)`
    - General approach
    - Technical choices
    - How long does the new process take (in seconds)?
    - How much time did you spend on the exercise?
    - Remaining todos
    - ... and any other item you think should appear in a README.

The code, its comments and the README should all be in English. Don't forget to proofread yourself (tip: feel free to use Grammarly)!

## Functional specifications

We have implemented a very simple data pipeline that puts raw JSON data into a Postgres database. There are a lot of things that are wrong with our implementation. Can you fix them? Please document what you fixed, either via clear git commit messages, or with a list of items in your README.

We are also not happy with the performance: it takes a very long time to ingest the data. What are you ideas to improve the time to ingest? Document them in your README, then implement them. To keep the architecture realistic, please do not challenge the fundamental assumption that we're using a relational database storing its data on disk and focus on the ingestion process.

➡️  ➡️  Here's the code:

[hiring-test-data-engineering.tar.gz](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b477f537-1eb5-4114-90b3-65222b398555/hiring-test-data-engineering.tar.gz)

Here are some ideas of other things to build if you have time:

- Propose a better structure for the SQL tables
- Provide a nice datavisualization of the data
- Add the ability to handle larger files (1 Go? 10 Go? The sky's the limit!)
- How would you handle an input that is too big to fit in memory?

## Technical specifications

- We can read most programming languages. Just so you know, we mostly use Python and TypeScript at Octopize. Justify the language you chose in your README.
- You can use any library or framework. Justify all your important choices in your README.
- You can challenge *anything* that we've currently implemented.

## How we review

The most important thing is that **you should feel proud of your work**. If you don't have time to finish, it is better to polish what you've already done than start something and risk not doing it well. You can always include a list of remaining todos in the README - we will take it into account when we review. Focus on the things that let your skills shine!

We will have a look at the following aspects:

- Correctness: does your implementation work?
- Performance: does your implementation significantly speed up the process? How fast is the process now?
- Maintainability: does your code include the necessary best practices to make it easy for a team to build on top of it? Have you fixed most of the issues with our implementation?
- Code style: how easy is it to read and comprehend your code? Are you following the language's code style (e.g. PEP8 for Python)?
- Devexp: how easy & automated is it to bootstrap the project?

Those aspects are **critical** to us:

- Writing skills: make sure to proofread yourself and remove all typos, orthographical mistakes, etc.
- Important technical tradeoffs need to be justified.

## Our tips

If you're using Python:

- Consider using poetry to handle dependencies
- Consider using a linter (e.g. flake8) and an autoformatter (e.g. black)

## Need help?

Any question? Reach out to us! We'd love to help you!

🚀  Good luck & happy coding!