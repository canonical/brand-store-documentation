Brand store configuration
=========================

When using your Brand Store, your main resource will be the documentation found in the `IoT App Store documentation <https://ubuntu.com/core/services/guide/iot-app-store-intro>`_.
This section provides links to some key pages in the documentation, as well as information specific to your Brand Store.

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

All stores (including your Device View Snap Store) always include the snapd snap, as well as the LTS-versioned Core snaps (i.e. core18, core20, core22, core24).

.. note::

   If and when your organisation decides to create additional models, please ensure that you first request and use a new Device View Store for each new model. This can be done by opening a support ticket via your support portal. Using a single Device View Store per model allows for better isolation between your various models and ensures that potential changes to the inclusion rules for one model don't impact other models which may already be in use in production.

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


Ubuntu Pro & Support Portal Account
-----------------------------------

An Ubuntu Pro account and Support Portal access are also included with your Brand Store. Both are accessed using the SSO account associated with the following email address:

    {{CUSTOMER_PRO_EMAIL}}


Ubuntu Pro Dashboard
********************

Brand Store customers are provided an Ubuntu Pro account to enable access to ESM updates during snap builds. This is accomplished by adding your Pro token to CI/CD systems used to build your snaps. This token can be accessed by signing into the `Ubuntu Pro Dashboard <http://ubuntu.com/pro/dashboard>`_ using the account mentioned at the beginning of this section.

Support Portal
**************

Brand Store customers are also provided access to our Support Portal which can be used to create support cases, including snap interface connection requests. The support portal can be accessed by signing into the `Support Portal Dashboard <https://support-portal.canonical.com/dashboard>`_ using the account mentioned at the beginning of this section. 


Serial Vault
------------

The ``{{CUSTOMER_ADMIN_EMAIL}}`` account was also added to Serial Vault, allowing this account to log into the Serial Vault for administrative purposes, including making configurations required for device authentication against a Brand Store, as described in :doc:`how-to-configure-serial-vault`. 

To get started with the `Serial Vault <https://serial-vault-admin.canonical.com/>`_ (SV admin account required), read the following pages. You can click the next button in the bottom right corner to move from one to the next.

- `Serial Vault Overview <https://ubuntu.com/core/services/guide/serial-vault-overview>`_
- `Signing Keys <https://ubuntu.com/core/services/guide/signing-keys>`_
- `Device Model and Identity <https://ubuntu.com/core/services/guide/device-model-and-identity>`_

.. note::

    Please be sure to review the signing keys sub-section on key roles. Use of key roles is a best practice which helps to limit the scope of what type of assertions each key can be used to sign. This is meant to limit your exposure if a key were to be compromised. Use of key roles also means that you **must no longer register your keys** using ``snapcraft register-key``. This will now be handled by the Snap Store admins as part of the key role assignment. And finally, please note that key roles can only be assigned to new keys, they cannot be added to keys at a later time.

To configure Serial Vault, see :doc:`how-to-configure-serial-vault`.