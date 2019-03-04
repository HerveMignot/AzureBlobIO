import io
import azure.storage

class AzureBlobIO(io.BytesIO):
    """Class to read Azure blobs as a stream, using some buffer.
    """

    def __init__(self, blob_service, container_name, blob_name, snapshot=None, chunksize=None):
        """Build a stream from a blob to stream Azure service call.
        """
        # Init the BytesIO instance
        #super().__init__()
        super()

        self._blob_service = blob_service
        self.container_name = container_name
        self.blob_name = blob_name
        self.snapshot = snapshot

        # Download as a stream
        self._blob = self._blob_service.get_blob_to_stream(self.container_name,
                                                           self.blob_name,
                                                           self,
                                                           self.snapshot)
        self.seek(0)
