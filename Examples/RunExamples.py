# Import modules
import groupdocs_editor_cloud
from Common import Common

# Get your app_sid and app_key at https://dashboard.groupdocs.cloud (free registration is required).
Common.app_sid = "XXXX-XXXX-XXXX-XXXX"
Common.app_key = "XXXXXXXXXXXXXXXX"
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
