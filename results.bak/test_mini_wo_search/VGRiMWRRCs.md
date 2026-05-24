Now I have enough information. Let me produce the final consolidated review.

## Summary

This paper proposes an Empirical Bayesian perspective for group robustness without group labels, and introduces "Learn from Known Unknowns," a method that uses evidential deep learning to estimate epistemic uncertainty and reweights the retraining loss by this uncertainty. Experiments on Colored MNIST, Waterbirds, CelebA, MultiNLI, and CivilComments show competitive worst-group accuracy compared to existing group-label-free methods.

## Strengths

- **Unified Empirical Bayes formulation of group robustness**: Section 3.2–3.4 formalizes group robustness as latent-variable inference and shows in Table 1 that methods like LfF, JTT, and SELF correspond to different choices for estimating p(g|x,θ) and p(θ). This provides a conceptual lens that prior work lacked, enabling systematic comparison. (Verifiable: lines 59–110, Table 1.)

- **Novel uncertainty-guided reweighting mechanism**: The paper introduces a concrete method (Section 4) that uses evidential deep learning to compute epistemic uncertainty u(x) = K/S(x) and reweights the retraining loss by this uncertainty. This is a clean, principled alternative to ad-hoc selection heuristics in prior work. (Verifiable: lines 166–190.)

- **Competitive worst-group accuracy**: The method matches or exceeds existing group-label-free approaches (CVaR DRO, LfF, JTT, AFR) on Waterbirds, MultiNLI, and CivilComments, with a small gap to oracle methods. (Verifiable: Tables 4 and 5; textual summary at lines 236–240.)

- **Computational efficiency via last-layer retraining**: The method retrains only the final layer, avoiding the cost of training a new model from scratch as required by JTT and CnC. (Verifiable: line 190, lines 240–241.)

## Weaknesses

### Fatal
None.

### Major

