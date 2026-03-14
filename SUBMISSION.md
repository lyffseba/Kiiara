# Kiiara: Your Wise Grandmother AI - Hackathon Submission

## Project Overview

Kiiara is a voice-first, intelligent financial assistant that helps organize your finances and projects with Nostr security and Google Drive backup. As a wise grandmother AI, Kiiara speaks warmly and offers practical advice, making financial management feel like a family conversation.

## Problem Statement

Managing personal finances is overwhelming, especially for non-technical users. Traditional finance apps are complex, lack personality, and don't address security concerns. Users need a compassionate, intelligent assistant that:
- Makes financial management approachable and personal
- Ensures privacy and security of sensitive data
- Provides real-time, voice-first interaction
- Integrates seamlessly with existing financial tools

## Solution

Kiiara combines cutting-edge AI with decentralized technology to create a warm, secure financial companion:

### Key Features
1. **Real-time Voice Interaction**: Natural conversations using Gemini Live API with grandmotherly warmth
2. **Nostr-based Security**: Decentralized identity and client-side encryption
3. **Google Drive Backup**: Encrypted backup of all financial data
4. **Comprehensive Financial Tools**: Budget tracking, bill reminders, savings goals, investment advice
5. **PWA Installation**: Install as a Chrome app for quick access

### Technical Innovation
- **Gemini Live API Integration**: Real-time voice and vision processing
- **Nostr Protocol**: User-owned identity and encrypted data
- **Google Cloud Native**: Serverless backend on Cloud Run with Firestore
- **Agent Development Kit (ADK)**: Modular tool-based architecture

## How It Works

### Voice-First Experience
Users speak naturally to Kiiara, who understands context and executes financial tasks:
- "Add $85 expense for groceries today"
- "What's my spending this month?"
- "Help me create a savings goal for vacation"

### Security Architecture
1. **Nostr Key Generation**: Each user gets a unique Nostr identity
2. **Client-side Encryption**: Financial data encrypted with user's private key
3. **Zero-knowledge Backup**: Encrypted data stored on Google Drive
4. **JWT Authentication**: Secure API access without password storage

### Financial Intelligence
- **Pattern Recognition**: Analyzes spending habits and provides insights
- **Goal Tracking**: Monitors progress toward savings objectives
- **Bill Management**: Reminds of upcoming payments
- **Investment Guidance**: Personalized advice based on risk tolerance

## Technology Stack

### Frontend
- **React + TypeScript**: Type-safe UI components
- **Tailwind CSS**: Beautiful, responsive design
- **Nostr-tools**: Nostr protocol integration
- **PWA**: Offline support and installability

### Backend
- **Python + Google ADK**: Agent framework with tool system
- **Gemini Live API**: Real-time voice and vision
- **Vertex AI RAG**: Persistent memory and context
- **Firestore**: Financial data storage
- **Google Drive API**: Encrypted backup service

### Infrastructure
- **Google Cloud Run**: Serverless container hosting
- **Cloud Scheduler**: Periodic memory consolidation
- **Secret Manager**: Secure credential storage

## Hackathon Requirements Met

### Live Agents Category ✅
- Real-time voice interaction with interruption (barge-in)
- Vision capabilities for receipt scanning
- Natural conversation flow with grandmother personality
- Context-aware responses using persistent memory

### Technical Implementation ✅
- Built with Google Agent Development Kit (ADK)
- Uses Gemini Live API (gemini-live-2.5-flash-native-audio)
- Deployed on Google Cloud Run
- Integrates multiple Google Cloud services

### Innovation & UX ✅
- Breaks "text box" paradigm with voice-first interface
- Nostr-based security model for privacy
- Grandmother AI personality creates emotional connection
- Seamless multimodal interaction (voice + vision)

## Monetization Strategy

- **Free Tier**: 50 voice minutes/month, 500MB storage
- **Premium**: $9.99/month for unlimited usage
- **Future**: Real bank integrations, premium investment advice

## Future Enhancements

1. **Real Bank Integrations**: Connect to actual Nubank, Revolut, Coinbase accounts
2. **Family Sharing**: Shared financial goals with family members
3. **Advanced AI**: Predictive analytics and personalized recommendations
4. **Mobile Apps**: Native iOS and Android applications

## Team

Developed by a passionate team focused on making financial management accessible and secure for everyone.

## Conclusion

Kiiara represents the future of personal finance: voice-first, AI-powered, and privacy-focused. By combining Google's Gemini Live API with Nostr's decentralized security, we've created an assistant that feels like family while protecting your most sensitive data.

**Try Kiiara today and let your wise grandmother AI guide your financial journey!**