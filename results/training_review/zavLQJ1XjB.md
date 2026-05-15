I have carefully verified each claim against the paper text. Let me now produce the consolidated review.

## Summary

This paper studies the limitations of temperature scaling (TS) for classification under class-overlapping data distributions. The authors prove that for ERM interpolators satisfying a local Lipschitz-like condition (γ-regularity), even oracle temperature scaling yields calibration error that grows with the overlap between classes and becomes no better than random as the number of classes increases. Conversely, they prove that models minimizing a modified Mixup objective (d-Mixup, mixing d+1 points) provably achieve constant calibration error independent of overlap. Experiments on synthetic Gaussian data (with d-Mixup d=2,4) and image benchmarks CIFAR-10/100, SVHN (with 2-point Mixup) show that Mixup-based models substantially outperform ERM+TS under label noise.

## Strengths

1. **First rigorous theoretical identification of class overlap as a specific bottleneck for temperature scaling.** Theorem 4.1 (generalerm) and Proposition 4.1 (warmuperm) formally prove that for ERM interpolators satisfying γ-regularity, even oracle-optimal temperature scaling yields calibration error that scales with overlap α and becomes vacuous as k grows. This provides a principled explanation for empirical observations that TS often underperforms training-time methods.

2. **Provable guarantee that d-Mixup circumvents this bottleneck.** Theorem 4.3 (generalmix) and Proposition 4.2 (warmupmix) prove that d-Mixup interpolators achieve calibration error independent of the overlap parameter α, whereas ERM+TS error degrades with α. Lemma 3.1 (infdmixopt) gives an exact characterization of d-Mixup optimal predictions, enabling the analysis.

3. **Empirical validation across both synthetic and realistic settings.** Table 2 (synthetic Gaussian with μ=0.25, 0.05, 0.01) shows that ERM+TS NLL jumps from 0.26 to 4.30 with increasing overlap while d-Mixup (d=4) NLL stays near 0.74. Table 3 (CIFAR-10/100, SVHN with 0–50% label noise) shows the same qualitative pattern: ERM+TS NLL degrades much faster than Mixup NLL. The SVHN result is particularly clean, as the paper notes ERM actually achieves better test error but far worse NLL.

4. **Empirical verification that practical models exhibit large logit separation (Table 1).** ResNeXt-50 models on CIFAR-10/100 and SVHN show max logit ~11–19 and second-max logit ranging from ~0.4 to -4.2, supporting the ERM interpolator definition and making the theory's assumptions grounded in observed behavior.

## Weaknesses

### Major

1. **Theory-practice gap: the positive theoretical result covers d-Mixup, but the practical method that works in image experiments is standard 2-point Mixup.** The paper proves calibration guarantees for d-Mixup (mixing d+1 points) but all image benchmarks use regular 2-point Mixup. The paper offers only a conjecture that "due to the structure of practical models (i.e. neural networks), even mixing two points is sufficient" — with no theoretical justification or systematic empirical bridge. When d-Mixup (d>2) is tested on images, the paper reports it "led to underconfidence" and omits the results. This means: (a) the theory does not explain why regular Mixup works on real data, and (b) the positive experimental evidence for d-Mixup is limited to a 2-class 300D synthetic problem, which is far from the many-class asymptotic regime the theory addresses. The paper's central claim — that training-time modifications like Mixup provably overcome TS's limitations — is formally proven for a different algorithm than the one validated on real benchmarks.

2. **The γ-regularity assumption (Definition 2.2) is neither verified nor obviously plausible at the required scale.** Theorem 4.1 requires models to be r-regular where r is such that a sphere of radius r in ℝ^d has volume k/(2MN). In the synthetic experiment (d=300, N=4000, k=2), this radius is vanishingly small. The paper provides no empirical evidence — by measuring local logit variation at this scale or citing existing results — that neural networks satisfy the required Lipschitz condition at such tiny radii. Table 1 shows large logit margins on training points, but this does not imply local smoothness at sub-training-point scales. Without verification, the negative result may describe a scenario that does not occur in practice. (The experiments do show ERM+TS *does* fail with overlaps, but this could be caused by other factors — the mechanism is not isolated.)

### Minor

3. **Missing baselines weaken the empirical support for the paper's framing.** The main experimental comparison is ERM+TS vs. Mixup (without TS). Left out: (a) ERM without TS — without this, we cannot assess whether TS helps at all or whether the story is simply "ERM is bad, Mixup is better," which is already known (Thulasidasan et al., 2019); (b) Mixup+TS — if TS further improves Mixup, the "limitations of TS" framing would need nuance, and if it does not, that claim should be demonstrated. Neither baseline is included.

4. **Incomplete calibration metrics on image benchmarks.** For synthetic data (Table 2), the paper reports NLL, ECE, and ACE. For image data (Table 3), only NLL is tabulated. The paper mentions that "ACE does not remain consistent" and that confidence histograms and reliability diagrams were generated, but these results are not shown. Without ECE/ACE for image experiments or the visualizations, calibration quality cannot be fully assessed on the main benchmarks.

