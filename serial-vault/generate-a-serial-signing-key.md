(generate-a-serial-signing-key)=
# Generate a serial signing key

To proceed, you need to generate a signing key as the Brand Account. This will be uploaded to the Serial Vault and used to sign Serial Assertions. The key must abide by the following conditions:

* This key must be generated and registered as the Brand Account
* This key must be passwordless

As a note, generating the key takes some time. Moving the mouse or typing can help to speed up the process, as does installing the `rng-tools` Debian package beforehand.
`
In this next step, do not enter a passphrase for this key when prompted. This special key is used exclusively for providing devices access to the store and must be passwordless. When prompted in the terminal, or if a pop-up displays, do not enter text as a Passphrase and do not enter text to Confirm it. If you do, this key does not function to sign Serial Assertions.

```bash
$ snapcraft create-key serial
Passphrase:  # must be a passwordless key, so press Enter twice
Confirm passphrase:

[ . . . ]
```

## Register a serial signing key

Now you can register the serial key. As prompted, enter the credentials for the Brand Account. The key does not function if another account is specified. This is by design in order to ensure the Brand Account’s scope of authority.

```sh
$ snapcraft register-key serial

[ . . . ]
```

## Verify the serial key exists

Use `snapcraft list-keys` to verify a key named serial exists.
```text
$ snapcraft list-keys
    Name          SHA3-384 fingerprint
*   serial        <fingerprint>
```

## Armor the serial key

Export the serial key as an armored file so that it can be safely uploaded to the Serial Vault, as follows:
```text
$ gpg --homedir ~/.snap/gnupg --armor --export-secret-key serial > serial.asc
```
You should now have a `serial.asc` file registered that can be imported to the Serial Vault.
