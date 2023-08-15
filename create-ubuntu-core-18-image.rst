How to create an Ubuntu Core 18 image
=====================================

This section walks through the process of creating and booting Ubuntu Core and Classic image for amd64 architecture to validate the store setup done above.

Creating the gadget snap
------------------------

For building a custom gadget snap for production systems start by forking a suitable candidate from the `Canonical supported gadgets <https://snapcraft.io/docs/gadget-snap#heading--setup>`__ and follow these `instructions <https://docs.snapcraft.io/the-gadget-snap/696>`__.

For this particular case, validating the initial store setup, let's fork the pc-amd64-gadget. This gadget enables the device to request store credentials from the Serial Vault, as configured above:

Creating a gadget snap for Ubuntu Core image
********************************************


.. terminal::
    :scroll:
    :input: sudo apt-get install git

    :input: git clone -b <CUSTOMER-UBUNTU-CORE-VERSION> https://git.launchpad.net/~lyoncore-team/lyoncore-snaps/+git/pc-amd64-gadget <CUSTOMER-STORE-PREFIX>gadget
    :input: cd <CUSTOMER-STORE-PREFIX>gadget

Update "name" field in the snapcraft.yaml to ""``<CUSTOMER-STORE-PREFIX>gadget``". Feel free to also adjust the "version", "summary" and "description" to be more meaningful in your context. Update "<volume name>:" field in gadget.yaml from "pc:" to "``<CUSTOMER-MODEL-NAME>:``".

Build the snap informing the model **API Key** generated during the Serial Vault setup above:

.. terminal::
    :scroll:
    :input: SNAPCRAFT_BUILD_ENVIRONMENT=host MODEL_APIKEY=<API-key-for-model-from-serial-vault> snapcraft
    
    …
    Snapped <CUSTOMER-STORE-PREFIX>gadget_18-0.1_amd64.snap


.. note::
    
    The sample “product_serial” is loosely generated (`date -Is`) in this gadget. In production the serial number should be derived from a value inserted during the factory process, or from a unique hardware identifier, for uniqueness and traceability.

Now register the snap name in the target store and push the initial revision:

.. terminal::
    :input: snapcraft whoami

    email:        <CUSTOMER-BRAND-EMAIL>
    developer-id: <CUSTOMER-BRAND-ACCOUNT-ID>

    :input: snapcraft register <CUSTOMER-STORE-PREFIX>gadget --store=<CUSTOMER-STORE-ID>
    ...
    you, and be the software you intend to publish there? [y/N]: y
    Registering <CUSTOMER-STORE-PREFIX>gadget.
    Congrats! You are now the publisher of '<CUSTOMER-STORE-PREFIX>gadget'.

    :input: snapcraft push <CUSTOMER-STORE-PREFIX>gadget_18-0.1_amd64.snap
    ...
    The Store automatic review failed.
    A human will soon review your snap, but if you can't wait please write in the snapcraft forum asking for the manual review explicitly.
    If you need to disable confinement, please consider using devmode, but note that devmode revision will only be allowed to be released in edge and beta channels.
    Please check the errors and some hints below:
    - (NEEDS REVIEW) type 'gadget' not allowed


.. note:: 
    
    The Brand account must be a **Publisher** under "Manage Users and their roles" to register and publish the gadget snap.

Logged in as the **Store Administrator** (benefiting of its **Reviewer** permission in this setup), access the `reviews page <https://dashboard.snapcraft.io/reviewer/\<CUSTOMER-STORE-ID\>/>`__ and **Approve** the gadget revision. All gadget uploads require manual review. 

Once the revision is approved, use snapcraft to release it in the stable channel:

.. terminal::
    :input: snapcraft whoami

    email:        <CUSTOMER-BRAND-EMAIL>
    developer-id: <CUSTOMER-BRAND-ACCOUNT-ID>

    :input: snapcraft release <CUSTOMER-STORE-PREFIX>gadget 1 stable
    Track    Arch    Channel    Version    Revision
    latest   all     stable     18-0.1  1
                     candidate  ^          ^
                     beta       ^          ^
                     edge       ^          ^
    The 'stable' channel is now open.


The gadget snap is now available for installation from the ``<CUSTOMER-STORE-NAME>`` stores, and for inclusion in images.

Creating a gadget snap for Ubuntu Classic image
***********************************************

.. terminal::
    :scroll:
    :input: sudo apt-get install git

    :input: git clone -b classic https://git.launchpad.net/~lyoncore-team/lyoncore-snaps/+git/pc-amd64-gadget \
    <CUSTOMER-STORE-PREFIX>gadget-classic
    :input: cd <CUSTOMER-STORE-PREFIX>gadget-classic

