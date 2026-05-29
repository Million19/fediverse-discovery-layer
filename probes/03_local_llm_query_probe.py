# probes/03_local_llm_query_probe.py

"""
[INNOVATION HEADER]
Phase: 1 - Environmental Discovery & Telemetry (File 3 of 10)
Paradigm: Agentic Probe Explorer / Defensive Paranoia
Target: Verifying local Ollama daemon connections, hardware token generation speeds,
        and VRAM offloading telemetry (keep_alive) for the Semantic Extractor layer.
"""

import asyncio
import httpx
import time

async def probe_local_inference(model_name: str = "llama3.2"):
    print(f"[DISCOVERY] Initiating Local LLM Physics Probe (Target: {model_name})...")
    
    endpoint = "http://localhost:11434/api/generate"
    
    # Simulating Layer 2: The Semantic Extraction Engine
    test_prompt = """
    Extract the core relationship from this social post into a Subject-Predicate-Object triplet.
    Post: "Michael just boosted a fascinating article about decentralized AI by @alice."
    Return ONLY a JSON array like: ["Subject", "Predicate", "Object"]
    """

    # We inject keep_alive to test the blueprint's VRAM ejection telemetry
    payload = {
        "model": model_name,
        "prompt": test_prompt,
        "stream": False,
        "keep_alive": "0m" # Forces immediate VRAM unload after response for testing
    }

    print("  -> Connecting to local Ollama daemon...")
    start_time = time.perf_counter()
    
    # 60s read timeout because local LLMs can take time to load into VRAM on first boot
    timeout_fence = httpx.Timeout(60.0, connect=5.0)

    try:
        async with httpx.AsyncClient(timeout=timeout_fence) as client:
            response = await client.post(endpoint, json=payload)
            
            # Trap Model Not Found (404) safely
            if response.status_code == 404:
                print(f"\n[ERROR] Model '{model_name}' not found locally.")
                print(f"[RECOVERY] Run this command in your terminal: ollama pull {model_name}")
                return

            response.raise_for_status()
            data = response.json()

            elapsed = time.perf_counter() - start_time
            
            # Hardware Telemetry Math
            eval_count = data.get("eval_count", 0)
            eval_duration_ns = data.get("eval_duration", 1) # in nanoseconds
            eval_duration_s = eval_duration_ns / 1e9
            tokens_per_second = eval_count / eval_duration_s if eval_duration_s > 0 else 0

            print(f"\n[SUCCESS] Local Inference Complete in {elapsed:.2f}s")
            print(f"  => Hardware Speed: {tokens_per_second:.2f} Tokens/Second")
            print(f"  => Total Tokens Generated: {eval_count}")
            print(f"  => VRAM Telemetry: 'keep_alive=0m' executed successfully.")
            print(f"  => LLM Semantic Output:\n     {data.get('response', '').strip()}")

    except httpx.ConnectError:
        print("\n[FATAL] Connection Refused.")
        print("[RECOVERY] Ollama daemon is not running. Please start the Ollama application.")
    except httpx.ReadTimeout:
        print("\n[ERROR] Read Timeout. Hardware took longer than 60 seconds to process the prompt.")
    except Exception as e:
        print(f"\n[FATAL] Unknown Inference Error: {type(e).__name__} - {str(e)}")

if __name__ == "__main__":
    # Feel free to change this to "llama3", "mistral", or whatever model you have installed
    TARGET_MODEL = "gemma4:e4b" 
    asyncio.run(probe_local_inference(TARGET_MODEL))
