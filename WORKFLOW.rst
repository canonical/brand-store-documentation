Workflow
********

Generating documentation locally
================================

Documentation can be generated locally using the template files. Simply set the ``TEMPLATE`` variable when calling ``make``. For example, to create a PDF of the ``acme-alpha`` template use the following command:

.. code-block:: none

    make pdf TEMPLATE="templates/acme-alpha.yaml"

.. note::

    Local generation of PDF files requires some system packages. You will be prompted to use ``make pdf-prep-force`` to install the required packages if they are not found on your system.


For new customers
=================

Setting up the Brand Store documentation for a new customer involves the Store team creating and configuring a new project on ReadTheDocs and Field Engineering filling in a template containing customer-specific values.

Store Team
----------

These instructions assume that you have the proper permissions under the GitHub and ReadTheDocs projects.

1. Create a new project on Read The Docs under the Canonical organization.
#. Go to https://readthedocs.com/organizations/canonical/, click the project, click the "Admin" tab.
#. Change the "Repository URL" to ``git@github.com:canonical/brand-store-documentation.git`` and click "Save".
#. Click on "Environment Variables", click on "Add Environment Variable"; fill in "Name" with ``TEMPLATE_FILENAME``, value with ``templates/<template-filename>``, and click "Save".

   - The template filename can really be anything unique, but ideally is of the form ``company-brand.yaml``. For example, the example Acme company has a brand named Alpha and so the template filename is ``acme-alpha.yaml``.

#. Click on "SSH Keys", click the displayed key, and add the public key to the https://github.com/canonical/brand-store-documentation GitHub repository; the key only requires Read permissions.
#. Click on "Integrations", click on "GitHub incoming webhook", click "Resync webhook"
#. Create a new file under the ``templates/`` directory in the ``canonical/brand-store-documentation`` repository with a filename that matches the filename used above.

Field Engineering
-----------------

These instructions assume that you have the proper permissions under the GitHub project.

1. Fill in the values in ``templates/<template-filename>`` with the correct values for the brand that is being created.

Updating existing documentation
===============================

Updating existing documentation for Brand Store customers requires editing the reStructuredText source code in the GitHub repository and then downloading the generated PDF from ReadTheDocs. It is assumed that only Field Engineering will be making documentation updates, and so documentation for the Store team is not explicitly provided. If necessary, a Store team member can follow the Field Engineering steps listed below.

Field Engineering
-----------------

1. On the webpage corresponding to the part of the documentation you wish to edit, scroll to the bottom and click "Edit this page on GitHub". Alternatively, clone the repository from GitHub, make the changes, and manually create a pull request.
#. Make the necessary changes.
#. Submit a PR with the changes.
#. A few automated checks will run for the PR. Once those checks complete, and assuming the changes can be cleanly merged, click on the "Merge" button to merge the pull request.
#. Wait for the documentation to rebuild.
#. Go to the generated PDF document located at ``https://canonical-<readthedocs-project-name>.readthedocs-hosted.com/_/downloads/en/latest/pdf/`` and download the PDF.

   - Downloading the generated PDFs is currently a manual process which must be done for each brand store customer when the documentation is updated.

Creating a new documentation page
=================================

To create a new documentation page, create a new ``*.rst`` document in the root directory of the Git repository and add the new document to the ``toctree`` at https://github.com/canonical/brand-store-documentation/blob/main/index.rst.

Adding a new template variable
==============================

New template variables can be created by adding the variable and its default value to ``templates/TEMPLATE.yaml``. For example, to add a ``CUSTOMER_TITLE`` variable to a page, first add a new line to ``TEMPLATE.yaml``: ``CUSTOMER_TITLE: "NULL"``.

Then, add a new line to any templates corresponding to Brand Stores that require the new variable with the desired value (for example, ``CUSTOMER_TITLE: "Dr."``). The variable can then be used in the corresponding document like any other variable (by wrapping the variable in ``{{}}``)
