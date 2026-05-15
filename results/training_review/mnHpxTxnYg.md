Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper investigates black-box membership inference attacks against GANs, where the adversary only has access to generator samples (not the discriminator). The core attack ("Detector") trains a classifier to distinguish GAN-generated samples from real distribution samples, then uses that classifier's confidence as a membership score. The paper introduces an augmented variant (ADIS) that enriches the detector's feature space with distance-based statistics, provides a theoretical analysis (Theorem 4.1) motivating why such detectors can work for membership inference, and evaluates seven attack methods across two genomic datasets (1KG, dbGaP) at three dimensionalities and four image GAN architectures on CIFAR-10.

## Strengths

- **Thorough empirical evaluation across diverse domains and architectures.** The paper evaluates 7 attack methods on 2 genomic datasets at 3 dimensions each, using 2 GAN architectures per dataset, plus 4 image GAN architectures on CIFAR-10. Each configuration is averaged over 11 training runs. This is the most comprehensive black-box MIA benchmark for GANs to date.

- **Addresses a practical gap in prior work.** Most prior GAN privacy attacks assume white-box access to the discriminator (which is typically not released). Focusing on the black-box setting where only generator samples are available is more practically relevant, especially for copyright and sensitive-data sharing scenarios.

- **Proper evaluation methodology.** The paper adopts best-practice MIA evaluation metrics (log-log ROC curves, TPR at low FPRs of .001, .005, .01, .1) as advocated by Carlini et al. (2021), going beyond the average-case AUC metrics used in prior GAN attack papers.

- **ADIS provides a genuine improvement over existing attacks.** The augmented detector variant (ADIS), which enriches the detector's feature space with distance-based statistics, achieves measurably higher TPRs at low FPRs (up to 10× the random baseline on dbGaP WGAN-GP), outperforming both pure detector and pure distance-based attacks in several settings.

- **Systematic comparison against multiple baselines.** The paper evaluates one-way/two-way distance attacks, DOMIAS, and the robust Homer attack across all settings, providing a clear picture of relative attack effectiveness that varies by GAN architecture, data domain, and dimensionality.

## Weaknesses

### Major

- **Low-FPR results lack uncertainty quantification.** The paper repeatedly emphasizes TPR at low FPRs (0.001, 0.005, 0.01) as the most meaningful metric, yet reports only AUC standard deviations, not variances for the low-FPR TPRs themselves. On 1KG (500 member + 500 non-member evaluation points), an FPR of 0.001 corresponds to roughly 0.5 expected false positives, making per-run estimates extremely noisy. Averaging over 11 runs helps, but without confidence intervals or standard deviations for the low-FPR TPRs, it is difficult to assess whether the reported 2–6× improvements over random are statistically robust or driven by tail noise. This should be addressed with bootstrapped intervals or reported standard deviations for the TPR at each fixed FPR.

- **Abstract and introduction overstate the novelty of the Detector attack.** The abstract says "introduce a suite of membership inference attacks" and calls the method "The Distinguisher" (inconsistently named versus "Detector" in the rest of the paper). The contributions list frames the Detector as the paper's main attack. However, as the paper itself acknowledges in Section 2 (lines 27), Hayes et al. (2019, Section 4.4) previously proposed a black-box attack that "is very similar to the Detector"—training a discriminative model to classify GAN samples from test samples. The paper distinguishes itself via (i) new genomic data domains, (ii) the ADIS extension, and (iii) log-log ROC evaluation. These are valid differentiators, but the framing in the abstract/intro does not adequately reflect that the core Detector idea is adapted from prior work, not newly proposed. This naming inconsistency and framing gap should be fixed.

### Minor

