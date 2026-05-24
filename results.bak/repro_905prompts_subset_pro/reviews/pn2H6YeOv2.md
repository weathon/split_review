Now I have a clear calibration. Let me synthesize the final review.

**Round 1 bracket**: 6.5–8.0 (Pi-CCA is clearly above C-CLIP at 6.50 but below strong 8.0+ papers)
**Round 2 narrowing**: Compared against TiC-CLIP (6.25), C-CLIP (6.50), and RoboShot (7.50)

Pi-CCA is empirically stronger and more principled than C-CLIP (6.50), but the correlation analysis issue and missing specification details place it below RoboShot (7.50), which has cleaner presentation and theory. **Final score: 7.0**.

---

## Summary
This paper proposes Pi-CCA, a replay-free continual learning framework for vision-language models that reframes catastrophic forgetting as drift in the geometry of cross-modal alignment. Rather than regularizing proxy signals (logits, similarities, weights), Pi-CCA maintains a compact "CCA certificate" capturing the top-k canonical correlations and sketched canonical subspaces, and enforces spectral and subspace-angle consistency during adaptation using only mini-batch statistics. A prompt-invariance mechanism averages text projectors over perturbations to improve robustness to phrasing changes. Across four VL-CL benchmarks (MTIL, X-TAIL, VLCL, ConStruct-VL), Pi-CCA achieves state-of-the-art results among replay-free methods, with thorough ablation demonstrating that each component contributes meaningfully.

## Strengths
- **Strong and broad empirical results.** Tables 1–2 show Pi-CCA achieves top performance among replay-free methods across all four benchmarks: MTIL Avg 76.8 / Last 75.5, X-TAIL Avg 68.1, VLCL I2T R@1 48.6, and ConStruct-VL FA 75.2 / AF 2.7. On VLCL retrieval, it even surpasses a synthetic-replay method (GIFT) without storing or generating any data.
- **Thorough component-level ablation.** Table 3 quantifies the contribution of each design element — removing the spectral loss, subspace loss, prompt invariance, certificate EMA, or covariance EMA each causes measurable degradation, with the spectral and subspace terms being most critical. This provides credible evidence that the geometry-preserving mechanism, not confounding factors, drives the performance.
- **Prompt-invariance stress test is convincing.** Figure 4 demonstrates that the prompt-invariance loss (L_pi) meaningfully flattens accuracy decay under increasing ID/OOD perturbation strength, with +2.44–2.51 p.p. R@1 gains at maximum perturbation and consistently lower forgetting. This directly validates a core claimed capability.
- **Efficiency analysis establishes practical viability.** The Pareto analysis in Figure 2 shows that certificate capacity (k, h) admits a broad efficient ridge balancing memory, time, and accuracy — a "small yet sufficient" certificate is genuinely achievable.
- **Conceptually clean framing.** Reframing forgetting as alignment-geometry drift and targeting canonical correlations/subspaces as first-class invariants is a principled departure from proxy-based regularization approaches, and the method is agnostic to downstream task objectives.

## Weaknesses

### Fatal
None.

### Major
- **Correlation analysis (Figure 3) reports implausible statistics and is internally contradictory.** The figure annotates Pearson r = 1.00 and Spearman ρ = 1.00 for subspace-angle drift vs. performance drops, while the caption claims "realistic scatter." A perfect linear relationship (r = 1.00) is, by definition, scatter-free. These numbers are obtained from sweeping hyperparameter configurations of Pi-CCA itself (certificate size, EMAs, invariance strength, etc.), and while a strong correlation is expected (configurations that preserve geometry better should perform better), exact unity across multiple measured quantities with finite samples is not credible. This does not invalidate the paper's core method — the ablation study (Table 3) provides independent evidence that the geometry-preserving losses matter — but the figure as presented undermines the "geometry predicts performance" narrative and should be corrected with honest correlation coefficients.

### Minor
- **Initial certificate construction is underspecified.** The paper states that the reference CCA certificate is constructed "from a diverse anchor prompt set" (line 102) but does not describe what images, text prompts, or dataset size are used to compute the initial ρ*, U*, V*. The certificate is refreshed via EMA during training (Eq. 13), which mitigates dependence on the initial state, but for reproducibility the initialization procedure should be specified — at minimum, what data passes through the frozen pre-trained model to compute the reference CCA.
- **No variance reported for classification results (Table 1).** Table 2 includes standard deviations; Table 1 does not. The gaps between Pi-CCA and the next-best method on MTIL (76.8 vs. 75.2 Avg, 75.5 vs. 73.8 Last) are large enough to be meaningful, but for tighter comparisons (e.g., X-TAIL Last: 66.9 vs. 66.3) error estimates would strengthen confidence. This is a presentation gap rather than a methodological flaw.

