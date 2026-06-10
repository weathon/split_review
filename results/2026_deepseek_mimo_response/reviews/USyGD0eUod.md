Now I have enough calibration data. Let me finalize my assessment.

**Comparison with anchors:**
- Clearly better than "SAEs Find Highly Interpretable Features" (4.8) — more focused experimental design, clearer contribution
- Better than "Residual Stream Analysis with MLSAEs" (6.5, Accept) — more impactful finding about metrics failing
- Comparable to but slightly below "Towards Principled Evaluations of SAEs" (7.0) and "SAEs Do Not Find Canonical Units" (7.0) — those papers introduce novel technical methods, while this paper has a simpler but equally important empirical finding
- Similar in importance to "A is for Absorption" (7.5, Reject) — both identify SAE failure modes, but this paper's finding is broader

The paper lands around 6.5-7.0. Its missing statistical reporting and underdeveloped mechanistic analysis prevent it from reaching 7.0, but its clear experimental design and important finding place it solidly above 6.0.

## Summary
This paper demonstrates that widely used SAE auto-interpretability metrics (fuzzing and detection AUROC) fail to distinguish SAEs trained on trained Pythia transformers from those trained on randomly initialized models, across model sizes 70M–6.9B. The paper proposes token distribution entropy as a proof-of-concept discriminator and provides toy model analysis suggesting random networks preserve or amplify input superposition.

## Strengths
- **Well-designed multi-variant randomization with proper negative control**: Five conditions (trained, re-randomized incl/excl embeddings, step-0, Gaussian control) across five model sizes. The Gaussian control yields AUC ≈ 0.50 (Figure 1), confirming metrics function correctly, while all non-control random variants score similarly to trained models (AUC 0.87–0.88 vs. 0.79 for Pythia-6.9B).
- **Systematic scale analysis showing the problem worsens with size**: Figure 2 demonstrates across five model sizes that the AUROC gap between trained and random narrows with model size, critical since the community focuses on large models.
- **Token distribution entropy as a concrete constructive contribution**: Figure 2 (last row) shows trained models have increasing entropy across layers (abstract multi-token features), while random models have low entropy (single-token features), identifying a measurable property aggregate metrics miss.
- **Comprehensive multi-metric evaluation**: Seven metrics (EV, cosine sim, L1 norm, AUROC fuzzing/detection, CE loss, token entropy) across all variants and scales, with CE loss appropriately noted as only meaningful for trained models.
- **Robustness across SAE hyperparameters**: Results confirmed robust across expansion factors (16–128) and sparsity values (16, 32) on Pythia-160M (referenced Figure 18).

## Weaknesses

### Fatal
None

### Major
- **No error bars or statistical reporting in the main text**: The paper samples 100 features per SAE for auto-interpretability scoring and claims trained and random distributions are "similar" without reporting variance, confidence intervals, or statistical tests in the main text. Multiple random seeds are deferred to Appendix E. A reader cannot assess whether the observed "similarity" is robust or whether a few outlier features would change the picture. Even one figure showing per-feature AUROC distributions (violin plots or histograms) for trained vs. random at a representative layer would be far more informative.

- **Underdeveloped analysis of the single-token detector mechanism**: The paper's most striking result — random models score 0.87 AUROC vs. 0.79 for trained (Figure 1) — has a relatively straightforward explanation the paper acknowledges but doesn't fully develop: SAEs with expansion factor 64 and k=32 have capacity to learn per-token detectors, which are trivially "interpretable" by the metrics' definition. The token entropy analysis (Figure 2, last row) captures this partially, but the paper would be significantly strengthened by (a) showing example features from random models with their AUROC scores and maximally activating tokens in the main text, and (b) quantifying what fraction of high-scoring latents are single-token detectors per variant. Without this, the paper diagnoses the problem but leaves the key mechanism underexplored.

### Minor
- **Toy model section is somewhat disconnected from empirical results**: Section 4 provides mechanistic hypotheses for why random networks preserve superposition, but doesn't validate these mechanisms on actual Pythia activations (e.g., measuring sparsity properties of random-model activations directly). The MLP example in Figure 3 (3→2→3 dimensions) is hard to generalize from, and the Pareto frontier analysis (Figure 5) shows the difference between superposed and Gaussian outputs is "much smaller" than between inputs, which could be read as evidence that random networks mostly *destroy* superposed structure and replace it with something that just happens to be somewhat sparse.
- **Only TopK SAEs tested**: The paper uses k-sparse autoencoders exclusively. ReLU-based or JumpReLU SAEs are also widely used; a brief check would strengthen generality.

### Trivial
- **Single random seed for GloVe analysis**: Section 4.3 uses a single random seed, making this particular comparison less robust than the rest of the paper.

