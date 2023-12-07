:orphan:

Brand Store Documentation
=========================

Forked off the `Canonical Sphinx Docs Starter Pack <https://github.com/canonical/sphinx-docs-starter-pack>`_.

.. list-table:: Active RTD projects
    :header-rows: 1

    * - Store
      - Admin link
      - Docs link
    * - Template
      - `Admin <https://readthedocs.com/projects/canonical-canonical-brand-store/>`_
      - `Docs <https://canonical-canonical-brand-store.readthedocs-hosted.com/en/latest/>`_
    * - Acme: Alpha
      - `Admin <https://readthedocs.com/projects/canonical-brand-store-acme-alpha/>`_
      - `Docs <https://canonical-brand-store-acme-alpha.readthedocs-hosted.com/en/latest/>`_
    * - Canonical: Alliances Demo
      - `Admin <https://readthedocs.com/projects/canonical-canonical-alliances-demo-brand-store/>`_
      - `Docs <https://canonical-canonical-alliances-demo-brand-store.readthedocs-hosted.com/en/latest/>`_

For more brand store details see:
  * Store management for super-admins
  * Brand Store Customers
  * Admin dashboard
  * ...these links are only available to brand store admins

Getting started
---------------

There are make targets defined in the ``Makefile`` that do various things. To
get started, we will:

* install prerequisite software
* view the documentation

Install prerequisite software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To install the prerequisites:

.. code-block:: none

   make install

This will create a virtual environment (``.sphinx/venv``) and install
dependency software (``.sphinx/requirements.txt``) within it.

A complete set of pinned, known-working dependencies is included in
``.sphinx/pinned-requirements.txt``.

View the documentation
~~~~~~~~~~~~~~~~~~~~~~

To view the documentation:

.. code-block:: none

   make run

This will do several things:

* activate the virtual environment
* build the documentation
* serve the documentation on **127.0.0.1:8000**
* rebuild the documentation each time a file is saved
* send a reload page signal to the browser when the documentation is rebuilt

The ``run`` target is therefore very convenient when preparing to submit a
change to the documentation.

Submit your change
~~~~~~~~~~~~~~~~~~

Prior to submitting your change, it is recommended to do a fresh build in order
to surface any errors that may cause build issues on the RTD side:

.. code-block:: none

   make clean-doc
   make html

Configure the documentation
---------------------------

You must modify some of the default configuration to suit your project.
To simplify keeping your documentation in sync with the starter pack, all custom configuration is located in the ``custom_conf.py`` file.
You should never modify the common ``conf.py`` file.

Go through all settings in the ``Project information`` section of the ``custom_conf.py`` file and update them for your project.

See the following sections for further customisation.

Configure the header
~~~~~~~~~~~~~~~~~~~~

By default, the header contains your product tag, product name (taken from the ``project`` setting in the ``custom_conf.py`` file), a link to your product page, and a drop-down menu for "More resources" that contains links to Discourse and GitHub.

You can change any of those links or add further links to the "More resources" drop-down by editing the ``.sphinx/_templates/header.html`` file.
For example, you might want to add links to announcements, tutorials, getting started guides, or videos that are not part of the documentation.

Configure the spelling check
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If your documentation uses US English instead of UK English, change this in the
``.sphinx/spellingcheck.yaml`` file.

To add exceptions for words the spelling check marks as wrong even though they are correct, edit the ``.wordlist.txt`` file.

Configure the link check
~~~~~~~~~~~~~~~~~~~~~~~~

If you have links in the documentation that you don't want to be checked (for
example, because they are local links or give random errors even though they
work), you can add them to the ``linkcheck_ignore`` variable in the ``custom_conf.py`` file.

Activate/deactivate feedback button
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A feedback button is included by default, which appears at the top of each page
in the documentation. It redirects users to your GitHub issues page, and
populates an issue for them with details of the page they were on when they
clicked the button.

If your project does not use GitHub issues, set the ``github_issues`` variable
in the ``custom_conf.py`` file to an empty value to disable both the feedback button
and the issue link in the footer.
If you want to deactivate only the feedback button, but keep the link in the
footer, set ``disable_feedback_button`` in the ``custom_conf.py`` file to ``True``.

Add redirects
~~~~~~~~~~~~~

You can add redirects to make sure existing links and bookmarks continue working when you move files around.
To do so, specify the old and new paths in the ``redirects`` setting of the ``custom_conf.py`` file.

Add custom configuration
~~~~~~~~~~~~~~~~~~~~~~~~

To add custom configurations for your project, see the ``Additions to default configuration`` and ``Additional configuration`` sections in the ``custom_conf.py`` file.
These can be used to extend or override the common configuration, or to define additional configuration that is not covered by the common ``conf.py`` file.

Change log
----------

See the `change log <https://github.com/canonical/sphinx-docs-starter-pack/wiki/Change-log>`_ for a list of relevant changes to the starter pack.
