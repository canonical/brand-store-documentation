.. _setting-roles:

Set up account roles
====================

Account roles can be set either when a store administrator adds a new Ubuntu
One SSO account to the store, or after. When setting up account roles, the
administrator should add appropriate accounts with roles to the :ref:`Base store <base-stores>`,
where all snaps should be registered and published, as well as the :ref:`Device View store <device-view-stores>`,
which all devices will connect to for updates.

To add a new user to a store or modify account permissions, an administrator should:

1. Navigate to `https://snapcraft.io/admin <https://snapcraft.io/admin>`_
#. Find the appropriate store in the left-side dropdown box and
#. select the :guilabel:`Members` menu in the sidebar of the dashboard beneath
   the dropdown

To add a new user, select :guilabel:`Add new member` and enter the Ubuntu One
SSO email, assigning roles as needed.

To update permissions for already added accounts, select or deselect the
corresponding tick boxes.

Ensure you have reviewed the `roles <https://documentation.ubuntu.com/dedicated-snap-store/how-to/setting-up-account-roles>`_
and have covered the appropriate permissions for each account. You should ensure the following roles are set for each store:

* Base Store

  * Publisher
  * Admin, Reviewer
  * Viewer
* Device View Store

  * Admin
  * Viewer

The Device View store does not require Publishers or Reviewers since it does not
host snaps but is only a mechanism for curating snaps for device groups.

A Device View store should have at least a Viewer account. This is needed
when building images that point to the Device View store. A viewer account can
download snaps from the store for inclusion into the image.
