Dedicated Snap Store configuration
==================================

{% if 'admin@acme.com' in CUSTOMER_ADMIN_EMAIL %}
.. warning:: 

  Example values are provided for store configuration in this document. If
  you are a Dedicated Snap Store customer, you will be provided with a set of
  documentation with the details of your store.

{% endif %}

This section provides links to useful documentation as well as important facts
associated with your Dedicated Snap Store.

Store architecture
------------------

Your Dedicated Snap Store is composed of two stores, your :ref:`Base store <base-stores>`
and your :ref:`Device View store <device-view-stores>`.

Your Base store is:  ``{{CUSTOMER_STORE_NAME}}`` (``{{CUSTOMER_STORE_ID}}``)

Your Device View store is: ``{{CUSTOMER_DEVICEVIEW_NAME}}`` (``{{CUSTOMER_DEVICEVIEW_ID}}``)

Your Device View store is configured to automatically include all snaps from ``{{STORES_WITH_WHOLESALE_INCLUSION}}``

All stores (including your Device View store) always include the snapd snap and
the LTS core snaps (i.e. core18, core20, core22, core24).

Accounts and roles
------------------

Ubuntu SSO accounts underpin developer interactions with the various Stores. To
understand accounts and roles, please read:

* `Ubuntu SSO Accounts <https://documentation.ubuntu.com/dedicated-snap-store/explanation/ubuntu-sso-accounts/>`_
* `Setting up account roles <https://documentation.ubuntu.com/dedicated-snap-store/how-to/setting-up-account-roles>`_

Your store has been provisioned with the following IDs and roles:

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

Brand account
-------------

The Brand account was set up for your Dedicated Snap Store at the time of store
creation. The Brand account defines the Brand scope of authority, and it must
be used for certain functions You can find those functions :ref:`here <brand-accounts>`.

Your Brand account is: ``{{CUSTOMER_BRAND_EMAIL}}`` (account-id: ``{{CUSTOMER_BRAND_ACCOUNT_ID}}``)

As a publisher, after registering snap names the Brand account may make other
developer accounts **Collaborators** on these snaps. These accounts may then
upload future revisions of these snaps. We recommend that collaborators be
added as soon as possible to avoid using the Brand credentials for longer than
necessary.

Brand keys
**********

Keys are used for signing a variety of documents called `assertions <https://snapcraft.io/docs/assertions>`_,
Some of these assertions are signed by Canonical, and some must be signed by
keys registered to the Brand account.

Limit access to Brand keys. It's strongly advised that you consider using a
PKI system or key vault to protect your Brand keys, and limit access to them.
Hardware cryptotokens are another possibility, although they may be more
challenging to use than PKI systems in practice.

Ubuntu Pro & Support Portal account
-----------------------------------

An Ubuntu Pro account and Support Portal access are also included with your
Dedicated Snap Store.

Access has been granted to the SSO account: {{CUSTOMER_PRO_EMAIL}}

Ubuntu Pro Dashboard
********************

Dedicated Snap Store customers are provided an Ubuntu Pro account to
enable access to ESM updates during snap builds (enabled by use of the
``SNAPCRAFT_UA_TOKEN`` environment variable). This is accomplished by adding your
Pro token to CI/CD systems used to build your snaps. This token can be accessed
by signing into the `Ubuntu Pro Dashboard <http://ubuntu.com/pro/dashboard>`_
using the account mentioned at the beginning of this section.

Support Portal
**************

Dedicated Snap Store customers are also provided access to our
Support Portal which can be used to create support cases. The Support
Portal can be accessed by signing into the `Support Portal Dashboard <https://support-portal.canonical.com/dashboard>`_
using the account mentioned at the beginning of this section.

Canonical support will setup one contact point for the support account.
Currently the Technical support contact set for the Dedicated Snap Store is
{{CUSTOMER_PRO_EMAIL}}.

For examples on some common support tickets, refer to :doc:`/how-to/support-tickets`.

.. _landscape:

Landscape
---------

Landscape enables you to manage a fleet of devices by controlling updates,
triggering remote snap installation, and other more advanced fleet management
features.
 
Landscape is made available to you through a software-as-a-service (SaaS) model,
hosted and managed by Canonical, or as a self-hosted option. Refer to the `Landscape documentation <https://documentation.ubuntu.com/landscape/explanation/landscape/about-landscape/>`_
for more.

Please contact customersuccess@canonical.com to request a Landscape SaaS
account.

Serial Vault
------------

The `Serial Vault <https://serial-vault-admin.canonical.com>`_ is responsible
for providing your devices with a `serial assertion <https://documentation.ubuntu.com/core/reference/assertions/serial>`_,
which is used for connecting to a Device View store. The Serial Vault can be
accessed by the administrator, {{CUSTOMER_ADMIN_EMAIL}}.

To get started with the Serial Vault, please refer to the
:doc:`/how-to/configure-serial-vault`.
