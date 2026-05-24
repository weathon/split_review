Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper proposes PI-CCA, a replay-free continual learning method for vision-language models that preserves cross-modal alignment by directly constraining the canonical correlation spectrum and subspace (a "CCA certificate") rather than proxy signals like logits or similarities. The certificate is stored compactly via random orthonormal sketches, making memory constant regardless of past data volume. A prompt-invariance mechanism further stabilizes text-side representations under prompt perturbations. Across four benchmarks (MTIL, X-TAIL, VLCL, ConStruct-VL), PI-CCA achieves state-of-the-art results among replay-free methods, and ablations confirm that both spectral and subspace terms are necessary for the gains.

## Strengths

1. **Principled conceptual reframing of VL-CL forgetting.** The paper identifies that prior methods regularize proxy quantities (logits, similarities, parameters) rather than the cross-modal alignment geometry itself. Operating on the whitened cross-covariance's canonical spectrum and subspaces is a well-motivated first-principles alternative. This is clearly stated (§1): "We recast forgetting in VL-CL as alignment-geometry drift instead of matching proxy quantities."

2. **Replay-free, constant-memory consolidation.** The Pi-CCA certificate stores only sketched canonical subspaces via random orthonormal sketches with $h \ll d_v, d_t$, keeping memory independent of past data size. The certificate is explicitly defined (§3.2) as $(\rho_{1:k}^*, \mathbf{S}_v^*, \bar{\mathbf{S}}_t^*)$ with $\mathbf{S}_v^* \in \mathbb{R}^{h \times k}$. Figure 2 confirms a broad Pareto ridge where performance is stable, supporting the "small yet sufficient" hypothesis.

3. **SOTA empirical results across all four benchmarks without replay.** PI-CCA consistently outperforms all replay-free baselines, and on VLCL and ConStruct-VL it even surpasses GIFT, which uses synthetic replay (Tables 1–2). For example, MTIL Avg is **76.8** (vs. 75.2 for C-CLIP), VLCL I2T R@1 is **48.6** (vs. 47.3 for GIFT), and ConStruct-VL AF is **2.7** (vs. 3.3 for GIFT).

4. **Thorough component ablations.** Table 3 systematically removes each loss term. Removing the spectral term ($\lambda_1=0$) drops MTIL Avg by -2.5; removing the subspace term ($\lambda_2=0$) drops it by -2.2; disabling prompt invariance ($\lambda_3=0$) drops it by -1.5. The Hungarian pairing surrogate and SRHT sketch alternatives yield nearly identical results (76.7 and 76.6 vs. 76.8), confirming robustness to design choices.

5. **Low sensitivity to task ordering.** Figure 5 shows narrow interquartile ranges across 20 random MTIL orders (span ~1.4 p.p.), supporting that the method does not rely on a favorable task sequence.

6. **Prompt-invariance mechanism with stress-test validation.** The $\mathcal{L}_{\text{pi}}$ loss (§3.3, Eq. 11) demonstrably flattens the degradation slope under increasing perturbation strength (Figure 4). At $s=1.0$, it improves VLCL I2T R@1 by +2.44 p.p. (ID) and +2.51 p.p. (OOD) vs. the ablated variant.

## Weaknesses

### Minor

1. **Figure 3 correlation values are suspiciously perfect.** The paper reports Pearson $r=1.00$ and Spearman $\rho=1.00$ for two panels, and $r=0.99, \rho=1.00$ for the other two, across a sweep of multiple perturbation types. For real experimental data with heterogeneous perturbations (certificate size, EMA rates, invariance strength, whitening, pairing, LoRA capacity, sketch type), correlation coefficients this extreme are highly unusual and likely reflect rounding (e.g., $0.9998 \to 1.00$). The figure caption's mention of "95% confidence interval shaded area" suggests scatter exists, which is inconsistent with truly perfect correlation. The paper should report coefficients to sufficient precision (e.g., $r=0.998$) and acknowledge whether the drift and performance metrics are deterministically coupled by construction (both computed relative to the same reference configuration). This does **not** undermine the paper's core empirical claims (the SOTA results in Tables 1–2 are independent of this figure), but it weakens the "why it works" argument as presented. This is a reporting/analysis issue, not a fatal flaw.

2. **Missing efficiency comparison against baselines.** The paper provides its own certificate-capacity Pareto analysis (Figure 2) showing step time and peak memory for varying $k$ and $h$, but never compares step time, peak memory, or throughput against any of the competing methods (C-CLIP, ZSCL, Mod-X, etc.). Since the paper claims to be "simple, generator-free, constant-memory" and positions this as an advantage, the lack of comparative efficiency data makes it difficult to assess whether the performance gains come at a meaningful computational cost relative to baselines. This is a standard comparison to expect in a systems-oriented CL paper.

3. **No task-agnostic / class-incremental variant evaluated.** The paper uses task-incremental (MTIL, X-TAIL, VLCL, ConStruct-VL) settings where task boundaries are known. While X-TAIL is task-agnostic at test time, the model still trains with known task boundaries. Given that the certificate is described as "task-agnostic," evaluating on a strict class-incremental protocol (e.g., Split CIFAR-100 or ImageNet as a CLIP-based CIL benchmark) would broaden the contribution. This is a scope limitation rather than a flaw.

### Trivial

- The paper states it uses 20 random MTIL orders but does not report which 11 domains or give the order seeds for reproducibility (deferred to appendix, which is stripped from the extracted text).

## Nice-to-Haves

- A comparison of efficiency metrics (step time, peak memory, number of trainable parameters) against the main baselines (C-CLIP, Mod-X, ZSCL, etc.) would substantially strengthen the practical claims.
- Reporting correlation coefficients with more significant digits (e.g., $r=0.997$ rather than $1.00$) would avoid the appearance of over-claiming in Figure 3.

