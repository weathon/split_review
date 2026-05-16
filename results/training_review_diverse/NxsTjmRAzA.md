Now I have a thorough understanding of the paper. Let me compile the final review.

## Final Review

## Summary

This paper proposes a test-time augmentation (TTA) based OOD detection method that uses K-nearest-neighbor search on mild TTAs (sequential masks) rather than on a large reference set of InD training data. The key contributions are: (1) a systematic categorization of TTAs into InD Augmentations (IDA) and OOD Augmentations (OODA) based on their effect on OOD score distributions, (2) a data-efficient, InD-independent OOD detector that generates only 16–25 masked variants of the test sample and compares their embeddings, and (3) demonstration that this approach is competitive with or outperforms methods that rely on hundreds of thousands of reference samples.

---

## Strengths

1. **Novel and well-motivated approach to data-efficient OOD detection.** The core idea — replacing a large reference set with synthetic TTAs of the test sample itself — is clever and practically appealing. On CIFAR-10, the method achieves 94.19% average AUROC (vs. KNN's 93.72%) using only 16 masked variants instead of the full 50k training set. On ImageNet, 25 TTAs yield 84.22% average AUROC, outperforming KNN (82.39% with 200k samples) and VIM (81.17%). These results are substantiated in Tables 3 and 4.

2. **Systematic IDA/OODA taxonomy with clear empirical support.** The paper provides the first systematic analysis of which TTAs preserve vs. shift InD score distributions. Table 1 shows a clean separation: IDA methods (HFlip, Gray, Mask, Crop) achieve 81–89% AUROC on CIFAR-10, while OODA methods (VFlip, Rotate90, ColorJitter, Invert) are near-random (31–57%). Table 2 correlates LPIPS scores with detection performance, providing an actionable metric for selecting IDAs. This taxonomy is a useful conceptual contribution beyond the specific method.

3. **InD-independence as a key differentiator.** Unlike KNN, VIM, and Mahalanobis-distance methods, the proposed approach requires no access to training data at test time. This makes it applicable in privacy-sensitive or memory-constrained settings where retaining the full training set is infeasible. The method is also model-agnostic (demonstrated across ResNet50, ViT-B/16, Swin-B, DeiT-S in Table 8) and can be combined with ReAct activation rectification (Table 5) for further gains.

4. **Strong adversarial robustness compared to logit/softmax-based methods.** Under PGD attacks, MSP, Energy, and ODIN collapse to near-random performance, while the proposed sequential-mask method maintains 80.50% average AUROC on CIFAR-10 (Table 6). This is a genuine practical advantage for deployment in adversarial settings.

---

## Weaknesses

### Fatal

None.

### Major

1. **Headline claim about "1.2 million images" is in tension with the experimental setup.** The abstract, introduction (line 24), Figure 1 caption (line 15), contribution list (line 27), and Section 4.3 (line 126) all claim that the method outperforms KNN "using the entire training set (1.2 million images)" or "with 1.2 million images as a reference set." However, the experimental setup (line 105) states: *"VIM and KNN require 50,000 and 200,000 InD data on CIFAR-10 and IMAGENET, respectively."* The main comparison in Table 4 therefore uses KNN with 200k samples, not 1.2M. If Figure 1 includes KNN results at 100% sampling (1.2M) that support the claim, the paper should explicitly state this. If the claim is extrapolated from the sampling-ratio plot, that must be clearly labeled as an estimate. As it stands, the prominent "1.2 million" claim appears to exceed what the experiments directly demonstrate. The core contribution (25 TTAs vs. 200k reference samples) is still impressive and does not depend on this overstatement, but the mismatch between claim and evidence needs correction.

2. **Overclaiming relative to ASH, the actual SOTA.** On ImageNet (Table 4), ASH achieves 86.25% average AUROC vs. the proposed method's 84.22%. The paper acknowledges this (line 124) but the abstract and conclusion claim the method "outperforms state-of-the-art methods" and "consistently outperforms the SOTA methods" (line 28). These blanket statements are misleading without qualification. The paper's genuine advantage is InD-independence, not raw performance — it should be positioned as a strong InD-independent alternative, not as universally SOTA. Moreover, the ablation section (line 154) claims that even with the worst hyperparameter the method achieves "over 86% on IMAGENET, surpassing the SOTA (85.54%)," but this 85.54% figure is inconsistent with the 86.25% ASH number cited earlier, and the relationship between these numbers is never explained.

3. **Sequential mask TTA is underspecified for reproducibility.** The paper describes it as applying masks "in a sequential manner" (line 66) and gives mask sizes (8×8 for CIFAR-10, 44×44 for ImageNet) and counts (16 and 25), but does not specify the spatial algorithm: Are masks applied systematically (e.g., scanning window) or randomly? Are they overlapping? What is the sequence generation procedure? Figure 9 provides visualizations but no algorithmic description. For a paper whose central methodological contribution is this TTA strategy, the lack of a precise specification (pseudocode or detailed spatial procedure) is a reproducibility gap.

### Minor

1. **The IDA/OODA analysis is qualitative where it could be quantitative.** The claim that IDA "does not affect the score distribution of InD data" while OODA causes a shift (Figure 2) is supported only by visual inspection of density plots. Adding distribution discrepancy metrics (KL divergence, Wasserstein distance, or KS statistic) would turn an observation into a measurable finding. Similarly, LPIPS values in Table 2 are reported without variance, making it unclear whether differences are significant.

2. **The "robust to adversarial examples" claim in the abstract is too broad.** Section 4.5 (line 142) honestly reports that under C&W attacks, "the detection performance is relatively low." This limitation is at odds with the unqualified "robust to adversarial examples" in the abstract. The claim should be caveated to reflect the method's vulnerability to certain attack types.

3. **Test-time computational cost is not discussed.** The method runs the model 17–26 times per sample (1 input + 16 or 25 TTAs). This is a significant overhead compared to single-pass methods (MSP, Energy, ODIN) and should be acknowledged. The trade-off with KNN (which stores a large reference set but only does one forward pass plus a search) is relevant for practitioners.

4. **No confidence intervals or significance tests.** Given small performance differences (e.g., 0.47% AUROC on CIFAR-10), it is unclear whether improvements over KNN are statistically reliable. This is standard practice in OOD detection benchmarks, but it limits the certainty of fine-grained comparisons.

5. **Inconsistency in SOTA numbers between sections.** The ablation (line 154) cites SOTA as 85.54%, while Section 4.3 (line 124) implies ASH achieves ~86.25%. These numbers need to be reconciled or contextualized.

### Trivial

- Section 4.3 claims "our method maintains consistent performance across different InD datasets without such dataset-specific adaptations" — this is an advantage worth highlighting, but the paper provides no experiment showing the method applied to multiple InD datasets without tuning.

---

## Nice-to-Haves

- **Add distribution discrepancy metrics** (KL divergence, Wasserstein distance) to quantify the IDA/OODA distribution shift in Figure 2, strengthening the evidentiary basis for the taxonomy.
- **Include a brief discussion of test-time overhead** (number of forward passes) and compare it with the storage/search costs of KNN to help practitioners evaluate the trade-off.
- **A sensitivity analysis for the 95% ID classification threshold** would clarify how dependent results are on this hyperparameter.

---

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"First comprehensive study" / "first to investigate" — He et al. (2022) already used TTAs for OOD detection.** *Reason for removal:* The paper acknowledges He et al. (line 22) and qualifies its contribution as the *first systematic study* (not first use) of TTA *types* for OOD detection. This is a fair distinction. The reviewer's criticism is a misreading of the scope claim.
- **LPIPS without error bars — unclear over how many samples.** *Reason for removal:* This is a presentation nitpick; LPIPS is typically reported as an average. The paper's conclusions about LPIPS are at the scale of comparing augmentation categories (IDA vs. OODA), where the differences are large and ordinal, not fine-grained.
- **K-value selection procedure described as vague.** *Reason for removal:* The paper references "the validation method in Hendrycks et al. (2018b)" — this is a standard citation to an established procedure. Demanding that it be re-described in full text is a reproducibility nitpick beyond reasonable bounds.
- **Missing appendix references / proofs.** *Reason for removal:* Parser-stripped sections. The original submission contains these.
- **Formatting/style nitpicks.** *Reason for removal:* Parser artifacts, not author errors.
- **Missing related works.** *Reason for removal:* Cannot verify existence of unmentioned works without external knowledge; violates hard rules.
- **The method should also cover domain Y / task Z.** *Reason for removal:* Scope creep — the paper focuses on a specific method and benchmark, and demands for additional tasks constitute broadening the paper rather than strengthening it.
- **Strengths from Strength Finder that are generic:** Several strengths framed generically (e.g., "model agnosticism and plug-and-play integration" as a separate strength when it overlaps with InD-independence) are merged into the main strengths or dropped where redundant.

---

## Novel Insights

Beyond the paper's own contributions, the reviews surface one genuinely novel observation: the connection between the IDA/OODA taxonomy and the LPIPS perceptual similarity metric is an underexplored direction. The paper shows a strong correlation (low LPIPS → good OOD detection) with one exception (grayscale). If this relationship holds more broadly, LPIPS could serve as a cheap proxy for screening candidate TTAs without running full OOD detection experiments. This is a testable hypothesis that the paper enables but does not fully exploit. The possibility that C&W attacks are "invisible" to masking-based TTAs (because tiny perturbations don't interact with coarse masks) is another insight that could inform future work on TTA-based adversarial defenses.

