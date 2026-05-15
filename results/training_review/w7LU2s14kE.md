Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

This paper investigates whether relation decoding in transformer LMs (the computation that maps a subject representation to a corresponding object representation) is approximately linear. The authors propose estimating a Linear Relational Embedding (LRE) via the Jacobian of the model's internal function, averaged over a small number of examples. They test this on GPT-J, GPT-2-XL, and LLaMA-13B across ~47 relations spanning factual, commonsense, linguistic, and bias categories, finding that for ~48% of relations the LRE achieves >60% faithfulness. They provide causal validation by inverting the LRE to edit subject representations and change model predictions, and introduce an "attribute lens" application to reveal latent knowledge even when the LM outputs falsehoods. The paper also identifies relations that are not linearly decodable, preventing overclaiming.

## Strengths

- **Principled, probe-free estimation method.** The LRE is derived directly from the LM's own Jacobian (first-order Taylor expansion of the internal function F), avoiding the pitfalls of training separate probing classifiers that may learn to solve the task themselves. This is a clean and theoretically motivated approach.

- **Causal validation via editing.** The paper goes beyond correlational faithfulness by showing that inverting the LRE to edit subject representations can causally change the model's predicted object, matching an oracle substitution baseline (Fig. 5, §4.2). This provides stronger evidence that the linear approximation captures something about the model's actual computation, not just correlation.

- **Honest reporting of negative results.** The paper explicitly identifies relations (e.g., Company CEO) where faithfulness remains below 6% despite accurate LM predictions, and speculates about why (large output spaces, multi-layer encoding). This heterogeneity prevents overclaiming and makes the finding more credible.

- **Useful application (attribute lens).** The attribute lens demonstrates a practical use case: decoding object distributions from intermediate representations even when the LM is baited into outputting a falsehood, evaluated on ~12k adversarial prompts (Table 2). This shows the LRE can surface latent knowledge that doesn't reach the output layer.

- **Observation of a "mode switch" in later layers.** The finding that LRE faithfulness drops sharply after a certain layer, and that removing relation-specific context delays this drop (§4.3, Fig. 8), offers an interesting insight into how transformer representations transition from encoding relational knowledge to next-word prediction.

## Weaknesses

### Fatal
None.

### Major

- **Unclear whether faithfulness evaluation uses held-out subjects (§3.2, §4.1).** The paper states that LREs are estimated from n=8 examples and that results are averaged over 24 trials with random draws, but it never explicitly states whether the faithfulness metric (Eq. 3) is evaluated on the *same* subjects used for estimation or on *disjoint, held-out* subjects. If evaluation is performed on subjects included in the estimation set, the reported numbers reflect *training fit* rather than generalization, which would substantially weaken the central claim that "48% of relations have robust LREs." The 24-trial random resampling provides some protection, but without explicit clarification this is a meaningful ambiguity that undermines confidence in the results. This is the single most important issue for the authors to address.

- **Linear regression baseline is not a meaningful test of linearity (§4.1).** The paper compares LRE (Jacobian-based) against a linear regression trained on the same n=8 examples to predict objrep from subjrep. With 8 examples and presumably ~4096-dimensional representations, this regression is severely underdetermined, so its poor performance is expected. The comparison does not test whether the true underlying mapping is linear — it primarily reflects that the Jacobian estimator is more *sample-efficient* because it leverages gradient information. A proper test of linearity would train the regression on many more examples (e.g., all available correct subjects) with appropriate regularization. Without this, the results conflate "the relation is linear" with "our estimation method works well with few shots."

### Minor

- **Attribute lens evaluation lacks a Logit Lens baseline (§5).** The distracted-prompt experiment (Table 2) shows that the attribute lens recovers correct knowledge within top-3 predictions, but it does not compare against the standard Logit Lens or a linear shortcut probe under the same adversarial conditions. Since Logit Lens is a natural and well-known baseline for decoding from intermediate representations, its absence makes the reported accuracy numbers difficult to interpret — they may be impressive or merely adequate.

- **Mode-switch analysis is primarily qualitative and limited to one example (§4.3, Fig. 8).** While the paper references the appendix for additional sweeps, the main paper's discussion centers on a single illustrative relation. The claim that a "mode switch" occurs would be stronger with a quantified analysis showing how many relations exhibit this pattern and whether it correlates with LRE quality.

- **Causality hyperparameter selection could introduce selection bias (§4.2).** Hyperparameters (layer, rank) are selected via grid search to maximize *causal influence* on each relation. This means causal efficacy is reported under optimal conditions, not averaged over reasonable ranges. The paper acknowledges that the faithfulness–causality correlation weakens when hyperparameters are chosen for faithfulness (footnote in §4.2), which somewhat undercuts the claim that these metrics are tightly coupled. While not fatal, this nuance should be more prominently discussed.

