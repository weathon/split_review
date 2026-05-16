Now I have a comprehensive understanding of both the paper and the reviewer inputs. Let me produce the consolidated review.

## Summary

This paper introduces CADS (Condition-Annealed Diffusion Sampler), an inference-time technique that adds scheduled, monotonically decreasing Gaussian noise to the conditioning signal during diffusion model sampling. The method requires no retraining, works with any pretrained model and sampler, and demonstrably increases output diversity while maintaining quality across four conditional generation tasks (class-conditional ImageNet, pose-to-image, identity-conditioned face generation, and text-to-image). CADS achieves a new state-of-the-art FID of 1.70 (256×256) and 2.31 (512×512) on class-conditional ImageNet using only improved sampling on a pretrained DiT-XL/2 model.

## Strengths

- **Novel, simple, and effective method with no retraining required**: CADS introduces a well-motivated condition-annealing strategy — adding noise to the conditioning signal with a piecewise linear schedule — that can be plugged into any pretrained diffusion model. This is validated across four tasks (Table 1 in the paper) with consistent FID, Recall, MSS, and Vendi Score improvements, making it broadly applicable.

- **State-of-the-art FID on class-conditional ImageNet via inference-time modification alone**: Using a pretrained DiT-XL/2 model, CADS achieves FID of 1.70 (256×256) and 2.31 (512×512), surpassing the previous best MDT model that required retraining. This demonstrates that a purely inference-time sampling strategy can set new benchmarks.

- **Substantially alleviates the diversity-quality trade-off at high guidance scales**: Figure 5 (referenced in the paper) quantitatively shows that as CFG scale increases, CADS maintains significantly better FID and Recall compared to standard DDPM, with the gap widening at higher guidance values. This enables practitioners to use high guidance for quality without suffering catastrophic diversity loss.

- **Compatible with multiple samplers and outperforms Dynamic CFG**: Table 3 shows CADS improves FID and Recall when applied to DDPM, DDIM, and DPM-Solver++. Table 4 directly compares CADS (FID 9.47, Recall 0.62) to Dynamic CFG (FID 18.42, Recall 0.39), demonstrating that stochastic noise injection is substantially more effective than naive guidance modulation.

- **Preserves condition alignment while increasing diversity**: Table 5 shows nearly identical Top-1 accuracy (0.96 vs. 0.98), MPJPE (0.02 both), and CLIP score (0.31 both) compared to standard DDPM, confirming diversity gains do not come at the cost of fidelity.

- **Comprehensive ablation studies with practical guidelines**: Section 4.2 systematically examines noise scale \(s\), cutoff threshold \(\tau_1\), and rescaling factor \(\psi\) through multiple figures and tables, offering clear guidance on hyperparameter selection.

## Weaknesses

### Fatal
None.

### Major
None. No weakness in this set undermines the paper's core claims. The issues identified are presentation-level or standard for this class of work.

### Minor

- **SOTA FID claim lacks exact experimental conditions in the main text**: The paper reports SOTA FIDs of 1.70 and 2.31 but defers the exact guidance scale(s), sampling steps, and hyperparameter values (\(s\), \(\tau_1\), \(\tau_2\), \(\psi\)) used for these runs to the appendix. While the paper explains conceptually that "higher guidance values" are used and that \(s\) and \(\tau_1\) are adjusted accordingly, a reader cannot precisely reproduce the SOTA setup from the main text alone. For a headline result that surpasses a different architecture (MDT), the exact settings should be stated upfront rather than relegated to supplementary material.

- **No variance or confidence intervals reported for FID / Recall**: The paper states it uses "the exact same random seeds" for fair comparisons, but does not report any measure of variance (standard deviation, confidence intervals) across multiple runs of the same configuration. Given the stochastic nature of generative sampling, this makes it difficult to assess whether small improvements (e.g., FID 1.79 → 1.70) are systematic or within sampling noise. *Context*: This is not unique to this paper — it is standard practice in the diffusion literature — but a SOTA claim would be strengthened by reporting variance.

- **"Resolves a long-standing trade-off" overstates the contribution**: The introduction claims CADS "resolves a long-standing trade-off between diversity and quality," but the ablation study (Section 4.2) shows that too much noise degrades quality and too little does not help diversity — meaning the trade-off is *alleviated* but not resolved. The paper itself later uses the more measured phrasing "substantially alleviate this trade-off" in Section 4.1. The introduction should be consistent with this more accurate characterization.

