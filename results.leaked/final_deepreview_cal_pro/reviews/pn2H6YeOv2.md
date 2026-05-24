Now I have a thorough understanding of the paper and the calibration anchors. Let me synthesize the final review.

---

## Summary

Pi-CCA proposes a replay-free continual learning method for vision-language models that preserves cross-modal alignment by matching a compact CCA certificate (top-k canonical correlations and sketched subspaces). During adaptation on new tasks, the method regularizes toward these spectral and subspace invariants using only mini-batch statistics, and adds a prompt-invariance loss via projector averaging over perturbations. The paper evaluates across four standard VL-CL benchmarks (MTIL, X-TAIL, VLCL, ConStruct-VL) and reports state-of-the-art performance among replay-free methods, backed by extensive ablations and analysis.

## Strengths

- **SOTA replay-free performance across four VL-CL benchmarks.** Tables 1–2 show Pi-CCA ranking first among all replay-free methods on MTIL (Avg 76.8), X-TAIL (Avg 68.1), VLCL (I2T R@1 48.6), and ConStruct-VL (FA 75.2, AF 2.7), even surpassing the synthetic-replay method GIFT on retrieval. The consistent margin across diverse evaluation protocols is a strong empirical signal.

- **Principled geometry-first framing.** The paper reframes forgetting in VL-CL as drift in the canonical alignment geometry (spectrum + subspaces of the whitened cross-covariance) rather than drift in proxy signals (logits, similarities, parameters). This conceptual shift is well-motivated in the introduction and related work (§1–2) and is executed cleanly in the method design (§3).

- **Thorough component-wise ablation.** Table 3 demonstrates that removing the spectral term (λ₁=0), subspace term (λ₂=0), or prompt-invariance term (λ₃=0) each cause measurable degradation across multiple metrics (e.g., −2.5 pp MTIL Avg for λ₁=0, −2.7 pp VLCL I2T R@1 for λ₂=0). The ablation also validates design choices (EMA, Hungarian pairing, sketch type) showing expected small effects.

- **Task-order robustness demonstrated convincingly.** Figure 5 shows boxplots over 20 random MTIL task orders with narrow IQRs (<1 pp for Avg, <1.5 pp for Last), ruling out the possibility that results are an artifact of a favorable sequence.

- **Certificate capacity Pareto analysis is informative.** Figure 2 sweeps k ∈ [16,128] and h ∈ [128,384], identifying a robust ridge (k ∈ [48,96], h ∈ [192,320]) where performance is near-optimal. The default (64,256) sits at the knee, confirming the "small yet sufficient" hypothesis with concrete evidence.

- **Prompt-invariance stress test isolates L_pi's effect.** Figure 4 shows that with L_pi, the degradation slopes flatten as perturbation strength s increases, with clear quantitative improvements (+2.44 pp R@1 ID, +2.51 pp OOD at s=1.0) over the ablated model.

## Weaknesses

### Fatal

None.

### Major

- **Implausible correlation coefficients in the geometry–performance analysis (Figure 3).** The paper reports Pearson r = 1.00 and Spearman ρ = 1.00 for two of the four panels (D_ang vs ΔAvg and D_ang vs ΔR@1), and r = 0.99 / ρ = 1.00 for the remaining two. These values are annotated on the figure and stated in the caption (lines 241–243). However, the figure caption on line 245 describes the plots as showing "realistic scatter," which directly contradicts a perfect linear correlation. A Pearson r of 1.00 across a sweep of diverse perturbations (certificate size, EMAs, invariance strength, whitening, pairing, LoRA capacity/LR, sketch type) is extraordinary and, combined with the "scatter" description, indicates a likely error in either the correlation computation, the annotation, or the data generation. Because this evidence is cited as the paper's key mechanistic validation that geometry drift *predicts* performance (line 269: "stability of the canonical subspace/spectrum reliably predicts downstream performance"), the suspicious coefficients weaken that specific claim. The core contributions — the method design and benchmark results — do not depend on the exact r values, but the figure must be corrected with properly computed correlations over a transparently described set of independent runs.

### Minor

- **Baseline implementation transparency.** The paper does not specify whether the baseline numbers in Tables 1–2 were obtained by re-running all methods under a unified codebase, backbone, and hyperparameter budget, or whether some were copied from original publications. In VL-CL, many of these methods use different CLIP variants and protocol details. While Pi-CCA's consistent margin across benchmarks partially mitigates this concern, a brief statement clarifying the source of each baseline number (re-run vs. reported) would strengthen the comparisons. This is standard practice and does not invalidate the results.

- **Prompt perturbation distribution undefined in main text.** The perturbation strength s is described as controlling "token-level synonym swap/back-translation/template jitter ratio" (line 259), but the distribution P and its parameterization are not defined in the main paper. The details are presumably in the stripped appendix (§A.2), but the stress test in §4.3 is difficult to interpret without at least a summary of how perturbations are generated.

- **CLAP4CLIP mentioned but absent from tables.** Line 211 lists CLAP4CLIP as a "replay/synthetic-replay reference" but it does not appear in any result table. GIFT (the other replay reference) does appear in Table 2. The paper should either include CLAP4CLIP numbers or clarify why it is mentioned but not reported.

### Trivial

- **No variance estimates for classification results.** Table 1 reports MTIL and X-TAIL results as single numbers without standard deviations, while Table 2 (VLCL, ConStruct-VL) includes ±std. Reporting variance across seeds for the primary classification benchmarks would be consistent.

## Nice-to-Haves

- A brief limitations paragraph discussing when the certificate might be insufficient (e.g., when k is too small to capture alignment, or when the anchor prompt set is not representative of future tasks) would add nuance.
- A concise algorithmic summary in the main text (beyond the reference to Algorithm 1 in the appendix) would help readers understand the training loop without consulting supplementary material.

