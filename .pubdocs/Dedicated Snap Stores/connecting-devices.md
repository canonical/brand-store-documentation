(connecting-devices)=
# Connecting new devices

<!-- 
Status: Document is unfocused and does not fit into a Diataxis quadrant
Rewrite: Rework into explanation
 -->

Ubuntu Core devices are onboarded to their owner’s Dedicated Snap Store in a secure manner. Secure onboarding prevents unauthorised access to private software and services. It also establishes a secure communication link between devices and their cloud backend.

Secure device onboarding is a four stage process that starts with a request for serial keys, proceeds with device initiation from the cloud, and ends with device authentication and authorisation. The first two stages are handled by the serial vault which is a service that issues credentials to devices.

![Secure device onboarding four stage process Illustration|690x419](https://assets.ubuntu.com/v1/29944474-19c88fc1e15e2058793f9d8be18ba042603eb2c7_2_690x419.png)

## Device initialisation

The secure onboarding process starts at first boot. When turned on for the first time, an Ubuntu Core device extracts its private key, its serial number, and its owner’s ID from metadata stored in its model assertion. Based on this data, the device will send a request for a serial assertion to its vault, which is hosted either by Canonical or on premise. The vault service processes the request. Had the device’s public key been stored in the vault, a serial assertion is issued as response to the request. The serial assertion issued by the serial vault is then stored on the device.

## Authentication and authorisation

Both the serial and the model assertions will be used by devices to access your Dedicated Snap Store. Devices will use these secure documents to initiate a handshake with your store. The Dedicated Snap Store authenticates the keys and authorises the device for a fixed period of time.

## Helpful information

* [Authentication through the Serial Vault](https://ubuntu.com/core/docs/dedicated-snap-stores#heading--device-authentication)
