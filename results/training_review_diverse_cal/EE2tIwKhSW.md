Now I have all the information I need to write the final consolidated review. Let me synthesize.

---

## Summary

This paper identifies two critical defects in prior membership inference attack (MIA) evaluations on diffusion models — over-training (models trained for hundreds of epochs) and dataset shift (members and non-members drawn from different distributions) — which artificially inflate reported MIA performance. To address these, the authors propose CopyMark, the first unified benchmark using pre-trained models (trained for one epoch) with minimally or unshifted member/non-member pairs. Through extensive experiments on three realistic setups (SD1.5 on LAION, CommonCanvas-XL on CommonCatalog/MS-COCO, Kohaku-XL on HakuBooru), the paper demonstrates that loss-based MIAs (SecMI, PIA, PFAMI) perform near chance and classifier-based MIAs (GSA₁, GSA₂) suffer severe false-positive-rate inflation on held-out test sets. A two-stage validation/test evaluation protocol reveals that classifier-based methods overfit to the validation set, and a blind baseline (ConvNext without model access) often outperforms loss-based MIAs. The paper concludes that current MIAs on diffusion models are unreliable as evidence of unauthorized data usage.

## Strengths

- **Systematic identification of two fatal defects in prior MIA evaluation — over-training and dataset shift.** The paper provides a clear, table-driven breakdown (Table 1, Section 3) showing that every prior evaluation setup either over-trains the model (300–500 epochs) or uses non-members from a different distribution (e.g., CelebA members vs. FFHQ non-members), or both. This diagnosis is concrete and directly explains prior inflated performance.

- **Construction of CopyMark, the first unified benchmark for diffusion model MIAs that eliminates both defects.** CopyMark uses three pre-trained models (SD1.5, CommonCanvas-XL-C, Kohaku-XL-Epsilon) trained for only one epoch, and pairs members with non-members from identical or near-identical distributions (Section 4.1, Table 2). The CLIP-embedding analysis (Figure 1, Table 3) quantitatively verifies that these setups have minimal or no distribution shift, unlike prior setups where CLIP could separate members/non-members with >90% accuracy.

- **Introduction of a two-stage blind evaluation protocol that reveals overfitting in classifier-based MIAs.** The paper separates data into validation and test sets (Section 4.4, Algorithms 1 and 2). This exposes that classifier-based MIAs (GSA₁, GSA₂) achieve perfect AUC on the validation set but their test-set FPR far exceeds the intended bound (e.g., FPR = 0.27–0.43 on setups (c) and (e), Table 4). No prior MIA evaluation on diffusion models used such a blind test.

- **Comprehensive empirical evidence that current MIAs fail under realistic conditions.** Table 4 shows that on the three realistic setups (c), (d), (e), loss-based MIAs achieve TPR@1%FPR near 0.01 (essentially random), and classifier-based MIAs suffer large FPR inflation. The blind baseline often outperforms loss-based MIAs, confirming that prior "success" was confounded by distribution shift.

- **Critical analysis of the role of MIAs in AI copyright lawsuits.** Section 6.2 argues that even a perfect MIA only provides a binary membership indicator, while copyright law requires "substantial similarity" between generated images and original works, making current MIAs unsuitable as legal evidence. This grounding in real-world legal requirements adds practical significance beyond the technical benchmark.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Uneven control of dataset shift across the three new setups.** Setup (d) (CommonCanvas-XL with CommonCatalog members / MS-COCO non-members) has a detectable distribution shift — CLIP hyperplane classification achieves TPR 0.690/0.606, well above random. While the paper explicitly acknowledges this as "minor" and still qualifies the setup, the evidence for MIA failure on (d) is less clean than on the no-shift setups (c) and (e). On (d), GSA₁ achieves TPR@1%FPR=0.891 on the test set (albeit with FPR=0.313), and the blind baseline achieves TPR=0.880 (FPR=0.156), showing some remaining signal. The paper's narrative would benefit from more explicitly distinguishing the evidentiary strength across the three setups rather than grouping them uniformly as failures. This does not invalidate the core finding (loss-based MIAs still fail on (d) with TPRs near 0.01), but it bounds how broadly the results can be claimed.

- **Limited model coverage constrains the strength of general claims.** The paper tests only three pre-trained models (SD1.5, CommonCanvas-XL, Kohaku-XL), the maximum possible given the dual constraint of publicly accessible training datasets and valid non-members. The paper's conclusion — "MIAs on diffusion models are not reliable" — is stated broadly, but the empirical basis covers only three models, one of which (SD1.5) is the only widely-used one. The paper does not examine *why* loss-based MIAs fail mechanistically (e.g., whether the cause is one-epoch training, dataset size, model capacity, or noise schedule). The discussion (Section 6.1) speculates that "the difference is smaller" and "variance may grow bigger," but this is post-hoc rather than derived. Without deeper analysis, the possibility remains that some pre-trained model trained on fewer images or with different schedules could still exhibit vulnerability. The paper is transparent about this constraint, but the claims should be tempered accordingly.

