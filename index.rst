Canonical Dedicated Snap Store
==============================

A Dedicated Snap Store is a dedicated, private Snap Store which facilitates the publication of private snaps and curation of public snaps for Ubuntu
Core devices associated with the Dedicated Snap Store.   

A Dedicated Snap Store permits the use of privileged snapd interfaces, the hosting of gadget and kernel snaps, while providing a
Dedicated Snap Store namespace for snap registration. It can function in offline environments and allows full control over snaps available to
devices associated with the store.

A Dedicated Snap Store provides an optimised, private, and secure distribution mechanism for software distribution via snap packages. This includes
an extensive permission model which provides control over the confinement rules governing snaps published in the Dedicated Snap Store.

The use cases for a Dedicated Snap Store are broad, from IoT devices in the field to cloud and desktop machines. This includes IoT companies, ODMs &
OEMs, silicon vendors and others.

This documentation provides information on some key concepts and processes specific to your Dedicated Snap Store.

.. important::

   **To see the configuration values for your store**, see the :doc:`Reference <configuration-values>` section.

.. rubric:: :h2:`In this documentation`

.. grid:: 1 1 2 2
   
   .. grid-item:: :doc:`Tutorial <create-ubuntu-core-image>`

      To validate that the store was provisioned correctly, and that you are able to access it, we recommend creating and booting an Ubuntu Core image on amd64.

   .. grid-item:: :doc:`How-to guides <how-to-main>`

      Step-by-step guides covering key operations and common tasks.

.. grid:: 1 1 2 2
   :reverse:

   .. grid-item:: :doc:`Reference <configuration-values>`

      Important information for store configuration.

   .. grid-item:: :doc:`Explanation <explanation-main>`

      Discussion and clarification of key topics, like :doc:`Snap confinement <snap-confinement-snapd-connection>`.

.. note:: For general use of the Dedicated Snap Store, see the `main documentation source <https://ubuntu.com/core/services/guide/iot-app-store-intro>`_.

.. toctree::
   :maxdepth: 1
   :hidden:

   Tutorial <create-ubuntu-core-image>

.. toctree::
   :maxdepth: 2
   :hidden:

   How-to <how-to-main>

.. toctree::
   :maxdepth: 2
   :hidden:

   Reference <configuration-values>

.. toctree::
   :maxdepth: 1
   :hidden:

   Explanation <explanation-main>

Having trouble? We would like to help!
--------------------------------------

* Please submit a `support ticket <https://portal.support.canonical.com>`_ for additional support.

