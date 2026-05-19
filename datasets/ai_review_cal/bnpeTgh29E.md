- Decision: Reject
- Avg Score: 3.75
- Scores: 3, 3, 6, 3
Now I have all the information I need. Let me produce the final consolidated review.

## Summary

The paper proposes SDA-Net, a framework for fine-grained semantic segmentation that addresses intra-domain (soft domain) gaps. It divides a single domain into sub-domains based on object density, uses a sub-domain classifier to identify the sub-domain of an input, and fine-tunes a baseline network with two novel loss functions (sieve loss and fine-tuning loss). Experiments on four datasets (WHU, BDD100K, GTA5, ADE20K) report mIoU improvements of +3.6% to +6.7% over state-of-the-art baselines.

## Strengths

- **Novel problem identification with concrete evidence of the phenomenon**: Section 2.1 uses t-SNE and DBSCAN clustering on the LoveDA dataset to discover three sub-domains, and Table 1 quantifies performance degradation from cross-sub-domain training/test splits. This demonstrates a real problem that standard domain adaptation methods do not address.

- **Significant and consistent accuracy gains across diverse benchmarks**: Table 7 reports mIoU improvements over strong baselines (InternImage, LoveDA, Segmenter, etc.) of +6.7% on WHU, +3.6% on BDD100K, +5.1% on GTA5, and +4.8% on ADE20K, with standard deviations reported. The gains span aerial imagery, autonomous driving, and scene parsing.

- **Ablation confirms individual contribution of both novel losses**: Table 5 shows that removing either sieve loss (ℒ_SV) or fine-tuning loss (ℒ_FT) degrades mIoU on all four datasets, with the full combination yielding the highest values.

- **Balanced per-category performance demonstrated**: Figure 7 and Table 8 show that SDA-Net delivers more uniform mIoU across categories compared to CCNet and InternImage, suggesting robustness to density variation within a domain.

## Weaknesses

### Fatal
None.

### Major

- **FT-loss formulation appears computationally infeasible for inference-time fine-tuning as described**. Equation 8 defines the FT-loss as \( \mathcal{L}_{\text{CE-S}}(\mathcal{C}^{\theta_{\text{BN}}}; D_i^c(\mathbb{X})) - \mathcal{L}_{\text{CE-S}}(\mathcal{C}^{\theta_{\text{BN}}}; D_{\text{all}}^c(\mathbb{X}) - D_i^c(\mathbb{X})) \). The negative term requires computing cross-entropy loss over the complement of the sub-domain within the full training set. Algorithm 2 places this inside a per-test-sample fine-tuning loop of up to 10 epochs, with the gradient term \( \nabla_{\theta_{\text{SDC}}} \mathcal{L}_{\text{FT}}(\mathcal{C}^{\theta_{\text{BN}}}; \mathbb{X}) \) referencing the full training set \( \mathbb{X} \). Yet Table 6 reports SDA-Net prediction time as 172ms vs. 162ms for CCNet — a difference far too small to accommodate per-sample fine-tuning over the entire training dataset. The paper does not explain how this is reconciled, nor whether the reported times include or exclude fine-tuning. This is a structural inconsistency that undermines the practical validity of the claimed framework.

- **Missing ablation that isolates the effect of sub-domain splitting from the fine-tuning mechanism**. The ablation study (Table 5) removes the loss functions but never removes the sub-domain classifier itself. A critical baseline is missing: SDA-Net with a single domain (i.e., same architecture, same fine-tuning procedure with both losses, but no sub-domain classification). Without this, the reported gains cannot be attributed to sub-domain awareness as opposed to the fine-tuning procedure or increased model capacity from the SDC parameters. Table 4 varies the *number* of sub-domains, which partially addresses this, but a single-domain version of the full system (including both losses) is needed.

- **Disconnect between the motivating preliminary study and the actual sub-domain definition**. Section 2.1 uses unsupervised clustering (t-SNE + DBSCAN) to discover sub-domains in LoveDA. Section 2.2 then defines sub-domains by density thresholds (Eq. 1: \( D_i^c(\mathbb{X}) = \{\mathcal{X} \mid \frac{i}{N} \leq d^c(\mathcal{X}) < \frac{i+1}{N}\} \)). The paper never establishes that the DBSCAN clusters correspond to density-based splits, nor that density is the attribute driving the intra-domain gap observed in Table 1. The method and the motivation are thus misaligned: the problem is demonstrated via clustering, but solved via density partitioning, without evidence that these are the same phenomenon.

- **Ensemble baseline mentioned but never compared**. The paper motivates SDA-Net by contrasting it with an ensemble of sub-domain-specific models (Eq. 4), stating that ensembles are memory-inefficient. However, no experiment compares SDA-Net to such an ensemble. A direct comparison would clarify whether SDA-Net achieves the claimed efficiency-accuracy trade-off relative to the natural alternative.

