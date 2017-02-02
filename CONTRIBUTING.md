If you're looking to contribute to the development of **HiRezPy**, this document will be useful for you. It's fairly short, but contains all the information you need to make a satisfactory pull request and/or issue.

## Guidelines
* **We will not accept** PRs or issues regarding code cleanups or cosmetic changes, unless the changes will make the library faster. HiRezPy may not entirely follow, for example, [PEP 8](https://www.python.org/dev/peps/pep-0008/). This is a delibrate design choice and therefore PRs regarding it won't be accepted.
* It would be helpful if the **base branch** for your PRs was the `dev` branch. This gives us less work, and allows you to ensure that what you're proposing isn't already implemented in the in-development version of the library.
* When making PRs, your additions or changes should contribute towards the helpfulness of the library. We won't add random things, like a call to a different API.
* If your PR is to fix an issue, please tag it in your submission. If you would like to improve an existing PR, please try using GitHub's [review system](https://help.github.com/articles/reviewing-proposed-changes-in-a-pull-request/) to let the proposee know of changes they could make. If they are unresponsive, or the PR has been inactive for a while, feel free to make a new PR in place of it.
* **Please test your code.**
    * You should test any changes against: **Python 3.5, 3.6** to ensure they work as intended.
    * You can use `virtualenv`, [documented here](http://docs.python-guide.org/en/latest/dev/virtualenvs/), to test your changes in different versions.

If you do create an issue or pull request, then cheers! Thanks for contributing towards the repo in some shape/form. Open-source contributions are what keeps projects like this active and current.
