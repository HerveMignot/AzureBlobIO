# -*- coding: utf-8 -*-
import pytest

"""
Test reading simple csv file on public blob storage.
"""

import pandas as pd
from azure.storage import blob

from azureblobio import AzureBlobIO

def test_azureblobio():
    blob_service = blob.BlockBlobService(account_name='equancypublic')
    titanic_df = pd.read_csv(AzureBlobIO(blob_service, 'datasets', 'titanic.csv'))
    assert titanic_df.shape[0] == 1309
