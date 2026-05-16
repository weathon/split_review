Now I have a thorough understanding of the paper and all the claims. Let me produce the final consolidated review.

## Summary

This paper introduces Test-Time Ensemble (TTE), a method that enhances existing Test-Time Adaptation (TTA) approaches through weight-space ensembling (adaptive EMA), dropout-based diversity, and a de-biased knowledge distillation objective. The core insight is that TTA models exhibit linear mode connectivity (LMC), enabling efficient weight averaging that captures ensemble benefits in a single model. TTE integrates with three TTA baselines (Tent, SAR, DeYO) and delivers consistent accuracy gains across challenging scenarios (label shifts, batch size 1, mix shifts, continual TTA, natural distribution shifts) on ImageNet-C, ImageNet-R, ImageNet-S, and ImageNet-V2, with improvements of up to +11.1% on ResNet50-GN.

## Strengths

1. **Significant and consistent empirical gains across diverse challenging scenarios**: TTE integrated with DeYO achieves average accuracy improvements of +9.9% in Label Shifts, +8.3% in Batch Size 1, and +11.1% in Mix Shifts on ResNet50-GN for ImageNet-C (Tables 1–2). It outperforms prior continual TTA methods (Table 3) and delivers gains on natural distribution shifts (Table 4). The improvements are consistent across three base methods and two architectures, demonstrating broad applicability.

2. **Adaptive momentum scheme for online ensemble construction**: The proposed adaptive EMA (Eq. 2) dynamically adjusts the momentum based on divergence between adapter and ensemble outputs. In continual TTA with non-i.i.d. conditions, this mechanism yields a +1.8% accuracy improvement over fixed momentum (Figure 5), and momentum values sensibly decrease during distribution transitions to promote faster ensemble updating.

3. **Dropout-based diversity during fine-tuning is novel in TTA**: Incorporating high dropout (0.9 for ResNet50-GN) in the penultimate layer adds a +1.6% accuracy gain over weight-space ensemble alone (Table 5), leveraging the insight that fine-tuning is approximately linear. This avoids the computational cost of multiple forward passes.

4. **De-biasing scheme demonstrably stabilizes optimization and prevents collapse**: The paper identifies and addresses a genuine failure mode — when the TTA model collapses, naive ensembling degrades performance (Figure 3). The de-biased distillation (Eq. 3–5) reduces performance variance across seeds (Figure 7) and prevents collapse in scenarios where baselines fail (e.g., continual TTA, Table 3).

5. **Plug-and-play integration with fixed hyperparameters**: TTE uses a single set of hyperparameters across all scenarios and base methods, reducing concerns about over-tuning. The sensitivity analysis (Figures 6–7) confirms robustness to hyperparameter choices.

## Weaknesses

### Fatal
None.

### Major

1. **De-biasing scheme may produce invalid probability vectors without stated post-processing**: Equation 4 defines $\hat{\boldsymbol{y}}_{e,i}^{\prime} = \hat{\boldsymbol{y}}_{e,i} - w(s_i) \cdot \boldsymbol{c}_{bias}$. Since both $\hat{\boldsymbol{y}}_{e,i}$ (a softmax output) and $\boldsymbol{c}_{bias}$ (an EMA of softmax outputs) are probability-like vectors, subtracting a scalar multiple can produce negative values or break the unit-sum property. The paper uses $\hat{\boldsymbol{y}}_{e}^{\prime}$ as the target distribution in reverse KL divergence $KL(\hat{\boldsymbol{y}}_a || \hat{\boldsymbol{y}}_e^{\prime})$, which requires both arguments to be valid probability distributions. The paper does not mention any post-processing (clipping, re-normalization, or logit-space correction). The authors must clarify how $\hat{\boldsymbol{y}}_{e}^{\prime}$ is made a valid probability vector before use.

### Minor

2. **LMC evidence is limited in scope and not fully specified**: The preliminary LMC experiments (Figure 1, Section 2.2) do not specify which TTA method was used to produce the adapted models ($\theta_1, \theta_2$). The paper claims "TTA models generically exhibit linear mode connectivity" but only shows this for one (unreported) method and one type of pair (two different corruptions). The claim would be strengthened by demonstrating LMC for multiple TTA methods (Tent, SAR) and reporting the loss barrier quantitatively across more pairs.

3. **Noise-robust distillation claim relies on oracle-labeled analysis**: Figure 4's justification for reverse KL divergence uses true labels to distinguish correct from incorrect predictions and compute gradient ratios. While this provides intuition, the claim of "noise-robustness" in an unsupervised TTA setting would be better supported by directly comparing forward vs. reverse KL within the actual TTA pipeline (without oracle knowledge), or providing a theoretical argument that does not depend on labels. The empirical results of TTE do validate the overall approach, but the specific "noise-robust" framing overreaches the evidence in Figure 4.

