# Import modules
import groupdocs_editor_cloud
from Common import Common

#  This example demonstrates how to edit word processing document
class EditWordProcessingDocument:
    @classmethod  
    def Run(cls):
        # Create necessary API instances
        editApi = groupdocs_editor_cloud.EditApi.from_keys(Common.app_sid, Common.app_key)
        fileApi = groupdocs_editor_cloud.FileApi.from_keys(Common.app_sid, Common.app_key)

        # The document already uploaded into the storage.
        # Load it into editable state
        fileInfo = groupdocs_editor_cloud.FileInfo("WordProcessing/password-protected.docx", None, None, "password")
        loadOptions = groupdocs_editor_cloud.WordProcessingLoadOptions()
        loadOptions.file_info = fileInfo
        loadOptions.output_path = "output"
        loadResult = editApi.load(groupdocs_editor_cloud.LoadRequest(loadOptions))        
        
        # Download html document
        htmlFile = fileApi.download_file(groupdocs_editor_cloud.DownloadFileRequest(loadResult.html_path))
        html = ""        
        with open(htmlFile, 'r') as file:
            html = file.read()

        # Edit something...    
        html = html.replace("Sample test text", "Hello world")

        # Upload html back to storage
        with open(htmlFile, 'w') as file:
            file.write(html)
        
        fileApi.upload_file(groupdocs_editor_cloud.UploadFileRequest(loadResult.html_path, htmlFile))

        # Save html back to docx
        saveOptions = groupdocs_editor_cloud.WordProcessingSaveOptions()
        saveOptions.file_info = fileInfo
        saveOptions.output_path = "output/edited.docx"
        saveOptions.html_path = loadResult.html_path
        saveOptions.resources_path = loadResult.resources_path
        saveResult = editApi.save(groupdocs_editor_cloud.SaveRequest(saveOptions))

        # Done
        print("Document edited: " + saveResult.path)
        