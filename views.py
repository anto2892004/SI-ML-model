import pickle
import numpy as np
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SensorData, CropRecommendation
from .serializers import SensorDataSerializer, CropRecommendationSerializer

# Load trained ML model
with open("crop/crop_model.pkl", "rb") as f:
    model = pickle.load(f)

@api_view(['POST'])
def recommend_crop(request):
    """
    API to predict the best crop based on sensor data.
    """
    serializer = SensorDataSerializer(data=request.data)
    if serializer.is_valid():
        sensor_data = serializer.save()

        # Prepare data for model
        features = np.array([
            sensor_data.temperature,
            sensor_data.humidity,
            sensor_data.nitrogen,
            sensor_data.phosphorus,
            sensor_data.potassium
        ]).reshape(1, -1)

        # Make prediction
        predicted_crop = model.predict(features)[0]

        # Save recommendation
        recommendation = CropRecommendation.objects.create(
            crop_name=predicted_crop,
            probability=0.9,  # Adjust based on ML confidence
            sensor_data=sensor_data
        )

        return Response({
            "recommended_crop": predicted_crop,
            "probability": recommendation.probability
        })

    return Response(serializer.errors, status=400)
