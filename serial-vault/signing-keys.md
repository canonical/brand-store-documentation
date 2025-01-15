(signing-keys)=
# Signing keys

The Serial Vault provides encrypted storage for signing keys intended for use with a Dedicated Snap Store. Signing keys can be generated locally and uploaded, and users with Admin permissions can generate keys from within the Serial Vault. A signing key needs to be registered with the Dedicated Snap Store so it can be used to verify the signature of serial assertions. The Serial Vault holds the private key, whereas the Dedicated Snap Store holds only the public key as an account-key assertion.

[note type="important" status="Info"]
The private key of any key pair generated within the Serial Vault cannot be downloaded for local use.  If you wish to sign both model and serial assertions with the same key, ensure the key is generated locally and then uploaded to the Serial Vault.
[/note]

The steps needed with local key generation and registration are:

1. Generating the key(s)
2. Registering the key with the Dedicated Snap Store
    * See [Register a signing key with limited roles](#key-roles) on constraining a key for only certain assertion types
3. Exporting the key as ASCII-armored
4. Uploading the ASCII-armored key file to the Serial Vault

The Serial Vault will need the private keys uploaded to its database for the following keys:

* Key for signing serial assertions
* Key for signing system-user assertions
* (if model pivoting is needed) Key for signing model assertions

Although one key can be used for each of these three purposes, it is recommended to use a separate signing key for each type of assertion.

Signing keys that are to be uploaded to the Serial Vault need to be passwordless (i.e. keeping a blank password when generating the key). Using a key that has a password results in an error when uploading the signing key.

(key-roles)=
## Register a signing key with limited roles

Role-scoped keys are signing keys that are limited to be able to sign only specific assertion types. These limitations can be set when first registering the key with the Dedicated Snap Store. For example, a key can be registered for only signing serial assertions, and can be further constrained to the serial assertions for only certain models. This improves security as it limits the potential impact of a leaked key.

Customers currently cannot register a role-scoped signing key themselves. They must raise a support request as documented below.

A key can be scoped to a single or a combination of the following assertion types:
* Serial
* Model
* System-user
* Preseed

For the serial, model, and preseed assertion types, keys can be further be constrained on model names matching a certain regular expression, e.g. `foo-.*`

[note type="important" status="Info"]
If role-scoped keys are in use, it is recommended to limit the roles of all available keys for increased security.
[/note]

<h3 id='heading--role-scoped-key-instructions'>Procedure for requesting a role-scoped key</h3>

To register a role-scoped key, raise a support request with the Dedicated Snap Store with the following details:

* Account ID of the brand account to which the key would be registered
* Name for the key
* Verbatim base64-encoded output of `snap export-key`, ran against the locally created signing key they wish to register
* Model name constraints for the serial, model, and preseed assertion types, if any

Currently, roles can only be defined for new keys. Once registered, the role(s) of a role-scoped signing key cannot be changed.
