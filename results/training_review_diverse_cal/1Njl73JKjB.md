Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

This paper proposes a framework for evaluating sparse feature dictionaries (e.g., SAEs) by comparing them against *supervised* feature dictionaries derived from task-relevant attributes. On the IOI task with GPT-2 Small, the authors show that mean-aggregation supervised dictionaries achieve near-perfect reconstruction sufficiency/necessity, >80% attribute-editing accuracy, and perfect interpretability scores. They then use these supervised dictionaries as a benchmark to evaluate task-specific and full-distribution SAEs, finding that SAEs capture interpretable features but fall short on sparse controllability. The paper also documents two qualitative phenomena in SAE training — feature occlusion and feature over-splitting — reproduced in toy models.

## Strengths

1. **Principled evaluation framework with supervised dictionaries as a benchmark.** The paper proposes a concrete, replicable three-step methodology (parametrize inputs via attributes, compute supervised dictionaries, evaluate unsupervised dictionaries) to address the lack of ground-truth features in SAE evaluation. This is operationalized with three well-motivated tests (sufficiency/necessity, sparse controllability, interpretability), providing a more objective basis for comparing feature dictionaries than existing indirect metrics (auto-interpretability, MMCS, toy models), which the paper surveys in Section 7.

2. **First demonstration of high-quality supervised feature dictionaries on a realistic LLM task.** The paper shows that mean feature dictionaries computed from IOI attributes achieve near-perfect logit difference recovery (Figure 2) and >80% attribute-editing accuracy (Figure 3) for the IOI task in GPT-2 Small. This validates that task-relevant attributes are linearly represented and can be disentangled in a realistic setting — a result the paper explicitly claims as a first (abstract, Section 1).

3. **Identification of novel qualitative phenomena in SAE training.** The paper documents and systematically investigates feature occlusion (higher-magnitude attributes overshadowing causally relevant lower-magnitude ones) and feature over-splitting (binary attributes split into many non-interpretable features). Both are demonstrated through controlled experiments (Figure 4, Section 5) and reproduced in toy models, providing insights into SAE behavior not previously documented.

4. **Interpretation-agnostic controllability evaluation.** The sparse controllability test (Section 3.3) is designed as a combinatorial optimization problem over dictionary features, avoiding the need to assume features correspond to human-chosen concepts. This allows fair evaluation of any feature dictionary regardless of its interpretability.

5. **Causal evaluation of interpretability beyond correlation.** Test 3 includes interpretation-aware sufficiency/necessity and sparse control (Section 3.4). Results show that keeping/removing high-F1 features preserves/degrads model performance (Section 5.2), strengthening the validity of the interpretability method beyond correlational measures alone.

## Weaknesses

### Major

1. **Circularity risk in the supervised-dictionary validation.** The supervised dictionaries are validated using the *same* tests (sufficiency/necessity, controllability, interpretability) that later serve as benchmarks for SAEs. The paper acknowledges this (Section 7, Limitations): "there could be many parametrizations that are just as consistent." However, the acknowledgment is brief relative to how central this assumption is to the entire framework. If the supervised dictionaries capture spurious correlations (e.g., between IO name and syntactic position beyond what Pos captures) rather than the causally relevant features, they could still pass the tests while systematically favoring certain kinds of SAE features over others. The MSE alternative (Section 4.1) is mentioned but not compared in detail for the IOI case. This matters because the entire benchmark rests on the supervised dictionaries being a reasonable "skyline"; their validity is not independently verifiable.

2. **Asymmetric advantage for supervised dictionaries in the controllability test.** The sparse controllability test compares against the "ground truth" edit of directly replacing an activation with its counterfactual (Section 3.3). For supervised dictionaries, the edit (subtract one mean feature, add another) is a closed-form operation that aims directly at this ground truth. For SAEs, the edit must be discovered via greedy search over an exponentially large feature space, and the metric is distance to that same counterfactual activation. This creates an inherent structural asymmetry: supervised dictionaries are guaranteed to find the optimal edit for the chosen objective by construction, whereas SAEs can only approximate it. The Pareto curves (Figure 5) help by showing trade-offs, but the x-axis (weight removed) is also normalized relative to the supervised weight, so the comparison remains anchored to supervised dictionaries' frame of reference. The conclusion that supervised dictionaries are "better" on controllability partly reflects this built-in advantage.

