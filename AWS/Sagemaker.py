import boto3

sagemaker = boto3.client('sagemaker')

response = sagemaker.create_model(
    ModelName='crop-prediction-model',
    PrimaryContainer={
        'Image': '763104351884.dkr.ecr.us-west-2.amazonaws.com/sklearn-inference:latest',
        'ModelDataUrl': 's3://your-s3-bucket/crop_model.tar.gz',  
    },
    ExecutionRoleArn='arn:aws:iam::123456789012:role/service-role/AmazonSageMaker-ExecutionRole-2023'
)

print("SageMaker model created:", response)
