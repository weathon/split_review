Now let me write the final consolidated review.

## Summary

The paper proposes PI-CCA, a replay-free continual learning framework for VLMs that preserves cross-modal alignment by directly constraining the canonical correlation spectrum and subspaces of the whitened image-text cross-covariance, summarized in a compact, prompt-invariant certificate. Across MTIL, X-TAIL, VLCL, and ConStruct-VL, PI-CCA achieves top results among replay-free methods and even outperforms some synthetic-replay baselines without storing or generating past data.

## Strengths

- **Principled geometry-first formulation.** PI-CCA recasts forgetting as drift of CCA invariants (canonical correlations and subspaces) of the whitened cross-covariance matrix — a clean conceptual departure from prior methods that regularize proxy signals (logits, similarities, parameters). The ablation study (Table 3) confirms that removing the spectral or subspace terms causes the largest performance drops (MTIL Avg drops 2.5 and 2.2 p.p., respectively), supporting the design rationale.

- **Strong empirical results across diverse benchmarks.** PI-CCA achieves the best results among replay-free methods on all four tracks: MTIL Avg 76.8 (vs. next-best C-CLIP 75.2), VLCL I2T R@1 48.6±1.0 (vs. 46.1±1.4), ConStruct-VL FA 75.2±1.3 and AF 2.7±0.2. It even surpasses the synthetic-replay method GIFT (47.3 R@1) without generating any data. This breadth — covering classification, retrieval, and structured-concept matching — strengthens the claim that the approach generalizes.

- **Prompt-robustness mechanism with measurable effect.** The \(\mathcal{L}_{\text{pi}}\) loss (projector averaging + dispersion contraction) demonstrably reduces sensitivity to prompt variation. Figure 4 shows consistent improvements at perturbation strength \(s=1.0\): +2.44 p.p. (ID) and +2.51 p.p. (OOD) on VLCL I2T R@1, with flatter degradation slopes for AF across the full stress range.

- **Comprehensive efficiency analysis.** Figure 2 provides a systematic Pareto sweep over certificate dimensions \((k, h)\), showing a broad efficient ridge with low memory (3–4 GB) and step time, supporting the "small yet sufficient" certificate claim. The paper reports both peak memory and wall-clock time.

## Weaknesses

### Fatal

None.

### Major

- **Questionable correlation values in the geometry → performance analysis (Fig. 3).** The paper reports Pearson \(r=1.00\) and Spearman \(\rho=1.00\) for two of the four subplots, and \(\rho=1.00\) for all four. Perfect correlations are effectively impossible for any real experimental data with even minimal stochasticity (from network training, minibatch sampling, etc.). This suggests either (a) a very small number of data points, (b) computational error in the reporting, (c) heavy rounding that hides real variance, or (d) that the drift and performance drop are computed from the same deterministic function of the same hyperparameters, making the correlation tautological. Since this figure is presented as the paper's central mechanistic evidence ("stability of the canonical subspace/spectrum reliably predicts downstream performance"), the lack of trustworthy correlation values undermines a key supporting claim. The authors should disclose the number of data points, recompute with proper decimal precision, and ideally include error bars from multiple runs.

- **Missing controlled baseline: LoRA + task loss only.** The ablations in Table 3 remove one CCA term at a time but retain the rest of the CCA infrastructure. Without a baseline that runs the same frozen backbone with only \(\mathcal{L}_{\text{task}}\) (e.g., InfoNCE) and no CCA losses, the reader cannot judge whether the gains come from the CCA certificates or simply from LoRA fine-tuning itself. This is a standard control and its absence is a significant gap in the experimental design.

- **Backbone architecture not explicitly stated in main paper.** The paper describes the setup as "frozen backbone + LoRA" but does not specify which backbone (e.g., RN50, ViT-B/16, ViT-L) is used for the main results. The reproducibility statement mentions "backbones/adapters" in the Appendix (stripped from the submission), but without this information in the main text, the reported state-of-the-art comparisons are hard to interpret — different baselines may have used different backbones or fine-tuning protocols. The "SOTA among replay-free methods" claim requires a controlled apples-to-apples comparison on the same backbone.

### Minor

- **No uncertainty reported in Table 1 (MTIL, X-TAIL).** Table 2 reports \(\pm\) values for VLCL and ConStruct-VL, but Table 1 gives only point estimates. Since continual learning experiments are sensitive to random seeds, the absence of variance makes it difficult to assess whether the reported margins (e.g., 76.8 vs. 75.2 on MTIL Avg) are statistically meaningful.

- **Computational cost analysis lacks baseline comparison.** The paper reports per-step wall time and peak memory for PI-CCA (Fig. 2), but does not compare these against any baseline method. The whitening + SVD per mini-batch incurs \(O(d^3)\) cost (eigendecomposition for \(\Sigma^{-1/2}\) and SVD of \(M\)), and without knowing whether this is comparable to or substantially slower than methods like C-CLIP or ZSCL, the practicality claim is incomplete.

- **Certificate update via EMA permits drift; tension with "invariant" framing not discussed.** The certificate is updated every step via EMA (Eq. 13), meaning it is not truly invariant but slowly drifts toward recent tasks. The paper acknowledges this and provides an ablation (\(\alpha=0\) drops MTIL Avg by 1.2 p.p.), but the conceptual tension between "preserving pre-trained alignment" and "continuously updating the certificate" is not examined. Does the certificate converge to a blend that still represents all tasks, or does it simply track the most recent task with a lag?

### Trivial

- Figure 3 scatter plots are described in the text as showing "scatter" and "realistic scatter" (caption), yet the correlation values reported are 1.00 — the text and numbers are contradictory.
- The paper would benefit from clarifying whether Table 1 results are single-seed or multi-seed.

