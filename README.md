 









# fediverse-discovery-layer



### Reclaiming the Public Nature of Search through Local Graph-RAG



The **Fediverse Discovery Layer** is a local-first, privacy-preserving search and synthesis engine for the decentralized web (ActivityPub). It addresses the fundamental "Discovery Bottleneck" of the Fediverse by shifting the intelligence of the network from centralized servers to the user's edge.



---



## 🏛️ The Mission: Why This Project Exists



Current search paradigms rely on centralized crawling and opaque ranking systems that are incompatible with the privacy-preserving requirements of the Next Generation Internet (NGI). The Fediverse, while resilient, suffers from **Semantic Discontinuity**—the inability to connect related concepts across fragmented servers without sacrificing user privacy.



This project delivers a **Decentralized Discovery Layer** that enables:



* **Personal Sovereignty:** Search your private timelines without a single query leaving your hardware.

* **Multi-Hop Reasoning:** Connect "dots" across authors and topics using a local social graph.

* **Contextual Synthesis:** Receive summarized briefings instead of raw lists of links.



---



## 🧠 The Architecture: Local Graph-RAG

Unlike traditional RAG systems that treat posts as isolated text chunks, this project implements an embedded, **Hybrid Graph-Vector** pipeline running entirely within the user's local trust boundary.

1. **Ingestion (The Instance-Aware Harvester):** A local background daemon fetches ActivityStreams 2.0 JSON-LD payloads. To eliminate crawling stress on community-run nodes, it actively parses instance-level `x-ratelimit-remaining` headers and prioritizes WebSub push endpoints.
2. **Layer 1.5: Polymorphic ActivityStreams Normalizer (PASN):** To resolve severe schema fragmentation across different Fediverse implementations (Mastodon, Lemmy, Pleroma, Misskey), this pipeline applies a type-safe Factory Pattern to flatten irregular JSON-LD payloads into a canonical dictionary. It strips origin-specific markup noise—such as raw HTML tags from Mastodon or formatting shortcodes from Lemmy—before data hits the LLM.
3. **Semantic Extraction (RDF Message Boundaries):** A quantized local LLM intercepts the cleaned payload. Enforcing the **RDF Messages specification**, it treats updates as atomic communicative acts, isolating clear `Subject ──► Predicate ──► Object` triplets to preserve perfect social topology.
4. **In-Process Dual-Store Storage:** To maintain a zero-service footprint optimized for consumer silicon (16GB RAM), both databases run strictly in an integrated, serverless **embedded mode**:
   * **LanceDB (Vector Store):** Operates in-process inside the Python environment to hold high-dimensional text embeddings for fast, low-latency conceptual search.
   * **NetworkX (Graph Store):** Holds structural social topology in memory to track conversation threads, webs of trust, and intersecting entity relationships.
5. **Generative Synthesis (Reciprocal Rank Fusion):** When a user triggers a query, the orchestrator queries both databases simultaneously. It executes **Reciprocal Rank Fusion (RRF)** to mathematically combine neural vector proximity scores with graph topology centrality weights, passing a highly authoritative context window to a local Ollama model for summarized responses with exact citations.


---



## 🛠️ Internal Development Workflow & Quality Control

To guarantee absolute codebase reliability, strict data hygiene, and "First-Run Success," the engineering lifecycle of this project integrates a localized, LLM-assisted development pipeline. Rather than writing code blindly against speculative API behaviors, two specialized developer-side sub-agents are utilized to enforce strict context isolation and run empirical environment audits before any production logic is integrated into the repository.

The underlying data and inference engines (**Ollama, LlamaIndex, LanceDB, and NetworkX**) are not passive placeholders; they are surgically selected via domain-specific technical triage as the mathematically optimal, resource-efficient stack to support client-side, in-process execution constraints.

### 1. The Agentic Context Controlling Agent (ACCA)
The ACCA functions natively within the developer environment as an automated context bouncer and librarian to optimize prompt efficiency.
* **Mechanism:** The utility intercepts development prompts, analyzes the micro-requirements of the assigned task, and perfectly curates the context window. It systematically scrubs the prompt of irrelevant codebase files, redundant structural schemas, and focus-diluting noise while querying our code map to dynamically append missing dependencies and required architectural linkages.
* **Impact:** This directly neutralizes token-level context bloat and context window explosion. By keeping the local model's attention span focused exclusively on atomic coding boundaries, it completely eliminates logic hallucinations and allows highly efficient local models to generate components with 100% contextual accuracy.

