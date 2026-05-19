- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 6, 6, 5
Now I have all the information needed. Let me produce the final consolidated review.

## Summary

The paper proposes a Fixed Non-negative Orthogonal (FNO) classifier and introduces the concept of "zero-mean neural collapse" to explain the training dynamics of fixed orthogonal classifiers that cannot converge to a simplex ETF. The authors prove that under an orthogonal layer-peeled model (OLPM), the FNO classifier's global minimizer induces a collapsed solution where class means align with the fixed orthogonal columns centered at the origin. They further leverage the resulting Feature Dimension Separation (FDS) property to enhance masked softmax in continual learning and to propose arc-mixup for imbalanced learning. Experiments on split datasets for continual learning and long-tailed benchmarks for imbalanced learning demonstrate competitive performance.

## Strengths

- **Theoretical framing of collapse for fixed orthogonal classifiers.** Theorem 1 formally addresses an underexplored gap: while fixed orthogonal classifiers cannot converge to a simplex ETF (standard neural collapse), the paper shows that under non-negativity and orthogonality constraints, the OLPM's global minimizer induces a collapsed form (Eq. 7) that constitutes a well-defined alternative collapse pattern (zero-mean neural collapse). This provides a theoretical foundation for analyzing fixed classifiers beyond the simplex ETF setting.