### Minor

- **Sieve loss formulation is incomplete and the mechanism is underspecified**. Equation 6 writes the Gaussian integral as \( \int_{-\infty} \frac{1}{\sqrt{2\pi}} e^{-\frac{x^2}{2}} dx \) without an upper bound, making the expression formally undefined. The paper states that "prior work reported that the ρ_E extracts the ratio of the attention area" without explaining how this maps to the cumulative product of Gaussian CDF values, or how the loss backpropagates through the activation thresholds. While the general idea (matching activation ratios to density predictions) is plausible, the formulation needs to be complete and self-contained.

- **Paper does not clarify whether "CCNet" as a standalone baseline uses the same configuration as the CCNet inside SDA-Net**. The paper states "CCNet was used as the Baseline-Network for SDA-Net" and separately reports CCNet as a baseline in Table 7. It is not explicitly stated whether both use the same backbone, training protocol, and DeepLabV3 head. Minor clarification needed.

- **Sieve loss and fine-tuning loss terms in Algorithm 2 show ∇θ_SDC where the text says only BN is fine-tuned**. Algorithm 2 lists ∇θ_SDC for the ℒ_SV and ℒ_FT terms, but the text explicitly states "only BN is fine-tuned" (Section 3.3). This is either a notation error or a genuine contradiction that needs resolution.

### Trivial
None.

## Nice-to-Haves

- Comparison against the ensemble model (Eq. 4) to validate the claimed efficiency advantage.
- Discussion of limitations: cases where density may not be a good proxy for sub-domains (e.g., multi-class scenes where different objects have different density distributions).
- Clarification on whether the number of sub-domains is fixed a priori or automatically determined, and whether density thresholds are dataset-dependent.

## Removed Points

- *"The +12.6% average improvement over vanilla models is suspiciously large"* — Removed as speculative; the paper quantifies this as improvement over U-Net and CCNet baselines, and the per-dataset gains are reported. Without access to the numerical table to verify, this assertion is not grounded.
- *"No statistical significance is reported"* — Removed as factually incorrect. Table 7 caption states "Results were measured in terms of mIoU and standard deviation values."
- *"Missing appendix, missing proofs in appendix, or absent references"* — Removed per instruction that parser strips these; they exist in the original submission.
- *"All models trained at 256×256 may disproportionately harm large models"* — Removed as a generic criticism; consistent resolution across all models is standard practice for fair comparison.
- *"The number of sub-domains for each dataset is not specified"* — Table 7 specifies "SDA-Net with ten sub-domains," so this is specified.
- Strength Finder strength 2 ("Sieve loss enables efficient fine-tuning") — Retained but with caveat reflected in Major weakness 1 (the FT-loss, not sieve loss, is the efficiency concern). The sieve loss itself (updating only 𝒜(θ_BN)) is a real efficiency design choice; this strength is partially supported.

## Novel Insights

The harsh critic's observation about the FT-loss requiring full training set access at inference (Major weakness 1) is the most significant novel insight — it is subtle and not obvious from a casual reading, but verifiable from Equations 8 and Algorithm 2. This issue is distinct from standard reproducibility nitpicks; it goes to whether the method can work as claimed. The critic's catch that the ablation study never removes the sub-domain classifier (Major weakness 3) is also insightful: it exposes a logical gap where the headline claim ("sub-domain awareness improves performance") is not disentangled from the fine-tuning machinery.

## Suggestions

1. **Clarify the FT-loss computation pipeline**: State explicitly whether fine-tuning happens per-test-sample, per-sub-domain as a pre-processing step, or offline. If it uses the full training set, report the actual wall-clock time including this step. Consider reformulating the FT-loss to avoid dependence on the full training set (e.g., pre-computing the negative term or using a representative subset).
2. **Add a single-domain ablation**: Compare SDA-Net with k=1 sub-domain (no sub-domain classification) using the same fine-tuning procedure with both losses, to isolate the effect of sub-domain splitting from fine-tuning.
3. **Align the sub-domain definition with the preliminary study**: Either show that DBSCAN clusters correspond to density ranges, or use the clustering directly to define sub-domains. Otherwise, the problem diagnosis and solution are decoupled.
4. **Fix the sieve loss formulation**: Provide the complete integral with proper bounds and explain the differentiability and optimization path.
5. **Add an ensemble baseline**: Compare SDA-Net against an ensemble of sub-domain-specific models (as described in Eq. 4) to validate the efficiency claim.
6. **Fix the notational inconsistency in Algorithm 2**: Clarify whether ∇θ_SDC or ∇θ_BN is intended for the sieve loss and FT-loss gradient terms.
