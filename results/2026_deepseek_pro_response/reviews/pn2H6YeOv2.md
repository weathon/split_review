Now I have all the information I need. Let me write the final review.

---

## Summary
PI-CCA proposes a replay-free continual learning method for vision-language models that preserves cross-modal alignment by directly constraining the canonical correlation spectrum and subspaces of the whitened image-text cross-covariance matrix. Instead of regularizing proxy signals (similarities, logits, parameters) as prior work does, it stores a compact certificate of alignment invariants (top-k canonical correlations and sketched subspaces) and enforces spectral and subspace-angle consistency during adaptation using only mini-batch statistics. The method achieves state-of-the-art results among replay-free methods across four VL-CL benchmarks (MTIL, X-TAIL, VLCL, ConStruct-VL).

## Strengths
- **Novel conceptual reframing**: The paper recasts forgetting in VL-CL as alignment-geometry drift rather than proxy-signal mismatch, directly targeting the whitened cross-covariance structure that underlies CLIP-style zero-shot generalization. This is mathematically well-motivated and distinguishes the approach from prior work (ZSCL, Mod-X, C-CLIP) that regularizes derived quantities.
- **Compact, replay-free certificate design**: The certificate stores only ρ*_{1:k} ∈ ℝ^k plus two sketch matrices S_v*, S̄_t* ∈ ℝ^{h×k}, requiring constant memory with no replay buffer, generative model, or reference corpus. The Pareto analysis (Fig. 2) empirically validates that (k, h) = (64, 256) sits near the efficient frontier, and Table 2 shows PI-CCA surpasses the synthetic-replay method GIFT without storing or generating any data.
- **Strong empirical results across diverse benchmarks**: Tables 1–2 show PI-CCA achieving top performance among replay-free methods on MTIL (Avg: 76.8), X-TAIL (Avg: 68.1), VLCL retrieval (I2T R@1: 48.6), and ConStruct-VL (FA: 75.2, AF: 2.7), consistently ranking first across all four tracks.
- **Thorough ablation study**: Table 3 systematically isolates each component (spectral term, subspace term, prompt invariance, certificate EMA, covariance EMA, spectral moments, Hungarian pairing, sketch type), with removing spectral or subspace terms causing the largest drops (2.2–2.7 points), confirming both are necessary.
- **Prompt-invariance mechanism with convincing stress test**: The projector-averaging approach (Eq. 5–6, Eq. 11) handles sign/rotation ambiguity gracefully, and Fig. 4 demonstrates that the invariance loss substantially flattens degradation under increasing prompt perturbation strength, improving R@1 by +2.4 to +2.5 points at s=1.0.

## Weaknesses

### Fatal
None.

### Major
- **Structurally circular geometry–performance correlation analysis**: Figure 3 sweeps only Pi-CCA hyperparameter configurations (certificate size, EMAs, invariance strength, whitening, pairing, LoRA capacity/LR, sketch type). Both the geometry drift metrics (D_ang, D_ρ) and the performance drops (ΔAvg, ΔR@1) are measured relative to a single Pi-CCA configuration, meaning both quantities are consequences of the same underlying perturbation. The near-perfect correlation (Pearson r=1.00, Spearman ρ=1.00) therefore demonstrates that badly-configured Pi-CCA variants perform poorly by both geometry and accuracy metrics — not that geometry drift is a general predictor of forgetting across methods. The conclusion's claim that "stability of the canonical subspace/spectrum reliably predicts downstream performance" (line 256) overstates what this evidence supports. This weakens the paper's third claimed contribution and the conceptual takeaway.
- **Central causal claim is untested**: The paper's motivation (lines 21–22) argues that proxy-based methods (ZSCL, C-CLIP, Mod-X, etc.) fail because they "permit slow drift of the alignment geometry that drives zero-shot performance." Yet the paper never measures CCA geometry drift for any baseline method. Without evidence that baselines exhibit larger geometry drift — and that this drift, rather than some other factor, explains their performance gap — the reframing of forgetting as alignment-geometry drift remains a hypothesis rather than a demonstrated insight. The method works empirically, but the paper does not demonstrate it works for the reason claimed.

### Minor
- **Certificate construction under-specified**: The initial Pi-CCA certificate is described as "constructed from a diverse anchor prompt set" (line 89) and "pre-continual" (line 71), but the paper never specifies what data, how many samples, or from which distribution. This affects reproducibility and the reader's ability to assess whether the certificate captures appropriate alignment structure for downstream continual learning domains.
- **Table 1 lacks standard deviations**: The primary classification results (MTIL, X-TAIL) report scores without any measure of variance. Margins over strong baselines like C-CLIP are 1–2 points (e.g., 76.8 vs. 75.2 on MTIL Avg). Table 2 does include ± values, suggesting the data exists, and the task-order analysis (Fig. 5) with narrow IQRs partially mitigates this concern, but reporting variance for the main results table is standard practice.

### Trivial
- **Typo in Eq. 12** (line 129): The expression for M^{(t)} reads "(∑_{v=1}^t S_v^{(t)})^{-1/2} (∑_{v=1}^t S_v^{(t)})^{-1/2}" — both factors use S_v, while one should presumably be Σ_{tt} (the text covariance factor).

