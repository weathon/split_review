Here is my consolidated review.

## Summary

This paper proposes CONFST, a method to steer LLMs at inference time by constructing a "confident steering direction" from user history. The approach trains a logistic regression classifier on token-level activations from a fixed layer, selects activations above a confidence threshold, averages them to form a steering vector, and adds it to the model's activations during generation. The paper also presents a Bayesian theoretical framework (adapted from Xie et al. 2021) to characterize what makes a steering direction effective. Experiments are run on GPT2-XL (1.5B), Mistral (7B), and Gemma-it (9B) for topic shift (AgNews, Emotion) and style shift (conciseness, helpfulness, detoxification) tasks.

## Strengths

- **Demonstrates multi-class steering beyond binary direction choices.** Unlike prior methods (e.g., Act Addition, ITI) that are limited to two opposite directions (truthful vs. untruthful, harmless vs. harmful), CONFST can steer toward one preference among four (AgNews) or six (Emotion) candidate classes. Figures 4–5 show this empirically, confirming the paper's central practical claim. This is a genuine step forward in capability.

- **No need to iterate over all layers/heads to find separable activations.** Unlike ITI (Li et al., 2024b) and related work that searches all layers and attention heads, CONFST operates on a single fixed layer, reducing computational overhead. This is a practical advantage clearly differentiated from prior work in Section 2.

- **Empirical scope across multiple model sizes and task types.** The paper tests on three models (1.5B, 7B, 9B) and covers both topic shift and style shift (conciseness, helpfulness, detoxification, indirect emotion expression), demonstrating broad applicability.

- **Ablation on confidence threshold β reveals an honest trade-off.** Remark 4 acknowledges that higher β can hurt performance (e.g., "sports" in AgNews, "anger"/"fear" in Emotion) because fewer selected activations yield a biased preference estimate. This transparency about the method's limitations is commendable and provides practical guidance.

## Weaknesses

### Fatal
None.

### Major

1. **The abstract overclaims about layer selection, directly contradicting the algorithm.** The abstract states: "It is very simple to implement, since there is no need to determine which layer the steering vector should be added to." However, Algorithm 1 (line 223) takes a target layer ℓ as input, and experiments manually set ℓ=1 for Mistral and ℓ=0 for Gemma (Section 5.2). The paper never shows that performance is insensitive to this choice, nor does it provide a principled way to set ℓ. The advantage over prior work is that CONFST avoids *searching* over layers — a weaker and more honest claim — but the text says "no need to determine which layer," which is flatly contradicted by the method's own implementation.

2. **Theory–method gap: the Bayesian framework does not meaningfully guide the algorithm.** Section 3 derives that a good steering direction should maximize \(P(\theta^* \mid f(\mathcal{T}(A_{1:n})))\) (posterior probability of the ground-truth preference). The method then trains a logistic regression on token-level activations, selects high-confidence ones, and averages them. The conceptual leap from "maximize posterior on the full direction" to "train a classifier on individual token activations and threshold" is never formally justified. The theory does not guide the choice of layer ℓ, subsequence length s, token position t, or threshold β. Assumptions 1–3 involve infinite-data asymptotics and idealized separability, but their connection to the finite-sample, threshold-based selection procedure is unexamined. The theory functions as motivation, not as a foundation that constrains or explains the algorithm's design decisions.

3. **Inadequate baseline definitions and comparisons.** (a) The baselines "Massive Mean Shift" and "Act Addition" are named in Figure 4 and 5 captions but never defined in the paper text — the reader cannot tell what these methods are or how they were implemented. This is a reproducibility failure. (b) Style shift experiments (Figures 6, 7, 9) compare only against the unsteered model, not against any other steering method. The sole comparison is detoxification (Figure 10), where CONFST beats mean steering once, with no variance reported. Without systematic comparison to methods like ITI, contrastive activation addition, or prompt-based ICL across all tasks, the claimed advantages are not convincingly supported.

4. **No statistical rigor.** All experiments lack confidence intervals, error bars, and statistical significance tests. Results are reported as point estimates from (presumably) single runs. Given the noise visible in the ablation results (some categories degrade with higher β), variance reporting is essential to assess whether differences are reliable.

5. **Missing ablations on key hyperparameters.** Only threshold β is ablated. There is no analysis of sensitivity to layer ℓ, subsequence length s, or token position t. Since the paper claims robustness ("no need to determine which layer"), demonstrating insensitivity to ℓ is essential but absent.

### Minor