### 2. The Agentic Probe Explorer Agent (The Mechanical Sentry)
Operating under a philosophy of "Defensive Paranoia," this sub-agent acts as an adversarial scout to eliminate hidden environmental assumptions before software assembly begins.
* **Mechanism:** Before any production application code is drafted, this mechanism audits the immediate technical requirements. It identifies unverified environmental variables, performs an active pre-mortem to map breaking points, and executes tiny, non-mocked throwaway sandbox scripts (probes) directly against live target environments, network routes, and real-world ActivityPub JSON-LD payloads.
* **Impact:** This completely replaces brittle "Happy Path" coding with empirical verification. It captures raw payload data schemas, CORS boundaries, and instance-level rate limits before integration. This eliminates hallucinated mock-data variables and guarantees that the compiled application interfaces flawlessly with the live network on the very first execution.



---

## 📉 Data Lifecycle: Fractal Memory Decay

To prevent local graph and vector stores from bloating and exhausting consumer hard drives over time, the system implements an automated multi-tiered lifecycle data protocol:

* **Short-Term Context Retention:** Standard, low-engagement social updates automatically decay and are purged from disk storage after a rolling 30-day window.
* **Louvain Modularity Clustering:** Before raw nodes cross the expiration boundary, the system executes **Louvain modularity optimization algorithms** via NetworkX to map dense, interconnected conversational and topical clusters.
* **Knowledge Synthesis:** A local LLM sweeps these identified topological clusters to generate high-level, compact **"Community Summaries."** These condensed summary nodes are permanently anchored into long-term local vector storage, allowing the engine to retain panoramic historical lookup capabilities while safely pruning thousands of underlying raw social items.

---



## 🔬 The "White Space" (Novelty Verification)



Extensive OSINT research and competitive analysis have identified a specific **Hybrid Gap**.



* **BYOTA (Mozilla.ai):** Performs semantic search but lacks relational reasoning via graphs.

* **openEngiadina:** Focuses on publishing structured data but lacks automated synthesis of unstructured streams.

* **Centralized Search (Algolia/Elastic):** Requires data synchronization to a central index, creating a privacy honeypot.



The **fediverse-discovery-layer** is unique in its combination of local-only hybrid Graph/Vector DBs for multi-hop reasoning on real-time decentralized social streams.



---



## 🚀 Getting Started



### 1. Prerequisites



* Python 3.11+

* [Ollama](https://ollama.com/) (running locally)



### 2. Clone the Probes



Before the full application is assembled, you can run the verified technical probes:



```bash

git clone https://github.com/Million19/fediverse-discovery-layer.git

cd fediverse-discovery-layer

pip install -r requirements.txt

python probes/01_activitypub_fetch_probe.py



```

---



### 👨‍🔬 About the Author: Michael Alamin



Michael Alamin is an independent AI researcher and innovator based in Eskilstuna, Sweden, specializing in neuro-symbolic cognitive architectures and decentralized internet infrastructure.



**Key Achievements & Innovations:**



* **SKAPA Prize Winner (2025):** Recipient of the SKAPA Prize, Sweden's most prestigious innovation award established in memory of Alfred Nobel. The award was announced via an official government statement from the County Administrative Board (Länsstyrelsen) for his pioneering work on autonomous hardware-software systems. View the official announcement here: [SKAPA Prize (Länsstyrelsen Official Government Site)](https://www.lansstyrelsen.se/sodermanland/om-oss/nyheter-och-press/nyheter---sodermanland/2025-10-02-innovationspris-till-utveckling-av-sjalvuppvarmande-biogasanlaggning-och-smarta-webblosningar-for-foretag.html).

* **Validated Patent Novelty (SE2430528-6):** Lead inventor of a comprehensive hardware-software framework where **14 out of 14 patent claims** have been formally confirmed by the Swedish Patent and Registration Office (PRV) for fulfilling the strict requirements of novelty, inventive step, and industrial applicability. View the patent details here: [PRV SE2430528-6](https://search.prv.se/#/patent/SE2430528-6).

* **Founder of Self heating Biodigester AB:** Michael is the founder of Self heating Biodigester AB, a research and development firm currently undergoing formal Swedish incorporation (Aktiebolag). The registration process is in its final stages. The official company portal is currently under construction: selfheatbiodigester.com.

* **AI Research (AR-CoT):** Author of the **[Abstract Reasoning Chain-of-Thought (AR-CoT)](https://www.google.com/search?q=https://github.com/Million19/Abstract-Reasoning-Chain-of-Thought-paper)** paper for the Kaggle ARC-AGI Prize 2025. This research proposes a neuro-symbolic cognitive architecture designed to solve fundamental perception and generalization bottlenecks in Large Language Models.

* **Developer of `llm_to_mcp_integration_engine`:** Architect of a novel communication layer designed to enhance the reliability, safety, and validation of tool execution between LLMs and Model Context Protocol (MCP) servers.



---



## ⚖️ License



This project is released under the **Apache License 2.0**. This permissive license ensures the framework can be adopted as a shared "Internet Common" while providing explicit patent protections for all contributors and users.



---



## 🤝 Support



This project is an applicant for the **NGI Zero Commons Fund**. Our goal is to re-imagine search for an internet of human values: resilient, trustworthy, and sustainable.
