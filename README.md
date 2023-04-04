# Python_scripts

#!/bin/bash

# Set the name of the S3 bucket
BUCKET_NAME="your-bucket-name"

# Set the name of the file you want to download
FILE_NAME="your-file-name"

# Set the expiration time for the pre-signed URL (in seconds)
EXPIRATION_TIME=3600

# Set your AWS access key ID and secret access key
AWS_ACCESS_KEY_ID="your-access-key-id"
AWS_SECRET_ACCESS_KEY="your-secret-access-key"

# Generate the URL and download the file using curl
URL="https://$BUCKET_NAME.s3.amazonaws.com/$FILE_NAME"
EXPIRES=$(date -u -d "+$EXPIRATION_TIME seconds" '+%Y-%m-%dT%H:%M:%SZ')
STRING_TO_SIGN="GET\n\n\n$EXPIRES\n/$BUCKET_NAME/$FILE_NAME"
SIGNATURE=$(echo -en "${STRING_TO_SIGN}" | openssl sha1 -hmac "${AWS_SECRET_ACCESS_KEY}" -binary | base64)
SIGNED_URL="$URL?AWSAccessKeyId=$AWS_ACCESS_KEY_ID&Expires=$(echo $EXPIRES | sed 's/:/%3A/g')&Signature=$(echo $SIGNATURE | sed 's/\+/%2B/g' | sed 's/\//%2F/g' | sed 's/=/%3D/g')"
curl -o /path/to/local/file $SIGNED_URL
