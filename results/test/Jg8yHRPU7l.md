Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper studies the mechanism behind "clean-priority learning"—the phenomenon where neural networks trained on label-noise-corrupted data first learn clean patterns and only later overfit the noise, producing a U-shaped test error curve. For infinitely wide ReLU networks, the authors show that at initialization, label corruption flips the sign of noisy sample-wise gradients, causing noisy and clean segment gradients to point in opposite directions with the clean gradient having larger magnitude (due to numerical majority). They prove that if this opposition persists during training, the GD update becomes equivalent to training on clean data alone (with a rescaled learning rate), clean loss decreases while noisy loss increases, and the clean gradient dominance monotonically diminishes, eventually terminating the clean-priority phase. Experiments on MNIST and CIFAR-10 with finite-width networks corroborate the predicted dynamics.

## Strengths

- **Principled mechanism for how the model "distinguishes" clean from noisy samples without access to ground-truth labels.** The paper shows concretely that label corruption flips the sign of $(y - f(\mathbf{w};\mathbf{x}))$, reversing the sample-wise gradient direction. Combined with the cluster structure in $\nabla h$ space (similar inputs have similar $\nabla h$ vectors), this produces opposing segment gradients at initialization—a clean data-driven explanation rather than an appeal to "simplicity bias."

- **Clean theoretical isolation of the cancellation effect.** Lemma 4.2 is the paper's theoretical core: under Assumption 4.1 (segments remain opposite during training), the GD update on the noisy dataset is equivalent to GD on the clean dataset with a positive rescaled learning rate $\eta'_t = \frac{1-\alpha_t}{1+\alpha_t}\eta$. This formally shows how the noisy contribution is cancelled and the update direction is determined entirely by clean samples.

- **Theorems 4.4 and 4.5 provide a self-contained account of why clean-priority eventually terminates.** Theorem 4.4 shows clean loss decreases while noisy loss increases; Theorem 4.5 proves $\alpha_t$ (the noisy-to-clean magnitude ratio) increases monotonically. Together they explain both the initial clean-priority and its eventual decay—the clean segment's gradient magnitude shrinks as its residuals shrink, while the noisy segment's grows as its residuals grow.

- **Experimental confrontation of core predictions on finite-width networks.** Figures 5–8 on MNIST (binary and multi-class) and CIFAR-10 show the predicted patterns: clean error decreases / noisy error increases in the early stage, clean gradient dominance diminishes over time, and the U-shaped test error aligns with the onset of noise fitting. These experiments go beyond the infinite-width setting of the theory.

## Weaknesses

### Major

- **All theoretical results are conditional on Assumption 4.1, which is not derived from first principles and is stronger than the paper's supporting arguments can justify.** Assumption 4.1 asserts that throughout the early training stage, $g_{noise}^{(c)}(\mathbf{w}_t) = -\alpha_t\,g_{clean}^{(c)}(\mathbf{w}_t)$ with exact collinearity. The paper justifies this by noting that (a) opposition holds at initialization, and (b) each sample-wise gradient's direction is fixed during training (since $\nabla h$ is fixed in infinite-width NTK). However, as the critic correctly observes, fixing individual directions does **not** guarantee that the *sums* over the clean and noisy sets remain exactly collinear: if the scalar factors $(f(\mathbf{w};\mathbf{x}_i)-y_i)$ shrink at different rates across samples within each segment, the direction of each segment gradient can change. The assumption requires additional structure (e.g., that all sample-wise gradients within a segment share a common direction, or that their scalar factors remain proportional). The paper does not provide this structure, nor does it analyze how much deviation the mechanism tolerates.

- **The paper's contribution statement overclaims what is proven.** The third bullet in the introduction states: "For fully connected networks with mild assumption on data we theoretically prove our empirical observation." But the theorems in Section 4 are all conditional on Assumption 4.1—an assumption about *training dynamics*, not about data. A reader expecting a proof that clean-priority follows from the infinite-width architecture and label-noise structure alone will be disappointed. The theory shows what *would* happen if the opposition persists, but does not prove that it *must* persist. This gap between the claimed contribution and what is actually established is meaningful.

- **No experimental verification of the key assumption's validity during training.** The paper reports magnitude ratios ($\|g_{clean}\|/\|g_{noise}\|$) in Figures 6 and 8, but never measures the *angle* or cosine similarity between the two segment gradients over time. This is the most direct experimental test of Assumption 4.1. Without it, the reader cannot tell whether the clean-priority observed in experiments arises from the proposed cancellation mechanism or from some other effect. Given that the theory crucially depends on the segments remaining opposite (not just having a favorable magnitude ratio), this missing measurement is a significant gap.

### Minor

