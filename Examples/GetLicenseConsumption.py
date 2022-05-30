# Import modules
import groupdocs_editor_cloud
from Common import Common

# This example demonstrates how to get metered license consumption info
class GetLicenseConsumption:
    @classmethod  
    def Run(cls):
        licenseApi = groupdocs_editor_cloud.LicenseApi.from_config(Common.GetConfig())
        result = licenseApi.get_consumption_credit()
        print("Credits = " + str(result.credit))