Now I have sufficient calibration data. Let me construct the final review.

## Calibration Round 1 — Bracketing

**Query 1 (weak anchors, score < 3.5):** "learned image compression Mamba state-space model" → MambaVC (3.00–3.40)  
**Query 2 (middle anchors, 3.5–7.5):** "learned image compression content-adaptive state-space model" → MambaVC (4.80), Zero-shot diffusion (4.25), LLM lossless (5.67), SSM layers (6.75)  
**Query 3 (strong anchors, >7.5):** "learned image compression content-adaptive token permutation Mamba" → Diffusion compression (8.00), Vision-RWKV (8.00)

**Round 1 bracket:** 5.0 – 7.0. The paper is clearly above MambaVC (4.80) due to genuine compression-specific innovations, but below strong theoretical contributions at 7+.

## Calibration Round 2 — Narrowing

**Query 1 (4.5–6.0):** "learned image compression Mamba content-adaptive" → MambaVC (4.80), Vision-Language Mamba (4.60), MambaMatcher (5.50), Autoregressive Mamba (5.75)  
**Query 2 (6.0–7.5):** "learned image compression rate-distortion Mamba ablation" → MambaQuant (6.25), Lattice Transform Coding (7.20), Mamba original (6.25), Point cloud Mamba (6.20)

**Comparison to anchors:**
- vs MambaVC (4.80, rejected): This paper has substantially more novelty — two compression-specific mechanisms (CTP, GPP) vs applying a stock VSS block. The ablation study and ERF analysis are much stronger. **This paper is clearly better.**
- vs Autoregressive Mamba in Vision (5.75, accepted): Similar-level novelty (applying AR pretraining vs applying CTP/GPP). The AR pretraining paper was criticized for limited novelty ("AIM but with Mamba"). This paper's CTP and GPP are more specifically tailored to the compression problem. **This paper is comparable to slightly stronger.**
- vs MambaQuant (6.25, accepted): MambaQuant addresses quantization of Mamba models with technically deep contributions. This paper's contributions are more architectural. **Comparable strength, different domains.**
- vs Lattice Transform Coding (7.20, accepted): Stronger theoretical contribution. **This paper is weaker than this anchor.**

**Final score: 6.0.** The paper sits above 5.75 (AR pretraining) in terms of compression-specific innovation and below 7.20 (lattice transform coding) in theoretical depth. It is clearly stronger than MambaVC (4.80) and comparable to accepted papers in the 6.0–6.25 range.

Now I'll write the review.

---

## Summary

This paper introduces Content-Aware Mamba (CAM) for learned image compression, addressing two specific limitations of vanilla Mamba when applied to images: (1) the rigid, content-agnostic raster scan order, and (2) the strict causality of the SSM which prevents access to global context. The authors propose **Content-Adaptive Token Permutation (CTP)** — clustering tokens by feature similarity and permuting the scan sequence so that content-correlated tokens are processed contiguously — and **Global-Prior Prompting (GPP)** — injecting sample-specific prompts derived from cluster centroids to relax the causal constraint. Built into the CMiC model, these components collectively achieve strong RD performance on Kodak, Tecnick, and CLIC datasets.

## Strengths

1. **Two clearly motivated, well-validated architectural innovations.** CTP and GPP directly target known limitations of Mamba for image compression (content-agnostic scanning and strict causality). The ablation study (Table 2) cleanly isolates each component's contribution: CTP alone yields 1.8–2.4% BD-rate improvement, GPP alone yields 0.5–1.4%, and together they achieve 2.7–3.6% total gain over the vanilla Mamba baseline. This level of decomposition is strong evidence that both mechanisms matter.

2. **Compelling ERF analysis validates the design rationale.** Figure 9 is particularly effective: it shows that a single Mamba layer with neither CTP nor GPP has a strictly causal ERF (zero activation beyond the raster-scan midpoint), GPP alone extends ERF beyond the causal barrier, and CTP reshapes activations toward semantically related regions. Figures 7–8 further show that CMiC's ERF is both more global and more content-adaptive than competing methods.

3. **Competitive RD performance with favorable efficiency.** CMiC achieves strong BD-rate savings across three datasets (−15.91% Kodak, −21.34% Tecnick, −17.58% CLIC vs VTM-21.0) while using only 69.11M parameters, 2.39 TFLOPs, and 0.405s decoding latency — substantially more efficient than MambaIC (157.09M, 5.56 TFLOPs, 0.669s) and competitive with transformer-based models. The minimal overhead from the clustering mechanism (5% training time increase, 4% decoding latency increase) demonstrates practical viability.

## Weaknesses

### Fatal
None.

### Major

1. **The "state-of-the-art" claim is not uniformly supported by the data in Table 1.** CMiC achieves −15.91% BD-rate on Kodak, which is *worse* than the reported MLICv2 number (−16.16%). While CMiC outperforms MLICv2 on Tecnick (−21.34 vs −20.13) and CLIC (−17.58 vs −15.79), the unqualified "SOTA" headline in the abstract and conclusion overstates the result. The paper would be stronger with a more precise claim such as "competitive with or exceeding recent SOTA LIC methods while being substantially more efficient than prior Mamba-based models."

2. **The uncontrolled inter-model comparison limits what can be concluded from Table 1.** BD-rate numbers for competing methods are drawn from their original papers without controlling for training data, training schedule, or hyperparameter budgets. This is standard practice in the LIC literature and does not invalidate the method, but it means the reader cannot attribute the absolute performance gap specifically to CAM rather than to differences in training setup. The *within-framework* ablation (Table 2) and the structural comparison (Table 4) are the proper evidence for the method's effectiveness, and they are convincing — the uncontrolled comparison should be de-emphasized relative to these.