- **The multi-class extension is handled at a sketch level.** The paper introduces single-logit gradients and derives approximate initialization ratios, but then says "we expect similar learning dynamics" without extending Assumption 4.1 or the main theorems to the multi-class setting. The paper itself notes that a noisy sample may be "clean" for most logits (only the ground-truth and corrupted-class logits are affected), which could complicate the cancellation story. The experiments are encouraging, but the theoretical analysis for $C>2$ is much rougher than for binary.

- **The connection to early stopping is descriptive, not analytical.** The title promises a mechanism of clean-priority learning in "early stopped neural networks," but the paper does not characterize the early stopping point, derive its location, or discuss optimal stopping. It partitions training into "before" and "after" the early stopping point and observes that the clean-priority phase ends roughly when the dominance ratio reaches 1. The link to early stopping is phenomenological rather than predictive.

- **The factorization in Equation (5) is presented without justification.** The paper writes $\mathbb{E}[\nabla l] = \mathbb{E}[f(\mathbf{w}_0;\mathbf{x})-y]\,\mathbb{E}[\nabla h]$, which assumes $(f-y)$ and $\nabla h$ are uncorrelated. At initialization for infinite-width binary networks, $f(\mathbf{w}_0;\mathbf{x}) \approx 0.5$ approximately constant across inputs, so the factorization is a reasonable approximation; but the paper does not discuss this independence. The multi-class extension inherits the same gap.

### Trivial

None.

## Nice-to-Haves

- Direct experimental verification of the angle/cosine similarity between $g_{clean}$ and $g_{noise}$ during training would substantially strengthen the paper.
- A relaxation analysis bounding how much deviation from exact collinearity the clean-priority mechanism can tolerate would make the theory more robust.
- The paper could benefit from being more explicit about what the "mild assumption on data" is (presumably the cluster structure in $\nabla h$ space).

## Removed Points

- **Theorem 3.1 truncated in extracted text / "The theorem in Section 3 is unverifiable":** This is a PDF-parser artifact, not an author error. The paper states the claim (similar inputs → similar ∇h) and supports it with experimental evidence (Figure 2) and a citation (Liu et al., 2020).
- **"No discussion of the NTK limitation":** The paper explicitly discusses the infinite-width NTK property ($\nabla h$ fixed during training, citing Liu et al. 2020) and how it underpins Assumption 4.1.
- **"$\delta < 0.5$ not stated as limitation":** The paper clearly states on line 52: "In this paper, we set $\delta < 0.5$, i.e., the majority of training samples are not corrupted."
- **"Missing appendix / proofs":** Parser artifact — these sections exist in the original submission.

## Novel Insights

None beyond the paper's own contributions. The reviewers' insights reinforce the paper's core observations (gradient opposition at initialization, cancellation mechanism, diminishing dominance) while correctly identifying that the theoretical edifice rests on an assumption that is not fully justified. The most valuable critical insight is that the transition from "individual gradients keep their direction" to "segment sums remain exactly collinear" is nontrivial and needs either a proof or a relaxation.

## Suggestions

1. **Address the Assumption 4.1 gap directly.** Either (a) prove that exact collinearity holds under the infinite-width NTK regime with appropriate data conditions (e.g., showing that within each segment, all sample-wise gradients share a common direction or that the scalar factors remain proportional), or (b) relax the assumption to approximate collinearity and bound the deviation, showing the mechanism still operates within a tolerance.

2. **Add experimental measurement of the cosine similarity between $g_{clean}$ and $g_{noise}$ during training** for the finite-width networks used in the experiments. This is the most direct test of whether the proposed mechanism is actually at work.

3. **Tone down the contribution claim.** Replace "we theoretically prove our empirical observation" with a more precise statement such as "we provide a theoretical framework showing that clean-priority learning follows from gradient opposition during early training, and we provide experimental evidence consistent with this mechanism."

4. **Clarify the factorization in Eq. (5)** by noting that $f(\mathbf{w}_0;\mathbf{x}) \approx 0.5$ at initialization for infinite-width binary networks, making $(f-y)$ approximately constant within each class, so the expectation factorization is justified.

## Score and Decision

The paper addresses a genuinely important question—how neural networks learn clean patterns before overfitting label noise—and proposes a clean, intuitive mechanism supported by both theory and experiment. The theoretical framework (Lemma 4.2, Theorems 4.4–4.5) elegantly shows what clean-priority dynamics would look like under gradient opposition. The experiments confirm the predicted qualitative behavior. The main weakness is real: the theoretical contribution is conditional on an assumption that is plausible but not proven, and the paper's framing overstates what is established. The missing experimental verification of the gradient angle during training makes the gap harder to evaluate. However, these problems are addressable in revision and do not invalidate the paper's empirical findings or the conceptual value of the proposed mechanism.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>