Now I'll write the final calibrated review.

## Summary
Thoughtbubbles introduces a transformer architecture variant that learns to fork (duplicate) or prune residual streams at intermediate layers during pretraining, using only language modeling loss. A forking decision function assigns keep/fork scores to each residual stream, and top-k selection controls the computation budget. Scores are made learnable by attenuating both attention and residual updates by cumulative scores, forcing the model to assign high scores to needed tokens. Experiments at 150M–772M scales on OpenWebText and peS2o show consistent perplexity improvements over both parameter-matched and computation-matched baselines, with strong zero-shot results on LAMBADA and HellaSwag.

## Strengths
- **Consistent perplexity improvements across all 12 settings**: Table 1 shows Thoughtbubbles achieves the lowest perplexity in all 12 configurations (3 scales × 2 datasets × 2 κ values). The 319M Thoughtbubbles model achieves 20.23 perplexity on OpenWebText, outperforming the 772M baseline's 21.22 — a smaller model beating one over 2× its size.
- **Elegant self-supervised score-attenuation mechanism**: Equations 8–10 attenuate both attention logits (via additive log-scores) and residual writes (via multiplicative scaling) proportional to cumulative scores. This forces the model to assign high scores to streams it depends on, creating gradient signal for learning which tokens to fork — all without any auxiliary loss.
- **Computation-matched baseline demonstrates adaptive allocation benefits**: The Copy-3 and Copy-5 baselines match or exceed Thoughtbubbles' FLOPs using non-adaptive duplication. Thoughtbubbles consistently outperforms these on perplexity (Table 1), showing improvements come from *adaptive* allocation rather than just more compute.
- **Interpretability analysis shows semantically meaningful computation allocation**: Figure 5 shows strong correlation between per-token output entropy and fork count, verified using entropy from both the forking model and an independently trained baseline LM. Figure 4 confirms forked streams meaningfully influence parent token computation through attention scores an order of magnitude higher than unrelated tokens.
- **Novel concave entropy-computation relationship**: The model allocates less computation at the *highest* entropy tokens (Figure 5), forming a concave parabolic curve — moderate-uncertainty tokens benefit most from extra computation, an insightful and non-obvious finding.

## Weaknesses

### Fatal
None.

### Major
- **No comparison against prior adaptive computation baselines**: The experimental comparison (Table 1) only includes standard transformer and Copy-N variants. No comparison against pause tokens (Goyal et al., 2024; Herel & Mikolov, 2024), mixture-of-depth models (Raposo et al., 2024), or Universal Transformer (Dehghani et al., 2019) is provided in the same experimental setup. These are discussed in Section 6 as related work, but the paper's core narrative — that *adaptive* allocation of extra compute drives the gains — requires empirical comparison against at least one such method at matched FLOPs. The Copy-N baseline is a reasonable lower bound but is the weakest possible form of non-adaptive additional computation. Without this comparison, the reader cannot distinguish whether Thoughtbubbles' advantage comes from being adaptive or from being a better implementation of additional residual streams.
- **No variance or error bars on any reported metric**: Table 1 reports single numbers for every configuration across 12 settings × 5 methods × 5 metrics. Given that these are models trained for only 2.5B tokens, variance across random seeds could be meaningful — especially on zero-shot tasks where differences are sometimes thin (e.g., 319M peS2o HellaSwag: Thoughtbubbles κ=4L = 27.2 vs Copy-3 = 27.2, tied at Table 1 lines 202 and 205). Without even one rerun to bound variance, the reader cannot distinguish signal from noise for tighter comparisons. The perplexity improvements are large enough to be robust, but several zero-shot claims rest on margins that could reverse with a different seed.

