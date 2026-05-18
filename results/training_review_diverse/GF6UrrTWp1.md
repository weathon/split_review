Here is my consolidated final review.

---

## Summary

This paper proposes the "invariance starvation hypothesis" — that deep neural networks learn spurious correlations not because of an inevitable simplicity bias, but because they lack sufficient invariant information (data) to encode the true predictive function. Through reasoning tasks (LEGO, PVR), the authors show that scaling dataset size while maintaining the proportion of spurious samples eventually overcomes spurious correlations. In contrast, on vision (CelebA) and language (MultiNLI) benchmarks, the same approach can *exacerbate* spurious correlations, which the paper attributes to "atypical" samples containing poorly represented invariant features. A remedy is mentioned in the abstract and conclusion (sampling samples with easier invariant features) but is not experimentally validated.

## Strengths

1. **Identifies a genuinely counterintuitive failure mode in complex distributions.** The finding that adding more data from the *same* distribution (maintaining spurious-to-invariant proportion) can *worsen* worst-group accuracy on CelebA and MultiNLI is non-obvious and worth understanding. Most of the literature focuses on proportion-imbalance or distribution-shift remedies; this specific data-scaling phenomenon has not been systematically documented before.

2. **Demonstrates that in reasoning tasks, data scale alone (not proportion rebalancing) can overcome spurious correlations.** The experiments on LEGO (Tasks 1–2) and PVR (Task 3) show that maintaining spurious proportion while increasing total data leads to perfect accuracy on test sets that break the spurious rule. This cleanly isolates data quantity as a factor, separate from the proportion-based explanations dominant in prior work.

3. **Cross-domain scope.** The paper examines three domains (reasoning, vision, language) with consistent methodology and metrics, lending breadth to the invariance starvation hypothesis beyond a single toy setting.

## Weaknesses

### Fatal

None. The core empirical findings (the reasoning-task result and the exacerbation phenomenon) are present and meaningful, even if the paper overclaims in places.

### Major

1. **The remedy promised in the abstract is not delivered.** The abstract states: "Taking inspiration from reasoning tasks, we present an effective remedy to this problem to ensure that drawing more samples from the distribution always overcomes spurious correlations." The conclusion says: "if one carefully draws samples with easier invariant features from the training distribution, one can overcome invariance starvation." **Nowhere in the paper is this remedy operationalized, algorithmically specified, or experimentally evaluated.** There is no description of how to identify "easier invariant features," no ablation, no comparison to baselines. This is a significant gap between what is advertised and what is delivered. The paper should either include the remedy experiments or revise the abstract to reflect what is actually shown.

2. **The explanation for exacerbation in vision/language is speculative and unsupported.** The paper attributes exacerbation to "samples that are atypical or difficult for a network to generalize to" (line 139) and "general features that are not well represented in the original training set" (line 16). However, there is no empirical analysis to support this: no characterization of the newly added samples, no measurement of "typicality" or feature difficulty, no ablation isolating the proposed mechanism, and no evidence that the problematic samples differ from harmless ones in any measurable sense. Without this, the explanation remains an untested narrative rather than a validated finding.

3. **No error bars, confidence intervals, or multiple-seed replication.** The paper reports single training trajectories with no measure of variance. For a study making claims across three domains with relatively small starting dataset sizes (1,000 for CelebA, 6,000 for MultiNLI), it is impossible to assess whether the observed trends are reliable or within the noise of training. This is a basic expectation for experimental work of this nature.

### Minor

4. **Framing overclaims.** The paper states that it "refutes" the claim that "deep neural networks are biased toward simpler predictive features, they are certain to learn and rely on spurious correlations" (line 14). The existing literature (including the works cited by the paper, such as Shah et al. 2020) does not universally claim inevitability *regardless of data scale* — many works discuss how data quantity, model capacity, and training dynamics mediate simplicity bias. The paper's actual contribution — showing that data scale helps in reasoning tasks while maintaining proportion — is a useful empirical finding but is better described as extending existing understanding rather than refuting it.

