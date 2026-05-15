Now I have all the information needed to verify claims against the actual paper. Let me synthesize the final review.

---

## Summary

This paper proposes BaFTA, a backpropagation-free test-time adaptation method for CLIP-based zero-shot classification. Instead of fine-tuning text prompts via gradient descent (as in TPT), BaFTA directly refines class embeddings through online clustering in a projected embedding space, and aggregates predictions from both text-based and clustering-based sources using Rényi entropy weighting. The method achieves consistent improvements over SOTA test-time adaptation methods across 15 datasets while being approximately 5× faster than TPT.

## Strengths

- **Novel backpropagation-free test-time adaptation with 5× speedup.** BaFTA takes 158.7 ms per image (ViT-B/16) versus 873 ms for TPT (Section 5.2), while simultaneously outperforming TPT by +3.17% on ImageNet and +4.65% on OOD average (Table 1). This validates the core efficiency claim.

- **Consistent SOTA results across 15 datasets and two backbones.** BaFTA surpasses TPT, CoOp, PromptAlign, CALIP, and SwapPrompt on nearly all benchmarks. On OOD average with ViT-B/16, BaFTA achieves 65.46% vs. TPT 60.81% and PromptAlign 63.56% (Table 1). On fine-grained average, BaFTA achieves 68.77% vs. TPT 65.10% (Table 2). Gains hold for RN50 as well.

- **Demonstrated superiority of Rényi entropy aggregation over alternatives.** Ablation Table 4 compares seven weighting functions for merging augmented-view predictions. Rényi entropy with α=0.5 achieves 71.00% on ImageNet, outperforming simple averaging (69.43%), max-confidence weighting (70.60%), and TPT's entropy thresholding (70.34%).

- **Transparent ablation study quantifying each component's contribution.** Table 3 isolates the contribution of each component: CLIP multi (63.46%) → BaFTA-TE (66.70%, +3.24%) → full BaFTA (68.11%, +4.65%). The paper honestly reports that BaFTA-OC (clustering alone + Rényi) gives only +0.83%, and that combining TE and OC yields the full benefit.

- **Robustness demonstrated across severe distribution shifts.** On ImageNet-A, BaFTA improves from CLIP multi 49.89% to 63.36% (ViT-B/16), a large gain of 13.47% under adversarial domain shift.

## Weaknesses

### Fatal

None.

### Major

None. The paper's core claims (backpropagation-free adaptation can achieve SOTA with faster inference) are supported by the evidence. The component contributions are honestly presented in the ablation, allowing readers to assess what drives performance.

### Minor

- **Narrative over-emphasizes online clustering as the primary driver of gains.** The paper consistently frames BaFTA as an "online clustering" method, but the ablation (Table 3) shows that clustering alone (BaFTA-OC, +0.83%) contributes much less than the Rényi entropy aggregation applied to text-embedding predictions (BaFTA-TE, +3.24%). The full gain (+4.65%) comes from combining both, with clustering providing a 1.41% increment over BaFTA-TE. The contributions list and introduction lead readers to believe clustering is the central innovation, when the evidence suggests the Rényi aggregation mechanism carries more weight. The authors should reframe to reflect this more accurately.

- **The assignment rule for online clustering is underspecified.** In Section 3.1 (Eq. 4), the update rule uses $y_i$ as the prediction for test example $v_i$, but the paper never explicitly states how $y_i$ is determined in the clustering context. Is it the argmax of cosine similarity to current centroids $\{w_j\}$ (self-training), or the text-embedding classifier, or the aggregated prediction from Section 3.3? This is a meaningful reproducibility gap, as the entire clustering loop depends on this assignment mechanism and potential confirmation bias is a known concern for self-training approaches.

- **Default value of $\beta$ not reported.** Equation 9 introduces $\beta$ as a balancing weight between text-embedding and clustering predictions, but its default value is never stated. This makes the experimental setup incompletely specified.

- **Inconsistency in "negative Rényi Entropy" terminology.** The paper states it uses "negative Rényi Entropy" (line 146) but gives the standard (non-negative) Rényi entropy formula. For the Rényi entropy order used in experiments (α=0.5), the formula yields non-positive values, but the naming and equation disagree in a way that will confuse readers. A clearer explanation of how the quantity is used as a weight (or whether the formula is intentionally negated) is needed.

