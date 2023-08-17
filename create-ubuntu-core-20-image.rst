How to create an Ubuntu Core 20 or Classic image
================================================

This section walks through the process of creating and booting Ubuntu Core and Classic image for amd64 architecture to validate the store setup done above.

.. note::

    The provisioning of Ubuntu Core and Classic image is only for verification of the Brand store and Serial Vault service, and it’s not mandatory for production delivery.

Creating the gadget snap
------------------------

For building a custom gadget snap for production systems start by forking a suitable candidate from the Canonical supported gadgets and follow these instructions.

For this particular case, validating the initial store setup, let's fork the ``pc-amd64-gadget``. This gadget enables the device to request store credentials from the Serial Vault, as configured above:

Creating a gadget snap for Ubuntu Core image
********************************************

.. terminal::
    :input: sudo apt-get install git

    :input: git clone -b <CUSTOMER-UBUNTU-CORE-VERSION>
    https://github.com/snapcore/pc-amd64-gadget  \
      <CUSTOMER-STORE-PREFIX>
    :input: cd <CUSTOMER-STORE-PREFIX>

Update "name" field in the snapcraft.yaml to "``<CUSTOMER-STORE-PREFIX>``". Feel free to also adjust the "version", "summary" and "description" to be more meaningful in your context. Update "<volume name>:" field in ``gadget.yaml`` from "pc:" to "``<CUSTOMER-DEVICEVIEW-ALIAS>:``".

Build the snap informing the model **API Key** generated during the Serial Vault setup above:

.. terminal::
    :input: SNAPCRAFT_BUILD_ENVIRONMENT=host \ MODEL_APIKEY=<API-key-for-model-from-serial-vault> snapcraft

    …
    Snapped <CUSTOMER-STORE-PREFIX>_20-0.1_amd64.snap

.. note::

    The sample “product_serial” is loosely generated (``date -Is``) in this gadget. In production the serial number should be derived from a value inserted during the factory process, or from a unique hardware identifier, for uniqueness and traceability.

Now register the snap name in the target store and push the initial revision:

.. terminal::
    :input: snapcraft whoami

    email:        <CUSTOMER-BRAND-EMAIL>
    developer-id: <CUSTOMER-BRAND-ACCOUNT-ID>

    :input: snapcraft register <CUSTOMER-STORE-PREFIX> --store=<CUSTOMER-STORE-ID>
    ...
    you, and be the software you intend to publish there? [y/N]: y
    Registering <CUSTOMER-STORE-PREFIX>.
    Congrats! You are now the publisher of '<CUSTOMER-STORE-PREFIX>'.

    :input: snapcraft upload <CUSTOMER-STORE-PREFIX>_20-0.1_amd64.snap
    ...
    The Store automatic review failed.
    A human will soon review your snap, but if you can't wait please write in the snapcraft forum asking for the manual review explicitly.
    If you need to disable confinement, please consider using devmode, but note that devmode revision will only be allowed to be released in edge and beta channels.
    Please check the errors and some hints below:
      - (NEEDS REVIEW) type 'gadget' not allowed

.. note::

    The Brand account must be a **Publisher** under `Manage Users and their roles <https://dashboard.snapcraft.io/dev/store/\<CUSTOMER-STORE-ID\>/permissions/>`__ to register and publish the gadget snap.

Logged in as the **Store Administrator** (benefiting of its **Reviewer** permission in this setup), access the `reviews page <https://dashboard.snapcraft.io/reviewer/\<CUSTOMER-STORE-ID\>/>`_ and **Approve** the gadget revision. All gadget uploads require manual review.

Once the revision is approved, use snapcraft to release it in the stable channel:

.. terminal::
    :input: snapcraft whoami

    email:        <CUSTOMER-BRAND-EMAIL>
    developer-id: <CUSTOMER-BRAND-ACCOUNT-ID>

    :input: snapcraft release <CUSTOMER-STORE-PREFIX> 1 stable
    Track    Arch    Channel    Version    Revision
    latest   all     stable     20-0.1  1
                     candidate  ^          ^
                     beta       ^          ^
                     edge       ^          ^
    The 'stable' channel is now open.

