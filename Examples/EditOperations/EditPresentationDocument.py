# Import modules
import groupdocs_editor_cloud
from Common import Common

# This example demonstrates how to edit presentation document
class EditPresentationDocument:
    @classmethod  
    def Run(cls):
        # Create necessary API instances
        editApi = groupdocs_editor_cloud.EditApi.from_keys(Common.app_sid, Common.app_key)
        fileApi = groupdocs_editor_cloud.FileApi.from_keys(Common.app_sid, Common.app_key)

        # The document already uploaded into the storage.
        # Load it into editable state
        fileInfo = groupdocs_editor_cloud.FileInfo("Presentation/with-notes.pptx")
        loadOptions = groupdocs_editor_cloud.PresentationLoadOptions()
        loadOptions.file_info = fileInfo
        loadOptions.output_path = "output"
        loadOptions.slide_number = 0
        loadResult = editApi.load(groupdocs_editor_cloud.LoadRequest(loadOptions))        
        
        # Download html document
        htmlFile = fileApi.download_file(groupdocs_editor_cloud.DownloadFileRequest(loadResult.html_path))
        html = ""        
        with open(htmlFile, 'r') as file:
            html = file.read()

        # Edit something...    
        html = html.replace("Slide sub-heading", "Hello world!")

        # Upload html back to storage
        with open(htmlFile, 'w') as file:
            file.write(html)
        
        fileApi.upload_file(groupdocs_editor_cloud.UploadFileRequest(loadResult.html_path, htmlFile))

        # Save html back to pptx
        saveOptions = groupdocs_editor_cloud.PresentationSaveOptions()
        saveOptions.file_info = fileInfo
        saveOptions.output_path = "output/edited.pptx"
        saveOptions.html_path = loadResult.html_path
        saveOptions.resources_path = loadResult.resources_path
        saveResult = editApi.save(groupdocs_editor_cloud.SaveRequest(saveOptions))

        # Done
        print("Document edited: " + saveResult.path)
        