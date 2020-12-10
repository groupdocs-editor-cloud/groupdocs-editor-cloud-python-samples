import groupdocs_editor_cloud
import glob
import os

class Common:

    # This properties are set from main class
    client_id = None
    client_secret = None 
    myStorage = None
    
    @classmethod  
    def GetConfig(cls):
        configuration = groupdocs_editor_cloud.Configuration(cls.client_id, cls.client_secret)
        configuration.api_base_url = "https://api.groupdocs.cloud"
        return configuration   

    @classmethod  
    def UploadSampleFiles(cls):
        
        # api initialization
        storageApi = groupdocs_editor_cloud.StorageApi.from_config(cls.GetConfig())
        fileApi = groupdocs_editor_cloud.FileApi.from_config(cls.GetConfig())

        # upload sample files
        for filename in glob.iglob("Resources/**/*.*", recursive=True):
            destFile = filename.replace("Resources\\", "", 1)            
            fileExistsResponse = storageApi.object_exists(groupdocs_editor_cloud.ObjectExistsRequest(destFile))
            if not fileExistsResponse.exists:                                
                fileApi.upload_file(groupdocs_editor_cloud.UploadFileRequest(destFile, filename))
                print("Uploaded file: "+ destFile)
