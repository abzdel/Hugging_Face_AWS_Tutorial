# Hosting Hugging Face Models on Amazon SageMaker

Welcome to the comprehensive guide on hosting your own stable inference environment for Hugging Face models using Amazon SageMaker! Whether you're a seasoned developer or just getting started, this tutorial will walk you through the steps to effortlessly deploy and serve your models with confidence. By the end, you'll have a robust setup on AWS SageMaker, empowering you to seamlessly deploy your models for real-world applications.

For our application, we'll be hosting [our own instance of Stable Diffusion 2 for text-to-image generation!](https://huggingface.co/stabilityai/stable-diffusion-2)

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
- Basic knowledge of AWS services (specifically Lambda + SageMaker) will be helpful but not required


<br>WIP after this<br>
## Step 1: Authenticate your Environment

To authenticate for a command line tool like this one, we need to access AWS through access key credentials.
Head over to your AWS console and go to IAM Users. Click on the yellow "Create User" button on the top right:

![Alt text](images/image-1.png)

Make sure you check the box that says "Provide Access to the Management Console". For this tutorial, we'll tick the second box to create an IAM User.
![Alt text](images/image-3.png)

To keep things simple, we won't require a new password for the new user's first sign-in.
![Alt text](images/image-4.png)

As for permissions, let's attach policies directly and look for "AmazonSageMakerFullAccess":
![Alt text](images/image-5.png)

Navigate through the remainder of user creation. Once AWS takes you back to your list of all IAM Users, click on your new user to generate credentials. TODO: create access key, authenticate with aws configure, check on script to see if role is still needed

<br><br>

Head over to your AWS console and go to IAM Roles. Click on the yellow "Create Role" button on the top right:
![Alt text](images/image.png)


