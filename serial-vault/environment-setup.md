(environment-setup)=
# Environment setup

It is recommended that [Ubuntu desktop](https://ubuntu.com/download/desktop) is used for the creation and management of signing keys.

## Install snapcraft and login as the brand

Snapcraft is usually pre-installed. If it is not, you can install it as follows:
```bash
sudo snap install snapcraft --classic
```
Login to snapcraft as the Brand Account:

```bash
$ snapcraft login
Enter your Ubuntu One Email address and password.
If you do not have an Ubuntu One account, you can create one at https://snapcraft.io/account
Email: <YOUR-BRAND-EMAIL>
Password: ******

Login successful.

$ snapcraft whoami
email:        <YOUR-BRAND-EMAIL>
developer-id: <YOUR-BRAND-ACCOUNT-ID>
```
Now you should be logged in with the Brand Account.
