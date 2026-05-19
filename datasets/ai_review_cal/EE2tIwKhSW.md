- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 6, 5
Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper identifies two critical defects in prior evaluations of membership inference attacks (MIAs) on diffusion models — over-training on small datasets and distribution shift between member and non-member sets — which inflate apparent MIA performance. The authors introduce CopyMark, a benchmark employing pre-trained diffusion models (trained for 1 epoch) with unshifted or minimally-shifted member/non-member pairs and a two-stage evaluation protocol (validation set for threshold tuning, held-out test set for blind evaluation). Experiments show that existing MIAs fail under these realistic conditions: loss-based methods achieve near-random performance, and classifier-based methods suffer large test-set FPR spikes (0.10–0.43) despite perfect validation AUC.

## Strengths

- **Systematic identification of two defects in prior MIA evaluation on diffusion models (Table 1, Section 3):** The paper explicitly catalogs nine prior evaluation setups, marking each for over-training and/or dataset shift. This tabular evidence cleanly demonstrates that both defects are pervasive and that prior MIA "success" may be entirely an artifact of these unrealistic conditions.

- **Two-stage evaluation protocol that prevents threshold overfitting (Algorithms 1 and 2, Section 4.4):** The paper separates validation and test datasets. Table 2 shows that classifier-based MIAs (GSA₁, GSA₂) achieve perfect AUC on validation sets but their test-set FPRs spike to 0.10–0.43, directly demonstrating that prior single-dataset evaluations overestimate real-world performance.

- **Construction of three realistic evaluation setups with pre-trained models and minimal dataset shift (Table 2, Figure 1):** The paper selects SD1.5 (LAION→LAION), CommonCanvas-XL (CommonCatalog→MS-COCO), and Kohaku-XL (HakuBooru→HakuBooru) — all trained for 1 epoch. CLIP embedding analysis validates that member/non-member pairs are nearly indistinguishable (TPRs ~0.53–0.69 on new setups vs. 0.88–0.95 on defective setups).

- **Cross-validation of implementation against original papers (Section 5):** The paper reproduces prior results on defective setups (a) and (b) within a few percentage points of the published numbers (e.g., PFAMI AUC 0.9172 vs. 0.961 in original), confirming that the implementation is correct and that performance drops are attributable to the benchmark design, not implementation errors.

- **Blind baseline exposes confound (Table 2):** A ConvNext classifier trained directly on pixel features (no model access) matches or beats all loss-based MIAs on the realistic setups and achieves comparable performance to classifier-based MIAs, demonstrating that prior MIA success was confounded by distribution shift rather than reflecting genuine membership inference.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims — that prior evaluations are defective and that current MIAs fail under realistic conditions — are well-supported by the evidence. The weaknesses below are important to address but do not threaten the validity of the main contribution.

### Minor

- **Setup (d) has a moderate distribution shift that exceeds what "minor" typically conveys.** The paper acknowledges this (CLIP embedding classifier achieves TPR 0.690/0.606 on validation/test), and the results remain consistent with the failure narrative. However, this setup sits in an awkward middle ground: the shift is clearly non-negligible compared to setups (c) and (e) (where TPRs are ~0.53–0.59), yet the paper labels it alongside them as a "real-world" setup. The paper would be stronger by either providing a clearer quantitative justification for the "minor" label or explicitly reclassifying (d) as a "controlled-shift" setup distinct from the unshifted ones. The results are not harmed by removing or reclassifying (d), so this is a framing issue rather than an evidential one.

- **Results lack variance estimates.** All metrics are point estimates from a single validation/test split with a fixed random seed (stated in Section 4.3). For loss-based MIAs the near-random scores are so far from success that variance is unlikely to change the conclusion. But for classifier-based MIAs, the test-set FPR values (0.10–0.43) are the core evidence of overfitting; reporting results over 3–5 random splits or providing standard deviations would strengthen confidence that these FPR spikes are stable and not artifacts of a particular split.

