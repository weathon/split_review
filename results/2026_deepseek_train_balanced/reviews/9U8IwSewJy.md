## Summary

This paper proposes MoQT, a transformer-based architecture for Camouflaged Instance Segmentation (CIS) with two key components: (1) a Frequency Enhancement Feature Extractor (FEFE) that leverages Fourier phase/amplitude decomposition to enhance contours and suppress color interference, and (2) a Mixture-of-Queries Decoder (MoQ Decoder) that uses multiple groups of queries (called "experts") combined via a gating network for hierarchical mask refinement. The method achieves consistent improvements over prior CIS-specific methods: +2.69% AP on COD10K and +1.93% AP on NC4K.

## Strengths

- **Clear and consistent empirical gains over prior CIS-specific methods.** On COD10K, MoQT achieves 51.77% AP₇₅ — 4.27% above DCNet — and these gains hold across AP, AP₅₀, and AP₇₅ on both COD10K and NC4K (Table 1). The improvements are corroborated by multiple backbone configurations (ResNet-50/101, Swin-Tiny/Small in Table 3), showing the method is robust to backbone choice.

- **Principled frequency-domain motivation grounded in the nature of camouflage.** The paper identifies that Fourier phase preserves contour/high-level semantics while amplitude preserves color/low-level statistics, demonstrates this visually (Figure 1), and then operationalizes this insight through dedicated Contour Enhancement (CEM) and Color Removal (CRM) modules. This gives the method a clearer scientific motivation than prior CIS approaches that treat feature extraction as a black box.

- **Systematic ablation of design choices.** The paper ablates the number of queries per expert (Figure 5), number of decoder layers (Table 4), multiple backbones (Table 3), and loss hyperparameters (Figure 6). The ablation in Table 2 confirms that both FEFE and MoQ individually contribute to performance, with removing MoQ causing a 2.23% AP drop on COD10K.

## Weaknesses

### Fatal
None.

### Major

- **The ablation of the MoQ Decoder does not control for query count or parameter count.** When the MoQ Decoder is removed (Table 2), it is unclear what replaces it — specifically, how many queries the ablated version uses. The MoQ Decoder processes M×N queries per layer (M expert groups of size N), which is M times more than a standard decoder. Without controlling for total query count, the reported gains from MoQ could be partially or entirely due to having more queries/parameters rather than the mixture mechanism itself. A proper control would compare MoQ against a standard transformer decoder with the *same total number of queries* and similar parameter count.

- **The MoQ Decoder's connection to Mixture-of-Experts is superficial and may mislead readers about the nature of the mechanism.** The paper invokes MoE twice ("according to the success of MoE," "benefiting from the success of MoE") and uses the term "expert" for query groups. However, the mechanism differs from MoE in critical ways: (a) the "experts" are newly randomly initialized and discarded each decoder layer, accumulating no learned specialization across layers; (b) the combination uses dense softmax weighting (not sparse top-k routing); and (c) the gating weight is a single scalar per expert applied identically to all N queries within that expert, rather than per-input routing. The actual operation is a learned weighted average of the decoder output and randomly initialized query sets conditioned on pixel decoder features. This is closer to a learned residual connection with noise injection than to MoE. The paper would benefit from describing the mechanism directly rather than relying on the MoE analogy.

### Minor

- **The default value of M (number of expert groups) is never stated.** The paper defines M experts throughout Section 3.3 but never specifies the value used in experiments. This is a critical architectural hyperparameter that determines the cost and behavior of MoQ.

- **No analysis demonstrating that FEFE actually removes color or enhances contours.** The paper motivates CRM and CEM based on Fourier principles but provides no feature-map visualizations or quantitative analysis showing that the modules suppress color-corrupted regions or amplify contour information. Without such analysis, the mechanism's claimed function is asserted but not verified. Additionally, the CRM uses a global vector F_color ∈ ℝ^C to modulate all spatial locations identically, which seems too coarse for spatially varying color interference.

- **Training details are absent from the main text.** Section 4.1 specifies datasets and metrics but provides no optimizer, learning rate schedule, batch size, number of epochs, weight decay, image resolution, or data augmentation. While some of these may appear in a stripped appendix, the main text as presented is insufficient for reproducibility.

- **The abstract's claim of outperforming "18 state-of-the-art CIS approaches" is imprecise.** The paper actually compares against 5 CIS-specific methods and 13 generic instance segmentation methods. The 13 generic methods (Mask R-CNN, YOLACT, etc.) are standard tools applied to CIS data, not "CIS approaches." The meaningful comparison is against the 5 CIS-specific methods where gains are demonstrated, and the paper should frame its results accordingly.

### Trivial
None.

## Nice-to-Haves

- Report the default value of M and provide a brief analysis of gating behavior (e.g., do different experts specialize in different camouflage types? Are gating weights non-uniform across experts?)
- Include inference speed or FLOPs to contextualize the computational cost of the MoQ mechanism (which processes M×N queries per layer).
- Report statistical significance or confidence intervals for the main results.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Table 1 is an image":** Parser artifact — tables in the original submission are rendered as figures by the extraction process. Not a paper issue.
- **"No indication generic methods were adapted for CIS — making them weaker baselines by design":** The paper controls for backbone (ResNet-50) and follows the standard evaluation protocol from prior CIS work. The core comparison is against 5 CIS-specific methods where the paper shows clear gains. The generic methods are supplementary. The framing criticism (merged above) is retained; the stronger claim about unfair comparison is removed as overblown.
- **"The mapping from Fourier observation to CRM/CEM design is not explained":** The paper does explain the conceptual link (amplitude→color→CRM, phase→contour→CEM). The specific implementation choices could be better justified, but this is not a weakness, it is a depth-of-presentation preference.
- **"Random queries add no value that a standard decoder with more queries couldn't achieve":** This is speculation; the ablation empirically shows MoQ contributes. The controlled-ablation concern (retained above) addresses the proper testing methodology.

## Novel Insights

None beyond the paper's own contributions. The reviewers did not surface an insight about the method or problem that the paper itself does not already articulate.

## Suggestions

1. **Run a controlled ablation** comparing the MoQ Decoder against a standard transformer decoder with the same total number of queries (M×N) and similar parameter count. Report whether the gain persists.
2. **Specify the default value of M** (number of expert groups) in the main experimental setup.
3. **Add feature-map visualizations** showing the effect of CRM and CEM on intermediate representations, to verify that color is suppressed and contours are enhanced as claimed.
4. **Frame the results more precisely** in the abstract: distinguish between "5 CIS-specific methods" and "13 generic instance segmentation methods" rather than lumping all 18 as "CIS approaches."

## Score and Decision

This paper addresses a challenging and relevant task with a method that has a principled motivation (frequency-domain feature enhancement) and shows clear empirical gains over prior CIS-specific work. The core results are credible and the ablation confirms both components contribute. However, the paper has two real issues that prevent it from meeting ICLR's high bar in its current form: (1) the MoQ ablation does not control for the trivial confound of increased query count, so the claimed advantage of the mixture mechanism over simply having more queries is not established, and (2) the MoE/MoQ framing overstates the connection to a well-known architecture paradigm. These are addressable in revision, and I encourage the authors to do so.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>