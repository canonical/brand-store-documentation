Accounts and roles
==================

Ubuntu SSO accounts underpin developer interactions with the various Stores. To understand accounts and roles, please read:

* Ubuntu SSO Accounts
* Users and Roles:
    * Administrator
    * Reviewer
    * Viewer
    * Publisher
    * Collaborator
* Setting up Account Roles

Your store has been provisioned with the following data:

.. list-table::
   :widths: 20 40 40
   :header-rows: 1
   :stub-columns: 1

   * -
     - Base Store
     - Device view Store
   * - Store Name
     - ``<CUSTOMER-STORE-NAME>``
     - ``<CUSTOMER-DEVICEVIEW-NAME>``
   * - Store ID
     - ``<CUSTOMER-STORE-ID>``
     - ``<CUSTOMER-DEVICEVIEW-ID>``
   * - Admin(s)
     - ``<CUSTOMER-ADMIN-EMAIL>``
     - ``<CUSTOMER-ADMIN-EMAIL>``
   * - Publisher(s)
     - ``<CUSTOMER-BRAND-EMAIL>``
     - (none)
   * - Reviewer(s)
     - ``<CUSTOMER-ADMIN-EMAIL>``
     - (none)
   * - Viewer(s)
     - ``<CUSTOMER-VIEWER-EMAIL>``
     - ``<CUSTOMER-VIEWER-EMAIL>``

The Admin role can be used to grant these roles to other accounts, as well.

3.1 Brand Account
----------------- 

Account: ``<CUSTOMER-BRAND-EMAIL> (account-id: <CUSTOMER-BRAND-ACCOUNT-ID>)``

The Brand account was set for your Brand Stores at the time of store creation.  The Brand account defines the Brand scope of authority, and it must be used for certain functions.

The Brand account:

* Generates, registers and holds the signing keys for the Brand infrastructure.
* Signs Model assertions used to build images that point at Brand Stores.
* Signs System-User assertions used to trigger user-account creation on Brand devices.
* Publishes any gadget snaps in the store. Kernel and gadget snap names must be owned by the Brand account or by Canonical. Typically, Canonical owns kernels, and the Brand account owns gadget snaps. To do this, the Brand account must be given the **Publisher** role in the Base store. 
    * After registering the names, the Brand account may make other developer accounts Collaborators on these snaps. These accounts then may upload future revisions of these snaps.

**Note:** Use of the Brand account and its credentials should be strictly limited. Canonical recommends that the Brand account not be assigned any roles that are not strictly needed. The Brand account will need the **Publisher** role, but do not make the Brand account a store **Administrator**, **Reviewer**, or **Viewer**.  

