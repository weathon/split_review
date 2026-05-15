Now I have thoroughly cross-checked all claims against the paper. Let me write the final consolidated review.

## Summary

This paper proposes k-CCP (k-Class-Conditional Conformal Prediction), a method that adds a per-class rank threshold on top of the standard class-conditional conformity-score threshold to produce smaller prediction sets while maintaining class-conditional coverage. The key idea is to restrict candidate labels to only the top-k predicted classes (based on the classifier's soft scores), using a second calibrated threshold per class. The paper provides theoretical analysis of why marginal CP fails on imbalanced data, a theorem giving sufficient conditions for k-CCP to achieve class-conditional coverage, and a theorem characterizing when k-CCP produces smaller sets than CCP. Experiments on CIFAR-10/100, mini-ImageNet, and Food-101 with three imbalance types show consistent and often large reductions in average prediction set size compared to CCP and cluster-CP.

## Strengths

- **Simple and intuitive algorithmic idea with strong empirical payoff.** The double-calibration approach (score threshold + rank threshold) is easy to understand and implement. The empirical results are striking: across four datasets and multiple imbalance settings (EXP, POLY, MAJ), k-CCP consistently halves or more the average prediction set size compared to CCP while maintaining the same near-zero under-coverage rate (e.g., mini-ImageNet EXP ρ=0.1 APS: APSS drops from 22.09 to 7.90 in Table 1).

- **Comprehensive empirical evaluation across diverse settings.** The paper tests on 4 datasets (CIFAR-10, CIFAR-100, mini-ImageNet, Food-101) with 3 imbalance types (EXP, POLY, MAJ), 2 scoring functions (APS, RAPS), and 2 imbalance ratios (ρ=0.5, 0.1). This is more thorough than typical CP papers. The sensitivity analysis (Figure 2) across a range of g values further demonstrates robustness.

- **Empirical verification of the theoretical condition for smaller prediction sets.** The paper measures the class-specific weights σ_y (from Theorem 2) and confirms they are much smaller than 1 on real datasets (Figure 1, last column), directly validating that the condition for smaller sets holds in practice. This bridges theory and observation.

- **Formal failure analysis of marginal CP for the class-conditional setting.** Proposition 1 provides a clean formalization of when and why marginal CP fails to provide class-conditional coverage, and the empirical visualization of class-wise quantile deviations (Figure 1, first column) validates that this failure mode is real on imbalanced data.

## Weaknesses

### Fatal
None.

### Major

1. **Balanced calibration set sidesteps the full imbalanced-data challenge.** The paper explicitly states: "We keep the calibration and test set balanced and unchanged" (Section 5.1). While the *training* set is imbalanced, the calibration set is balanced — meaning each class has the same number of calibration examples n_y. In a real imbalanced deployment, calibration data would typically exhibit the same long-tail distribution as the training data, and minority classes would have far fewer calibration points, directly affecting the concentration bound ε_{n_y} in Theorem 1. The paper never tests this scenario, so its central claim — that k-CCP is an effective solution *for imbalanced data* — is only partially supported by the experiments. The method may work well, but the hardest case (imbalanced calibration, where minority classes suffer from scarce calibration data) is unexamined.

2. **Theory-practice gap in the coverage guarantee.** Theorem 1 provides a sufficient condition involving ε_{n_y}, δ, and ε_y for the inflated miscoverage ñ_y. However, the practical algorithm (Equation 11) determines \hat{k}(y) using a heuristic rule with g/√n_y where g is tuned on validation, and there is no proof that this rule satisfies the condition in Theorem 1. The paper claims a "provable" coverage guarantee for k-CCP, but the proof applies to an idealized version of the algorithm, not the one actually implemented with hyperparameter tuning. The gap is acknowledged implicitly (g is "tuned on validation data in terms of small prediction sets") but the strength of the claim is not commensurate with the theoretical support. This is a substantive concern because the coverage guarantee is the main theoretical selling point.

3. **Theorem 2 is close to tautological and provides no actionable insight.** Theorem 2 states that if the σ_y-weighted sum of inclusion probabilities is smaller than the unweighted sum, then k-CCP produces smaller sets than CCP. Since σ_y is defined as the ratio of k-CCP's per-class inclusion probability to CCP's, the condition essentially restates "k-CCP includes each class with lower probability than CCP in aggregate." The real empirical contribution is showing σ_y < 1 (which the paper does), but the theorem itself does not provide a condition that can be checked a priori or that offers design guidance. This inflates the theoretical contribution beyond its substance.

### Minor

4. **Proposition 1 formalizes a well-known phenomenon without specific insight for imbalanced data.** The result that marginal CP can over-cover some classes and under-cover others when per-class quantiles deviate from the marginal quantile is a direct consequence of definitions and does not specifically address *why* imbalanced data makes this worse. The paper's empirical demonstration (Figure 1) of this deviation is more valuable than the proposition itself. The failure mechanism for minority classes is asserted rather than proven from properties of imbalanced data.

5. **UCR values are non-negligible on CIFAR-10 (≤0.16).** The paper reports controlling UCR "under 0.16 on CIFAR-10." With only 10 classes, this means ~1-2 classes are under-covered on average. For a method claiming class-conditional coverage, this is a notable empirical gap from the ideal (UCR=0). While finite-sample effects explain this, the paper should be more transparent about this limitation and discuss whether certain classes (e.g., minority) are disproportionately under-covered.

6. **Dependency of ε_y on the calibration set is not clarified.** The definition ε_y = ℙ_Z{r_f(X,Y) > \hat{k}(y) | Y=y} depends on \hat{k}(y), which is a function of the calibration data. The paper does not discuss whether the guarantee in Theorem 1 is conditional on the calibration set or unconditional, which affects the interpretation of the theoretical result.

### Trivial

7. The algorithm description (Section 4.1) refers to "Algorithm 1" but the pseudocode is not present in the extracted text (likely in the appendix). The paper should present the core logic inline.

## Nice-to-Haves

- **Imbalanced calibration ablation:** Repeating the main experiments with the calibration set drawn from the same imbalanced distribution as the training set would directly address the most significant gap and verify the method's robustness.
- **Standard deviation of coverage across classes:** The paper claims k-CCP has "more concentrated" class-conditional coverage than CCP (Figure 1, second column) but does not provide a quantitative comparison (e.g., standard deviation of per-class coverage). This would strengthen the visual claim.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **Harsh Critic point #3 (missing ablation — CCP with inflated quantile only):** REMOVED — Factually wrong. The evaluation methodology explicitly states: "we uniformly add g/√n to inflate the nominated coverage 1-α to each baseline" (Section 5.1). CCP, cluster-CP, and k-CCP all receive the same inflation treatment. The comparison isolates the rank constraint.
- **Harsh Critic point about missing related work (Podkopaev & Ramdas 2021):** REMOVED — Factually wrong. The paper explicitly cites this work in the Related Work section: "label-distribution shift (Podkopaev and Ramdas, 2021)."
- **Harsh Critic point about Proposition 1 derivation being "unclear":** REMOVED — Part of the garbled text is a parser artifact. The core idea (class-wise quantiles deviating from marginal quantile causes over/under coverage) is clearly stated.
- **Harsh Critic point about $\epsilon_y$ hiding calibration dependency:** MOVED to minor weakness #6 — The point has some validity but does not invalidate the result; it is standard for CP guarantees.
- **Strength Finder's strength #4 ("Formal failure analysis"):** WEAKENED — Proposition 1 does formalize the failure mode, but it is standard. This is reflected in minor weakness #4.
- **Strength Finder's strength #2 ("Theoretical guarantee of class-conditional coverage"):** LIMITED — The theory-practice gap (major weakness #2) tempers this strength. The paper has a theoretical framework but the implemented algorithm's guarantee is not proven.
- **Several generic strengths from Strength Finder (e.g., "identifies a genuine problem")** are generic and specific contributions are better captured by the strengths listed above.

## Novel Insights

The most interesting observation from the reviews is the identification of a disconnect between the paper's problem framing and experimental design. The paper motivates the work with the difficulty of imbalanced data, yet the experiments use a balanced calibration set. This reveals a broader pattern in the CP literature: it is common to use balanced calibration even when studying imbalanced training, but this choice means the method is only tested on half the challenge (imbalanced *training* affects the classifier's score distribution; imbalanced *calibration* affects the statistical power of the quantile estimates). The paper's results show k-CCP works well in the first scenario, but whether it survives the second — where minority classes have few calibration points — remains unknown. The theory-practice gap further suggests that, like many CP papers, the real contribution is algorithmic/empirical rather than theoretical, and the paper would be better served by acknowledging this framing.

