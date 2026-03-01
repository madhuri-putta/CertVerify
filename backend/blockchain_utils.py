from web3 import Web3
import json
import os

# Connect to local Hardhat node
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

# Contract Configuration
CONTRACT_ADDRESS = "0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512"
# Minimal ABI for addCertificate and verifyCertificate
CONTRACT_ABI = [
    {
      "inputs": [],
      "stateMutability": "nonpayable",
      "type": "constructor"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "string",
          "name": "fileHash",
          "type": "string"
        },
        {
          "indexed": False,
          "internalType": "string",
          "name": "studentName",
          "type": "string"
        },
        {
          "indexed": False,
          "internalType": "string",
          "name": "institute",
          "type": "string"
        }
      ],
      "name": "CertificateRegistered",
      "type": "event"
    },
    {
      "inputs": [
        {
          "internalType": "string",
          "name": "",
          "type": "string"
        }
      ],
      "name": "certificates",
      "outputs": [
        {
          "internalType": "string",
          "name": "fileHash",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "studentName",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "course",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "institute",
          "type": "string"
        },
        {
          "internalType": "uint256",
          "name": "timestamp",
          "type": "uint256"
        },
        {
          "internalType": "address",
          "name": "issuer",
          "type": "address"
        },
        {
          "internalType": "bool",
          "name": "isValid",
          "type": "bool"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "owner",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "string",
          "name": "_fileHash",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "_studentName",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "_course",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "_institute",
          "type": "string"
        }
      ],
      "name": "registerCertificate",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "string",
          "name": "_fileHash",
          "type": "string"
        }
      ],
      "name": "verifyCertificate",
      "outputs": [
        {
          "internalType": "bool",
          "name": "isValid",
          "type": "bool"
        },
        {
          "internalType": "string",
          "name": "studentName",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "course",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "institute",
          "type": "string"
        },
        {
          "internalType": "uint256",
          "name": "timestamp",
          "type": "uint256"
        },
        {
          "internalType": "address",
          "name": "issuer",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    }
]

contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)

# Use the first account as the default signer (for prototype)
DEFAULT_ACCOUNT = w3.eth.accounts[0]

def verify_on_blockchain(file_hash: str):
    try:
        # Call the smart contract
        result = contract.functions.verifyCertificate(file_hash).call()
        is_valid = result[0]
        # result structure: (isValid, studentName, course, institute, timestamp, issuer)
        if is_valid:
            return {
                "verified": True,
                "student_name": result[1],
                "course": result[2],
                "institute": result[3],
                "timestamp": result[4],
                "issuer": result[5]
            }
        return {"verified": False}
    except Exception as e:
        print(f"Blockchain Verification Error: {e}")
        return {"verified": False}

def store_on_blockchain(file_hash: str, student_name: str, course: str, institute: str, issuer_email: str):
    try:
        # Send transaction to smart contract
        # Note: issuer_email is not stored on-chain in this contract version
        tx_hash = contract.functions.registerCertificate(
            file_hash, student_name, course, institute
        ).transact({'from': DEFAULT_ACCOUNT})
        
        # Wait for transaction receipt
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        if receipt.status == 0:
            raise Exception("Transaction Failed (Reverted)")
        return receipt.transactionHash.hex()
    except Exception as e:
        print(f"Blockchain Storage Error: {e}")
        return None
