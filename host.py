import sagemaker
import boto3
from sagemaker.huggingface import HuggingFaceModel
import os
import json

role = os.environ['ROLE_ARN']

# Hub Model configuration. https://huggingface.co/models
hub = {
	'HF_MODEL_ID':'distilbert/distilgpt2',
	'SM_NUM_GPUS': json.dumps(1)
}

print("Creating Model")
# create Hugging Face Model Class
huggingface_model = HuggingFaceModel(
	transformers_version='4.37.0',
	pytorch_version='2.1.0',
	py_version='py310',
	env=hub,
	role=role, 
)

print("Deploying to SageMaker")
# deploy model to SageMaker Inference
predictor = huggingface_model.deploy(
	initial_instance_count=1, # number of instances
	instance_type='ml.m5.xlarge', # ec2 instance type
	endpoint_name='huggingface-inference-endpoint-2'  # Name of the endpoint

)