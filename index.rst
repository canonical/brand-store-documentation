Canonical Brand Store
=====================


A Brand Store is a dedicated, private Snap Store which facilitates the publication of private snaps and curation of public snaps for Ubuntu
Core devices associated with the Brand Store.   

A Brand Store permits the use of hardware / privileged snapd interfaces, and the hosting of gadget and kernel snaps, in addition to providing a
Brand Store namespace for snap registration. It can function in offline environments, and allows full control over snaps available to
devices associated with the store.

A Brand Store provides an optimised, private, and secure distribution mechanism for software distribution via snap packages. This includes
an extensive permission model which provides control over the confinement rules governing snaps published in the Brand Store.

The use cases for a Brand Store are broad, from IoT devices in the field to cloud and desktop machines. This includes IoT companies, ODMs &
OEMs, silicon vendors and others.

This documentation provides links to some key pages, and provides information on some key concepts and processes specific to your Brand Store.


In this documentation
---------------------

.. grid:: 1 1 2 2
   
   .. grid-item:: :doc:`Tutorial <create-ubuntu-core-22-image>`

      Create an Ubuntu Core 22 image to better understand how to build snaps for use within your Brand Store environment.

   .. grid-item:: :doc:`How-to guides <controlling-updates>`

      How to control updates on your devices.

.. grid:: 1 1 2 2
   :reverse:

   .. grid-item:: :doc:`Reference <configuration-values>`

      Important information for store configuration.

   .. grid-item:: :doc:`Explanation <snap-confinement-snapd-connection>`

      Discussion and clarification of key topics, like `Snap confinement <snap-confinement-snapd-connection>`_.


.. toctree::
   :maxdepth: 1
   :hidden:

   Tutorial <create-ubuntu-core-22-image>

.. toctree::
   :maxdepth: 1
   :hidden:

   How-to <controlling-updates>

.. toctree::
   :maxdepth: 1
   :hidden:

   Explanation <snap-confinement-snapd-connection>

.. toctree::
   :maxdepth: 2
   :hidden:

   Reference <configuration-values>

.. note:: For general use of the Brand Store, see the `main documentation source <https://ubuntu.com/core/services/guide/iot-app-store-intro>`_.

Having trouble? We would like to help!
--------------------------------------

* Please submit a `support ticket <https://portal.support.canonical.com>`_ for additional support.