- **The "optimization-free" framing is misleading.** The paper describes model steering as "optimization-free" (abstract, Sections 1, 3), yet CONFST trains a logistic regression classifier — a nontrivial optimization step — on activation data. While this is less costly than fine-tuning, it is not optimization-free, and the characterization should be qualified.

- **The method requires splitting user history into train/test sets.** This may be infeasible for users with limited interaction history, and the paper does not discuss how to handle such cases.

- **The theoretical contribution borrows heavily from prior work.** Claim 2 is explicitly noted (Remark 3) as similar to Theorem 1 in Xie et al. (2021). Claim 1 is a direct application of Bayes' rule and the data-processing inequality. While the adaptation to the steering setting is new, the core theoretical machinery is not.

- **"Multiple preferences aligned simultaneously" is ambiguously stated.** The abstract claims preferences can be "aligned simultaneously," but the experiments steer toward *one* target at a time among multiple candidates. The co-steering experiment (topic+style) combines two directions via linear addition, which any additive method can do. This does not validate simultaneous alignment of three or more distinct preferences.

### Trivial
None.

## Nice-to-Haves

- A practical guideline or heuristic for setting β automatically (e.g., based on a held-out validation set) would strengthen usability, since the paper shows that optimal β varies across directions.
- Comparing the computational cost of training the logistic regression versus the layer-search overhead of methods like ITI would substantiate the efficiency claim.
- Qualitative examples comparing CONFST and mean-steering outputs would help readers understand when the method makes a practical difference.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Fig. 11 referenced but missing" / "missing appendix content":** Removed per instructions — parser strips appendix sections from all papers; they exist in the original submission.
- **"The theory is not referenced again after Section 3":** Factually incorrect — Section 4.2 (line 147) explicitly recalls the theory: "Recall in Section 3.2, we have discussed that given the history A_{1:n} the 'good' direction... should satisfy that P(θ*|f(T(A_{1:n}))) is close to 1."
- **"No explicit user instruction is not unique; many methods also infer direction from history":** This is actually a strength, not a weakness. The paper's method infers preferences from history without requiring users to articulate them, which is a genuine practical advantage.
- **"Missing related works":** Cannot be confirmed without external sources; per instructions these criticisms are removed.
- **Formatting/typo nitpicks:** Removed as parser artifacts.

## Novel Insights

The most interesting observation is a subtle one the paper uncovers almost accidentally: the confidence threshold β reveals a non-monotonic trade-off where higher purity of selected activations can reduce effectiveness due to low sample size (Remark 4, Figure 4 "sports"). This is an instance of the classic bias-variance trade-off in a novel setting — a small set of "pure" activations may be more biased than a larger, noisier set that better covers the preference distribution. This insight could guide future work on sample-efficient steering direction construction. Otherwise, the review process did not surface genuinely novel insights beyond the paper's own contributions.

## Suggestions

1. **Correct the overclaims in the abstract and introduction.** Replace "no need to determine which layer" with "no need to search over layers — a single fixed layer suffices." Clarify that "multiple preferences can be aligned simultaneously" means the method handles >2 candidate directions (not simultaneous alignment of many preferences at once).

2. **Define all baselines** (Massive Mean Shift, Act Addition) with citations and implementation details. Compare against at least one state-of-the-art steering method (e.g., ITI, contrastive activation addition) on all tasks.

3. **Report variance** (error bars or confidence intervals) across multiple runs or seeds for all quantitative results.

4. **Add ablation studies** showing sensitivity to layer ℓ, subsequence length s, and token position t. This is essential to support the claim that layer choice is not critical.

5. **Strengthen the theory–method connection** by either (a) empirically testing whether directions with higher classifier confidence indeed produce lower KL divergence to the target distribution, or (b) explicitly stating that the theory provides only high-level motivation and the method is designed heuristically.

## Score and Decision

This paper tackles a real problem (efficient steering toward one of many preferences) with a clean, intuitive approach. The core idea — using a classifier to filter noisy activations before averaging — has merit and the multi-class experiments are a genuine advance over binary-only methods. However, the paper is undermined by significant overclaims (layer selection, optimization-free framing, simultaneous alignment) and insufficient empirical validation (undefined baselines, no statistical rigor, missing ablations). The theoretical framework is largely decorative rather than foundational.

The paper is not fatally flawed — the method could work and the idea could be useful — but in its current form the claims outrun the evidence. A major revision addressing the evaluation gaps and correcting the overclaims could make this a solid contribution.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>