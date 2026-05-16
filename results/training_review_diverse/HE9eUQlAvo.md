Now I have all the information I need. Let me synthesize the final review.

---

## Summary

This paper proposes a framework that uses influence functions—extended to utility, fairness (demographic parity), and adversarial robustness—to identify which training samples benefit or harm a convex classifier. The contributions are: (1) tree-based models (Algorithm 1) that map feature ranges to influence values for interpretability, and (2) a simple trimming heuristic (Algorithm 2) that removes negative-influence samples to improve performance. Experiments span conventional classification, distribution-shift fairness correction, fairness-poisoning defense, adaptive evasion attacks, online learning with noisy labels, and active learning. The method is demonstrated to improve fairness and robustness consistently, and accuracy in several settings, across tabular, image, and text datasets.

## Strengths

- **Unified framework for utility, fairness, and robustness**: The paper defines influence functions for three distinct metrics—accuracy, demographic parity, and adversarial robustness (Section 2)—and shows that trimming based on these influences improves all three metrics on real-world datasets (Adult, Bank, CelebA, Jigsaw Toxicity in Figure 2). Most prior influence-based work focuses on utility alone.

- **Demonstrated effectiveness across diverse challenging scenarios**: The method is validated in five distinct application settings beyond standard classification: distribution-shift unfairness (Section 5.1, Figure 4), fairness poisoning attacks (Section 5.2, Table 1), adaptive evasion attacks (Section 5.3, Figure 5), online learning with noisy labels (Section 5.4, Figure 6 A–D), and active learning (Section 5.5, Figure 6E). This breadth of successful deployment provides evidence of generality.

- **Efficient data selection without repeated retraining**: Unlike Shapley-based approaches that require O(√n log(n)²) retraining steps, the proposed method computes influence in a single forward/backward pass and uses a simple sorting heuristic for trimming. The active learning variant additionally avoids label access by training the tree estimator without labels (Section 5.5), which is a practical innovation over methods like ISAL that require pseudo-labels.

- **Novel application to fairness poisoning defense**: Section 5.2 applies influence-based trimming against RAA/NRAA fairness attacks, where the paper correctly notes that no well-performing defenses exist in the supervised setting. The results show improved fairness (and sometimes utility) post-attack on German, Compas, and Drug datasets.

## Weaknesses

### Fatal
None.

### Major

- **Baseline comparison in the main trimming experiment (Figure 2) is too weak**. The only baseline is random trimming, which is known to often harm performance, so beating it is unsurprising. The paper claims to "boost the performance of methods such as the influence-based data reweighing approach of (Li & Liu, 2022)" and "outperform existing influence-based approaches for active learning," yet the main supervised trimming experiments (Figure 2) include no comparisons to: (a) core-set selection, (b) influence-based reweighting, (c) removing high-loss samples, (d) removing points far from the decision boundary, or (e) other simple data pruning heuristics. Without such baselines, it is unclear whether the *specific* influence-based criterion provides unique benefit or whether any reasonable pruning of low-utility points would suffice. This weakens the paper's central empirical claim.

- **Interpretability claim is unsubstantiated**. The paper's title and abstract emphasize interpretability ("interpreting the feature space," "Enhancing Model Performance and Interpretability"), and Algorithm 1 is presented as an interpretability tool. However, the sole evidence is one example subtree (Figure 3) shown without any analysis of its quality, depth, or utility. No user study, quantitative measure, or discussion of whether the learned feature splits align with domain knowledge is provided. In the toy data experiments (Figure 1), the paper visualizes "positive" and "negative" influence regions but does not analyze the tree's decision rules. If interpretability is a claimed benefit, it must be evaluated; if it is merely a tool to enable data selection, the paper should not foreground it as a contribution.

### Minor

- **Poisoning defense evaluation lacks alternative defense baselines**. Section 5.2 claims the method is "potentially the first defense" against RAA/NRAA attacks, but reports only pre-attack, post-attack, and post-trimming metrics. No comparison to other possible defenses (e.g., outlier detection, robust training, or data sanitization) is provided. Without such comparisons, the claim of being an effective defense is incompletely supported.

- **Non-convex extension is mentioned but never demonstrated**. Section 2 discusses a linear-surrogate strategy for non-convex models and states "In this paper, we adopt the above first strategy." Yet all experiments use convex models (logistic regression or linear SVM) directly. The paper later concedes it is "primarily focused on convex models" (line 47), making the non-convex discussion a dangling claim. The paper should either demonstrate the surrogate approach on at least one non-convex model or remove the claim of having "adopted" the strategy.

- **No hyperparameter sensitivity analysis**. The method depends on budget *b* and (for the tree) regularization parameter λ. Only *b* is varied (Figure 2), and λ is not analyzed at all. For a method that claims simplicity, robustness to its few hyperparameters should be demonstrated.

- **No reporting of computational cost or runtime**. Influence functions require Hessian inversion (O(d³) where d is feature dimension). The paper does not report runtime for any dataset, nor discuss computational feasibility for high-dimensional feature spaces.

