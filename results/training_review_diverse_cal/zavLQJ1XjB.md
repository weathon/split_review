Now I have a thorough understanding of the paper and all the reviewer claims. Let me construct the final review.

## Summary

This paper studies the limitations of temperature scaling (TS) for calibrating neural networks on classification distributions with overlapping class supports. The authors prove a theoretical lower bound: for ERM interpolators that satisfy a local Lipschitz-like condition (γ-regularity), even oracle temperature scaling yields KL divergence that grows with the number of classes, becoming asymptotically no better than random when overlap is present. They further prove that a modified form of Mixup (d-Mixup) overcomes this limitation. Experiments on synthetic Gaussian data and image benchmarks (CIFAR-10/100, SVHN with label noise) confirm the qualitative predictions: ERM+TS degrades sharply with increasing overlap while Mixup remains relatively robust.

## Strengths

- **Rigorous theoretical identification of a fundamental bottleneck for temperature scaling.** The paper provides formal lower bounds (Proposition 1 / Theorem 6) showing that for ERM interpolators satisfying γ-regularity over overlapping regions, even oracle-optimal temperature scaling yields KL divergence of Θ((1−α−1/k) log k), which is asymptotically no better than random when α = O(1) and k is large. This identifies a concrete mechanism — interpolating models with local smoothness on overlapping distributions — by which TS can provably fail.

- **Theoretical proof that d-Mixup circumvents the limitation.** The paper shows (Proposition 2 / Theorem 7) that d-Mixup interpolators achieve O(1) KL divergence independent of the overlap parameter α, establishing that training-time modifications can provably overcome the bottleneck that defeats TS.

- **Strong empirical validation of the predicted qualitative behavior.** On 300-D synthetic Gaussian data (Table 1), ERM+TS NLL jumps from 0.26 to 4.30 as overlap increases, while Mixup variants stay below 0.83. On CIFAR-10/100, SVHN with label noise (Table 2), the same pattern holds: ERM+TS NLL degrades sharply (e.g., CIFAR-10: 2.01 → 5.95) while Mixup NLL increases much more slowly (0.82 → 1.77). Confidence histograms (Figure 1) confirm the mechanism is calibration, not accuracy.

- **Use of an oracle temperature scaling baseline strengthens the negative result.** The theory considers TS that has access to the ground-truth π(Y|X) (Eq. 4), making the failure result stronger than if it only used a finite calibration set. Despite this unrealistic advantage, the lower bound still holds.

- **Empirical grounding of the interpolation condition.** Table 1 reports ResNeXt-50 logit statistics on CIFAR-10/100 and SVHN, showing large max/second-max logit gaps (14.6 vs 0.37 on CIFAR-10), validating the ERM interpolator definition (Definition 2).

## Weaknesses

### Fatal
None.

### Major
None. The paper's core contributions — conditional theoretical results and empirical demonstrations that match the predicted qualitative behavior — are valid. The weaknesses below are substantive but do not invalidate the paper's claims.

### Minor

- **γ-regularity assumption is not empirically verified despite being described as "empirically-observed."** The paper's negative theorem (Theorem 6 / Proposition 1) is conditional on the γ-regular condition (Definition 3). The paper provides empirical evidence for the interpolation condition (Table 1: logit separation) but presents no measurement of whether trained networks satisfy the γ-regular property — i.e., that logits change by at most Lγ within γ-balls around training points with high conditional probability. The paper describes the models as satisfying "some empirically-observed regularity properties" (line 69), which is accurate for interpolation but unverified for γ-regularity. This does not invalidate the theoretical result (which is a conditional statement), but it weakens the claim that the theory directly explains the empirical observations, since the causal link (trained models are actually γ-regular) is not checked. The paper would be stronger with a direct measurement (e.g., logit variation within γ-sized balls on the synthetic data).

- **The positive theoretical result uses d-Mixup, while the practical experiments primarily use standard 2-Mixup.** The paper fully acknowledges this gap (Remark, lines 145–147: "we conjecture that due to the structure of practical models... even mixing two points as in traditional Mixup is sufficient"). The theory proves that d-Mixup (mixing d+1 points) works; the experiments show that standard Mixup works empirically. On image benchmarks, d>2 Mixup underperforms (line 282). This gap means the theory does not directly explain why the practical method succeeds, though the authors are transparent about it and provide a reasonable conjecture. The synthetic experiments with d=2,4 Mixup partially bridge this gap.