### Minor

1. **Greedy optimization gap in sparse controllability is not quantified.** The greedy algorithm (Section 5.1) is described as minimizing ℓ₂ distance to the counterfactual activation. The paper acknowledges the problem is NP-hard (SubsetSum reduces to it) but does not report how well the greedy solution approximates the true minimum. Without this, it is unclear whether the worse performance of SAEs in controllability partly reflects optimization difficulty rather than representation quality. Reporting the gap between the greedy solution and an oracle bound (e.g., by comparing to the supervised edit when applicable) would clarify this.

2. **Interpretability search space: only maximum F₁ reported, not its distribution.** The interpretability method considers unions of up to 10 attribute values (30 for OpenWebText) and reports the maximum F₁ score for each feature. It matters whether this maximum is peaked or broad: if many different candidate interpretations achieve similar F₁, the feature is not uniquely interpretable, weakening the interpretability claim. The paper should report the distribution of F₁ scores across candidate interpretations, not just the maximum.

3. **Frozen-decoder baseline is informative but insufficiently controlled.** The frozen-decoder baseline (Section 5.1) shows that trained decoders outperform random ones. However, it does not rule out that the encoder learns to select from a large set of random directions that happen to correlate with attributes — the controllability might come from the encoder's selection, not from any meaningful structure in the decoder. A stronger baseline would match the reconstruction quality (ℓ₀, MSE) of the trained SAE while keeping random features, isolating the contribution of feature learning.

4. **Occlusion analysis: toy model assumes simplest geometry.** The toy model used to reproduce occlusion (Section 6.1) assumes i.i.d. isotropic features — exactly the setting where SAEs should work best. Showing that occlusion occurs when features have more realistic correlations (e.g., non-isotropic, correlated) would strengthen the claim that it is a general phenomenon rather than an artifact of the specific geometry. The paper's own surgical experiment (reducing IO features → more S features discovered) is the more compelling evidence here.

5. **Over-splitting: conditions for optimality vs. artifact not fully characterized.** The paper shows over-splitting is not random (different seeds/datasets give similar splits) and reproduces it in a toy model. However, it does not characterize the conditions under which over-splitting is *optimal* for the SAE's training objective versus an artifact of training dynamics or initialization. This limits practical insight: if over-splitting is often optimal for the SAE objective, then requiring monosemantic features for binary attributes may be a misguided design goal.

### Trivial

None.

## Nice-to-Haves

- **Automate or provide heuristics for attribute discovery.** The framework currently relies on prior circuit analysis (IOI circuit from Wang et al. 2022) to choose attributes. For a new task where the circuit is unknown, guidelines for finding attributes that yield good supervised dictionaries (e.g., start with input tokens; check that the dictionary passes sufficiency/necessity above a threshold) would dramatically increase portability.
- **Give a decision rubric for interpreting the three tests together.** The paper presents four sets of results (sufficiency/necessity, sparse controllability, correlational interpretability, causal interpretability). Stating explicitly what pattern of outcomes implies (e.g., "if a dictionary passes test X but fails test Y, conclude Z") would make the framework more prescriptive.
- **Quantify sensitivity to attribute choice.** The paper mentions experimenting with other attribute sets (appendix references) but does not show in the main text how different attribute choices affect the supervised dictionary quality or the comparisons.
- **Consider a controllability normalization.** To address the asymmetry in point Major #2, one could normalize the SAE's controllability score by what can be achieved with a random dictionary of matched sparsity, or by the best achievable edit using the same greedy algorithm on the supervised dictionary's features (holding the optimization procedure fixed).

## Removed Points

These points were flagged by reviewers but removed after verification against the paper:

