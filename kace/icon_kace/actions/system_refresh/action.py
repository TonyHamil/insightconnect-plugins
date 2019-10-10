import komand
from .schema import SystemRefreshInput, SystemRefreshOutput, Component


class SystemRefresh(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='system_refresh',
                description=Component.DESCRIPTION,
                input=SystemRefreshInput(),
                output=SystemRefreshOutput())

    def run(self, params):
        devicelookup = params.get('device_name')

        return self.connection.api.system_refresh(devicelookup)
