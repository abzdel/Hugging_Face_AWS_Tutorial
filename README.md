# Hosting Hugging Face Models on Amazon SageMaker

Welcome to the comprehensive guide on hosting your own inference environment for Hugging Face models using Amazon SageMaker! Whether you're a seasoned developer or just getting started, this tutorial will walk you through the steps to effortlessly deploy and serve your models with confidence. By the end, you'll have a robust setup on AWS SageMaker, empowering you to seamlessly deploy your models for real-world applications.

For our application, we'll be hosting [our own instance of GPT2 for text generation!](https://huggingface.co/distilbert/distilgpt2)

## Why Amazon SageMaker? Why Hugging Face?

SageMaker offers managed solutions for the entire machine learning lifecycle. It provides a hassle-free environment to deploy, manage, and scale your models. If you're looking for ways to get your models into production without needing to worry too much about the underlying complexities of model hosting, SageMaker is your tool.

As for Hugging Face - you and I don't have millions of dollars to throw at training advanced neural networks (at least not yet :wink:) with billions of parameters. Luckily for us, Hugging Face has changed the game and allowed users to host their own custom models that we can download, fine-tune, and host either in-house in Hugging Face Spaces or seamlessly transfer over to AWS. Hugging Face allows mass availability of open-source models designed with the most cutting-edge methods. I believe expertise around using pre-trained models will grow in demand for MLOps practitioners in the near future, as it's simply too efficient and cost-effective to ignore.

## What you'll Learn
- Setting up an Amazon SageMaker instance
- Preparing your Hugging Face model for deployment
- Deploying your model on SageMaker with ease
- Accessing your deployed model


## Prerequisites
Before getting started, ensure you have:
- An AWS Account
- [A trained Hugging Face model you'd like to host](https://huggingface.co/models)
- Basic knowledge of Python and Linux
- Basic knowledge of AWS services (specifically SageMaker) will be helpful but not required


## Step 1: Authenticate your Environment
- for this, we need an IAM User and IAM role
- skip to step 2 if you already have this set up

### 1.1 Setup IAM User

To authenticate for a command line tool like this one, we need to access AWS through access key credentials.
Head over to your AWS console and go to IAM Users. Click on the yellow "Create User" button on the top right:

![Alt text](images/image-1.png)

Make sure you check the box that says "Provide Access to the Management Console". For our purposes, we'll tick the second box to create an IAM User.
![Alt text](images/image-3.png)

To keep things simple, we won't require a new password for the new user's first sign-in.
![Alt text](images/image-4.png)

As for permissions, let's attach policies directly and look for "AmazonSageMakerFullAccess":
![Alt text](images/image-5.png)

Navigate through the remainder of user creation. Once AWS takes you back to your list of all IAM Users, select the IAM User you just created. Navigate to the security credentials tab:
![Alt text](images/image-6.png)

Scroll down a bit to create access keys. When prompted for a use case, select command line interface (should be the first option).
![Alt text](images/image-7.png)

Now, we have an access key and a secret key.
![Alt text](images/image-8.png)

We can now authenticate our environment using these keys. Type in ```aws configure```, copy and paste your access keys, and select your desired region (we will use us-east-1).
![Alt text](images/image-9.png)


<br><br>
### 1.2 Setup IAM Role

Head over to your AWS console and go to IAM Roles. Click on the yellow "Create Role" button on the top right:
![Alt text](images/image.png)


Select AWS service, and SageMaker when prompted. It should automatically attach the SageMaker Full Access policy. Name your role, and continue with the default settings.
![Alt text](images/image-10.png)

Select the role you just made and copy your ARN. Export this to an environment variable
![Alt text](images/image-11.png)
![Alt text](images/image-12.png)

## Step 2: Setting up Deployment Steps

Choose the Hugging Face model you'd like to be hosted. For this project, we'll host our own version of [DistilGPT2](https://huggingface.co/distilbert/distilgpt2)

I've split up this process into two files. I've made the following changes to the default py deployment file you can find on Hugging Face:
- host.py
    - changed the top few lines to load in Role from environment variable
    - added some print statements
    - removed model querying - this notebook should only deploy the model to SageMaker
- query.py
    - this takes command line input that will be passed to our model
    - we're using a text generation model, so this will tell the model what to generate

I recommend using these two python files, but if you'd like to create your own you can find the boilerplate on your model's hugging face page:

On the right side of the page, look for Deploy->Amazon SageMaker
![Alt text](images/image-13.png)
From here, you can copy and paste the python code into your own file and make changes as you see fit.

## Step 3: Host your model
Now comes the fun part. Run ```python host.py``` This will take a few minutes - this is the step that deploys your model to SageMaker for inference.
![Alt text](images/image-14.png)

## Step 4: Query your model
You may need to open *query.py* and change endpoint_name to your model endpoint's name. To find this, go to your AWS Management Console and head over to SageMaker. On the left side, look for Inference->Endpoints, and copy the name of the endpoint you just created via the host.py script.
![Alt text](images/image-15.png)

Then, run *query.py* and see your deployed text generation model in action:
![Alt text](images/image-16.png)

As can be seen, the output is truncated due to model constraints, and it doesn't give an output we'd consider ideal given out input. This is a drawback of using a smaller model. For larger models, we'd either have to increase the instance size, or look to another inference solution altogether.

## Step 5: IMPORTANT!! Delete your resources!
Once you're done using your model, you don't want to be billed for the idle resources. Navigate to SageMaker on the AWS Management Console and scroll down the left hand side until you find "inference". The Model, Endpoint, and Endpoint Configuration should all be deleted.
![Alt text](images/image-17.png)

Fortunately, the python files in this project lend themselves to high reproducibility, and this solution can be spun-up again in minutes.
