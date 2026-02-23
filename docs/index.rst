.. meta::
    :description: Documentation for the Canonical Dedicated Snap Store using the Diátaxis framework, covering tutorials, how-to guides, reference materials, and explanations for managing private snap repositories.

Dedicated Snap Store
====================

.. include:: home.rst
   :start-after: landing-page-start
   :end-before: landing-page-end

.. important::

   **To see the configuration values for your store**, see the :doc:`Reference
   <reference/configuration-values>` section.

.. rubric:: :h2:`In this documentation`

.. list-table:: 
   :header-rows: 0
   :widths: 25 75

   * - Getting Started
     - :doc:`Tutorial: Create an Ubuntu Core image <tutorial/create-ubuntu-core-image>` •
       :doc:`How-to: Configure Serial Vault <how-to/configure-serial-vault>` •
       :doc:`Reference: Configuration values <reference/configuration-values>`
   * - Security and Access Control
     - :doc:`Explanation: Dedicated Snap Store security <explanation/security>` •
       :doc:`How-to: Setting up account roles <how-to/setting-up-account-roles>` •
       :doc:`Explanation: Brand accounts <explanation/brand-accounts>`
   * - Software controls
     - :doc:`Explanation: Connecting devices <explanation/connecting-devices>` •
       :doc:`Explanation: Controlling updates <explanation/controlling-updates>` •
       :doc:`Explanation: Snapd interface connections <explanation/snapd-interface-connections>`
   * - Architecture & Concepts
     - :doc:`Explanation: Base Stores and Device View Stores <explanation/base-stores-and-device-view-stores>`
       :doc:`Explanation: Brand accounts <explanation/brand-accounts>` •

.. toctree::
   :maxdepth: 1
   :hidden:

   Tutorial <tutorial/create-ubuntu-core-image>

.. toctree::
   :maxdepth: 2
   :hidden:

   How-to <how-to>   

.. toctree::
   :maxdepth: 2
   :hidden:

   Reference <reference/configuration-values>

.. toctree::
   :maxdepth: 1
   :hidden:

   Explanation <explanation>

.. rubric:: :h2:`How this documentation is organised`

This documentation uses the `Diátaxis documentation structure <https://diataxis.fr/>`_.

* The :doc:`tutorial <tutorial/create-ubuntu-core-image>` provides a step-by-step walkthrough to help you get started.
* :doc:`How-to guides <how-to>` offer practical guides for specific tasks related to managing your Dedicated Snap Store.
* The :doc:`reference section <reference/configuration-values>` contains detailed information about configuration values and store settings.
* :doc:`Explanation <explanation>` gives context and background to help you understand the Dedicated Snap Store concepts and architecture.


Project and community
---------------------

The Dedicated Snap Store is a member of the Store family. It's a project that welcomes suggestions, fixes and constructive feedback.

* `Join the Discourse forum <https://forum.snapcraft.io/c/store/16>`_
* `File a bug <https://bugs.launchpad.net/snapstore-server>`_

Having trouble? We would like to help!
--------------------------------------

* Please submit a `support ticket <https://portal.support.canonical.com>`_ for
  additional support.


.. raw:: html

   <h1>Dynamic Greeting</h1>

   <form id="url-form" method="GET">
      <input type="text" name="username" placeholder="Enter your name..." required>
      <button type="submit">Update Page</button>
   </form>

   <hr>

   <div id="output-area">
      <p>Hello, <span id="display-name">Guest</span>!</p>
   </div>

   <script>
      // 1. Grab the URL parameters
      const urlParams = new URLSearchParams(window.location.search);
      const userName = urlParams.get('username');

      // 2. If the 'username' parameter exists, update the DOM
      if (userName) {
         document.getElementById('display-name').innerText = userName;
      }
   </script>


Test
----

.. url-form::

   name: Your name
   host: Your host name

Results
-------

Hello :url:`name`! Your job is :url:`job`.

.. parsed-literal::

   What about :url:`name` in regular text?

.. code::

   What about :url:`name` in code?

.. terminal::

   echo "Hello {{name}} Your job is {{job}}."


