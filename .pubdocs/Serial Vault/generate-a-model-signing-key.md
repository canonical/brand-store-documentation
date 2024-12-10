(generate-a-model-signing-key)=
#  Generate a model signing key

To sign model assertions you will need to create and register a model signing key. The procedure is similar to generating a serial signing key locally.

Logged in as the Brand account in snapcraft and in the same home directory used before for generating the serial key for the Brand account, create and register a new key named ```model```. This will be used exclusively to sign model assertions.

Usually the model key is not uploaded to the Serial Vault. However, some advanced Serial Vault functionality does involve uploading a model key, so you may want to upload this or another registered model signing key to the Serial Vault later.

## Verify you are logged into snapcraft as the Brand Account

Use ```snapcraft whoami``` to verify you are logged on as the Brand account:
```text
$ snapcraft whoami
email:        <YOUR-BRAND-EMAIL>
developer-id: <YOUR-BRAND-ACCOUNT-ID>
```
## Create the model signing key

Create a key named model, and verify it is created and not yet registered,

**The model key must have a passphrase.**

```text
$ snapcraft create-key model
Passphrase: ...      # Passphrase is needed
Confirm passphrase: ...

$ snapcraft list-keys
    Name          SHA3-384 fingerprint
*   serial        <fingerprint>
*   model         <fingerprint> (not registered)
```

## Register the model key

Register the key providing the Brand Account credentials, and verify it is registered. The key will not function if another account is specified. This is by design in order to ensure the Brand Account’s scope of authority. 
```text
$ snapcraft register-key model
[ . . . ]

$ snapcraft list-keys
    Name          SHA3-384 fingerprint
*   serial        <fingerprint>
*   model         <fingerprint>
```
