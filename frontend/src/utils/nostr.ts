import { useState, useEffect } from 'react'
import { generatePrivateKey, getPublicKey, nip19 } from 'nostr-tools'

// Utility function to get keys from localStorage
export const getStoredKeys = () => {
  const savedKeys = localStorage.getItem('kiiara_nostr_keys')
  if (savedKeys) {
    try {
      return JSON.parse(savedKeys)
    } catch (e) {
      console.error('Error parsing stored keys', e)
      return null
    }
  }
  return null
}

// Global state hook for Nostr keys
export const useNostrKeys = () => {
  const [keys, setKeys] = useState<{ privateKey: string; publicKey: string; nsec: string; npub: string } | null>(null)

  useEffect(() => {
    setKeys(getStoredKeys())
  }, [])

  const generateKeys = () => {
    try {
      // In nostr-tools v1/v2, generateSecretKey/getPublicKey is the new API,
      // but if generatePrivateKey exists (v1 older), we use it.
      const privateKeyBytes = generatePrivateKey()
      const publicKeyBytes = getPublicKey(privateKeyBytes)
      
      const nsec = nip19.nsecEncode(privateKeyBytes)
      const npub = nip19.npubEncode(publicKeyBytes)
      
      const newKeys = { 
        privateKey: privateKeyBytes, 
        publicKey: publicKeyBytes, 
        nsec, 
        npub 
      }
      
      setKeys(newKeys)
      localStorage.setItem('kiiara_nostr_keys', JSON.stringify(newKeys))
      return newKeys
    } catch (error) {
      console.error("Error generating keys:", error)
      alert("Failed to generate Nostr keys. Check console for details.")
      return null
    }
  }

  const logout = () => {
    localStorage.removeItem('kiiara_nostr_keys')
    setKeys(null)
  }

  return { keys, generateKeys, logout }
}
