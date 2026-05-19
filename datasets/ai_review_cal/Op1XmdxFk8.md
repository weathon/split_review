- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 5, 5, 6
Now I have a complete picture of the paper and can evaluate all claims against the actual content. Let me produce the consolidated review.

## Summary

This paper identifies a "granularity gap" in transfer learning for fine-grained tasks, where pre-trained features contain excessive non-discriminative information that hinders learning of fine-grained class-discriminative details. The authors propose ProtoReg, a regularization method that initializes class-discriminative prototypes (via class-wise feature mean or linear probing weights), refines them during training, and enforces feature aggregation toward correct prototypes while separating from incorrect ones. The method achieves substantial improvements over standard fine-tuning and prior transfer learning regularizers on four fine-grained benchmarks (6.4% average gain, 13.4% in limited-data scenarios) and demonstrates OOD robustness on Waterbirds.

## Strengths

- **Large and consistent performance gains across benchmarks.** ProtoReg outperforms all compared methods (L2-SP, BSS, SN, Co-tuning, LP-FT, Robust FT, DR-Tune) across every dataset and sampling rate. The gains are substantial (e.g., +9.18% over the best compared method on FGVC Aircraft at 100% sampling; +8.73% on Stanford Cars at 15% sampling), directly validating that prioritizing discriminative information effectively addresses the granularity gap.

- **Strong evidence of learning class-discriminative representations.** CKA similarity analysis (Figure 4) shows ProtoReg induces substantial representation changes in intermediate layers, unlike CE which primarily modifies only the penultimate layer. This empirically supports that ProtoReg acquires new fine-grained discriminative information beyond what the pre-trained model provides.

- **Thorough ablation study validates each component.** Table 4 isolates the contribution of each design choice: aggregation loss (+4.92%), prototype refinement (+8.70%), and separation loss (+9.24%) all provide meaningful improvements, and the full combination yields the best result. The stage-wise analysis (Table 3) further confirms that early-stage regularization is critical.

- **OOD robustness on Waterbirds.** The model fine-tuned with ProtoReg shows a significantly smaller accuracy drop on Waterbirds (10% at 100% sampling vs. 24% for CE; 19% at 15% sampling vs. 49% for CE), demonstrating reduced reliance on spurious background correlations.

- **Clear problem motivation.** Section 3 provides concrete evidence of the granularity gap through t-SNE visualizations (Figure 2) and image retrieval examples (Figure 1), showing that pre-trained features are not linearly separable for fine-grained classes and that CE fine-tuning alone fails to capture discriminative features.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Waterbirds evaluation protocol could be more explicit.** The paper evaluates a 200-way CUB-trained model on the Waterbirds test set and reports "test accuracy." While the natural interpretation is 200-way top-1 accuracy using the CUB species labels preserved in Waterbirds, the paper does not explicitly state this. Given that the standard Waterbirds benchmark is commonly framed as binary (waterbird vs. landbird), a one-sentence clarification of the label mapping and metric would eliminate ambiguity. This does not affect the validity of the results but is a presentation gap.

- **Hyperparameter values for λ_aggr and λ_sep across datasets are not stated.** Figure 5 shows a sensitivity grid on FGVC Aircraft, but the paper does not specify whether the same λ values are used across all datasets or tuned per dataset. This is a minor reproducibility gap.

- **Memory and time overhead not discussed.** The self variant stores features for all training samples per epoch in class-wise memory banks. For large datasets or high-dimensional features, this introduces non-trivial storage and computational cost. A brief note on overhead would help practitioners assess trade-offs.

### Trivial
None.

## Nice-to-Haves

- A brief practical guideline on when to use ProtoReg (self) vs. ProtoReg (LP) would strengthen the paper's utility. (self) avoids the linear probing step and is simpler; (LP) generally performs better but requires an extra tuning stage. The paper already provides the empirical comparison but no guidance.
- The paper could briefly note that baseline methods were tuned following the same protocol (it states it adopts the protocol of Kou et al., 2020 and You et al., 2020, which is sufficient but could be more explicit).

## Removed Points

- **Baseline tuning fairness concern (from Harsh Critic):** The critic questions whether baselines were tuned fairly given the large gains. The paper explicitly states it adopts the evaluation protocol of prior studies (Kou et al., 2020; You et al., 2020), which is standard practice. The concern is speculative with no evidence of unfair comparison. **Removed** as unsubstantiated.

- **"Waterbirds results cannot be interpreted" (from Harsh Critic):** The critic asserts the Waterbirds protocol is so ambiguous that results cannot be interpreted. The paper clearly states the model is trained on CUB-200-2011 and evaluated on Waterbirds, which consists of CUB-200-2011 images with backgrounds replaced. The species labels are preserved by construction, making "test accuracy" naturally interpretable as 200-way top-1 accuracy. **Demoted to Minor** (the paper could be more explicit, but the results are interpretable as-is).

- **Generic areas-of-concern sweep (from Harsh Critic):** The critic raises questions about data splits, hyperparameter selection for each baseline, and method-specific hyperparameter re-tuning. These are category-driven probes, not specific identified problems. **Removed** as speculative.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a new perspective on the method not already present in the paper.

## Suggestions

1. Add a sentence clarifying the Waterbirds evaluation: "We evaluate 200-way top-1 classification accuracy using the CUB-200-2011 species labels that are preserved in the Waterbirds dataset."
2. State the λ_aggr and λ_sep values used for each dataset (or state explicitly that they are fixed across all experiments).
3. Add a brief note on computational overhead (memory bank size and wall-clock time comparison with CE fine-tuning).
