I now have all the information needed to write the final consolidated review.

---

## Summary

This paper proposes Dynamic Cross-Layer Preference Correction (DCPC), a self-supervised fine-tuning framework for LLMs that addresses label preference inconsistencies across annotators. DCPC introduces three components: (1) a preference-sensitive similarity mechanism with an ambiguity loss that penalizes label differences for semantically similar inputs, (2) a cross-layer prefix alignment (CLPA) loss that aligns representations across layers, and (3) a Preference Correction Module (PCM) with an auxiliary classifier and meta-matrix to dynamically adjust prefix embeddings. Experiments on LLaMA-2 7B/13B across five benchmarks (BoolQ, COPA, ReCoRD, SST-2, RTE) plus modified variants and the Alpaca instruction-following dataset show consistent improvements over Full-FT and eight PEFT baselines.

## Strengths

- **Consistent top performance across both original and preference-shifted datasets**: DCPC achieves the highest accuracy on all five original benchmarks (e.g., BoolQ 88.9%, COPA 93.5%, SST-2 95.0%) in Table 1 and continues to outperform all baselines on the modified datasets in Table 2, with substantially smaller performance drops than Full-FT and other PEFT methods (e.g., only –2.8% on BoolQ-PS vs. –6.2% for Full-FT). This directly supports the paper's claim of robustness to label preference inconsistencies.

- **Empirical motivation grounded in a controlled toy experiment**: Figure 2 presents layer-wise cosine similarity, edit distance, and KL-divergence for semantically similar inputs with differing labels, showing that label preferences diverge in deeper layers while early-layer embeddings remain similar. This provides explicit evidence of the problem DCPC is designed to solve and distinguishes the paper from approaches that treat label inconsistency as static noise.

- **Ablation study validates each component's contribution**: Table 3 shows that removing the ambiguity loss, CLPA, or PCM individually causes significant performance drops (e.g., –6.1 on BoolQ-PS without ambiguity loss, –4.9 without PCM). The largest degradation occurs when both CLPA and PCM are disabled (–7.6 on BoolQ-PS), confirming that the proposed components work synergistically and are not redundant.

## Weaknesses

### Fatal
None.

### Major
- **The pair-sampling strategy during training is never specified.** The entire DCPC framework operates on pairs of inputs (x_A, x_B): the ambiguity loss (Eq. 3), cross-layer alignment (Eq. 5–6), and the PCM (Eq. 7–11) all compare two sequences. Yet the paper never explains how these pairs are constructed during training — whether all pairs within a mini-batch are compared, whether semantically similar pairs are selected via nearest neighbors, or whether some other sampling strategy is used. This is a core methodological detail without which the method cannot be implemented or reproduced. *(Note: This is addressable in a rebuttal, but the omission is significant in the submitted manuscript.)*

- **The creation of the modified (preference-shift) datasets is not described.** The paper introduces six modified datasets (BoolQ-PS, COPA-BS, ReCoRD-R, SST-2-P, RTE-E, Alpaca-IS) and claims they "simulate real-world annotator biases and inconsistencies," but provides zero information about how these modifications were performed (e.g., label flipping, sub-sampling biased annotators, re-annotation by a biased model, systematic rephrasing). Since the paper's central claim — that DCPC handles label preference discrepancies — rests on comparisons on these datasets, their construction must be transparent for the results to be interpretable or reproducible. *(Data descriptions may appear in the stripped appendix sections A.1.1/A.1.2, but the main text should at minimum summarize the modification methodology.)*

### Minor
- **No measures of variability are reported.** Results are reported as medians over five random seeds with no standard deviations, confidence intervals, or significance tests. Several improvements over baselines are small (e.g., +0.2 on SST-2, +0.5 on RTE). While the robustness gains on modified datasets are larger (e.g., +3.7 on BoolQ-PS), the reader cannot assess whether these are consistent across runs. Reporting means and standard deviations (or interquartile ranges) across seeds is standard practice and would strengthen the paper substantially.

