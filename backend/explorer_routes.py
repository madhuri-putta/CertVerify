from fastapi import APIRouter
from typing import List
import datetime

router = APIRouter()

@router.get("/explorer/blocks")
def get_blocks():
    # Mock data for blockchain explorer
    return [
        {
            "block_number": 12345,
            "timestamp": datetime.datetime.now().isoformat(),
            "transactions": 5,
            "miner": "0xMinerAddress...",
            "hash": "0xBlockHash1..."
        },
        {
            "block_number": 12344,
            "timestamp": (datetime.datetime.now() - datetime.timedelta(minutes=1)).isoformat(),
            "transactions": 2,
            "miner": "0xMinerAddress...",
            "hash": "0xBlockHash2..."
        },
        {
            "block_number": 12343,
            "timestamp": (datetime.datetime.now() - datetime.timedelta(minutes=2)).isoformat(),
            "transactions": 8,
            "miner": "0xMinerAddress...",
            "hash": "0xBlockHash3..."
        }
    ]
