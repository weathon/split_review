Now I have all the information I need. Let me compose the final consolidated review.

## Summary

This paper proposes SBGC, an unsupervised method for heterogeneous change detection in remote sensing images. It combines self-supervised contrastive learning (via pseudo-Siamese networks with a sub-ResNet18 encoder) to extract modality-invariant features, constructs KNN graphs from these features, and introduces bidirectional graph comparison (BGC) — comparing original and mapped graph structures in both directions — to capture change information more completely than prior one-way approaches. The method is evaluated on three heterogeneous datasets against seven baselines, reporting strong performance in both accuracy and computational efficiency.

## Strengths

- **Self-supervised feature learning improves over raw-pixel baselines**: The paper replaces the original-pixel features used in prior graph-based methods (e.g., Sun et al. 2021b, 2022) with SSL-learned features. The ablation study (Table 3) confirms that adding SSL alone raises KC by 4–10% across datasets, providing clear evidence that this component contributes meaningfully.

- **Bidirectional graph comparison is a principled extension of prior one-way approaches**: The paper identifies that previous work (e.g., Sun et al. 2022) discards change information from the original modality's graph by comparing only the mapped graph against one target. BGC addresses this by computing differences both between the original and mapped graphs within the same modality and between the mapped graph and the other modality's graph (Eq. 4). Ablation shows adding BGC on top of SSL further improves KC by 3–5%.

- **Strong empirical results with dramatic speed advantage**: SBGC achieves the highest OA and KC on all three datasets while requiring the lowest computation time by a large margin (e.g., on Shuguang: 92.05% KC in 19.35s vs. second-best INLPG at 89.73% KC in 2015.95s). This combination of accuracy and efficiency is the paper's strongest evidence for practical utility.

- **Hyperparameter analysis for patch size**: Section 3.4 and Fig. 4 systematically explore the effect of patch size on KC, providing practical guidance for applying the method.

## Weaknesses

### Fatal
None.

### Major

1. **The contrastive loss formulation (Eq. 1) is non-standard and lacks justification.** The loss is written as:
   \[
   \mathcal{L}_{\mathrm{CL}}^{\chi}=-\sum_{i=1}^{M}\log\frac{d_{\Theta}(z_{x^{i}},p_{x^{i}})}{\sum_{j=1}^{M}d_{\Theta}(z_{x^{j}},p_{x^{j}})}
   \]
   The denominator sums the cosine similarities of *all positive pairs* across all M patches, with *no negative pairs* or temperature parameter. This is not a standard InfoNCE, NT-Xent, or BYOL-style loss. In standard contrastive learning, the denominator includes the positive pair plus explicitly sampled negative pairs; without negatives, the loss may allow or even encourage feature collapse (if all patches learn identical features, each ratio becomes 1/M and the loss is constant). The paper provides no theoretical or empirical analysis showing that this formulation avoids collapse, and the description ("positive sample pairs are assigned a higher value representing a close distance") does not explain why the denominator sums across patches rather than including negatives. If the actual implementation uses a different loss (e.g., a standard InfoNCE), this must be corrected. This is a structural methodological concern because the SSL component is central to the method's claimed improvement over prior work.

2. **Potential discrepancy between claimed KC improvements and Table 2 values on the Sardinia dataset.** The text states that SBGC achieves "an improvement in KC of … 14.38% (PMBCN), 20.31% (NPSG), 19.74% (INLPG), and 23.5% (SRGCAE)" on Sardinia. The harsh reviewer reports that Table 2 actually shows SBGC's KC is *lower* than PMBCN's (0.5814 vs. 0.5942) and that the relative improvements over NPSG, INLPG, and SRGCAE are substantially smaller than claimed (e.g., ~9% instead of 20.31%). **I cannot independently verify these exact values because Table 2 is embedded as an image** — however, the discrepancy asserted by the reviewer, if confirmed, would mean the text makes materially false quantitative claims. The authors must clarify: (a) report the actual KC values for all methods on Sardinia, and (b) reconcile any mismatch between the text's stated relative improvements and the table values. This is the single most urgent issue for assessing the paper's credibility.

3. **No information on baseline method configuration.** Section 3.2 lists the seven baselines but provides no details on how they were configured — whether official implementations were used, whether hyperparameters were tuned per dataset, or what default settings were applied. Without this information, it is difficult to assess whether the comparisons are fair or whether a well-tuned baseline might close the reported gaps. Given that the method reports a large speed advantage over several baselines (e.g., 19s vs. 2016s for INLPG), the community needs to know whether these baselines were run under the same conditions.

### Minor

- **Weight sharing in pseudo-Siamese networks is ambiguous.** The paper states "the upper branch shares the same network architecture, excluding the predictor" (Section 2.2). This describes architecture sharing, but does not clarify whether the *encoder weights* are shared between the two branches (as in BYOL/SimSiam) or not. If weights are not shared, the encoders could learn different feature spaces for X and Y, which would complicate cross-modal graph construction. This must be stated explicitly.

