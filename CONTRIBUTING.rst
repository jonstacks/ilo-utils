============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/jonstacks13/ilo-utils/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug"
is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "feature"
is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

ilo-utils could always use more documentation, whether as part of the
official ilo-utils docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at http://github.com/jonstack13/ilo-utils/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `ilo-utils` for local development.

1. Fork the `ilo-utils` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/ilo-utils.git

3. Install your local copy into a virtualenv. Assuming you have virtualenvwrapper installed, this is how you set up your fork for local development::

    $ mkvirtualenv ilo-utils
    $ cd ilo-utils/
    $ python setup.py develop

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass flake8 and the tests::

    $ make lint
    $ make test

   To get flake8 and tox, just pip install them into your virtualenv.

6. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the GitHub website.

8. Once your pull request is approved, update our GitHub hosted documentation!

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.

Updating GitHub hosted documentation
------------------------------------

After your pull request is merged into master and you have deleted your old
featurebranch, please be sure to update the documentation that we host with
the ``gh-pages`` branch. This will allow those reading the documentation to be
aware of your changes and make use of your brand new features :)

Here are the basic steps that I use to update the ``gh-pages`` branch:

1. With the master branch checked out, run the `make docs` command from the
   project root. This will build all of the html documentation that we need
   and save it in: ``_build/html``.

2. Copy the ``html`` folder to another location temporarily.
3. Checkout the ``gh-pages`` branch: ``git checkout gh-pages``
4. Copy the contents of the ``html`` folder into the project directory. This
   will update any ``.html`` files that were changed or add new ones.
5. Go ahead and git add the files that were added or changed. Make sure to not
   add files that are not relevant to the documentation.
6. Commit your changes and push to origin.