- **Inclusion of few-shot methods (CoOp, PromptAlign) in main comparisons is not well-justified.** These methods use 16 labeled examples per class on ImageNet and are expected to transfer worse to OOD data. Their inclusion alongside zero-shot test-time methods creates an unbalanced comparison. The paper mentions this follows TPT's convention, but the distinction should be more prominently discussed.

- **SwapPrompt comparison on fine-grained datasets is incomplete.** SwapPrompt has 5 out of 10 entries missing for RN50 (Table 2). The paper notes this is due to different evaluation splits, but the incomplete comparison limits the validity of the average.

### Trivial

- **No error bars or variance estimates.** All results are reported as single numbers without variance over augmentation seeds or initialization randomness. While this is standard practice for large-benchmark evaluations in this subfield, it would strengthen the paper to include at least a sensitivity analysis for key results.

- **No per-dataset breakdown in the component ablation.** Table 3 reports averages over 15 datasets but does not show whether the online clustering helps more on certain dataset types (e.g., fine-grained with many classes vs. coarse-grained).

## Nice-to-Haves

- **Visualization of the projected embedding space** before and after online clustering (e.g., t-SNE of centroids vs. text embeddings vs. visual embeddings) would help build intuition about whether the clustering converges to sensible class centers.
- **Analysis of clustering accuracy over the course of inference** — how do the centroids evolve as more test examples are seen, and are early predictions harmed by poor initialization?
- **Sensitivity analysis for hyperparameters α and β** across multiple datasets to guide practitioners on default choices without validation data.

## Removed Points

*These points are flagged to be removed — treat them with caution.*

- The criticism that the "Ĥ(p^b)" column in Table 4 uses an undefined formula: **removed because the paper does define it** (lines 302-303: $\hat{H}(p^b) = (H^{max} - H(p^b))/H^{max}$). The critic appears to have missed this definition.
- The criticism about missing variance: **downgraded from "meaningful gap" (critic's framing) to trivial** because single-run reporting is the community standard for large-benchmark evaluations in this subfield (TPT, CoOp, etc. all follow the same practice). It would be a "nice-to-have" improvement rather than a real weakness.
- The characterization that the core claim is "not supported by the evidence" and that this is a "structural flaw": **weakened to minor.** The paper presents the ablation transparently and both contributions (clustering + Rényi aggregation) are stated in the contributions list. The narrative emphasis is somewhat imbalanced, but the data is honestly reported and the core claim — that backpropagation-free adaptation via this combination works well — is supported. This is a framing issue, not a structural flaw.

## Novel Insights

None beyond the paper's own contributions. The interplay between the honest ablation data and the imbalanced narrative emphasis is worth noting, but this is a meta-observation about presentation, not a novel insight about the method itself.

## Suggestions

1. **Reframe the narrative** to accurately reflect what drives performance: position Rényi entropy aggregation over augmented text-embedding predictions as the primary source of gains, and online clustering as a complementary component that provides an additional ~1.4% improvement. This would align the paper's claims with the evidence in Table 3.

2. **Explicitly state how $y_i$ is computed** in the online clustering update (Eq. 4). If it is based on cosine similarity to current centroids, discuss the potential for confirmation bias and how it is mitigated.

3. **Report the default value of $\beta$** and ideally include a sensitivity analysis across datasets.

4. **Clarify the "negative Rényi Entropy" terminology.** Either use the correct name (Rényi entropy) and explain how the values are used as weights, or explicitly define the transformation applied to obtain a reliability score.

5. **Include BaFTA-TE in the main results tables** as an additional baseline, to let readers directly assess the marginal contribution of online clustering without cross-referencing the ablation.

## Score and Decision

The paper presents a genuine contribution: backpropagation-free test-time adaptation that achieves both superior accuracy and a ~5× speedup over TPT. The method is well-evaluated on 15 datasets with two backbones, and the ablation study is transparent. The main weaknesses are presentation/narrative issues rather than methodological flaws. The paper's core claims are supported by evidence, and the contributions are useful to the community.

**Score: 7.0/10** — a solid paper with real contributions and honest data, held back primarily by narrative imbalance and minor specification gaps that should be addressed in revision.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>