- **The mixing factor \(\psi\) introduces an additional hyperparameter that must be tuned per task**: While the paper recommends \(\psi=1\) as a default and suggests decreasing it only if diversity is insufficient, the ablation shows \(\psi\) trades off FID versus Recall linearly (Figure 7). This means users must tune an extra parameter per task / guidance scale. This is acceptable for a practical method but should be acknowledged more clearly as a tuning burden.

### Trivial

- **Diversity metrics computation set**: The paper should clarify whether the MSS and Vendi Score are computed on the same set of generated samples used for FID or on a separate subset.

- **Limitation on dense spatial conditioning**: The conclusion mentions that CADS may not work for dense spatial conditioning (e.g., segmentation maps) but offers no conjecture about why. A brief explanation of the likely cause would strengthen the limitations discussion.

## Nice-to-Haves

- Compare against a baseline that adds the same noise to the condition at every step *without* annealing (unannealed version). This would directly test whether the annealing schedule is essential or whether any noise injection helps.
- Provide a practical heuristic for setting \(s\) and \(\tau_1\) as a function of the guidance scale \(w_{\text{CFG}}\) (e.g., \(s = a \cdot w_{\text{CFG}} + b\)), which would make the method easier to adopt without per-task tuning.
- Report FID with multiple seeds (even 3) to give a sense of stability for the headline SOTA numbers.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- *"A single seed is used for all comparisons"* — The paper states it uses "the exact same random seeds" (plural), which is ambiguous but does not assert "a single seed." The underlying concern about missing variance is retained as a Minor weakness above.
- *"The SOTA table is referenced but not included here — the reader must trust these tables. This is a limitation of the review process, not the paper per se."* — The reviewer acknowledges this is a parser limitation. The table exists in the original submission.
- *"The paper does not mention the exact guidance scale(s) used"* — Partially addressed: the paper states "higher guidance values" and explains the adjustment strategy. The criticism that exact numbers are deferred to the appendix is retained in Minor weaknesses.
- *Complaints about missing appendix content* — The appendix is stripped by the parser; it exists in the original submission.
- *Pure formatting/style nitpicks* — Removed per guidelines.

## Novel Insights

The reviews surface an interesting tension: the harsh critic's most credible concern is about evidential transparency for the SOTA claim (exact hyperparameters, variance), yet the same critic also acknowledges the paper's core contribution is solid and recommends acceptance. The strength finder correctly identifies that the paper's empirical breadth across four tasks is its strongest asset. The key insight from synthesizing both is that the paper would be significantly strengthened by a single concise table in the main text listing the exact settings (guidance scale, \(s\), \(\tau_1\), \(\tau_2\), sampling steps, number of seeds) for each SOTA run — this would preempt the main credible critique without requiring any additional experiments.

## Suggestions

1. Add a dedicated "SOTA Settings" table in the main text (not appendix) listing the exact guidance scale, \(s\), \(\tau_1\), \(\tau_2\), sampling algorithm, and number of sampling steps used for each ImageNet resolution's SOTA FID result.
2. Run each configuration with at least 3 different seeds and report mean ± std for FID and Recall, at least for the headline ImageNet 256×256 SOTA claim.
3. Soften "resolves" to "substantially alleviates" in the introduction to match the paper's own more careful language in the experimental sections.
4. Add a brief conjecture about why CADS may not extend to dense spatial conditioning (e.g., "spatial conditions are tightly coupled to spatial structure, so noise may break this coupling irreversibly, unlike class or text embeddings where noise merely blurs semantic content").
5. Clarify in the metrics description whether diversity metrics (MSS, Vendi Score) are computed on the same sample set as FID.

## Score and Decision

This is a solid method paper with a novel, simple, and well-validated idea. The core contribution — scheduled noise injection into the conditioning signal during inference — is clearly motivated, theoretically grounded, and empirically supported across diverse tasks. The weaknesses are presentation-level and addressable: the SOTA claim needs more transparent hyperparameter reporting, variance would strengthen confidence, and the introduction slightly overstates. None of these threaten the paper's central findings. I recommend acceptance.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>