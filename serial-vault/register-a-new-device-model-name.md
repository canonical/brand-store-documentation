(register-a-new-device-model-name)=
# Register a new device model name

When you build an image, you provide a Model Assertion that defines the devices running the image. For example, the Model Assertion defines the devices as part of your Brand. Here, you create a corresponding Model definition in the Serial Vault.

Note: Both the Serial Vault Model configuration and the Model Assertion (created later) must use the same Model name.

Log in to the [Serial Vault](https://serial-vault-admin.canonical.com/) with the Administrator account. Select the Models section at the top, click the ![plus icon|69x50, 50%](/images/plus-icon.png){.test h=1em} button to create a new model.

![new model|690x537, 100%](/images/register-new-device-model-name1.png) 

The Brand field is pre-populated with your Brand account ID and is uneditable.

Enter the desired model name in the Model field. The name you enter here must be the same as used on your Model Assertions that you will create

For Serial Assertion Key, select the reference for an already uploaded serial key

For System-User Assertion Key, select a key that will be used for system-user generation. In production, you should create and use a dedicated key for the system-user.

The API Key field can be left blank. Its value is generated after the form is submitted. The API Key is used in the creation of a gadget snap that can be included in a factory image. The generated API Key can be retrieved from the edit model menu by pressing the pencil icon as shown below.

![models|690x280](/images/register-new-device-model-name2.png) 

![edit model|637x616, 75%](/images/register-new-device-model-name3.png)