- **Framework–method disconnect undermines the claimed theoretical contribution**: Theorem 3.1 (Tweedie's formula) provides a general guarantee that the posterior mean of a latent group variable can be estimated from observations under exponential-family conditions. However, the actual method defines \hat{p}(g|x,θ) = u(x) = K/S(x) (line 179) without any derivation showing that the Dirichlet-based evidential uncertainty approximates the Tweedie estimate. The theorem assumes a differentiable marginal likelihood with exponential-family conditional distributions, but the evidential model outputs a Dirichlet distribution over class probabilities — not over group membership. The connection between "uncertainty" and "group posterior" is asserted (lines 168–180) without formal justification or empirical verification of the approximation. The EB framework thus serves as a post-hoc taxonomy of prior work (Table 1) rather than a constructive foundation for the proposed method. **(Verifiable: compare Theorem 3.1 at lines 87–99 with the method at lines 168–188.)**

- **Critical retraining detail is underspecified, harming reproducibility**: Section 4.2 (the method description) states that samples are reweighted by u(x) but omits any mention of subset selection. Section 5.2 (experimental setup) adds: "retraining samples are randomly sampled from the misclassified portion of the training set and the validation set" (line 211). This is a significant algorithmic detail — it means the method does not reweight all training samples, only a subset filtered by misclassification. The fraction of misclassified samples selected, the subset size, and whether selection is done once or iteratively are all unspecified. Without this information, the method cannot be reproduced. Moreover, this discrete filtering step is a separate heuristic not derived from the uncertainty estimates, raising the possibility that gains come from discarding correctly-classified samples rather than from uncertainty reweighting per se. An ablation isolating the two effects is needed. **(Verifiable: lines 166–190 vs. line 211.)**

- **Average accuracy is not reported**: The paper reports only worst-group accuracy (WGA) in Tables 4 and 5. Without average accuracy, it is impossible to assess whether the method trades off overall performance for robustness — a critical concern for practical deployment. **(Verifiable: Tables 4 and 5; textual description at lines 236–240.)**

- **Quantitative evidence for the core thesis (uncertainty ≈ group membership) is missing**: Section 5.5 mentions that "Quantitative analysis showed correlations between uncertainty values and true group labels across all datasets" (line 257), but no actual correlation numbers (e.g., Spearman's ρ, AUC, separability metrics) are reported anywhere. The only supporting evidence is qualitative: GradCAM visualizations for 5 samples per category (Figure 2) and a t-SNE plot (Figure 1). Given that the paper's entire approach depends on this proxy relationship, the absence of quantitative validation is a significant gap. **(Verifiable: lines 248–262.)**

### Minor

- **The claim of reduced hyperparameter tuning is unsupported**: The abstract and introduction claim that the method "reduces reliance on hyperparameter tuning" (line 4–5, line 20). However, the experimental procedure (lines 211–212) includes: a dynamic λ annealing schedule from 0 to 1, random sampling of learning rates from predefined ranges, and selection of the best of 10 random configurations based on validation performance. No ablation or sensitivity analysis is provided to demonstrate robustness to these choices, so the claim is asserted without evidence. (And the "self-adaptive held-out set" mentioned in the introduction (line 20) is never operationalized in the method section.)

- **Synthetic experiment lacks error bars**: The Colored MNIST result reports improvement from 3.74% to 84.58% on the minority group (line 225) without standard deviations or replication details. This makes it impossible to assess the stability of the result. The experiment also lacks an uncertainty baseline (does reweighting by random values produce similar gains?).

- **GradCAM evidence is anecdotal**: Figure 2 shows only 5 samples per category (highest/lowest uncertainty). Without a quantitative measure of alignment frequency across the full dataset, the visualizations are suggestive but not evidential.

### Trivial

- The term σ² in Theorem 3.1 is introduced (condition 3, line 91) but never connected to the method. This is a minor expositional gap.

## Nice-to-Haves

- **Ablation of the subset selection step**: Run (a) full training set + uncertainty reweighting, (b) the current misclassified-subset approach, and (c) a random subset of the same size. This would isolate whether the uncertainty weighting or the filtering drives performance.
- **Correlation statistics** between uncertainty scores and true group labels (e.g., Spearman's ρ, group separability by uncertainty threshold) for each dataset.
- **Average accuracy** alongside WGA in main tables, to assess trade-offs.
- **Hyperparameter sensitivity analysis** demonstrating stability across learning rates, λ schedules, and subset fractions.

## Removed Points

*"Baseline set is not current (LaBonte et al., 2024a should be included)"* — The paper cites LaBonte et al. (2024a) at line 14 only to note that class-balancing techniques show inconsistent performance; it is not presented as a method the paper should compare against. The paper does include SELF (LaBonte et al., 2024b) as an oracle baseline in Tables 4 and 5. This criticism is not well-grounded.

*"The method is outperformed on CelebA by CnC (a 2023 method)"* — The paper explicitly acknowledges this at line 236–237 and explains why (CnC uses self-supervised learning). The paper also highlights that its approach performs competitively on three other datasets. This is transparent reporting, not a weakness.

*"Theorem 3.1 is vague; σ² is unused; no conditions are given"* — The conditions ARE given at lines 88–92 (differentiable marginal likelihood, exponential family, estimable variance). The theorem is standard Tweedie's formula; it is not vague by the standards of such statements. This criticism is inaccurate.

## Novel Insights

The most substantive insight emerging from the review is that the paper's method actually comprises two independent design decisions — (1) a misclassification-based sample filter and (2) an uncertainty-based loss reweighting — yet the algorithm is described as a single coherent procedure derived from the EB framework. The filtering step is descoped to the experimental section without justification or ablation, and the framework provides no guidance on either choice. This means the method's competitive results may be driven by a combination of heuristics that are neither separately validated nor jointly derived from the claimed theoretical foundation. A second insight is that the paper's central causal claim — that epistemic uncertainty reveals latent group membership — has only qualitative support despite being the linchpin of the approach. These gaps suggest the paper is best read as presenting an intriguing hypothesis with promising preliminary empirical results, rather than a validated methodology.

## Suggestions

1. **Either tighten or drop the theoretical framing.** Either derive a concrete connection between Tweedie's formula and the evidential uncertainty (e.g., show that u(x) approximates the posterior mean of a group indicator under specific conditions), or explicitly re-frame Theorem 3.1 as related background and present the method as a heuristically-motivated empirical approach.
2. **Specify and ablate the subset selection.** Report the fraction of misclassified samples used for retraining across datasets, and run ablations that compare full-set+reweighting vs. subset+reweighting vs. random subset+reweighting.
3. **Report average accuracy** alongside worst-group accuracy in all tables, and discuss any observed trade-offs.
4. **Add quantitative correlation metrics** between uncertainty scores and true group labels for every dataset.
5. **Provide hyperparameter sensitivity analysis** or moderate the claim about reduced tuning.
6. **Add standard deviations** to the synthetic experiment.

## Score and Decision

Score: 5.0. The paper addresses an important problem and the empirical results are promising, but the core theoretical claim is disconnected from the actual method, key design choices are underspecified, essential validation (uncertainty–group correlation, average accuracy, ablation of selection heuristic) is missing, and the hyperparameter claim is unsupported. Substantial revision is needed before acceptance.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>