## Nice-to-Haves
- Show that a combined metric (AUROC + entropy threshold) successfully discriminates trained from random, demonstrating the diagnosis is actionable
- Per-feature AUROC distribution plots (violin/histogram) for a representative layer to show overlap directly

## Removed Points
These points are flagged to be removed, treat them with caution.
- None needed — all reviewer criticisms were either verified against the paper or already filtered.

## Novel Insights
The paper's most novel insight is that auto-interpretability metrics reward a specific failure mode: SAEs on random models learn single-token detector features that are trivially "interpretable" by current definitions, because the operational definition of "interpretability" used by these metrics is too weak. Combined with the scaling observation (the gap narrows with model size), this constitutes a genuine methodological warning for the mechanistic interpretability community. The constructive proposal of token distribution entropy adds practical value beyond the critique.

## Suggestions
- Add per-feature AUROC distribution plots (violin/histogram) for a representative layer and model size
- Quantify the fraction of high-scoring latents that are single-token detectors for each variant
- Include 3–5 example features from trained vs. random models in the main text with AUROC scores and maximally activating tokens
- Add bootstrapped CIs or statistical tests for key AUROC comparisons

## Reporting: Calibration Anchors

**All anchors retrieved:**

| Round | Paper | Avg Score | Comparison |
|-------|-------|-----------|------------|
| 1 | `tcsZt9ZNKD.md` - "Scaling and evaluating sparse autoencoders" | 1.75 | Far below our paper; unclear why so low (possibly parser issue — preview says 8.20) |
| 1 | `89wVrywsIy.md` - "Automatically Identifying Sparse Circuits" | 3.40 | Weaker; narrow scope, less rigorous evaluation |
| 1 | `Wxl0JMgDoU.md` - "Skill Adaptation Using SAEs" | 2.50 | Weaker; niche application |
| 1 | `9L9j5bQPIY.md` - "Metanetwork" | 2.50 | Weaker; speculative approach |
| 1 | `1Njl73JKjB.md` - "Towards Principled Evaluations of SAEs" | 7.00 | Comparable; proposes a full evaluation framework vs. our demonstration of failure mode |
| 1 | `F76bwRSLeK.md` - "SAEs Find Highly Interpretable Features" | 4.80 | Our paper is clearly stronger in experimental design and focus |
| 1 | `9ca9eHNrdH.md` - "SAEs Do Not Find Canonical Units" | 7.00 | Comparable; more technically novel (stitching, meta-SAEs), our finding is more impactful for practitioners |
| 1 | `ghH6YYDs15.md` - "Compute Optimal Inference in SAEs" | 4.67 | Our paper is stronger |
| 1 | `I4e82CIDxv.md` - "Sparse Feature Circuits" | 8.00 | Stronger paper; introduces novel methods and applications |
| 1 | `kbjJ9ZOakb.md` - "Learning invariance manifolds" | 8.00 | Different domain; stronger |
| 1 | `k38Th3x4d9.md` - "Root Cause Analysis" | 8.00 | Different domain; stronger |
| 1 | `xriGRsoAza.md` - "Interpretable Time Series" | 8.00 | Different domain; stronger |
| 2 | `6KZ80APcxf.md` - "Benchmarking XAI Explanations" | 5.50 | Weaker; less focused contribution |
| 2 | `bXeSwrVgjN.md` - "Benchmarking Deletion Metrics" | 6.00 | Similar in spirit (metrics critique) but less impactful |
| 2 | `62K7mALO2q.md` - "In-Context Learning Dynamics" | 6.00 | Different area; comparable rigor |
| 2 | `VvAiCXwPvD.md` - "Do Models Explain Themselves" | 5.67 | Weaker scope |
| 2 | `LC2KxRwC3n.md` - "A is for Absorption" | 7.50 | Comparable; identifies SAE failure mode in controlled setting; narrower scope but rejected despite high score |
| 2 | `XAjfjizaKs.md` - "Residual Stream Analysis with MLSAEs" | 6.50 | Similar quality; our finding is more impactful |

**Round 1 bracket: 6.0–7.5** (above the 4.8 and 5.5 anchors, below the 7.0 and 7.5 anchors)

**Round 2 narrowing: 6.5–7.0** (comparable to MLSAE at 6.5, slightly below Principled Evaluations and Canonical Units at 7.0)

The paper is clearly above 6.0 (better experimental design, more impactful finding than the 6.0 anchors) and slightly below 7.0 (the 7.0 anchors introduce novel technical methods while this paper's contribution is primarily empirical). The 7.5 "Absorption" paper was rejected, suggesting that even strong critique papers need to clear a high bar. Our paper sits between 6.5 and 7.0 — closer to 6.5 given the missing error bars and underdeveloped mechanistic analysis, but the importance of the finding pulls it up.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>