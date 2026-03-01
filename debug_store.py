from backend.blockchain_utils import store_on_blockchain
import traceback

def debug_store():
    print("🚀 Debugging Store on Blockchain...")
    
    import random
    rand_hash = f"test_hash_{random.randint(1000, 9999)}"
    try:
        tx_hash = store_on_blockchain(
            rand_hash,
            "Test Student",
            "Test Course",
            "Test Institute",
            "test@email.com"
        )
        
        if tx_hash:
            print(f"✅ Success! Tx Hash: {tx_hash}")
        else:
            print("❌ Failed! returned None")
            
    except Exception as e:
        print(f"❌ Exception: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    debug_store()