- **Only one fairness metric (demographic parity) is used**. The paper should acknowledge that improving DP may not improve other fairness notions (e.g., equal opportunity, equalized odds) and could even harm them.

- **Only one attack type is tested for robustness** (a white-box orthogonal perturbation for linear models). Results may not generalize to stronger attacks (PGD, CW, etc.), which should be acknowledged or tested.

- **Ethics statement makes an overly strong safety claim**. The statement that "the approaches cannot be used in a problematic way by a malicious adversary" (line 176) is too categorical. Influence functions identify which data points affect fairness—a malicious actor could use this knowledge to deliberately inject points that harm fairness. The paper should acknowledge dual-use risks.

### Trivial
- The active learning results (Figure 6E) show a modest gap over baselines, and runs are reported as deterministic (no error bars over seeds). The paper could strengthen this with variance estimates (e.g., different random splits of the initial labeled set).

- The prose describing Algorithm 2 uses slightly unusual phrasing ("sort J in order of increasing positive influence") but the logic (ascending sort → first min{b,b'} indices → remove) is coherent. Clarifying the wording would aid reproducibility.

- Figure captions could more clearly distinguish which subfigures show validation vs. test performance.

## Nice-to-Haves

- A small ablation comparing trimming to alternative heuristics (remove high-loss points, remove farthest-from-boundary points) in the main experiment (Figure 2) would substantially strengthen the paper.
- A depth-limited tree (e.g., depth 3) with a brief discussion of whether the splits align with domain knowledge would go a long way toward substantiating the interpretability claim.
- Reporting runtime for influence computation and tree fitting on the largest dataset would help practitioners assess practical applicability.
- Testing the non-convex surrogate strategy on a single dataset (e.g., a pre-trained CNN on a small subset of ImageNet) would validate the claimed generality.

## Removed Points

- **Algorithm 2 description is contradictory/ambiguous**: The reviewer claimed a "critical inconsistency" in the algorithm description (sorting by "increasing positive influence" vs. selecting negative-influence samples). In fact, the prose describes a coherent algorithm: sort influence values ascending (negative/most harmful first), take the first min{b,b'} indices (capped by budget and by the actual number of negative-influence samples), and remove those samples. The garbled pseudocode in the image is a PDF-parser artifact, not an author error. The description is clear enough to reproduce. **Reason: Factually incorrect criticism — the reviewer misread the algorithm.**

- **Double-y-axis plots are hard to read**: This is a formatting/style nitpick. **Reason: Removed per formatting-nitpick rule.**

- **Paper overstates novelty (abstract/intro)**: The framing that the answer is "samples with negative influence" is an operationalization of what influence functions already quantify. While the differentiation (trees, application breadth) is modest, this is a subjective judgment about framing rather than a technical weakness. **Reason: Generically subjective; not a concrete technical flaw.**

- **Interpretability strength from Strength Finder**: The Strength Finder claimed "Interpretable feature-space analysis via tree-based influence estimation" as a strength, but this conflicts with the verified weakness that interpretability is unvalidated. Per the conflict rule, the weakness wins. **Reason: Strength conflicts with verified weakness.**

## Novel Insights

None beyond the paper's own contributions. The reviews confirm the paper's value — a unified influence-based framework spanning utility, fairness, and robustness with broad experimental coverage — while identifying that the evaluation is not yet strong enough to fully support the central claims. The key gap identified (weak baselines, unvalidated interpretability) is about the strength of evidence rather than about a novel critique of the methodology.

## Suggestions

1. **Add ≥3 concrete baselines to the main trimming experiments (Figure 2)** — at minimum, remove high-loss samples, remove farthest-from-boundary samples, and random trimming with multiple seeds to show variance. This would establish whether the *influence* criterion provides unique benefit.
2. **Provide a minimal evaluation of the interpretability tree** — show a depth-limited tree for one dataset and discuss whether the feature splits align with domain knowledge. A single analyzed example would substantiate the interpretability claim.
3. **Either demonstrate the non-convex surrogate strategy or remove the claim** — test on one non-convex model (e.g., embeddings from a pre-trained CNN) to validate the stated approach, or acknowledge that it is a direction for future work rather than a current contribution.
4. **Soften the ethics statement** — acknowledge that influence functions have dual-use potential (identifying influential points could enable targeted attacks on fairness).
5. **Add a brief computational cost analysis** — report runtime for Hessian inversion and tree fitting on the largest dataset used.

## Score and Decision

The paper addresses an important question and proposes a practical, coherent framework. The breadth of application scenarios is impressive and demonstrates real potential. However, the central empirical claim — that influence-based trimming outperforms alternatives — rests on a too-weak baseline comparison (only random trimming). The interpretability claim, featured in the title, is almost entirely unvalidated. These weaknesses are substantive but not fatal: they weaken rather than invalidate the contribution. The method is sensible and the evidence, while incomplete, is generally positive. With moderate revisions (adding baselines, evaluating interpretability, softening overclaims), the paper would be acceptable. In its current form, the evidence is not yet convincing enough to recommend acceptance.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>