Store Architecture
==================

A Snap Store is a repository for hosting and publishing snaps so that they can be consumed by snapd-enabled devices.

There are several Snap Store instances that will be relevant to you. To understand these instances, and the relationship between them, please read:

- `Snap Store vs Brand Store <https://ubuntu.com/core/services/guide/snap-store-vs-iot-app-store>`_
- `Base Stores and Device View Stores <https://ubuntu.com/core/services/guide/base-stores-and-device-view-stores>`_

Your Base Snap Store is:  ``<CUSTOMER-STORE-NAME>`` (``<CUSTOMER-STORE-ID>``)

Your Device View Snap Store is: ``<CUSTOMER-DEVICEVIEW-NAME>`` (``<CUSTOMER-DEVICEVIEW-ID>``) 

Your Device View Store is configured:

- to automatically include all snaps from ``<STORES-WITH-WHOLESALE-INCLUSION>``
- to include a specific set of snaps from ``<STORES-WITH-CURATED-INCLUSION>``

All stores (including your Device View Snap Store) always include the snapd snap, as well as the LTS-versioned Core snaps (i.e. core18, core20, core22).

.. note::
   If and when your organisation decides to create additional models, please ensure that you first request and use a new Device View Store for each new model. This can be done by opening a support ticket via your support portal. Using a single Device View Store per model allows for better isolation between your various models and ensures that potential changes to the inclusion rules for one model don't impact other models which may already be in use in production.