---

## Suggestions

1. **Correct the "1.2 million" overstatement.** Either (a) run KNN with the full 1.2M training set (or the largest feasible subset) and report results, or (b) revise all claims to accurately reflect that the comparison used 200k samples, noting that the 1.2M figure represents the full training set size in principle. This is the single most important revision.

2. **Reconcile the SOTA numbers** (85.54% vs. 86.25%) and ensure the paper's positioning reflects that ASH outperforms the proposed method on average AUROC for ImageNet, even if it requires dataset-specific tuning.

3. **Add a pseudocode block or precise spatial description** for the sequential mask algorithm (e.g., stride, overlap, scanning order) to ensure reproducibility.

4. **Qualify the adversarial robustness claim** to acknowledge the C&W vulnerability, and add a brief discussion of test-time computational cost.

5. **Add confidence intervals** for the main results or acknowledge their absence as a limitation.

6. **Tone down blanket "outperforms SOTA" statements** in the abstract and conclusion to reflect the actual comparative picture: superior to KNN/VIM, competitive with but below ASH on average, with the key differentiator being InD-independence.

---

## Score and Decision

The paper presents a genuine, practical contribution: a clever, data-efficient, InD-independent OOD detector built on a novel TTA strategy with a useful accompanying taxonomy. The core idea is sound, the experiments are broad, and the results are competitive. However, the paper is marred by a significant evidential gap in its headline claim (the "1.2 million images" comparison is not clearly supported by the experimental setup described in the paper), by overclaiming relative to ASH (which outperforms the method on average), and by an underspecified algorithmic contribution (sequential mask). These are fixable issues — they do not invalidate the contribution — but they require substantive revision to the paper's claims and presentation. The paper would be suitable for acceptance after these corrections but cannot be accepted in its current form.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>