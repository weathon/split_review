## Summary

This paper introduces Multimodal Iterative Adaptation (MIA), a gradient-based meta-learning framework for Implicit Neural Representations (INRs) that enables independent unimodal learners to exchange state information (parameters and gradients) via meta-learned State Fusion Transformers (SFTs). SFTs comprise Unimodal SFTs (model intra-modal dependencies), Multimodal SFTs (capture cross-modal interactions), and Fusion MLPs (integrate both). The method is evaluated on four multimodal regression tasks (1D synthetic, CelebA images, ERA5 climate, AV-MNIST) and consistently outperforms both unimodal baselines (CAVIA, MetaSGD, GAP, ALFA) and multimodal encoder-based methods (MTNPs, Encoder), often by wide margins.

## Strengths

- **Consistent and substantial improvement across diverse multimodal tasks.** MIA achieves the lowest MSE in every modality and sampling-ratio range across all four datasets (Tables 1–4). For example, on CelebA (Table 2) MIA achieves 4.47 (×10⁻³) at R<0.02 versus 7.84 for the next best; on AV-MNIST audio (Table 4) MIA scores 27.32 (×10⁻⁴) versus 31.13. The trend is clear, repeated, and not cherry-picked.

- **Well-motivated and technically sound architecture.** The three-component SFT design (USFTs → MSFTs → Fusion MLPs) is principled and the ablation (Table 5a, despite the dataset-identification issue below) supports the distinct roles of each component: USFTs specialize in memorization, MSFTs in generalization, and Fusion MLPs combine both for best overall performance.

- **Diagnostic analysis connects mechanism to behavior.** The analysis in Section 5.5 (Figure 5) shows that increasing multimodal support set sizes consistently improves target-modality performance, especially when target data is scarce, providing direct evidence that the method correctly identifies and exploits cross-modal interactions.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **The ablation study (Table 5a) does not state which dataset produced the results.** The text says "averaged across the modalities" (Section 5.5) but never names the dataset(s). Since the ablation disentangling USFTs, MSFTs, and Fusion MLPs is central to the paper's architectural claims, and since relative error reductions (+19.2%, +29.4%) could vary substantially across data types, the reader cannot judge how generalizable these component attributions are. This is not a fatal issue—the pattern is consistent with the overall method's logic—but it is a significant omission in reporting rigor.

- **The headline quantitative claim ("at least 61.4% and 81.6% error reduction") in the Introduction (line 33) is not explicitly traceable to any specific table or aggregation.** While the experimental tables clearly show large improvements, a reader cannot determine which baselines, which modalities, or which sampling-ratio ranges produce these particular minima. Adding a sentence that anchors these numbers (e.g., "across all datasets and sampling ratios, the minimum improvement observed was…") would resolve this.

- **No variance estimates reported for the 5-seed averages in the main tables.** The tables note "averaged over 5 random seeds" but report no standard deviations, confidence intervals, or any measure of variability. Without error bars, the reliability of the reported improvements—however large—cannot be assessed. This is a standard expectation for experimental papers.

- **The sampling-ratio ranges for AV-MNIST (Section 5.4) are asymmetric without justification.** Images use [0.001, 1.000] while audios use [0.250, 1.000]. The paper offers no rationale for this choice. Since audio can never receive fewer than 25% of its total samples, methods with cross-modal transfer (like MIA) could be systematically advantaged if image-derived features compensate for the lack of low-support audio conditions. An ablation with a matched range or a clear justification would strengthen confidence in the results.

- **Key architectural hyperparameters are not specified in the main text.** The paper mentions L₁ (USFT depth), L₂ (MSFT depth), hidden dimensions D_z, learning rates, and other details only as symbols; their actual values are absent from the main text. While the appendix likely contains them (and the parser may have stripped parts), a brief summary in the main text would aid readability.

### Trivial

None.

## Nice-to-Haves

- **Discussion of missing modalities at test time.** The framework assumes all modalities are available for every sample during both training and testing. Real-world multimodal data often have missing channels; acknowledging this limitation would strengthen credibility.
- **Computational cost analysis.** The paper does not report wall-time per inner step, total parameter increase from the SFT modules, or memory overhead. For a method that adds transformer blocks and Fusion MLPs, this is relevant for practical adoption.
- **A matched-range experiment on AV-MNIST.** Running an ablation with both modalities using the same [0.001, 1.000] range would address the asymmetry concern definitively.

## Removed Points

- **Criticism that Table 9 (correlation analysis) "cannot be examined."** This table is in the appendix, which the parser strips from all papers. The weakness is a parser artifact, not an author error.
- **Complaint that the abstract declares specific percentages "61.4% and 81.6%."** The abstract uses the phrase "substantial enhancements" (line 14); the specific numbers appear in the Introduction (line 33). The reviewer mislocated them. The substance (traceability) is kept as a Minor weakness above; the location error is corrected.
- **"The paper should cover more tasks / domains"** type criticisms. The paper already covers four diverse multimodal settings (synthetic, vision, climate, audiovisual) which is adequate for a methods paper.
- **Criticism that "the dimensions of state representations are not discussed for the case where modalities have different context-parameter sizes."** The paper explicitly mentions projection MLPs to a common dimension D_z (line 99), which handles this case. This is a non-issue.
- **"Final paragraph of the Introduction already states the figures"** — this duplicates the traceability point already kept above.

## Novel Insights

The reviewers collectively recognize that the paper's core contribution—using cross-modal state fusion (parameters + gradients) via transformers to iteratively guide INR learners—is genuinely novel and well-executed. The consistent gains across four very different multimodal settings, combined with the diagnostic evidence that MSFT attention correlates with gradient quality, provide credible mechanistic support for the approach. The main weaknesses are in reporting rigor (dataset labeling, variance, hyperparameter disclosure, claim traceability), not in the method's validity or the quality of the contribution. No reviewer has identified a flaw that would invalidate the central claim.

## Suggestions

1. **Label the ablation dataset explicitly** in Table 5's caption and text. Better yet, run the ablation on two datasets (e.g., CelebA and ERA5) and report both.
2. **Add a traceability sentence** for the 61.4%/81.6% claim: identify which baseline(s), modality/modalities, and sampling ratio(s) produce these minima, or drop the exact numbers in favor of qualitative language.
3. **Add standard deviations** (or ± ranges) to Tables 1–4. Even a brief footnote stating "standard deviations across seeds were below X% of the mean" would help.
4. **Justify or remove the AV-MNIST range asymmetry** with a brief rationale, or include a matched-range experiment in the supplement.
5. **Summarize key hyperparameters** (L₁, L₂, D_z, learning rates) in the main text with a clear pointer to the appendix for full details.

## Score and Decision

This is a solid paper with a well-motivated method, clean experiments across diverse tasks, and consistent results. The issues identified are about presentation rigor and missing details—none threaten the method's validity or the paper's core contribution. The paper should be accepted after addressing these points.

**Originality:** High — the idea of cross-modal state fusion for INR meta-learning is novel.  
**Importance of question:** High — scarce-data multimodal learning is a practically relevant problem.  
**Claims supported:** Mostly yes, though headline percentages need traceability and ablation needs dataset label.  
**Soundness of experiments:** Solid — comprehensive baselines, diverse tasks, consistent results.  
**Clarity of writing:** Good — the method is clearly explained; some experimental details are deferred.  
**Value to community:** Positive — the framework is general and can be applied to existing INR meta-learners.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>