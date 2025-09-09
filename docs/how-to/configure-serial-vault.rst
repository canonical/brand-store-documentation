.. _serial-vault:

Configure Serial Vault
======================

..
	TODO: will also need documentation for the Model Service

.. configure-serial-vault-start

{% if 'admin@acme.com' in CUSTOMER_ADMIN_EMAIL %}
.. warning:: 

	Example values are provided for store configuration in this document. If
	you are a Dedicated Snap Store customer, you will be provided with a set of
	documentation with the details of your store.

{% endif %}

When following the instructions for configuring your Serial Vault, keep in mind the following information:

* Your model name is: ``{{CUSTOMER_MODEL_NAME}}``,
* Your Brand account email is: ``{{CUSTOMER_BRAND_EMAIL}}``, and
* your Brand account ID is: ``{{CUSTOMER_BRAND_ACCOUNT_ID}}``

.. warning::

	It is **strongly recommended** that instead of generating and registering the
	serial assertion signing key **locally**, the Serial Vault be used to generate
	and register the key instead.

	This enhances key security by ensuring it is never stored on a local,
	potentially compromised device and instead is created and stored within
	Canonical's infrastructure.

To get started with the `Serial Vault <https://serial-vault-admin.canonical.com/>`_
follow the how-to guides available for `its <https://canonical-serial-vault.readthedocs-hosted.com>`_
documentation.

The explanation section provides some useful context for what a lot of the terms
you'll encounter when working with your Dedicated Snap Store mean.
