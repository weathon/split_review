## Summary

The paper proposes MIAU (Membership Inference Attack Unlearning Score), a metric that quantifies machine unlearning quality by combining three Membership Inference Attack (MIA) comparisons—Forget vs Test, Retain vs Forget, and Retain vs Test—and normalizing the results between a baseline model (trained on full data) and a retrained model (trained without the forget set). The authors present MIAU as an offline auditing benchmark to select the most suitable unlearning method for a given model-dataset setting, avoiding full retraining during deployment. Experiments across datasets (MNIST, CIFAR-10/20, MUCAC) and architectures (ResNet-18, All-CNN, ViT) with four unlearning methods are reported.

## Strengths

- **Addresses a relevant gap**: The paper correctly identifies that current MIA-based unlearning evaluations often use a single comparison and lack proper reference points. The idea of integrating three MIA perspectives and normalizing against baseline/retrain is a sensible improvement over ad-hoc evaluations.

- **Thorough experimental setup**: The authors evaluate across multiple datasets, architectures, unlearning methods, and random seeds, providing a good degree of coverage. The inclusion of partial-retraining baselines (25%, 50%, 75%) is a thoughtful way to test whether the metric captures gradual forgetting.

- **Honest reporting of negative findings**: The paper highlights that MIAU does not always show monotonic increase under progressive retraining (Figure 3) and that statistical significance is weak for many comparisons (Figure 4). This transparency is valuable, even if it undermines the claimed benefits of the metric.

## Weaknesses

### Fatal

**The main claim is contradicted by the paper’s own evidence.** The authors state (Section 7) that MIAU “aligns with desirable properties … including consistency under progressive removal,” but Figures 3 and 4 and the accompanying text explicitly show that the expected progression MIAU_25 < MIAU_50 < MIAU_75 < MIAU_full **does not hold consistently** across datasets. Moreover, most one-sided p-values in Figure 4 are >0.05 (many >0.4), meaning MIAU cannot statistically distinguish between different levels of forgetting. Since the entire justification for MIAU rests on its ability to quantify the degree of forgetting, this empirical invalidation is fatal. The paper acknowledges the issue (“inherent limitations of MIAs”) but never resolves it; the proposed metric inherits these limitations without a solution.

### Major

- **The requirement of a “retrained reference” model undermines the claimed practical value.** The paper presents MIAU as an offline auditing tool that eliminates the need for retraining during deployment, yet computing MIAU still requires training a full retrained model (from scratch, without the forget set). This is exactly the expensive operation that unlearning is supposed to avoid. The “one-time” argument is weak: in practice, the forget set composition can change over time (new deletion requests), and re-running the full audit would be prohibitive. Furthermore, the baseline and retrained models must be trained once per dataset/model pair, which is already a large overhead.

- **The calibration of the logistic transformation (α = 13.8) is ad hoc and not validated.** The derivation in Appendix A.1 likely forces the baseline to near 0 and retrain to near 100, but this depends heavily on the specific MIA accuracies observed. For different models/datasets where the baseline and retrain MIA values are more or less separated, the same α will not preserve the same anchor points. This makes MIAU scores not directly comparable across different setups, which is a significant flaw for a proposed standardized metric.

- **Equal weights for the three MIA tasks are used without justification.** The paper states β = γ = δ = 1/3 “to provide a balanced evaluation,” but there is no analysis of whether equal weighting is appropriate. Different applications may value removal effectiveness (Forget vs Retain) differently from residual memorization (Forget vs Test). The metric should either justify a principled weighting scheme or treat the three components separately.

### Minor

- The attack model (binary logistic regression on softmax outputs) is relatively simple. Stronger MIAs (e.g., loss-based, gradient-based) might yield different MIAU values. The paper includes one saliency-map variant, but this is only for two experiments.

- The four unlearning methods are representative but limited. The paper does not include state-of-the-art methods like SISA or more recent influence-based approaches, which limits the strength of the ranking claims.

### Trivial

- In Section 5, the description of MIA tasks includes “Retain vs Forget” twice and omits the third comparison in the text. The table in Section 6 has a row “MIA (Train vs Test)” that is not defined in the method; it seems to be a different setup (full train vs test) that is not part of MIAU.

## Nice-to-Haves

- The paper would benefit from a synthetic experiment where the ground-truth forgetting level is known (e.g., by corrupting a known fraction of the forget set) to establish whether MIAU truly tracks forgetting rather than confounding factors.

- Including a comparison with other unlearning evaluation scores (e.g., NoMUS, ZRF) on the same gradual-forgetting setting would help contextualize MIAU’s behavior.

## Novel Insights

The paper’s main novel insight is negative but important: even a carefully designed MIA-based composite metric (combining three comparisons with normalization) fails to reliably distinguish degrees of forgetting, and MIAs themselves are inherently unstable across seeds and insensitive when models generalize well. This suggests that the unlearning community may need to look beyond MIA-based auditing for reliable evaluation.

## Suggestions

1. Reconsider the central claim that MIAU is a “reliable and consistent measure of forgetting quality.” The evidence does not support this. The paper would be more honest as a critical analysis showing the limitations of MIA-based unlearning metrics, with MIAU as an illustrative (but imperfect) effort.

2. If the metric is to be salvaged, validate it on datasets or settings where there is a known ground truth for forgetting (e.g., model trained on data with injected poisoning, or using synthetic data where forget set influence is controlled).

3. Provide guidance on how to set the α parameter without requiring baseline and retrain models to be evaluated first—otherwise the calibration itself defeats the purpose of a reference-free metric.

## Score and Decision

**Score:** 3

**Decision:** Reject

**Rationale:** The paper proposes a metric that is not empirically validated as claimed. The core requirement for MIAU—that it consistently reflects the degree of forgetting—is refuted by the paper’s own results (non-monotonic behavior under partial retraining, lack of statistical significance). Combined with the practical overhead of requiring a truly retrained reference model, the contribution does not bring sufficient value to the community as a reliable evaluation tool. The work has merit as an analysis piece highlighting MIA limitations, but as a proposed metric it falls short of acceptance standards.

MY FINAL SCORE: <score>3</score>
MY FINAL DECISION: <decision>Reject</decision>