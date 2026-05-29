# probes/02_graph_extraction_probe.py

"""
[INNOVATION HEADER]
Phase: 1 - Environmental Discovery & Telemetry (File 2 of 10)
Paradigm: Agentic Probe Explorer / Defensive Paranoia
Target: Verifying NetworkX in-memory RAM footprints and Louvain modularity 
        execution times to protect 16GB consumer hardware limits.
"""

import time
import tracemalloc
import networkx as nx

def probe_graph_physics():
    print("[DISCOVERY] Initiating In-Memory Graph Physics Probe...")
    
    # Start tracing Python memory allocation
    tracemalloc.start()
    
    try:
        # Step 1: Generate a synthetic social topology
        # Mimics 2,000 Fediverse users with dense local clusters and sparse remote connections
        print("  -> Generating 2,000-node synthetic social graph...")
        sizes = [500, 500, 500, 500] # 4 distinct communities
        probs = [[0.05, 0.001, 0.001, 0.001],
                 [0.001, 0.05, 0.001, 0.001],
                 [0.001, 0.001, 0.05, 0.001],
                 [0.001, 0.001, 0.001, 0.05]]
        
        graph = nx.stochastic_block_model(sizes, probs, seed=42)
        node_count = graph.number_of_nodes()
        edge_count = graph.number_of_edges()
        
        print(f"  => Graph Generated: {node_count} Nodes, {edge_count} Edges")

        # Step 2: Algorithmic Stress Test (Louvain Clustering)
        print("  -> Executing Louvain Modularity Clustering...")
        start_time = time.perf_counter()
        
        # This is the algorithm that will drive our "Fractal Memory Decay"
        communities = nx.community.louvain_communities(graph, seed=42)
        
        elapsed_time = time.perf_counter() - start_time
        
        # Step 3: Memory Telemetry Extraction
        current_mem, peak_mem = tracemalloc.get_traced_memory()
        peak_mb = peak_mem / (1024 * 1024)
        
        print(f"\n[SUCCESS] Algorithmic Execution Complete")
        print(f"  => Louvain Execution Time: {elapsed_time:.4f} seconds")
        print(f"  => Peak RAM Consumption: {peak_mb:.2f} MB")
        print(f"  => Communities Detected: {len(communities)}")
        
        # Print anatomical distribution of the clusters
        print(f"  => Cluster Sizes: {[len(c) for c in communities]}")

    except nx.NetworkXError as e:
        print(f"\n[ERROR] Graph Topology Failure: {str(e)}")
    except Exception as e:
        print(f"\n[FATAL] Unknown Physics Error: {type(e).__name__} - {str(e)}")
    finally:
        tracemalloc.stop()

if __name__ == "__main__":
    probe_graph_physics()