- **Discrepancies between reproduced results and original paper results are larger than acknowledged.** For PFAMI on setup (a), the paper reports AUC 0.9172 vs. the original 0.961 — a gap of 0.044. For SecMI on setup (b), the paper's TPR@1%FPR is 0.2888 vs. the original 0.1858 — a 55% relative improvement. The paper attributes these to "differences in random seed and dataset sampling," but differences of this magnitude deserve specific investigation. While these do not affect the paper's core findings about the new setups, they weaken the cross-validation claim.

- **Missing implementation details for MIA methods.** The paper does not specify how many timesteps, noise levels, or random seeds are used when computing loss/score for SecMI, PIA, and PFAMI. For pre-trained models like SD1.5 with thousands of timesteps, the computational cost is high, and approximations may introduce noise that itself degrades performance. The paper should state the exact procedure (e.g., number of timesteps sampled per image, number of random seeds) to ensure reproducibility and to rule out the possibility that implementation choices contributed to the observed failure.

### Trivial

- **No confidence intervals or measures of statistical significance.** Results (Table 4) show single numbers without confidence intervals. Given the random sampling of 2500 members and 2500 non-members, TPRs at low FPR could have non-trivial variance (25 FPs at 1% of 2500). Reporting standard errors or showing stability across multiple random splits would increase confidence.

- **Blind baseline training specification is incomplete.** The paper states the blind baseline trains a ConvNext to classify members and non-members but does not specify the exact training data split (whether it uses the same validation set as the MIA methods) or architecture details. Clarifying this would ensure fair comparison.

## Nice-to-Haves

- **Analyze the loss distributions directly.** The paper's discussion (Section 6.1) says loss-based MIAs fail because "the difference is smaller" and "variance may grow bigger." Computing and visualizing the actual distribution of losses for members vs. non-members on the pre-trained models (similar to how Section 3 uses CLIP embeddings to quantify dataset shift) would make the failure mechanism concrete and visual, strengthening the argument.

- **Disentangle the two factors (over-training and dataset shift) in the defective setups.** The paper could more explicitly compare setup (b) (SD1.5 with shifted non-members) vs. setup (c) (same model with unshifted non-members) to isolate the effect of dataset shift. This comparison is already implicit in the results — the dramatic drop from (b) to (c) is the paper's most compelling evidence — but foregrounding it would sharpen the narrative.

- **Quantify the degree of over-training in defective setups.** Showing the gap between training loss and hold-out loss for members vs. non-members on over-trained models would directly illustrate why loss-based MIAs worked on those setups and why they fail on pre-trained models.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **Critical Issue 3 (Harsh Reviewer):** The claim that the paper "does not convincingly show that previous evaluations were actually using the same dataset for threshold selection and reporting" and "overstates the novelty" of the two-stage evaluation. This criticism misunderstands the paper's contribution — the paper correctly identifies that prior diffusion-model MIA evaluations lacked a held-out test set, and the two-stage protocol reveals genuine classifier overfitting. The novelty lies specifically in demonstrating this validation-to-test gap for diffusion model MIAs, which no prior work had done. The reviewer's argument conflates the standard practice of threshold search (which the paper does not criticize) with the absence of held-out testing (which the paper correctly identifies as a gap). *Removed per Hard Rule #2 (factually incorrect/misunderstands the paper).*

2. **"Strengthening the Paper on Its Own Terms" section (Harsh Reviewer):** These are constructive suggestions (analyzing loss distributions, disentangling over-training and shift, computing loss distributions), not weaknesses. Moved to Nice-to-Haves.

## Novel Insights

The most noteworthy observation across the reviews is that the results expose an asymmetry between loss-based and classifier-based MIAs that previous work missed entirely: loss-based MIAs actually generalize well (consistent validation/test performance) but are fundamentally uninformative (near-random), while classifier-based MIAs achieve perfect validation-set performance but catastrophically overfit to held-out data. This suggests that the two families of methods have orthogonal failure modes — one signal-starved, the other overfitting-prone — which implies that simply combining them will not solve the problem. A genuinely robust MIA would need to address both issues simultaneously: finding a signal that exists even after one training epoch while using a representation that does not overfit to the validation set. This diagnostic insight is more actionable than the paper's own "refine feature selection" suggestion.

## Suggestions

- **For the camera-ready version:** Add standard errors or confidence intervals to Table 4, or show stability across multiple random splits. Specify the exact procedure for loss-based MIAs (number of timesteps, noise levels, random seeds). Clarify the blind baseline training setup.
- **For future work building on this benchmark:** The paper convincingly shows that current MIAs fail, but does not identify *why* at a mechanistic level. Computing and visualizing the distribution of per-sample losses for members vs. non-members on pre-trained models would turn the post-hoc speculation in Section 6.1 into a concrete diagnosis.
- **Narrative refinement:** Reframe the conclusion from "MIAs fail on diffusion models" to "MIAs fail on currently testable pre-trained diffusion models under properly controlled conditions," and explicitly grade the strength of evidence across the three setups.

## Score and Decision

This paper makes a solid contribution by exposing systematic over-optimism in prior MIA evaluation on diffusion models through careful diagnosis and a new benchmark. The weaknesses are real but minor — they bound the generalizability of the claims rather than invalidating them. The paper is original, the experiments are sound, the writing is clear, and the benchmark will be valuable to the community.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>