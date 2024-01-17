Brand store configuration values
================================

Store Architecture
------------------

A Snap Store is a repository for hosting and publishing snaps so that they can be consumed by snapd-enabled devices.

There are several Snap Store instances that will be relevant to you. To understand these instances, and the relationship between them, please read:

- `Snap Store vs Brand Store <https://ubuntu.com/core/services/guide/snap-store-vs-iot-app-store>`_
- `Base Stores and Device View Stores <https://ubuntu.com/core/services/guide/base-stores-and-device-view-stores>`_

Your Base Snap Store is:  ``{{CUSTOMER_STORE_NAME}}`` (``{{CUSTOMER_STORE_ID}}``)

Your Device View Snap Store is: ``{{CUSTOMER_DEVICEVIEW_NAME}}`` (``{{CUSTOMER_DEVICEVIEW_ID}}``)

Your Device View Store is configured:

- to automatically include all snaps from ``{{STORES_WITH_WHOLESALE_INCLUSION}}``
- to include a specific set of snaps from ``{{STORES_WITH_CURATED_INCLUSION}}``

All stores (including your Device View Snap Store) always include the snapd snap, as well as the LTS-versioned Core snaps (i.e. core18, core20, core22).

.. note::

   If and when your organisation decides to create additional models, please ensure that you first request and use a new Device View Store for each new model. This can be done by opening a support ticket via your support portal. Using a single Device View Store per model allows for better isolation between your various models and ensures that potential changes to the inclusion rules for one model don't impact other models which may already be in use in production.

Controlling updates
------------------

One important consideration when deploying devices running Ubuntu Core is determining a method to control updates, in particular when those updates are for snaps from other publishers (e.g. Canonical). There are three general approaches to controlling and/or gating snap updates on Ubuntu Core:

  * `Refresh Control https://ubuntu.com/core/docs/refresh-control`_ - this method provides a way to hold one or more snaps at specific revisions until newer revisions have first been validated by the brand. It can be enabled by opening a support ticket and requires a special gating snap which much be included in your images.
  * `Validation Sets https://snapcraft.io/docs/validation-sets`_ - this method provides a similar mechnism to Refresh Control, however it's based on a special type of assertion called a validation-set. These assertions can be added at runtime to Ubuntu Core devices or seeded at image creation time by specififying one or more validation-set assertions in your model assertion. One advantage of validation sets vs. Refresh Control is that they allow a set of inter-related snaps to be validated as a set vs. validating snaps one by one.
  * **Device Agent** - the final method that can be used to control updates involves use of a device agent, which is a dedicated service that takes full control of updates on an Ubuntu Core system by use of snapd's REST API. For more details, please see the `snapd-control interface https://snapcraft.io/docs/snapd-control-interface`

**Note** - while Refresh Control is still supported, Validation Sets provide a more comprehensive approach to controlling updates, and in particular can guarantee that only specific combinations of snap revisions can be installed together.

   Accounts and roles
------------------

Ubuntu SSO accounts underpin developer interactions with the various Stores. To understand accounts and roles, please read:

* `Ubuntu SSO Accounts <https://ubuntu.com/core/services/guide/ubuntu-sso-accounts>`__
* Users and Roles:
    * `Administrator <https://ubuntu.com/core/services/guide/administrator-role>`__
    * `Reviewer <https://ubuntu.com/core/services/guide/reviewer-role>`__
    * `Viewer <https://ubuntu.com/core/services/guide/viewer-role>`__
    * `Publisher <https://ubuntu.com/core/services/guide/publisher-role>`__
    * `Collaborator <https://ubuntu.com/core/services/guide/collaborator-role>`__
* `Setting up Account Roles <https://ubuntu.com/core/services/guide/setting-up-account-roles>`__

Your store has been provisioned with the following data:

.. list-table::
   :widths: 20 40 40
   :header-rows: 1
   :stub-columns: 1

   * -
     - Base Store
     - Device view Store
   * - Store Name
     - {{CUSTOMER_STORE_NAME}}
     - {{CUSTOMER_DEVICEVIEW_NAME}}
   * - Store ID
     - {{CUSTOMER_STORE_ID}}
     - {{CUSTOMER_DEVICEVIEW_ID}}
   * - Admin(s)
     - {{CUSTOMER_ADMIN_EMAIL}}
     - {{CUSTOMER_ADMIN_EMAIL}}
   * - Publisher(s)
     - {{CUSTOMER_BRAND_EMAIL}}
     - (none)
   * - Reviewer(s)
     - {{CUSTOMER_ADMIN_EMAIL}}
     - (none)
   * - Viewer(s)
     - {{CUSTOMER_VIEWER_EMAIL}}
     - {{CUSTOMER_VIEWER_EMAIL}}

The Admin role can be used to grant these roles to other accounts, as well.

Brand Account
-------------

Account: ``{{CUSTOMER_BRAND_EMAIL}}`` (account-id: ``{{CUSTOMER_BRAND_ACCOUNT_ID}}``)

The Brand account was set for your Brand Stores at the time of store creation.  The Brand account defines the Brand scope of authority, and it must be used for certain functions.

The Brand account:

- Generates, registers and holds the signing keys for the Brand infrastructure.
- Signs Model assertions used to build images that point at Brand Stores.
- Signs System-User assertions used to trigger user-account creation on Brand devices.
- Publishes any gadget snaps in the store. Kernel and gadget snap names must be owned by the Brand account or by Canonical. Typically, Canonical owns kernels, and the Brand account owns gadget snaps. To do this, the Brand account must be given the **Publisher** role in the Base store.

  * After registering the names, the Brand account may make other developer accounts **Collaborators** on these snaps. These accounts then may upload future revisions of these snaps.

.. note::

  Use of the Brand account and its credentials should be strictly limited. Canonical recommends that the Brand account not be assigned any roles that are not strictly needed. The Brand account will need the **Publisher** role, but do not make the Brand account a store **Administrator**, **Reviewer**, or **Viewer**.

Serial Vault
------------

To get started with the `Serial Vault <https://serial-vault-admin.canonical.com/>`_ (SV admin account required), read the following pages. You can click the next button in the bottom right corner to move from one to the next.

- `Serial Vault Overview <https://ubuntu.com/core/services/guide/serial-vault-overview>`_
- `Signing Keys <https://ubuntu.com/core/services/guide/signing-keys>`_
- `Device Model and Identity <https://ubuntu.com/core/services/guide/device-model-and-identity>`_

The ``{{CUSTOMER_ADMIN_EMAIL}}`` account was also added to the Serial Vault, allowing this account to log into the Serial Vault for administrative purposes, including making configurations required for device authentication against a Brand Store, as described below. To configure your serial vault, follow the instructions at the links below, using ``{{CUSTOMER_MODEL_NAME}}`` as the model name, ``{{CUSTOMER_BRAND_EMAIL}}`` as the brand email, and ``{{CUSTOMER_BRAND_ACCOUNT_ID}}`` as the brand ID:

- `Environment Setup <https://ubuntu.com/core/services/guide/environment-setup>`_
- `Generate a Serial Signing Key <https://ubuntu.com/core/services/guide/generate-a-serial-signing-key>`_
- `Import a Serial Signing Key <https://ubuntu.com/core/services/guide/import-a-serial-signing-key>`_
- `Register a New Device Model Name <https://ubuntu.com/core/services/guide/register-a-new-device-model-name>`_
- `Generate a Model Signing Key <https://ubuntu.com/core/services/guide/generate-a-model-signing-key>`_
- `Check the Signing Log <https://ubuntu.com/core/services/guide/check-the-signing-log>`_