## Suggestions

1. **Add experiments with imbalanced calibration set (same imbalance ratio as training).** This is the single most important addition. It would directly validate whether the method works under the full imbalanced-data setting the paper claims to address.
2. **Clarify the connection between Theorem 1 and the practical algorithm (Equation 11).** Either show that the g/√n_y rule is a valid instantiation of the theorem's condition with an empirical concentration bound, or clearly state that the algorithm is a heuristic motivated by the theory and the "provable" claim applies to an idealized version with known ε_y.
3. **Report the standard deviation of per-class coverage** (and ideally a per-class breakdown of coverage for minority vs. majority classes) to quantitatively support the "more concentrated" claim.
4. **Discuss the UCR=0.16 on CIFAR-10 explicitly** and report which classes (minority vs. majority) are under-covered. A UCR of 0.16 with C=10 means ~1-2 classes are under-covered, which deserves more analysis.

## Score and Decision

**Originality:** The dual-threshold calibration (score + rank) for class-conditional CP is a novel algorithmic contribution. The theoretical analysis is less novel (formalizing known phenomena).

**Importance of research question:** Class-conditional coverage for imbalanced data is a practically important problem, and producing small prediction sets has direct relevance for human-ML collaboration.

**Claims support:** The main empirical claim (k-CCP produces smaller sets than CCP/cluster-CP under balanced calibration) is well-supported. The claim of a "provable" coverage guarantee for the implemented algorithm is partially overstated. The claim about handling imbalanced data is only partially tested.

**Soundness of experiments:** The experimental design is generally solid (10 random splits, multiple datasets and imbalance types, controlled UCR). The main gap is the balanced calibration set choice.

**Clarity of writing:** The paper is generally clear, though the gap between theoretical presentation and algorithmic implementation could be better explained.

**Value to research community:** The algorithm is simple to implement and the improvements are substantial. The paper is likely to be practically useful.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>