Now I have all the information needed. Let me write the final consolidated review.

## Summary

This paper proposes a framework for evaluating sparse autoencoders (SAEs) by constructing "supervised feature dictionaries" from human-chosen attributes (IO, S, Pos) on the IOI task in GPT-2 Small. These supervised dictionaries serve as a benchmark or "skyline" against which unsupervised dictionaries (task-specific and full-distribution SAEs) are compared along three axes: sufficiency/necessity of reconstructions, sparse controllability, and interpretability. The paper finds that supervised dictionaries perform near-ideally, while SAEs capture interpretable features but fall short on controllability. Two qualitative phenomena—feature occlusion and over-splitting—are documented and reproduced in toy models.

## Strengths

- **Novel three-axis evaluation framework.** The paper proposes a structured methodology (Test 1: sufficiency/necessity, Test 2: sparse controllability, Test 3: interpretability with causal checks) that moves beyond indirect metrics like MMCS or auto-interpretability alone. The framework is clearly described and principled in its design (Section 3).

- **Supervised dictionaries genuinely work well on the IOI task.** The supervised mean-feature dictionaries achieve near-perfect reconstruction quality (Figure 1, orange bars) and enable editing any single attribute by replacing exactly one feature with >80% agreement with ground-truth interventions (Figure 2, orange bars). This validates the attribute choice and confirms that sparse linear decomposition is feasible at this circuit location.

- **Agnostic controllability test is well-designed.** Test 2 operates via combinatorial optimization over feature subsets without requiring any human interpretation of features (Section 3.2). This is a real methodological contribution: it allows evaluation of control even when the dictionary's ontology differs from the chosen attributes.

- **Qualitative findings (occlusion, over-splitting) are interesting and reproduced in toy models.** The demonstration that SAEs systematically learn only the higher-magnitude of two co-occurring attributes (occlusion) and split binary concepts into many uninterpretable features (over-splitting) is novel, empirically grounded (Section 6), and reproduced in simple toy models, suggesting the phenomena are not artifacts.

## Weaknesses

### Fatal
None.

### Major

- **Confounded comparison between task-specific and full-distribution SAEs.** The paper's comparative claim that "task-specific SAEs allow us to edit attributes by changing fewer features compared to full-distribution SAEs" (line 112) is based on SAEs trained on dramatically different data distributions and sizes (IOI dataset vs. OpenWebText) without controlling for training set size, number of features relative to data, or hyperparameter tuning. The paper acknowledges it "did not perform exhaustive hyperparameter tuning" (lines 605–610), but the comparative claim is presented as an empirical finding, not just a methodological demonstration. The frozen-decoder baseline partially controls for the task-specific SAEs, but there is no equivalent control for the distribution-size confound.

- **No error bars, variance reporting, or significance tests on quantitative results.** Figures 3, 4, 5, and 6 report single runs without confidence intervals, variance across seeds, or significance tests. SAE training has substantial stochasticity (different initializations, different data subsets), and the absence of any variance quantification means the paper's comparative claims (e.g., "full-distribution SAEs require a significantly larger number of features," lines 728–730) are not statistically grounded.

- **Structural reliance on human-chosen attributes limits what the framework can claim.** The paper acknowledges this as its "central conceptual limitation" (Section 7), and it is a real constraint on the contribution. The evaluation framework measures how well unsupervised dictionaries align with the *chosen* attribute decomposition, not feature quality per se. The agnostic tests (Test 1, Test 2) partially mitigate this, but Test 2 still targets the chosen attributes as the editing objective, and Test 3's interpretability search is anchored to unions/intersections of the same attributes. The paper would be strengthened by evaluating on at least one task without known circuit analyses or on multiple distinct attribute sets.

### Minor

- **Single task and single model.** The paper only evaluates on IOI / GPT-2 Small, and acknowledges this limitation (line 1040–1041). This makes it unclear how well the framework generalizes to other tasks or models.

- **No explicit held-out evaluation for task-specific SAEs.** The paper does not state whether evaluation prompts were disjoint from training prompts for task-specific SAEs, raising the possibility of overfitting inflating the reported performance.

- **Greedy controllability algorithm is uncharacterized.** The paper correctly notes the optimization problem is NP-hard (lines 631–632) and uses a greedy algorithm, but does not evaluate how far from optimal the greedy solutions are, even for small feature sets where exhaustive search would be feasible. Without this, it is unclear whether the reported controllability results reflect the dictionary's quality or the algorithm's limitations.

- **Qualitative phenomena analysis is narrow.** Occlusion and over-splitting are demonstrated only for one specific location (L10H0 queries) using task-specific SAEs. The toy models are suggestive but the analysis remains preliminary.

