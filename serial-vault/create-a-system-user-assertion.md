(create-a-system-user-assertion)=
# Create a system-user assertion

```{note}
This feature has been deprecated. Please see the [updated system-user assertion functionality](https://ubuntu.com/core/docs/system-user).
```

A [system-user assertion](https://ubuntu.com/core/docs/reference/assertions/system-user) allows you to create a user on an unmanaged Ubuntu Core system. The system-user assertion can be pre-populated into an image, or it can be auto-imported from a USB drive. More about the [system user configuration](https://ubuntu.com/core/docs/system-user) can be found in the Ubuntu Core docs.

Through the System-User menu in the Serial Vault you can create a system-user assertion for your brand and model as follows:

1. Click System-User.
2. Enter the email of the system user.
3. Enter the desired login name of the system user in the Username field.
4. Enter the system user password in the Password field.
5. Enter the complete name of the user in the Full Name field.
6. Select the model of the device this user is being created from the Model combo box.
7. Set date and time in UTC since this assertion is valid in Since (UTC) field. This date must be after the date on which the key used to sign the system user assertion was registered.

![system user assertion form|690x420](/images/create-system-user-assertion.png) 

After pressing **Create**, the generated assertion is displayed. Click **Download** to save it to a local file.

You can name this file ```auto-import.assert``` and place it in the root directory of a USB drive. If the USB drive is inserted in an unmanaged Ubuntu Core system, the assertion is imported and a system user is created.