- **The "fail" criterion could be stated more precisely.** The paper asserts "all MIA methods fail on our new real-world setups," which is accurate for loss-based MIAs (TPRs near the FPR threshold = no better than random). For classifier-based MIAs, "fail" means the test FPR far exceeds the intended bound (1% or 0.1%) — these methods do detect some members (TPR 0.55–0.89) but at an uncontrolled false positive rate that renders them unreliable as evidence. The paper already makes this distinction in Section 5 but could carry it more clearly into the abstract and conclusion to avoid ambiguity.

### Trivial

- **Blind baseline details are sparse.** The ConvNext architecture (size, training hyperparameters, data augmentation) is not specified, making exact reproduction harder. Given the baseline's importance for comparison, these details would be useful.

- **No discussion of computational cost** of feature extraction or attack execution, which would be helpful for practitioners considering using these methods.

## Nice-to-Haves

- An ablation where the GSA classifier's threshold is tuned on a held-out subset of the validation data (rather than the full validation set) to further isolate the overfitting mechanism.
- Extension to other model families (PixArt-α, DALL-E variants) noted as future work, which the paper already suggests implicitly.

## Removed Points

These points were considered but removed or demoted in the final review:

- **Harsh critic's claim that setup (d) "weakens the central claim that CopyMark eliminates distribution shift":** The paper never claims to eliminate distribution shift in (d); the caption for Table 2 explicitly says "minor or no dataset shift" and the CLIP analysis section transparently acknowledges the shift. The core finding (MIAs fail) is supported by (c) and (e) alone, so (d) does not weaken the central claim. The concern is retained as a **minor** weakness (framing issue), not a major one.

- **"The justification for including setup (d) despite its shift is thin":** The paper does provide justification — the shift is quantified via CLIP, compared against the severe shifts in (a)/(b), and the results still show failure — so this criticism is partially addressed. Retained at the minor level with reduced weight.

- **"The blind baseline's architecture details are not given, making it harder to reproduce":** Retained as a trivial point.

- **Strength Finder strength about "the paper addressed an important problem":** This is a generic/superficial strength about problem importance, not specific to this paper's execution. Dropped.

## Novel Insights

The reviews collectively highlight a meta-point not explicit in the paper: the CLIP-based validation methodology used to certify CopyMark's benchmark quality itself establishes an upper bound on what any semantic-content-based attack could achieve. On setup (c), CLIP achieves TPR 0.53–0.54 — essentially random — while on setup (d) it reaches TPR 0.69. The fact that classifier-based MIAs achieve TPRs of 0.70–0.89 on the test set of these same setups yet suffer FPR spikes of 0.10–0.43 reveals that these attacks are learning features that are *more predictive than semantic content alone* on the validation set but entirely fail to generalize. This suggests the classifier overfitting is not merely capturing dataset artifacts but is learning spurious correlations in model features that break under distribution shift — a stronger indictment than simply "MIAs fail."

## Suggestions

1. **Clarify the status of setup (d)** in the table caption and methodology section. Either (a) explicitly reclassify it as a "controlled distribution shift" setup rather than grouping it with the unshifted setups (c) and (e), or (b) provide a quantitative justification for why CLIP TPR 0.69 constitutes "minor" shift (e.g., by showing that it does not enable any MIA method to succeed).

2. **Add variance estimates** for the key test-set FPR and TPR values in Table 2, reporting results over at least 3 random validation/test splits. This is particularly important for the classifier-based MIAs where the FPR spike is the central evidence.

3. **Sharpen the "fail" language** in the abstract and conclusion. For example: "Loss-based MIAs perform no better than random; classifier-based MIAs achieve unacceptably high false positive rates (exceeding intended bounds by 10–40×) on held-out test data." This makes the precise nature of failure clear upfront.

4. **Provide minimal architecture details** (or a citation to the exact ConvNext variant) for the blind baseline to support reproduction.
