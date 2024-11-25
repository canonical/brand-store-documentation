(device-model-and-identity)=
# Device model and identity

The Serial Vault needs to be configured with the details of the models and signing keys that will be authorised to use the functionality for an account.
![model relationship|689x561, 75%](upload://aS7sqINt7QV0qnWHz0rwJWvPEuS.png) 

The diagram above shows how the different entities relate to each other. The account, model and signing keys all belong to the same Brand, which is the account-id of the Brand in the [store](https://dashboard.snapcraft.io/dev/account/). The ID is shared across the entities, though they may be referred to differently for each entity e.g. brand-id on the model and authority-id on the signing-key.

## Models

Every device is provisioned using an Ubuntu Core image that includes a signed model assertion and [Gadget snap](https://ubuntu.com/core/docs/gadget-snaps). The [model assertion](https://ubuntu.com/core/docs/reference/assertions/model) holds important information related to the identity of the device:

* brand-id: the ID of the Brand
* model: the model name of the device
* store: the ID of the Brand Store
* sign-key-sha3-384: the key ID of the signing key (must be registered with the Brand Store)

An essential part of a device's identity is its serial number. This and that is recorded in the [serial assertion](https://ubuntu.com/core/docs/reference/assertions/serial), rather than the model assertion. The serial and model assertions are used to authenticate the device with the Brand Store. [The connecting new devices page](https://ubuntu.com/core/services/guide/connecting-devices) provides an overview of the onboarding process.

The serial assertion is not a part of the device image, as the serial number will differ from one device to another. Each device retrieves its serial assertion from the Serial Vault. For the Serial Vault to recognize a device as valid, it needs to have a model entity defined for the device. 

The Model entity provides a number of attributes that must match the device (brand-id and model), and an API key that must match that held in the Gadget snap. The model must be associated with a signing key so it can generate and sign a serial assertion.

Models can be added, changed and deleted from the Models section of the Serial Vault. Once a model is added, it is immediately available to provide a signed serial assertion to snapd.
