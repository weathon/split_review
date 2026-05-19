- Decision: Reject
- Avg Score: 3.75
- Scores: 6, 3, 3, 3
Now I have all the information needed. Let me compose the final consolidated review.

## Summary

This paper proposes the Graph Sequence Model (GSM), a unifying three-stage framework (Tokenization → Local Encoding → Global Encoding) for understanding and comparing graph-to-sequence models. It provides extensive theoretical analysis characterizing when Transformers, SSMs/RNNs, and different tokenization strategies (node vs. subgraph) are advantageous across counting, sensitivity, connectivity, and motif counting tasks. Building on these insights, the paper introduces GSM++, a hybrid model using Hierarchical Affinity Clustering (HAC) for tokenization, a Mamba+Transformer global encoder, hierarchical positional encodings, and a Mixture of Tokenization (MoT) module. GSM++ achieves strong empirical results, outperforming baselines in 8/10 benchmark tasks.

## Strengths

- **Unifying framework (GSM) for systematic comparison (Section 2).** The formal decomposition into Tokenization, Local Encoding, and Global Encoding captures virtually all existing graph sequence models and provides a common language for theoretical analysis. This is a genuine contribution to organizing the field.
- **Theorem 1 and Proposition 1 (Section 3.1) formally characterize counting capability.** The paper proves that recurrent models can count node colors iff their width ≥ number of colors, while non-causal Transformers without positional encodings cannot count. This cleanly identifies a fundamental difference between the model families.
- **Theorem 2 + Corollaries 1–2 (Section 3.2) prove SSM sensitivity and representational collapse.** The analysis shows SSMs have distance-sensitive sensitivity (advantage over Transformers) but collapse to first-token dependence as layers increase. This directly motivates the paper's hybrid design, and the U-shape effect finding is noteworthy.
- **Theorems 3–5 (Section 3.3) characterize connectivity task efficiency with precision.** Transformers solve connectivity with sublinear depth/width (Cor. 3), while recurrent/kernel/local-attention models require at least Ω(N^{1/8}) parameters (Thm. 3). However, with node-locality ≤ k, a single-pass recurrent model suffices (Thm. 4), whereas Transformers still need non-constant depth/width unless NC¹=TC⁰ (Thm. 5). These results rigorously connect tokenization ordering to model efficiency.
- **Theorems 6–7 (Section 3.4) prove tokenizer-task matching matters.** Subgraph tokenizers yield more parameter-efficient shortest path (Thm. 6) and motif counting (Thm. 7) solutions than node tokenizers, providing theoretical grounding for the observation that no single tokenizer is universally best.
- **Table 3 and Section 5.4: GSM++ achieves strong benchmark performance.** GSM++ (BFS/DFS) achieves first or second best on most datasets (Cora, Citeseer, CIFAR10, PATTERN, Peptides-Func), outperforming baselines in 8/10 cases. This provides direct empirical validation that the proposed enhancements yield a practically competitive model.
- **Ablation study (Table 4) quantifies component contributions.** Each component of GSM++ (HAC tokenization, hybrid encoder, hierarchical PE, MoT) is shown to improve performance, with HAC having larger impact on recurrent models — aligning with Theorems 4 and 8.
- **Large-scale comparison (Section 5.2, Figure 3) evaluating 54 model combinations across 7 datasets.** The finding that no model dominates supports the "no free lunch" conclusion and reinforces the theoretical analysis.

## Weaknesses

### Fatal
None.

### Major

- **Experimental setup for Tables 1 and 2 is underspecified.** These tables are central to the paper's empirical validation of its claims about tokenization and global encoder choice for synthetic graph tasks (node degree, cycle check, triangle counting, connectivity, color counting, shortest path). The paper names the tasks and states that parameters are fixed, but provides no information about graph sizes, graph distributions, number of samples/trials per condition, how metrics are computed, or whether results are averaged over multiple runs. Without these details the results are not reproducible and their reliability cannot be assessed. This is the most significant weakness in the current manuscript.

### Minor

- **Theorem 2's analysis uses HiPPO initialization but the model uses Mamba (selective SSM).** The sensitivity analysis (Theorem 2) is explicitly derived for SSMs "with HiPPO initialization," while GSM++ uses Mamba, which employs a selective scan mechanism with fundamentally different dynamics. The paper does not discuss whether the sensitivity bounds and representational collapse results carry over to selective SSMs. This creates a gap between the theoretical motivation and the actual architecture used.

- **MoT mechanism description is too brief in the main text.** The paper mentions a "discrete router that chooses top-2 tokenizations from τ for each node" with concatenation of encodings, but does not describe how the router is trained, how gradients flow through the discrete selection (e.g., straight-through estimator, REINFORCE, or Gumbel-Softmax), or the computational overhead. While additional details may exist in the appendix (stripped from this version), the main text should provide enough information for a reader to understand the mechanism.