- **Image experiments introduce label noise on training labels while evaluating on clean test data, which differs from the theoretical setup.** The theory considers a distribution π with genuinely overlapping class supports, with calibration evaluated w.r.t. the same π. The image experiments (Section 5.2) add label noise to training labels but evaluate on clean test data — a train–test shift, not identical distribution. While label noise creates effective class overlap in the training distribution (matching the theory's mechanism), the clean test evaluation introduces a distribution mismatch. The synthetic Gaussian experiments (Section 5.1), where test data shares the same overlapping distribution as training, are a clean test of the theory. The image experiments are best interpreted as supplementary practical validation showing the phenomenon generalizes to realistic settings, rather than a direct test of the theory. Clarifying this framing would help.

### Trivial

- **The choice of γ (radius such that sphere volume = k/(2MN)) is derived from volume-based packing arguments but the paper does not discuss how this γ compares to typical distances between training points or to the local behavior of trained networks.** Since γ-regularity is a critical assumption, adding intuition about the scale of γ would improve readability. For instance, in the synthetic Gaussian setup (d=300, N=4000, k=2, M=1), one could compute and report γ to give readers a concrete sense of the scale.

## Nice-to-Haves

- Compare Mixup against other training-time calibration methods (e.g., label smoothing, MMCE, focal loss) to help isolate whether Mixup's advantage is specific to it or general to training-time regularization.
- Design an image experiment where the test distribution genuinely has overlapping class supports (e.g., by blurring or merging classes) rather than relying on label noise, to provide a cleaner test of the theory on realistic data.

## Removed Points

These points from the reviews are not included as weaknesses; they are preserved here in case useful:

1. **"The oracle temperature scaling is so unrealistic."** — The reviewer treats this as a weakness, but the paper uses it as a strength: showing TS fails even with an (impossible) oracle makes the negative result stronger. This is a standard "best-case analysis" approach.

2. **"d>2 underperforms on image benchmarks."** — The paper explicitly acknowledges this (line 282). It is a practical limitation but not a flaw in the analysis; the key practical result is that standard Mixup (2-Mixup) works well.

3. **"The paper does not compare with other training-time calibration methods."** — This is scope creep; the paper focuses on Mixup vs. TS, and adding every alternative method would make it a different study. Included in Nice-to-Haves above.

4. **Various formatting, typo, or style complaints from the original reviews.** — These are parser artifacts, not author errors.

## Novel Insights

The most interesting synthesis from the reviews is that the paper's core theoretical contribution (the γ-regularity assumption as a sufficient condition for TS failure) is simultaneously its most original and least verified aspect. The reviewers correctly identify that the interpolation condition alone is insufficient for the negative result — the local Lipschitz structure (γ-regularity) is what makes the analysis work. This suggests a potentially productive research direction: empirical characterization of the local Lipschitz constants of neural networks at the scale of typical inter-point distances, which could either validate or refine the theoretical assumptions made here. The d-Mixup analysis is also noteworthy for the technical innovation of using (d+1)-point convex combinations to achieve measure-theoretic coverage of the ambient space, a technique that may find use beyond calibration.

## Suggestions

- **Empirically validate γ-regularity on the synthetic Gaussian data.** Measure logit variation within γ-sized balls around training points (where γ is derived from the volume condition) and report the fraction of balls where the conditional probability in Definition 3 holds. This would directly connect the theory to the experiments and significantly raise confidence in the mechanism.

- **Reframe the image experiments.** Explicitly state that the synthetic experiments are the clean test of the theory, while the image benchmarks are practical extensions that demonstrate the phenomenon carries over to realistic settings despite a train–test distribution mismatch. Add a sentence clarifying how label noise relates to (but differs from) the distributional overlap of Definition 5.

- **Compute and report γ for the synthetic setup.** This would ground the otherwise abstract parameter and let readers assess its plausibility relative to typical inter-point distances.

- **Consider adding a footnote or short discussion comparing the γ-regular condition to known results on adversarial robustness or local Lipschitz constants of overparameterized networks**, to help readers gauge whether the assumption is reasonable.

## Score and Decision

The paper makes a real contribution: it identifies a precise mechanism (interpolating γ-regular models on overlapping distributions) by which temperature scaling provably fails, and shows d-Mixup can overcome this. The theoretical work is rigorous, the experiments confirm the qualitative predictions, and the paper is transparent about its limitations (the d-Mixup/standard Mixup gap, the practical nature of the image benchmarks). The main weakness is that the critical γ-regularity assumption is not empirically verified, and the paper's framing slightly overstates the degree to which the conditions are "empirically observed." This is a genuine gap but not a fatal one — it weakens the theory→experiment link without invalidating either the conditional theory or the empirical observations independently. With a moderate revision addressing this gap and clarifying the experimental framing, the paper would be a solid contribution. In its current form, it is a strong paper with one significant unverified link.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>