Update "name" field in the snapcraft.yaml to "``<CUSTOMER-STORE-PREFIX>gadget-classic``" and “base” field in the snapcraft.yaml to “core18”. Feel free to also adjust the "version", "summary" and "description" to be more meaningful in your context. Update "<volume name>:" field in gadget.yaml from "pc:" to "``<CUSTOMER-MODEL-NAME>:``".

Build the snap informing the model **API Key** generated during the Serial Vault setup above:

.. terminal::
    :scroll:
    :input: SNAPCRAFT_BUILD_ENVIRONMENT=host MODEL_APIKEY=<API-key-for-model-from-serial-vault> snapcraft

    …
    Snapped <CUSTOMER-STORE-PREFIX>gadget-classic_0.1_amd64.snap

.. note::
    
    The sample “product_serial” is loosely generated (`date -Is`) in this gadget. In production the serial number should be derived from a value inserted during the factory process, or from a unique hardware identifier, for uniqueness and traceability.

Now register the snap name in the target store and push the initial revision:

.. terminal::
    :input: snapcraft whoami

    email:        <CUSTOMER-BRAND-EMAIL>
    developer-id: <CUSTOMER-BRAND-ACCOUNT-ID>

    :input: snapcraft register <CUSTOMER-STORE-PREFIX>gadget-classic --store <CUSTOMER-STORE-ID>
    ...
    you, and be the software you intend to publish there? [y/N]: y
    Registering <CUSTOMER-STORE-PREFIX>gadget-classic.
    Congrats! You are now the publisher of '<CUSTOMER-STORE-PREFIX>gadget-classic'.

    :input: snapcraft push <CUSTOMER-STORE-PREFIX>gadget-classic_0.1_amd64.snap
    ...
    The Store automatic review failed.
    A human will soon review your snap, but if you can't wait please write in the snapcraft forum asking for the manual review explicitly.
    If you need to disable confinement, please consider using devmode, but note that devmode revision will only be allowed to be released in edge and beta channels.
    Please check the errors and some hints below:
    - (NEEDS REVIEW) type 'gadget' not allowed


.. note::
    
    The Brand account must be a **Publisher** under "Manage Users and their roles" to register and publish the gadget snap.

Logged in as the **Store Administrator** (benefiting of its **Reviewer** permission in this setup), access the `reviews page <https://dashboard.snapcraft.io/reviewer/\<CUSTOMER-STORE-ID\>/>`__ and **Approve** the gadget revision. All gadget uploads require manual review. 

Once the revision is approved, use snapcraft to release it in the stable channel:

.. terminal::
    :input: snapcraft whoami

    email:        <CUSTOMER-BRAND-EMAIL>
    developer-id: <CUSTOMER-BRAND-ACCOUNT-ID>

    :input: snapcraft release <CUSTOMER-STORE-PREFIX>gadget-classic 1 stable
    Track    Arch    Channel    Version    Revision
    latest   all     stable     0.1  1
                     candidate  ^          ^
                     beta       ^          ^
                     edge       ^          ^
    The 'stable' channel is now open.


The gadget snap is now available for installation from the <CUSTOMER-STORE-NAME> stores, and for inclusion in images.

Creating model assertions for Ubuntu Core and Classic images
------------------------------------------------------------

The ``<CUSTOMER-DEVICEVIEW-NAME>`` device view is the target of the ``<CUSTOMER-MODEL-NAME>`` model and has to be populated with the snaps applicable to these devices.

Logged in as the **Store Administrator**, access the `View and manage snaps <https://dashboard.snapcraft.io/dev/store/\<CUSTOMER-DEVICEVIEW-ID\>/packages/>`__ page and include appropriate additional snaps (e.g., pc-kernel and hello) from Global store required in ``<CUSTOMER-MODEL-NAME>`` model. Core and snapd packages are included automatically and cannot be removed.

.. image:: /images/core-18-store-inclusion.png

Creating a model assertion for Ubuntu Core
******************************************

Fill the field ``<CUSTOMER-REQUIRED-SNAPS>`` with the required snaps (e.g., hello). Create and sign the model assertion for Ubuntu Core image:

.. terminal::
    :scroll:
    :input: cat << EOF > <CUSTOMER-MODEL-NAME>-model.json

    {
    "type": "model",
    "authority-id": "<CUSTOMER-BRAND-ACCOUNT-ID>",
    "brand-id": "<CUSTOMER-BRAND-ACCOUNT-ID>",
    "series": "16",
    "model": "<CUSTOMER-MODEL-NAME>",
    "store": "<CUSTOMER-DEVICEVIEW-ID>",
    "architecture": "amd64",
    "base": "core<CUSTOMER-UBUNTU-CORE-VERSION>",
    "classic": "false",
    "gadget": "<CUSTOMER-STORE-PREFIX>gadget",
    "kernel": "pc-kernel=<CUSTOMER-UBUNTU-CORE-VERSION>",
    "required-snaps": ["<CUSTOMER-REQUIRED-SNAPS>"],
    "timestamp": "$(date +%Y-%m-%dT%TZ)"
    }
    EOF

    :input: cat <CUSTOMER-MODEL-NAME>-model.json | snap sign -k model &> <CUSTOMER-MODEL-NAME>-model.assert

Creating a model assertion for Ubuntu Classic image
***************************************************

Fill the field ``<CUSTOMER-REQUIRED-SNAPS>`` with the required snaps (e.g., hello). Create and sign the model assertion for Ubuntu Classic image:

.. terminal::
    :scroll:
    :input: cat << EOF > <CUSTOMER-MODEL-NAME>-classic-model.json

    {
    "type": "model",
    "authority-id": "<CUSTOMER-BRAND-ACCOUNT-ID>",
    "brand-id": "<CUSTOMER-BRAND-ACCOUNT-ID>",
    "series": "16",
    "model": "<CUSTOMER-MODEL-NAME>",
    "store": "<CUSTOMER-DEVICEVIEW-ID>",
    "architecture": "amd64",
    "classic": "true",
    "gadget": "<CUSTOMER-STORE-PREFIX>gadget-classic",
    "required-snaps": ["<CUSTOMER-REQUIRED-SNAPS>"],
    "timestamp": "$(date +%Y-%m-%dT%TZ)"
    }
    EOF

    :input: cat <CUSTOMER-MODEL-NAME>-classic-model.json | snap sign -k model &> <CUSTOMER-MODEL-NAME>-classic-model.assert

Troubleshooting: When you sign the model assertion, you could get the following error message due to the locked gpg-agent.

.. terminal::
    :scroll:
    :input: cat <CUSTOMER-MODEL-NAME>-model.json | snap sign -k model &> <CUSTOMER-MODEL-NAME>-model.assert

    error: cannot sign assertion: cannot sign using GPG: /usr/bin/gpg --personal-digest-preferences SHA512 --default-key <my key> --detach-sign failed: exit status 2 ("gpg: signing failed: No such file or directory\ngpg: signing failed: No such file or directory\n")

Please unlock gpg-agent by following commands and then sign model assertions again.

.. terminal::
    :input: touch test.txt

    :input: gpg --homedir ~/.snap/gnupg --detach-sign --default-key model test.txt

Switching to a developer account
--------------------------------

The next steps will take you through the building of an image. The image build process requires that the Account running the build tools have “Viewer” access permissions to the Device View Store.  

Note that once the model is signed by the *Brand account*, there is no need to continue to use such powerful credentials. We recommend not added “Viewer” permissions to the Brand Account, and switching to a developer account to seed images. 

The only requirement is having **Store Viewer** permission on the ``<CUSTOMER-DEVICEVIEW-NAME>`` store. Go to "Manage Users and their roles" to add a developer account and then set it as **Viewer**.

Setup authentication for downloading snaps from the ``<CUSTOMER-DEVICEVIEW-NAME>`` store:

.. terminal::
    :input: snapcraft whoami

    email:        <CUSTOMER-VIEWER-EMAIL>
    developer-id: <CUSTOMER-VIEWER-ACCOUNT-ID>

    :input: snapcraft export-login --acls package_access store.auth
    Enter your Ubuntu One e-mail address and password.
    …
    This exported login is not encrypted. Do not commit it to version control!


Creating an Ubuntu Core image
-----------------------------

This section describes the details of Ubuntu Core image building against the ``<CUSTOMER-DEVICEVIEW-NAME>`` store.

Ensure tool for building images is available:

.. terminal::
    :input: sudo snap install ubuntu-image --classic 

    ...

Ubuntu Core image is built in the one line instruction by using the above developer account credential:

.. terminal::
    :scroll:
    :input: sudo UBUNTU_STORE_AUTH_DATA_FILENAME=./store.auth ubuntu-image snap -c stable <CUSTOMER-MODEL-NAME>-model.assert

    ...

Launching and verifying Ubuntu Core image
*****************************************

