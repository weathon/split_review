Now I have thorough calibration. Let me write the final consolidated review.

---

## Summary

This paper proposes RADAR, a neural framework for solving asymmetric vehicle routing problems (VRPs). It addresses two types of asymmetry: (1) *static asymmetry* in the input distance matrix, handled by initializing node embeddings via truncated SVD on the cost matrix; and (2) *dynamic asymmetry* in learned representations, handled by replacing row-wise softmax with Sinkhorn normalization in the encoder attention to enforce balanced bidirectional flows. Experiments across 17 synthetic and 3 real-world VRP variants show consistent improvements over strong learning-based baselines (MatNet, ICAM, RRNCO, etc.) and competitive performance against traditional OR solvers (LKH, HGS).

## Strengths

1. **Cleanly motivated technical contributions.** The decomposition into static vs. dynamic asymmetry is conceptually clear, and each component addresses a specific limitation of prior work. The SVD initialization injects global directional structure into node embeddings, and the Sinkhorn normalization replaces row-wise softmax to account for both interacting nodes' neighborhood contexts. Neither gimmick—both are well-grounded in the problem structure.

2. **Strong ablation isolating each component.** Table 6 provides a textbook 2×2 ablation (SVD ✓/✗ × Sinkhorn ✓/✗) on ATSP. The results are striking: on ATSP1000, no component yields a 38.64% gap, SVD alone reduces it to 7.24%, Sinkhorn alone to 22.89%, and the full RADAR to 4.13%. This convincingly attributes the gains to the proposed designs, not to architecture changes.

3. **Extensive and rigorous experimental evaluation.** The paper spans synthetic single-task (ATSP, ACVRP at 100–1000 nodes), a 16-variant multitask setting, and three real-world benchmarks (ATSP, ACVRP, ACVRPTW). Comparisons include multiple neural baselines (MatNet, ICAM, ELG, ReLD, UniCO, RRNCO) and strong OR baselines (LKH-100/1000/10000, HGS). RADAR achieves the best among learning-based methods across nearly all settings.

4. **Insightful analysis beyond bare results.** Section 5.4 (coordinates vs. distance matrices) shows that RADAR without coordinates outperforms RRNCO *with* coordinate augmentation on real-world ATSP, demonstrating that the SVD embeddings capture more structural information than raw coordinates. Section 5.5 systematically varies asymmetry levels, showing RADAR degrades more gracefully than all baselines.

5. **Real-world validation.** Table 3 shows RADAR achieving 0.74–1.18% gaps on real-world ATSP (vs. 1.80–2.30% for RRNCO and 3.98–5.88% for MatNet), and consistent improvements on ACVRP and ACVRPTW across in-distribution and out-of-distribution settings. This grounds the method in practical applicability.

## Weaknesses

### Fatal

None.

### Major

None. The paper's core claims are supported by the empirical evidence. The issues below are addressable and do not undermine the main findings.

### Minor

1. **Theoretical framing of Definition 1 is tautological.** Definition 1 defines "asymmetry-aware embedding" as one for which there *exist* linear transforms making a bilinear form approximate *D*. The paper then constructs the SVD-based embedding and exhibits specific transforms (Eq. 4–5) that satisfy the condition by construction. This is logically valid but adds no explanatory power—it states that good embeddings can reconstruct the distance matrix, and then the SVD embeddings can (by design). The real justification for the SVD initialization is empirical (Table 6), not theoretical. The paper would benefit from reframing this as a motivation rather than a formal definition. *(Section 4.1, Definition 1, Eq. 1–5)*

2. **Z-score normalization of the distance matrix before SVD is neither justified nor ablated.** Algorithm 1 standardizes *D* (subtract mean, divide by std) before truncated SVD. For non-negative distance matrices with zero diagonals, this produces negative values. The paper provides no rationale for this choice, no ablation comparing alternatives (e.g., min-max, no normalization), and no analysis of its effect on reconstruction quality. While the baseline methods also use z-score normalization (making comparisons fair), the reader cannot tell whether this choice is critical or benign. *(Algorithm 1, Section 4.1)*

3. **Masking interaction with Sinkhorn normalization is underspecified.** The paper states that visited nodes are masked in the decoder, but it is not specified how masking interacts with the Sinkhorn normalization in the encoder (e.g., whether self-loop masking or infeasibility masking is applied before or after Sinkhorn iterations). The encoder does not typically use masking (all nodes attend to each other), but for completeness the authors should clarify whether any masking is applied and how Sinkhorn handles it. *(Algorithm 2, Section 4.2)*

