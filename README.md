# Kiiara - Your Wise Grandmother AI

A voice-first, intelligent financial assistant that helps organize your finances and projects with Nostr security and Google Drive backup. Kiiara is a wise, tender grandmother AI that speaks warmly and offers practical advice.

## Features

- **Real-time Voice Conversation**: Talk naturally with Kiiara using Gemini Live API
- **Financial Management**: Track income, expenses, bills, and savings goals
- **Nostr Identity**: Decentralized identity for secure interactions
- **Google Drive Backup**: Encrypted backup of financial data
- **Smart Integrations**: Mock connections to Nubank, Revolut, and Coinbase
- **Investment Advice**: Personalized advice based on your risk tolerance
- **PWA**: Installable in any Chrome tab

## Architecture

```
Frontend (React PWA) ↔ Backend (Python ADK Agent) ↔ Gemini Live API
      ↓                        ↓                        ↓
  Nostr Auth            Financial Tools           Voice/Vision
  Google Drive Backup   Firestore Storage         RAG Memory
```

## Tech Stack

- **Frontend**: React, TypeScript, Tailwind CSS, Vite
- **Backend**: Python, Google Agent Development Kit (ADK)
- **AI**: Gemini Live API (gemini-live-2.5-flash-native-audio)
- **Database**: Google Cloud Firestore
- **Storage**: Google Drive API
- **Identity**: Nostr Protocol (secp256k1)
- **Hosting**: Google Cloud Run

## Setup Instructions

### Prerequisites

1. Python 3.12+
2. Node.js 18+
3. Google Cloud project with billing enabled
4. Google Cloud SDK (gcloud CLI)

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up Google Cloud authentication:
   ```bash
   gcloud auth application-default login
   ```

5. Set environment variables (create `.env` file):
   ```
   GOOGLE_CLOUD_PROJECT=jsgvlyff
   GOOGLE_CLOUD_LOCATION=us-central1
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start development server:
   ```bash
   npm run dev
   ```

## Running the Application

### Start Backend (ADK Web Server)

From the project root:
```bash
source backend/venv/bin/activate
adk web backend --port 8080
```

### Start Frontend

From the frontend directory:
```bash
npm run dev
```

The frontend will be available at `http://localhost:3000` and will proxy API requests to the backend on port 8080.

## Usage

1. Open the frontend in Chrome
2. Navigate to Settings to generate your Nostr identity
3. Go to Voice Assistant to start talking with Kiiara
4. Use the Dashboard to view financial overview
5. Connect Google Drive for encrypted backup

## Hackathon Submission

This project is submitted to the Gemini Live Agent Challenge under the **Live Agents** category.

### Requirements Met

- ✅ Uses Gemini Live API
- ✅ Built with Google Agent Development Kit (ADK)
- ✅ Deployed on Google Cloud (Cloud Run)
- ✅ Real-time voice + vision interaction
- ✅ Persistent memory using RAG
- ✅ Nostr identity integration
- ✅ Google Drive backup

## Monetization

- **Free Tier**: 50 voice minutes/month, 500MB storage
- **Premium**: $9.99/month for unlimited minutes, 10GB storage, advanced features

## License

MIT License