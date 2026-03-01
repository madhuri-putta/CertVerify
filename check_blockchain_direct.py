from web3 import Web3
import json

# Connect to local Hardhat node
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

# Contract Configuration (Must match backend/blockchain_utils.py)
CONTRACT_ADDRESS = "0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512"
CONTRACT_ABI = [
    {
      "inputs": [{"internalType": "string", "name": "_hash", "type": "string"}],
      "name": "verifyCertificate",
      "outputs": [
        {"internalType": "bool", "name": "", "type": "bool"},
        {"internalType": "string", "name": "", "type": "string"},
        {"internalType": "string", "name": "", "type": "string"},
        {"internalType": "string", "name": "", "type": "string"},
        {"internalType": "uint256", "name": "", "type": "uint256"},
        {"internalType": "address", "name": "", "type": "address"}
      ],
      "stateMutability": "view",
      "type": "function"
    }
]

contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)

HASH_TO_CHECK = "614abf4bcac54f351401a5155c959f080300262be7d8aa78477dc14605e20ec6"

def check_contract():
    print(f"🔍 Checking Contract at {CONTRACT_ADDRESS}...")
    print(f"   Hash: {HASH_TO_CHECK}")
    
    try:
        result = contract.functions.verifyCertificate(HASH_TO_CHECK).call()
        print(f"\n✅ Result: {result}")
        
        is_valid = result[0]
        if is_valid:
            print("   🎉 VALID! The certificate IS on the blockchain.")
        else:
            print("   ❌ INVALID! The certificate is NOT on the blockchain.")
            
    except Exception as e:
        print(f"   ❌ Error: {e}")

if __name__ == "__main__":
    check_contract()