## Removed Points

These points were flagged by reviewers but are not valid weaknesses. Treat them with caution.

- **"Unsubstantiated state-of-the-art claims due to uncontrolled baseline comparisons" (Harsh Critic, point 1):** The harsh critic framed the lack of baseline re-running transparency as an *evidential gap* that makes results untrustworthy. While improved transparency would be good (retained as Minor above), the claim that this "undermines the headline claims" overstates the problem. The paper evaluates on standard benchmarks using standard protocols, compares against a broad set of recent methods, and reports consistent margins — this is typical practice in the field. The SOTA claim is adequately supported by the numbers as reported. Demoted from fatal to minor.

- **"Framing as directly controlling alignment geometry could equally be viewed as a proxy" (Harsh Critic, §-by-§ notes):** This is a philosophical point about terminology, not a substantive weakness. The paper explicitly acknowledges that the sketched Frobenius distance is a "surrogate" (line 122). Removed.

- **"The use of random orthonormal sketches… would benefit from a clearer justification" (Harsh Critic):** The paper provides empirical justification in Table 3 (Gaussian vs. SRHT sketches yield nearly identical results, within 0.2 pp). The near-isometric property of random projections is a standard result. Removed.

- **"Missing related works" (Harsh Critic):** Not verifiable without external sources. Removed per instructions.

- **"Reproducibility commitment unusual" (Harsh Critic):** The paper explains its situation honestly. The absence of code during review is not a weakness of the research itself. Removed.

## Novel Insights

Beyond the paper's own contributions, the review process highlights an important methodological point: correlation analyses in ML papers that sweep hyperparameter configurations must be treated with the same rigor as other experiments. When every data point is a different model configuration (rather than an independent run), the number of points can be small and correlations can appear artificially perfect. Authors should report the number of data points, how they were generated, and avoid rounding artifacts that create implausible-looking r=1.00 values — even when the underlying relationship is genuinely strong.

## Suggestions

- **Fix Figure 3 immediately.** Recompute correlations with proper precision (e.g., 3 decimal places), explicitly state the number of data points and how each was generated, and ensure the text ("realistic scatter") matches the reported coefficients. If the data includes only a small number of points, report that transparently.
- **Add a one-sentence note in §4.1** clarifying the source of each baseline number (e.g., "All baseline numbers are from the original publications, except X, Y, Z which we re-ran under our protocol" or vice versa).
- **Include a brief definition of P and s** in the main text for the prompt perturbation stress test, even if full details remain in the appendix.
- **Add ±std to Table 1** for consistency with Table 2.

## Score and Decision

### Calibration Summary

| Anchor | Score | Round | Comparison to Pi-CCA |
|--------|-------|-------|----------------------|
| JIlIYIHMuv (LVLM-CL) | 2.50 | R1 | Substantially weaker; rejected |
| gNoqEdT2wO (MCIL benchmark) | 2.33 | R1 | Benchmark-only, weak methodology |
| TxIrMD6lAN (Incremental adapters) | 3.00 | R1 | Narrower scope, weaker results |
| G9Ea7mlqGO (CLIP online CL) | 3.80 | R1 | Less comprehensive, weaker |
| EKfcngSxwD (Task codebook VLMs) | 4.67 | R1 | Less principled, weaker results |
| 9aZ2ixiYGd (VL synergy CL) | 5.00 | R1 | Different approach, smaller scale |
| k9NYnsC4Mq (PROOF) | 5.67 | R1 | Related but weaker methodology; rejected |
| TLADT8Wrhn (TiC-CLIP) | 6.25 | R2 | Benchmark paper, different focus; Pi-CCA has stronger method contribution |
| sb7qHFYwBc (C-CLIP) | 6.50 | R2 | **Directly comparable.** Pi-CCA outperforms it on shared benchmarks, has broader evaluation, and a more principled approach, but has the Figure 3 correlation issue. Pi-CCA is comparable or slightly better. |
| V6uxd8MEqw (MISA) | 6.50 | R2 | Prompt-based GCL, different setting |
| 9bLdbp46Q1 (Adaptive retention) | 6.50 | R2 | Classification-only CL, narrower |
| b20VK2GnSs (Concept drift MLLM) | 7.00 | R2 | Similar quality level; Pi-CCA has cleaner method design |
| ftGnpZrW7P (GRAM) | 7.00 | R2 | Similar quality; both propose geometry-aware alignment |
| 7D9X2cFnt1 (EFCIL) | 7.00 | R2 | Different CL setting (exemplar-free CIL) |
| gc8QAQfXv6 (Function vectors) | 9.00 | R1 | Clearly stronger; different domain |
| WyEdX2R4er (Visual data-type) | 8.00 | R1 | Analysis paper, different topic |

**Round 1 bracket:** 5.5 – 8.0, based on the paper being clearly above the weak rejected papers (2.0–3.8) and below the 8.0+ analysis/modeling papers.

**Round 2 narrowing:** The paper lands between C-CLIP (6.50) and the 7.00 cluster (GRAM, Concept Drift MLLM). It is stronger than C-CLIP in methodology, evaluation breadth, and results, and comparable to the 7.00 papers in contribution quality. The Figure 3 correlation issue prevents it from exceeding the 7.00 cluster.

**Final score: 7.0.** The paper makes a clear, well-supported contribution with a novel geometry-first approach to VL continual learning, validated across four benchmarks with thorough analysis. The correlation anomaly in Figure 3 is a genuine but addressable presentation issue that does not undermine the core method or main benchmark results.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>