### Trivial

- The paper's claim that this is "the first time such a disentanglement has been achieved in a realistic LLM task" (footnote, line 99–102) is a strong assertion that would benefit from more careful qualification given prior work on linear probes and sparse coding in LLMs.

## Nice-to-Haves

- Train a full-distribution SAE on a matched-size sample of OpenWebText to control for dataset size effects in the comparison.
- Report results from multiple SAE training seeds with confidence intervals or error bars.
- Apply the framework to at least one additional task where attributes are not already known from circuit analysis.
- Characterize the greedy algorithm's approximation quality via exhaustive search for small k.

## Removed Points

These points from the input reviews were removed with brief justification:

- **"Circular evaluation framework invalidates the paper's headline claims" (Harsh Critic, Critical Issue #1).** The paper explicitly acknowledges this limitation (Section 3, lines 253–257; Section 7, lines 1019–1024), positions supervised dictionaries as a benchmark rather than ground truth, and designs agnostic tests to mitigate the issue. The criticism is fair as a structural limitation but not fatal—the paper is transparent about it, and the contribution is a framework for relative comparison given a chosen attribute set. Moved from "Fatal" to "Major" above.

- **"Test 1 measures approximation quality not interpretability/is unfair to SAEs."** The paper explicitly states Test 1 "only measures the quality of the dictionary as a whole, and not how effectively and sparsely it disentangles any hypothetical concepts" (lines 306–308). The reviewer's characterization is a strawman. Removed.

- **"Claim about 'first time such a disentanglement' is unverifiable."** The paper cites its own contribution; per hard rules, questioning a paper's self-attribution is not a valid criticism of factual accuracy about external references. Removed.

- **"Interpretability methodology is still anchored to chosen attributes."** The paper acknowledges this (Section 3, lines 409–428) and explains why this tradeoff is necessary for human-useful evaluations. This is a known limitation, not an unmentioned flaw. Removed.

- **"Limitation section reads as if the problem is minor."** Purely the reviewer's opinion about tone, not a substantive criticism. Removed.

- **Missing related work.** Per hard rules, I cannot confirm the existence of missing references. Removed.

- **Formatting/style nitpicks and reproducibility complaints about trivial implementation details.** Removed per hard rules.

- **Strength Finder's generic strengths** (e.g., "this paper addressed an important problem"). Dropped as superficial or redundant with more specific strengths listed above.

## Novel Insights

The most interesting observation emerging from these reviews—beyond the paper's own contributions—is that the evaluation framework's core strength and core weakness are two sides of the same coin: by grounding evaluation in human-chosen attributes, the paper gains concreteness and measurability but loses the ability to make absolute claims about SAE feature quality. The tension between "agnostic" tests and attribute-anchored evaluation is not fully resolved, and future work would benefit from developing evaluation methods that can validate feature quality without committing to a particular decomposition—perhaps by cross-validating across multiple attribute sets or by using behavioral tests that are provably independent of the feature ontology. The occlusion and over-splitting findings suggest that SAEs may systematically fail in ways that standard reconstruction metrics (MSE, ℓ0) do not capture, which is a genuinely important observation for practitioners.

## Suggestions

1. **Address the confounded comparison** by including a full-distribution SAE trained on a matched-size sample of OpenWebText, or reframe the task-specific vs. full-distribution comparison as purely illustrative of the framework's ability to distinguish dictionary classes (which the paper partially does already) rather than as a substantive empirical finding.

2. **Add variance reporting** from at least 3–5 random seeds for key quantitative results (Figures 3, 4, 5), or at minimum report the range across seeds. This is essential given the known stochasticity of SAE training.

3. **Apply the framework to at least one more task** (e.g., docstring completion, sentiment classification) to demonstrate that the methodology is not tailored to IOI's specific structure (known circuit, independent attributes). This would significantly strengthen the claim of generalizability.

4. **Benchmark the greedy algorithm** against exhaustive search for small edit budgets (k ≤ 3) to bound approximation quality and increase confidence in the controllability results.

5. **Explicitly state whether evaluation prompts are disjoint from training prompts** for the task-specific SAEs, and if they are not, add a held-out evaluation.

## Score and Decision

The paper proposes a genuinely useful evaluation framework and documents interesting qualitative phenomena. However, the experimental support for its central comparative claims is weakened by a confounded experimental design (task-specific vs. full-distribution SAEs trained on incomparable data) and the absence of any variance reporting. The framework itself is the main contribution, but the paper's strongest claims about SAE quality differences rest on empirical comparisons that are not rigorously controlled. Major revisions—particularly addressing the confounded comparison and adding statistical grounding—would be needed before the paper's empirical conclusions are reliable.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>