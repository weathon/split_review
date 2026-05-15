Now I will produce the final consolidated review.

## Summary

This paper proposes SnLH (Synergy Low-High Frequency Cross-Domain Network), a framework for unsupervised graph domain adaptation that explicitly separates and leverages low- and high-frequency spectral signals from graphs. The core premise is that low-frequency components capture domain-shared features while high-frequency components encode domain-specific information. The framework uses specially designed filters to decouple these signals, applies mutual information maximization on low-frequency features across domains, and employs contrastive learning on high-frequency features. Experiments on multiple benchmark datasets (Mutagenicity, NCI1, and six other TUDatasets) show that SnLH outperforms 13 baselines on 24 of 32 cross-domain tasks.

## Strengths

- **Principled spectral signal disentanglement**: The paper provides mathematically grounded low-pass and high-pass filters (Section 4.1) derived from the normalized adjacency matrix, with a clear derivation showing that the low-frequency filter corresponds to summing node and neighbor features while the high-frequency filter captures their difference. This gives the method a clean theoretical foundation.

- **Strong empirical results across diverse benchmarks**: On three evaluation suites totaling 32 cross-domain tasks, SnLH achieves the best performance on 24 tasks and obtains an average improvement of ~3% over the best competitor. The baselines include a comprehensive set of 13 methods spanning kernel approaches (WL), spatial GNNs (GCN, GIN, CIN, GMT), classical DA methods (CDAN, ToAlign, MetaAlign), and specialized UGDA methods (DEAL, CoCo, To-UGDA, A2GNN).

- **Ablation and controlled experiments validate the design choices**: The ablation study (Section 5.3, Tables 4–5) systematically removes each component—cross-domain contrastive learning, source/target mutual information, low-/high-frequency extraction, and replacing filters with GCN—confirming that all modules contribute positively. Additionally, the controlled experiment in Section 5.4 tests six frequency-signal combinations for the two modules, and the best configuration (L‑H: low-frequency for mutual information, high-frequency for contrastive) matches the paper's hypothesized spectral roles.

- **Hyperparameter analysis provides practical guidance**: The sensitivity study on the low-/high-frequency mixing ratio λ (Section 5.5, Figure 4) shows performance increasing up to λ=0.8 then plateauing, supporting the claim that low-frequency information is the dominant factor for cross-domain generalization while a complementary high-frequency component still helps.

## Weaknesses

### Fatal
None.

The paper's core methodology is implementable in principle, and the core claims are supported by the experimental results. The issues identified below are significant gaps in presentation and justification, but they do not invalidate the overall contribution.

### Major

1. **Missing mechanism for positive pair identification in the contrastive loss** (Section 4.3, Equation 11). The high-frequency contrastive loss is written as:

   $$\mathcal{L}_{high}^{cl} = \sum_{i=1}^{N_s} \log \frac{s(h_i^s, h_i^t)}{\sum_{j=1}^{N_t} s(h_i^s, h_j^t)} + \sum_{i=1}^{N_t} \log \frac{s(h_i^t, h_i^s)}{\sum_{j=1}^{N_s} s(h_i^t, h_j^s)}$$

   This treats $h_i^s$ and $h_i^t$ as positive pairs indexed by $i$. The paper states that "we benefit from constraining the cross-domain low-frequency information, allowing us to identify positive samples in the target domain that share the same semantics as those in the source domain" (line 171), but *no algorithm or mechanism is described* for how these positive pairs are actually established. In unsupervised GDA, source and target graphs are not naturally paired, and simply pairing by index within a batch has no semantic justification without an explicit pseudo-labeling or matching procedure. This is a significant gap: a reader cannot reproduce the method from the description, and the claimed benefit of the low-frequency module for pair identification is asserted without evidence.

2. **Central motivating experiment (Figure 1) lacks methodological description**. The paper claims to have discovered that "low-frequency topology signals signify the shared cross-domain features, while the high-frequency information indicates domain-specific knowledge" through an experimental study shown in Figure 1. However, the paper provides no description of how this experiment was conducted—what model was used, how frequencies were separated, what metric was measured. The figure itself is garbled in the extracted text and the caption is generic. Since this observation is the primary motivation for the entire framework, the inability to independently assess or reproduce this experiment is a substantial weakness. The paper would be strengthened by presenting this evidence with full experimental details (e.g., spectral energy distributions, t-SNE plots, or quantitative metrics).

### Minor

1. **Imprecise mathematical specification of the low-frequency mutual information loss** (Section 4.2, Equation 8). The KL divergence is written as:

   $$D_{KL}(P_s(l^s) \parallel P_t(l^s)) = \sum_i P_t(l_i^s) \log \frac{P_t(l_i^s)}{P_s(l_i^s)}$$

   Several issues: (a) the notation $D_{KL}(P_s \parallel P_t)$ but the sum uses $P_t$ outside the log and $P_t/P_s$ inside—this is structurally $D_{KL}(P_t \parallel P_s)$, not $D_{KL}(P_s \parallel P_t)$; (b) the distributions are evaluated on source samples $l_i^s$, which conflates the sample space. While the high-level concept (aligning source and target low-frequency distributions) is clear, the mathematical formulation as written cannot be directly implemented. The use of $\tau_{kd}^2$ as a scaling factor on the divergence (rather than a temperature inside a softmax) is also unusual and unexplained.