4. **HGS infeasibility rate on ACVRP should be reported in the main text.** Table 1 footnotes that HGS yields infeasible solutions and excludes it from gap computation, referencing Appendix G. Since HGS achieves lower costs than RADAR on several ACVRP sizes (e.g., HGS-Short 2.0806 vs. RADAR 2.1483 on ACVRP200), the reader needs to know the infeasibility rate to evaluate the fairness of the comparison. A single sentence reporting the rate or summarizing the appendix finding would suffice. *(Table 1 footnote)*

### Trivial

1. **Ablation baseline (no SVD, no Sinkhorn) is MatNet-Single (Random).** The paper could explicitly note that the "RADAR without SVD or Sinkhorn" row in Table 6 matches the MatNet-Single (Random) configuration from Table 1. Currently this is left implicit.

2. **Noise model for asymmetry-level experiments.** The paper uses θ ~ N(1, σ²) with σ ∈ {0.1, 0.2, 0.3}. For σ = 0.3, negative values are theoretically possible but negligible in practice (<0.04% probability). The paper could briefly note this is not a practical concern.

## Nice-to-Haves

- An ablation comparing normalization strategies (none, min-max, z-score) for the SVD step would strengthen the methodology.
- Visualizations of Sinkhorn vs. softmax attention matrices on a sample ATSP instance would help illustrate the "balanced bidirectional flows" claim.
- A brief experiment integrating RADAR embeddings into a local-search or improvement-based solver (as mentioned in future work) would demonstrate broader applicability.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Synthetic benchmark generation underspecified.** The harsh critic argues that the ACVRP asymmetry generation is not explained. However, the paper states "Full details are provided in Appendix A" — this section was stripped by the parser and exists in the original submission. *Reason: Per guidelines, criticisms about missing appendix content are removed because the parser strips these sections from all papers.*
- **"Already addressed" / scope-related reductions**: The critic's demand that the paper *prove* dynamic asymmetry emerges in learned representations via attention visualizations goes beyond what a systems paper typically provides. The Sinkhorn ablation provides sufficient empirical evidence. Similarly, requests for a full theoretical proof of the initialization's benefit over random initialization are scope-creep for an empirical paper.

## Novel Insights

The most interesting observation emerging from the reviews is that RADAR's main weakness (the tautological theoretical framing) and its main strength (the convincing ablation) are two sides of the same coin. Definition 1 does not *explain* why SVD helps, but the ablation (Table 6) provides overwhelming evidence that it *does* help. This suggests the paper's contribution is best understood as a well-executed empirical system that the community can build on, rather than a theoretically grounded framework. The coordinate analysis (Section 5.4) makes a second valuable empirical point: in asymmetric routing, distance-based embeddings can be more informative than raw coordinates—a counterintuitive finding that reframes the value of coordinate data in NCO.

## Suggestions

1. Remove or reframe Definition 1 as a motivation/high-level goal, not a formal definition. Let the ablation results (Table 6) carry the weight of justification.
2. Add a brief ablation of the z-score normalization (compare no normalization, min-max, and current approach on ATSP100).
3. Clarify how masking interacts with Sinkhorn normalization in the encoder (or confirm that no masking is applied in the encoder).
4. Report the HGS infeasibility rate for ACVRP in a single sentence in the main text.

## Score and Decision

**Calibration anchors** (all from the deepreview_13k_calibration set):

| Path | Avg Score | Comparison to this paper |
|------|-----------|-------------------------|
| jsWCmrsHHs.md (DRL for JSSP) | 7.50 | Stronger theoretical contribution (linear complexity proof); RADAR has broader experimental evaluation |
| yEwakMNIex.md (Unified Neural Solvers) | 6.25 | Similar topic (asymmetric TSP via matrix encoding); RADAR has cleaner ablation and more extensive benchmarks |
| TbTJJNjumY.md (Large-scale VRP) | 6.25 | Comparable acceptance level; RADAR's evaluation is more rigorous (multiple VRP variants, real-world data) |
| DKfcxPxunu.md (Multi-task VRP) | 5.75 | Rejected due to weak methodology; RADAR is substantially stronger empirically |
| CFLEIeX7iK.md (Neural Solver Selection) | 5.75 | Decent but rejected; RADAR has stronger technical novelty |
| iXBYYbYTvX.md (Embedding-enhanced LKH) | 3.50 | Weak experiments and presentation; RADAR is far superior |
| SrnTGdJKYG.md (Neural Deconstruction) | 3.00 | Weak methodology; RADAR is clearly stronger on all evaluation axes |

RADAR delivers strong empirical contributions (extensive benchmarks, clean ablation, SOTA results) with two well-motivated technical components. The weaknesses (tautological framing, unablated normalization) are minor and addressable. Compared to the 6.25-level accepted papers, RADAR has broader and more rigorous experiments. It is clearly above the 5.75-level rejected papers.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>