## Removed Points

- **Harsh critic's claim that the correlation issue is "critical evidential flaw" and "fatal."** This is overblown. The paper's core contribution (SOTA replay-free VL-CL via geometry preservation) is supported by Tables 1–2 and the ablation study (Table 3). Figure 3 is supporting/illustrative evidence for the mechanism, not the primary empirical claim. Even if the correlation values are rounded, the qualitative trend is clear and the main results stand independently.

- **Harsh critic's claim that the paper's "main argumentative thread is broken."** Disagreed. The central argument is that preserving alignment geometry via CCA certificates improves retention, which is demonstrated by SOTA results and ablations. The correlation figure is one piece of supporting evidence among several.

- **Strength finder's claim about "near-perfect linear correlation" as a top-tier strength.** Demoted from a core strength to a qualified observation. The correlation is clearly very high, but the reported values raise concerns about rounding/artifact that should be disclosed.

- **Generic/filler strengths from strength finder** (e.g., "agnostic to downstream task," "compatible with parameter-efficient tuning" — these are interesting properties but not demonstrated contributions beyond the standard use of LoRA).

## Novel Insights

None beyond the paper's own contributions. The key insight — that directly preserving CCA geometry (spectrum and subspaces) via a compact sketched certificate is an effective replay-free strategy for VL-CL — is the paper's own contribution, not something surfaced by the reviews.

## Suggestions

1. Report correlation coefficients in Figure 3 to at least 3 decimal places, and explicitly discuss whether the drift and performance-drop metrics are deterministically linked by construction (both differenced from the same reference configuration). If the relationship is truly that tight, a brief explanation of why (e.g., "the drift metric directly measures the quantity that Pi-CCA regularizes, so near-deterministic coupling is expected") would preempt concerns.

2. Add a simple efficiency comparison against baselines (e.g., a table with step time, peak memory, and trainable parameter count for each method). This is low-effort and would substantially strengthen the practical claims.

3. Consider evaluating on a strict class-incremental benchmark (e.g., ImageNet-based CIL with CLIP) to demonstrate task-agnostic certificate operation beyond the current protocols.

## Score and Decision

Round-1 bracketing placed the paper between 3.5–7.5, with weak anchors at ~2.3–3.0 (rejected papers with flawed methodology or weak results), middle anchors at 5.0–6.5 (C-CLIP at 6.5, Proof at 5.67, Vision-Language Synergy at 5.0), and strong anchors at 8.0+ (papers with breakthrough results or foundational contributions).  

**Initial bracket: 5.0–7.5** — the paper is clearly above the weak reject band (methodology is sound, results are strong) but not at the 8.0+ breakthrough level.

Round-2 narrowing used C-CLIP (6.50, Accept) as the primary anchor — the most directly comparable paper (same task, same backbones, overlapping baselines). PI-CCA outperforms C-CLIP on every benchmark (MTIL: +1.6, VLCL R@1: +2.5, ConStruct-VL AF: -1.2), has a more principled conceptual contribution, and provides more thorough ablations. However, it has the Figure 3 correlation concern and missing efficiency comparison — neither fatal but both real. Against the Proof paper (5.67, Reject), PI-CCA is substantially stronger in execution and evaluation breadth. Against the Spurious Correlations CL paper (6.25, Accept), PI-CCA has stronger empirical results but the correlation issue is a more salient concern than that paper's weaknesses.

**Final score: 6.5** — comparable to C-CLIP in overall quality, for different reasons. PI-CCA's conceptual contribution and benchmark results are stronger, but the Figure 3 correlation reporting and missing baseline efficiency comparison prevent it from clearly surpassing C-CLIP's score. The paper is a solid accept: the core method is novel, well-motivated, and convincingly supported by SOTA results across diverse benchmarks.

### Anchors consulted

| Path | Score | Round | Comparison to this paper |
|------|-------|-------|-------------------------|
| JIlIYIHMuv | 2.50 | R1 | Much weaker; flawed methodology and weak results |
| gNoqEdT2wO | 2.33 | R1 | Much weaker; benchmark-only contribution |
| WM5G2NWSYC | 2.00 | R1 | Much weaker; poor evaluation |
| A1JdcLawSu | 3.00 | R1 | Weaker; narrow scope |
| 9aZ2ixiYGd | 5.00 | R1 | Weaker; split reviews (8,6,3,3), less principled approach |
| k9NYnsC4Mq | 5.67 | R1 | Weaker; rejected over inference mismatch and lack of depth |
| G9Ea7mlqGO | 3.80 | R1 | Weaker; rejected with moderate scores |
| sb7qHFYwBc | 6.50 | R1/R2 | Comparable overall; C-CLIP has benchmark contribution but weaker results and less principled method |
| 3i13Gev2hV | 8.00 | R1 | Stronger; breakthrough-level VL contribution |
| WyEdX2R4er | 8.00 | R1 | Stronger; fundamentally different task |
| 1aF2D2CPHi | 8.00 | R1 | Stronger; different problem setting |
| gc8QAQfXv6 | 9.00 | R1 | Stronger; high-impact CF analysis |
| rwmwFnmjAX | 4.75 | R2 | Weaker; rejected with modest scores |
| G9qA1JZ0Sy | 5.33 | R2 | Weaker; rejected with moderate scores |
| OCpxDSn0G4 | 6.00 | R2 | Comparable; different domain (neural fields), similar quality |
| 3Y7r6xueJJ | 6.25 | R2 | Comparable; different CL subproblem, similar execution quality |

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>