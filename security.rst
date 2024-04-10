Brand Store Security
====================

Brand Stores are designed to allow the secure distribution of software defined as snaps. To facilitate this distribution, a Brand Store requires a few key pieces of information which are stored in different locations depending on the intended use of the information. This document exists to outline the various secrets which must be carefully handled to secure a Brand Store, where those secrets live, and how they must be handled.

Secrets required for a functioning Brand Store
----------------------------------------------

- Brand account credentials
  
  - Grants roles and privileges to the dedicated Snap Store, and is itself derived from a nominated `Ubuntu One SSO account <https://ubuntu.com/core/services/guide/ubuntu-sso-accounts>`_.
  - It is **strongly recommended** that the Ubuntu SSO account is used only for Brand activities and that its use is strictly limited and controlled. It is recommended that the Brand account is only assigned the “Publisher” role.
- Signing keys
  
  - Used to sign `assertions <https://ubuntu.com/core/docs/reference/assertions>`_, which are digitally signed documents used for authentication and authorisation throughout the snap ecosystem.
  - It is **recommended** to use a separate signing key for each type of assertion.
  - It is **strongly recommended** to use `role-scoped keys <https://ubuntu.com/core/services/guide/signing-keys#heading--key-roles>`_, which are limited to signing only specific assertion types and optionally only specific models.
- Other account credentials
  
  - Allows the use of roles to delegate control over various aspects of the snap lifecycle to specific Ubuntu One SSO accounts. For example, an account with the Reviewer role has the ability to review new snap uploads before they can be published, but does not have the ability to publish snaps. Each SSO account can have multiple roles associated with it.

Location of secrets
-------------------

Stored by Canonical
*******************

- Signing keys

Stored by you
*************

- Brand account credentials
- Other account credentials

How secrets are handled
-----------------------

By Canonical
************

- Canonical stores signing keys encrypted in the `Serial Vault <https://ubuntu.com/core/services/guide/serial-vault-overview>`_. No method is provided for downloading the private keys once uploaded.

By you
******

- Account credentials should be stored and transmitted in a secure manner, for example by using a shared credential manager. Access to account credentials should only by given to individuals on an "as-needed" basis, and account credentials should be rotated regularly.
