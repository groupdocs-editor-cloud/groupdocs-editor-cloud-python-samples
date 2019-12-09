# Import modules
import groupdocs_editor_cloud
from Common import Common

#  This example demonstrates how to obtain all supported file types
class GetSupportedFileTypes:
    @classmethod  
    def Run(cls):
        infoApi = groupdocs_editor_cloud.InfoApi.from_keys(Common.app_sid, Common.app_key)
        result = infoApi.get_supported_file_formats()
        for format in result.formats:
            print(format.file_format)