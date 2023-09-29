Accounts and roles
==================

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
----------------- 

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