- **Abstract says "from a single prompt" but method uses n=8 examples.** The abstract's phrasing slightly overstates the minimal-data nature of the method. The Jacobian is indeed computed from a single forward pass of the LM, but the LRE is averaged over 8 examples. This is a minor imprecision.

### Trivial
None.

## Nice-to-Haves

- A systematic analysis of *why* certain relations (e.g., Company CEO) fail to be linearly decodable, comparing output vocabulary size, embedding norms, or number of layers where object information appears, would make the findings more actionable.
- Testing on more recent model families (Llama-3, GPT-4 class) would strengthen claims about generality.
- A sensitivity analysis showing faithfulness as a function of n (number of estimation examples) would clarify how sample-efficient the Jacobian estimator is.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **Beta hyperparameter not defined/justified.** The paper states β is fixed per LM and references Appendix §A.2 for empirical measurements and selection details. Per our guidelines, criticisms about content deferred to an appendix that the parser strips are not valid — the details exist in the original submission. A sensitivity analysis would be a nice addition but is not a required flaw.

2. **"subjrep already incorporates context c, making the LRE test less stringent."** This misunderstands the paper's design. The LRE is defined as an approximation of F(subjrep, c), so the context is by design part of the input to the function being approximated. The paper is testing whether the mapping from *context-enriched* subject representations to object representations is linear — this is exactly the right test for the claim being made.

3. **"Identity and Translation baselines are expected to be low."** The paper uses these baselines to show that both the projection and bias terms of the affine LRE are necessary — a legitimate and controlled use of baselines. They are not intended as strong competitors.

4. **"Causality is tested only for relations where LREs are faithful — circular."** The paper tests all relations; hyperparameters (layer, rank) are per-relation optimizations, not a filter on which relations are evaluated. The causality experiment includes relations across the faithfulness spectrum, and Fig. 6 shows the correlation between the two metrics.

5. **Concerns about model release status or availability of cited prior work.** All cited models, datasets, and tools exist in the literature as of the current date.

## Novel Insights

Beyond verifying linearity for a subset of relations, two observations stand out. First, the "mode switch" finding — that LRE faithfulness drops sharply in later layers, and that removing relation-specific context delays this drop — suggests that transformer representations undergo a functional transition from relation-decoding to next-word-prediction. This is a genuinely interesting dynamical observation that merits deeper study. Second, the finding that some relations (e.g., Company CEO) are *not* linearly decodable despite being accurately predicted, and that this correlates with large output spaces (person/company names), provides a concrete boundary condition on when linear approximation works. This negative result is arguably as valuable as the positive results for understanding how LMs encode knowledge.

## Suggestions

1. **Clarify the train/evaluation split explicitly** — state whether faithfulness is measured on the same subjects used for LRE estimation or on held-out subjects. If the 24-trial procedure evaluates on all available subjects in each trial, report both training-set and held-out faithfulness separately.

2. **Add a proper linear regression baseline** trained on all available correct subjects (e.g., 50+ examples) with ridge or low-rank regularization. If this still underperforms the Jacobian-based LRE, it substantially strengthens the claim that the Jacobian method captures something special about the model's computation.

3. **Add Logit Lens as a baseline** in the attribute lens distracted-prompt experiment to contextualize the reported top-3 recall numbers.

4. **Report the chosen β value(s)** and briefly describe the selection criterion in the main paper, not just the appendix.

## Score and Decision

**Originality:** Good — connecting the LRE framework to Jacobian-based extraction from transformer internals is a novel methodological contribution.

**Importance of research question:** High — understanding whether and how LLMs implement linear relational computations is directly relevant to mechanistic interpretability.

**Claims well-supported:** Partially. The core results are plausible and several experiments point in the same direction, but the ambiguous train/test separation and the weak linear regression baseline leave room for over-interpretation.

**Soundness of experiments:** Adequate but with important gaps. The faithfulness and causality experiments are well-designed in principle but suffer from incomplete reporting (train/test split, β selection) and one unfair baseline comparison.

**Clarity of writing:** Good — the paper is well-structured and the main ideas are communicated effectively, though some experimental details could be more precise.

**Value to community:** Moderate to high. The LRE estimation method and attribute lens are likely to be reused, and the negative results provide useful calibration for future interpretability work.

**Overall:** The paper makes a solid empirical contribution with a clean method and several well-executed experiments. However, the two main weaknesses — the ambiguous train/test separation and the unfair linear regression baseline — are substantive enough to prevent the paper from fully establishing its central claims in the current form. The contribution is promising and the fix is achievable (clarify the split, add a proper baseline), but in its present form the evidence does not fully meet the bar for acceptance at a top venue.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>