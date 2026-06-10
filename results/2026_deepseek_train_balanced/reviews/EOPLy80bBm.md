## Summary

This paper conducts a systematic empirical and theoretical study disentangling the roles of data representation (hidden states, training dynamics, gradients) and selection objectives (difficulty, diversity, validation performance) in data pruning for NLP fine-tuning. The authors evaluate six representative methods across three tasks (classification, multiple-choice, generation) and multiple budgets. The central finding is that representation choice often dominates algorithm choice: gradient-based methods consistently outperform cheaper alternatives, hidden-state methods fail to beat random selection, and the same algorithm selects very different instances under different representations. The paper also identifies LESS's label-skew failure mode on imbalanced data and shows that Hard-to-Learn and Memorization are moderately correlated.

## Strengths

1. **Theoretical analysis of representation signals (§3.2).** The paper mathematically derives what each representation type encodes for instance similarity. The key result — that gradient similarity captures label agreement *and* prediction error magnitudes, while hidden-state similarity encodes neither — is clearly derived and directly explains why gradient-based methods outperform cheaper alternatives. This is a genuinely useful formalization.

2. **Clean synthetic experiments demonstrating representation-algorithm interaction (§3.3, Figure 1).** Using 2D Gaussian data, the paper visually proves that the same algorithm (Prototypicality, LESS) selects fundamentally different instances when operating on hidden states vs. gradients. This provides strong causal intuition that is rare in the data pruning literature, which usually treats representation and algorithm as a monolith.

3. **Useful negative result: hidden-state methods do not beat random (§4.4, Figure 4a).** The paper tests whether fine-tuned hidden states improve performance and finds they do not. This is a clear negative result that challenges a natural counter-hypothesis and provides practical guidance.

4. **Identification and mechanistic explanation of LESS's label-skew failure (§4.3).** The paper discovers that LESS over-selects majority-class instances on imbalanced data (e.g., 90% non-hateful on CAD), provides a theoretical explanation (gradient similarity is label-dependent due to anisotropic hidden-state space), validates with selection-ratio analysis (Figure 3), and proposes a practical mitigation. This is a concrete, actionable finding.

5. **Consistency analysis showing Hard-to-Learn can approximate Memorization (§4.2).** The finding that these two methods are moderately correlated (while having very different computational costs) is practically useful for practitioners choosing between efficiency and performance.

## Weaknesses

### Major

1. **The central ablation (§4.4) is methodologically underspecified.** The paper's headline claim — that "representation plays a more fundamental role than selection algorithm" — rests on an experiment that "combines all three different data representations with the selection algorithms of S2L, Prototypicality, and LESS" (line 143). However, the paper never specifies how each incompatible combination is operationalized. LESS is natively defined as a gradient dot product (line 57); what computation replaces this when applied to hidden states or training dynamics? S2L works on loss *trajectories* (per-epoch losses); how is it adapted to operate on a single hidden-state vector? The paper claims these algorithms are "representation-agnostic" (line 89) without justifying the claim or documenting the actual computation for each of the 3×3=9 combinations. The synthetic experiments (§3.3) implicitly demonstrate some combinations, but the main NLP-task ablation (Figures 4b–4c) provides no implementation detail. Without this specification, the reader cannot assess whether the observed patterns are meaningful or artifacts of ad-hoc design choices. This does not invalidate the claim, but it weakens the confidence in the paper's primary conclusion.

2. **No statistical uncertainty quantification in a comparative empirical study.** The paper reports single-curve results for each method–budget combination across multiple tasks. There are no confidence intervals, variance bars, or statements about number of independent runs with different random seeds. Data pruning is stochastic (subset selection involves randomness; reference model training is non-deterministic). A comparative claim like "gradient-based methods consistently outperform cheaper alternatives" would be materially strengthened by variance estimates. This is especially important for effects like "hidden-state methods do not beat random," where small performance differences could flip under noise.

### Minor

3. **Noise detection experiment concludes far beyond its evidence (line 151).** The experiment measures the *percentage of noisy instances selected* and finds that no method effectively avoids selecting noisy instances. From this, the paper concludes that "none of the data pruning methods are suitable for training with noisy data." This conflates two distinct goals: selecting the best training subset (which may include hard/noisy instances) vs. detecting/filtering noise. The conclusion is broader than the experiment supports. A more precise claim would be: "under the framing of avoiding selection of corrupted instances, all tested methods fail."

4. **Spearman correlation values not reported numerically (§4.2).** The paper describes correlations as "moderate" (line 125) but does not state the actual Spearman *r* values in the text (they are only in the figures, which the parser-stripped version cannot display). Numerical values should be stated explicitly.

5. **Asymmetric comparison in LESS label matching (Figure 2f).** LESS on CAD is evaluated both without and with forced label matching, and only the matched version is competitive. Other methods (Hard-to-Learn, Prototypicality, etc.) are not tested with a comparable balancing correction. The paper acknowledges this asymmetry in prose but does not assess whether applying a similar constraint would change their relative ordering. Since LESS's competitiveness partly depends on this correction, the comparison is not fully controlled.

### Trivial

6. The "Dummy" baseline's application to the generation task (DialogSum) is unclear — what does "a randomized predictor" mean for summarization evaluated with ROUGE-L?

## Nice-to-Haves

- **Specify the implementation of each representation–algorithm combination in §4.4** (or remove combinations that are not well-defined) and discuss whether the resulting comparisons are meaningful.
- **Quantify computational cost trade-offs.** A major finding is that gradients work better but are expensive. Providing runtime or FLOPs estimates would give practitioners actionable guidance beyond "very costly."
- **Report Spearman *r* values numerically** in the text.
- **Reframe the noise detection conclusion** to match what the experiment actually tests.

## Removed Points

These points were raised by reviewers but are filtered out per the guidelines:
- **"The theoretical analysis is quite basic"** — This is a subjective opinion about depth, not a well-formed weakness. The analysis is appropriate for an empirical/analytical paper and serves as motivation for the experiments.
- **"Hidden-state methods were designed for image classification, not NLP fine-tuning"** — The paper's scope is NLP fine-tuning; evaluating methods within that scope is appropriate. This is a contextualization suggestion, not a weakness.
- **"The paper should contextualize why hidden-state methods underperform"** — The paper *does* explain this (pretrained hidden states lack label information), and the follow-up experiment with fine-tuned hidden states directly tests the counter-hypothesis. The criticism is already addressed.
- **"Missing related works"** — Cannot be verified without external sources; removed per guidelines.
- **Various formatting/style nitpicks** — Removed per guidelines as parser artifacts.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Specify all 9 representation–algorithm combinations in §4.4.** For each combination, state the exact computation performed (e.g., "for LESS with hidden states, we replace the gradient dot product with cosine similarity between mean-pooled hidden states of training and validation instances"). If some combinations are not semantically meaningful, remove them and qualify the claim accordingly.

2. **Add variance estimates.** At minimum, report results from a small number of random seeds (e.g., 3) with error bars for the key findings (Figures 4b–4c, the comparison of gradient vs. hidden-state methods). Alternatively, acknowledge single-run results as a limitation.

3. **Report numerical Spearman *r* values in the text** for the key correlations reported as "moderate."

4. **Test other methods with label balancing** to make the LESS comparison fair, or explicitly justify why only LESS requires this correction.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>