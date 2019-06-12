## Contributing

First off, thank you for considering contributing to autosolo-timing. It's people
like you that will make this happen!

### Where do I go from here?

If you've noticed a bug or have a question that doesn't belong on social media, [search the issue tracker][https://github.com/bristolmotorclub/autosolo-timing/issues] to see if
someone else in the community has already created a ticket. If not, go ahead and
[make one][new issue]!

### Fork & create a branch

If this is something you think you can fix, then fork autosolo-timing and
create a branch with a descriptive name.

A good branch name would be (where issue #3 is the ticket you're working on):

```sh
git checkout -b 3-add-1920x1080-layout
```

### Get the test suite running

We don't have a test suite yet.  If you can help with that, then please do!

### Did you find a bug?

* **Ensure the bug was not already reported** by [searching all issues][https://github.com/bristolmotorclub/autosolo-timing/issues].

* If you're unable to find an open issue addressing the problem,
  [open a new one][new issue]. Be sure to include a **title and clear
  description**, as much relevant information as possible, and a **code sample**
  or an **executable test case** demonstrating the expected behavior that is not
  occurring.

### 5. Implement your fix or feature

At this point, you're ready to make your changes! Feel free to ask for help;
everyone is a beginner at first - and that means us, actually :smile_cat:

### 6. View your changes in a browser

autosolo-timing is meant to be used by humans, not cucumbers. So make sure to take
a look at your changes in a browser.

### Get the style right

Your patch should follow the same conventions & pass the same code quality
checks as the rest of the project. We've not implemented anything yet.  Feel free to suggest something...

### Make a Pull Request

At this point, you should switch back to your master branch and make sure it's
up to date with autosolo-timing's master branch:

```sh
git remote add upstream git@github.com:bristolmotorclub/autosolo-timing.git
git checkout master
git pull upstream master
```

Then update your feature branch from your local copy of master, and push it!

```sh
git checkout 3-add-1920x1080-layout
git rebase master
git push --set-upstream origin 3-add-1920x1080-layout
```

Finally, go to GitHub and [make a Pull Request][] :D

### Merging a PR (maintainers only)

A PR can only be merged into master by a maintainer if:

* It has no requested changes.
* It is up to date with current master.

Any maintainer is allowed to merge a PR if all of these conditions are
met.

### Shipping a release (maintainers only)

Maintainers need to do the following to push out a release:

* Make sure all pull requests are in and that changelog is current
* Update `version.rb` file and changelog with new version number

[search the issue tracker]: https://github.com/bristolmotorclub/autosolo-timing/issues?q=something
[new issue]: https://github.com/bristolmotorclub/autosolo-timing/issues/new
[fork autosolo-timing]: https://help.github.com/articles/fork-a-repo
[searching all issues]: https://github.com/bristolmotorclub/autosolo-timing/issues?q=
[make a pull request]: https://help.github.com/articles/creating-a-pull-request
