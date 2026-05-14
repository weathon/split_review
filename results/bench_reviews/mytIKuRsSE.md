Now I have all the information I need. Let me write the final consolidated review.

## Summary

This paper identifies and formalizes a new problem in multi-modal entity alignment (MMEA) called Dual-level Noisy Correspondence (DNC), where both intra-entity (entity-attribute) and inter-graph (entity-entity and attribute-attribute) correspondences are noisy. To address DNC, the authors propose RULE, which estimates correspondence reliability via uncertainty (evidential learning) and consensus principles, then uses these estimates to guide robust attribute fusion (DRF) and robust inter-graph discrepancy elimination (DRL) during training. At test time, RULE further employs an MLLM-based correspondence reasoning module (TTR) to uncover latent attribute connections. Extensive experiments on five benchmarks under three noise levels show strong improvements over seven baselines.

## Strengths

1. **Well-motivated problem with real-world grounding.** The paper provides empirical evidence (Appendix B.1) that over 50% of entity pairs in widely-used ICEWS benchmarks suffer from DNC, with concrete examples (Fig. 1a) showing how annotation errors propagate across entity-attribute and entity-entity levels. This convincingly establishes that existing methods' assumption of clean correspondences is unrealistic.

2. **Strong empirical results with clean ablation decomposition.** RULE achieves substantial gains across all five datasets and noise levels. Critically, even without the TTR module, RULE (w/o TTR) achieves 56.5% H@1 on ICEWS-WIKI (Non-name, 50% DNC) versus the best baseline HHEA at 43.9% — a 12.6-point gap that comes entirely from the training-time components (DRL + DRF). The ablation in Table 3 cleanly isolates each component's contribution, showing that DRL (removing it drops to 31.6%) and DRF are both essential.

3. **Principled two-fold reliability estimation.** The combination of evidential uncertainty (Dempster-Shafer theory) and consensus modeling addresses a genuine limitation of using uncertainty alone — Theorem 1 correctly notes that low uncertainty does not guarantee correct annotation. Fig. 3(b) and 4 visually confirm that the combined reliability metric separates clean, low-consensus, and high-uncertainty pairs, supporting the tailored training strategy for each subset.

4. **Model-agnostic design confirmed across backbones.** Appendix G.11 shows consistent improvements over baselines with SigLIP and BLIP backbones (e.g., 45.4% vs. 32.2% H@1 on SigLIP Non-name, 50% DNC), confirming that RULE's robustness is not tied to a specific feature extractor.

5. **Exhaustive evaluation scope.** The paper evaluates under three noise levels (inherent, 20%, 50% DNC), individual noise types (E-E, E-A, A-A NC in Appendix G.1), varying noise ratios (0–70%), and multiple MLLM backbones (Qwen2.5-VL 3B/7B/72B, LLaVA-1.6 34B), providing strong evidence of robustness.

## Weaknesses

### Fatal
None.

### Major

1. **The DNC novelty claim is partially overclaimed without a critical control experiment.** The paper frames DNC as a "new problem" distinct from studying entity-entity noise (REA) and entity-attribute noise (KG refinement) separately. However, no experiment tests whether joint dual-level handling outperforms a pipeline that applies existing entity-entity denoising + existing entity-attribute denoising sequentially. While the ablation in Table 3 shows that both DRL and DRF contribute, this does not demonstrate that the "dual-level" framing is necessary beyond combining known techniques. The paper would be stronger if it directly compared against pipeline baselines or framed the contribution more modestly.

2. **The TTR module creates a comparison asymmetry that the paper does not adequately acknowledge in the main text.** While Tables 1–2 present RULE's full results (with TTR) as the primary comparison, the paper correctly provides ablation showing w/o TTR still beats baselines significantly (56.5 vs. 43.9). However, the presentation in the main paper does not clearly flag to the reader that roughly 1.7 of the ~14-point gain on the Non-name 50% DNC setting comes from MLLM re-ranking that baselines cannot match. This is not a fatal flaw — the ablation exists — but the paper should explicitly decompose the "headline gap" into training-time and test-time contributions in the main text rather than deferring it to Appendix G.8.

### Minor

1. **No confidence intervals or significance tests.** Results are reported as point estimates with three significant digits (e.g., 58.2, 69.7, 63.6) without variance measures across runs. Given the modest size of some test sets (e.g., ~5,000 pairs for ICEWS-WIKI), it is unclear whether small differences between ablations (e.g., 56.5 vs. 56.6 in Table 3) are meaningful.

2. **The evidence formulation choice (tanh) is not justified.** The evidence in Eq. 2 uses exp(tanh(s_ij/τ)), which bounds evidence in [e⁻¹, e¹] ≈ [0.37, 2.72]. This is an unconventional choice compared to the softplus or exponential commonly used in evidential deep learning. The paper provides no ablation or justification for this design decision and no comparison against alternative formulations.

3. **No convergence or stability analysis for the bootstrapped reliability estimation.** The greedy marginal contribution strategy (Eq. 6–7) depends on representations trained with previous epoch's reliability estimates, creating an iterative dependency. The paper provides no analysis (empirical or theoretical) of whether this bootstrap converges to stable subsets across training runs or different initializations.

