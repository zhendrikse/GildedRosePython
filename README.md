# Goal

Teach / show people how to refactor legacy code, but before they even begin, how to take a snapshot of the current situation first using approval testing. The example used here is based on the well-known [Gilded Rose kata by Emily Bache](https://github.com/emilybache/GildedRose-Refactoring-Kata), but then in the updated version of [Gil Gonçalves](https://github.com/LuRsT/gilded_rose_kata).

## Approval tests and coverage reports

By default, approval tests are run, coverage reports are generated and served via an HTTP server, that is equipped with a hot reload. So no further manual actions are needed but a press on the run button.

## Branches

Currently, there are three branches:

1. The master branch, where you can start the kata
2. The approvals branch, where approval tests have been added
3. The polymorphism_breakpoint branch, where the refactoring up to polymorphism has been carried out
4. the polymorphism_done branch, where the refactoring using polymorphism has been completed

## References

- [Approval tests in Python](https://github.com/approvals/approvaltests.Python)
- [Emily Bache's version of the Gilded Rose](https://github.com/emilybache/GildedRose-Refactoring-Kata)
- [The updated version to Python 3 of Emily's version](https://github.com/LuRsT/gilded_rose_kata)
- [Run webserver locally](https://gist.github.com/willurd/5720255)