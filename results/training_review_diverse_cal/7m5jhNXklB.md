Now I have a thorough understanding of the paper and can write the consolidated review.

## Summary

The paper proposes VTruST, a controllable data-centric framework for selecting training data subsets that optimize trade-offs between accuracy, fairness, and robustness. The core ideas are: (1) defining additive value functions for each trustworthiness metric that can be combined via user-specified weights, (2) formulating subset selection as an online sparse approximation problem, and (3) solving it with a novel online variant of Orthogonal Matching Pursuit (OMP). Experiments on social, image, and scientific datasets show competitive performance.

## Strengths

1. **Novel controllable framework for multi-metric DCTAI**: The paper proposes combining accuracy, fairness, and robustness value functions via user-specified weights $\lambda$, enabling explicit control over trade-offs. The Pareto-front results (Figure 1) empirically demonstrate that varying $\lambda$ produces a continuum of operating points, validating the controllability claim. This capability is not offered by prior data-centric methods that optimize only a single metric.

2. **Online OMP algorithm with sound complexity**: The online variant of OMP (Algorithms 1 and 2) avoids storing all historical features by greedily replacing selected points with incoming ones when the residual error decreases. Per-epoch complexity is $\mathcal{O}(\omega M(N-\omega))$, which is linear in the number of training points $N$ and validation points $M$ — the $(N-\omega)$ factor is correct because only points after the filling phase trigger the $\mathcal{O}(\omega M)$ replacement check.

3. **Comprehensive empirical evaluation across diverse domains**: The paper evaluates on social (COMPAS, Adult Census, MEPS20), image (MNIST, CIFAR10, TinyImageNet), and scientific datasets (Spinodal, EOSL). VTruST variants generally outperform baselines on target metrics. For example, on TinyImageNet robust accuracy at 60% subset, VTruST-R achieves 41.50 vs. SSR's 30.07 (~38% relative improvement). The data-centric explanation analysis (CF-Gap, uncertainty/distinctiveness) provides supporting qualitative evidence.

## Weaknesses

### Fatal

1. **Fairness value function is not additive and incompatible with the framework**. The paper defines the fairness value function using equalized odds disparity: $ed(\theta,\cD') = \max(\|l(\theta,\cD'_{y_0,z_0})-l(\theta,\cD'_{y_0,z_1})\|, \|l(\theta,\cD'_{y_1,z_0})-l(\theta,\cD'_{y_1,z_1})\|)$, and then claims (line 96) that "$ed(\theta,\cD'_1)+ed(\theta,\cD'_2) = ed(\theta,(\cD'_1+\cD'_2))$ also holds true." This is mathematically false — the maximum of sums is not the sum of maxima, even when the underlying loss is additive over datapoints. More fundamentally, $ed(\theta,\cD')$ cannot be decomposed into per-validation-point contributions (it requires groupwise statistics and a max over groups), so the fairness value function is incompatible with the vector-valued sparse approximation formulation ($\vec{y}_t \in \mathbb{R}^M$ approximated by M-dimensional features). The entire fairness component of the framework is built on an invalid premise. **The accuracy and robustness components do not share this issue** (they use per-point additive loss-based value functions), but the paper's claims regarding fairness-specific results (VTruST-F, VTruST-FR, the tradeoff curves) cannot be attributed to the proposed framework as described.

### Major