- **"MSE alternative not compared in detail for IOI case"**: The paper explicitly discusses the MSE alternative (Section 4.1, lines 509–515) and references an appendix with detailed comparisons. The criticism is inaccurate — the comparison exists, it is simply deferred to the appendix as is standard.
- **"Supervised dictionaries = mean activations assumes linear/additive decomposition"**: This is not an unstated assumption; it is the explicit modeling choice (Eq. 1, Section 4.1). The paper states it directly and motivates it from the linear representation hypothesis.
- **Generic strengths from Strength Finder about "addressing an important problem" or "interesting question"**: Dropped because they lacked specific evidence or citation. The retained strengths all have concrete, verifiable content.
- **"The paper should also cover more tasks / models"**: Scope-creep demand. The paper is a *methodology* paper demonstrated on one task and model, which is standard for this type of contribution. Single-task demonstration is appropriate for introducing a new evaluation framework.
- **"Cannot be independently verified" / "not yet released" type criticisms**: None present; this rule is noted as satisfied.

## Novel Insights

The most valuable insight emerging from the reviews is that the paper's core weakness — the circularity of validating supervised dictionaries with the same tests they later benchmark — has a structural counterpart in the comparison itself: supervised dictionaries have a *definitional* advantage in the controllability test because the test's objective (minimize ℓ₂ distance to counterfactual activation) is exactly what the mean-feature edit achieves by construction. This means the "skyline" is not merely a high bar but a qualitatively different kind of bar — one that SAEs cannot cross even in principle unless they learn something isomorphic to the mean features. The paper's Pareto analysis partially addresses this by reframing the comparison in terms of trade-offs, but it does not fully resolve the interpretive question of how much of the SAE gap is due to representation quality versus objective mismatch. The occlusion and over-splitting phenomena, however, are robust observations that hold regardless of this structural issue, and they provide concrete failure modes that the field can address independently.

## Suggestions

1. **Quantify the greedy optimization gap.** Report the ℓ₂ distance between the greedy solution and the supervised closed-form edit (when editing the same attribute) to distinguish optimization failure from representation failure in the SAE controllability results.
2. **Report F₁ score distributions, not just maxima.** Show histograms of F₁ scores across candidate interpretations for a sample of features to establish whether the top interpretation is uniquely good or one of many similarly scoring candidates.
3. **Strengthen the frozen-decoder baseline.** Match reconstruction quality (ℓ₀ and MSE) between the frozen-decoder SAE and the trained SAE to rule out the possibility that controllability differences stem from reconstruction quality rather than feature meaningfulness.
4. **Flag the controllability asymmetry prominently.** Add a brief discussion (even 2–3 sentences) in the evaluation methodology section acknowledging that the supervised edit is closed-form optimal for the chosen objective, while the SAE edit must be discovered via search over a combinatorially large space. This would help readers correctly interpret the gap.

## Score and Decision

**Overall assessment.** This is a solid methodology paper that makes a genuine contribution to a pressing problem in mechanistic interpretability. The framework is well-motivated, carefully scoped, and honestly discusses its limitations. The qualitative phenomena (occlusion, over-splitting) are interesting and worth reporting in their own right. The two major weaknesses — the circularity risk and the asymmetric controllability comparison — are real but not fatal; the paper acknowledges the former explicitly and the latter is partially mitigated by the Pareto analysis. The paper does not claim to have solved evaluation, only to have taken a principled step, and it delivers on that promise.

**Decision: Accept.** The paper would benefit from addressing the minor weaknesses (greedy gap quantification, F₁ distribution reporting, stronger frozen-decoder baseline) and acknowledging the asymmetry more explicitly, but these are revision-level fixes, not reasons for rejection. The framework's value to the interpretability community — as a methodology that can be adapted to other tasks and used to compare SAE variants — justifies acceptance now.

**Score: 7.0** — A good paper, accepted. The contribution is solid and well-executed. The limitations are honestly discussed and the main claims are supported by the evidence. The weaknesses identified are addressable and do not undermine the core contribution.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>