## Nice-to-Haves

- Comparison against a simpler covariance regularization baseline (e.g., keeping \(\|\Sigma_{vt}\|_F\) close to its initial value) to assess whether the full CCA machinery is necessary or if weaker geometry constraints suffice.
- Profiling how step time scales with embedding dimension \(d \in \{512, 768, 1024, 1664\}\) to better characterize scalability.
- A concrete table of ID vs. OOD prompt perturbation examples to illustrate what "prompt invariance" means in practice.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"SOTA uninterpretable due to unknown backbone"** — Overstated. The paper reports comparisons against published numbers from the same benchmarks; while stating the backbone explicitly would improve rigor, the main results are still interpretable as benchmark-level comparisons. This has been moved to a Major weakness (backbone not stated) rather than a fatal flaw.
- **"Pearson r=1.00 suggests computational error (plotting variable against itself)"** — Speculative. The two subplots with r=0.99 show that this is not a self-correlation. The concern is genuine but the specific accusation of self-plotting is unsupported.
- **"The streaming covariance EMA stores \(d_v \times d_v\) matrices, prohibitive at scale"** — Partially addressed. The paper uses low-rank sketches (\(h \ll d\)) for the certificate. The actual covariance EMAs are \(d_v^2\) and \(d_t^2\), but the paper does mention the sketch reduces storage and the Pareto analysis (Fig. 2) shows memory footprint.
- **"Cannot be practically deployed on modern VLM scales"** — Speculative without evidence. The paper demonstrates on ViT-B scale with efficiency metrics. Whether it scales to ViT-L is an open question, not a demonstrated failure.
- **Missing related works** — Cannot verify without external sources.
- **Formatting/typo nitpicks** — Parser artifacts.
- **Appendix-dependent details not in main paper** — Parser-stripped content.

## Novel Insights

None beyond the paper's own contributions. The two reviews do not surface perspectives that go deeper than what the paper already articulates.

## Suggestions

1. **Fix Fig. 3.** Disclose the number of data points per subplot, report correlations with sufficient decimal precision (e.g., 0.999 rather than 1.00), and ideally include error bars from multiple runs. If the data is truly deterministic, explain why and note the limitations of this analysis.
2. **Add a LoRA-only baseline.** Run the same frozen backbone with only \(\mathcal{L}_{\text{task}}\) and no CCA terms. This is the minimal control for attributing gains to the CCA certificates.
3. **State the backbone architecture explicitly in the main paper.** Also clarify whether all baselines in Tables 1–2 are evaluated under the same backbone and protocol, or whether the comparison is against published numbers.
4. **Add uncertainty estimates to Table 1** (at minimum report standard deviations over 3+ seeds).
5. **Compare computational cost against baselines.** Report total training time and/or step time for PI-CCA vs. at least 2–3 baselines under the same hardware.

## Score and Decision

### Calibration Anchors

| Path | Human Score | Comparison to this paper |
|------|-------------|--------------------------|
| `/home/wg25r/review_agent/human_reviews_2026/rMHZfCznhZ.md` (RLAP-CLIP) | 6.00 | Accepted poster with similar VL-CL scope; classification-only evaluation but stronger experimental control. PI-CCA has broader benchmarks but weaker rigor on Fig. 3. |
| `/home/wg25r/review_agent/human_reviews_2026/T3Vc5fkTzV.md` (KeepLoRA) | 5.50 | Accepted poster; similar principled subspace approach with theoretical analysis. KeepLoRA has clearer experimental setup; PI-CCA has more benchmark diversity but questionable correlation evidence. |
| `/home/wg25r/review_agent/human_reviews_2026/eiTy6AYeQi.md` (Compo-ReAlign) | 6.00 | Accepted poster; geometry-first VL-CL method with compositional focus. Comparable evaluation breadth and analytical depth; fewer experimental gaps than PI-CCA. |
| `/home/wg25r/review_agent/human_reviews_2026/Hc71kKCEFG.md` (N2L) | 4.80 | Accepted poster targeting a different VL-CL scenario (unlabeled data). Lower conceptual novelty; PI-CCA's core idea is more original. |
| `/home/wg25r/review_agent/human_reviews_2026/HN18kuyf4o.md` (CaRD) | 4.00 | Rejected replay-based method with computational overhead concerns. PI-CCA is replay-free and more principled but has similar concerns about evaluation rigor. |
| `/home/wg25r/review_agent/human_reviews_2026/fQTw3w3hnA.md` (CoFiCL) | 3.00 | Rejected; limited novelty, dual-path design similar to prior work. PI-CCA's CCA-certificate approach is substantially more novel. |
| `/home/wg25r/review_agent/human_reviews_2026/WLSt5tIOSA.md` | 4.00 | Rejected; empirical study with limited novelty. PI-CCA has a stronger methodological contribution. |

### Decision Rationale

PI-CCA proposes a conceptually clean and well-motivated idea (preserving CCA invariants for replay-free VL-CL) with strong empirical results across four diverse benchmarks, extensive ablations, and efficiency analysis. However, the questionable perfect-correlation values in Figure 3 are a significant red flag for the paper's mechanistic evidence, and the evaluation has notable rigor gaps (unspecified backbone, missing LoRA-only baseline, no variance in Table 1). These issues are addressable in revision but prevent full confidence in the current form. Relative to accepted posters at this venue (KeepLoRA at 5.5, Compo-ReAlign at 6.0), PI-CCA has a more novel conceptual contribution but weaker experimental execution on several fronts.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>