3. **No statistical uncertainty quantification for BD-rate estimates.** Kodak has only 24 images, Tecnick ~100, and CLIC ~61. The reported BD-rate figures are point estimates without confidence intervals, bootstrapped bounds, or significance tests. Given the small sample size of Kodak, the ~0.25% gap between CMiC and MLICv2 could easily lie within sampling noise. While this is standard practice in the LIC community, the paper's central comparative claim would be materially strengthened by reporting, e.g., 95% bootstrap confidence intervals for the main BD-rate numbers.

### Minor

1. **Throughput is only reported at 256×256 with batch size 8 (Table 3).** For practical deployment, the clustering overhead (K-Means assignment, permutation) at full 2K evaluation resolution would be more informative, especially since Table 1 already provides decoding latency at 2K.

2. **Codebook initialization is fragile to the first batch's representativeness.** Centroids are initialized by partitioning the first training batch into K segments and averaging each segment. The paper notes that EMA updates mitigate drift over time, but there is no empirical check (e.g., varying random seeds or batch ordering) confirming that the initialization does not materially affect final performance.

### Trivial
None.

## Nice-to-Haves

- A controlled re-training experiment (e.g., retrain MambaIC within the CMiC training pipeline, or a simplified transformer baseline) would directly quantify CAM's contribution on a level playing field.
- Reporting training wall-clock time to convergence would be more informative than the per-step 5% overhead figure.
- A brief discussion of failure cases (e.g., uniform textures, low-contrast regions where clustering might be degenerate) would add depth.

## Removed Points

These points were flagged by reviewers but are removed with justification:

- **"Significantly" in Figure 1 caption** (Harsh Critic): The caption uses "significantly outperforms." While the difference in Figure 1(c) is visually clear, the reviewer objects to the word. Given the consistent margin shown in the RD curves and the ablation, this is a minor wording preference — not a substantive weakness. Removed as a style nitpick.

- **Hybrid training / gradient conflict between K-Means centroids and learned projection $\mathcal{A}$** (Harsh Critic): The paper explicitly notes that centroids are updated via non-gradient EMA while $\mathcal{A}$ is trained end-to-end. This is a common design pattern (VQ-VAE uses the same approach) and is well-understood to work in practice. The criticism is speculative without evidence of actual gradient conflict. Removed as a strawman.

- **Missing appendix details / proofs** (Harsh Critic): The parser strips appendix content from all submissions. These exist in the original. Removed per hard rule.

- **"Not yet released" / reproducibility concerns about code** (Harsh Critic's subtext): The paper states "Code will be released" with a GitHub link. Hard rule: do not question existence/release status of cited resources. Removed.

- **Various formatting and typos** (various): Parser artifacts, not author errors. Removed per hard rule.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Qualify the SOTA claim.** Replace "state-of-the-art" in the abstract and conclusion with a more precise statement, e.g., "competitive with leading LIC methods while significantly outperforming prior Mamba-based approaches," and note in Section 4.3 that CMiC slightly trails MLICv2 on Kodak while exceeding it on other datasets.

2. **Add bootstrap confidence intervals for BD-rate.** Report 95% confidence intervals for the main BD-rate figures (at least on Kodak, the smallest test set). This is straightforward and would substantially strengthen the evidence for all comparative claims.

3. **Report throughput at 2K evaluation resolution.** Provide inference throughput or latency breakdown at the native 2K resolution where decoding latency is already reported, to characterize whether clustering overhead scales unfavorably.

## Score and Decision

**Round 1 bracket (explicit):** 5.0 – 7.0. The paper is clearly above MambaVC (4.80, rejected) in novelty and compression-specific contribution, but below strong theoretical contributions like Lattice Transform Coding (7.20, accepted).

**Round 2 anchors (full list):**
- `KgJwbsfN7G` (MambaVC, 4.80, Reject) — Simply applies VSS blocks without compression-specific innovations. CMiC is substantially more novel.
- `0A6f1b66pE` (Vision-Language Mamba, 4.60, Reject) — Different domain. Less relevant.
- `GmE8ovvXaJ` (MambaMatcher, 5.50, Reject) — Semantic correspondence, different task.
- `PQpvhUrA1C` (Autoregressive Mamba, 5.75, Accept) — AR pretraining for Mamba vision; comparable novelty level.
- `KI45uDnmzv` (MambaQuant, 6.25, Accept) — Quantization of Mamba; comparable domain relevance.
- `Tv36j85SqR` (Lattice Transform Coding, 7.20, Accept) — Stronger theoretical contribution. CMiC is weaker.
- `AL1fq05o7H` (Mamba original, 6.25, Reject) — Foundational work, different standards.
- `E1ML0nEReb` (Point Cloud Mamba, 6.20, Reject) — Different task.

**Narrowing:** The paper is stronger than Autoregressive Mamba in Vision (5.75) — that paper was criticized for being "AIM but with Mamba," whereas CTP and GPP are specifically designed for the compression problem with supporting ERF analysis. It is comparable to MambaQuant (6.25) in terms of technical contribution depth. It is weaker than Lattice Transform Coding (7.20) which has stronger theoretical foundations.

**Final score:** 6.0. The paper makes two specific, well-motivated, and well-validated architectural contributions to a practical problem. The main weaknesses (overclaimed SOTA headline, absence of confidence intervals) are addressable and do not undermine the core mechanistic contributions validated by the ablation study and ERF analysis.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>