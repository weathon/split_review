- Decision: Reject
- Avg Score: 4.67
- Scores: 6, 3, 5
Now I have all the information needed to produce the consolidated review.

## Summary

This paper proposes DHCF, a model for multi-behavior collaborative filtering that jointly performs intent disentanglement via a parameterized heterogeneous hypergraph (with learnable hyperedge embeddings per behavior type) and hierarchical contrastive learning (node-level and graph-level) with adaptive augmentation via a meta-network. The method is evaluated on three public datasets against 18 baselines, with ablation studies, robustness analysis, efficiency comparisons, and a case study. The code is provided.

## Strengths

- **Parameterized heterogeneous hypergraph for intent disentanglement**: The paper introduces a learnable hypergraph structure (Section 3.3–3.4, Eq. 2–3) where multi-channel hyperedges per behavior type are generated via learnable weight matrices, enabling fine-grained disentangled representations across multiple interaction types. The ablation study (Figure 2, "w/o-InDi") shows substantial drops in NDCG and HR when this component is removed, directly supporting its contribution.

- **Hierarchical contrastive learning with adaptive augmentation**: The model jointly optimizes node-level (Eq. 7) and graph-level (Eq. 8) contrastive objectives, with a meta-network (Eq. 6) for personalized cross-behavior transformation. The ablation variants (w/o-NCL, w/o-GCL, w/o-Meta in Figure 2) each degrade performance, confirming that all components contribute. The robustness analysis (Figure 3) demonstrates consistent improvements across user sparsity groups.

- **Significant and consistent empirical gains**: DHCF is evaluated on three datasets (Beibei, Tmall, IJCAI) against 18 baselines from 6 research lines, with reported statistical significance (p < 1.6e⁻⁵). The ablation (Figure 2) confirms the full model achieves the best performance across all variants. Efficiency analysis (Table 2) shows competitive or better computational cost compared to top baselines.

## Weaknesses

### Fatal
None.

### Major

1. **Insufficient differentiation from MHCN (Yu et al., 2021).** MHCN is itself a hypergraph-based contrastive learning method designed for multi-behavior recommendation, yet the paper only lists it among 18 baselines (Section 4.1) without any architectural comparison in the Related Work or Methodology sections. The Related Work (Section 2) does not mention MHCN at all in the context of contrastive learning or hypergraph methods. Since both DHCF and MHCN use hypergraph message passing and contrastive objectives over multiple behavior types, the paper needs to explicitly describe how DHCF differs — specifically, the parameterized (learnable) hyperedge construction vs. MHCN's fixed hypergraph and the hierarchical contrastive design. Without this positioning, the novelty contribution is unclear. This is a framing/positioning weakness, not a methodological flaw.

2. **Overclaimed "theoretical analysis."** The contributions list claims "We provide theoretical analyses to demonstrate how our hypergraph-based representation disentanglement enriches and enhances the behavior-wise contrastive learning." However, Section 3.8 ("In-Depth Discussion of DHCF") contains only two brief (5-line) paragraphs that state high-level intuitions without any formal proof, derivation, or rigorous argument. This does not meet the standard of a theoretical analysis. The content itself is not wrong — it offers reasonable intuition — but it is misrepresented. The claim should be removed from the contributions or substantially expanded with genuine formal reasoning.

### Minor

3. **Meta-network parameterization is underspecified.** Equation (6) introduces parameters \(\mathbf{W}_{i,k'}^{(u,l)} \in \mathbb{R}^{d \times d}\) with a user-subscript \(i\), which suggests per-user weight matrices — this would be \(I \times K \times L \times d^2\) parameters. The text (Section 3.6) simply calls them "trainable parameters corresponding to the \(k'\)-th type of auxiliary behaviors" without clarifying whether they are per-user or shared. If shared, the notation is misleading; if per-user, the computational cost needs justification. This should be clarified.

4. **Case study visualization methodology not described.** Section 4.7 states embeddings are "projected into different colors" but does not specify the dimensionality reduction technique used (t-SNE, UMAP, PCA, or other). The interpretability claims about "global dependencies" rely on external item-side knowledge (categories/brands) that DHCF does not use, making it unclear whether the embedding proximity is learned from interaction data alone or conflated with side information.

5. **Notation inconsistency in Section 3.3.** The paragraph introducing Eq. (2) uses \(\mathbf{E}_k^{(u)}\) to denote behavior-aware embeddings composed from \(\bar{\mathbf{z}}_i^{(u)}\), but the equation itself (and subsequent text) uses \(\mathbf{Z}_k^{(u)}\). These appear to refer to the same quantity, creating confusion.

### Trivial

- The dropout operator \(m_{i,j}\) in Eq. (1) is clarified as being from SGL (Wu et al., 2021a) but the sentence structure is slightly garbled in the extraction; the original likely reads cleanly.
- Section 3.8 contains a stray "5." at the end of the second paragraph, likely a formatting artifact.

## Nice-to-Haves

- A direct architectural comparison table or paragraph contrasting DHCF with MHCN would substantially strengthen the paper's positioning.
- Reporting standard deviations or confidence intervals for the main results would strengthen the statistical rigor.
- Clarifying why LeakyReLU is chosen over other activations for the hypergraph propagation would be a helpful detail.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Table 1 (main results) is absent from the extracted text"** — This is a parser artifact. The original submission has the table as an embedded image (visible at line 170: `![](images/...jpg)`). Per Hard Rules, parser artifacts are not author errors.
- **"Missing appendix/proofs in appendix"** — Parser strips supplementary sections from all papers. These exist in the original submission.
- **"Missing comparison with MHCN on efficiency (Table 2)"** — Table 2 is an efficiency comparison; including every baseline is impractical. The paper compares against the best-performing baseline (KHGT) and several others. This is reasonable scope.
- **"Hypergraph adjacency normalization not defined"** — The text in Section 3.4 uses \(\tilde{\mathcal{H}}^{(u)}\) and states it is the normalized version implicitly; the "presumably" framing by the reviewer confirms this is speculation rather than a concrete error.
- **"Number of latent intents equal across behavior types"** — This is a standard experimental design choice; requiring different numbers per behavior type is speculative scope creep.
- **Strength Finder's claim about "Theoretical analysis of the learning objectives"** — This conflicts with verified Weakness #2 (overclaimed theory). Per instructions, when a strength and weakness disagree, the weakness wins. Removed.
- **Generic strength claims** (e.g., "this paper addresses an important problem") — removed as superficial.

## Novel Insights

None beyond the paper's own contributions. The Harsh Critic and Strength Finder both identify the core empirical contributions (parameterized hypergraph + hierarchical contrastive learning) but neither provides a genuinely novel analytical insight that reconceptualizes the work.

## Suggestions

1. Add a dedicated paragraph in the Related Work or Methodology section that explicitly compares DHCF's architecture with MHCN: contrast the parameterized (learnable) hyperedge construction against MHCN's fixed hypergraph, and explain how the hierarchical (node-level + graph-level) contrastive paradigm differs from MHCN's contrastive objective.
2. Remove the phrase "theoretical analyses" from the contributions list and either (a) replace Section 3.8 with a brief "Discussion" section labeled as such, or (b) expand it with a genuine formal argument (e.g., connecting the contrastive loss to an InfoNCE bound on mutual information across behavior types).
3. Clarify the meta-network parameterization: specify whether \(\mathbf{W}_{i,k'}^{(u,l)}\) is per-user or shared across users, and justify the computational design.
4. Describe the visualization methodology in Section 4.7 (dimensionality reduction technique, color mapping procedure).