Install the qemu-kvm package with the following command:

.. terminal::
    :input: sudo apt install qemu-kvm ovmf qemu-utils

    ...

Run the kvm-ok command to check KVM status and your hardware,

.. terminal::
    :input: kvm-ok

    ...

The message should say:

.. code:: text

    INFO: /dev/kvm exists
    KVM acceleration can be used

This is the best outcome — it means that Ubuntu Core will run fast on the system, taking advantage of hardware acceleration from CPU.

Now launch a virtual machine with KVM, using the following command:

.. terminal::
    :scroll:
    :input: kvm -smp 2 -m 1500 -netdev user,id=mynet0,hostfwd=tcp::8022-:22,hostfwd=tcp::8090-:80 -device virtio-net-pci,netdev=mynet0 -drive "file=<CUSTOMER-MODEL-NAME>.img"

Note: this command sets up port redirections:

- localhost:8022 is redirecting to port 22 of the virtual machine for accessing it through SSH
- localhost:8090 is redirecting to its port 80

There should be  a window now, with your Ubuntu Core virtual machine booting inside it.
The system will boot then become ready to configure. The device will display the prompt “Press enter to configure”. Press enter then select “Start” to begin configuring your network and an administrator account. Follow the instructions on the screen, you will be asked to configure your network and enter your Ubuntu SSO credentials. At the end of the process, you will see your credentials to access your Ubuntu Core machine:

.. code:: text

    This device is registered to <Ubuntu SSO email address>.
    Remote access was enabled via authentication with the SSO user <Ubuntu SSO user name>
    Public SSH keys were added to the device for remote access.


Once setup is done, you can login with SSH into Ubuntu Core, using the following command:

.. terminal::
    :input: ssh -p 8022 <Ubuntu SSO user name>@localhost

User name is the Ubuntu SSO user name, shown to you at the end of the account configuration step. Login and then verify if the seeded snaps are installed, the <CUSTOMER-MODEL-NAME> model is correct and a serial assertion was obtained:

