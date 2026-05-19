- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6
Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper introduces MemTree, an algorithm that maintains a dynamic tree-structured memory for LLMs to organize, store, and retrieve information from conversations or documents. The tree is built online via hierarchical insertion with an adaptive depth-dependent similarity threshold, parent nodes are updated with LLM-based aggregation, and retrieval uses collapsed-tree search over all nodes. Evaluated on four benchmarks (MSC, MSC-E, QuALITY, MultiHop RAG), MemTree outperforms flat online memory methods (MemoryStream, MemGPT) and approaches or matches offline methods (RAPTOR, GraphRAG) while retaining the ability to update incrementally.

## Strengths

- **Novel combination of online hierarchical clustering with adaptive depth-dependent thresholding.** The threshold function θ(d)=θ₀e^{λd} is a principled mechanism that forces deeper nodes (which represent more specific information) to require higher similarity for merging, preserving hierarchical specificity. This design choice is well-motivated and distinguishes MemTree from flat embedding stores and from offline tree builders like RAPTOR. (Section 3.1)

- **Demonstrated superiority over online methods on extended conversations.** On MSC-E (200 rounds), MemTree consistently outperforms MemoryStream across all evidence-position bins, showing that its structured representation provides real benefits as dialogue length grows. This is the setting where the paper's claimed advantage — dynamic hierarchical organization — is most plausibly decisive. (Section 5.1, Table 2)

- **Strong temporal reasoning performance.** On MultiHop RAG temporal questions, MemTree surpasses all baselines including offline methods (RAPTOR, GraphRAG) and human-annotated evidence. This is a genuinely interesting result that suggests the tree structure may excel at organizing event sequences in a way that benefits temporal queries. (Section 5.3, Table 5)

- **O(log N) insertion with online update capability.** MemTree's logarithmic insertion complexity and ability to update incrementally (vs. full rebuild for RAPTOR/GraphRAG) is a clear operational advantage for real-time or streaming scenarios. The paper provides concrete timing comparisons showing 10-second per-insertion cost vs. hours for offline rebuilds. (Section 3.1, Figure 6)

- **Qualitative evidence of hierarchical organization.** Figures 2 and 3 show that deeper nodes store increasingly specific content (e.g., from "USMNT's defeat to Germany" → "specific insights on individual performances" → "detailed analysis of Gio Reyna's impact"), providing visual evidence that the learned structure is semantically meaningful. (Section 5, Figures 2–3)

## Weaknesses

### Fatal
None.

### Major

- **Missing ablation studies prevent attribution of performance to specific components.** The paper claims its results come from the tree structure, adaptive threshold, and LLM-based aggregation, but provides no controlled experiments to validate any of these design choices. Critical open questions include: (1) How does a flat (non-hierarchical) memory with the same chunking and embedding compare? (2) How sensitive is performance to θ₀ and λ — are these tuned per dataset or fixed? (3) What is the effect of replacing the LLM aggregator with simpler text concatenation or averaging? Without these ablations, the reader cannot determine which component drives the observed performance. This is the single most significant gap in the paper.

- **The claimed approximation guarantee (Theorem 1) is not substantiated for the actual algorithm.** The paper states Theorem 1 as an informal β/3 approximation of the Moseley-Wang revenue, drawing a connection to the OTD algorithm. However, MemTree deviates from OTD in fundamental ways: it uses semantic embeddings (not OTD's explicit inter/intra-subtree similarity), LLM-based aggregation (not centroid-based), and a threshold-based traversal rule (not OTD's insertion rule). The paper merely says it "relaxes" these comparisons without showing that the relaxation preserves the required properties. No proof is given. This theorem, as presented, is at best irrelevant and at worst misleading. It should either be formally proven for MemTree's actual operations or removed.

- **Core hyperparameters are unreported.** The base threshold θ₀, exponential rate λ, retrieval threshold θ_retrieve, and top-k are never stated for any dataset. Since θ(d)=θ₀e^{λd} is central to the algorithm's behavior (an exponential increase means thresholds grow rapidly; at depth 13 with any non-trivial λ, the threshold may become so large that traversal past moderate depths is impossible), the absence of these values makes it impossible to assess the algorithm's sensitivity or reproduce results.

- **The strongest claim — temporal reasoning superiority over all offline methods — rests on a single dataset (MultiHop RAG) with a single LLM (GPT-4o).** This is too narrow a foundation for the paper's headline contribution. Replication on another multi-document temporal reasoning benchmark (e.g., TempLAMA, SituatedQA) or with a second LLM (e.g., Llama-3.1 70B) would be needed to establish generality. As it stands, this result is suggestive but not conclusive.

### Minor

- **No error bars, confidence intervals, or significance tests on any reported accuracy.** Many performance differences are small (e.g., 59.8% vs 59.0% on QuALITY, or 0.5 percentage points on overall MultiHop RAG), and the evaluation uses an LLM judge (binary accuracy per sample), which introduces variance. Without variance estimates, it is unclear which differences reflect genuine algorithmic advantages vs. noise. While this is a common gap in LLM evaluation papers, it genuinely weakens the comparative claims.