### Minor
- **Low absolute performance limits practical significance**: At 772M parameters with 2.5B training tokens, HellaSwag accuracy is 32.25% (vs. ~25% chance). While relative improvements that scale consistently are informative, both the improved and baseline models are in a regime of poor absolute performance, bounding confidence about the method's value at practical scales. The paper acknowledges this due to resource-limited training.
- **BLiMP results are mixed**: On BLiMP, Thoughtbubbles frequently underperforms the computation-matched baseline (e.g., 772M peS2o: 67.4 vs Copy-3's 73.3, Table 1 lines 200 and 197). The paper claims "outperforms across most zero-shot evaluations" which is generally true, but the BLiMP underperformance deserves more discussion.
- **Novelty claim could be better qualified**: The paper claims "first-known architecture to enable the unsupervised dynamic allocation of latent parallel computation" (line 33). Mixture-of-Depth models (Raposo et al., 2024, cited in Section 6) also learn to allocate computation adaptively during pretraining with standard LM loss, albeit through depth-skipping rather than stream-forking. The claim should more carefully distinguish from this prior work.

### Trivial
None.

## Nice-to-Haves
- Summarize the forking-layer placement ablation (Appendix B) in the main text — forking only in early layers (before layers 3, 7, 11) is a key design choice readers will scrutinize.
- Report training loss curves or evolution of forking patterns during training to show when and how the model learns meaningful fork allocation.
- Briefly explain the ratio-based dynamic forking scaling (Appendix E.1) in the main text for readability.

## Removed Points
These points are flagged to be removed, treat them with caution:
- The harsh critic's concern about the "first-known architecture" claim is partially valid but also partially addressed: the paper qualifies with "latent parallel computation" which distinguishes from MoD's depth-skipping. Kept as a minor weakness but demoted from harsh framing.
- Strength Finder's claim about cross-entropy output averaging being "principled" is valid (Equation 11, log-sum-exp trick) but is more of a design detail than a core strength.

## Novel Insights
The concave entropy-computation relationship (Figure 5) — where the model allocates less computation at the *highest* entropy tokens rather than monotonically increasing with uncertainty — is a genuinely novel empirical finding. The interpretation that moderate-uncertainty tokens (e.g., disambiguation points) benefit more from extra computation than maximally uncertain ones (e.g., clause boundaries) is insightful and has implications for future adaptive computation designs. Additionally, the finding that fixed-budget autoregression causes distribution shift (Section 5.1, Figure 6) with dynamic budget scaling as mitigation is a practical contribution.

## Suggestions
- Add at least one pause-token baseline at matched FLOPs to sharpen the core claim about adaptive allocation.
- Report variance for at least the 772M models across one additional seed.
- Briefly summarize the Appendix B forking-layer placement ablation in the main text.

## Calibration Report

**Round 1 anchors:**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| NSBP7HzA5Z (Inductive Transformers) | 3.00 | 1 | Weaker: conceptual, no real LM experiments |
| 5dDYhvt6dY (Efficient Transformer Position Embedding) | 3.00 | 1 | Weaker: small-scale translation task only |
| ulGwcj1egv (FiRST Router-Selective) | 3.00 | 1 | Weaker: inference-only optimization, not adaptive pretraining |
| tI3eqOV6Yt (Hyper-UT) | 5.00 | 1 | Weaker: synthetic tasks, less consistent results |
| 7igPXQFupX (CoTFormer) | 5.75 | 1 | Comparable: adaptive computation, but less consistent results and weaker analysis |
| 89XNDtqhpL (MatFormer) | 6.00 | 1 | Comparable: elastic inference architecture but different focus |
| STUGfUz8ob (Abstract Symbol Reasoning) | 7.60 | 1 | Stronger: theoretical proofs + empirical, broader impact |
| OvoCm1gGhN (Diff Transformer) | 8.00 | 1 | Stronger: much larger scale (3B/350B tokens), more benchmarks |
| PdaPky8MUn (Never Train from Scratch) | 8.00 | 1 | Stronger: methodological insight paper with broad implications |

**Round 2 anchors:**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| vPOMTkmSiu (Scaling Laws for MT) | 6.60 | 2 | Comparable quality but different focus |
| mz8owj4DXu (Scalable LM Continual Learning) | 6.50 | 2 | Comparable: adaptive method with consistent improvements |
| mao3y822aM (NanoLM) | 5.50 | 2 | Weaker: benchmark paper |
| T26f9z2rEe (DynMoE) | 7.00 | 2 | Comparable: adaptive MoE routing, similar consistency but Thoughtbubbles is more novel |
| t7P5BUKcYv (MoE++) | 8.00 | 2 | Stronger: large scale, clear throughput gains |
| W8K8slZ73R (Adaptive Transformer Programs) | 7.00 | 2 | Different focus (interpretability), comparable novelty |

**Round 1 bracket**: 5.5–7.5 (between CoTFormer at 5.75 and Differential Transformer at 8.0).

**Round 2 narrowing**: Thoughtbubbles is clearly above CoTFormer (5.75) with more consistent results and better analysis. It is comparable to DynMoE (7.0) in contribution quality but has weaker evaluation (no variance, missing adaptive baselines). It is below Diff Transformer (8.0) and MoE++ (8.0) which have much larger scale experiments. Final score: **6.5**, a solid paper with genuine novelty that should be accepted with minor revisions.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>