### Trivial
- The paper does not clarify whether baseline numbers in Tables 1–2 were re-run under identical conditions (backbone, LoRA configuration, learning rate schedule) or taken from prior publications. This is standard practice in the field, and the paper follows established protocols from ZSCL, RAIL, and C-CLIP, but a brief note would improve transparency.

## Nice-to-Haves
- The correlation analysis (Figure 3) would be more convincing if extended to compare drift–performance relationships *across different methods* (not just Pi-CCA hyperparameter variants), which would more directly support the claim that geometry drift causes forgetting generically rather than being a within-method consistency check.
- Reporting per-seed error bars for Table 1 and conducting significance tests against the strongest baselines would elevate the evaluation rigor.
- The task-order sensitivity study (Figure 5) currently covers only Pi-CCA on MTIL. Comparing order sensitivity across methods would strengthen claims of robustness.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **Harsh critic: "correlation analysis is fatal/structural."** Removed as "fatal." The ablation study independently validates the geometry-preserving components. The correlation figure is problematic but supplementary; correcting it would not change the paper's core contribution. Kept as Major weakness.
- **Harsh critic: "method is not reproducible / cannot be independently verified."** Removed. The paper provides algorithmic details (Algorithm 1 in appendix), streaming EMA equations, and states code will be released. The certificate initialization detail is a minor gap, not a barrier to reproducibility.
- **Harsh critic: "baselines were not re-run under identical conditions."** Moved to Trivial. Following standard benchmark protocols with published numbers is accepted practice; the paper explicitly follows ZSCL, RAIL, and C-CLIP protocols.
- **Harsh critic: "task-order sensitivity only covers one method."** Removed as a weakness. Studying the method's own sensitivity to order is legitimate supplementary analysis; comparing to baselines would be nice-to-have but is not required.
- **Strength Finder: "Direct evidence that alignment-geometry drift predicts performance loss (Figure 3)."** Demoted. While the trend direction is credible, the reported r=1.00 statistics undermine the strength of this evidence.
- **Harsh critic: demands about SVD differentiation bias, power-iteration convergence.** Removed. These are implementation-level concerns about a standard technique (power iteration with stop-gradient) that the paper already acknowledges and addresses.

## Novel Insights
The core conceptual move — treating the whitened cross-modal covariance's canonical spectrum and subspaces as the invariant to preserve, rather than distilling logits or matching similarity distributions — is genuinely novel for VL continual learning. While CCA has been used diagnostically in representation analysis, using it as an *optimization target* with sketched, replay-free certificates that are updated via EMA is a non-obvious synthesis. The projector-averaging trick for prompt invariance elegantly sidesteps sign/rotation ambiguity without Procrustes alignment, which is a clean technical contribution.

## Suggestions
- Recompute Figure 3 correlations and report actual values (even if they are, say, r = 0.92–0.97 — that would still strongly support the narrative). Remove the "realistic scatter" phrasing if the correlation is near-perfect, or explain why near-perfect correlation emerges from the hyperparameter sweep.
- Specify the anchor dataset used for initial certificate construction: what images, what prompts, and how many samples.
- Add standard deviations or confidence intervals to Table 1, at minimum for Pi-CCA's own results.

## Score and Decision

**Calibration summary:**
- TiC-CLIP (6.25): Benchmark contribution with limited method novelty; Pi-CCA is clearly stronger with a novel method and SOTA results.
- C-CLIP (6.50): Direct predecessor; Pi-CCA improves upon it empirically, conceptually, and in evaluation breadth. Pi-CCA > C-CLIP.
- RoboShot / fCeUoDr9Tq (7.50): Novel zero-shot robustification with theoretical grounding; cleaner presentation and more modest claims. Pi-CCA has broader benchmarks and stronger empirical results but the correlation figure issue and missing specification details place it slightly below.
- **Final score: 7.0** — a solid accept with fixable presentation issues in the correlation analysis.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>