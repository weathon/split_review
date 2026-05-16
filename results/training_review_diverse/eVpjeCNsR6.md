Now I have a thorough understanding of the paper and the reviewer claims. Let me verify the key issues against the actual paper text.

Here is my consolidated review.

---

## Summary

This paper proposes EraseDiff, an unlearning method for diffusion models. It formulates unlearning as a bi-level optimization problem where the outer objective finetunes on remaining data (to preserve utility) and the inner objective scrubs forgetting data by training the model to predict uniform noise instead of Gaussian noise on forgotten samples. A first-order approximation is used for efficiency. Experiments on CIFAR10, UTKFace, CelebA, and CelebA-HQ with both conditional and unconditional diffusion models show effective removal (FID on forgetting classes jumps from 19.62→256.27 on CIFAR10) with reasonable utility preservation (FID on remaining classes from 6.31→23.85) and dramatic speedup (~10 minutes vs. 32 hours for retraining).

## Strengths

- **Clear and effective core idea with strong empirical support.** The approach—finetune on remaining data while forcing the model to output uniform noise on forgetting data—is simple and demonstrably works. Tables 1–3 consistently show that EraseDiff achieves near-complete scrubbing (classification accuracy on forgetting classes drops to 0.002 on CIFAR10 and 0 on UTKFace) while maintaining reasonable generation quality on remaining classes, and it is the only method among those tested whose weight distance (1.3534) closely matches the retrained oracle (1.3533).

- **Dramatic computational savings.** The method unlearns in ~10 minutes on an A100, compared to 32 hours for full retraining—a ~200× speedup (Section 5.4). This is a practical advantage well-supported by the analysis and results.

- **Multi-faceted evaluation on several metrics and datasets.** The paper uses FID, classification accuracy, MIA loss distributions, KL divergence, weight distance, and visualizations across four datasets (CIFAR10, UTKFace, CelebA, CelebA-HQ) and two model types (conditional DDIM, unconditional DDPM), including a Hugging Face pre-trained model (Section 5.6). This breadth strengthens confidence in the method.

- **Demonstrates unlearning of a race attribute (Indian) on UTKFace**, showing applicability to legally sensitive fairness scenarios, not just image classes.

## Weaknesses

### Major

- **Missing empirical comparison with diffusion-specific unlearning methods cited in the related work.** The paper cites Gandikota et al. (2023a,b) and Heng & Soh (2023) as prior work on diffusion model unlearning/deletion but does not compare against them experimentally. The baselines used (Finetune, NegGrad, BlindSpot) are all adapted from classification/regression settings. While the settings differ (Gandikota focuses on text-to-image concept erasure; Heng & Soh assumes no training data access), the paper would be considerably stronger by either including the most comparable variants in experiments or providing a clear, principled explanation of why they cannot be fairly compared. Without this, the claim that EraseDiff "surpasses the baseline methods for diffusion unlearning" is only convincing relative to non-diffusion-specific baselines.

### Minor

- **The bi-level optimization framing adds unnecessary complexity and does not match the actual computation.** The paper frames the problem as a bi-level optimization (Eq. 5–7) but the implemented update (Eq. 9) is simply a weighted sum of two gradients ∇θℱ(θ,𝒟_r) + λ∇θf(θ,𝒟_f), evaluated at the same θ. The K-step inner-loop approximation of φ^K and the constraint f̂(φ,𝒟_f) ≤ 0 have their dependence on θ discarded in the final gradient computation—this is a first-order approximation, which is a legitimate technique, but the presentation makes it seem more novel than it is. The method's real contribution is the composite loss with the uniform-noise forgetting target; the bi-level formalism obscures this. The paper would be clearer by presenting a direct multi-task objective and then discussing the first-order approximation.

- **No error bars or variance information on any quantitative result.** Tables 1–3 report single values for FID, accuracy, and weight distance without standard deviations or confidence intervals over multiple runs. This makes it impossible to assess the significance of the observed differences between methods, especially given that several metrics are close (e.g., weight distances 1.3534 vs. 1.3533).

- **Section 5.6 ("USER STUDY") is a qualitative demonstration, not a formal user study.** It shows example images from Hugging Face models and visually compares outputs. There is no structured human evaluation, no raters, no quantitative user metrics. The section title oversells what is presented.

- **KL divergence is shown only as histograms (Figure 3) without numerical summary statistics.** Providing quantitative KL values (means, variances) would be more informative and precise than histograms alone.