4. **Missing comparison to output-space ensemble baselines**: The paper argues that prior approaches using multiple predictions (Jang et al., 2022; Yuan et al., 2023) are computationally heavy, and positions weight-averaging as an efficient alternative. However, it does not compare TTE to a simple output-space ensemble of multiple TTA copies (e.g., running 2–3 instances of Tent with different seeds and averaging outputs). Such a comparison is needed to quantify how much of the explicit ensemble benefit TTE retains, and to validate the claimed computational savings.

5. **Computational overhead is asserted but not measured**: The paper states TTE requires "only an additional feedforward pass for $f_e$, resulting in minimal computational overhead" (Section 4.1) but provides no wall-clock time, FLOPs, or throughput measurements. Given that TTE doubles the forward passes per step, the overhead relative to the base method and to alternative multi-model strategies should be quantified.

### Trivial

6. **Figure 1 presentation is somewhat unclear**: It is ambiguous whether the trajectories in Figure 1 show averages over many corruption pairs or a single representative pair. The axes define accuracy on "target" and "non-target" distributions but then refer to "noise and blur" in panel (a), which could be clarified.

7. **Cosine similarity for bias detection is a design choice without justification**: Using cosine similarity between probability vectors (Eq. 3) is valid but uncommon; the paper does not compare it to alternatives (e.g., Euclidean distance or inner product) or justify why cosine is preferred.

## Nice-to-Haves
- Include an algorithm pseudocode listing covering the forward pass, adaptive momentum update, bias accumulation, de-biasing, and loss computation.
- Add a dedicated limitations paragraph discussing: (a) TTE doubles the forward pass, (b) the de-biasing adds three hyperparameters (n, $\alpha$, $m_0$), (c) the method assumes the base TTA method is differentiable.
- Report standard deviations in main tables or at minimum note the range, especially for settings where baselines collapse to near-zero accuracy.

## Removed Points
These points are flagged to be removed; treat them with caution.
- **"Adaptive EMA creates a circular dependency"**: The critic claims $L_{rkl}$ depends on $\theta_e$ which depends on $\theta_a$, creating a feedback loop. This misunderstands the sequential nature of the algorithm — the loss is computed at step t to update the momentum for step t+1. Standard teacher-student framework, not a circular dependency.
- **"Cosine similarity for probability vectors is uncommon"**: This is a taste-based objection. Cosine similarity is a standard measure for any non-negative vector representation. The paper's choice is defensible.
- **"Standard deviations relegated to appendix"**: The paper states results with standard deviations are detailed in supplementary tables (14, 15, 16). This is standard practice for papers with many results, not a weakness.
- **"Dropout ratio not validated with all base methods"**: The paper shows sensitivity analysis with DeYO (Figure 6) and uses consistent hyperparameters across all base methods. This is sufficient for a hyperparameter sensitivity study.
- **Various missing-appendix complaints**: The parser strips appendix content; these exist in the original submission.
- **Formatting, typos, and grammar nitpicks**: These are parser artifacts, not author errors.

## Novel Insights
The most novel observation bridging the reviews is that the paper's central technical weakness (invalid probability vectors from de-biasing) and one of its core strengths (empirical success) create a tension worth exploring: the de-biasing scheme may work well in practice precisely because it produces slightly "invalid" unnormalized vectors that effectively sharpen the distillation signal, functioning similarly to logit adjustment or temperature scaling without explicit normalization. If the authors formalize this, it could turn a current bug into a feature. Beyond this, the reviews surface no insight beyond the paper's own claim that LMC in TTA is a new finding worth building on.

## Suggestions
1. Address the de-biased prediction validity issue explicitly: either (a) project $\hat{\boldsymbol{y}}_{e}^{\prime}$ back onto the simplex (e.g., clipping negative values and re-normalizing), or (b) reformulate the adjustment in logit space so the softmax output remains a valid distribution.
2. Specify the TTA method used for the LMC preliminary experiments and report LMC for at least one additional method (e.g., Tent) with quantitative loss-barrier measurements.
3. Add a direct comparison to a simple output-space ensemble (2–3 copies of the same TTA method) with wall-clock time or FLOPs to validate the claimed efficiency.
4. In the noise-robustness analysis, compare forward vs. reverse KL within the actual unsupervised TTA pipeline (without oracle labels) to directly support the framing.
5. Report wall-clock time per batch for the base method, base+TTE, and an explicit ensemble to quantify overhead.

## Score and Decision

This paper makes a real, empirically validated contribution to test-time adaptation. The weaknesses are fixable and do not undermine the core result — TTE consistently improves existing TTA methods. The de-biasing validity concern is the most substantive technical gap, but it is correctable and the empirical evidence for the method's effectiveness is strong across multiple challenging scenarios. I recommend acceptance with minor revisions.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>