Now I have a thorough understanding of the paper and have verified each reviewer claim. Let me construct the final review.

---

## Summary

This paper proposes ARB-LLM, a family of post-training binarization (PTQ) methods for LLMs built on an alternating refinement of binarization parameters (mean μ, scaling factor α, binary matrix B) to iteratively reduce quantization error. Two extensions incorporate calibration data (ARB-X) and row-column scaling (ARB-RC), and a refined column-group bitmap (CGB) improves weight partitioning. The method achieves large perplexity reductions over the prior SOTA (BiLLM) across OPT, LLaMA, and Vicuna families while maintaining comparable or lower memory requirements.

## Strengths

1. **Novel alternating refinement framework with strong motivation.** The core idea—iteratively updating μ, α, and B via closed-form optimal solutions under the quantization error L₁—is well-motivated by the observed distribution shift between binarized and full-precision weights (Fig. 2). The pseudocode (Algorithm 1) and the closed-form derivations in Section 3.1 are clearly presented.

2. **Large and consistent improvements over SOTA binary PTQ.** ARB-LLM_RC reduces perplexity by 50–75% over BiLLM across OPT (Table 1), LLaMA-1/2/3 (Table 2), and Vicuna (Table 3), often at the *same* or *lower* bit-width and memory footprint (e.g., 2.83 GB vs. 2.93 GB for LLaMA-7B). These gains are substantial and hold across model families and scales.

3. **Practical speedup via reformulation for calibration data integration.** Theorem 2 quantifies a ~389× speedup (with typical hyperparameters) from compressing the calibration tensor X into a 2D matrix S and precomputing it, making ARB-X computationally tractable. This is a concrete algorithmic contribution.

4. **Component-wise ablation validation.** The ablation study (Table 4) systematically demonstrates the contribution of each component: CGB contributes 4.48 perplexity points to ARB-LLM_X, row-column scaling contributes 8.64 points over vanilla ARB, and even one iteration of ARB already significantly beats BiLLM. The decoupling study (Table 4c) shows that both column and group bitmaps are necessary.

5. **Memory efficiency.** ARB-LLM_RC (with or without CGB) uses *less* memory than BiLLM (2.63 GB vs. 2.93 GB for LLaMA-7B without CGB), while ARB-LLM_X uses the same memory as BiLLM but with much better performance.

## Weaknesses

### Fatal
None.

### Major

- **Abstract overclaims the "surpass FP16" result.** The abstract (line 6) states "our ARB-LLM_RC is the first to surpass FP16 models of the same size" without any qualification. The introduction (line 53) correctly scopes this claim to "zero-shot QA datasets," and the conclusion does not repeat the overclaim. However, the abstract is the most widely read part of the paper and will mislead readers who do not check the body. The perplexity results (Tables 2–4) show ARB-LLM_RC remains far above FP16 on language modeling; the "surpass FP16" claim only holds on a specific evaluation axis (zero-shot QA accuracy) and for certain model families. The authors should either add the qualification to the abstract or remove the unqualified statement.

### Minor

- **Ablation does not fully isolate the basic ARB alternating refinement.** The caption of Table 4(a) states "all ARB methods are equipped with CGB except for ablation (b)." This means the "ARB" row (22.67 perplexity) includes CGB, so the reader cannot see the effect of the alternating refinement alone (without CGB). While the paper does show ARB-LLM_X without CGB (26.29) in Table 4(b), that variant includes the calibration data update, which also confounds interpretation. A pure ablation of basic ARB (alternating refinement, no CGB, no calibration data, no row-column scaling) vs. BiLLM would cleanly demonstrate the standalone value of the iterative refinement scheme. This does not weaken the paper's conclusions—the improvements are clearly large—but it leaves a methodological gap in the ablation.

- **QA accuracy evidence is presented only as aggregated averages.** Figure 6 shows average accuracy over 7 QA datasets, which is helpful as a high-level summary but does not allow the reader to assess whether the "surpass FP16" result is consistent across individual tasks or driven by a few datasets. Per-dataset results would strengthen the claim substantially. (The paper notes "More results are provided in the supplementary file"; this point is about what appears in the main text.)

### Trivial
None.

## Nice-to-Haves

- A brief study on sensitivity to the *choice* of calibration dataset (e.g., using WikiText-2 instead of C4) would strengthen robustness claims.
- Confidence intervals or standard deviations for the QA accuracy results would help the reader assess variability, though single-run evaluation is standard practice in this line of work.
- The paper acknowledges that ARB-X cannot update B due to its discrete nature (line 221); a brief discussion of potential relaxations or alternatives would be helpful context.

## Removed Points

*These points were flagged in the reviewer inputs but are removed under the filtering rules; treat with caution if reading the raw reviews.*

- **Theorem 1 proof concern.** The harsh critic questions whether the inequality in Theorem 1 is guaranteed to hold. The paper states the proof is in the supplementary file (line 116). Per hard rules, criticisms about missing appendix/supplementary proof content are removed since the parser strips these sections from all papers.
- **"One model family" claim for Fig 6.** The harsh critic states the QA evidence covers "one model family" (LLaMA). This is factually incorrect: Fig 6 (labeled "llama-acc") covers LLaMA-1, LLaMA-2, and LLaMA-3 (three families), and the teaser (Fig 1) covers OPT. The evidence spans at least two model families.
- **Per-dataset breakdown criticism.** The paper says "More results are provided in the supplementary file" (line 402). The breakdowns exist in the full submission.
- **Formatting/style nitpicks** about table alignment and presentation.
- **Missing related works** (hard rule: cannot verify without external sources).
- **Variance/confidence intervals for perplexity** (deterministic given model + calibration set; not standard for this metric).
- **Sensitivity to calibration data choice** (moved to Nice-to-Haves).
- **Criticism about missing pseudocode** for ARB-X and ARB-RC (deferred to appendix, which is stripped by parser).
- **OneBit/BinaryMoS comparison clarity** (the paper clearly distinguishes QAT vs. PTQ in Section 2; the mention of these methods in the binarization subsection is appropriate context).

## Novel Insights

The harsh critic's suggestion to isolate the pure ARB effect is a standard methodological check that the ablation study partially anticipates but does not fully deliver. The strength finder correctly identifies that the alternating refinement framework provides a formal theoretical grounding (Theorem 1) absent in prior binary LLM methods, even if the proof is deferred to supplementary. The tension between the abstract's sweeping "surpass FP16" claim and the body's narrower "on zero-shot QA datasets" qualification is a real presentation issue that will affect how readers perceive the contribution. Beyond these, no genuinely novel insight emerges from the reviews that is not already present in the paper's own analysis.

## Suggestions

1. **Fix the abstract overclaim.** Replace "surpass FP16 models of the same size" with "surpass same-size FP16 models on zero-shot QA datasets" to match the qualified language already used in the introduction (line 53).
2. **Add a pure-ARB ablation row.** Include a configuration: ARB (alternating refinement) without CGB, without calibration update, and without row-column scaling, compared directly to BiLLM. This would definitively attribute the gain to the iterative refinement itself.
3. **Provide per-dataset QA results.** Either in the main text or as a supplementary table explicitly referenced in the main text, show the accuracy on each of the 7 QA datasets individually for the key comparison (ARB-LLM_RC vs. FP16) so readers can assess consistency.

## Score and Decision

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>