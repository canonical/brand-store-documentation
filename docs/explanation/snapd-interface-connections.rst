Snapd interface connections
===========================

Snaps declare plugs for specific snapd `interfaces <https://snapcraft.io/docs/supported-interfaces>`_
in order to gain access to hardware, shared system resources, and other system
interfaces that are normally off-limits to strictly confined snaps. These plugs
must be connected to corresponding slots defined by core, application, or gadget
snaps. There are three ways that these automatic connections can happen:

a. Some interfaces, such as `network <https://snapcraft.io/docs/network-interface>`_,
   auto-connect (i.e. there's no action necessary to trigger automatic
   connection).

#. Some interfaces are classified as "`self-serve <https://dashboard.snapcraft.io/docs/brandstores/self-serve-interfaces.html>`_".
   These interfaces can be auto-connected by an account with the **Reviewer**
   role using the store's snap dashboard page. The **Reviewer** can only do this
   if they are not the **Publisher** of or    a **Collaborator** on the snap
   in question.

#. A store support portal ticket can be created to request auto-connection for
   super-privileged interfaces (e.g. `snapd-control <https://snapcraft.io/docs/snapd-control-interface>`_
   or `system-files <https://snapcraft.io/docs/system-files-interface>`_).
   Please work with your Field Engineer when you create your first such ticket,
   so as to ensure you provide all the required details. See :doc:`/how-to/support-tickets`.

As there's some manual review required for these tickets, please file them as
early as possible, as requests to expedite these requests are generally frowned
upon.