## Nice-to-Haves
- Adding baseline points (ZSCL, C-CLIP, Mod-X) to the Pareto analysis (Fig. 2) would let readers assess whether PI-CCA's memory/time/accuracy tradeoff is competitive in absolute terms rather than only internally.
- An analysis of streaming CCA estimate quality (effect of EMA rate β, batch size, and ridge γ on estimate stability) would strengthen the methodological contribution given that the approach relies on these estimates for its regularization.
- Clarifying the exact gradient flow (which quantities receive gradients from which loss terms, and whether stop-gradient is applied by default) would improve reproducibility.

## Removed Points
These points are flagged to be removed, treat them with caution:
- *Harsh critic: "r=1.00 is suspiciously perfect — diverse perturbation types would not collapse to a perfect linear relationship."* → REMOVED. This is speculation about data integrity without evidence. The paper reports r=1.00; we evaluate what that evidence means, not whether it was fabricated.
- *Harsh critic: "Streaming CCA reliability — CCA requires well-estimated covariance matrices and EMA mixing across tasks with different distributions may not produce meaningful estimates."* → REMOVED as a standalone weakness. This is a theoretical area-of-concern sweep. The paper includes ridge regularization and the empirical results demonstrate practical effectiveness. Moved to Nice-to-Haves as a suggested analysis.
- *Harsh critic: "The Pareto analysis (Fig. 2) sweeps k and h for Pi-CCA only — without baseline points the reader cannot assess competitive tradeoffs."* → REMOVED as a weakness. Fig. 2 is explicitly a certificate-capacity analysis, not a method-comparison plot. Added to Nice-to-Haves.
- *Harsh critic: "No discussion of whether prior methods have considered CCA or canonical correlation preservation in continual learning."* → REMOVED. This is a related-work coverage nitpick; the paper adequately distinguishes from Mod-X and other geometry-aware work.
- *Harsh critic: "Code will not be released during review, citing commercial use — this is a legitimate concern for independent verification."* → REMOVED per hard rule: do not criticize code/model availability.
- *Harsh critic: "Gradient flow ambiguity — the paper mentions stop-gradient 'if needed' without specifying the default."* → REMOVED as a standalone weakness. This is a minor implementation detail deferred to the appendix.
- *Strength Finder: "Evidence linking geometry preservation to downstream performance, validating the central claim — Fig. 3 shows strong correlation."* → RETAINED but with qualification; the correlation exists within Pi-CCA but the interpretation as general validation of the central claim is undermined by the circularity concern.

## Novel Insights
The paper makes an interesting observation that within the Pi-CCA framework, sorted pairing of canonical correlations (Eq. 8) performs nearly identically to exact Hungarian matching (Table 3: 76.8 vs. 76.7), suggesting that for continual learning of VLMs, spectral preservation does not require the full permutation-invariant matching that CCA-based methods typically demand. This is a practical insight with implications for efficient implementation.

## Suggestions
- The highest-impact improvement would be to measure CCA geometry drift (D_ang, D_ρ) for 2–3 baseline methods (e.g., ZSCL, C-CLIP, Mod-X) on the same benchmarks. If baselines show larger drift correlated with their performance gaps, this would convert the paper's central hypothesis from an untested claim into a demonstrated insight and make Fig. 3 far more compelling.
- Specify the initial certificate construction: what anchor prompts/templates, how many image-text pairs, and justify the choice for the downstream domains.
- Report standard deviations (or confidence intervals across seeds) for Table 1.
- Fix the Eq. 12 typo so both covariance factors are distinct.

---

**Anchor comparison**:

| Anchor | Score | Round | Comparison |
|---|---|---|---|
| C-CLIP (sb7qHFYwBc) | 6.50 | R1/R2 | Directly comparable VL-CL method; PI-CCA has more principled geometry-first methodology, broader benchmark coverage, and more thorough ablation |
| PROOF (k9NYnsC4Mq) | 5.67 | R1/R2 | VL-CL method; PI-CCA is clearly stronger in methodology, evaluation breadth, and ablation quality |
| TiC-CLIP (TLADT8Wrhn) | 6.25 | R2 | Benchmark paper with limited algorithmic contribution; PI-CCA has much stronger methodological novelty |
| Complementary Memory (wE1I9IGqeH) | 6.00 | R2 | Different CL approach; PI-CCA more comprehensive in evaluation |
| Concept Drift MLLM (b20VK2GnSs) | 7.00 | R2 | Different problem; similar experimental rigor but PI-CCA has cleaner presentation and stronger ablation |
| Budgeted Online CL (dOAkHmsjRX) | 7.50 | R2 | Strong clean contribution with fewer conceptual gaps; PI-CCA's circular analysis and untested causal claim pull it below this anchor |

**Bracket**: [6.0, 7.5] → narrowed to **7.0**. PI-CCA is clearly stronger than the 6.0–6.5 band (C-CLIP, TiC-CLIP) in methodology and evaluation breadth, but falls short of the 7.5 anchor (Budgeted Online CL) due to the circular correlation analysis and untested causal claim that weaken the conceptual contribution. The empirical results and ablation remain strong.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>