- **The design of the forgetting loss (predicting uniform noise) is heuristically justified.** The reasoning from "maximize KL divergence on forgetting data" to "train the model to predict uniform noise" is explained (replace q with q̂ using uniform ε̂), and the remark notes that any non-Gaussian distribution would work, with some results for N(μ,I) with μ≠0 mentioned. However, the connection between the goal of maximizing KL and the specific choice of uniform noise is not formally derived, and no ablation is presented to show whether alternative divergent distributions materially matter.

### Trivial

- The KL divergence axis labels in Figure 3 ("KL distance") are not precisely defined in the text (the paper computes distance between ε_θ output distribution and Gaussian noise distribution, but the exact estimator is unspecified).

- Section 5.4's complexity analysis uses O(·) notation informally (e.g., "O(h(N))" where h is undefined) rather than standard big-O bounds.

## Nice-to-Haves

- An ablation of the trade-off parameter λ and the number of inner steps K would further strengthen the paper, though the authors mention an ablation study was present in the (stripped) appendix.
- Comparison against a DP-trained baseline, as mentioned in the conclusion's discussion of mitigation strategies, would contextualize the results.
- Individual-sample unlearning (forgetting a handful of specific images, not just entire classes) would broaden the scope of claims about "data influence" removal, which the authors acknowledge as a limitation.

## Removed Points

- **MIA evidence is unreliable / does not support conclusions**: The paper itself acknowledges this limitation (Section 5.2: "the distribution of loss values on 𝒟_f is quite similar to that on the unseen data for the unscrubbed model, resulting in the instability of MIA performance"). The paper is transparent about the metric's limitations for diffusion models—this is an honest discussion of a known difficulty, not a flaw in the authors' evaluation.

- **The paper claims "state-of-the-art" performance**: The paper does not use this phrasing. It says "surpasses the baseline methods," which is an accurate description of the comparison performed.

- **Missing ablation studies / hyperparameter sensitivity**: The paper mentions "Implementation details and more results...including the ablation study" at line 136, indicating these were present in the full submission's appendix, which was stripped by the parsing process.

- **Connection from maximize KL to uniform noise is never formally established**: The paper provides the reasoning (lines 61–77): for forgetting data, maximize KL; to operationalize this, replace the ground-truth backward distribution q with a modified q̂ that uses uniform noise ε̂; then minimize the new KL(q̂||p_θ). The remark notes that any distribution different from the original Gaussian would work. The reasoning is present, though not as a rigorous formal theorem—acceptable for an empirical paper.

- **Criticism that the bi-level formalism "does not match the actual method"**: The paper explicitly states it uses a "first-order method" (line 84, citing Liu et al. 2022a) to solve the bi-level problem. First-order approximations that ignore the inner-loop parameter dependence are standard in bi-level optimization literature (e.g., FO-MAML). The paper is transparent about the approximation it uses.

## Novel Insights

None beyond the paper's own contributions. The reviews confirm that the core idea (composite objective with uniform-noise target for diffusion unlearning) is sound and well-executed, but do not surface an unexpected interpretation or framing beyond what the paper itself provides.

## Suggestions

1. **Replace the bi-level framing with a direct multi-task objective** (min ℱ(θ,𝒟_r) + λ f(θ,𝒟_f)) and only then discuss the first-order approximation as an efficiency technique. This would make the actual contribution clearer and avoid the mismatch between formalism and implementation.

2. **Add comparisons with at least one diffusion-specific unlearning method** (e.g., adapting Gandikota et al.'s concept erasure approach to the paper's setting, or Heng & Soh's EWC-based method). If these methods cannot be fairly compared, provide a clear paragraph explaining the divergence in problem setup.

3. **Report all main results with standard deviations over 3+ independent runs**, especially for FID and weight distance metrics. This is standard practice in the field and would substantially strengthen the evidence.

4. **Rename "USER STUDY" to "Qualitative Results on Public Models"** to accurately reflect what is presented.

## Score and Decision

The paper proposes a clearly effective method for diffusion model unlearning with convincing qualitative and quantitative results, dramatic computational savings, and evaluation across multiple datasets and model types. The core weakness is the absence of comparison with diffusion-specific unlearning baselines cited in the paper itself, which limits the strength of the comparative claims. The method is otherwise sound, the contribution is practical, and the limitations are honestly discussed. With additional baselines and proper statistical reporting, this would be a solid paper; in its current form, the evaluation gaps weigh against acceptance.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>