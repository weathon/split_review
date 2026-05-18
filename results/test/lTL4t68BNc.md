Now I have thoroughly analyzed the paper against all reviewer claims. Let me construct the final review.

---

## Summary

This paper proposes RGA-IB, a novel graph attention mechanism for robust semi-supervised node classification under adversarial attacks. The work makes two contributions: (1) it identifies an empirical correlation between Information Bottleneck (IB) loss and the robustness of attention-based GNNs, and (2) it designs an attention mechanism whose weight matrices are updated via a formula derived from gradient descent on the IB loss (Theorem 3.1). RGA-IB replaces local neighborhood aggregation with dense all-pair attention to overcome the two-hop locality limitation of prior IB-based GNNs (GIB, UGRL, RG-GIB). Experiments on Cora, Citeseer, Pubmed, and Polblogs under Metattack, Nettack, and Topology Attack show that RGA-IB consistently outperforms 12 baselines including GIB, GAR, Difformer, and GCORNs.

## Strengths

- **Consistent state-of-the-art robustness across diverse attack types and datasets.** Tables 1–3 show RGA-IB outperforming all 12 comparison methods on Cora, Citeseer, Pubmed, and Polblogs under Metattack, Nettack, and Topology Attack. On Pubmed, the average improvement over the second-best method is ~1.5% across all three attack types. Results are reported with 10 runs and standard deviations.

- **Novel conceptual connection between IB principle and robust graph attention.** While prior robust attention methods (GAT, UAG, GAR, RGCN) are empirically designed, the paper provides a principled motivation: attention mechanisms that better adhere to the IB principle (lower IB loss) tend to be more robust. This connection is new in the graph robustness literature and provides a design rationale rather than post-hoc justification.

- **Overcomes the local-dependency limitation of prior IB-based GNNs.** The paper correctly identifies that GIB, UGRL, and RG-GIB are constrained to two-hop neighborhoods and shows that RGA-IB's dense all-pair attention mitigates propagation from adversarial neighbors (Figure 1: >90% of nodes in the RGA-IB attention graph have <20 adversarial neighbors on Cora, vs. 60% in the attacked graph).

- **Comprehensive ablation and analysis.** Section 4.3 studies IB loss across layers (Table 4), showing that RGA-IB progressively reduces IB loss to lower levels than Difformer and GAR, and that a 2-layer RGA-IB network achieves the same IB loss reduction as a 4-layer one. Table 5 directly links IB loss to robust accuracy across multiple attention methods.

## Weaknesses

### Major

- **The claimed correlation between IB loss and robustness ("strong indicator") is not as thoroughly established as the paper asserts.** The evidence (Table 5) covers only 2 datasets (Cora, Citeseer) under 1 attack type (Metattack) at 2 perturbation rates. No correlation coefficient (Spearman/Pearson) is reported, no statistical test is performed, and the analysis does not extend to Nettack, Topology Attack, or larger datasets (Pubmed, Polblogs). The paper's central motivational claim — that IB loss is a "strong indicator of robustness" — goes beyond what the evidence supports. This does not invalidate RGA-IB's empirical performance, but the framing overstates the strength of the correlation.

- **The method's theoretical grounding and practical implementation have a gap that is not discussed.** Theorem 3.1 derives an IB gradient descent update for the attention matrix B, and the paper states that RGA-IB "explicitly minimizes the IB loss." However, Algorithm 1 shows that network weights are trained by cross-entropy alone — the IB loss never appears in the training objective, and no gradient from IB loss backpropagates to the network parameters. The attention matrices are computed via a feed-forward formula (Equation 1) using centroids from the previous epoch, which is a heuristic approximation of true gradient descent on IB loss. The paper would benefit from acknowledging this approximation explicitly and discussing whether the design still constitutes "explicit" minimization. This is not a fatal flaw — the attention update is still IB-inspired — but the current framing is imprecise and could mislead readers about the optimization.

### Minor

- **No analysis of computational complexity is provided.** RGA-IB uses dense N×N attention matrices, which is O(N²) in both memory and compute. For Pubmed (N≈19,717), this is a significant practical concern that is not discussed. Baselines like GCN, GAT, and GAR operate on sparse neighborhoods. The paper should at minimum acknowledge this trade-off and provide complexity analysis.

- **Statistical significance of improvements is not reported.** Several results show the RGA-IB mean within 1-2 standard deviations of the best baseline (e.g., Cora 25% Metattack: 84.43±1.41 vs. best baseline 83.21±1.08). Without paired statistical tests or effect-size measures, it is unclear whether some of the improvements are statistically reliable.

