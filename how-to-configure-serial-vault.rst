Configure Serial Vault
----------------------

.. configure-serial-vault-start

To get started with the `Serial Vault <https://serial-vault-admin.canonical.com/>`_ (SV admin account required), read the following pages. You can click the next button in the bottom right corner to move from one to the next.

- `Serial Vault Overview <https://ubuntu.com/core/services/guide/serial-vault-overview>`_
- `Signing Keys <https://ubuntu.com/core/services/guide/signing-keys>`_
- `Device Model and Identity <https://ubuntu.com/core/services/guide/device-model-and-identity>`_

.. note::

    Please be sure to review the signing keys sub-section on key roles. Use of key roles is a best practice which helps to limit the scope of what type of assertions each key can be used to sign. This is meant to limit your exposure if a key were to be compromised. Use of key roles also means that you **must no longer register your keys** using ``snapcraft register-key``. This will now be handled by the Snap Store admins as part of the key role assignment. And finally, please note that key roles can only be assigned to new keys, they cannot be added to keys at a later time.

To configure your serial vault, follow the instructions at the links below, using ``{{CUSTOMER_MODEL_NAME}}`` as the model name, ``{{CUSTOMER_BRAND_EMAIL}}`` as the brand email, and ``{{CUSTOMER_BRAND_ACCOUNT_ID}}`` as the brand ID:

- `Environment Setup <https://ubuntu.com/core/services/guide/environment-setup>`_
- `Generate a Serial Signing Key <https://ubuntu.com/core/services/guide/generate-a-serial-signing-key>`_
- `Import a Serial Signing Key <https://ubuntu.com/core/services/guide/import-a-serial-signing-key>`_
- `Register a New Device Model Name <https://ubuntu.com/core/services/guide/register-a-new-device-model-name>`_
- `Generate a Model Signing Key <https://ubuntu.com/core/services/guide/generate-a-model-signing-key>`_
- `Check the Signing Log <https://ubuntu.com/core/services/guide/check-the-signing-log>`_
