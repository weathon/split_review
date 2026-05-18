Now I have a thorough understanding of the paper and all the reviewer claims. Let me compose the final consolidated review.

## Summary

This paper proposes MILLET (Multiple Instance Learning for Locally Explainable Time series classification), a framework that upgrades existing deep learning TSC models (FCN, ResNet, InceptionTime) to produce inherently interpretable per-time-point explanations alongside predictions. By replacing global average pooling with MIL-based pooling methods — including a novel PADD (parallel attention and prediction) pooling — the authors show that models can localize class-conditional discriminatory motifs without sacrificing (and sometimes improving) predictive performance. The paper evaluates 12 new model variants on 85 UCR datasets and a new synthetic dataset (WeeklyAnomalies) designed for ground-truth interpretability evaluation.

## Strengths

- **Novel integration of MIL with TSC achieves inherent interpretability without accuracy loss**: The paper proposes a general framework that upgrades DL TSC backbones to produce built-in per-time-point explanations. On 85 UCR datasets (Table 2), the best MILLET model (PADD InceptionTime) achieves the highest balanced accuracy (0.834, rank 5.182), improving over the GAP baseline (0.832, rank 5.494) while remaining competitive with SOTA methods like Hydra-MR and HC2. This supports the core claim that inherent interpretability can be gained without harming predictive performance.

