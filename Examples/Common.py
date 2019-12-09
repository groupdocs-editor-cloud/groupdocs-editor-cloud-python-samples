import groupdocs_editor_cloud
import glob
import os

class Common:

    # Get your app_sid and app_key at https://dashboard.groupdocs.cloud (free registration is required).
    app_sid = None
    app_key = None    
    myStorage = None
    
    @classmethod  
    def UploadSampleFiles(cls):
        
        # api initialization
        storageApi = groupdocs_editor_cloud.StorageApi.from_keys(cls.app_sid, cls.app_key)
        fileApi = groupdocs_editor_cloud.FileApi.from_keys(cls.app_sid, cls.app_key)

        # upload sample files
        for filename in glob.iglob("Resources/**/*.*", recursive=True):
            destFile = filename.replace("Resources\\", "", 1)            
            fileExistsResponse = storageApi.object_exists(groupdocs_editor_cloud.ObjectExistsRequest(destFile))
            if not fileExistsResponse.exists:                                
                fileApi.upload_file(groupdocs_editor_cloud.UploadFileRequest(destFile, filename))
                print("Uploaded file: "+ destFile)
