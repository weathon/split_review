- Decision: Reject
- Avg Score: 2.00
- Scores: 3, 1, 1, 3
Now I have a thorough understanding of the paper and can verify each claim against the actual text. Let me compose the final consolidated review.

---

## Summary

This paper addresses the data imbalance problem in patch-based brain MRI super-resolution, where the cerebellum (small, detail-rich) is under-represented compared to the cerebrum (large, smooth). The authors propose a simple non-uniform patch sampling strategy that maintains a 50/50 distribution between whole-brain patches and cerebellum-dedicated patches. Experiments on the HCP dataset with two models (mDCSRN and mDCSRN-WGAN) show that this approach substantially improves cerebellum reconstruction quality (e.g., PSNR from 33.19→33.91 for mDCSRN) while preserving whole-brain performance. The method is architecture-agnostic, straightforward to implement, and requires no architectural changes.

## Strengths

- **Clear and measurable improvement on cerebellum reconstruction**: Tables 2 and 3 show consistent gains across PSNR, SSIM, and NRMSE for both mDCSRN and mDCSRN-WGAN when using the proposed non-uniform sampling, while whole-brain metrics remain essentially identical. The improvement is non-trivial (e.g., +0.72 PSNR for mDCSRN cerebellum, +0.52 for mDCSRN-WGAN).

- **Simple, architecture-agnostic method with practical value**: The approach is defined purely by the patch-sampling procedure (Section 3.2) and requires no modification to model architectures, loss functions, or inference pipelines. It is validated on two architecturally distinct families (CNN-based mDCSRN and GAN-based mDCSRN-WGAN), supporting the generality claim.

- **Evaluated under a more challenging degradation**: Using a scale factor of 4 (6.25% k-space) rather than the common factor of 2 (25% k-space), the paper tests models under substantially blurrier inputs. Table 1 confirms that models still achieve meaningful super-resolution (whole-brain PSNR >35 dB), extending the tested operating range beyond prior work.

- **Well-motivated and clearly communicated problem**: The paper identifies a concrete, overlooked issue — that uniform patch sampling systematically under-represents the cerebellum — and proposes an intuitive fix. The motivation is grounded in the observation that cerebrum reconstruction is already nearly indistinguishable from HR, while cerebellum reconstruction lags behind.

## Weaknesses

### Fatal
None.

### Major

- **No statistical significance reported (single run)**: Tables 2 and 3 report only point estimates without standard deviations, confidence intervals, or significance tests. With no indication of multiple runs, the reported improvements (e.g., PSNR 33.19→33.91) cannot be distinguished from variance due to random initialization, patch sampling, or optimizer noise. This is the most impactful gap — a straightforward fix with 3+ random seeds would substantially strengthen the paper's central claim.

- **No ablation of the sampling ratio**: The 50/50 split between whole-brain and cerebellum patches is presented as the method, but no experiment varies this proportion (e.g., 70/30, 30/70). Without this, it is unclear whether 50/50 is optimal, how sensitive the method is to this choice, or whether the improvement stems from balancing per se versus simply exposing the model to any additional cerebellum data. The paper acknowledges this in Section 6 ("more sophisticated sampling methods could be explored"), but the lack of characterization limits the contribution from a "proof of concept" to a properly understood method.

### Minor

- **Evaluation on a single dataset with two older architectures**: Only HCP T1-weighted data and two 2018-vintage models (mDCSRN and mDCSRN-WGAN) are tested. The paper claims the method is architecture-agnostic and not dataset-specific, but provides no evidence with more recent architectures (e.g., attention-based Zhang et al. 2021, transformer-based Li et al. 2022, both cited in the paper) or a second dataset with different contrast/resolution. The authors acknowledge this limitation in the discussion, which is fair, but the evaluation remains thin for the generality claimed in the contributions.

- **Unsubstantiated claim about real-world realism of scale factor 4**: The paper states that using a scale factor of 4 (6.25% k-space) makes LR images "more similar to real-world LR images" (Section 1) and "may improve model generalization ability on real-world images" (Contributions). No evidence or citation is provided that real-world low-field acquisitions correspond to this specific masking ratio. The choice is defensible as a harder stress test, but framing it as a realism claim without support weakens the contribution statement.

