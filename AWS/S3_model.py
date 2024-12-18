import boto3
import pickle

# AWS S3 credentials
s3 = boto3.client('s3')

# Define bucket and file names
bucket_name = 'Crop_bucket'
model_file = 'crop_model.pkl'

# Download model from S3
with open(model_file, 'wb') as f:
    s3.download_fileobj(bucket_name, model_file, f)

# Load the model
with open(model_file, 'rb') as f:
    model = pickle.load(f)

print("Model loaded successfully!")
