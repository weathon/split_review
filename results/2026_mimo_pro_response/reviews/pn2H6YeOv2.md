## Summary
PI-CCA introduces a replay-free continual learning framework for vision-language models that preserves cross-modal alignment geometry by maintaining a compact "CCA certificate" — the top-k canonical correlations and sketched canonical subspaces — updated via exponential moving averages. During adaptation, spectral and subspace losses constrain drift from the reference alignment, while a prompt-invariance loss (via projector averaging over perturbations) induces robustness to phrasing variation. The method achieves SOTA among replay-free approaches across four VL-CL benchmarks (MTIL, X-TAIL, VLCL, ConStruct-VL).

## Strengths
- **Well-grounded conceptual reframing with strong empirical support.** The paper's central thesis — that forgetting in VL-CL is better understood as alignment-geometry drift than as proxy-matching — is validated by Figure 3, which shows near-perfect correlations (Pearson r ≥ 0.99, Spearman ρ = 1.00) between subspace-angle/spectral drift and performance drops across diverse hyperparameter perturbations (certificate size, EMAs, invariance strength, whitening, pairing, LoRA capacity/LR, sketch type). This goes beyond anecdotal evidence.
- **Consistent SOTA across four diverse benchmarks.** Tables 1–2 show improvements over the strongest replay-free baselines: +1.6 p.p. Avg on MTIL over C-CLIP, +2.5 p.p. I2T R@1 on VLCL (surpassing even synthetic-replay GIFT), and +2.8 p.p. FA / −0.6 AF on ConStruct-VL. The breadth of evaluation across classification, retrieval, and structured-concept tasks exceeds most prior VL-CL work.
- **Thorough component-wise ablation (Table 3).** Removing spectral preservation (λ₁=0) causes −2.5 p.p. MTIL Avg drop; removing subspace loss (λ₂=0) causes −2.2 p.p.; removing covariance EMA (β=0) causes −2.7 p.p. Each component contributes materially. The ablation covers 8 single-factor variants including sketch type (Gaussian vs. SRHT), pairing strategy (sorted vs. Hungarian), and spectral moments.
- **Practical efficiency via constant-memory random sketching.** The certificate stores only ρ₁:ₖ ∈ ℝᵏ, S_v* ∈ ℝ^{h×k}, S̄_t* ∈ ℝ^{h×k} (Eq. 4) with h ≪ d_v, d_t. Figure 2's Pareto analysis identifies a broad efficient frontier at k ∈ [48,96], h ∈ [192,320], confirming the "small yet sufficient" hypothesis with the default (k=64, h=256) near the knee.
- **Task-order robustness and prompt invariance stress tests.** Figure 5 shows narrow IQRs across 20 random task orders. Figure 4 demonstrates L_pi flattens degradation curves under increasing prompt perturbation strength, with +2.44 p.p. R@1 improvement at s=1.0 (ID templates).

## Weaknesses

### Fatal
None.

### Major
- **Missing error bars on classification benchmarks (Table 1).** Table 1 reports MTIL and X-TAIL results as point estimates without standard deviations, while Table 2 (VLCL, ConStruct-VL) reports mean ± std. The margins in Table 1 are modest (+1.6 p.p. Avg on MTIL, +0.7 p.p. on X-TAIL over C-CLIP). Without variance estimates, it is impossible to assess whether these differences are statistically reliable. The paper should either add error bars to Table 1 or explicitly state whether these numbers come from single runs or are taken from prior papers.

- **Computational overhead of certificate machinery is not quantified.** The paper claims "constant memory" (true w.r.t. number of tasks), but the streaming EMAs of Σ_vv ∈ ℝ^{d_v×d_v}, Σ_tt ∈ ℝ^{d_t×d_t}, Σ_vt ∈ ℝ^{d_v×d_t} (Eq. 12) plus the eigendecomposition for Σ^{-1/2} (O(d³)) represent nontrivial overhead. The paper mentions Newton–Schulz iteration as an alternative but never reports per-step wall-clock time or memory overhead of PI-CCA vs. bare LoRA fine-tuning. Figure 2 sweeps k and h (affecting sketch/certificate size) but the covariance EMA overhead is fixed and not part of that sweep.

### Minor
- **Ambiguous gradient flow through whitening.** Line 131 states "stop-gradient on the inverse square root if needed" without specifying the default setting. Whether gradients flow through Σ^{-1/2} affects optimization dynamics significantly. The paper should state and justify the default.
- **Near-perfect geometry-performance correlations (Fig. 3) deserve more discussion.** The scatter plots show Pearson r = 0.99–1.00, which is suspiciously close to perfect. Some perturbations (e.g., changing k) directly alter the x-axis quantity while naturally affecting performance, potentially inflating the correlation. The paper should clarify which perturbation types contribute most to the spread.
- **Mention of TiC-YFCC/RedCaps study with no results in main text.** Line 146 states "We additionally report a time-continual study on a medium-scale split of TiC-YFCC/RedCaps" but no such results appear in the main text. Either include them or remove the mention.

### Trivial
None.

## Nice-to-Haves
- Analysis of sensitivity to the initial pre-trained alignment quality (e.g., domain-specific VLMs with poor starting alignment).
- Clarification of whether task boundaries are needed (the paper claims "no task IDs" but does not verify if step boundaries are required for bookkeeping).
- Details on prompt perturbation distribution P (currently deferred to appendix).

