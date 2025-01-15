(serial-vault-overview)=
# Serial Vault

![Illustration of the App Store architecture, demonstrating use of a combination of public and private snaps](/images/serial-vault-overview.png)

*The serial vault serves an important function in the management of a dedicated Dedicated Snap Store*


The Serial Vault is a Canonical-hosted multi-tenant web portal offered to customers. Customers may choose to set up their own dedicated Serial Vault service.

The main purpose of the Serial Vault is to provide a signed Serial Assertion to devices, which allows them to authenticate against a dedicated Snap Store. The Serial Vault also enables other functions, such as [remodelling](https://ubuntu.com/core/docs/uc20/remodelling) support.

The Serial Vault provides a user interface and an API to enable a device to receive digitally signed documents([assertions](https://ubuntu.com/core/docs/reference/assertions)) that are used for authentication and authorization. An authenticated device can have access to restricted snaps from a dedicated Snap Store, providing a customised experience to the device owners.

The main assertions that are handled by the Serial Vault are:

* Account Assertion
* Account Key Assertion
* Serial-Request Assertion
* Model Assertion
* Serial Assertion

All of these are used by the device, Serial Vault and dedicated Snap Store to verify and manage the access of a device.

In this section, we will cover a basic overview of the Serial Vault and how it is used.

```{toctree}
:glob:
:hidden:

serial-vault/*

```