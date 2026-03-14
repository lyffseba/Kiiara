import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom'
import Dashboard from './components/Dashboard'
import VoiceInterface from './components/VoiceInterface'
import Settings from './components/Settings'
import { useNostrKeys } from './utils/nostr'
import './App.css'

function App() {
  const { keys } = useNostrKeys()

  return (
    <Router>
      <div className="min-h-screen bg-gray-50">
        {/* Navigation */}
        <nav className="bg-white shadow-sm border-b border-gray-200 sticky top-0 z-10">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="flex justify-between h-16">
              <div className="flex">
                <div className="flex-shrink-0 flex items-center">
                  <span className="text-2xl font-bold text-primary tracking-tight">Kiiara 👵</span>
                </div>
                <div className="hidden sm:ml-8 sm:flex sm:space-x-8">
                  <Link to="/" className="border-transparent text-gray-600 hover:border-primary hover:text-primary inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium transition-colors">
                    Dashboard
                  </Link>
                  <Link to="/voice" className="border-transparent text-gray-600 hover:border-primary hover:text-primary inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium transition-colors">
                    Voice Assistant
                  </Link>
                  <Link to="/settings" className="border-transparent text-gray-600 hover:border-primary hover:text-primary inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium transition-colors">
                    Settings
                  </Link>
                </div>
              </div>
              <div className="hidden sm:ml-6 sm:flex sm:items-center space-x-4">
                {keys ? (
                  <div className="flex items-center space-x-2 bg-green-50 px-3 py-1.5 rounded-full border border-green-100">
                    <div className="w-2 h-2 bg-green-500 rounded-full animate-pulse"></div>
                    <span className="text-xs font-medium text-green-700">Nostr Secured</span>
                  </div>
                ) : (
                  <Link to="/settings" className="bg-primary text-white px-4 py-2 rounded-md text-sm font-medium hover:bg-primary/90 transition-colors shadow-sm">
                    Connect Nostr
                  </Link>
                )}
              </div>
            </div>
          </div>
        </nav>

        {/* Main content */}
        <main className="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8 h-[calc(100vh-4rem)]">
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/voice" element={<VoiceInterface />} />
            <Route path="/settings" element={<Settings />} />
          </Routes>
        </main>
      </div>
    </Router>
  )
}

export default App