- **Theorem 4.1 assumes an unvalidated condition.** The theorem assumes the generator distribution is a convex mixture of the training set and the reference distribution: G = βP + (1-β)T. The paper acknowledges this is "a stronger assumption" and that the result is "better viewed as showing why our Detector outperforms the random baseline." However, the assumption is never empirically validated for any trained GAN, and the link to "partial mode collapse" (which in standard usage means concentrating on few modes of P, not mixing in training points) is imprecise. The theorem provides useful intuition but would be strengthened by empirical verification (e.g., estimating β on held-out data or checking whether the detector's ranking correlates with the optimal score under the model).

- **The comparison to diffusion model privacy leakage is not directly supported.** The paper states that black-box access to GANs "seems much more private" than diffusion models (Carlini et al., 2023) and VAEs (Hayes et al., 2019). The paper hedges this claim ("is this actually the case, or is it simply a matter of developing better attack methods?") but the statement is still made without a controlled comparison under identical datasets and evaluation protocols. The results are not directly comparable across different papers with different experimental setups.

- **ADIS is only evaluated on genomic data, not on image GANs.** The augmented detector variant (ADIS) is one of the paper's more novel contributions, but is tested only on the tabular/genomic experiments (Section 5), not on the CIFAR-10 image experiments (Section 6). Evaluating ADIS on images would strengthen the generality claim.

- **Small training set sizes relative to feature dimensions for genomic GANs may inflate attack success.** On 1KG (3000 training samples for up to 10,000 SNPs) and dbGaP (6500 samples), the sample-to-dimension ratio is very low. The paper acknowledges this setting is realistic for genomic data but does not disentangle whether the observed attack success is due to GAN memorization of training points (which is more likely when the generator is severely overparameterized) versus a more general privacy leakage phenomenon.

- **The mixture-model assumption in Theorem 4.1 is not validated empirically.** This is worth repeating as a minor point because even a simple empirical check (e.g., whether the detector's learned decision boundary is consistent with the assumed mixture form) would significantly strengthen the paper's theoretical contribution.

### Trivial

- The paper calls the attack "The Distinguisher" in the abstract but "Detector" throughout the rest of the paper. This naming inconsistency should be resolved.

## Nice-to-Haves

- An ablation study for ADIS showing the marginal benefit of adding distance-based features versus the plain Detector, particularly in settings where distance-based attacks already perform well (e.g., Vanilla GAN on 1KG 805 SNPs).
- A characterization of which training points are successfully identified (e.g., are they outliers? Do they have unusual feature values?) to provide qualitative insight into what the detector is exploiting.
- Example visualizations of high-scoring members and false positives from the image experiments.

## Removed Points

These points were raised in reviews but removed because they are factually incorrect, misunderstand the paper, or violate the removal rules:

- **"The paper's main method is a re-evaluation of an existing attack on new domains, not a novel attack"** — The paper transparently acknowledges Hayes et al. (2019) as prior work describing a similar attack (Section 2). The ADIS variant is novel. The contribution is honestly scoped in the related work section, even if the abstract/intro framing could be improved. Kept as a minor (framing) weakness but the "not novel at all" characterization is too harsh given the acknowledged prior work and the novel ADIS extension.

- **"The theoretical contribution is vacuous and potentially misleading"** — The paper acknowledges Theorem 4.1 relies on a "stronger assumption" and presents it as providing intuition, not as a precise model of real GAN behavior. Calling it "vacuous" is an overstatement; it is a clean theoretical result under a stated idealization, which is standard practice. The criticism is retained in weakened form (unvalidated assumption).

- **"No variance or confidence intervals for low-FPR TPRs... the claim could be driven by noise"** — Retained as a major weakness regarding uncertainty quantification. However, the claim that results "could be driven by noise" is too dismissive—consistent 2–6× improvements across multiple architectures, datasets, and 11-run averages is unlikely to be pure noise, even if the exact TPR values at FPR 0.001 have wide confidence intervals.

- **Request to replicate Hayes et al. (2019) exact setup** — This is a reasonable suggestion but not a mandatory experiment; the paper clearly explains what differs from Hayes et al. (2019) and is not required to exactly reproduce their conditions to make a valid point about new data domains and metrics.

- **Request for white-box comparison** — The paper explicitly scopes itself to the black-box setting. Asking for white-box baselines is scope creep for this paper.

- **Formatting/style nitpicks** — Removed per instructions.

## Novel Insights

The reviews do not surface a genuinely novel observation beyond the paper's own contributions. The key tension that emerges—whether the Detector's success is driven by the GAN memorizing training points (inflated by low sample-to-dimension ratios in genomic settings) versus a more general property of the detector's decision boundary aligning with membership—is an important question the paper partially raises but does not resolve. This is a worthwhile direction for future work that the paper itself gestures toward.

## Suggestions

1. **Reframe the contribution honestly.** Revise the abstract and introduction to clearly state that the Detector attack builds on Hayes et al. (2019), and position the paper's novel contributions as: (i) the ADIS extension, (ii) the first systematic evaluation on genomic data, (iii) evaluation with modern best-practice MIA metrics, and (iv) the theoretical analysis. Resolve the "Distinguisher"/"Detector" naming inconsistency.

2. **Report confidence intervals or standard deviations for TPR at each low FPR** (0.001, 0.005, 0.01) across the 11 runs, not just for AUC. This is critical because at FPR 0.001 the number of expected false positives in the evaluation set is ≤1, making single-run estimates highly variable.

3. **Empirically validate or at least probe the mixture-model assumption** of Theorem 4.1, e.g., by fitting the mixing coefficient β on held-out data or checking whether the top-k detected members are consistent with the assumed generative process.

4. **Either add a controlled comparison to diffusion models under the same conditions** or remove/downplay the "more private than diffusion models" claim. As written, the claim references results from different papers with different setups.

5. **Evaluate ADIS on image GANs** to demonstrate its generality beyond genomic data, or explicitly scope it as a genomic-domain extension.

## Score and Decision

The paper makes a modest but genuine empirical contribution through its thorough evaluation of black-box MIAs against GANs on genomic and image data, its novel ADIS extension, and its adoption of best-practice evaluation metrics. However, the overstated novelty framing, lack of uncertainty quantification for the headline low-FPR results, and unvalidated theoretical assumptions prevent it from being a strong paper. These issues are fixable with revision, but in the current form they meaningfully weaken the paper.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>