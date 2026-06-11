Now I have all the calibration information needed. Let me produce the final consolidated review.

## Summary

This paper identifies and formally defines Dual-level Noisy Correspondence (DNC), a previously unstudied problem in Multi-modal Entity Alignment where noise exists at both the intra-entity (entity-attribute) and inter-graph (entity-entity, attribute-attribute) levels. The authors propose RULE, a framework that estimates correspondence reliability via a two-fold principle combining uncertainty (Dempster-Shafer theory) and consensus, then uses these estimates to guide robust attribute fusion and inter-graph discrepancy elimination. A test-time TTR module using Qwen2.5-VL-72B with chain-of-thought reasoning further refines similarity scores. Experiments on five benchmarks demonstrate substantial and consistent improvements over seven baselines.

## Strengths

- **Formal identification and formulation of DNC**: The paper provides a clean mathematical formalization (binary indicators $h_i^m$, $y_{ij}$, $y_{ij}^m$) of a practical problem that prior MMEA work assumed away. The empirical motivation — over 50% of alignments in ICEWS benchmarks contain NC — grounds the problem in real data.

- **Principled two-fold reliability estimation**: The combination of uncertainty (via Dempster-Shafer theory / Dirichlet distributions, Eq. 2-3) and consensus (Eq. 5) is theoretically motivated, including Theorem 1 proving that low uncertainty alone is insufficient for identifying correct correspondences. This insight justifies the three-way pair division ($\mathcal{S}_U$, $\mathcal{S}_I$, $\mathcal{S}_C$) and the tailored loss strategies.

- **Strong empirical results with large margins**: On the Non-name setting at 50% DNC, RULE achieves Avg H@1 of 64.3 vs. the next best (MEAformer at 54.0) — a 10.3-point margin. Under inherent DNC, RULE scores 73.8 Avg H@1 vs. next best (PMF, 68.6). Results are consistent across five datasets, two evaluation protocols, and three noise levels. Figure 3(a) further shows slower performance degradation under varying DNC ratios.

- **Comprehensive ablation study**: Table 3 systematically ablates training-phase components (DRL, DRF, uncertainty-only, consensus-only) and test-phase components (DRF, TTR, MLLM Enhance), confirming that each component contributes positively and the full design outperforms every ablated variant. The ablation demonstrates that even the training-only version ("w/o TTR" at 56.5) substantially beats the best baseline (MEAformer at 42.4) on ICEWS-WIKI Non-name at 50% DNC.

## Weaknesses

### Major

- **The test-time TTR module creates an asymmetric comparison in the main results.** Tables 1 and 2 present RULE (with Qwen2.5-VL-72B-Instruct, a 72B-parameter MLLM) against baselines that have no access to any such model. The paper states in Section 3.2 that "for fair comparisons, we adopt the same backbone (i.e., CLIP) for all baselines and our method," but this refers only to the feature extraction backbone, not to the test-time reasoning. The ablation (Table 3) shows the training-only version still substantially beats baselines (e.g., "w/o TTR" achieves 56.5 vs. best baseline 42.4 on Non-name ICEWS-WIKI at 50% DNC), so the core contribution holds. However, the main comparison tables conflate two very different contributions — the training-time robust learning framework and the inference-time MLLM augmentation — without allowing the reader to assess each independently. This is a presentation issue that is fixable but non-trivial: the paper should present training-time-only results alongside the full results, or give baselines access to comparable MLLM reasoning.

### Minor

- **Greedy consensus estimation has a potential bootstrapping issue.** The consensus estimation during inference (Eq. 6-7) uses a greedy marginal-contribution strategy over similarity scores $s_i^m$ — the same scores the model is learning. If the model's initial similarity estimates are poor (especially under high noise), the greedy selection could reinforce errors rather than correcting them. The paper does not analyze conditions under which the greedy approximation converges to the true $y_i$ or discuss failure modes. The initial subset size $|\pi_0| = \lfloor M/2 + 1\rfloor$ (Eq. 7) is also presented as a heuristic without justification.

- **Computational cost of the TTR module is not analyzed.** Running Qwen2.5-VL-72B per test query with CoT reasoning is extremely expensive. For large-scale KGs with hundreds of thousands of entities, this would be prohibitive. The paper provides no analysis of inference time, memory cost, or practical feasibility.

- **Missing comparison against a directly relevant baseline.** Chen et al. (2024) "Tackling Uncertain Correspondences for Multi-modal Entity Alignment" (NeurIPS 2024) appears in the reference list but is not included as a baseline. This paper addresses the same task (MMEA under uncertain/noisy correspondences) and its exclusion weakens the comparison.

- **No variance or confidence intervals reported.** The paper reports single numbers without variance across multiple seeds (confirmed by grep for "variance|standard deviation|seed" returning no matches). Given that the noise injection process is random, this makes it difficult to assess result stability.

- **Hyperparameter sensitivity for $\beta$ is not shown in the main paper.** The threshold $\beta$ (Eq. 8) is fixed at 0.3 across all experiments, yet it controls the entire partition into $\mathcal{S}_U$, $\mathcal{S}_I$, and $\mathcal{S}_C$. The paper cites Appendix G.10 for sensitivity analysis, which is not accessible in the review.

### Trivial

- The evidence function in Eq. 2 ($\exp(\tanh(s_{ij}/\tau))$) is presented without justification for why this specific form is chosen over alternatives such as softplus.