2. **No comparison with spectral-domain methods and weak novelty justification**. The paper claims to be "the first to study the spectral signal on the graph-level UGDA task" (line 47), but the related work section (Section 2.2) does not engage with any spectral graph methods or spectral domain adaptation approaches. While the absence of spectral GDA baselines in the experiments is natural if no prior method exists, the novelty claim itself is not situated within a detailed discussion of spectral graph learning. The paper's contribution is better stated as the finding that low- vs. high-frequency signals play distinct roles in UGDA, rather than a broad claim of being "first" to study spectral signals.

### Trivial

- The filter design (Section 3.2–4.1) transitions between the Laplacian eigendecomposition and filters defined on the normalized adjacency matrix $\widetilde{A}$ without clearly connecting why this specific choice ($S_{low}=I_n+\widetilde{A}$, $S_{high}=I_n-\widetilde{A}$ with $\mu=1$) is optimal for domain adaptation.
- The problem definition (Section 3.1) cuts off mid-sentence at "where $\mathcal{V}_i^s$ represents" (a likely parser artifact) but should be verified against the original submission.

## Nice-to-Haves

- An explicit description of the positive pair selection mechanism would resolve the most significant ambiguity. Even a simple approach (e.g., using the source classifier's predictions on target samples as pseudo-labels, or nearest-neighbor matching in the low-frequency feature space) would make the method reproducible.
- Visual evidence supporting the core spectral claim would be valuable: e.g., spectral energy plots showing that low-frequency feature distributions overlap across domains while high-frequency distributions are domain-specific, or t-SNE visualizations of the low- and high-frequency features before and after adaptation.
- Ablation comparing the spectral filters against two independent learnable linear transforms (without frequency constraints) would more cleanly isolate whether the spectral decomposition itself matters versus simply having two separate processing channels.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Criticism that the "first to study spectral signal" claim is likely false**: The critic asserted "there exist works on spectral alignment, graph filter banks, and spectral GNNs applied to domain adaptation" without providing specific citations. Per meta-review policy, I cannot verify the existence of unnamed works, and the paper's claim is appropriately hedged ("to the best of our knowledge"). This criticism is removed as unsubstantiated.
- **Criticism that the paper does not discuss whether label sets differ across domains (open-set/partial DA)**: The paper defines standard UGDA where label spaces are shared. Requiring discussion of open-set scenarios is scope creep beyond what the paper claims to address.
- **Criticism about the problem definition sentence cutting off**: This is a PDF parsing artifact, not an author error.
- **Criticism that baselines include no spectral GDA methods**: If the paper is indeed the first spectral method for graph-level UGDA, no such baselines exist. This is not a valid criticism.
- **Criticism about missing appendix/proofs**: The appendix was likely stripped during PDF extraction.
- **Criticism about only analyzing $\lambda$ for hyperparameters**: Varying all hyperparameters is impractical; analyzing the key design parameter is standard practice.

## Novel Insights

The reviews collectively surface an important tension: the paper's strongest claim—that low-frequency signals are domain-shared while high-frequency signals are domain-specific—is also its least well-supported piece of evidence. The harsh critic correctly identifies that Figure 1 is described without methodological detail, while the strength finder correctly identifies this finding as the "single most important piece of evidence" motivating the work. This tension reveals that the paper would benefit substantially from either (a) deferring the spectral finding to a preliminary experiment section with full details, or (b) reframing the contribution around the method itself (SnLH) rather than the empirical discovery. A genuinely novel observation—separate from the review process—is that the synergy pattern (using low-frequency for alignment and high-frequency for contrastive discrimination) forms a natural division of labor that mirrors the spectral bias of graph neural networks (which are inherently low-pass filters), suggesting the method may be exploiting and complementing a known inductive bias.

## Suggestions

1. **Clarify the positive pair selection mechanism for contrastive learning** and add an experiment validating the accuracy of the pair assignments (e.g., using oracle labels).
2. **Provide full experimental details for the motivating spectral study (Figure 1)**, including the model used, frequency decomposition method, and evaluation metric. Alternatively, add spectral energy plots or t-SNE visualizations to directly support the claim.
3. **Fix the KL divergence formulation** (Equation 8) to use a standard cross-entropy or mutual information objective, or clearly describe how the probability distributions $P_s$ and $P_t$ are estimated from samples.
4. **Tone down the "first to study spectral signal" claim** to something verifiable like "first to systematically investigate the distinct roles of low- and high-frequency spectral signals in graph-level UGDA."

## Score and Decision

The paper presents an interesting idea with a principled filter design and strong empirical results across multiple benchmarks. However, the two major weaknesses—the unexplained positive pair mechanism for the contrastive loss and the poorly documented motivating experiment—are significant gaps that undermine reproducibility and the strength of the core claim. These issues are addressable in revision but are too substantial to overlook in the current form.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>