- **No runtime or memory efficiency comparison despite claiming a "fast hybrid model."** The abstract and introduction emphasize efficiency advantages of SSMs and the hybrid design, but the paper reports no runtime, memory usage, or throughput measurements. Given the emphasis on efficiency as a motivation (quadratic vs. sub-quadratic complexity), the absence of any empirical efficiency data is a gap.

### Trivial
- The locality analysis (Definition 1, Theorems 4, 5, 8) focuses on edge tokenization with "node locality," but the HAC tokenization in GSM++ operates on nodes, not edges. The connection between these formulations is implicit and could be stated more clearly.

- Theorem 8 states there "exists a node embedding" that makes HAC ordering k-local — an existence claim. The paper does not check whether GatedGCN embeddings (used in practice) achieve low locality on real graphs. This does not undermine the paper because Theorem 8 is correctly framed as motivation rather than an empirical claim, but an explicit acknowledgment of this gap would strengthen the narrative.

## Nice-to-Haves

- Add a limitations paragraph discussing, e.g., HAC's worst-case O(n²) complexity, potential training complications from MoT's discrete routing, and boundary conditions where the theoretical benefits may not hold.
- The paper would benefit from an explicit statement about code/data release, particularly for the synthetic task generation.
- An empirical check of HAC locality (e.g., reporting average node locality on a few real graphs vs. random ordering) would directly support the motivation of Theorem 8.
- The normalization and ranking procedure for Figure 3 should be briefly described in the main text.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **Harsh Critic's claim that "the MoT mechanism is underspecified" as a Critical Issue:** The paper references "4 for additional information," indicating these details exist in the appendix (stripped by the parser). The main text description is brief but conveys the core idea. Demoted to Minor above.

2. **"Missing related works like GRIT, Exphormer":** Cannot verify these are missing — the appendix (stripped) may contain them. Removed per hard rules about unverifiable claims.

3. **"Missing proofs" / "no appendix":** The paper explicitly states proofs are in Appendices D, E, and F. These are stripped by the parser. Removed per hard rules.

4. **Formatting/parser artifacts:** The paper has garbled characters (e.g., `\bar{.}`, `\operatorname*{\ast}`) from PDF extraction. These are parser errors, not author issues. Removed per hard rules.

5. **"DFS traversals provide subgraph tokenization is not fully explained":** The paper actually explains this clearly — each DFS path from root to leaf is a sequence representing a hierarchy of clusters containing the leaf node. This is a reasonable description for a subgraph tokenization (each cluster in the path IS a subgraph). Removed as factually incorrect about the paper content.

6. **"Theorem 9 is informal" treated as a weakness:** The paper explicitly labels it "THEOREM 9 (INFORMAL)." The authors are upfront about its nature; this is not a flaw.

7. **Strength Finder's generic strengths about "important problem":** Dropped as generic and not specific to this paper's concrete contributions.

8. **Reproducibility nitpicks about code release and hyperparameters:** These are standard in the field and not unique weaknesses of this paper. Moved above to Nice-to-Haves where warranted.

## Novel Insights

The harsh critic raises a genuinely useful observation that the paper's field lacks: the mismatch between the HiPPO-based sensitivity analysis (Theorem 2, Corollaries) and the selective SSM (Mamba) used in the final architecture. While the paper frames the theory as motivation and the ablation studies independently validate the hybrid design choice, explicitly addressing whether the theoretical bounds on representational collapse extend to selective state-space models would strengthen the bridge between theory and architecture. Beyond this, the reviews do not surface an insight that the paper itself does not already articulate.

## Suggestions

1. **Add experimental specification for Tables 1 and 2:** Provide graph size ranges, generation method, number of trials, metric computation, and standard deviations. This is the single highest-leverage improvement.
2. **Clarify whether Theorem 2's analysis applies to selective SSMs (Mamba):** Add a brief discussion acknowledging the gap between HiPPO-based analysis and the selective SSM used, and either extend the analysis or explain why the qualitative conclusions still hold.
3. **Expand MoT description in the main text:** Briefly describe the router architecture, gradient estimation method, and computational cost (even one paragraph).
4. **Add a runtime/memory efficiency table:** A simple comparison of inference time per sample and peak memory for GSM++ vs. baselines would substantiate the claimed efficiency advantages.
5. **Add a limits section:** A brief discussion of HAC's complexity, boundary cases for theoretical results, and the gap between existence claims (Theorem 8) and practice would improve the paper's completeness.
