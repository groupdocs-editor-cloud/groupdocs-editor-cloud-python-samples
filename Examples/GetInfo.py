# Import modules
import groupdocs_editor_cloud
from Common import Common

# This example demonstrates how to get document info
class GetInfo:
    @classmethod  
    def Run(cls):
        infoApi = groupdocs_editor_cloud.InfoApi.from_config(Common.GetConfig())
        fileInfo = groupdocs_editor_cloud.FileInfo("WordProcessing/password-protected.docx", None, None, "password")
        result = infoApi.get_info(groupdocs_editor_cloud.GetInfoRequest(fileInfo))        
        print("Page count = " + str(result.page_count))