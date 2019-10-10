# KACE

## About

[KACE]

<https://www.quest.com/>
Work with KACE SMA.

## Actions

### Lookup Inventory Device

This action looks up a Device in the Inventory Category.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|device_name|string|None|True|Retrieves the Devices Inventory information|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Boolean indicating whether the business object was successfully created|
|system|[]system_inventory|True|The Requested information for the System that was Inputted|

Example output:

```
```

### Refresh System Information

This action refreshes the System Information so that it is up to date.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|device_name|string|None|True|The System to perform the System Refresh on|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Boolean indicating whether the business object was successfully created|
|system|string|True|If the Inventory Refresh was successful or not|

Example output:

```
```

## Triggers

_This plugin does not contain any triggers._

## Connection

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|organization|string|Default|True|KACE organization environment|None|
|ssl_verify|boolean|True|True|Whether to access the server over HTTPS|None|
|url|string|vulcan.hillwood.com|True|Hostname of the KACE Appliance|None|
|username_and_password|credential_username_password|None|True|KACE username and password|None|

## Troubleshooting

_This plugin does not contain any troubleshooting information._

## Workflows

Examples:

* EXAMPLE HERE

## Versions

* 1.0.0 - Initial plugin
* 1.0.1 - Fixed Lookup_Device Connection and added the KACE Icon
* 1.0.3 - Made the Lookup_Device an Object Array for looping through multiple systems
* 1.0.6 - Added 'Refresh System Information' to the Workflow

## References

[KACE]
<https://www.quest.com/>

## Custom Output Types

### system_inventory

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Bios_identification_code|string|False|BIOS Identification Code|
|Cdrom_devices|string|False|CDrom Devices|
|Created|date|False|System Created Date|
|Id|string|False|System ID|
|Ip|string|False|System IP|
|Last_inventory|date|False|Last Inventory Date|
|Last_sync|date|False|Last System Sync|
|Manual_entry|string|False|Manual Entry|
|Modified|date|False|System Modified Date|
|Monitor|string|False|System Monitor|
|Name|string|False|System Hostname|
|Os_name|string|False|OS Name|
|Os_number|string|False|OS Version Number|
|Pagefile_max_size|string|False|Maximum Possible Pagefile of the System|
|Pagefile_size|string|False|Pagefile of the System|
|Ram_Total|string|False|Total Memory Installed|
|Ram_max|string|False|Max Memory for the System|
|Ram_used|string|False|Total Memory Used|
|Registry_max_size|string|False|Maximum Registry Size of the System|
|Registry_size|string|False|Size of the Registry on the System|
|Sound_devices|string|False|Sound Devices|
|User|string|False|Logged in User|
|Video_controllers|string|False|Video Controllers|
