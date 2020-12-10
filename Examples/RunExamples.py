# Import modules
import groupdocs_editor_cloud
from Common import Common

# Get your ClientId and ClientSecret at https://dashboard.groupdocs.cloud (free registration is required).
Common.client_id = "XXXX-XXXX-XXXX-XXXX"
Common.client_secret = "XXXXXXXXXXXXXXXXX"
Common.myStorage = "First Storage"

print("Executing UploadSampleFiles...")
Common.UploadSampleFiles()

print("Executing example GetSupportedFileTypes")
from GetSupportedFileTypes import GetSupportedFileTypes
GetSupportedFileTypes.Run()

print("Executing example GetInfo")
from GetInfo import GetInfo
GetInfo.Run()

print("Executing example EditWordProcessingDocument")
from EditOperations.EditWordProcessingDocument import EditWordProcessingDocument
EditWordProcessingDocument.Run()

print("Executing example EditSpreadsheetDocument")
from EditOperations.EditSpreadsheetDocument import EditSpreadsheetDocument
EditSpreadsheetDocument.Run()

print("Executing example EditPresentationDocument")
from EditOperations.EditPresentationDocument import EditPresentationDocument
EditPresentationDocument.Run()

print("Executing example EditDsvDocument")
from EditOperations.EditDsvDocument import EditDsvDocument
EditDsvDocument.Run()

print("Executing example EditTextDocument")
from EditOperations.EditTextDocument import EditTextDocument
EditTextDocument.Run()