- The balanced hyperparameter $\gamma$ in Eq. 1 is "fixed as 0.5 for simplicity" with no ablation showing sensitivity to this choice in the main paper.

## Nice-to-Haves

- Reporting wall-clock inference time per query for the TTR module would help practitioners assess feasibility.
- A controlled experiment varying the quality of initial similarity estimates to measure the accuracy of greedy consensus estimation would build confidence in the bootstrapping strategy.

## Removed Points

These points were flagged by the Harsh Critic but are removed or downgraded after cross-checking against the paper:

1. **"The paper's framing implies RULE as a unified method"** — This is not a weakness; RULE is a unified method that includes TTR. The paper discloses Qwen2.5-VL-72B use. The concern about asymmetric comparison is kept above as Major, but the framing criticism is removed as overstated.

2. **"The DRL loss dependency on pair division creates circular dependency"** — The reviewer noted that $w_i$ from Eq. 1 is not used in the discrepancy elimination loss directly. This is a design observation rather than a concrete weakness. The DRF uses reliability weights for attribute fusion, and DRL uses pair division for discrepancy elimination — this is consistent, not a missed opportunity.

3. **"Dataset age concern (DBP15K from 2021)"** — This is standard practice in entity alignment; all baselines use the same datasets. Not a meaningful weakness to single out.

4. **"Section-by-section notes about missing appendix details"** — Removed per instructions: the parser strips appendices from all papers.

5. **"The TTR module is essentially a black-box augmentation"** — While TTR is not as fully formalized as other components, the paper provides the CoT formulation (Eq. 16) and references Appendix F.5 and I for details. This is not a core weakness beyond the asymmetry concern already captured.

6. **Strength Finder claims about "one of the first methods to enhance test-time robustness for the MMEA task"** — Kept as it is the paper's own claim; not a strength per se but a factual statement about novelty.

## Novel Insights

None beyond the paper's own contributions. The two-fold reliability principle (uncertainty + consensus) and Theorem 1's demonstration that low uncertainty does not imply correct correspondence are the paper's genuine conceptual contributions. The insight that DNC manifests differently at intra-entity and inter-graph levels and requires different mitigation strategies is well-motivated. No additional novel synthesis emerged from the reviews.

## Suggestions

1. Present the main results tables with two versions: "RULE (training only)" and "RULE (full)", so the reader can assess each contribution independently. The ablation suggests the training-only version still beats baselines substantially, which would be a cleaner result.

2. Add Chen et al. (2024) as a baseline or justify its exclusion in the experimental setup.

3. Report inference costs (wall-clock time per query) for the TTR module, given the use of a 72B MLLM.

4. Report results over multiple random seeds with variance to address the statistical reliability concern.

5. Include a sensitivity analysis for $\beta$ (threshold hyperparameter) and $\gamma$ (balanced weight in Eq. 1) in the main paper, not just the appendix.

## Score and Decision

**Round 1 — Bracketing**: The paper was compared against anchors from three bands. The <3.5 band contained papers with fundamental flaws (avg 3.0-3.4). The 3.5-7.5 band contained entity alignment and noisy correspondence papers (avg 4.5-6.67). The >7.5 band contained exceptionally clean papers (avg 8.0). RULE clearly sits in the middle band, with a plausible range of 5.5-7.0.

**Anchors examined in full**:
- **GEEA** (z3dfuRcGAK, avg 6.67): Entity alignment with generative models. Accepted. RULE has stronger empirical evaluation (5 datasets vs. DBP15K only) and a clearer problem novelty. Comparable.
- **NeuSymEA** (NNUiUwQWx6, avg 5.75): Neuro-symbolic entity alignment. Rejected. RULE is clearly stronger (more novel problem, larger empirical margins, cleaner ablation).
- **MoMoK** (ue1Tt3h1VC, avg 6.60): MMKG representation learning. Accepted. Similar evaluation breadth; RULE has greater novelty in problem formulation. Comparable.
- **OTGM** (6w2HEMxzq7, avg 5.50): Graph matching with noisy correspondence via OT. Rejected. RULE has stronger theoretical grounding and more comprehensive experiments.
- **BioBridge** (jJCeMiwHdH, avg 7.00): KG bridging for biomedical FMs. Accepted. Slightly stronger than RULE in cleanliness of presentation and absence of methodological concerns.
- **Norton** (9Cu8MRmhq2, avg 8.0): Noisy correspondence in video-language. Accepted. Notably stronger — cleaner writing, no asymmetry concerns, tighter contribution.

**Round 2 — Narrowing**: RULE is clearly stronger than the 5.5-5.75 reject-level papers and comparable to the 6.6-6.67 accept-level papers, but has a meaningful presentation concern (TTR asymmetry) that the top anchors do not share. It is slightly weaker than the 7.0 BioBridge anchor, which has a cleaner methodological narrative.

**Final score**: RULE is a solid paper with a genuine contribution (new problem formulation + robust training framework) and strong empirical validation, held back from a higher score by the TTR presentation issue and a few methodological gaps. I place it at **6.0**, just below the GEEA/MoMoK cluster (6.6-6.67) due to the asymmetric comparison concern, but well above the reject-level papers (5.5-5.75).

**Decision**: Accept. The core contribution — the DNC problem formulation and the training-time robust framework — is novel, well-supported, and independently strong. The TTR presentation issue is addressable in revision.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>