5. **"Invariant information" is used informally throughout.** The term is never given a formal definition, making it difficult to distinguish from "more data of any kind." The paper would benefit from clarifying what makes information "invariant" vs. merely "more abundant," especially as this is the paper's central concept.

6. **Hyperparameter tuning is mentioned but not reported.** The paper states hyperparameter tuning was performed to optimize worst-group accuracy using a validation set (line 114), but does not report the search space, number of configurations tried, or sensitivity of results to hyperparameter choices.

### Trivial

None.

## Nice-to-Haves

- An ablation or analysis of the new samples added at each doubling step (e.g., feature similarity, early-training loss/confidence) to support the atypicality explanation.
- A comparison of the data-scaling trajectory against existing debiasing methods (e.g., DRO, reweighting) to contextualize how severe the exacerbation problem is.
- Clarification on the operational meaning of "easier invariant features" in the hinted remedy — even a conceptual description would help.

## Removed Points

- **Harsh Critic #2 (central result on reasoning tasks is "unsurprising")** — Removed as overplayed. The result that scaling data while *maintaining* spurious proportion overcomes spurious correlations is a non-obvious finding worth documenting. The existing literature does not settle this question. The overclaiming about "refuting" is kept (as Minor #4 above), but the underlying result is genuine.
- **Harsh Critic #5 (paper is structurally incomplete)** — Downgraded/restated as Major #1 (remedy not delivered). The paper has all sections 1–6 with a conclusion; it is structurally complete but fails to deliver on the remedy promise. The reviewer's phrasing implies the paper literally ends prematurely, but the issue is about missing *content* (the remedy), not missing pages.
- **"Selection Bias does not form Spurious Correlations" — doesn't engage with literature** — Weakness removed because this is a framing claim in the introduction, and the paper is not positioned as a causal-discovery paper. The paper's actual experiments do address data starvation vs. selection bias.
- **Figures not described in sufficient detail / no tabular results** — Removed as a parser artifact; figures are not available in the text extraction.
- **Strength Finder #4 (practical remedy)** — Removed. The remedy is mentioned but not developed, operationalized, or tested. A "concrete, testable solution" does not exist in the paper; it is a one-sentence gesture. This strength conflicts with verified weakness #1.
- **Strength Finder #1 (refutes inevitability)** — Weakened. The paper shows a useful result but does not "refute" existing understanding. Kept in spirit as Strength #2 but without the "refutation" framing.
- **"Missing discussion of limitations" / "no comparison to existing debiasing methods"** — These are nice-to-haves, moved accordingly.

## Novel Insights

The paper's most genuinely novel insight is the *asymmetry* between reasoning tasks and complex perceptual tasks under data scaling. In reasoning tasks (LEGO, PVR), scaling data while maintaining spurious proportion monotonically improves robustness; in vision and language, it can actively harm worst-group accuracy. This suggests that the *structure* of the input space (e.g., whether features are combinatorially limited or high-dimensional and overlapping) fundamentally changes the data-scaling dynamics of spurious correlations — a hypothesis that goes beyond both the simplicity-bias and selection-bias explanations in the literature. This direction is worth pursuing, but the paper's current analysis (no mechanism validation, no remedy) does not yet deliver on this potential.

## Suggestions

1. **Either deliver the remedy or remove it from the abstract/title promise.** This is the single most important change. Either add experiments that operationalize "sampling easier invariant features" (e.g., based on feature variability, representational similarity, or training difficulty) and evaluate them, or revise the abstract to accurately reflect what the paper actually shows.
2. **Add statistical rigor.** Run 3–5 random seeds for each experiment and report means with error bars/confidence bands in all figures.
3. **Empirically support the atypicality explanation.** Analyze the added samples at each doubling step: measure their representational similarity to the original set, track per-sample loss/confidence early in training, and show that the samples that cause degradation are indeed those with poorly represented invariant features.
4. **Temper the "refutation" language.** Frame the contribution as extending or refining the understanding of simplicity bias, not refuting it.

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>