import { useState, useEffect } from 'react'
import { Key, Shield, Database, Cloud, Check, Copy, RefreshCw } from 'lucide-react'
import { generatePrivateKey, getPublicKey, nip19 } from 'nostr-tools'

export default function Settings() {
  const [nostrKeys, setNostrKeys] = useState<{ privateKey: string; publicKey: string; nsec: string; npub: string } | null>(null)
  const [isBackupEnabled, setIsBackupEnabled] = useState(false)
  const [backupStatus, setBackupStatus] = useState<'idle' | 'backing_up' | 'success' | 'error'>('idle')
  const [copied, setCopied] = useState<string | null>(null)

  useEffect(() => {
    // Load keys from localStorage if they exist
    const savedKeys = localStorage.getItem('kiiara_nostr_keys')
    if (savedKeys) {
      setNostrKeys(JSON.parse(savedKeys))
    }
  }, [])

  const generateNewKeys = () => {
    const privateKey = generatePrivateKey()
    const publicKey = getPublicKey(privateKey)
    const nsec = nip19.nsecEncode(privateKey)
    const npub = nip19.npubEncode(publicKey)
    
    const keys = { privateKey, publicKey, nsec, npub }
    setNostrKeys(keys)
    localStorage.setItem('kiiara_nostr_keys', JSON.stringify(keys))
  }

  const copyToClipboard = (text: string, field: string) => {
    navigator.clipboard.writeText(text)
    setCopied(field)
    setTimeout(() => setCopied(null), 2000)
  }

  const handleBackup = async () => {
    setBackupStatus('backing_up')
    // Simulate backup process
    await new Promise(resolve => setTimeout(resolve, 2000))
    setBackupStatus('success')
    setTimeout(() => setBackupStatus('idle'), 3000)
  }

  return (
    <div className="space-y-8">
      {/* Header */}
      <div>
        <h1 className="text-3xl font-bold text-gray-900">Settings</h1>
        <p className="text-gray-600">Manage your Nostr identity and backup settings</p>
      </div>

      {/* Nostr Identity Section */}
      <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
        <div className="flex items-center space-x-3 mb-6">
          <div className="p-2 bg-purple-100 rounded-lg">
            <Key className="w-6 h-6 text-purple-600" />
          </div>
          <div>
            <h2 className="text-xl font-semibold text-gray-900">Nostr Identity</h2>
            <p className="text-sm text-gray-500">Your decentralized identity for secure interactions</p>
          </div>
        </div>

        {!nostrKeys ? (
          <div className="text-center py-8">
            <p className="text-gray-600 mb-4">You don't have a Nostr identity yet.</p>
            <button 
              onClick={generateNewKeys}
              className="bg-purple-600 text-white px-6 py-2 rounded-lg hover:bg-purple-700 transition-colors"
            >
              Generate New Identity
            </button>
          </div>
        ) : (
          <div className="space-y-6">
            {/* Public Key */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">Public Key (npub)</label>
              <div className="flex items-center space-x-2">
                <input 
                  type="text" 
                  value={nostrKeys.npub} 
                  readOnly 
                  className="flex-1 p-3 bg-gray-50 border border-gray-300 rounded-lg font-mono text-sm"
                />
                <button 
                  onClick={() => copyToClipboard(nostrKeys.npub, 'npub')}
                  className="p-3 bg-gray-100 rounded-lg hover:bg-gray-200 transition-colors"
                >
                  {copied === 'npub' ? <Check className="w-5 h-5 text-green-600" /> : <Copy className="w-5 h-5" />}
                </button>
              </div>
            </div>

            {/* Private Key (hidden by default) */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">Private Key (nsec)</label>
              <div className="flex items-center space-x-2">
                <input 
                  type="password" 
                  value={nostrKeys.nsec} 
                  readOnly 
                  className="flex-1 p-3 bg-gray-50 border border-gray-300 rounded-lg font-mono text-sm"
                />
                <button 
                  onClick={() => copyToClipboard(nostrKeys.nsec, 'nsec')}
                  className="p-3 bg-gray-100 rounded-lg hover:bg-gray-200 transition-colors"
                >
                  {copied === 'nsec' ? <Check className="w-5 h-5 text-green-600" /> : <Copy className="w-5 h-5" />}
                </button>
              </div>
              <p className="mt-2 text-sm text-red-600 flex items-center">
                <Shield className="w-4 h-4 mr-1" />
                Never share your private key with anyone
              </p>
            </div>

            {/* Actions */}
            <div className="flex space-x-4 pt-4 border-t border-gray-200">
              <button 
                onClick={generateNewKeys}
                className="flex items-center space-x-2 px-4 py-2 bg-gray-100 rounded-lg hover:bg-gray-200 transition-colors"
              >
                <RefreshCw className="w-5 h-5" />
                <span>Regenerate Keys</span>
              </button>
            </div>
          </div>
        )}
      </div>

      {/* Google Drive Backup Section */}
      <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
        <div className="flex items-center space-x-3 mb-6">
          <div className="p-2 bg-blue-100 rounded-lg">
            <Cloud className="w-6 h-6 text-blue-600" />
          </div>
          <div>
            <h2 className="text-xl font-semibold text-gray-900">Google Drive Backup</h2>
            <p className="text-sm text-gray-500">Encrypted backup of your financial data</p>
          </div>
        </div>

        <div className="space-y-4">
          <div className="flex items-center justify-between p-4 bg-gray-50 rounded-lg">
            <div className="flex items-center space-x-3">
              <Database className="w-5 h-5 text-gray-600" />
              <span className="font-medium">Automatic Backup</span>
            </div>
            <button 
              onClick={() => setIsBackupEnabled(!isBackupEnabled)}
              className={`relative inline-flex h-6 w-11 items-center rounded-full transition-colors ${isBackupEnabled ? 'bg-blue-600' : 'bg-gray-300'}`}
            >
              <span className={`inline-block h-4 w-4 transform rounded-full bg-white transition-transform ${isBackupEnabled ? 'translate-x-6' : 'translate-x-1'}`} />
            </button>
          </div>

          {isBackupEnabled && (
            <div className="p-4 bg-blue-50 rounded-lg">
              <p className="text-sm text-blue-800 mb-3">
                Your data will be encrypted with your Nostr private key and backed up to Google Drive.
              </p>
              <button 
                onClick={handleBackup}
                disabled={backupStatus === 'backing_up'}
                className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition-colors disabled:opacity-50 flex items-center space-x-2"
              >
                {backupStatus === 'backing_up' ? (
                  <>
                    <RefreshCw className="w-4 h-4 animate-spin" />
                    <span>Backing up...</span>
                  </>
                ) : backupStatus === 'success' ? (
                  <>
                    <Check className="w-4 h-4" />
                    <span>Backup Complete!</span>
                  </>
                ) : (
                  <>
                    <Cloud className="w-4 h-4" />
                    <span>Backup Now</span>
                  </>
                )}
              </button>
            </div>
          )}
        </div>
      </div>

      {/* Financial Integrations (Mock) */}
      <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
        <div className="flex items-center space-x-3 mb-6">
          <div className="p-2 bg-green-100 rounded-lg">
            <Shield className="w-6 h-6 text-green-600" />
          </div>
          <div>
            <h2 className="text-xl font-semibold text-gray-900">Financial Integrations</h2>
            <p className="text-sm text-gray-500">Connect to Nubank, Revolut, and Coinbase (Demo)</p>
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div className="p-4 border border-gray-200 rounded-lg hover:border-purple-300 transition-colors cursor-pointer">
            <div className="flex items-center space-x-3">
              <div className="w-10 h-10 bg-purple-100 rounded-full flex items-center justify-center">
                <span className="text-purple-600 font-bold">N</span>
              </div>
              <div>
                <p className="font-medium">Nubank</p>
                <p className="text-sm text-gray-500">Connected</p>
              </div>
            </div>
          </div>
          <div className="p-4 border border-gray-200 rounded-lg hover:border-blue-300 transition-colors cursor-pointer">
            <div className="flex items-center space-x-3">
              <div className="w-10 h-10 bg-blue-100 rounded-full flex items-center justify-center">
                <span className="text-blue-600 font-bold">R</span>
              </div>
              <div>
                <p className="font-medium">Revolut</p>
                <p className="text-sm text-gray-500">Connected</p>
              </div>
            </div>
          </div>
          <div className="p-4 border border-gray-200 rounded-lg hover:border-yellow-300 transition-colors cursor-pointer">
            <div className="flex items-center space-x-3">
              <div className="w-10 h-10 bg-yellow-100 rounded-full flex items-center justify-center">
                <span className="text-yellow-600 font-bold">C</span>
              </div>
              <div>
                <p className="font-medium">Coinbase</p>
                <p className="text-sm text-gray-500">Connected</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
