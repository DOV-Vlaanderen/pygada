.. _dev-guidelines:

Development guidelines
-----------------------

Coding guidelines
^^^^^^^^^^^^^^^^^^

The following are some guidelines on how new code should be written. Of course, there are special cases and there
will be exceptions to these rules. However, following these rules when submitting new code makes the review easier so new
code can be integrated in less time.

Uniformly formatted code makes it easier to share code ownership. The
pygada project tries to closely follow the official Python guidelines
detailed in `PEP8 <https://www.python.org/dev/peps/pep-0008/>`_ which detail
how code should be formatted and indented. Please read it and follow it.

In addition, we add the following guidelines:

* Use underscores to separate words in non class names: ``n_samples`` rather than ``nsamples``.
* Avoid multiple statements on one line. Prefer a line return after a control flow statement (\ ``if/for``\ ).
* Please don't use ``import *`` in any case. It is considered harmful by the official Python recommendations. It makes the code harder to read as the origin of symbols is no longer explicitly referenced, but most important, it prevents using a static analysis tool like pyflakes to automatically find bugs.
* Use the `numpy docstring standard`_ in all your docstrings.
* The attributes for specific classes are Pandas data.frames, please use lowercase names (eventually with `_`) as column names.

Contributing workflow
^^^^^^^^^^^^^^^^^^^^^

The preferred workflow for contributing is to fork the `main repository <https://github.com/DOV-Vlaanderen/pygada>`_ on
GitHub, clone locally, and develop on a branch. For more information on this workflow,
see the `github workflow <https://guides.github.com/introduction/flow/>`_.

The workflow is provided for command line usage and using the `Github for Desktop <https://desktop.github.com/>`_
application. Feel free to use the environment you like the most.

#.
   Fork the `project repository <https://github.com/DOV-Vlaanderen/pygada>`_ by clicking on the 'Fork' button near the top right of the page. This creates a copy of the code under your personal GitHub user account.


   .. image:: https://github-images.s3.amazonaws.com/help/bootcamp/Bootcamp-Fork.png
      :target: https://github-images.s3.amazonaws.com/help/bootcamp/Bootcamp-Fork.png
      :alt: forkrepo
      :height: 100px

#.
   You’ve successfully forked the pygada repository, but so far, it only exists on GitHub. To be able to work on the project, you will need to clone it to your computer.

    Clone your fork of the pygada repo from your GitHub account to your local disk:

   .. code-block:: bash

       $ git clone https://github.com/DOV-Vlaanderen/pygada.git
       $ cd pygada

   If you’re using the GitHub for Desktop application, navigate over to the bottom on the right hand side bar and click ``Open with GitHub Desktop``. Once you've clicked this, it’ll ask you if you want to launch the desktop application to clone the repository, and where you want to save it. Pick a location on your computer that you feel comfortable with creating files and folders.


   .. image:: https://docs.github.com/assets/cb-88692/mw-1000/images/help/repository/open-with-desktop.webp
      :target: https://docs.github.com/assets/cb-88692/mw-1000/images/help/repository/open-with-desktop.webp
      :alt: clonerepo
      :height: 200px


#.
   Create a ``my-feature`` branch (give it the name of the feature you want to develop) to hold your development changes:

   .. code-block:: bash

       $ git checkout -b my-feature

   When using Github for Desktop, in the top left corner of the repository view, create a new branch.


   .. image:: https://desktop.github.com/images/screens/windows/branch.png
      :target: https://desktop.github.com/images/screens/windows/branch.png
      :alt:
      :height: 200px

   Always use a ``my-feature`` branch. It's good practice to **never work on the ``master`` branch**\ !

#. Make sure your development environment is setup to have all the required tooling available
   (code, unit tests, documentation,...). Follow the development installation instructions :ref:`for package contributors <devinstallation>`
   to setup the tooling.

#.
   Develop the feature on your feature branch. Add changed files using ``git add`` and then ``git commit`` files:

   .. code-block:: bash

       $ git add modified_files
       $ git commit

   which is similar in Github for Desktop, just craft your commit message in the UI.


   .. image:: https://desktop.github.com/images/screens/windows/craft.png
      :target: https://desktop.github.com/images/screens/windows/craft.png
      :alt:
      :height: 200px


   Make sure you split your contribution in small commits with well-describing names. Write unit tests for new features
   and make sure these tests are successful. Have a look at the section on :ref:`unit tests <unittests>` on how to run
   the unit tests. Don't forget to update the documentation pages, see the :ref:`section on sphinx documentation <docs-technical>`.

#.
   Right now, you’ve essentially told Git, “Okay, I’ve taken a snapshot of my changes!” You can continue to make more changes, and take more commit snapshots. When you’re ready to push your changes up to GitHub.com, push the changes to your GitHub account with:

   .. code-block:: bash

       $ git push -u origin my-feature

   or, using the Github for Desktop, click on the **Sync** button, which is right above your list of changes.

#.
   Go to the GitHub web page of your fork of the pygada repo.

    Click the 'Pull request' button to send your changes to the project's maintainers for review. This will send an email to the committers.


   .. image:: https://github-images.s3.amazonaws.com/help/pull_requests/recently_pushed_branch.png
      :target: https://github-images.s3.amazonaws.com/help/pull_requests/recently_pushed_branch.png
      :alt: pullrequestrepo
      :height: 130px


If any of the above seems like magic to you, please look up the `Git documentation <https://git-scm.com/documentation>`_ on the web, or ask a friend or another contributor for help.

Setting up your environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To start developing, make sure to setup a development environment, provided
in the development installation instructions :ref:`for package contributors <devinstallation>`.

.. note::
   The repository contains multiple ``requirements_*.txt`` files:

   * ``requirements.txt`` required packages to use pygada
   * ``requirements_dev.txt`` required packages to run the pygada test suite and contribute to pygada code

   When adding dependencies, make sure to make the appropriate adjustments in the individual file!

.. note::
   The repository contains also an ``environment*.yml`` file, to create the conda environment.

   When adding dependencies, make sure to also adjust this file!

.. _unittests:

Running the unit tests
^^^^^^^^^^^^^^^^^^^^^^^

To run the unit tests, ``pytest`` is used. In the common line, you can run all the tests from the terminal,
using the command line. Navigate to the ``pygada`` main directory and do:

::

   pytest

When adding new functionality or adjusting code, make sure to check/update/add the unit tests. Test files
are grouped by the functionality. Each file name starts with ``test_*`` (required for pytest), followed
by the module name.


.. _docs-technical:

Creating the documentation
^^^^^^^^^^^^^^^^^^^^^^^^^^

We are glad to accept any sort of documentation: function docstrings, reStructuredText
documents, tutorials, etc. Documentation lives in the ``docs/`` directory.

You can edit the documentation using any text editor and then generate the HTML
output by typing ``make html`` from the ``doc/`` directory. For building the
documentation, you will need `Sphinx`_ and `pandoc`_. The ``_build``
directory is not included in the repository as we rely on CI tooling for the
documentation building. The documentation is checked on Travis_ and build
by `Read the docs`_.

.. _Travis: https://travis-ci.org/DOV-Vlaanderen/pygada
.. _Read the docs: https://readthedocs.org/


.. _Travis.ci: https://travis-ci.org/DOV-Vlaanderen/pygada
.. _pypi: https://pypi.org/project/pygada/
.. _packaging instructions: https://packaging.python.org/tutorials/packaging-projects/
.. _numpy docstring standard: https://numpydoc.readthedocs.io/en/latest/format.html
.. _Sphinx: http://www.sphinx-doc.org/en/master/
.. _pandoc: https://pandoc.org/
