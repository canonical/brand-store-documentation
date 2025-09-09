Control updates
===============

One important consideration when deploying devices running Ubuntu Core is
determining how to control updates, in particular when those updates are for
snaps from other publishers (e.g. Canonical). There are two general approaches
to controlling snap updates on Ubuntu Core:

* `Validation Sets <https://snapcraft.io/docs/validation-sets>`_
   This method uses `validation-set assertions <https://documentation.ubuntu.com/core/reference/assertions/validation-set/>`_.
   These assertions can be added at runtime to Ubuntu Core devices or seeded at image
   creation time by specifying one or more validation-set assertions in your
   `model assertion <https://documentation.ubuntu.com/core/reference/assertions/model/>`_.
   Validation sets allow a set of interrelated snaps to be validated as a set
   vs. validating snaps one by one.

* **Device Agent**
   This method involves use of a device agent, which is a dedicated service that
   takes full control of updates on an Ubuntu Core system by use of snapd's
   `REST API <https://snapcraft.io/docs/snapd-api>`_.
   For more details, see the `snapd-control interface <https://snapcraft.io/docs/snapd-control-interface>`_.
   You may either create your own custom device agent (or use another one
   available in a store), or use :ref:`Landscape <landscape>` to fulfill the
   device management role.