2. **Second-order Taylor expansion derivation is incorrect**. The paper claims (lines 68-72) to derive features $\vec{X}_i^k = \nabla l(\cdot)^T\nabla l(\cdot) + \frac{(\nabla l(\cdot)^T\nabla l(\cdot))^2}{2}$ by "truncating the Taylor expansion till the second-order terms." The correct second-order term would involve the Hessian: $\frac{1}{2}\eta_t^2 \nabla l(\theta,d_i)^T H \nabla l(\theta,d_i)$. The squared-gradient inner product appearing in the paper is not derivable from any standard Taylor expansion of $l(\theta^{i-1}+\Delta\theta,\cD')$. This means the claimed theoretical grounding for the feature construction is invalid. The features might still work empirically as a heuristic, but the paper presents them as derived from a Taylor expansion, which is misleading, and this undermines the claimed connection between the sparse approximation and the intended value function.

3. **Training protocol is not specified**. The paper never clarifies whether: (a) the subset $S_T$ is used to train a final model from scratch, (b) the model that produced the value functions during training is the one evaluated, or (c) some other protocol is used. The paper says "models trained on subsets selected by VTruST" (line 34) but Algorithm 1 appears to run *during* a training trajectory. If (b), there is a risk of overfitting to the validation set since selection happens using the same model being updated. If (a), the online motivation is weakened. This omission is critical for reproducibility.

### Minor

4. **Theorem 1 is vacuous**. Theorem 1 states a condition under which an incoming point $x$ replaces an existing point $z$ in the selected set, essentially paraphrasing the DataReplace algorithm's own logic. It provides no guarantee about solution quality, convergence, recovery of a true sparse representation, or any optimality property. The theorem's title ("Conditions for Optimality of the Selected Subset") is misleading — it adds no theoretical substance.

5. **$\gamma \leq 0$ condition in DataReplace lacks justification**. Algorithm 2's line 8 requires the coefficient $\beta_q^p$ of a selected point to be $\leq 0$ for replacement. This biases selection toward positive-coefficient points and discards negative-coefficient points outright without justification. An ablation comparing this rule against simpler alternatives (e.g., always pick the point with smallest projection magnitude) would be helpful.

6. **Some baseline comparisons conflate subset selection with training algorithms**. In Table 1, FairMixup and FairDummies are training-time algorithms (modifying the loss), not subset-selection methods. Similarly, AugMax in Table 2 is an augmentation strategy using all data. While these comparisons are still informative (showing data-centric selection can compete with algorithmic approaches), they do not control for the same data regime as VTruST. A cleaner comparison against other subset-selection methods (e.g., TRAK-based influence selection) would strengthen the evaluation.

7. **Several competitive differences are within one standard deviation**. In Table 1, for COMPAS, VTruST-F's EO Disparity (0.15±0.01) overlaps with FairMixup (0.15±0.03) and many other values have overlapping error bars. With only 3 runs, statistical significance is unclear.

### Trivial

- The hyperparameter selection section claims "monotonicity of metrics w.r.t. $\lambda$" without empirical verification — tradeoff curves for fairness and robustness are not guaranteed to be monotonic.

## Nice-to-Haves

- Replace the fairness value function with a genuinely additive measure (e.g., a weighted sum of groupwise losses) or drop the fairness component entirely and focus on accuracy–robustness tradeoffs, which are on solid mathematical footing.
- Provide an ablation removing the squared-gradient term from the features to verify whether it contributes to performance.
- Add a random-shuffle experiment to study sensitivity to data ordering (the algorithm is online and order-dependent).
- Add comparison with influence-function-based subset selection (TRAK) as a more direct subset-selection baseline.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Complexity criticism**: The harsh critic claimed the $(N-\omega)$ factor in $\mathcal{O}(\omega M(N-\omega))$ "seems to assume that the chosen point is always already in $S$." This is incorrect — the factor $(N-\omega)$ correctly accounts for the filling phase: for the first $\omega$ points, only simple addition is needed ($O(\omega)$ cost); for the remaining $N-\omega$ points, the DataReplace call costs $O(\omega M)$. The critic's own proposed fix yields the same expression.
- **Criticism that "10-20% improvement" is unsupported**: Several metrics show improvements in this range (e.g., TinyImageNet RA at 60%: 38% relative improvement; MEPS20 EO Disparity: 50% relative improvement). The claim is reasonable for the best cases.
- **Criticism about comparing against AugMax/FairMixup as apples-to-oranges**: While these are different classes of methods, the comparisons are informative rather than invalid — they show that selecting a subset can match or exceed full-data algorithmic approaches. This does not constitute a flaw in the results, though additional subset-selection baselines would strengthen the paper.
- **Formatting/style nitpicks and missing appendix concerns**: These are parser artifacts or outside the scope of evaluation.

## Novel Insights

The most interesting observation from the reviews is the unresolved tension between the paper's two central claims: the theoretical framework (additive value functions → sparse approximation → online OMP) and the empirical results. The fairness component has a provably incorrect mathematical premise, and the Taylor-based feature derivation is not mathematically defensible. Yet the empirical results for all three metrics (including fairness) are competitive. This suggests that either (a) the algorithm works for reasons other than those claimed (the features are acting as effective heuristics despite not corresponding to the claimed derivation, and the fairness results may arise from the accuracy component indirectly), or (b) the empirical setup has uncontrolled confounds that happen to produce favorable numbers. The paper would benefit from acknowledging this gap rather than presenting a unified theoretical story that does not hold up to scrutiny. The accuracy–robustness parts of the framework, which use properly additive loss-based functions, are on firmer ground and could form the basis of a more defensible contribution.

## Suggestions

- Drop fairness entirely or replace the equalized-odds-disparity value function with a genuinely additive fairness measure. The framework is valid for accuracy and robustness; extending it to fairness requires a fundamentally different value function that can be decomposed per-validation-point.
- Either derive the sparse approximation features using a proper Hessian-based second-order expansion, or honestly present the gradient inner-product features as a heuristic design choice (e.g., "select points whose validation-gradient alignment is largest") without claiming a Taylor derivation.
- Clearly specify the training protocol: describe whether the final model is trained from scratch on $S_T$ or whether the training trajectory that produces the value functions is the one being evaluated. If the latter, discuss potential overfitting.
- Add subset-selection-only baselines (e.g., TRAK, random subsets at the same size) and remove or clearly contextualize comparisons against training-algorithm baselines.
- Replace Theorem 1 with a meaningful theoretical claim (e.g., convergence analysis, recovery guarantees under sparsity assumptions) or remove it.

## Score and Decision

**Originality**: Good — the idea of controllable multi-metric subset selection via online sparse approximation is novel.
**Importance of research question**: High — controllable DCTAI is practically relevant.
**Claims well-supported**: No — the fairness additivity claim is false; the Taylor derivation is incorrect; and the training protocol is underspecified.
**Soundness of experiments**: Moderate — results are positive but some baselines are methodologically different, error bars overlap in several cases, and lack of ablation studies weakens the evidence.
**Clarity of writing**: Moderate — the method section is dense and the algorithm description is reasonably clear, but the training protocol is never specified.
**Value to community**: Potentially high for accuracy–robustness tradeoffs, but the fairness component as presented is misleading.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>