- **The CPU parallelization claim is imprecise.** The paper states that "content aggregation and embedding updates for parent nodes can be parallelized on the CPU." However, the aggregation is explicitly "implemented as an LLM-based operation" — LLM inference is typically GPU-accelerated, not CPU-parallelizable in any practical sense. The embedding update (via `text-embedding-3-large` or `E5-Mistral`) can run on CPU but is commonly GPU-accelerated. This phrasing suggests an unrealistic efficiency profile and should be corrected.

- **How the "human-annotated evidence" baseline works in MultiHop RAG is underspecified.** The paper states that annotated evidence for temporal questions is "less precise" and leads to worse performance, but does not explain how this evidence is used — does it replace the retrieval step entirely? Is it fed directly as context? Without this clarification, the comparison with human evidence is difficult to interpret. (Section 5.3)

- **The conclusion overstates findings.** The claim that MemTree "consistently maintains high performance and demonstrates human-like knowledge aggregation" goes beyond what the evidence supports. The improvements over baselines are modest on most metrics, and "human-like" is not operationalized or measured in any way. (Section 6)

### Trivial

- The method section does not explicitly describe the first insertion (empty tree case). While it can be inferred from the algorithm's logic (no children → all similarities below threshold → attach as child of root), stating it explicitly would improve clarity.

## Nice-to-Haves

- A comparison with a simple vector store (e.g., FAISS with overlapping chunks) on document QA tasks would help isolate the value of hierarchical structure vs. any retrieval-augmented system.
- Demonstrating tree quality independently of downstream QA accuracy (e.g., measuring Moseley-Wang revenue or another tree quality metric) would give substance to the OTD connection without requiring a formal proof.
- A discussion of failure cases or limitations (e.g., does the tree structure hurt when information must be combined across very different subtrees?) would strengthen the paper.
- Reporting per-update latency (not just cumulative cost) would better frame the online vs. offline trade-off.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Missing FAISS baseline"** — The critic asserts the paper omits a "FAISS with overlapping chunks" baseline. MemoryStream already serves as a flat retrieval baseline; the paper's contribution is about structured vs. flat memory, and requiring a specific vector-store implementation is scope creep. *Removed: not a required baseline for the paper's core claim.*

- **"Root node handling underspecified"** — The paper states the root is a structural node with no content (line 99) and traversal starts from the root (line 109). The empty-tree case follows from the algorithm's logic. *Removed: the concern is addressed by the paper's description.*

- **"Missing appendix details (prompts, token budgets, etc.)"** — The parser strips supplementary materials from all papers; these details likely exist in the original submission. *Removed per rule about missing appendix content.*

- **"Short-context datasets (MSC, QuALITY) are weak evidence"** — The paper acknowledges these are short-context settings (lines 215, 221) and mainly uses them to compare memory management algorithms under controlled conditions, not as primary evidence for scalability. The headline claims rest on MSC-E and MultiHop RAG. *Removed: acknowledged by the paper, not central to claims.*

- **Strength about "theoretical approximation guarantee"** — This strength conflicts with the verified Major weakness that the guarantee is not substantiated for the actual algorithm. Per instructions: "when a strength and weakness disagree, the weakness wins." *Removed.*

- **Strength about "CPU parallelization"** — The CPU parallelization claim is identified as imprecise in the Minor weaknesses. The O(log N) insertion is the real strength; the CPU framing is misleading. *Removed: the valid core (O(log N)) is already covered as a strength.*

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add ablation studies as the highest priority.** At minimum: (a) compare against a flat (non-hierarchical) version of MemTree using the same chunking and retrieval, (b) fix the threshold to a constant to evaluate the adaptive threshold's value, and (c) replace the LLM aggregator with simple concatenation or averaging to measure its contribution. These experiments directly test whether the claimed benefits come from the tree structure, the adaptive threshold, or the aggregation method.

2. **Report θ₀, λ, θ_retrieve, and top-k for each dataset**, ideally with a sensitivity analysis showing how performance varies across reasonable ranges.

3. **Either provide a formal proof of the approximation guarantee for the actual MemTree algorithm (with semantic embeddings and LLM aggregation), or remove the theorem and instead provide an empirical analysis of tree quality** (e.g., comparing tree structure metrics to OTD's or measuring correlation with downstream accuracy).

4. **Add confidence intervals** (e.g., bootstrap over samples) for all main results. For differences as small as 0.5%, the reader needs to know whether the comparison is meaningful.

5. **Clarify the human-annotated evidence baseline** — specify whether it replaces retrieval or augments it, and whether the same LLM reads the evidence.

6. **Correct the CPU parallelization claim** to state where computation actually occurs (GPU for LLM aggregation and embedding, with parallelization across nodes on the same device).
