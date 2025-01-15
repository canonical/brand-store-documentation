Configure Serial Vault
------------------------

.. configure-serial-vault-start

To get started with the `Serial Vault <https://serial-vault-admin.canonical.com/>`_ (SV admin account required), read the following pages. You can click the next button in the bottom right corner to move from one to the next.

- `Serial Vault Overview <https://ubuntu.com/core/services/guide/serial-vault-overview>`_
- `Device Model and Identity <https://ubuntu.com/core/services/guide/device-model-and-identity>`_

To configure your serial vault, follow the instructions at the links below, using ``{{CUSTOMER_MODEL_NAME}}`` as the model name, ``{{CUSTOMER_BRAND_EMAIL}}`` as the brand email, and ``{{CUSTOMER_BRAND_ACCOUNT_ID}}`` as the brand ID:

- `Environment Setup <https://ubuntu.com/core/services/guide/environment-setup>`_
- `Generate a Serial Signing Key <https://ubuntu.com/core/services/guide/generate-a-serial-signing-key>`_
- `Register a New Device Model Name <https://ubuntu.com/core/services/guide/register-a-new-device-model-name>`_
- `Generate a Model Signing Key <https://ubuntu.com/core/services/guide/generate-a-model-signing-key>`_
- `Check the Signing Log <https://ubuntu.com/core/services/guide/check-the-signing-log>`_

.. note::

    Although it's possible to generate a local serial signing key and upload it to the Serial Vault, a more secure practice is to use the Serial Vault's key generation facility instead. Using this approach reduces the attack surface as the private key is not accessible externally.
