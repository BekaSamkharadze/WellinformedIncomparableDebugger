import boto3


def set_object_access_policy(aws_s3_client, bucket_name, file_name):
  # set the Lifecycle configuration for the S3 bucket
  lifecycle_configuration = {
    'Rules': [{
      'Expiration': {
        'Days': 120,
      },
      'Status': 'Enabled',
      'Prefix': file_name
    }]
  }
  aws_s3_client.put_bucket_lifecycle_configuration(
    Bucket=bucket_name, LifecycleConfiguration=lifecycle_configuration)

  # set the object access policy for the S3 object
  response = aws_s3_client.put_object_acl(ACL="public-read",
                                          Bucket=bucket_name,
                                          Key=file_name)
  status_code = response["ResponseMetadata"]["HTTPStatusCode"]
  if status_code == 200:
    return True
  return False