- **The alternating centroid update is a practical approximation that could affect the theoretical guarantees.** In Algorithm 1, centroids are computed from node representations after the forward pass (line 182) and used to compute attention matrices at the next epoch. This means the gradient step in Equation (1) uses stale centroids and ignores the dependency of centroids on B. The paper does not discuss whether this approximation affects the claim that the attention mechanism minimizes IB loss.

### Trivial

- The paper's self-characterization as "explicitly minimizing IB loss" through the attention mechanism alone (without IB in the training loss) is technically defensible but would benefit from more precise language such as "attention weights are updated via a formula derived from gradient descent on IB loss."

- Table captions and references to supplementary sections (Section C) are present in the text but the corresponding content was stripped by the parser; this is a formatting issue only.

## Nice-to-Haves

- Augment the IB-robustness correlation analysis with more datasets (Pubmed, Polblogs), more attack types (Nettack, Topology Attack), and compute Spearman/Pearson correlations.
- Include a controlled ablation where the attention matrix is learned via standard backpropagation (trainable attention as in GAT/Transformer) vs. the IB-derived update, to isolate the contribution of the IB-inspired mechanism.
- Report paired statistical significance tests (e.g., t-test or Wilcoxon) for the main results.
- Provide complexity analysis (time and memory) for the dense attention.

## Removed Points

- **"Gradient derivation is not credible / outer product form unlikely"** — This criticism is factually incorrect. The chain rule through Z=BF gives exactly ∂IB/∂B = (∇_Z I(Z,X) - ∇_Z I(Z,Y))·F^T. The outer product form is the expected structure; the complexity resides in Q (∇_Z I terms), which are deferred to the appendix. This is standard mathematics, not a flaw.

- **"Missing appendix / Lemma A.1 and A.2 not available"** — Per policy, the parser strips supplementary sections. The full derivation exists in the original submission and cannot be judged from the extracted text.

- **"GIB not discussed in context of local dependency"** — The paper explicitly discusses GIB's two-hop limitation (lines 31, 33) and lists GIB in all main experiment tables (Tables 1-3, line 204).

- **"Table 4 does not compare with Difformer"** — Table 4 explicitly compares IB loss across layers for RGA-IB, Difformer, and GAR. This claim is false.

- **"The IB loss is never used"** — The attention weight matrices in Algorithm 1 (line 180) ARE computed via Equation (1), which is derived from IB loss gradient descent. The method does use the IB-driven update for attention weights even though network parameters are trained by cross-entropy. This is a design choice, not an absence.

- **Generic/filler strengths from Strength Finder** — "Code is provided for reproducibility" is a generic strength shared by many papers and does not specifically support this paper's contribution claims. Dropped.

## Novel Insights

The harsh critic raises a point worth noting: the gap between the theoretical framing (explicit IB minimization via gradient descent) and the actual training procedure (cross-entropy on network weights + feed-forward IB-inspired attention update) is real, though the severity is overestimated. This is a recurring tension in the IB-for-GNNs literature, where the loss is often used as a design principle rather than a training objective. The paper does not acknowledge this distinction, which weakens its theoretical positioning. The paper's real contribution — a well-performing robust attention mechanism with a principled design rationale — stands independently of whether the optimization strictly minimizes IB loss.

## Suggestions

1. Clarify the relationship between the IB-derived attention update and the training objective. Distinguish between "attention weights designed via IB gradient descent" and "training loss includes IB." If the method is best understood as an IB-inspired architectural design (rather than IB optimization), state this explicitly.

2. Expand the IB-robustness correlation analysis (Table 5) to cover more datasets and attack types, and report a correlation coefficient, or alternatively soften the claim from "strong indicator" to "consistent empirical observation that motivates the method."

3. Add a computational complexity analysis, especially noting the O(N²) memory cost of dense attention and discussing when this trade-off is acceptable in practice.

4. Report statistical significance (paired tests) for the main accuracy comparisons, particularly where improvements are modest relative to standard deviations.

5. Acknowledge the centroid staleness issue in Algorithm 1 and discuss whether it affects the theoretical connection to IB minimization.

## Score and Decision

**Originality:** Good. The IB-inspired gradient-descent attention update and the empirical link between IB loss and attention-based robustness are novel.

**Importance:** Good. Adversarial robustness for GNNs is an active and important area.

**Claims:** The empirical claims (SOTA performance) are well-supported. The motivational claim (IB loss as "strong indicator") is somewhat overclaimed relative to the evidence.

**Soundness:** The experiments are comprehensive (3 attack types, 4 datasets, 12 baselines, 10 runs). The theoretical derivation via chain rule is mathematically correct; the gap between the theoretical framing and practical implementation should be acknowledged.

**Clarity:** The paper is generally well-structured. Key design choices could be better motivated.

**Value:** The method achieves consistent improvements across diverse settings and the IB-inspired design provides a principled alternative to purely empirical attention mechanisms.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>