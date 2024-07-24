Tutorial: Create an Ubuntu Core image
======================================

.. only:: latex

    .. important:: For initial provisioning and setup of your Brand Store, make sure you are familiar with :doc:`configuration-values`.

.. only:: html

    .. note:: :doc:`configuration-values` contains information relating to the specific configuration of your Brand Store.

To validate that the store was provisioned correctly, and that you are able to access it, we recommend creating and booting an Ubuntu Core image on amd64.

.. important::

    Ensure the Serial Vault is set up before proceeding with this tutorial. See :doc:`how-to-configure-serial-vault`.

Creating the gadget snap
------------------------

The first step in building an Ubuntu Core image that can communicate with your store is to build a gadget snap. Gadget snaps do many things, but for our purposes here, the important functionality is generating a serial number and using that serial number, along with a pre-shared API key, to get credentials to talk to the store. You can also use the gadget snap to set default configuration values for application snaps, and auto-connect some interfaces.

To build a custom gadget snap, we start by forking a suitable candidate from the `Canonical supported gadgets <https://snapcraft.io/docs/the-gadget-snap>`_
and follow these `instructions <https://docs.snapcraft.io/the-gadget-snap/696>`_.

For this particular case, validating the initial store setup, let's fork the ``pc-amd64-gadget``. This gadget enables the device to request store credentials from the Serial Vault, as configured above.

.. important::
    
    Gadget snaps for Ubuntu Core 24 must be built on the corresponding LTS classic release (Ubuntu 24.04) using ``snapcraft`` 8.x or later. You should also ensure that the build-packages needed to build the gadget snap are already installed, so that you're not required to use sudo when building the snap itself.

.. term::
    :input: sudo snap install snapcraft -classic --channel=8.x/stable
    
    ...

    :input: snapcraft version
    snapcraft 8.3.1

.. note::

    As the gadget snap also provides a means to provision static snap configuration for the seeded snaps in an image, you may need to require multiple gadget snaps for different models. Please see the `gadget specification <https://ubuntu.com/core/docs/gadget-snaps#heading--gadget>`_ for more details on how to provide default snap and/or system configuration for your models. It's also possible to use a single gadget for multiple devices if there are no configuration differences. If you do this, please be aware that you'll need to ensure that the models in the Serial Vault use the same **API KEY**.

.. term::
    :scroll:
    :input: sudo apt update

    :input: sudo apt install -y git
    :input: git clone -b {{CUSTOMER_UBUNTU_CORE_VERSION}} https://github.com/snapcore/pc-gadget {{CUSTOMER_STORE_PREFIX}}
    :input: cd {{CUSTOMER_STORE_PREFIX}}

.. ISSUE IN DOCUMENT:  https://docs.google.com/document/d/11z7iKogO7FDouJBfYgh9hROK41xDeaPy0ruS2_flyL0/edit?disco=AAAAxWHTvf4

Update the "name" field in the ``snapcraft.yaml`` to "``{{CUSTOMER_STORE_PREFIX}}``-pc". Feel free to also adjust the "version", "summary" and "description" to be more meaningful in your context.

Build the snap, using the model **API Key** generated during the Serial Vault setup above:

.. Following input works with or without --destructive-mode

.. term::
    :input: MODEL_APIKEY=<GENERATED-API-KEY> sudo snapcraft --destructive-mode

    ...
    Snapped {{CUSTOMER_STORE_PREFIX}}-pc_24-0.1_amd64.snap

.. note::

    The sample “product_serial” is loosely generated (``date -Is``) in this gadget. In production the serial number should be derived from a value inserted during the factory process, or from a unique hardware identifier, for uniqueness and traceability. See :ref:`dmidecode` for an example of how to modify the gadget to use dmidecode (x86 only) to read the serial number from the DMI table.

Now register the snap name in your Base Snap Store and push the initial revision:

.. term::
    :input: snapcraft whoami

    email:        {{CUSTOMER_BRAND_EMAIL}}
    developer-id: {{CUSTOMER_BRAND_ACCOUNT_ID}}

    :input: snapcraft register {{CUSTOMER_STORE_PREFIX}}-pc --store={{CUSTOMER_STORE_ID}}
    ...
    you, and be the software you intend to publish there? [y/N]: y
    Registering {{CUSTOMER_STORE_PREFIX}}-pc.
    Congrats! You are now the publisher of '{{CUSTOMER_STORE_PREFIX}}-pc'.

    :input: snapcraft push {{CUSTOMER_STORE_PREFIX}}-pc_24-0.1_amd64.snap
    The Store automatic review failed.
    A human will soon review your snap, but if you can't wait please write in the snapcraft forum asking for the manual review explicitly.

    If you need to disable confinement, please consider using devmode, but note that devmode revision will only be allowed to be released in edge and beta channels.
    Please check the errors and some hints below:
      - (NEEDS REVIEW) type 'gadget' not allowed

.. note::

    The Brand Account must be a **Publisher** under `Manage Users and their roles <https://dashboard.snapcraft.io/dev/store/{{CUSTOMER_STORE_ID}}/permissions/>`_ to register and publish the gadget snap.

