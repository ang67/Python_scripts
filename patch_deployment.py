import re
from kubernetes import client, config

# Load current Kubernetes context from kubectl config
config.load_kube_config()

# Create an API client
api_client = client.ApiClient()

# Define the regex pattern for the image tag
tag_regex = re.compile(r'^1\.\d+\.\d+$')

# Prompt for the image and tag if not provided
IMAGE_NAME_TAG = input("Enter the image and tag (e.g., your-image:your-tag): ").strip()
while not IMAGE_NAME_TAG:
    print("Image and tag cannot be empty. Please try again.")
    IMAGE_NAME_TAG = input("Enter the image and tag (e.g., your-image:your-tag): ").strip()

# List deployments with name 'nginx-controller' in all namespaces
api_instance = client.AppsV1Api(api_client)
deployments = api_instance.list_deployment_for_all_namespaces(
    field_selector=f'metadata.name=nginx-controller'
).items

# Iterate over deployments and ask for confirmation before patching
for deployment in deployments:
    container = deployment.spec.template.spec.containers[0]
    image_tag = container.image.split(':')[-1]
    if not tag_regex.match(image_tag):
        namespace = deployment.metadata.namespace
        image_name = container.image.split(':')[0]
        print(f"Namespace: {namespace}\nImage: {image_name}\nTag: {image_tag}")
        confirm = input("Patch this deployment? (y/n): ")
        if confirm.lower() == "y":
            try:
                container.image = IMAGE_NAME_TAG
                api_instance.patch_namespaced_deployment(
                    name=deployment.metadata.name,
                    namespace=namespace,
                    body=deployment
                )
                print("Deployment patched successfully.")
            except Exception as e:
                print(f"An error occurred while patching the deployment: {str(e)}")
        else:
            print("Skipping deployment patch.")
        print()
