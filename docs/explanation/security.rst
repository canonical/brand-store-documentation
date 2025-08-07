Dedicated Snap Store security
=============================

Dedicated Snap Stores are designed to ensure the secure distribution of
software defined as snaps. To facilitate this distribution, a Dedicated Snap
Store requires a few key pieces of information which are stored in different
locations depending on the intended use of the information. Dedicated Snap
Stores require various secrets which must be carefully handled to ensure a
secure Store.

Required secrets
----------------

- Account credentials

  - Specifically, the :ref:`Brand account <brand-accounts>` credentials

    - The Brand account should only have the Publisher role in a Dedicated Snap Store.
    - Brand account access should be strictly limited.

  - Other Ubuntu One SSO accounts can be granted privileged access to Dedicated Snap Stores

    - Such as publishing new names or reviewing recently uploaded snaps
- Signing keys
  
  - Used to sign `assertions <https://ubuntu.com/core/docs/reference/assertions>`_.
  - A separate key should be used for signing for each type of assertion.
  - Each key should have an `assigned role <https://canonical-serial-vault.readthedocs-hosted.com/serial-vault/signing-keys/#register-a-signing-key-with-limited-roles>`_
    to limit the scope of its use.
  
Location of secrets
-------------------

Safeguarding secrets is critical. Some secrets will be controlled and protected
by Canonical, while others are controlled by the customer. It is critical you
protect these secrets.

Secrets stored by Canonical
***************************

- Serial assertion signing keys

  - Should be generated in the Serial Vault UI.

Secrets stored by you
*********************

- Account credentials

  - Most importantly, the Brand account credentials
- Registered keys

  - Including those used to sign model and system-user assertions

How secrets are handled
-----------------------

Canonical has specific practices for handling secrets. Additionally, there are
some general recommendations for you.

By Canonical
************

- Serial assertion signing keys are stored in the `Serial Vault <https://canonical-serial-vault.readthedocs-hosted.com/>`_
  The private keys cannot be accessed once generated or uploaded to the Serial
  Vault.

By you
******

- Account credentials should be stored and transmitted in a secure manner, for
  example by using a shared credential manager. Access to account credentials
  should only by given to individuals on an "as-needed" basis, and account
  credentials should be rotated regularly.
- Multi-factor authentication should be used for all Ubuntu One SSO accounts.
- Private keys should never be shared.

  - You may wish to generate keys on a dedicated hardware security module.