Log into the web dashboard as ``{{ CUSTOMER_ADMIN_EMAIL }}`` (because it has the **Reviewer** role on the ``{{CUSTOMER_DEVICEVIEW_NAME}}`` store), access the `reviews page <https://dashboard.snapcraft.io/reviewer/{{ CUSTOMER_STORE_ID }}/>`_ and **Approve** the gadget revision. All gadget uploads require manual review.

.. note::

    One other important capability of the Reviewer role is the ability to grant "self-serve" interface connections for snaps published in the Brand Store. See `Self-serve Snap Interfaces <https://dashboard.snapcraft.io/docs/brandstores/self-serve-interfaces.html>`_ for more details.

Once the revision is approved, use snapcraft to release it in the stable channel:

.. term::
    :input: snapcraft whoami

    email:        {{CUSTOMER_BRAND_EMAIL}}
    developer-id: {{CUSTOMER_BRAND_ACCOUNT_ID}}

    :input: snapcraft release {{CUSTOMER_STORE_PREFIX}}-pc 1 stable
    Track    Arch    Channel    Version    Revision
    latest   all     stable     24-0.1     1
                     candidate  ^          ^
                     beta       ^          ^
                     edge       ^          ^
    The 'stable' channel is now open.

The gadget snap is now available for installation from the ``{{CUSTOMER_STORE_NAME}}`` store, and for inclusion in images.

Creating the model assertion
----------------------------

One final step before you can build a custom Ubuntu Core image is creation of a signed model assertion, which provides image related metadata which ubuntu-image uses to customise the image. In order to sign the model assertion, a brand model key must be created and registered using the brand account. For details on how to create and register a model key, please refer to `Sign a model assertion <https://ubuntu.com/core/docs/sign-model-assertion>`_.

Example model assertions can be found `here <https://github.com/snapcore/models>`_. This tutorial provides an example model assertion below.
Once a valid model key is available, create and sign the model assertion for your test Ubuntu Core image:

.. term::
    :input: cat << EOF > {{CUSTOMER_MODEL_NAME}}-model.json

    {
      "type": "model",
      "authority-id": "{{CUSTOMER_BRAND_ACCOUNT_ID}}",
      "brand-id": "{{CUSTOMER_BRAND_ACCOUNT_ID}}",
      "series": "16",
      "model": "{{CUSTOMER_MODEL_NAME}}",
      "store": "{{CUSTOMER_DEVICEVIEW_ID}}",
      "architecture": "amd64",
      "base": "core{{CUSTOMER_UBUNTU_CORE_VERSION}}",
      "grade": "signed",
      "snaps": [
        {
          "default-channel": "latest/stable",
          "id": "{{CUSTOMER_SNAP_IDS}}",
          "name": "{{CUSTOMER_STORE_PREFIX}}-pc",
          "type": "gadget"
        },
        {
          "default-channel": "24/stable",
          "id": "pYVQrBcKmBa0mZ4CCN7ExT6jH8rY1hza",
          "name": "pc-kernel",
          "type": "kernel"
        },
        {
          "default-channel": "latest/stable",
          "id": "amcUKQILKXHHTlmSa7NMdnXSx02dNeeT",
          "name": "core24",
          "type": "base"
        },
        {
          "default-channel": "latest/stable",
          "id": "PMrrV4ml8uWuEUDBT8dSGnKUYbevVhc4",
          "name": "snapd",
          "type": "snapd"
        },
        {
          "name": "console-conf",
          "type": "app",
          "default-channel": "24/edge",
          "id": "ASctKBEHzVt3f1pbZLoekCvcigRjtuqw",
          "presence": "optional"
        },
        {
          "default-channel": "latest/stable",
          "id": "{{CUSTOMER_SNAP_IDS}}",
          "name": "{{CUSTOMER_REQUIRED_SNAPS}}",
          "type": "app"
        }
      ],
      "timestamp": "$(date +%Y-%m-%dT%TZ)"
    }
    EOF

    :input: snapcraft list-keys
        Name          SHA3-384 fingerprint
    *   serial        <fingerprint>
    *   model         <fingerprint>

    :input: snap sign -k model {{CUSTOMER_MODEL_NAME}}-model.json > {{CUSTOMER_MODEL_NAME}}-model.assert

.. note::

    The timestamp for model assertion MUST be after the date of the model signing key being registered by snapcraft.

Log in to the web dashboard as ``{{CUSTOMER_ADMIN_EMAIL}}`` (because it has the Admin role on the ``{{CUSTOMER_DEVICEVIEW_NAME}}`` store), access the `View and manage snaps <https://snapcraft.io/admin>`_ page. Use the “Include snap” dialog to ensure that all snaps listed in the model assertion but published in the Global store (like pc-kernel in this case) get included in your private store. The core, core18, core20, core22 and snapd packages are included automatically and cannot be removed.

.. image:: /.sphinx/images/core-22-add-snap.png

Access the snap page https://dashboard.snapcraft.io/snaps/SNAPNAME to get the snap-id and fill the fields ``{{CUSTOMER_SNAP_IDS}}`` and ``{{CUSTOMER_REQUIRED_SNAPS}}``.