- **Feature Dimension Separation (Definition 3) is a clean and testable property.** The observation that a non-negative orthogonal weight matrix forces class weight vectors to have disjoint nonzero index sets (𝕁ₖ ∩ 𝕁ₖ' = ∅) is well-defined and directly leads to the claimed practical benefits. Theorem 2 then builds on this to prove that arc-mixup without class-wise interference requires both orthogonality and non-negativity.

- **Empirical results on continual learning (Table 2).** The FNO classifier consistently outperforms masked replay (Kim et al., 2023a) baselines across multiple continual learning settings (e.g., 84.61% vs. 78.43% on CIFAR-100 with buffer size 500), providing evidence that FDS enhances masked softmax by reducing class-wise interference.

- **Competitive results on long-tailed benchmarks (Tables 3, 4).** Arc-mixup with FNO achieves strong accuracy on CIFAR100-LT, ImageNet-LT, and Places-LT, with consistent improvements under high imbalance ratios, supporting the claim that the approach is effective for imbalanced learning.

## Weaknesses

### Fatal
None.

### Major

- **No empirical verification of zero-mean neural collapse, the paper's central phenomenon.** Section 4 claims to have "conducted comprehensive experiments" to verify that zero-mean neural collapse is a "natural phenomenon" when training with the FNO classifier, but the paper presents zero quantitative data, metrics, or visualizations to support this. Standard neural collapse measurements (e.g., within-class variability, alignment of class means with classifier columns, NC1–NC4 metrics from Papyan et al., 2020) are not reported. Given that the paper's entire theoretical narrative hinges on this phenomenon, the lack of direct empirical validation is a significant gap. The downstream task improvements (continual learning, imbalanced learning) do not substitute for verifying that the claimed collapse behavior actually occurs.

- **Missing ablation isolating the role of non-negativity.** The experiments compare FNO against learnable classifiers and against masked replay baselines, but never against a fixed orthogonal classifier that is *not* non-negative (e.g., a random orthogonal matrix with mixed signs, or a Hadamard matrix). Without this ablation, it is unclear whether the improvements come from orthogonality alone or from the specific FDS property created by non-negativity. This is essential for attributing the claimed mechanism.

- **Arc-mixup is not compared to standard mixup on the same FNO backbone.** In Tables 3 and 4, arc-mixup+FNO is compared against methods using different classifiers and loss functions, but there is no direct comparison of arc-mixup vs. standard mixup (with label mixing) using the same FNO classifier. Without this control, the benefit of the novel mixing strategy itself (as opposed to the fixed classifier) cannot be isolated. The paper's claim that mixup "worsens the imbalanced effect" (line 255) is supported only by a single line referencing Table 4, not by a systematic head-to-head comparison.

- **The procedure for generating a random non-negative orthogonal matrix is not described.** The paper states "initialize the linear classifier Q as a random fixed non-negative orthogonal matrix by Eq. 8" (line 107), but Eq. 8 is not present in the main text. Constructing a matrix with QᵀQ = I, all entries ≥ 0, and D ≥ K is non-trivial; omitting this procedure harms reproducibility and makes it impossible for readers to implement the method.

### Minor

- **Theorem 2's non-negativity argument is incomplete.** After proving that orthogonality is necessary for ‖ŵ‖ = 1, the paper states "non-negativity is a natural result as the definition of FDS and Eq. 12" (line 226) without derivation. While the conclusion may be correct, the proof as presented lacks a clear argument for why non-negativity is *necessary* rather than merely convenient.

- **How the FNO classifier handles new classes in continual learning is not clarified.** In class-incremental learning, new classes appear over time. The paper does not explain whether all K columns are pre-allocated (requiring knowing K in advance) or whether columns can be added incrementally. This is essential for understanding the continual learning setup.

- **"Zero masking in mini-batches" is mentioned but never defined.** Figure 3b caption references "arc-mixup and zero masking in mini-batches" as part of the imbalanced learning method, but no definition or description of zero masking appears in the main text.

- **The D ≥ K limitation is acknowledged but no practical mitigation is discussed.** The conclusion notes this limitation and points to the Thomson problem as a future direction, but offers no interim strategy for handling datasets where the number of classes exceeds the feature dimension. Since D ≥ K is a requirement for orthogonality with non-negative entries, this is a real constraint on applicability.

### Trivial
None that survive the filtering rules (remaining formatting issues are parser artifacts).

## Nice-to-Haves

- An ablation that compares the FNO classifier with a fixed simplex ETF classifier in the same continual learning / imbalanced learning setups would help position the work relative to existing fixed-classifier approaches (e.g., Yang et al., 2022b; Liang & Davis, 2023).
- A figure showing the evolution of class means and within-class variability during training with FNO (similar to Figure 1 in Papyan et al., 2020) would substantially strengthen the empirical case for zero-mean neural collapse.

## Removed Points

These points were raised by reviewers but are removed per the filtering rules; treat with caution:

1. **Missing proof of Theorem 1 (appendix content).** The paper states "Proof 1." as a placeholder with the full proof deferred to the appendix. Per the system instructions, the appendix was stripped by the parser and criticisms about missing appendix proofs are removed. The proof exists in the original submission.

2. **Theory-practice gap: OLPM constraint not enforced.** The critic claimed the constraint ∑_{j≠k} h^T q_j ≥ 0 is critical to Theorem 1 but unenforced in practice. This is a factual misunderstanding: since h = ReLU(f_θ(x)) (line 40) has all non-negative elements and Q has all non-negative elements (line 122), each individual term h^T q_j ≥ 0, so the sum over j≠k is automatically ≥ 0. The constraint is trivially satisfied during training without explicit enforcement.

3. **Arc-mixup "inconsistency" with fixed classifier.** The critic argued that mixing weight vectors in arc-mixup contradicts the claim that the classifier is fixed. This is a misunderstanding: mixing fixed weight vectors to create a soft target ĝ does not update the classifier weights Q; the classifier remains frozen. The mixed ĝ is a synthetic label, not a parameter update.

4. **Missing Eq. 8 reference.** The paper references "by Eq. 8" for generating the non-negative orthogonal matrix. This equation was in the appendix (stripped by parser). The core concern (procedure not described) is retained as a Major weakness above; the specific "missing equation" framing is removed as appendix-content criticism.

5. **Missing related works / formatting nitpicks / reproducibility complaints about undisclosed hyperparameters.** These are removed per the filtering rules.

## Novel Insights

None beyond the paper's own contributions. The reviewer inputs do not surface any observation about the paper that the paper itself does not already state or imply.

## Suggestions

1. **Add empirical neural collapse measurements.** Report standard NC metrics (within-class variability, class-mean alignment with classifier columns, etc.) on a simple balanced dataset (e.g., CIFAR-10) during training with the FNO classifier. Show that class means center at the origin and align with the orthogonal columns. This is the single most important addition to validate the paper's central claim.

2. **Add an ablation comparing FNO with a fixed orthogonal classifier that is not non-negative** (e.g., a random orthogonal matrix with both positive and negative entries, or a Hadamard matrix). This isolates the effect of FDS from orthogonality alone.

3. **Add a direct comparison between arc-mixup and standard mixup (with label mixing)** on the same FNO backbone to isolate the contribution of the mixing strategy.

4. **Describe the non-negative orthogonal matrix generation procedure** in full, or provide pseudocode and a citation to a known construction. This is essential for reproducibility.

5. **Clarify the continual learning setup:** explain how new classes are handled (pre-allocated columns vs. dynamic expansion) and define "zero masking in mini-batches."

6. **Strengthen the proof sketch of Theorem 2** by providing a brief argument for why non-negativity is necessary for the claimed property, rather than stating it as a "natural result."
