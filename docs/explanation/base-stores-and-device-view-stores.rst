Base stores and Device View stores
==================================

A Dedicated Snap Store is the union of a base store and at least one device
view store. The Base store is where the collection of snaps reside, whereas the
Device View stores are curated windows into a specific Base store.

.. _base-stores:

Base stores
-----------

A Base store is the store to which every snap name should be registered
and published through. This store is the primary point of interaction between
developers and the Dedicated Snap Store infrastructure. All snap names and
revisions flow through the Base store.

In this way, the Base store can be thought of as a centralized location for
specific applications, through which various Device View stores are allowed to
filter through to curate a proper collection of device- or function-specific
software.

.. _device-view-stores:

Device View stores
------------------

A Device View store is the store which a specific device model is able to
view a curated collection of snaps picked from a collection of Base stores,
including the Brand Base store, the Global store, or even other Brand Base
stores.

A device model is specifically related to the name associated with any
particular model assertion one may use to generate Ubuntu Core images, which
should always point at a corresponding Device View store.

Important facts
---------------

Devices should be thought of as particular 'classes'. This means that if a
device does a specific function, it is a unique category; devices which fulfill
other needs fit into a different category. As such, each class of device
should have its own Device View store, which serves snaps from the Base store
corresponding to that class' particular function. This ensures a logical
separation in the kind of software which can be installed to any particular
device, corresponding to its given model assertion model name.

Regardless of the kind of store, they are all private to a collection of
Ubuntu One SSO accounts which have specifically been given access to them. For
instance, only an account which has been given the Viewer role for a Device View
or Base store can see the snaps available in that store.

.. image:: /images/store-architecture.png
   :alt: Illustration of the App Store architecture, demonstrating use of a combination of public and private snaps

*A standard store configuration using a Base and Device store*

.. TODO: Serial Vault going the way of the dinosaurs; replace with Model Service language.

Snap stores are represented by the cylinders, with the Device View store is
represented by the cylinder with Acme in the top-right. Acme \_view store 1\_
has been configured to include snaps from the Global snap store and the `Serial Vault <https://canonical-serial-vault.readthedocs-hosted.com/>`_
is used by the company’s devices to authenticate and thereby gain access to
private snaps.