.. image:: /.sphinx/images/core-22-snap-id.png

Switching to a developer account
--------------------------------

Now that the model has been signed by the **Brand Account**, there is no need to continue to use such powerful credentials. We recommend switching to a developer account to seed images.

The account used must have the **Viewer** role on the ``{{CUSTOMER_DEVICEVIEW_NAME}}`` store. Log in to the web dashboard as ``{{CUSTOMER_ADMIN_EMAIL}}`` (because it has the Admin role on the ``{{CUSTOMER_DEVICEVIEW_NAME}}`` store), go to "Manage Users and their roles" to add a developer account and then set it as **Viewer**. You may also give ``{{CUSTOMER_ADMIN_EMAIL}}`` the **Viewer** role.

Set up authentication for downloading snaps from the ``{{CUSTOMER_DEVICEVIEW_NAME}}`` store:

.. term::
    :input: snapcraft whoami

    email:        {{CUSTOMER_VIEWER_EMAIL}}
    developer-id: {{CUSTOMER_VIEWER_ACCOUNT_ID}}

    :input: snapcraft export-login --acls package_access store.auth
    Enter your Ubuntu One e-mail address and password.
    ...
    This exported login is not encrypted. Do not commit it to version control!

.. note::

    Exported credentials have a default expiration of 12 months, so (a) treat them with care, and (b) note that they may need to be refreshed sometime in the future.

Creating the image
------------------

This section describes the details of Ubuntu Core image building against the ``{{CUSTOMER_DEVICEVIEW_NAME}}`` store.

Ensure a Linux build environment (Ubuntu 24.04 or later) and tool for building images are available:

.. term::
    :input: sudo snap install ubuntu-image --classic
    
    ...

Ubuntu Core image is built in the one line instruction by using the above developer account credential:

.. term::
    :input: UBUNTU_STORE_AUTH=$(cat store.auth) ubuntu-image snap {{CUSTOMER_MODEL_NAME}}-model.assert

    ...

.. note::

    It's also possible to test your gadget snap without releasing it to the store. If you do this, you'll need to copy the .snap file to the directory you're running ubuntu-image in, ensure that your model assertion removes the snap-id and channel for the gadget snap, and use the ``--snap=ubuntu-image`` command-line option to instruct ``ubuntu-image`` to use the local snap.

Launching and verifying the image
---------------------------------

To launch and test your newly generated Ubuntu Core image, follow the steps here: `Ubuntu Core: Testing with QEMU <https://ubuntu.com/core/docs/testing-with-qemu>`_. Once the image is booted and installed, you can log in then verify if the seeded snaps are installed, the {{CUSTOMER_MODEL_NAME}}  model is correct and a serial assertion was obtained:

.. note:: The following shows the expected output for a Ubuntu Core 22 image.

.. term::
    :user: {{UBUNTU_SSO_USER_NAME}}
    :host: ubuntu

    Welcome to Ubuntu 22.04 LTS (GNU/Linux 5.15.0-48-generic x86_64)

    The programs included with the Ubuntu system are free software;
    the exact distribution terms for each program are described in the
    individual files in /usr/share/doc/*/copyright.

    Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
    applicable law.

    * Ubuntu Core:     https://www.ubuntu.com/core
    * Community:       https://forum.snapcraft.io
    * Snaps:           https://snapcraft.io

    This Ubuntu Core 22 machine is a tiny, transactional edition of Ubuntu,
    designed for appliances, firmware and fixed-function VMs.

    If all the software you care about is available as snaps, you are in
    the right place. If not, you will be more comfortable with classic
    deb-based Ubuntu Server or Desktop, where you can mix snaps with
    traditional debs. It's a brave new world here in Ubuntu Core!

    Please see 'snap --help' for app installation and updates.

    …

    :input: snap list

    Name       Version        Rev    Tracking       Publisher   Notes
    <CUSTOMER-STORE-PREFIX>-pc    22-0.1 1     stable  <CUSTOMER-BRAND-ACCOUNT-ID>  gadget
    core22     20220706       275    stable         canonical✓  base
    <CUSTOMER-REQUIRED-SNAPS>
    pc-kernel  5.15.0-48.54.2 1105   22/stable      canonical✓  kernel
    snapd      2.57.1         16778  stable         canonical✓  snapd

    :input: snap changes
    ID   Status  Spawn               Ready               Summary
    1    Done    today at 07:15 UTC  today at 07:16 UTC  Initialize system state
    2    Done    today at 07:16 UTC  today at 07:16 UTC  Initialize device

    :input: snap model --assertion
    type: model
    authority-id: <CUSTOMER-BRAND-ACCOUNT-ID>
    series: 16
    brand-id: <CUSTOMER-BRAND-ACCOUNT-ID>
    model: <CUSTOMER-MODEL-NAME>
    ... 

    :input: snap model --serial --assertion
    type: serial
    authority-id: <CUSTOMER-BRAND-ACCOUNT-ID>
    revision: 1
    brand-id: <CUSTOMER-BRAND-ACCOUNT-ID>
    model: <CUSTOMER-MODEL-NAME>
    ...
