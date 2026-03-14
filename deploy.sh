#!/bin/bash
set -e

# Configuration
PROJECT_ID="jsgvlyff"
REGION="us-central1"
SERVICE_NAME="kiiara-backend"
IMAGE_NAME="gcr.io/${PROJECT_ID}/${SERVICE_NAME}"

echo "Deploying Kiiara backend to Google Cloud Run..."

# Authenticate if needed
if ! gcloud auth list --filter=status:ACTIVE --format="value(account)" | grep -q .; then
    echo "No active gcloud authentication. Please run: gcloud auth login"
    exit 1
fi

# Set project
gcloud config set project ${PROJECT_ID}

# Enable required APIs
echo "Enabling required APIs..."
gcloud services enable \
    run.googleapis.com \
    containerregistry.googleapis.com \
    artifactregistry.googleapis.com \
    cloudbuild.googleapis.com

# Build and push Docker image
echo "Building Docker image..."
cd backend
gcloud builds submit --tag ${IMAGE_NAME} .

# Deploy to Cloud Run
echo "Deploying to Cloud Run..."
gcloud run deploy ${SERVICE_NAME} \
    --image ${IMAGE_NAME} \
    --region ${REGION} \
    --platform managed \
    --allow-unauthenticated \
    --set-env-vars "GOOGLE_CLOUD_PROJECT=${PROJECT_ID},GOOGLE_CLOUD_LOCATION=${REGION}"

# Get the service URL
SERVICE_URL=$(gcloud run services describe ${SERVICE_NAME} --region ${REGION} --format="value(status.url)")
echo "Backend deployed to: ${SERVICE_URL}"
echo "Test with: curl ${SERVICE_URL}/health"

# Save deployment info
echo "SERVICE_URL=${SERVICE_URL}" > .deployment.env
echo "Deployment complete!"