- **Missing implementation details for the encoder.** The sub-ResNet18 architecture is described only as modifying "the stride of the first layer from 1 to 2" and removing "the third and fourth layers." The output feature dimension after the encoder is not stated, nor is it explained how 9×9 patches are processed by a ResNet with modified strides (e.g., whether padding is used, what the effective receptive field becomes). These details are needed for reproducibility.

- **Otsu thresholding assumption not discussed.** The thresholding step assumes a bimodal histogram in the difference image. The paper does not discuss whether this assumption holds for heterogeneous difference images or verify bimodality on the used datasets. While the results suggest the approach works, acknowledging this limitation would strengthen the paper.

- **No variance or multiple-run statistics reported.** For an unsupervised method with stochastic components (SSL initialization, data augmentations), reporting mean ± std over multiple runs is standard practice. The paper reports only single-run results, making it impossible to assess the stability of the claimed improvements.

- **No discussion of limitations or failure cases.** The paper does not discuss conditions under which SBGC might struggle (e.g., extreme modality heterogeneity, very small changed regions, sensitivity to the choice of K). Adding this would improve the paper's scientific rigor.

### Trivial

- Equation numbering is slightly garbled in the extracted text (e.g., `\bar{\mathcal{L}}` in the loss equation).
- The paper says "modifying the stride of the first layer from 1 to 2" — in standard ResNet18, conv1 already has stride 2; the intended modification is unclear.

## Nice-to-Haves

- A pseudocode or algorithmic description of the BGC procedure would improve reproducibility and clarity, since BGC is the method's key novel component.
- A variant in the ablation that includes BGC *without* SSL would more cleanly isolate BGC's individual contribution (the current ablation compares: raw pixels+one-way → SSL+one-way → SSL+BGC, which is informative but confounds the two components' interaction).
- An analysis of sensitivity to the choice of K (number of nearest neighbors) would strengthen the hyperparameter discussion.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Criticism about BGC's KNN sets potentially referring to different spatial locations (harsh critic's Section 2.3 note).** The reviewer questions whether comparing independently-determined KNN sets of x^i and y^i is meaningful. However, the BGC comparison in Eq. 4 uses the *same spatial coordinates* for both graphs — G_{x^i}^X uses x^i's neighbors in X feature space, and G_{x^i}^Y uses the *same spatial neighbors* but with Y features. The second term compares this mapped graph to G_{y^i}^Y (the graph of the corresponding location y^i in Y space). The rationale — that unchanged areas should preserve structural relationships across modalities — is standard in the graph-based CD literature and was already explained in Fig. 2. This criticism misunderstands the paper's design.

- **Abstract complaint that SBGC does not win on every single dataset individually.** The abstract claims "best performance with an average OA of 96.69%." This is an average claim, not a claim of winning every dataset. The reviewer acknowledges it is accurate on average, then points out that on California SBGC is outperformed by two methods (per the reviewer's reading of the table). Even if true, this is a reasonable presentation of average results and not a weakness of the paper.

- **Several formatting/style nitpicks and requests for appendix content or missing references.** These are parser artifacts or outside the scope of the conference submission format.

- **Request for a "BGC without SSL" variant in ablation.** This was moved to Nice-to-Haves; while it would be nice to have, the current ablation already shows each component's contribution (SSL over raw pixels, BGC over SSL-only) and is sufficient to support the paper's claims.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Correct or clarify the contrastive loss.** Either rewrite Eq. 1 as a standard InfoNCE/NT-Xert loss with explicit negative sampling if that is what was implemented, or if the current formulation is correct, provide a justification and show empirically that it avoids collapse (e.g., analyze feature diversity or add a regularization term).

2. **Reconcile the Sardinia KC claim with Table 2.** Report the actual KC values for all methods on Sardinia in the text and ensure the stated relative improvements match the table. If the table values indeed show SBGC below PMBCN, this must be acknowledged and explained.

3. **Specify baseline configurations.** Add a sentence or table describing how each baseline was set up (official code, default hyperparameters, any per-dataset tuning).

4. **Clarify weight sharing** in the pseudo-Siamese network and report the output feature dimension of the sub-ResNet18 encoder.

## Score and Decision

This paper makes a reasonable contribution — combining SSL features with bidirectional graph comparison for heterogeneous CD is a sensible extension of prior work, and the ablation supports the value of both components. The computational efficiency results are impressive. However, the paper has two significant unresolved issues: (1) the contrastive loss as written is non-standard and may not function as claimed, and (2) a potential discrepancy between the text's claimed KC improvements and the actual table values on the Sardinia dataset needs urgent clarification. These issues directly affect whether the paper's central quantitative claims are reliable. Combined with the missing implementation details and lack of variance reporting, the paper requires major revision before it can be accepted.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>