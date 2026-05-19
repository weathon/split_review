- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 5, 5, 1
Now I have a thorough understanding of the paper and the reviewer inputs. Let me synthesize the final review.

## Summary

This paper systematically dissects nine influential Transformer-based 3D medical image segmentation networks across two datasets (AMOS, KiTS19). Through identity-replacement experiments, representational similarity analysis, data-efficiency scaling, and receptive field probing, it finds that: (1) most of these "Transformer" architectures are driven by substantial ConvNet backbones, while the Transformer components provide marginal performance benefit; (2) Transformers are less data-efficient than CNNs at the small sample sizes typical of medical imaging; and (3) even limited receptive fields achieve competitive performance, questioning the necessity of long-range interactions.

## Strengths

- **Identity-replacement experiments provide clean causal evidence.** Replacing whole Transformer blocks (attention + MLP) with identity mappings (Fig. 1, Table 2) shows that 8/9 architectures retain >90% performance similarity (P_sim) on both AMOS and KiTS19 without Transformers. Six networks on AMOS suffer less than a 2% DSC drop. This is the paper's strongest evidence — it directly measures marginal contribution rather than relying on correlation.

- **Data-scaling analysis over a realistic sample-size range (1%–100%).** Figure 4 shows that 3D Transformer architectures exhibit a wider performance gap to the nnU-Net CNN baseline at low sample counts (5–25 samples), and this gap narrows as data increases. This directly supports the claim that dataset size — a well-known but often-ignored factor in the medical domain — is a key roadblock for Transformer adoption.

- **Systematic quantification of convolutional backbone sizes.** Table 1 reports that 3D Transformer architectures contain 48%–352% as many convolution parameters as a standard 3D-UNet, even while 7/9 networks allocate >40% of total parameters to Transformer blocks. This grounds the "ConvNets in Disguise" observation in concrete numbers rather than speculation.

- **Volumetric Error Overlap (VEO) and CKA analyses add diagnostic depth.** Beyond DSC, VEO (Eq. 1–2) measures error-map similarity between original and Transformer-ablated models, and CKA (Fig. 2, Eq. 3–4) tracks representational changes. These reveal a spectrum of Transformer utilization — from genuinely altering representations (CoTr, nnFormer) to producing negligible representational change (TransBTS, TransUNet) — that pure accuracy metrics alone would miss.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The long-range interaction experiment (§5.3) is overclaimed relative to its evidence.** The abstract states it "question[s] the need for long-range interactions inherent to Transformers," but the experiment has three significant confounds acknowledged by the authors themselves: (a) it uses a single dataset (AMOS) and a single architecture (nnU-Net); (b) receptive field is reduced by removing downsampling stages, which also reduces model depth and capacity; (c) it tests CNN receptive field size, not the content-adaptive long-range interactions that attention provides. The paper honestly notes these as limitations in §5.3, but the framing in the abstract and introduction (e.g., "questioning the necessity of Transformer-based architecture designs") is stronger than the evidence supports. A more carefully scoped claim — e.g., "on this specific organ segmentation task, a moderate CNN receptive field suffices" — would be more appropriate.

- **Hyperparameter sensitivity is acknowledged but not tested.** The paper states (§6) that Transformers are more sensitive to hyperparameters than CNNs, and asserts this "does not significantly impact the core findings" without experimental verification. While the identity-replacement experiments are somewhat robust to this concern (they measure marginal contribution regardless of absolute performance), the claim that Transformer networks might be undertrained under the nnUNet training pipeline (designed for CNNs) is a material confound that could affect the data-efficiency experiment (Fig. 4) and the long-range interaction experiment. A controlled sensitivity analysis for at least one representative architecture (e.g., UNETR or SwinUNETR) would substantially strengthen the claim.

- **VEO and CKA categorization thresholds are used without justification.** The four-category taxonomy (Underutilized, Compensable, Non-compensable, Critical) is defined by arbitrary thresholds (VEO > 0.95, 0.85–0.95, 0.7–0.85, < 0.7; P_sim > 0.95, > 0.95, > 0.90, < 0.90). As noted by one reviewer, TransFuse has VEO = 0.92 on AMOS — just below the 0.95 threshold for "Underutilized." A small threshold shift would move architectures between categories. The paper's core finding — a spectrum of Transformer utilization — does not depend on rigid bins, and presenting the data as continuous dimensions (e.g., a scatter plot of P_sim vs. VEO) would be more transparent.

- **No error bars or confidence intervals in the data-reduction experiment (Fig. 4).** The paper reports averages over 3 folds, which is commendable, but at low sample counts (1%–5% of training data) variance is likely substantial. Showing variance would make the convergence trends more interpretable.

### Trivial
- The paper does not specify in the main text how 2D architectures (TransFuse, SwinUNet, TransUNet) were adapted to 3D volumes. While this is likely addressed in the stripped appendix (§B), it is a relevant methodological detail worth noting.
- The "5-25 samples region" annotation in Fig. 4 uses absolute sample counts while the x-axis appears to use percentage, creating a minor inconsistency.

## Nice-to-Haves

- **A controlled hyperparameter sensitivity study** for at least one or two representative architectures (e.g., UNETR, SwinUNETR) varying learning rate and warmup schedule would confirm that the core findings are not artifacts of undertuned Transformers.

- **Training time / GPU-hour reporting** would help practitioners judge whether the marginal Transformer benefit is worth the extra compute — a useful dimension for a study that may influence architecture choices in resource-constrained settings.

- **The long-range interaction experiment** could be strengthened by (a) using dilated convolutions to vary receptive field while keeping depth constant, and (b) including a second dataset with larger anatomical structures.

## Removed Points

*These points were flagged during the review process but are removed for the following reasons:*

- **"The paper dismisses hyperparameter sensitivity too lightly"** as a *major* or *fatal* weakness: The paper explicitly acknowledges this as a limitation in §6 ("training Transformers is known to be sensitive to hyperparameters, more so than CNNs"). The identity-replacement experiments (Table 2) measure marginal contribution, which is less affected by absolute performance levels. Demoted to **minor**.
- **Criticism about 2D-to-3D adaptation not being described**: The paper states "Further details are provided in §B" (stripped appendix). Since this information exists in the original submission and is only missing from the parser output, this criticism reflects a parser artifact, not an author omission.
- **Criticism that the long-range interaction experiment is "not evidential"**: The paper is transparent about limitations (§5.3), calling it a "lower bound." The experiment is suggestive and the paper claims only to "question" (not "prove") the necessity. Retained as **minor** overclaim, not a structural flaw.

## Novel Insights

None beyond the paper's own contributions. The synthesis of the two reviews does not surface a perspective that the paper itself does not already present or implicitly acknowledge.

## Suggestions

- **Reframe the long-range interaction contribution.** Replace "questioning the necessity of Transformer-based architecture designs" with a more circumscribed claim: "on the AMOS organ segmentation task, a moderately large CNN receptive field achieves competitive performance, suggesting that the unique value of Transformers may lie in content-adaptive interactions rather than raw receptive field size."
- **Remove or justify the hard VEO/CKA thresholds.** Present the data as a continuous scatter plot of P_sim vs. VEO with architecture labels, and describe the categories as rough descriptive regions rather than crisp partitions.
- **Add error bars or confidence bands to Figure 4**, particularly in the low-data regime where variance is expected to be high.
- **Briefly state in the main text** how 2D architectures were adapted to 3D volumes (even one sentence: "2D architectures were applied per-slice" or "using 2.5D patches").