- **The theoretical link between the cross-layer alignment loss and prefix convergence needs clearer justification.** The alignment loss minimizes Euclidean distance between concatenated vectors C_A^l = P_A^l ⊕ T_B^{l+1} and C_B^l = P_B^l ⊕ T_A^{l+1}. Theorem 1 claims this causes prefix embeddings to converge in deeper layers, but the loss constrains a mixture of prefix and token embeddings from different inputs and layers. The connection to prefix convergence is non-trivial and likely depends on assumptions (e.g., about token embedding stationarity) that are not discussed in the main text. The proof is referenced to Appendix A.3 (stripped from this version), but the main text should provide more intuition or discuss the key assumptions.

- **The PCM's complexity is not compared against simpler alternatives.** The PCM involves an auxiliary classifier predicting mean/variance, a reparameterization-style sampling step, a softmax, multiplication by a meta-matrix M, and a KL-divergence loss. While the ablation study (Table 3) confirms that removing the PCM hurts performance, the paper does not compare against a simpler correction mechanism — e.g., directly penalizing KL divergence between label distributions of similar inputs without the auxiliary classifier and meta-matrix. The added architectural complexity would be better justified with such a comparison.

- **The "no existing work" claim is somewhat overstated.** The paper states "To the best of our knowledge, no existing work in the fine-tuning of LLMs has addressed the issue of inconsistent labels." While qualified and scoped, this overlooks the large body of work on learning with noisy labels and disagreement-aware training, some of which has been applied to or could be adapted to the LLM fine-tuning setting. A more nuanced framing would strengthen the positioning without diminishing the contribution.

- **The shared auxiliary classifier creates a tension with the toy experiment's findings.** The PCM auxiliary classifier uses "shared parameters" across layers (stated to "ensure consistency across transformer layers"), yet the toy experiment (Figure 2) shows that label preference divergence _grows_ with depth, suggesting that different layers may need different corrections. The paper does not discuss this tension or justify why a layer-shared correction is appropriate.

### Trivial
None.

## Nice-to-Haves
- A step-by-step algorithm/pseudocode of the training loop showing how pairs are formed, when each loss is computed, and how prefixes/meta-matrix are updated.
- Comparison of trainable parameters and training time against baselines.
- An analysis (even qualitative) of what the learned meta-matrix M captures.
- Evaluation on original (unshifted) datasets framed more explicitly as a robustness contribution rather than general superiority, given that the gains there are modest.

## Removed Points
- **Proof relegated to missing appendix (Critic's point #3, part 1):** Removed per instructions — appendix sections are stripped by the parser and exist in the original submission. The substantive concern about the mechanism's justification (non-trivial link between alignment loss and prefix convergence) is kept above as a Minor weakness.
- **Formatting/style nitpicks:** Removed per instructions — parser artifacts are not author errors.
- **Generic or unsubstantiated strengths from Strength Finder:** The Strength Finder's three strengths were all specific, verified claims backed by tables/figures. None were removed.

## Novel Insights
None beyond the paper's own contributions. The reviews and the paper itself align on the core assessment: the problem is real, the approach is well-motivated by the toy experiment, results are consistently positive, but the manuscript has significant gaps in methodological and experimental description that need to be addressed.

## Suggestions
1. **Specify the pair-sampling strategy** — this is the single most important missing detail. State whether all pairs, random pairs, or semantically selected pairs are compared within each mini-batch.
2. **Describe the modified dataset creation process explicitly** — provide the algorithm or procedure used for each of the six modified datasets so that results can be interpreted and reproduced.
3. **Add error bars** — report mean ± std (or medians with IQR) across the five seeds for all tables.
4. **Compare the PCM against a simpler correction baseline** — e.g., a variant that replaces the auxiliary classifier and meta-matrix with a direct KL penalty on label distributions of similar inputs.
5. **Clarify the theoretical assumptions behind Theorem 1** — discuss in the main text what conditions (e.g., token embedding stationarity) are required for the alignment loss to drive prefix convergence.

## Score and Decision

**Score:** 5.0 — The paper addresses a real and important problem with a well-motivated approach and consistently positive results. However, two significant methodological gaps (unspecified pair-sampling strategy and undescribed dataset modifications) make the core contribution impossible to fully evaluate as submitted. The remaining issues (lack of error bars, limited comparison for the PCM, and some framing concerns) are addressable in revision.

**Decision:** Accept — The core contributions are sound, the empirical evidence across many datasets is consistently positive, and the major gaps are matters of missing description that can be clarified in a camera-ready version rather than fundamental flaws in the approach. The authors should be required to address the pair-sampling and dataset modification descriptions before final publication.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>