5. **Logit margin verification is reported only as means, not per-point.** Definition 2.1 requires every training point to satisfy a logit margin > log k. Table 1 reports mean max and second-max logits, which is insufficient to verify that all points satisfy the margin. Individual outliers could violate the condition.

### Trivial

6. **The definition of ℳ_d(𝒳) (the allowed mixing set) is informal.** The paper states mixings must involve points "at most some constant distance away" that are not "too highly correlated," without quantifying either condition. While formal details may appear in the appendix (which is stripped by the parser), the main text would benefit from a precise definition.

## Nice-to-Haves

- Testing the many-class prediction directly: running the synthetic Gaussian experiment with k=10, 50, 100 (not just 2) would directly probe Theorems 4.1/4.2.
- For the image benchmarks, reporting ECE/ACE and including confidence histograms / reliability diagrams (as done for synthetic data) would strengthen the empirical support.
- An analysis of why d-Mixup (d>2) causes underconfidence on image data would clarify whether the theoretical d-Mixup story can ever be practical for high-dimensional inputs, or whether 2-point Mixup succeeds for different reasons.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The bimodal TS histogram contradicts the theory's claim that TS pushes predictions toward uniform."** REMOVED (factually incorrect). The theory's lower bound (KL divergence ≥ Θ((1−α−1/k) log k)) is about the *optimal* TS solution. The bimodal histogram shows practical TS performs at best this poorly (often worse), which is fully consistent. The theory does not claim predictions become uniform in the finite-sample setting — the bound is the same sign as the empirical observation, not a contradiction.

- **"Oracle TS is unrealistic; the paper should note that experimental TS uses a finite calibration set."** REMOVED (paper already addresses this). Lines 65–69 explicitly state: "we will in fact consider an even more powerful (and impractical) form of temperature scaling" and "even when we allow this 'oracle' temperature scaling, we cannot hope to calibrate models."

- **"The spacing assumption is restrictive and not discussed in context of real data."** REMOVED (paper already discusses it). Lines 159–160 state: "The spacing of k between pairs of classes is introduced only to simplify the d-Mixup analysis; it is not necessary for proving the negative results regarding ERM interpolators, and will not feature when we generalize to Definition 3.4."

- **"The choice of expected KL divergence is not used in experiments."** REMOVED (paper justifies this). Lines 56–58 explain that KL divergence is used because it more accurately characterizes calibration, but it is "difficult to estimate in reality as we do not know π(Y|X)." The justification is adequate.

- **"L in Definition 2.2 is unspecified."** REMOVED (standard modeling choice in theory papers). The existence of a universal constant L is a standard theoretical modeling assumption.

- **"The paper should note that the label noise procedure differs from the general overlapping supports in the theory."** REMOVED (this is scope creep — the paper is providing a controlled experimental instantiation of overlap, which is standard practice).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Bridge the d-Mixup / 2-Mixup gap.** Either (a) prove that 2-point Mixup induces neighborhood constraints for relevant function classes (e.g., ReLU networks with bounded Lipschitz constant), or (b) provide an empirical study showing that 2-point Mixup, d-Mixup, and the theory's predictions are quantitatively consistent on a controlled synthetic problem with many classes.

2. **Add the two missing baselines:** ERM without TS and Mixup+TS on both synthetic and image data. This would clarify whether TS helps at all and whether Mixup leaves room for further post-hoc improvement.

3. **Report ECE and ACE for image benchmarks** and include confidence histograms/reliability diagrams (as done for synthetic data) to give a complete picture of calibration quality.

4. **Verify γ-regularity empirically** on the synthetic or image data by measuring how much the winning logit changes within spheres of the theoretically specified radius. If the assumption is violated, discuss what other mechanism might drive the observed TS failure.

5. **Report per-point logit margin statistics** (e.g., minimum margin, 5th percentile) in addition to means, to confirm that the ERM interpolator condition holds for all training points.

## Score and Decision

The paper makes a genuine theoretical contribution by formally identifying class overlap as a bottleneck for temperature scaling and showing that d-Mixup can circumvent it. The core intuition (neighborhood constraints) is sound, and the theoretical development is rigorous under the stated assumptions. The experiments provide supporting evidence for the overall qualitative story.

However, the paper suffers from a meaningful theory-practice gap: the positive result is proven for d-Mixup while the practical successes on real data use 2-point Mixup, with only a conjecture linking them. The γ-regularity assumption underlying the negative result is unverified at the required scale. The experimental evaluation has addressable holes (missing baselines, incomplete metrics). These weaknesses are not fatal — the paper's contributions are real — but they prevent the paper from being a strong accept.

The paper would be strengthened substantially by addressing the theory-practice gap (either theoretically or with more complete d-Mixup experiments), adding baselines, and reporting full metrics. As it stands, the paper offers a valuable theoretical framework and suggestive empirical evidence, but stops short of a fully closed case.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>