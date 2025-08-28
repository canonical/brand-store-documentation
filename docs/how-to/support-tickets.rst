.. _support-tickets:

File a support ticket
=====================

.. support-tickets-start

{% if 'admin@acme.com' in CUSTOMER_ADMIN_EMAIL %}
.. warning:: 

	Example values are provided for store configuration in this document. If
	you are a Dedicated Snap Store customer, you will be provided with a set of
	documentation with the details of your store.

{% endif %}

Several key activities require some intervention from Canonical. These
types of requests are done via the `Canonical Support Portal Dashboard <https://support-portal.canonical.com/dashboard>`_.

Below are some things which require intervention, along with an example request.

Interface auto-connections
--------------------------

Setting up interfaces to automatically connect is important for ensuring smooth
snap functionality in production, and is one of the most common requests you
will make.

Provide the following information when submitting a snap interface
connection request support case:

::

	I would like to request the auto-connection of the interface <interface
	name> for the snap <snap name>, ID <snap ID>. This snap should auto-connect
	when installed from the store {{CUSTOMER_DEVICEVIEW_NAME}}, ID {{CUSTOMER_DEVICEVIEW_ID}}.

	This snap should auto-connect to the slot <slot name> provided by the snap
	<snap name>, ID <snap ID> provided by the store {{CUSTOMER_STORE_NAME}}, ID {{CUSTOMER_STORE_ID}}.

	This interface needs to be auto-connected because <reason>

Key roles
---------

The usage of `key roles <https://canonical-serial-vault.readthedocs-hosted.com/serial-vault/signing-keys/>`_
is a best practice which limits the types of assertions any registered key
can be used to sign. This helps to limit exposure in case a key were to become
compromised.

Importantly, in order to give a key a specific role you must *refrain from
registering the key with* ``snapcraft register-key``. Instead, this process is
handled by the Snap Store team.

This process requires exporting part of the key and supplying it in the support
ticket. This can be done with `snap export-key <key name>`.

::

	I would like to give my key <key name> the <model|preseed|serial|system-user> role.

	This key should be registered to our Brand account, {{CUSTOMER_BRAND_ACCOUNT_ID}}.

	This key should be constrained to the following model names:

	* <model name>
	* <model name>
	* ...

	Below is the base64-encoded key:

	AcbB...eRazZtg58e/OF8sAEQEAAQ==

Additional Device View stores
-----------------------------

When your organization decides that a new model is required beyond the original
one your Dedicated Snap Store was provisioned with, you should create a new
Device View store for that model to use. This will allow for greater isolation
of the available software between your various models, ensuring that each device
only has access to the software and infrastructure it requires to function.

::

	I would like to request an additional Device View store.

	This Device View store should have alias <new store alias> and it should
	have targetted inclusion of my Base store {{CUSTOMER_STORE_NAME}}, ID {{CUSTOMER_STORE_ID}}.

	The model name associated with this Device View store is <model name>.

