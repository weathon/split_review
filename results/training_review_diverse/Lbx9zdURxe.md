Now I have a thorough understanding of the paper and can verify/refute the reviewer claims. Let me write the consolidated review.

---

## Summary

This paper proposes to investigate and regularize the energy difference among in-distribution (training) data samples, moving beyond prior work that focused only on energy differences between in-distribution and OOD data. It shows both empirically (Figure 2) and theoretically (Section 3.2) that existing long-tail recognition methods — specifically data reweighting and margin control — can be understood as applying implicit energy regularization. It then proposes Influence Aware Energy Regularization (IAER), which uses influence functions to determine per-sample energy regularization coefficients for more general OOD generalization scenarios (subpopulation shift, domain generalization). Experiments on CIFAR-LT, ImageNet-LT, iNaturalist, and several domain generalization benchmarks show modest but generally positive gains.

## Strengths

- **Novel perspective on energy among training samples.** Prior work on energy-based models for classifiers focused on energy differences between ID and OOD data (OOD detection) or between source and target domains (domain adaptation). This paper is the first to systematically investigate and call attention to energy differences among training samples themselves, and to show that these differences affect generalization. This is a genuinely novel framing.

- **Empirical demonstration that LDAM equalizes energy across classes.** Figure 2 shows a clear and convincing result: ERM-trained models have a strong negative correlation between class frequency and average energy (Pearson's R = −0.74 on CIFAR10-LT, −0.60 on CIFAR100-LT), while LDAM-trained models reduce this correlation to near zero (−0.26 and +0.16). This directly supports the claim that margin-control methods implicitly regularize energy.

- **Theoretical connection between energy regularization and two branches of long-tail methods.** Section 3.2 derives that adding an explicit energy regularization term \(\hat{\beta}_{\mathbf{x}} E_\theta(\mathbf{x})\) to cross-entropy produces a gradient (Eq. 6) with two simultaneous effects: data reweighting (via factor \(1-\hat{\beta}_{\mathbf{x}}\)) and margin adjustment (via shifting the margin term from \(\bar{p}(y|\mathbf{x})-1\) to \(\bar{p}(y|\mathbf{x})-\frac{1}{1-\hat{\beta}_{\mathbf{x}}}\)). This provides a unified mathematical lens for understanding why reweighting and margin control — previously seen as distinct branches — can be effective: they both amount to different forms of energy regularization.

- **Broad empirical validation across three generalization settings.** The paper evaluates IAER on long-tail classification (CIFAR-LT, ImageNet-LT, iNaturalist), subpopulation shift (CMNIST, MetaShift, NICO++, Waterbirds, CivilComments), and domain generalization (CMNIST, PACS, VLCS). This breadth supports the claim that energy regularization is a generally useful principle rather than a narrow technique.

- **Interesting finding that influence of energy regularization is uncorrelated with training loss.** Figure 4 reports a Pearson correlation of −0.04 between influence magnitude and training loss, showing that energy regularization targets a different signal than standard loss minimization. This provides a useful diagnostic for future work.

## Weaknesses

### Fatal
None.

### Major

- **The central "unification" claim is imprecisely framed and overreaches what the derivation shows.** The derivation in Section 3.2 demonstrates that *adding an energy regularizer* produces gradient effects interpretable as a combination of reweighting and margin adjustment. This shows energy regularization *entails* both effects. But the paper repeatedly claims the converse — that existing reweighting and margin-control methods "could be unified as implicit energy regularization" — without proving that any given reweighting scheme or margin loss is equivalent to some instance of energy regularization. Figure 2 provides empirical support for LDAM (margin control), but the claim about reweighting methods is only argued intuitively ("by assigning different weights... the energy on more frequently trained data would be lower"). The paper would be stronger by framing this as a *connection* or *reinterpretation* rather than a unification, which would better match what the mathematics actually establishes.

- **No variance estimates or statistical significance reported for any experimental result.** The paper reports only point estimates (single numbers) across all tables. There are no standard deviations, confidence intervals, or multiple-seed results. The text mentions "random search of 5 trails" for domain generalization, but no per-trial breakdown or variance is shown. Given that the gains are modest (1–2 percentage points on ImageNet-LT and many domain generalization settings), it is impossible to assess whether these improvements are statistically reliable or within the noise of a single run. This is a significant gap in experimental rigor.

- **The IAER method inherits well-known limitations of influence functions that are not fully addressed.** The influence function (Eq. 8–10) assumes: (a) the loss is twice differentiable and strictly convex, (b) the perturbation \(\epsilon\) is infinitesimal, and (c) the estimate is evaluated at the optimum. The paper then uses the computed influence to set per-sample coefficients \(\beta_{\mathbf{x}_i}\) via Eq. 11 and fine-tunes the model for multiple epochs (5 on CIFAR, 10 on ImageNet-LT, 30 on iNaturalist). During this fine-tuning, the parameters move significantly from the point where the Hessian was evaluated, the linear approximation becomes stale, and the convexity assumption is violated for neural networks. The paper acknowledges these limitations in the conclusion ("as defined for convex loss functions, the influence function may not reflect the actual influence for neural networks") but does not provide any analysis of how badly the approximation degrades during fine-tuning, nor does it justify why multi-epoch updates are reasonable despite the local nature of the estimate.

- **High computational cost with modest gains.** Table 6 reports that influence approximation takes 718 seconds on CIFAR10 (ResNet-32), and substantially more on larger datasets. The gains over strong baselines are often 1–2 percentage points, and on some settings (e.g., CIFAR100) the improvement is very small or the paper itself attributes the weak results to the influence estimate being inaccurate. For a method with this overhead, a user would need stronger evidence that the influence-based coefficients provide meaningful benefit over cheaper alternatives (e.g., uniform energy penalty, class-frequency-based coefficients, or gradient clipping).

### Minor

- **No ablation on the key hyperparameter \(\gamma\).** The coefficient \(\beta_{\mathbf{x}_i}\) in Eq. 11 depends on \(\gamma\) (stated as \(0<\gamma<1\)), but no sensitivity analysis or recommended value is provided. It is unclear how stable the results are to this choice.

- **The validation set for influence computation is drawn from the training set.** While this is standard practice in influence-function literature (Koh & Liang, 2017) and the paper is transparent about it, the paper's motivation section argues that energy regularization should push \(p(\mathbf{x})\) closer to the *test* distribution. Using a held-out training subset as the validation proxy means the method is optimizing for generalization within the training distribution, not explicitly aligning with an unknown test distribution. The paper does not disentangle whether IAER's gains come from this standard cross-validation effect or from a genuinely novel energy-alignment mechanism.

- **No comparison to simpler (non-influence) approaches for setting energy regularization coefficients.** The paper does not compare IAER against baselines such as: uniform energy penalty (same \(\beta\) for all samples), class-frequency-based \(\beta\) (higher penalty for frequent classes in long-tail settings), or gradient-norm-based weighting. Such comparisons would help attribute the gains specifically to the influence mechanism rather than to energy regularization in general.

- **Remark 4.1 (Arbitrary Energy) shows static decoupling but does not establish orthogonality during training.** The remark correctly proves that energy can be changed independently of conditional probabilities by adding a constant to all logits. However, during *training*, energy and predictions co-evolve through gradient updates; the remark does not guarantee that optimizing an energy regularizer does not interfere with risk optimization through training dynamics. The orthogonality claim (used to argue that energy regularization complements IRM) is therefore overstated based on this remark alone.

### Trivial
- The paper could include a small synthetic experiment where the ground-truth test distribution is known, to more cleanly illustrate how energy regularization aligns predicted \(p(\mathbf{x})\) with the test distribution.

## Nice-to-Haves
- An analysis of how the influence estimate changes during fine-tuning (e.g., does the sign/correlation remain stable across epochs?)
- Ablation study on \(\gamma\) showing sensitivity and recommended value
- Comparison to a "uniform energy penalty" baseline to isolate the value of influence-based coefficients
- Standard deviations or confidence intervals for the main results

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The specific CIFAR100 step-imbalance result (41.43% to 42.30%) shows regression."** The paper explicitly states that IAER *improves* on this setting ("IAER also improves the testing performance... on step-imbalanced CIFAR100"). The specific numbers cited by the reviewer come from an embedded table image that cannot be independently verified from the extracted text. Giving the paper text the benefit of the doubt, this claim is removed.

- **"Validation set from training is circular / does not help OOD generalization."** Using a held-out subset of training data as a validation set is standard practice in influence-function literature (Koh & Liang, 2017) and in meta-learning / cross-validation broadly. It is not "circular" — the validation set is held out from the training process. The paper also explicitly states this is done "for a fair comparison with previous works."

- **"The broad scope means each experiment is thin."** This is a subjective preference rather than a weakness. Covering three generalization settings (long-tail, subpopulation shift, domain generalization) demonstrates broad applicability and is appropriate for a method claiming to address OOD generalization generally.

- **"Section 5.2 finding is not used."** The paper does use this finding to argue that energy regularization targets a different signal from loss minimization, and to support the claim that unregularized energy on well-classified points may contribute to overfitting.

- **"Remark 4.1 orthogonality claim is completely unsupported."** The remark proves static decoupling, and the paper uses this to argue that energy regularization is *orthogonal* to risk-based methods (i.e., they address different aspects). This is a valid theoretical observation, though its limitations during training dynamics are noted in the Minor section above.

## Novel Insights

The reviews surface a tension in the paper's framing: the theoretical derivation shows energy regularization *produces* reweighting and margin effects, while the paper wants to claim that reweighting and margin methods *are* (implicitly) energy regularization. These are different logical directions, and the paper conflates them. The more defensible claim — and the one the evidence actually supports — is that energy regularization provides a *unifying perspective* under which reweighting and margin control can be understood as different manifestations of the same underlying principle. This is still a valuable intellectual contribution, especially when paired with the empirical finding that LDAM indeed equalizes energy. The paper's most interesting scientific contribution may be the empirical demonstration that energy among training samples is biased and that existing methods inadvertently correct this bias, rather than the IAER method itself, which has practical limitations.

## Suggestions

1. **Reframe the "unification" claim more precisely.** State that energy regularization produces gradient effects that *combine* reweighting and margin control, and that existing methods *can be reinterpreted* through this lens (supported by Figure 2 for LDAM). Avoid claiming equivalence without formal proof.

2. **Report standard deviations for all main results** (Tables 2–5) by running experiments with at least 3 random seeds. This would substantially strengthen the empirical contribution.

3. **Include an ablation on \(\gamma\)** and a comparison to simpler energy-regularization baselines (e.g., uniform \(\beta\), class-frequency-based \(\beta\)). This would help disentangle the value of the influence mechanism from the value of energy regularization in general.

4. **Analyze how the influence estimate evolves during fine-tuning** (e.g., track the Spearman correlation between initial influence scores and the actual effect of energy regularization after k epochs). This would directly address the concern about the local linear approximation becoming stale.

5. **Consider a lightweight variant** that replaces influence functions with a simpler heuristic (e.g., energy variance penalty, or class-frequency-based coefficients) to demonstrate that the core idea (regularizing training energy) is practically viable without the computational overhead.

## Score and Decision

**Originality:** High — the paper introduces a genuinely novel perspective (energy among training samples) and provides a new theoretical connection.
**Importance:** Medium — the energy perspective could influence future work, but the proposed method (IAER) has practical limitations.
**Claims supported:** Partially — the theoretical derivation is sound and Figure 2 is convincing, but the unification claim is imprecise and the experimental results lack statistical rigor.
**Soundness:** Moderate — reasonable theoretical analysis with acknowledged limitations; experiments are broad but underreported (no variance).
**Clarity:** Good — the paper is well-structured and mostly clear.
**Value:** Medium — the core insight (energy regularization among training samples) is valuable; the specific method is less compelling.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>