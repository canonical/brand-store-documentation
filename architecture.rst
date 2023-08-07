Store Architecture
==================

A Snap Store is a repository for hosting and publishing snaps so that they can be consumed by snapd-enabled devices.

There are several Snap Store instances that will be relevant to you. To understand these instances, and the relationship between them, please read:
Snap Store vs Brand Store
Base Stores and Device View Stores

Your Base Snap Store is:  <CUSTOMER-STORE-NAME> (<CUSTOMER-STORE-ID>)

Your Device View Snap Store is: <CUSTOMER-DEVICEVIEW-NAME> (<CUSTOMER-DEVICEVIEW-ID>) 

Your Device View Store is configured:
to automatically include all snaps from <STORES-WITH-WHOLESALE-INCLUSION>
to include a specific set of snaps from <STORES-WITH-CURATED-INCLUSION>

<PREPARER NOTE> (Please remove after edits) - a Device View Store can be configured to include snaps from other Brand Stores, or the Global Store via the Store inclusion feature. A Device View Store can include another Store wholesale (i.e. all snaps from the other store are now available) or in Curated mode, which then allows an admin to selectively include snaps from the included store. Please replace the two <STORES-WITH-{CURATED,WHOLESALE}-INCLUSION> fields with text based upon the initial Store inclusion configuration requested by the customer. If one of the two tags has no stores (e.g. the Device View Store is configured so that it does not wholesale include any store) replace it with the text “no stores”. The most common scenario will be one Base Store and one Device View Store, with wholesale inclusion of the Base Store by the Device View Store, and the curated inclusion of no stores by the Device View Store.

All stores (including your Device View Snap Store) always include the snapd snap, as well as the LTS-versioned Core snaps (i.e. core18, core20, core22).

⚠ Note: If and when your organization decides to create additional models, please ensure that you first request and use a new Device View Store for each new model. This can be done by opening a support ticket via your support portal. Using a single Device View Store per model allows for better isolation between your various models and ensures that potential changes to the inclusion rules for one model don't impact other models which may already be in use in production.