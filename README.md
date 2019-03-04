# Azure Blob IO
Wrapper class for reading files stored on Azure Blob storage as ByteIO streams.

## Using Azure Blob IO

See also example in associated notebook.

First, get a connection to Azure service.

    from azure.storage import blob
    blob_service = blob.BlockBlobService(account_name='equancypublic'))

using the right connection string to Azure Blog storage.

Then, files can be read wherever `ByteIO` streams are supported.

    import pandas as pd
    from azureblobio import AzureBlobIO
    
    my_df = pd.read_csv(AzureBlobIO(blob_service, 'datasets', 'titanic.csv'))


## Installation

### Requirements

Install Azure SDK:

    pip install azure

to install the SDK.

### Installation

Use:

    pip install azureblobio

to install the package.


## TO DO

* increase tests range
