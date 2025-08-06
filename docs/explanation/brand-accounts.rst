.. _brand-accounts:

Brand accounts
==============

Brand accounts are a key concept for Dedicated Snap Stores. The Brand account is set
for the Dedicated Snap Store at the time of store creation. The Brand Account
defines the Brand (or company) scope of authority, and it must be used for
certain functions:

* Must be the registered owner of keys used to sign `model assertions <https://documentation.ubuntu.com/core/reference/assertions/model/>`_.
* Register snap names for snaps owned by the Brand

  * The Brand is required to register the gadget snap's name

The use of the Brand account and its credentials should be strictly limited.
Canonical recommends that the Brand Account is assigned only roles that are
truly needed. The Brand account should not be a store Administrator, Reviewer
or Viewer.

When the Brand account generates keys, they are stored on the local disk
in (``$HOME/.snap/gnupg``). This account must be secured by the company using it.
It is highly recommended that all accounts, and specifically the Brand and
Administrator accounts enable multi-factor authentication on their SSO accounts.