## Removed Points
These points are flagged to be removed, treat them with caution:
- **Garbled expression at Line 129**: The harsh critic noted M^{(t)} = (Σ_v^{(t)})^{-1/2} (Σ_v^{(t)})^{-1/2} appears to be missing Σ_{vt}. This is a PDF parsing artifact — the original paper almost certainly contains the correct expression consistent with Eq. 2. Removed per formatting artifact policy.
- **Stop-gradient vagueness as major concern**: The concern is real but the paper does describe two whitening approaches (eigendecomposition and Newton-Schulz) and mentions stop-gradient. Demoted from major to minor.
- **General concerns about initial alignment quality**: Speculative concern not supported by any specific failure mode in the paper.

## Novel Insights
The paper's genuinely novel insight is the reframing of VL-CL forgetting as alignment-geometry drift in the canonical correlation structure of the whitened cross-modal covariance, rather than as a mismatch in proxy signals (logits, similarities, parameters). The empirical validation in Figure 3 — showing that subspace-angle and spectral drift are near-perfect predictors of downstream performance degradation across diverse perturbations — provides compelling evidence that this is not merely a conceptual reframing but a practically useful invariant. The CCA certificate mechanism (spectral + subspace + prompt-invariant text sketch) is a clean operationalization of this insight achieving constant-memory, replay-free consolidation.

## Suggestions
- Add mean ± std over at least 3 seeds to Table 1 for MTIL and X-TAIL, matching the reporting convention of Table 2.
- Add a small table or paragraph reporting per-step wall-clock time and memory overhead of PI-CCA vs. bare LoRA fine-tuning.
- State the default gradient flow setting for the whitening operation explicitly with justification.
- In the Fig. 3 caption, break down which perturbation types contribute most to the x-axis spread to address potential circularity.
- Either include TiC-YFCC/RedCaps results in the main text or remove the mention from §4.1.

## Calibration Report

**Round 1 — Bracketing.** Searched for comparable papers across 6 score bands on continual learning for vision-language models.

**All anchors retrieved:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| 5lUdTogEL3.md | 1.00 | 1 | Weak clothing ReID paper; PI-CCA is far stronger |
| JIlIYIHMuv.md | 2.50 | 1 | LVLM-CL reject; PI-CCA has cleaner method + better results |
| gNoqEdT2wO.md | 2.33 | 1 | Multimodal CL benchmark only; PI-CCA is more complete |
| G9Ea7mlqGO.md | 3.80 | 1 | CLIP online CL reject; simpler method, less rigorous |
| 9aZ2ixiYGd.md | 5.00 | 1 | VLM synergy for CL; wider score variance, less rigorous |
| rwmwFnmjAX.md | 4.75 | 1 | Continual LLaVA reject; novelty concerns |
| EKfcngSxwD.md | 4.67 | 1 | Task Codebook VLM; narrower scope |
| k9NYnsC4Mq.md | 5.67 | 1 | PROOF VLM-CL reject; less principled than PI-CCA |
| sb7qHFYwBc.md | 6.50 | 1/2 | C-CLIP (baseline in PI-CCA); PI-CCA clearly outperforms |
| TLADT8Wrhn.md | 6.25 | 1/2 | TiC-CLIP benchmark; PI-CCA has stronger method |
| ScI7IlKGdI.md | 6.33 | 1 | Spurious forgetting in LLMs; different domain |
| Hcb2cgPbMg.md | 6.25 | 2 | Spectral regularization CL; PI-CCA has better VL evaluation |
| kIP0duasBb.md | 6.67 | 2 | CLIP TTA; narrower scope |
| mz8owj4DXu.md | 6.50 | 2 | SLM continual; different modality focus |
| b20VK2GnSs.md | 7.00 | 2 | Concept drift MLLM; comparable quality, PI-CCA cleaner eval |
| 7D9X2cFnt1.md | 7.00 | 2 | EFC; comparable principled approach, good experiments |
| cmXWYolrlo.md | 7.50 | 2 | Geometric inductive biases; analysis paper, not CL |
| OZVTqoli2N.md | 7.50 | 2 | Second-order compositionality; different focus |
| dOAkHmsjRX.md | 7.50 | 2 | Budgeted online CL; more narrow setting |
| 9bMZ29SPVx.md | 7.50 | 2 | CLIP data selection; different problem |
| uAFHCZRmXk.md | 8.00 | 1 | Modality gap analysis; stronger theoretical contribution |
| 3i13Gev2hV.md | 8.00 | 1 | Hyperbolic VLM; novel representation learning |

**Round 1 bracket: 6.5–7.5.** PI-CCA clearly surpasses C-CLIP (6.50) and the rejected VL-CL papers (3.8–5.67). It is comparable in quality to EFC (7.00) and Concept Drift MLLM (7.00) — both principled methods with strong evaluation that received Accept decisions. It falls slightly below the 7.5+ papers which tend to have either stronger theoretical contributions or broader impact.

**Round 2 narrowing:** The 7.0 anchors (EFC, Concept Drift) are the best comparators. PI-CCA matches them in rigor (4 benchmarks, thorough ablation, novel analyses) and has a slightly more distinctive conceptual contribution (alignment-geometry drift as an invariant). The missing error bars on Table 1 and unquantified computational overhead pull it slightly below 7.5.

**Final score: 7.0.**

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>