4. **The "over 50% DNC" statistic relies on a single-sample annotation without inter-annotator agreement.** The statistic in Appendix B.1 is based on manual annotation of 1,000 random pairs by an unspecified number of annotators, and no inter-annotator agreement score is reported. This weakens the claim about DNC prevalence.

### Trivial
- The parameter analysis in Appendix G.2 varies one hyperparameter at a time, ignoring potential interactions between λ, τ, and β. A small grid or sensitivity surface would be more informative.

## Nice-to-Haves
- Comparing RULE (w/o TTR) against baselines augmented with the same MLLM re-ranking would cleanly address the asymmetry concern.
- A pipeline baseline (first denoise E-E pairs with REA's method, then denoise E-A pairs separately, then run standard MMEA) would substantiate the "dual-level" framing.
- Reporting variance across 3–5 random seeds would improve interpretability of the numerical results.

## Removed Points
- **"The TTR module re-uses the test set labels during inference."** This is factually incorrect. The TTR module selects top-10 candidates using the model's own prior similarity scores **s**_i_^m (model predictions), not ground-truth labels. The paper is clear that `T_i^m` denotes "the set of correspondences with the highest similarity in prior results **s**_i_^m" (Eq. 16, line 421). This is standard re-ranking practice and does not leak test labels.
- **"The comparison is fundamentally unfair because baselines don't have MLLM."** Overstated. The paper provides ablation (Table 3) showing w/o TTR achieves 56.5 vs. best baseline 43.9 on the hardest setting. The training-time components alone produce the majority of the gains. This is acknowledged in Appendix G.8. The criticism is partially valid as a presentation concern (see Major #2 above) but not as a fatal flaw invalidating all results.
- **"The DRL loss is identical to Sensoy et al. (2018)."** The paper clearly states the closed-form MSE loss follows Sensoy et al. (2018). The novelty is in the pair division and refined correspondence **ŷ**_i_ (Eq. 12), which differs from standard evidential learning. The paper does not claim the MSE formulation itself is novel.
- **"The problem framing overclaims novelty."** Weakened to a Major weakness (see above) rather than treated as fatal, since the paper does provide ablation evidence that both levels matter but lacks the pipeline control experiment.
- **Missing related works.** Removed per instructions as I cannot independently verify existence of uncited works.
- **Formatting and presentation nitpicks.** Removed per instructions (parser artifacts).
- Various minor points about missing appendix content — removed per instructions (parser strips appendix content from all papers).

## Novel Insights

None beyond the paper's own contributions. The reviews surface a genuine tension: the paper makes a strong empirical case for the RULE method through careful ablation, but the "new problem" framing of DNC and the asymmetric TTR evaluation each introduce ambiguities that the paper could resolve with one additional control experiment each. The most interesting observation from the review process is that the core training-time contribution (DRL + DRF) is quite clearly responsible for the bulk of the performance gains (56.5 vs. 43.9), making the TTR asymmetry a secondary concern — a fact the paper could signal more prominently in the main text.

## Suggestions

1. **Add a training-time-only leaderboard to the main paper.** Present a version of Tables 1–2 where the RULE column reports w/o TTR results, with the full RULE results in parentheses or a separate column. This would immediately clarify that the large gains are not driven by the MLLM.

2. **Add a "separate vs. joint" experiment.** Compare RULE against a pipeline that applies existing EE denoising (e.g., REA) followed by EA denoising independently, to substantiate the claim that joint dual-level handling is necessary.

3. **Report standard deviations** across multiple runs for at least the key settings (ICEWS-WIKI 50% DNC, DBP15K ZH-EN inherent DNC).

## Score and Decision

**Calibration anchors (retrieved from human review corpus):**

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| ALMEA (MMEA + active learning) | 5.0 | Similar domain, less thorough experiments (2 datasets vs. 5), less novel problem. RULE is stronger. |
| DiffNCL (noisy correspondence learning) | 5.0 | Similar noise-robustness theme but weaker empirical support and missing implementation details. RULE is more complete. |
| CorreGen (noisy correspondence for MVC) | 7.0 | Accepted Oral. Cleaner theoretical framing (EM + OT), comparable experimental rigor. RULE has broader benchmarks but a less clean theoretical contribution. |
| ContrastEA (entity alignment) | 3.5 | Limited technical novelty, narrow evaluation. RULE is substantially stronger. |
| Noise-Aware Few-Shot Learning | 3.0 | Weak motivation and execution. Not comparable. |
| RAM-TTT (test-time reasoning) | 4.67 | Different domain, less convincing results. |
| Graph Alignment for GNN | 4.0 | Different problem, weaker empirical support. |

Positioning relative to anchors: RULE is clearly stronger than the rejected MMEA/noisy-correspondence papers (ALMEA 5.0, DiffNCL 5.0) and substantially stronger than low-scoring entity alignment papers (ContrastEA 3.5). It is comparable to but slightly below the accepted CorreGen (7.0) due to the cleaner theoretical framing of that paper and the evaluation asymmetry concern in RULE. The paper has genuine contributions (problem identification, two-fold reliability, strong empirical results) but is held back by the overstated novelty claim and the insufficiently decomposed evaluation.

**MY FINAL SCORE: <pineapple>6.0</pineapple>**
**MY FINAL DECISION: <orange>Accept</orange>**