Now I have a thorough understanding of both the paper and the reviews. Let me produce the final consolidated review.

## Summary

The paper proposes a simple meta-heuristic for detecting distribution shift in offline model-based optimization (MBO): train a binary classifier to distinguish training data from designed sequences, and use its logit scores as a metric for selecting reliable designs. The method is validated on a 2D toy problem, a simulated protein folding task, and — most importantly — a real-world AAV capsid design experiment where ~5,000 sequences across 15 iterations and 9 trajectories were experimentally measured. The real-world experiment documents severe distribution shift (surrogate MSE rising sharply, >60% of designs becoming adversarial by later iterations) and shows that OOD scores separate functional from non-functional variants and can guide sequence selection with lower regret compared to deep ensemble uncertainty.

## Strengths

- **Rare real-world validation of MBO under distribution shift.** Most MBO papers benchmark only on simulated tasks. This paper conducts a real AAV experiment, experimentally labels every step of multiple optimization trajectories (~5,000 sequences), and directly measures surrogate model failure as a function of design iteration. The empirical documentation of shift severity in Figures 1 and 3a is a genuine contribution to the field.

- **OOD scores clearly separate functional from non-functional designs and outperform deep ensemble uncertainty.** In Figure 3b, the OOD score histograms for functional vs. non-functional variants show near-complete separation, while deep ensemble uncertainties exhibit substantial overlap. In Figure 3c, filtering by OOD scores consistently achieves lower regret across cutoff percentiles, often reaching zero regret. The advantage over deep ensemble uncertainty is clear and consistent.

- **The method is simple, theoretically grounded, and broadly compatible.** The derivation from the density-ratio trick (Equations 2–4) provides a principled justification. The method works with any surrogate model and any search algorithm, requires only a single additional classifier, and is accessible to practitioners without deep MBO expertise.

- **The experimental design is itself a methodological contribution.** The paper explicitly designs the AAV dataset to study distribution shift retrospectively by labeling every step of the optimization trajectory, addressing a critical gap where "there exists very few examples of real-world evaluation of design strategies, and none that explicitly study distribution shift."

- **Evaluation at multiple scales.** Toy (2D, visual validation), simulated protein folding (ESMfold as ground truth), and real-world AAV — this progression convincingly demonstrates the method's utility across increasing complexity.

## Weaknesses

### Fatal

None.

### Major

None. The potential concerns below are substantive but do not invalidate the paper's core claims.

### Minor

1. **The "far more severe" claim about real-world vs. simulated distribution shift lacks quantitative comparison in the main text.** The abstract and introduction state that "real world distribution shift is far more severe than observed in simulated settings," and the introduction says simulated settings "show much weaker distributions shift." However, the simulated protein experiment (Section 4.2) is described only qualitatively ("We see signs of distribution shifts caused by design") with no numbers presented alongside the real-world results. A direct quantitative comparison (e.g., MSE increase rate, fraction of adversarial examples across iterations) between the simulated and real experiments in the main text would substantiate this central claim.

2. **The OOD classifier is trained on all designed sequences and evaluated on the same set.** The classifier is "trained to classify the training data as negative samples and the designed sequences as positive examples" (Section 4.3), and OOD scores are then reported and used for selection on those same designed sequences. While this protocol matches the intended use case (train after generating designs, select from the same pool), it does not test whether the OOD scores generalize to designs from held-out trajectories or new MBO runs. A leave-one-starting-point-out or held-out-iteration evaluation would substantially strengthen claims about the method's robustness. As presented, the results are in-sample performance measures for this specific design run.

3. **Bootstrap resamples are used instead of trajectory-level variance estimates.** The error bars in Figure 3c come from "50 bootstrap resamples" of the same data, which measures estimation uncertainty from the current sample, not variability across different design trajectories or OOD classifier initializations. A more meaningful uncertainty estimate would partition trajectories (e.g., leave-one-starting-point-out) and report variance across folds.

4. **The LLM mention is a dangling sentence.** Line 146 states "We also evaluate the use of different model architectures including large language models (LLMs) pretrained on hundreds of millions of protein sequences adapted to our regression task with linear probing," but no results are presented and no appendix reference is given. If these experiments exist, they belong in the main evaluation or should be explicitly referenced; if not, the sentence should be removed.

### Trivial

- No discussion of computational overhead (training time, model size, data requirements) for the OOD classifier, which would support the practical simplicity argument.
- Three selection strategies are proposed (cutoff, stratified, utility) but only cutoff is tested. The paper would be slightly stronger with at least a brief evaluation of one alternative.

## Nice-to-Haves

- Evaluate the OOD classifier with a trajectory-level held-out split (e.g., train on designs from 8 of 9 starting points, evaluate on the 9th).
- Test stratified or utility-based selection strategies beyond the cutoff scheme.
- Report training time and model size for the OOD classifier.
- Provide a side-by-side quantitative table comparing shift severity metrics (e.g., MSE growth rate, adversarial fraction) between the simulated and real experiments.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The comparison with Deep Ensemble uncertainties is rendered uninformative because the two metrics are not evaluated on the same footing (one is in-sample, the other is out-of-sample)."** — Removed because the comparison reflects the intended use case: OOD scores are designed to leverage post-design information, while deep ensemble uncertainties do not. The asymmetry is by design and the comparison remains informative as a practical head-to-head.

- **"The paper would be stronger if it demonstrated which selection strategy works best under a valid evaluation."** — Partially removed from weaknesses section; moved to Nice-to-Haves as it is a scope-expansion suggestion rather than a flaw.

- **Missing appendix content criticisms.** Removed per instructions — the parser strips appendix sections; they exist in the original submission.

## Novel Insights

None beyond the paper's own contributions. The core finding — that a simple binary OOD classifier trained on training vs. designed sequences can separate functional from non-functional designs and improve selection regret — is the paper's own contribution, not an insight that emerges from the reviews.

## Suggestions

- Add a quantitative comparison table (real-world vs. simulated) for shift severity metrics (e.g., surrogate MSE at final iteration, % adversarial examples) to substantiate the "far more severe" claim in the main text.
- Add at least one held-out evaluation (leave-one-trajectory-out) for the OOD classifier to demonstrate generalization.
- Either present the LLM results or remove the dangling sentence.

## Score and Decision

**Originality:** Good. The method itself is a straightforward application of density ratio estimation, but the real-world experimental design and the study of distribution shift in a deployed MBO setting are novel.
**Importance of research question:** High. Distribution shift is a critical problem in offline MBO, and practical detection methods are needed.
**Claims supported:** Reasonably well, though the "far more severe" claim needs quantitative backing and the OOD classifier evaluation would benefit from held-out validation.
**Soundness of experiments:** The real-world experiment is a strength. The evaluation protocol is not fundamentally flawed but could be stronger with held-out splits.
**Clarity of writing:** Clear and well-structured.
**Value to the research community:** Moderate-high. The real-world dataset and trajectory analysis are valuable resources, and the method is practically useful.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>