- **Inference pipeline not discussed**: The paper does not explicitly clarify that the method is a training-only modification and that at inference time the model processes whole volumes without requiring a cerebellum segmentation. This is implicitly clear from the method description but should be stated explicitly to avoid confusion.

### Trivial

- **Step 2 of the sampling procedure (Section 3.2) is slightly ambiguous**: "Generate patches from the whole brain volume and randomly select 50% of the generated patches" could be misread as discarding 50% of patches. Reading steps 2–4 together clarifies the intent, but the phrasing could be tightened.

- **FastSurfer error propagation not discussed**: The method uses FastSurfer segmentations of HR images to extract cerebellum masks, but does not discuss how segmentation errors could propagate to misaligned LR/HR patch pairs. A brief acknowledgement would suffice.

## Nice-to-Haves

- Repeat all experiments with 3 random seeds and report means ± standard deviations in Tables 2 and 3. This would directly address the most significant weakness.
- Ablate the sampling ratio (e.g., 30/70, 50/50, 70/30 cerebellum/whole-brain patches) to characterize sensitivity and optimality.
- Add results on a second dataset (e.g., IXI, ADNI) and at least one more recent architecture (e.g., attention-based or transformer-based).
- Compare against simpler alternatives: oversampling cerebellum patches within uniform sampling, or per-region loss weighting — to isolate whether the key factor is balancing or just providing more cerebellum data.
- Report training time overhead and computational cost of additional cerebellum patch generation.

## Removed Points

*These points are flagged to be removed. Treat them with caution if they appear in discussion.*

- **"First work" claim overstated (Harsh Critic #4)**: The critic asserts that region-specific sampling has been explored before, citing Zhu et al. 2019's "lesion-focused approach." However, Zhu et al. focuses on *pathological* lesion regions with a 2D model and loss weighting — a materially different setting from the paper's claim about treating the brain as *two coarse anatomical regions* (cerebellum vs. non-cerebellum) for 3D patch sampling. The paper qualifies the claim with "to the best of our knowledge," which is standard. Removed as a strawman that misaligns the cited prior work with the paper's specific claim.

- **Typo "NRMAE" instead of "NRMSE" (line 156)**: Parser artifact; removed per hard rules on formatting/typo criticisms.

- **Patch size 32³ with no rationale**: Overly granular; requesting rationale for every fixed hyperparameter is scope creep.

- **LR generation not specifying readout dimension**: Standard practice; the paper describes masking along two phase-encoding axes, which implicitly leaves the readout axis fully sampled.

- **No compute resources reported**: A nice-to-have but not a weakness; many papers at this length do not report this.

- **"Fail to handle the whole brain volume and the cerebellum" phrasing ambiguity**: The sentence (line 61) is clear enough in context — the referenced models reconstruct whole volumes but underperform on the cerebellum. This is not a substantive weakness.

- **Comparison with alternative balancing strategies as a requirement**: The critic calls this a "methodological gap," but the paper's contribution is specifically a patch-sampling fix, not a general framework for handling regional imbalance. The paper should be evaluated on whether the proposed approach works, not on whether it beats every conceivable alternative.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an observation about the work that the paper itself does not already make.

## Suggestions

1. **Run experiments with 3 random seeds and report mean ± std** in Tables 2 and 3. This single change would address the most consequential weakness and allow readers to assess whether the reported improvements are reliable.
2. **Add an ablation varying the sampling ratio** (e.g., 70/30, 50/50, 30/70). Even a simple three-condition ablation would significantly deepen the paper's contribution from "demonstration" to "characterization."
3. **Frame the scale factor 4 choice as a stress test** rather than a realism claim, unless a citation connecting 6.25% k-space to a specific real-world acquisition can be provided.
4. **Explicitly state** that the method is training-only and that inference requires no segmentation.
5. **Add one more recent architecture** (e.g., an attention-based model like Zhang et al. 2021) to strengthen the architecture-agnostic claim.
