# Import modules
import groupdocs_editor_cloud
from Common import Common

# This example demonstrates how to edit spreadsheet document
class EditSpreadsheetDocument:
    @classmethod  
    def Run(cls):
        # Create necessary API instances
        editApi = groupdocs_editor_cloud.EditApi.from_config(Common.GetConfig())
        fileApi = groupdocs_editor_cloud.FileApi.from_config(Common.GetConfig())

        # The document already uploaded into the storage.
        # Load it into editable state
        fileInfo = groupdocs_editor_cloud.FileInfo("Spreadsheet/four-sheets.xlsx")
        loadOptions = groupdocs_editor_cloud.SpreadsheetLoadOptions()
        loadOptions.file_info = fileInfo
        loadOptions.output_path = "output"
        loadOptions.worksheet_index = 0
        loadResult = editApi.load(groupdocs_editor_cloud.LoadRequest(loadOptions))        
        
        # Download html document
        htmlFile = fileApi.download_file(groupdocs_editor_cloud.DownloadFileRequest(loadResult.html_path))
        html = ""        
        with open(htmlFile, 'r') as file:
            html = file.read()

        # Edit something...    
        html = html.replace("This is sample sheet", "This is sample sheep")

        # Upload html back to storage
        with open(htmlFile, 'w') as file:
            file.write(html)
        
        fileApi.upload_file(groupdocs_editor_cloud.UploadFileRequest(loadResult.html_path, htmlFile))

        # Save html back to xlsx
        saveOptions = groupdocs_editor_cloud.SpreadsheetSaveOptions()
        saveOptions.file_info = fileInfo
        saveOptions.output_path = "output/edited.xlsx"
        saveOptions.html_path = loadResult.html_path
        saveOptions.resources_path = loadResult.resources_path
        saveResult = editApi.save(groupdocs_editor_cloud.SaveRequest(saveOptions))

        # Done
        print("Document edited: " + saveResult.path)
        