The gadget snap is now available for installation from the ``<CUSTOMER-STORE-NAME>`` stores, and for inclusion in images.

Creating a gadget snap for Ubuntu Classic image
***********************************************

.. terminal::
    :input: sudo apt-get install git

    :input: git clone -b classic https://git.launchpad.net/~lyoncore-team/lyoncore-snaps/+git/pc-amd64-gadget \
      <CUSTOMER-STORE-PREFIX>-classic
    :input: cd <CUSTOMER-STORE-PREFIX>-classic

Update "name" field in the ``snapcraft.yaml`` to "``<CUSTOMER-STORE-PREFIX>``-classic" and “base” field in the snapcraft.yaml to “core20”. Feel free to also adjust the "version", "summary" and "description" to be more meaningful in your context. Update "<volume name>:" field in ``gadget.yaml`` from "pc:" to "``<CUSTOMER-DEVICEVIEW-ALIAS>:``".

Build the snap informing the model **API Key** generated during the Serial Vault setup above:

.. terminal::
    :input: SNAPCRAFT_BUILD_ENVIRONMENT=host MODEL_APIKEY=<API-key-for-model-from-serial-vault> snapcraft

    …
    Snapped <CUSTOMER-STORE-PREFIX>-classic_0.1_amd64.snap

.. note::

    The sample “product_serial” is loosely generated (``date -Is``) in this gadget. In production the serial number should be derived from a value inserted during the factory process, or from a unique hardware identifier, for uniqueness and traceability.

Now register the snap name in the target store and push the initial revision:

.. terminal::
    :input: snapcraft whoami

    email:        <CUSTOMER-BRAND-EMAIL>
    developer-id: <CUSTOMER-BRAND-ACCOUNT-ID>

    :input: snapcraft register <CUSTOMER-STORE-PREFIX>-classic --store <CUSTOMER-STORE-ID>
    ...
    you, and be the software you intend to publish there? [y/N]: y
    Registering <CUSTOMER-STORE-PREFIX>-classic.
    Congrats! You are now the publisher of '<CUSTOMER-STORE-PREFIX>-classic'.

    :input: snapcraft upload <CUSTOMER-STORE-PREFIX>-classic_0.1_amd64.snap
    ...
    The Store automatic review failed.
    A human will soon review your snap, but if you can't wait please write in the snapcraft forum asking for the manual review explicitly.
    If you need to disable confinement, please consider using devmode, but note that devmode revision will only be allowed to be released in edge and beta channels.
    Please check the errors and some hints below:
      - (NEEDS REVIEW) type 'gadget' not allowed

.. note::

    The Brand account must be a  Publisher in the Manage Users and their roles for registering and publishing the gadget snap.

Logged in as the **Store Administrator** (benefiting of its **Reviewer** permission in this setup), access the reviews page and **Approve** the gadget revision. All gadget uploads require manual review.

Once the revision is approved, use snapcraft to release it in the stable channel:

.. terminal::
    :input: snapcraft whoami

    email:        <CUSTOMER-BRAND-EMAIL>
    developer-id: <CUSTOMER-BRAND-ACCOUNT-ID>

    :input: snapcraft release <CUSTOMER-STORE-PREFIX>-classic <REVISION-NUMBER>1 stable
    Track    Arch    Channel    Version    Revision
    latest   all     stable     0.1        1
                     candidate  ^          ^
                     beta       ^          ^
                     edge       ^          ^
    The 'stable' channel is now open.


The gadget snap is now available for installation from the ``<CUSTOMER-STORE-NAME>`` stores, and for inclusion in images.

Creating model assertions for Ubuntu Core and Classic images
------------------------------------------------------------

The ``<CUSTOMER-DEVICEVIEW-NAME>`` device view is the target of the ``<CUSTOMER-MODEL-NAME>`` model and has to be populated with the snaps applicable to these devices.

