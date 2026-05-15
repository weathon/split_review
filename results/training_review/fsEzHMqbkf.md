Now I have a thorough understanding of the paper and can verify the reviewer claims. Here is my consolidated review:

## Summary

This paper proposes the Conditional Density Ratio (CDR) score for post-hoc OOD detection. CDR combines a class-conditional generative model in latent space (via Mahalanobis or KDE) with a pre-trained discriminative classifier through Bayes' rule, estimating marginal density without marginalizing over classes. An automated temperature scaling method that requires only a small ID validation set (no OOD data) is introduced. Experiments on CIFAR10, CIFAR100, and ImageNet benchmarks show competitive performance.

## Strengths

- **Principled avoidance of marginalization via conditional density ratio.** The CDR score derives from the law of conditional probability ($p(z) = p(z|y)p(y)/p(y|z)$) without summing over classes, avoiding the constant-partition-function assumption that limits energy and GEM scores. This is a conceptually clean formulation (Section 3.2).

- **Automatic temperature scaling using only ID validation data.** The paper proposes a temperature tuning method (Algorithm 1) that requires no OOD samples — a practically important advantage for realistic deployment scenarios. Figure 3 shows temperature scaling consistently improves AUROC over no scaling, and Figure 4 demonstrates that automatically chosen temperatures yield AUROC close to optimal values.

- **Robustness to classifier quality demonstrated quantitatively.** The paper shows CDR maintains high OOD detection performance when classifier accuracy degrades (e.g., CIFAR10→CIFAR100: Energy AUROC drops from 91.99% to 77.20%, while CDR_Maha drops only from 97.41% to 95.66%). This robustness directly supports the claim that combining generative and discriminative components is beneficial.

- **General framework compatible with multiple density estimators.** CDR is instantiated with both Mahalanobis distance and KDE, and both variants achieve strong results (Tables 1-3). The extension to self-supervised learning (Table 4) further demonstrates the framework's generality.

- **Addresses a practical but under-explored scenario.** The setup (post-hoc detection with no training data, no OOD samples, only a small ID validation set) is realistic and well-motivated in the introduction.

## Weaknesses

### Fatal
None.

### Major

- **Unfair baseline comparison undermines headline results.** The paper states: "To compare with the baseline methods in their original configurations, we set temperatures to 1 for all the baseline methods" and "temperatures are only applied to the CDR scores." This means every baseline (MSP, Energy, Mahalanobis, GEM, GradNorm) uses default T=1 while CDR benefits from automated temperature tuning. Temperature scaling is known to significantly improve Energy and GEM scores (Liang et al., 2017; Lee et al., 2018). Moreover, temperature tuning for baselines using ID-only data is possible (e.g., NLL calibration for MSP is standard practice per Guo et al., 2017). The paper's central empirical claim — that CDR outperforms baselines on average — conflates the benefit of the CDR formulation with the benefit of temperature tuning. This issue cuts across all main tables (Tables 1–3) and Table 4.

- **Temperature scaling loss for $T_\phi$ can be undefined.** The loss function (Equation 4) takes the logarithm of $\hat{p}_\phi(z_i|y=y_i) - \frac{1}{K-1}\sum_{j\neq y_i}\hat{p}_\phi(z_i|y=j)$. This quantity can be negative (when the average density of non-ground-truth classes exceeds that of the true class), making the loss undefined. The paper neither discusses this edge case nor provides any guarantee or mitigation strategy. The grid search would silently fail for temperature values that produce negative arguments.

### Minor

- **No error bars or confidence intervals.** None of the results (Tables 1–4) report variance across different validation splits or random seeds. Given the small validation set (10% of training data for CIFARs, 25 samples/class for ImageNet), it is unclear how stable the reported numbers are. This is standard empirical practice for the field and would help assess reliability.

- **Limited analysis of failure cases.** The paper honestly acknowledges that CDR underperforms Energy on CIFAR100 hard-OOD when Mahalanobis distance performs poorly, but does not investigate the root cause (e.g., per-class diagnostics, whether the generative or discriminative component is the weaker link). A deeper failure analysis would strengthen the paper.

- **Grid search details are underspecified.** Algorithm 1 states "argmin" for temperature optimization but does not specify the search range, step size, or resolution. The text mentions grid search (line 123) but provides no operational details, affecting reproducibility.

### Trivial
None.

## Nice-to-Haves

- Run baselines with ID-data-based temperature tuning (e.g., NLL calibration for MSP, temperature search maximizing ID likelihood for Energy/GEM) to isolate CDR's contribution from the benefit of temperature scaling.
- Report results across multiple validation set splits with means and standard deviations.
- Ablate the effect of validation set size on CDR performance to support the claim of requiring "only a small number of inlier samples."

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Theoretical justification does not connect to empirical practice"** (Harsh Critic #3): The reviewer argues that CDR's validity depends on alignment between $\hat{p}_\phi(z|y)$ and $\hat{p}_\psi(y|z)$ and that the paper does not analyze conditions for accuracy. The paper provides a mathematically correct derivation from Bayes' rule, the regularization term in Equation 4 is designed to enforce alignment, and the ablation (Figure 2) empirically shows GCR is near zero for ID samples with correct scaling — providing reasonable if not formal validation. The paper also acknowledges limitations in the Discussion section. This is an empirical paper, and the criticism demands a theoretical rigor that is beyond scope.

- **"Algorithm 1 is vague"** (Section-by-Section notes): The criticism that no search range or step size is specified for grid search. While slightly underspecified, the paper notes that logits can be pre-computed and cached, making the grid search efficient. The specific grid range is a standard implementation detail that can be documented in a camera-ready revision but does not invalidate the method.

- **"The energy score requiring a constant partition function is not new"**: This is acknowledged in the paper's related work section and is background motivation, not a claimed contribution.

- **Generic strength from Strength Finder:** "Clear empirical advantage over prior post-hoc methods" — this strength is diminished by the baseline comparison issue identified above and should not be stated without caveat.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a central tension: the paper's core methodological idea (combining generative and discriminative densities via conditional ratios to avoid marginalization) is principled and the practical problem setup is well-motivated, but the experimental evaluation conflates the advantage of the CDR formulation with the advantage of temperature scaling, making it impossible to tell which factor drives the reported gains. This tension is the critical issue a revision must resolve.

## Suggestions

1. **Re-run all baselines with ID-data-based temperature tuning.** For MSP, use NLL calibration (standard practice, Guo et al., 2017). For Energy and GEM, search for the temperature that maximizes ID likelihood or some other ID-only criterion analogous to what CDR uses. Report both T=1 and tuned results so readers can isolate the effect of tuning from the effect of CDR's formulation.

2. **Address the log-instability in Equation 4.** Either prove that the quantity inside the log is always positive for well-chosen temperatures, add a small constant/clipping to ensure numerical stability, or discuss when and why it might become negative and how the grid search handles it.

3. **Add error bars.** Run experiments with different validation set splits (or bootstrap) and report standard deviations for AUROC and FPR95.

4. **Specify grid search details.** Document the temperature range and step size used in the paper's experiments.

## Score and Decision

The paper's core idea (CDR) is principled and the practical setup is well-motivated. However, the experimental evaluation contains a significant confound: CDR benefits from automated temperature scaling while baselines are restricted to default T=1. This undermines the headline empirical claims. The temperature scaling loss function also has a mathematical edge case that is not addressed. The paper needs substantial revision before its contribution can be properly assessed.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>