- **PADD pooling is a genuine methodological contribution**: The proposed PADD (parallel attention and prediction) pooling performs attention and classification independently on time point embeddings, then scales predictions by attention weights. Averaged across backbones on UCR data (Section 5.1), PADD raises accuracy from 0.841 (GAP) to 0.846 ± 0.009 and yields the best AOPCR (6.00 vs. GAP's 5.71). The parallel design ensures the classifier cannot rely on the attention head to warp the feature space, which is a principled improvement over sequential ADD pooling.

- **Synthetic dataset enables rigorous ground-truth interpretability evaluation**: The WeeklyAnomalies dataset (10 classes, 1008-length time series with known motif locations) provides a reproducible benchmark. On this dataset, MILLET achieves substantially better AOPCR (17.53 vs. CAM's 15.42 and SHAP's −0.69) and NDCG@n (0.612 vs. CAM's 0.607 and SHAP's 0.266), while being >800× faster than SHAP. This directly validates that the explanations correspond to actual class-conditional motifs.

- **Single-forward-pass explanations are dramatically more efficient than post-hoc methods**: MILLET produces interpretations inherently during inference (one forward pass). The paper reports >800× speedup over SHAP and contrasts favorably with perturbation methods requiring 100+ forward passes (Section 2), which is critical for practical deployment.

## Weaknesses

### Fatal
None.

### Major

1. **Missing ablation: enhancements are confounded with the pooling method in the comparison with GAP baselines.** The paper introduces three enhancements — positional encoding, replicate padding, and dropout (Section 3.4) — that are applied to the MILLET models but not to the GAP baselines. Since the GAP baselines use zero padding and no positional encoding or dropout, the reported performance differences (e.g., accuracy improvement from 0.850 to 0.874 on the synthetic dataset) cannot be attributed solely to the MIL pooling method. The term "plug-and-play" (used multiple times) is misleading in this context because the comparison is between models that differ in more than just the pooling operation. The paper would be substantially strengthened by an ablation that applies the enhancements to GAP baselines as well, or at least isolates the effect of the pooling method alone (e.g., GAP + positional encoding + replicate padding + dropout vs. MIL + same enhancements).

### Minor

1. **The UCR interpretability evaluation measures model-centric faithfulness rather than ground-truth motif localization.** On the 85 UCR datasets, interpretability is assessed exclusively via AOPCR, which measures how quickly predictions change when the model's own most-attributed points are removed. This tells you whether the model is sensitive to the points it highlights, but not whether those points correspond to true class-conditional motifs. The paper is transparent about this limitation (ground-truth labels do not exist on UCR) and the synthetic dataset is designed to fill this gap. However, the abstract's phrasing ("higher quality than other well-known interpretability methods") conflates the two kinds of quality across the two evaluation settings. The paper would be stronger with a brief, explicit acknowledgment that on UCR, the interpretability claim is limited to *model-centric faithfulness* rather than *ground-truth motif localization*.

2. **The ResNet ensemble's puzzling interpretability behavior is noted but not discussed.** The Pareto plot (Figure in Section 5.2) shows that MILLET dominates GAP for FCN and InceptionTime but not ResNet. The paper notes that MILLET gives better interpretability than GAP for individual ResNet models but "struggles with the ensemble ResNet models." This is an interesting finding that invites speculation (e.g., ensembling may smooth out sparse attention patterns) but receives none. A brief discussion would improve the paper's depth.

3. **The "conjunctive additive" (PADD) name is non-standard and the analogy is imprecise.** The term *conjunctive* suggests a logical AND operation, but the mechanism is a product of attention weights and class predictions. The name is defined in the text, but the gap between the intuitive reading and the actual mechanism may confuse readers. Clarifying the motivation more directly (rather than relying on the name to do the work) would help.

### Trivial
None.

## Nice-to-Haves

- **Failure-case analysis on UCR**: Are there specific UCR datasets where MILLET's AOPCR is worse than GAP's? Characterizing those datasets (length, number of classes, noise) would help practitioners decide when to use the framework.
- **Comparison with a shapelet-based interpretable TSC method** (e.g., Learning Time-Series Shapelets) on a subset of UCR datasets would substantiate the claim that MILLET provides "higher quality" explanations relative to the state of the art in *inherently interpretable* TSC, not just relative to post-hoc methods. However, the paper's scope is explicitly DL-based TSC, so this is a desideratum rather than a flaw.
- **Exploration of sparsity tunability**: The paper honestly notes that MILLET's sparsity sometimes misses parts of the discriminatory region (e.g., the middle of the Cutoff signature). A sparsity regularizer on attention weights could allow practitioners to control this trade-off.

## Removed Points

These points were raised by reviewers but are inaccurate, misinterpret the paper, or fail hard rules, and are excluded from the main review:

- **"SHAP comparison is unfair / inflates the significance of the comparison"** — The paper does not claim MILLET is intrinsically superior to SHAP; it demonstrates that SHAP with default settings is impractical and ineffective on 1008-length time series (negative AOPCR). This is a valid empirical finding that motivates the need for inherent interpretability and is not framed as a head-to-head method comparison. The paper is transparent about using SHAP with 500 samples. This criticism misreads the paper's intent.

- **"First comprehensive analysis / first to apply MIL to TSC overclaims novelty"** — The paper explicitly acknowledges prior domain-specific MIL-for-TSC work (Section 2: "earlier work focused on domain-specific problems..."). The claims are qualified ("in a more general sense," "comprehensive analysis," "to the best of our knowledge"). Given the explicit citation of prior work, these claims are reasonable.

- **"Missing related works / missing comparison with Matrix Profile"** — The paper scopes itself to DL TSC methods and cites Matrix Profile as having inherent interpretability. It is not required to compare against every interpretable TSC method to validate its contribution.

- **"Discussion of attention faithfulness literature (Jain & Wallace 2019) is missing"** — The paper validates explanations via synthetic ground-truth data (NDCG@n) and AOPCR, which addresses the faithfulness question directly. Citing specific attention faithfulness literature is a reasonable suggestion but not a weakness, as the paper already provides empirical validation.

- **"Missing ablations for the three enhancements"** — This is already in the main review as a Major weakness, but the specific phrasing "the paper cannot attribute the observed improvements specifically to the MIL pooling" overstates: the improvements are small (0.841→0.846 on UCR), and even in the worst case (all improvement from enhancements), the core claim that MIL provides inherent interpretability without hurting performance still holds. The concern is real and present, but reframed as a methodological gap rather than a fatal attribution error.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a genuine methodological concern (the confounded comparison with GAP baselines) but do not independently advance understanding of MIL or TSC beyond what the paper itself provides.

## Suggestions

1. **Run an ablation study** that applies the three enhancements (positional encoding, replicate padding, dropout) to the GAP baselines, producing a set of GAP+ models. This isolates the effect of the MIL pooling method from the effect of the enhancements, directly addressing the most serious weakness. If the GAP+ models match or approach MILLET's performance, the contribution is primarily from the enhancements; if MILLET still outperforms GAP+, the MIL pooling is the driver. Either outcome is informative.

2. **Tighten the abstract's phrasing** to distinguish between interpretability claims supported by ground-truth evaluation (synthetic dataset) and those supported by model-centric faithfulness (UCR). For example: "On our synthetic dataset with known motifs, MILLET explanations match ground truth better than CAM and SHAP; on 85 UCR datasets, MILLET yields AOPCR scores indicating higher prediction sensitivity to its highlighted regions compared to GAP."

3. **Briefly discuss why the ResNet ensemble hurts interpretability** in the Pareto analysis. Even a well-motivated speculation would improve the paper's depth.

4. **Add a small number of failure-case examples** on UCR where MILLET's AOPCR is worse than GAP's, with a characterization of those datasets.

## Score and Decision

The paper presents a solid contribution: a practical framework for making DL TSC models inherently interpretable, a novel pooling method (PADD), a useful synthetic benchmark, and extensive evaluation on 85 UCR datasets. The main weakness — the confound between the pooling method and the three auxiliary enhancements in the comparison with GAP baselines — is significant but fixable with additional experiments, and does not threaten the paper's core thesis that MIL-based pooling can provide interpretability without sacrificing performance. The paper is clearly written, the empirical scope is large, and the framework has practical value. I recommend acceptance conditional on the authors addressing the ablation concern.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>