Logged in as the **Store Administrator**, access the `View and manage snaps <https://snapcraft.io/admin>`_ page and include appropriate additional snaps (e.g., pc-kernel and hello) from Global store required in ``<CUSTOMER-MODEL-NAME>`` model. Core and snapd packages are included automatically  and cannot be removed.

.. image:: /images/core-20-model-assertion.png

Creating a model assertion for Ubuntu Core
******************************************

Access the snap page https://dashboard.snapcraft.io/snaps/SNAPNAME to get the snap-id and fill the fields ``<CUSTOMER-SNAP-IDS>`` and ``<CUSTOMER-REQUIRED-SNAPS>``.

.. image:: /images/core-20-model-assertion-core.png

Create and sign the model assertion for Ubuntu Core image:

.. terminal::
    :input: cat << EOF > <CUSTOMER-DEVICEVIEW-ALIAS>-model.json

    {
    "type": "model",
    "authority-id": "<CUSTOMER-BRAND-ACCOUNT-ID>",
    "brand-id": "<CUSTOMER-BRAND-ACCOUNT-ID>",
    "series": "16",
    "model": "<CUSTOMER-MODEL-NAME>",
    "store": "<CUSTOMER-DEVICEVIEW-ID>",
    "architecture": "amd64",
    "base": "core<CUSTOMER-UBUNTU-CORE-VERSION>",
    "grade": "signed",
    "snaps": [
        {
        "default-channel": "latest/stable",
        "id": "<CUSTOMER-SNAP-IDS>",
        "name": "<CUSTOMER-STORE-PREFIX>",
        "type": "gadget"
        },
        {
        "default-channel": "20/beta",
        "id": "pYVQrBcKmBa0mZ4CCN7ExT6jH8rY1hza",
        "name": "pc-kernel",
        "type": "kernel"
        },
        {
        "default-channel": "latest/beta",
        "id": "DLqre5XGLbDqg9jPtiAhRRjDuPVa5X1q",
        "name": "core20",
        "type": "base"
        },
        {
        "default-channel": "latest/beta",
        "id": "PMrrV4ml8uWuEUDBT8dSGnKUYbevVhc4",
        "name": "snapd",
        "type": "snapd"
        },
        {
        "default-channel": "latest/stable",
        "id": "<CUSTOMER-SNAP-IDS>",
        "name": "<CUSTOMER-REQUIRED-SNAPS>",
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

    :input: cat <CUSTOMER-DEVICEVIEW-ALIAS>-model.json | snap sign -k model &> <CUSTOMER-DEVICEVIEW-ALIAS>-model.assert


.. note::
    
    The timestamp for model assertion MUST be after the date of the model signing key being registered by snapcraft.

Creating a model assertion for Ubuntu Classic image
***************************************************

Fill the field ``<CUSTOMER-REQUIRED-SNAPS>`` with the required snaps (e.g., hello). Create and sign the model assertion for Ubuntu Classic image:

.. terminal::
    :input: cat << EOF > <CUSTOMER-DEVICEVIEW-ALIAS>-classic-model.json

    {
    "type": "model",
    "authority-id": "<CUSTOMER-BRAND-ACCOUNT-ID>",
    "brand-id": "<CUSTOMER-BRAND-ACCOUNT-ID>",
    "series": "16",
    "model": "<CUSTOMER-MODEL-NAME>",
    "store": "<CUSTOMER-DEVICEVIEW-ID>",
    "architecture": "amd64",
    "classic": "true",
    "gadget": "<CUSTOMER-STORE-PREFIX>-classic",
    "required-snaps": ["core20", "<CUSTOMER-REQUIRED-SNAPS>"],
    "timestamp": "$(date +%Y-%m-%dT%TZ)"
    }
    EOF

    :input: snapcraft list-keys
        Name          SHA3-384 fingerprint
    *   serial        <fingerprint>
    *   model         <fingerprint>

    :input: cat <CUSTOMER-DEVICEVIEW-ALIAS>-classic-model.json | snap sign -k model &> <CUSTOMER-DEVICEVIEW-ALIAS>-classic-model.assert


.. note::
    
    The timestamp for model assertion MUST be after the date of the model signing key being registered by snapcraft.

**Troubleshooting:** When you sign the model assertion, you could get the following error message due to the locked gpg-agent.

.. terminal::
    :input: cat <CUSTOMER-DEVICEVIEW-ALIAS>-model.json | snap sign -k model &> <CUSTOMER-DEVICEVIEW-ALIAS>-model.assert

    error: cannot sign assertion: cannot sign using GPG: /usr/bin/gpg --personal-digest-preferences SHA512 --default-key <my key> --detach-sign failed: exit status 2 ("gpg: signing failed: No such file or directory\ngpg: signing failed: No such file or directory\n")


Please unlock gpg-agent by following commands and then sign model assertions again.

.. terminal::
    :input: touch test.txt

    :input: gpg --homedir ~/.snap/gnupg --detach-sign --default-key model test.txt

Switching to a developer account
--------------------------------

The next steps will take you through the building of an image. The image build process requires that the Account running the build tools have “Viewer” access permissions to the Device View Store.

Note that once the model is signed by the *Brand* account, there is no need to continue to use such powerful credentials. We recommend not adding “Viewer” permissions to the Brand Account, and switching to a developer account to seed images.

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
_____________________________

This section describes the details of Ubuntu Core image building against the ``<CUSTOMER-DEVICEVIEW-NAME>`` store.

Ensure a Linux build environment (Ubuntu 20.04 or later) and tool for building images are available:

.. terminal::
    :input: sudo snap install ubuntu-image --classic

    ...

Ubuntu Core image is built in the one line instruction by using the above developer account credential:

.. terminal::
    :input: sudo UBUNTU_STORE_AUTH_DATA_FILENAME=./store.auth ubuntu-image snap <CUSTOMER-DEVICEVIEW-ALIAS>-model.assert

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

This is the best outcome — it means that Ubuntu Core will run fast on the system, taking advantage of hardware acceleration from the CPU.

Now launch a virtual machine with KVM, using the following command:

.. terminal::
    :input: qemu-img resize -f raw <CUSTOMER-DEVICEVIEW-ALIAS>.img +3G

    :input: sudo qemu-system-x86_64 -smp 2 -m 2048 -net nic,model=virtio -net user,hostfwd=tcp::8022-:22,hostfwd=tcp::8090-:80 -drive file=/usr/share/OVMF/OVMF_CODE.fd,if=pflash,format=raw,unit=0,readonly=on -drive file=<CUSTOMER-DEVICEVIEW-ALIAS>.img,cache=none,format=raw,id=disk1,if=none -device virtio-blk-pci,drive=disk1,bootindex=1 -machine accel=kvm


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

User name is the Ubuntu SSO user name, shown to you at the end of the account configuration step. Login and then verify if the seeded snaps are installed, the ``<CUSTOMER-MODEL-NAME>`` ``model`` is correct and a ``serial`` assertion was obtained:

.. code:: text

    Welcome to Ubuntu 20.04 LTS (GNU/Linux 5.4.0-33-generic x86_64)

    The programs included with the Ubuntu system are free software;
    the exact distribution terms for each program are described in the
    individual files in /usr/share/doc/*/copyright.

    Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
    applicable law.

    * Ubuntu Core:     https://www.ubuntu.com/core
    * Community:       https://forum.snapcraft.io
    * Snaps:           https://snapcraft.io

    This Ubuntu Core 20 machine is a tiny, transactional edition of Ubuntu,
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

    Name       Version        Rev    Tracking     Publisher   Notes
    <CUSTOMER-STORE-PREFIX>   20-0.1        1     stable     <CUSTOMER-BRAND-ACCOUNT-ID>  gadget
    core20     20             696    latest/beta  canonical✓  base
    hello      2.10           38     stable       canonical✓  -
    pc-kernel  5.4.0-33.37.1  515    20/beta      canonical✓  kernel
    snapd      2.48           10238  latest/beta  canonical✓  snapd

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

Ensure a Linux build environment (Ubuntu 20.04 or later), tools for mounting, and launching images are available:

.. terminal::
    :input: sudo apt install qemu-system-x86 cloud-image-utils kpartx qemu-kvm

    ...

Create a ``user.img`` partition with basic ``cloud-init`` configuration for launching an image:

.. terminal::
    :input: cat << EOF > user-data

    #cloud-config
    password: <a-password-for-the-image-ubuntu-account>
    chpasswd: { expire: False }
    ssh_pwauth: True
    EOF

    :input: cloud-localds -v user.img user-data
    wrote user.img with filesystem=iso9660 and diskformat=raw


Download the Focal (20.04) classic cloud image and verify it is unmodified:

.. terminal::
    :input: wget https://cloud-images.ubuntu.com/releases/focal/release/ubuntu-20.04-server-cloudimg-amd64.img
    
    …
    :input: sha256sum https://cloud-images.ubuntu.com/releases/focal/release/SHA256SUMS


Mount the image so it can be modified 'in-place':

.. terminal::
    :input: rm -f ubuntu-seeded.img && \

    cp ubuntu-20.04-server-cloudimg-amd64.img ubuntu-seeded.img && \
    mkdir -p /tmp/img && \
    sudo modprobe nbd && sleep 1 && \
    sudo qemu-nbd --connect=/dev/nbd0 ubuntu-seeded.img && sleep 1 && \
    sudo kpartx -a /dev/nbd0 && sleep 1 && \
    sudo mount /dev/mapper/nbd0p1 /tmp/img


Seed the required snaps for the ``<CUSTOMER-MODEL-NAME>`` model, and optionally extra ones, into the image mounted in ``/tmp/img``:

.. terminal::
    :input: sudo /usr/lib/snapd/snap-preseed --reset /tmp/img/

    :input: sudo rm -r /tmp/img/var/lib/snapd
    :input: sudo \
    UBUNTU_STORE_ID=<CUSTOMER-DEVICEVIEW-ID> \
    UBUNTU_STORE_AUTH_DATA_FILENAME=./store.auth \
    snap prepare-image --classic \
    <CUSTOMER-DEVICEVIEW-ALIAS>-classic-model.assert \
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

The snap seeding process and ``cloud-init`` configuration take a few minutes. Wait until the following syslog message is displayed:

.. code:: text
    
    [  OK  ] Reached target Cloud-init target.


Login as "``ubuntu``" using the password defined in the ``cloud-init`` configuration above. Verify the seeded snaps are installed, the ``<CUSTOMER-MODEL-NAME>`` ``model`` is correct and a serial assertion was obtained:

.. code:: text

    Welcome to Ubuntu 20.04.1 LTS (GNU/Linux 5.4.0-54-generic x86_64)

    * Documentation:  https://help.ubuntu.com
    * Management:     https://landscape.canonical.com
    * Support:        https://ubuntu.com/advantage

    System information as of Tue Nov 24 13:32:07 UTC 2020

    System load:           0.2
    Usage of /:            67.7% of 1.96GB
    Memory usage:          13%
    Swap usage:            0%
    Processes:             112
    Users logged in:       1
    IPv4 address for ens5: 10.0.2.15
    IPv6 address for ens5: fec0::5054:ff:fe12:3456

    0 packages can be updated.
    0 updates are security updates.
    …

.. terminal::
    :user: ubuntu
    :host: ubuntu
    :input: snap list

    Name                    Version    Rev   Tracking    Publisher     Notes
    <CUSTOMER-STORE-PREFIX>-classic  1.0        1     stable    <CUSTOMER-BRAND-ACCOUNT-ID>  gadget
    core                    20         696   latest/beta canonical✓    base
    hello                   2.10       38    stable      canonical✓    -

    :input: snap changes
    ID   Status  Spawn               Ready               Summary
    1    Done    today at 13:29 UTC  today at 13:29 UTC  Initialize system state
    2    Done    today at 13:29 UTC  today at 13:29 UTC  Initialize device

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
