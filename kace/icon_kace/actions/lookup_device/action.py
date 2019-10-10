import komand
from .schema import LookupDeviceInput, LookupDeviceOutput, Component


class LookupDevice(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='lookup_device',
            description=Component.DESCRIPTION,
            input=LookupDeviceInput(),
            output=LookupDeviceOutput())

    def run(self, params):
        devicelookup = params.get('device_name')

        return self.connection.api.machine_inventory(devicelookup)

#        return {
#            "search_results": response
#        }
