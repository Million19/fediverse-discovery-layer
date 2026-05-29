# probes/01_activitypub_fetch_probe.py

"""
[INNOVATION HEADER]
Phase: 1 - Environmental Discovery & Telemetry (File 1 of 10)
Paradigm: Agentic Probe Explorer / Defensive Paranoia
Target: Verifying live Fediverse network timeouts, polymorphic exception trapping, 
        and empirical JSON-LD payload extraction without mocks.
"""

import asyncio
import httpx
import time

async def probe_activitypub_endpoint(target_url: str, max_retries: int = 3):
    print(f"[DISCOVERY] Initiating probe against: {target_url}")
    
    # Mathematical Timeout Fence: 5s to connect, 10s to read.
    timeout_fence = httpx.Timeout(10.0, connect=5.0)
    
    headers = {
        "Accept": "application/activity+json",
        "User-Agent": "FediverseDiscoveryLayer/0.1 (Research Probe; +https://github.com/Million19/fediverse-discovery-layer)"
    }

    async with httpx.AsyncClient(timeout=timeout_fence, headers=headers) as client:
        for attempt in range(1, max_retries + 1):
            start_time = time.perf_counter()
            try:
                print(f"  -> [Attempt {attempt}/{max_retries}] Executing GET request...")
                response = await client.get(target_url)
                
                # Trap 4xx/5xx errors safely
                response.raise_for_status()
                
                elapsed = time.perf_counter() - start_time
                
                # Safe Telemetry Extraction (Mitigating WCGW KeyError)
                rate_limit = response.headers.get("x-ratelimit-remaining", "[HEADER MISSING]")
                content_type = response.headers.get("content-type", "UNKNOWN")
                payload = response.json()
                
                print(f"\n[SUCCESS] Response received in {elapsed:.3f}s")
                print(f"  => HTTP Status: {response.status_code}")
                print(f"  => Content-Type: {content_type}")
                print(f"  => X-Ratelimit-Remaining: {rate_limit}")
                
                # Print anatomical structure instead of full payload (Telemetry Rule)
                print(f"  => Payload Root Keys: {list(payload.keys())}")
                
                # Empirical schema check
                if "@context" in payload:
                    print("  => Verification: Valid JSON-LD '@context' detected.")
                
                return payload # Successful exit

            except httpx.ConnectTimeout as e:
                print(f"\n[ERROR] Connection Timeout on attempt {attempt}: {str(e)}")
            except httpx.ReadTimeout as e:
                print(f"\n[ERROR] Read Timeout on attempt {attempt}: {str(e)}")
            except httpx.HTTPStatusError as e:
                print(f"\n[ERROR] HTTP Status {e.response.status_code} on attempt {attempt}: {str(e)}")
            except httpx.RequestError as e:
                print(f"\n[ERROR] General Network Failure on attempt {attempt}: {str(e)}")
            except Exception as e:
                print(f"\n[FATAL] Unknown Exception: {type(e).__name__} - {str(e)}")
                break # Hard failure, do not retry unknown bugs
            
            # Self-Healing Decay Loop
            if attempt < max_retries:
                sleep_time = 2 ** attempt # 2s, 4s...
                print(f"  -> Backing off for {sleep_time} seconds before retry...")
                await asyncio.sleep(sleep_time)
            else:
                print("\n[DISCOVERY FATAL] Maximum retries exhausted. Network probe failed.")

if __name__ == "__main__":
    # Target: The official Mastodon public actor profile
    TARGET_URI = "https://mastodon.social/users/Mastodon"
    asyncio.run(probe_activitypub_endpoint(TARGET_URI))
