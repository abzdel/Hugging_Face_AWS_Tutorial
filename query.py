import boto3
import io
from PIL import Image
import json
import botocore.session

# Initialize Boto3 SageMaker client
sagemaker_client = boto3.client('sagemaker')
sagemaker_runtime_client = boto3.client('sagemaker-runtime')

# Specify the name of the endpoint
##### CHANGE YOUR ENDPOINT NAME HERE #####
endpoint_name = 'huggingface-inference-endpoint-2'

# Get information about the endpoint
response = sagemaker_client.describe_endpoint(EndpointName=endpoint_name)

# Extract the endpoint ARN from the response
endpoint_arn = response['EndpointArn']

# take user input for prompt
prompt = input("Enter a prompt: ")

data = ({
	"inputs": prompt,
})

# Convert data to JSON string
payload = json.dumps(data)

# Configure the HTTP session with custom timeout
session = botocore.session.get_session()
config = session.create_client('sagemaker-runtime', config=botocore.client.Config(connect_timeout=5, read_timeout=300))

# Send the request to the endpoint for inference
print("Sending request to endpoint...")
response = config.invoke_endpoint(
    EndpointName=endpoint_name,
    Body=payload,
    ContentType='application/json',  # Adjust content type based on your model's requirements
)

# print the response
print(response['Body'].read().decode('utf-8'))

# Save the response body as a text file
print("Saving response to file...")
# export to a text file
with open('response.txt', 'w') as f:
    f.write(response['Body'].read().decode('utf-8'))