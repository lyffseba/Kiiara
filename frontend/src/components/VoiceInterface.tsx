import { useState } from 'react'
import { Mic, MicOff, Video, VideoOff, Maximize2, Minimize2 } from 'lucide-react'

export default function VoiceInterface() {
  const [isVoiceEnabled, setIsVoiceEnabled] = useState(true)
  const [isVideoEnabled, setIsVideoEnabled] = useState(true)
  const [isFullscreen, setIsFullscreen] = useState(false)

  return (
    <div className="h-full flex flex-col">
      {/* Header */}
      <div className="flex justify-between items-center mb-6">
        <div>
          <h1 className="text-3xl font-bold text-gray-900">Voice Assistant</h1>
          <p className="text-gray-600">Talk to Kiiara, your wise grandmother AI</p>
        </div>
        <div className="flex items-center space-x-3">
          <button 
            onClick={() => setIsVoiceEnabled(!isVoiceEnabled)}
            className={`p-3 rounded-full ${isVoiceEnabled ? 'bg-green-100 text-green-600' : 'bg-red-100 text-red-600'}`}
          >
            {isVoiceEnabled ? <Mic className="w-6 h-6" /> : <MicOff className="w-6 h-6" />}
          </button>
          <button 
            onClick={() => setIsVideoEnabled(!isVideoEnabled)}
            className={`p-3 rounded-full ${isVideoEnabled ? 'bg-green-100 text-green-600' : 'bg-red-100 text-red-600'}`}
          >
            {isVideoEnabled ? <Video className="w-6 h-6" /> : <VideoOff className="w-6 h-6" />}
          </button>
          <button 
            onClick={() => setIsFullscreen(!isFullscreen)}
            className="p-3 rounded-full bg-gray-100 text-gray-600 hover:bg-gray-200"
          >
            {isFullscreen ? <Minimize2 className="w-6 h-6" /> : <Maximize2 className="w-6 h-6" />}
          </button>
        </div>
      </div>

      {/* Voice Interface Container */}
      <div className={`flex-1 bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden ${isFullscreen ? 'fixed inset-0 z-50 rounded-none' : ''}`}>
        <iframe 
          src="http://localhost:8080" 
          className="w-full h-full border-0"
          title="Kiiara Voice Assistant"
          allow="microphone; camera"
        />
      </div>

      {/* Instructions */}
      <div className="mt-4 bg-blue-50 rounded-lg p-4">
        <h3 className="font-semibold text-blue-900 mb-2">How to use:</h3>
        <ul className="text-sm text-blue-800 space-y-1">
          <li>• Click the microphone button to start/stop voice input</li>
          <li>• Use camera button to enable/disable video feed</li>
          <li>• Speak naturally to Kiiara about your finances</li>
          <li>• Ask questions like "What's my spending this month?" or "Help me create a budget"</li>
        </ul>
      </div>
    </div>
  )
}
