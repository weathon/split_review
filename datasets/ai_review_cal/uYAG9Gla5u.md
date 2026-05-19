- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 6, 6, 3
Now I have all the information I need. Let me verify the key claims against the paper and produce the consolidated review.

---

## Summary

This paper proposes MEGA-GNN, a message-passing framework for multigraphs (graphs with parallel edges) that employs a **two-stage aggregation** in each layer: first, parallel edges between a given pair of nodes are aggregated via an EdgeAgg function; then the resulting per-neighbor embeddings are aggregated at the node level. This addresses two limitations of prior multigraph GNNs — Multi-GNN's lack of permutation equivariance without edge ordering, and ADAMM's inability to preserve per-edge features across layers. The paper provides theoretical guarantees (permutation equivariance generally, universality under strict total edge ordering) and demonstrates strong empirical gains on AML transaction datasets (up to ~12 percentage points F1 improvement over Multi-PNA) while matching state-of-the-art on an Ethereum phishing detection task.

## Strengths

1. **Provably permutation equivariant while prior multigraph GNN is not**: Theorem 1 establishes that MEGA-GNN is permutation equivariant when EdgeAgg and AGG are permutation-invariant, directly addressing Proposition 1 which shows that Multi-GNN's port-numbering scheme lacks this property. This is a genuine theoretical advance over the prior state-of-the-art.

2. **Universality coexists with permutation equivariance**: Lemma 1 and Theorem 2 (Corollary 1) prove that MEGA-GNN can compute unique node IDs in connected multigraphs given a strict total ordering of edges, and is therefore universal under the conditions of Loukas (2020). Crucially, this universality does not sacrifice permutation equivariance — a trade-off that Multi-GNN cannot resolve.

3. **Significant empirical gains on AML transaction classification**: On the four AML datasets (Table 1), MEGA-GNN variants consistently and substantially outperform the previous best method. MEGA-PNA achieves **78.26 ± 0.11** on AML Medium HI versus Multi-PNA's **66.48 ± 1.63** — an absolute improvement of ~12 percentage points. The improvements are consistent across all four dataset configurations with low variance.

4. **Preserves and updates individual edge features across layers**: Unlike ADAMM (which collapses parallel edges into a single super-edge before message passing), Equation 6 updates each individual edge feature using the aggregated embedding. This enables edge-level tasks (e.g., transaction classification) and repeated multi-edge aggregation in deeper layers, which ADAMM cannot support.

5. **Ablation study cleanly isolates the core mechanism's contribution**: Table 2 (ablation) shows that MEGA-GIN and MEGA-PNA without bi-directional MP and without Ego-IDs already outperform most baselines. For example, MEGA-GIN (Unidirectional MP) scores 69.98 on AML Small HI, while Multi-GIN scores 64.79. This confirms that the two-stage aggregation itself drives the performance gain, not auxiliary components.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are well-supported by theory and experiments, and no verified weakness undermines the central contribution.

### Minor

1. **"Artificial nodes" terminology creates unnecessary conceptual ambiguity.** The paper introduces `V^{art}` (Equation 3) and defines `h_{ij}` as the output of EdgeAgg over parallel edges (Equation 4). The formalism is mathematically clear as a two-stage aggregation: EdgeAgg pools parallel edges, then AGG pools across neighbors. However, labeling this mechanism as "artificial nodes" suggests a new entity in the computational graph without specifying whether these nodes have their own parameters, participate in message passing as senders/receivers, or are merely a notational convenience. The method is implementable from Equations 4–6 regardless, but the framing could confuse readers and the paper would benefit from stating explicitly whether artificial nodes exist as actual computational entities or are a narrative device.

2. **ETH node classification results are not statistically distinguishable from Multi-PNA.** MEGA-PNA achieves 64.84 ± 1.73 vs. Multi-PNA's 64.61 ± 1.40 (Table 2). The difference (0.23) is well within one standard deviation. The abstract appropriately says "on par" and the conclusion says "slightly improving," but the discussion in Section 4.2 states that MEGA-PNA "surpasses" Multi-PNA, which overstates the evidence. The authors should either report a significance test or downgrade the claim to "no statistically significant difference." This does not weaken the paper — the AML results carry the empirical contribution — but precise language would strengthen credibility.

3. **No discussion of asymptotic complexity.** The throughput analysis (Figure 4) shows wall-clock speed, which is useful. However, the paper does not discuss how the two-stage aggregation affects asymptotic memory or computation complexity relative to standard message-passing. Each unique neighbor pair now involves an additional aggregation over parallel edges (EdgeAgg), which practitioners would need to understand for scaling decisions. This is a straightforward addition.

### Trivial
None.

## Nice-to-Haves

- **Controlled ablation for iterative pooling**: The paper could add an ablation where multi-edge aggregation is applied only once (layer 1) and then a standard GNN runs on the resulting simple graph, to more directly isolate whether iterative multi-edge aggregation matters beyond one-time pooling. Currently the comparison to ADAMM confounds this with other differences (bidirectional MP, per-edge updates).
- **Brief note on the ADAMM trade-off**: The critique of ADAMM is accurate, but noting that ADAMM's super-edge collapse could be a scalability design choice (fewer edges in message passing) would make the discussion more balanced.
- **Explicit invariance requirements**: Theorem 1 should explicitly state in the main text that EdgeAgg must be permutation-invariant over the multiset of parallel edges, and AGG over the set of neighbors. (The theorem already says "permutation invariant EdgeAgg and AGG functions" — this could be slightly expanded for clarity.)

## Removed Points

- **Harsh critic's note about "proofs in appendix"**: The critic mentions proofs being deferred to the appendix and calls this "acceptable." This is standard practice and not a weakness. Removed.
- **Harsh critic's note about Ego-ID performance drop interpretation**: The critic suggests the paper should explain why Ego-IDs sometimes hurt (e.g., MEGA-PNA on AML Small HI). This is a reasonable curiosity but not an actionable weakness — the paper already reports the phenomenon. Removed as not substantive enough for a weakness.
- **Harsh critic's claim that the paper overclaims ETH results in the discussion/conclusion**: The paper's abstract says "on par" and the conclusion says "slightly improving." These are appropriate. Only one sentence in Section 4.2 uses "surpassing" which is slightly strong; this is already captured in Weakness #2 above. The broader claim of overclaiming is not supported by the paper's actual language.

## Novel Insights

The two-stage aggregation framework cleanly decouples two fundamentally different types of information in multigraphs: what distinguishes parallel edges (e.g., individual transaction amounts, timestamps) from what distinguishes different neighbors (e.g., aggregate behavior patterns from each counterparty). This separation mirrors a natural inductive bias in financial and communication networks where both levels carry distinct signals — for instance, the maximum single payment from a sender and the sum of that sender's payments reveal different fraud indicators. The paper shows that this hierarchy cannot be recovered by a single-stage node-level aggregation, which provides a principled explanation for the large empirical gains on AML data.

## Suggestions

1. Clarify the "artificial nodes" terminology: either state explicitly that they are real nodes in an augmented graph with a specification of how their features are initialized/updated, or drop the metaphor and present the method directly as two-stage aggregation (EdgeAgg then AGG) without introducing a new node type.
2. Add a statistical significance test (e.g., paired bootstrap) for the ETH comparison, or soften the claim to "matching" state-of-the-art.
3. Add a brief asymptotic complexity analysis (big-O or otherwise) for the two-stage aggregation relative to standard MPNNs.
