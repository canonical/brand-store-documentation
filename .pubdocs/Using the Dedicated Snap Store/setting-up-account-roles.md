(setting-up-account-roles)=
# Setting up account roles

When setting up account roles, the Administrator should add appropriate accounts with roles to your Base store, where all snaps are registered and published. Here is a look at the [dashboard](https://snapcraft.io/admin) screen an Administrator uses to add Ubuntu SSO accounts to a specific Snap Store with various roles.

An Administrator can navigate to the Users and Roles screen as follows:

* https://snapcraft.io/admin
* Find the appropriate store on the (left side) displayed list, and select the Members on the Top bar of the dashboard.
* Under Users and Roles, select Manage users and their roles.

![|476x219](https://lh5.googleusercontent.com/QaGGrfgBUJm5eXSnRwXzSGM12rcOh0qKc_nesD9OJB0p-FVa0F9f2Id-99QZESwui2mYdQp3fRTZBfNcrM7xXTUGcGgQd0a2VPs4A22iFNsBb0XIZcAhTRDGj4cqqFXwaVrmVPeEZUDw7FoE0jA)![|244x421](https://lh5.googleusercontent.com/16PT0FWIPPFLFSn45tpnwG43VcGcwxbAx7Ij6rh3Gwsl-hVP1JbZZXQVCmPBqy6NOS7CA29f0w3OesU496MKpzrg41dsWhKnYSi5UQ9mL5PsLe1I95o5YoFxB77x3TMbe9FMBm6j2-bhxK1uvwA)

You should then review and set the following roles for each store:

* Base Store
  * Publisher
  * Admin, Reviewer
  * Viewer
* Device View Store
  * Admin
  * Viewer

The Device View store does not require Publishers or Reviewers since it does not host snaps but is only a mechanism for curating snaps for device groups.

A Device View store should have at least a Viewer account. This is needed when building images that point to the Device View store. A viewer account can download snaps from the store for inclusion into the image.
