- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6
Now I have a complete picture. Let me synthesize the final review.

## Summary

This paper proposes to regularize energy values among training samples for out-of-distribution (OOD) generalization. The authors (1) empirically and theoretically show that existing long-tail recognition methods (data re-weighting and margin control) can be unified as implicit energy regularization, and (2) propose influence-aware energy regularization (IAER) that uses influence functions to determine per-sample energy regularization coefficients, extending the framework to subpopulation shift and domain generalization where distribution shifts are more implicit.

## Strengths

- **First to call attention to energy disparity among in-distribution samples.** Prior work (Liu et al. 2020, Bitterwolf et al. 2022) focused on energy differences between ID and OOD data; this paper identifies that energy variation *within* the training set itself affects generalization, a genuinely novel perspective (Section 1, line 17).

- **Theoretical unification of reweighting and margin control under energy regularization.** Section 3.2 (Eqs. 5–6) formally derives that adding an energy penalty with coefficient $\hat{\beta}_\mathbf{x}$ simultaneously produces a sample-weighting factor $(1-\hat{\beta}_\mathbf{x})$ and a margin adjustment $\frac{1}{1-\hat{\beta}_\mathbf{x}}$, connecting two previously separate branches of long-tail methods as special cases of energy regularization.

- **Clear empirical evidence that LDAM implicitly levels energy across classes.** Figure 2 shows ERM yields strong negative correlation between class sample size and average energy (Pearson −0.74 on CIFAR10-LT, −0.60 on CIFAR100-LT), while LDAM brings correlations close to zero (−0.26, +0.16). This directly supports the claim that margin control acts as implicit energy regularization.

- **IAER provides a principled way to extend energy regularization beyond long-tail scenarios.** The influence-function approach (Section 4.1) provides a method for setting per-sample energy regularization coefficients when the distribution shift is implicit, addressing a genuine challenge in applying energy regularization to general OOD settings.

- **Consistent improvements across multiple OOD generalization benchmarks.** Despite modest gains, IAER shows improvement over baselines on long-tail (CIFAR10-LT error reduced from 29.64% to 24.17%), subpopulation shift (CMNIST, MetaShift, NICO++, Waterbirds, CivilComments), and domain generalization (PACS, VLCS, CMNIST).

## Weaknesses

### Fatal
None.

### Major

- **Remark 4.1 (Arbitrary Energy) creates an unresolved tension with the paper's core thesis.** The paper proves that for any classifier, one can change the energy on each point to any real number without affecting the conditional predictions (Remark 4.1). The paper uses this remark to argue that energy regularization is *orthogonal* to risk-based invariant risk minimization. However, if energy and predictions can be decoupled, the reader is left wondering why regularizing energy during training should improve generalization at all — the optimizer could, in principle, learn the classification task and separately offset energy without affecting predictions. The paper never explicitly reconciles this: it neither shows that the decoupling offset is unreachable during SGD optimization nor provides a mechanism by which energy regularization shapes the learning trajectory despite the formal decoupling at optimality. This is not a fatal contradiction (energy regularization could still affect optimization dynamics meaningfully), but the paper's silence on this point undermines its motivation.

- **The influence function method operates outside its theoretical guarantees, with no empirical validation.** The influence function derivation (Eqs. 8–11) assumes the loss is twice-differentiable and *strictly convex*. Neural networks are non-convex; the Hessian may be indefinite or singular. The paper mentions this in the conclusion (line 295: "as defined for convex loss functions, the influence function may not reflect the actual influence for neural networks") but treats it as a minor caveat rather than a structural concern. Critically, the paper provides **no empirical validation** that the influence estimates are reliable in this setting (e.g., by comparing the influence-predicted effect of upweighting energy on a point with the actual effect of retraining the model with that upweighting). Without such validation, the core mechanism of IAER is an unverified heuristic, and its experimental successes could stem from other implicit mechanisms (e.g., the fine-tuning step itself).

- **Empirical evaluation lacks rigor in baselines and statistical reporting.** (a) *Limited baselines*: For long-tail (Tables 2–3), only ERM and LDAM-DRW are compared against; no SOTA long-tail methods (e.g., Balanced Softmax, C2L, MiSLAS) are included. For subpopulation shift (Table 4), the "Baseline" column is not identified by name. For domain generalization (Table 5), only ERM is compared, despite the paper claiming orthogonality to invariant risk minimization — the combination is never tested. (b) *No variance or confidence intervals*: No standard deviations, error bars, or statistical significance tests are reported for any result. Given that several improvements are modest (e.g., CIFAR100-LT ratio 100: 39.44 → 39.64), the reader cannot assess whether these gains are reliable. (c) *Influence validation set issue*: The "validation set" for the influence function is sampled from the training set itself, meaning the influence measures how energy regularization on one training point affects loss on *other training points*. There is no guarantee this generalizes to a test distribution — this is a form of potential overfitting to the training subset, a risk the paper does not discuss.