.. code:: text

    Welcome to Ubuntu Core 18 (GNU/Linux 4.15.0-74-generic x86_64)

    The programs included with the Ubuntu system are free software;
    the exact distribution terms for each program are described in the
    individual files in /usr/share/doc/*/copyright.

    Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
    applicable law.

    * Ubuntu Core:     https://www.ubuntu.com/core
    * Community:       https://forum.snapcraft.io
    * Snaps:           https://snapcraft.io

    This Ubuntu Core 18 machine is a tiny, transactional edition of Ubuntu,
    designed for appliances, firmware and fixed-function VMs.

    If all the software you care about is available as snaps, you are in
    the right place. If not, you will be more comfortable with classic
    deb-based Ubuntu Server or Desktop, where you can mix snaps with
    traditional debs. It's a brave new world here in Ubuntu Core!

    Please see 'snap --help' for app installation and updates.

    …

.. terminal::
    :user: <Ubuntu SSO user name>
    :host: localhost
    :input: snap list

    Name            Version       Rev   Tracking  Publisher     Notes
    <CUSTOMER-STORE-PREFIX>gadget  18-0.1        1     stable    <CUSTOMER-BRAND-ACCOUNT-ID>  gadget
    core            16-2.42.5     8268  stable    canonical✓    core
    core18          20200113      1650  stable    canonical✓    base
    hello           2.10          38    stable    canonical✓    -
    pc-kernel       4.15.0-74.84  365   18        canonical✓    kernel
    snapd           2.42.5        5754  stable    canonical✓    snapd

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

Creating and seeding an Ubuntu Classic image
--------------------------------------------

Detailed instructions for seeding a classic ubuntu image here: `Seeding a Classic image <https://drive.google.com/open?id=1XtHpAVJu2Q828PSquq6ElbwmM8A8Y5jS>`_ document. Here are condensed steps customized for ``<CUSTOMER-NAME>``.

Ensure tools for mounting and launching images are available:

.. terminal::
    :input: sudo apt install qemu-system-x86 cloud-image-utils kpartx qemu-kvm

    ...

Create a user.img partition with basic cloud-init configuration for launching an image:

.. terminal::
    :input: cat << EOF > user-data

    #cloud-config
    password: <a-password-for-the-image-ubuntu-account>
    chpasswd: { expire: False }
    ssh_pwauth: True
    EOF

    :input: cloud-localds -v user.img user-data
    wrote user.img with filesystem=iso9660 and diskformat=raw

Download the bionic (18.04) classic cloud image and verify it is unmodified:

.. terminal::
    :scroll:
    :input: wget https://cloud-images.ubuntu.com/releases/bionic/release/ubuntu-18.04-server-cloudimg-amd64.img
    
    …
    
    :input: sha256sum https://cloud-images.ubuntu.com/releases/bionic/release/SHA256SUMS


Mount the image so it can be modified 'in-place':

.. terminal::
    :input: rm -f ubuntu-seeded.img && \
    
    cp ubuntu-18.04-server-cloudimg-amd64.img ubuntu-seeded.img && \
    mkdir -p /tmp/img && \
    sudo modprobe nbd && sleep 1 && \
    sudo qemu-nbd --connect=/dev/nbd0 ubuntu-seeded.img && sleep 1 && \
    sudo kpartx -a /dev/nbd0 && sleep 1 && \
    sudo mount /dev/mapper/nbd0p1 /tmp/img

Seed the required snaps for the ` ``<CUSTOMER-MODEL-NAME>`` ` model, and optionally extra ones, into the image mounted in /tmp/img:

.. terminal::
    :input: sudo \
    
    UBUNTU_STORE_ID=<CUSTOMER-DEVICEVIEW-ID> \
    UBUNTU_STORE_AUTH_DATA_FILENAME=./store.auth \
    snap prepare-image --classic \
    <CUSTOMER-MODEL-NAME>-classic-model.assert \
    /tmp/img/

Unmount the modified image file: 

.. terminal::
    :input: sudo umount /tmp/img && \

    rm -rf /tmp/img && \
    sudo kpartx -d /dev/nbd0 && \
    sudo qemu-nbd --disconnect /dev/nbd0 && \
    sudo modprobe -r nbd

Launching and verifying classic image
*************************************

Launch the seeded image with QEMU (with User Networking setup):

.. terminal::
    :input: qemu-system-x86_64 \

    -drive "file=ubuntu-seeded.img,id=bootdisk,if=none,index=0" \
    -device "virtio-blk,drive=bootdisk" \
    -drive "file=user.img,id=user,if=none,format=raw,index=1" \
    -device "virtio-blk,drive=user" \
    -device virtio-net-pci,netdev=net00 \
    -netdev type=user,id=net00,hostfwd=tcp::8022-:22,hostfwd=tcp::8090-:80 \
    -smp 2 -m 1500 -enable-kvm

The snap seeding process and cloud-init configuration take a few minutes. Wait until the following syslog message is displayed:

.. code:: text

    [  OK  ] Reached target Cloud-init target.

Login as "ubuntu" using the password defined in the cloud-init configuration above. Verify the seeded snaps are installed, the ``<CUSTOMER-MODEL-NAME>`` model is correct and a serial assertion was obtained:

.. code::

    Welcome to Ubuntu 18.04.3 LTS (GNU/Linux 4.15.0-72-generic x86_64)

    * Documentation:  https://help.ubuntu.com
    * Management:     https://landscape.canonical.com
    * Support:        https://ubuntu.com/advantage

    System information as of Thu Jan 16 07:45:52 UTC 2020

    System load:  0.32              Processes:           88
    Usage of /:   54.2% of 1.96GB   Users logged in:     0
    Memory usage: 13%               IP address for ens3: 10.0.2.15
    Swap usage:   0%


    0 packages can be updated.
    0 updates are security updates.
    …

.. terminal::
    :user: ubuntu
    :host: ubuntu
    :input: snap list

    Name                    Version    Rev   Tracking  Publisher     Notes
    <CUSTOMER-STORE-PREFIX>gadget-classic  1.0        1     stable    <CUSTOMER-BRAND-ACCOUNT-ID>  gadget
    core                    16-2.42.5  8268  stable    canonical✓    core
    hello                   2.10       38    stable    canonical✓    -

    :input: snap changes
    ID   Status  Spawn               Ready               Summary
    1    Done    today at 07:42 UTC  today at 07:42 UTC  Initialize system state
    2    Done    today at 07:42 UTC  today at 07:42 UTC  Initialize device

    :input: snap model --assertion
    type: model
    authority-id: <CUSTOMER-BRAND-ACCOUNT-ID>
    series: 16
    brand-id: <CUSTOMER-BRAND-ACCOUNT-ID>
    model: <CUSTOMER-MODEL-NAME>
    …

    :input: snap model --serial --assertion
    type: serial
    authority-id: <CUSTOMER-BRAND-ACCOUNT-ID>
    revision: 1
    brand-id: <CUSTOMER-BRAND-ACCOUNT-ID>
    model: <CUSTOMER-MODEL-NAME>
    …
