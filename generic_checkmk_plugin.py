from .agent_based_api.v1 import * # type: ignore

PLUGIN_NAME = "HP UPS R5500 XR - Battery Status"
SERVICE_NAME = "HP UPS R5500 XR - Battery Status Service"
SNMP_SECTION = "HP UPS R5500 XR - Battery Status SNMP Battery Section"

register.snmp_section( # type: ignore
    name = SNMP_SECTION,
    detect = exists(".1.3.6.1.2.1.33.1.1.1.0"), # type: ignore
    fetch = [
        SNMPTree( # type: ignore
        base = '.1.3.6.1.2.1.33.1.2',
        oids = ['4']
        )
    ]
)

def discovery_powerware_r5500_xr(section):
    yield Service() # type: ignore

def check_powerware_r5500_xr(section):
    pass

register.check_plugin( # type: ignore
    name=PLUGIN_NAME,
    service_name=SERVICE_NAME,
    discovery_function = discovery_powerware_r5500_xr,
    check_function = check_powerware_r5500_xr,
    check_default_parameters={},
)