### Minor

- **CIFAR100-LT improvements are negligible and the explanation is speculative.** On CIFAR100-LT with imbalance ratio 100, IAER improves LDAM-DRW from 39.44% to 39.64% — a 0.2% gain. The paper attributes this to smaller per-class sample sizes in CIFAR100 making influence estimates less accurate. This is a plausible but untested speculation, and the result itself does not support the claimed significance of the method for this setting.

- **Domain generalization evaluation is narrow.** Only 3 datasets are tested, and only *average* accuracy across domains is reported. No worst-case per-domain accuracy is given (which is standard practice in DG), and the paper does not combine IAER with IRM or other DG methods despite claiming orthogonality.

- **"Unification" claim could be misinterpreted.** The derivation in Section 3.2 shows that *adding explicit energy regularization* can replicate the gradient effects of reweighting and margin control. This is correctly described as an equivalence in the gradient update, but the framing ("long-tail recognition methods are implicit energy regularization") could be read as a stronger causal claim than what is actually proven (i.e., that existing methods operate *via* energy rather than merely having effects that can be reproduced by energy regularization).

### Trivial
None.

## Nice-to-Haves

- **Validate influence estimates empirically**: Compare the influence-predicted effect of upweighting energy on a small subset with actual retraining, even on a small scale. This would substantially strengthen the paper's core claim.
- **Combine IAER with IRM** or other invariant-risk methods to substantiate the orthogonality claim.
- **Report standard deviations / confidence intervals** for all main results, especially given the modest improvements.
- **Analyze failure cases**: The paper notes that IAER sometimes hurts performance (e.g., some CIFAR100 configurations), but does not analyze when or why.

## Removed Points

These points were raised in the reviews but are removed or demoted upon verification against the paper:

- *"Eq. (6): the term 'bar{p}(y')=0' appears to be a typesetting error"* — This is a parser-induced formatting artifact, not an author error. **Removed.**
- *"Table 1 is an embedded image that was not rendered"* — Parser artifact. **Removed.**
- *"Missing appendix content" / "code and data splits not detailed enough for reproduction"* — Hard rules: parser strips appendix content from all papers; these exist in the original submission. **Removed.**
- *"Remark 4.1 (Arbitrary Energy) justifies orthogonality"* (listed as a strength by Strength Finder) — This remark creates a tension rather than being an unqualified strength. It is better characterized as a conceptual point the paper does not fully resolve. **Removed from strengths.**
- *"The influence function approximation time is reported only for a single setting"* — The paper actually reports time across multiple datasets (Table 6). **Removed.**
- *"The paper should include more models in the model zoo"* — Generic request; the evaluation is already adequate in breadth across 3 different OOD settings. **Removed.**
- *"The paper should use a larger dataset"* — No evidence current sizes are insufficient. **Removed.**
- *"Requesting theoretical proofs for an empirical systems paper"* — The paper already provides theoretical derivation (Section 3.2); the influence function convexity concern is a real limitation (kept above) but demanding full proof for non-convex influence functions is outside community standards. **Weakened from fatal to major.**

## Novel Insights

The harsh critic raises a genuinely insightful point that even the paper seems unaware of: Remark 4.1, which the paper presents to explain why prior work overlooked energy and why energy regularization is orthogonal to risk-based methods, actually raises a fundamental question about the paper's own method. If energy can be arbitrarily modified at fixed predictions, what is the mechanism by which energy regularization *during training* produces better generalization? The most plausible resolution — that the decoupling offset is not reachable via standard SGD in finite time, so energy regularization shapes the optimization trajectory before convergence — is never articulated. This tension between the formal property (arbitrary energy) and the empirical practice (energy regularization helps) is the paper's most interesting unresolved question and points toward a deeper understanding of how energy regularization interacts with optimization dynamics.

## Suggestions

1. **Reconcile Remark 4.1 with the method's motivation**: Either argue that the energy-offsetting solution is not reachable during SGD optimization (so regularization matters for the learning trajectory), or provide an experiment where a model trained with energy regularization is post-hoc adjusted for energy and the benefits persist — demonstrating the effect is not merely from the fine-tuning trajectory but from genuine generalization improvements.

2. **Validate influence estimates against actual retraining**: On a small dataset (e.g., CIFAR10-LT), compare the influence-predicted effect of upweighting energy on a set of points with the actual effect of retraining the model with that upweighting. Report the correlation.

3. **Broaden baseline comparisons**: Include at least one additional SOTA long-tail method (e.g., Balanced Softmax or MiSLAS) and one established subpopulation shift method (e.g., GroupDRO or JTT). For domain generalization, combine IAER with at least one invariant-risk method.

4. **Report variance**: Add standard deviations or confidence intervals for all main results, derived from multiple runs.
