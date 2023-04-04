# Python_scripts

#!/bin/bash

# Set the name of the S3 bucket
BUCKET_NAME="your-bucket-name"

# Set the path to the folder you want to list (optional)
FOLDER_PATH="your-folder-path"

# Set your AWS access key ID and secret access key
AWS_ACCESS_KEY_ID="your-access-key-id"
AWS_SECRET_ACCESS_KEY="your-secret-access-key"

# Generate the URL and list the contents of the folder using curl
URL="https://$BUCKET_NAME.s3.amazonaws.com/?delimiter=/&prefix=$FOLDER_PATH"
DATE=$(date -u +"%a, %d %b %Y %H:%M:%S GMT")
STRING_TO_SIGN="GET\n\n\n${DATE}\n/$BUCKET_NAME/\n$URL"
SIGNATURE=$(echo -en "${STRING_TO_SIGN}" | openssl sha1 -hmac "${AWS_SECRET_ACCESS_KEY}" -binary | base64)
curl -H "Authorization: AWS $AWS_ACCESS_KEY_ID:$SIGNATURE" \
     -H "Date: ${DATE}" \
     $URL
