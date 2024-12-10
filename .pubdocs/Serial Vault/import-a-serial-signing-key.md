(import-a-serial-signing-key)=
# Import a serial signing key

### Uploading the key to the Serial Vault

The ASCII-armored file can be uploaded to the Serial Vault. To import the serial signing key, Log in to the Serial Vault with the Administrator account. Select the Signing Keys section at the top, and click the ![plus icon|69x50, 50%](upload://tGkdd69CxHPqepc1a3RvdzNpVbA.png)  button to import a signing key. Note that the Serial Vault cannot be logged in via the Brand Account.

![import signing key|690x316](upload://jP4latuZDSetjEGzeXWEJUdMfAW.png) 

Enter ```serial``` in the Key Name field as shown in the screenshot above.

In the Signing Authority field, select the account ID of the Brand Account. This is the same value as the ```developer-id``` displayed by ```snapcraft whoami``` when you are logged into snapcraft as the Brand Account.

Click **Choose File**, and browse to and select the serial.asc file on your local system as created above.

Click **Save** to complete the upload.

## Backing up and protecting keys

The signing keys that have been generated are an essential part of verifying the authenticity of a device at the Dedicated Snap Store. So these keys need to be protected and backed up. They are stored by default in ```~/.snap/gnupg``` on the current machine.

Whilst the Serial Vault does hold the private key (encrypted in the database), it does not provide a mechanism to download a signing key. The Dedicated Snap Store only has the public part of the key. So it is important to ensure that the generated keys are backed up.
