import sagemaker
import boto3
from sagemaker.huggingface import HuggingFaceModel
import os

role = os.environ['ROLE_ARN']

# Hub Model configuration. https://huggingface.co/models
hub = {
	'HF_MODEL_ID':'stabilityai/stable-diffusion-2',
	'HF_TASK':'text-to-image'
}

# create Hugging Face Model Class
huggingface_model = HuggingFaceModel(
	transformers_version='4.37.0',
	pytorch_version='2.1.0',
	py_version='py310',
	env=hub,
	role=role, 
)

# deploy model to SageMaker Inference
predictor = huggingface_model.deploy(
	initial_instance_count=1, # number of instances
	instance_type='ml.m5.xlarge' # ec2 instance type
)

image_bytes = predictor.predict({
	"inputs": "Astronaut riding a horse",
})
# You can access the image with PIL.Image for example
import io
from PIL import Image
image = Image.open(io.BytesIO(image_bytes))

