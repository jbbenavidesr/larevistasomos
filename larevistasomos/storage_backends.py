from storages.backends.s3boto3 import S3Boto3Storage

class Media Storage(S3Boto3Storage):
    location = 'media'
    