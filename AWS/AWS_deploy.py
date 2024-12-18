import json
import boto3
import numpy as np
import pickle

# Load model from S3
s3 = boto3.client('s3')
bucket_name = 'Crop_bucket'
model_file = 'crop_model.pkl'

def lambda_handler(event, context):
    # Parse input data
    input_data = json.loads(event['body'])  # Assuming JSON input from API Gateway
    features = np.array(input_data['features']).reshape(1, -1)

    # Download and load model
    with open('/tmp/' + model_file, 'wb') as f:
        s3.download_fileobj(bucket_name, model_file, f)
    with open('/tmp/' + model_file, 'rb') as f:
        model = pickle.load(f)

    # Predict crop
    prediction = model.predict(features)

    return {
        'statusCode': 200,
        'body': json.dumps({'predicted_crop': prediction[0]})
    }
