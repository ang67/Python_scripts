#!/bin/bash

# Prompt for the image and tag if not provided
read -p "Enter the image and tag (e.g., your-image:your-tag): " IMAGE_NAME_TAG
while [[ -z "$IMAGE_NAME_TAG" ]]; do
    echo "Image and tag cannot be empty. Please try again."
    read -p "Enter the image and tag (e.g., your-image:your-tag): " IMAGE_NAME_TAG
done

# List deployments with name 'nginx-controller' in all namespaces
deployments=$(kubectl get deployments --all-namespaces --field-selector metadata.name=nginx-controller --output json)

# Iterate over deployments and ask for confirmation before patching
echo "$deployments" | jq -r '.items[] | select(.spec.template.spec.containers[0].image != null) | select(.spec.template.spec.containers[0].image | contains(":1.")) | [.metadata.namespace, .spec.template.spec.containers[0].image] | @tsv' |
while IFS=$'\t' read -r namespace image; do
    image_name="${image%%:*}"
    image_tag="${image#*:}"
    echo "Namespace: $namespace"
    echo "Image: $image_name"
    echo "Tag: $image_tag"
    read -p "Patch this deployment? (y/n): " confirm
    if [[ $confirm =~ ^[Yy]$ ]]; then
        kubectl patch deployment -n "$namespace" nginx-controller --type='json' -p='[{"op": "replace", "path": "/spec/template/spec/containers/0/image", "value": "'"$IMAGE_NAME_TAG"'"}]'
        echo "Deployment patched successfully."
    else
        echo "Skipping deployment patch."
    fi
    echo
done
