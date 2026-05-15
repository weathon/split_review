Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper studies the double descent phenomenon in deep learning by analyzing the learned feature space of trained models. The authors introduce a k-NN based metric \(P\) that measures how often noisy training points have nearest clean neighbors sharing the same original (pre-corruption) class in the penultimate-layer representation space. Across experiments with FCNN+MNIST, CNN+CIFAR-10, and ResNet18+CIFAR-10 at varying label noise levels, the paper finds that for FCNN and CNN, \(P\) correlates with test accuracy across model widths, while for ResNet18 the k-NN predicts the *noisy* label rather than the clean label for over-parameterized models. The paper argues that over-parameterized models "isolate" noisy data by interpolating them among correct same-class samples, and that this explains the second descent.

## Strengths

- **Simple, interpretable probe of the learned feature space.** The k-NN accuracy \(P\) (Eq. 1) is a straightforward diagnostic that asks whether noisy training points are geometrically closer to clean points of their true class than to points of other classes. This avoids opaque summaries and makes the analysis directly testable. The computation uses only the training set and requires no separate validation data.

- **Replication of double descent across architectures and noise levels is thorough.** The paper follows the established setup of Nakkiran et al. (2021) and reproduces double descent for three architectures, two datasets, and multiple noise levels (p=0%, 10%, 20%). The experimental protocol — no data augmentation, no explicit regularization, controlled width scaling — is clearly documented and consistently applied, making the results reproducible.

- **Honest reporting of contradictory evidence.** The ResNet18 result (\(P\) drops to zero at the interpolation threshold and the k-NN predicts noisy labels) is explicitly identified as contradicting the paper's hypothesis (Sec. 4, Fig. 3 caption, and the surrounding text). The authors do not suppress or gloss over this result. This transparency is a scientific strength, even though the contradiction is not resolved.

- **The paper demonstrates that \(P\) can serve as a training-set-only signal that co-varies with generalization for FCNN and CNN.** This is a concrete empirical observation that goes beyond simply noting that double descent exists — it connects the phenomenon to a measurable property of the learned representation (for those architectures).

## Weaknesses

### Fatal

None.

### Major

- **The ResNet18 results directly contradict the paper's central explanatory mechanism, and the contradiction is not resolved.** The paper claims that over-parameterized models improve generalization by "isolating" noisy samples — i.e., placing them among clean samples of the same original class. For FCNN+MNIST and CNN+CIFAR-10, \(P\) (which measures exactly this) rises in the over-parameterized regime, consistent with the story. For ResNet18+CIFAR-10, however, \(P\) drops to zero at the interpolation threshold and stays zero — the k-NN predicts the *noisy* label, not the clean one. Since ResNet18 exhibits double descent as clearly as the other architectures, the proposed mechanism cannot be the general explanation the paper claims. The paper's only explanation ("superior feature extraction ability of ResNets," line 171) is vague and does not account for *why* double descent still occurs despite the opposite isolation pattern. This is not a minor caveat — it undermines the core claim that noise isolation *drives* the second descent. (Sec. 4, Fig. 3, lines 171–174)

- **The evidence is correlational, not causal; no intervention establishes that \(P\) drives test performance.** The paper shows that, for two of three architectures, the trend of \(P\) (computed on training data) roughly follows that of test accuracy. Correlation does not imply causation, and the paper offers no experiment that manipulates \(P\) (e.g., via regularization, architectural modifications, or training interventions) to test whether changing \(P\) changes test performance. Without such evidence, the paper does not demonstrate that "noise isolation" is a mechanism rather than a epiphenomenon. The paper's own language ("correlation," "weak predictor") tacitly acknowledges this, but the framing (e.g., "could serve to elucidate the internal mechanism" in the contributions list) overclaims. (Sec. 4, lines 115–118, 146–147; Abstract, line 4)

### Minor

- **The k-NN methodology is incompletely specified and not validated for sensitivity.** The paper does not state the value of \(k\) used in the k-NN analysis (the "\(k\)" in Eq. 1). No sensitivity analysis is performed with respect to \(k\), different distance metrics are not tested, and no comparison against random baselines or alternative diagnostics (e.g., spectral properties, margin distributions) is provided. As model width increases, the dimensionality of the penultimate layer grows, and distance metrics in high dimensions can behave pathologically — this confound is not discussed. The authors explicitly state that "the k-NN method functions solely as an estimation technique" (line 78), but the conclusions drawn from \(P\) depend on the robustness of this estimation, which is not demonstrated. (Sec. 3.3, Eq. 1)

- **The "perfect learner / imperfect learner" framework in the conclusion is speculative and untested.** The paper claims that double descent "should not be observable in perfect learners where perfect regularization should eliminate the effect" and attributes double descent to "imperfect learners with sub-optimal regularization." No experiment with explicit regularization (weight decay, early stopping, or any method that could approximate a "perfect regularizer") is performed to test this claim. The framework is presented as an intuitive narrative rather than a conclusion drawn from the experiments. The authors acknowledge this ("a comprehensive theoretical framework is yet to be developed," line 196), but the framing in the Conclusion (Fig. 4, lines 190–194) reads as a stronger claim than the evidence supports. (Conclusion, Fig. 4)

### Trivial

- The paper uses the variable \(k\) both for model width (FCNN hidden units) and for the number of nearest neighbors in k-NN, which is confusing. For example, in the FCNN setup, "\(k=15\)" refers to width (line 109), while elsewhere \(k\) refers to the k-NN parameter.
- Several figure captions contain garbled text (e.g., line 99: "`   \fontsize{8}{8}\selectfont") — these appear to be parser artifacts.

## Nice-to-Haves

- **Causal intervention:** An experiment that perturbs the feature space (e.g., by re-training with a frozen feature extractor learned at one width and varying only the classifier) could test whether changing \(P\) changes test performance, moving beyond correlation.
- **Explicit regularization ablation:** Training models with weight decay or early stopping would test whether the proposed "perfect learner" narrative has empirical grounding.
- **Visualization of the feature space:** t-SNE or UMAP plots of the penultimate-layer representations at selected widths (before, at, and after the interpolation threshold) would visually illustrate whether "isolation" occurs in the geometric sense the paper invokes.
- **Comparison to alternative measures:** Computing other known double-descent diagnostics (e.g., sharpness from Gamba et al. 2022, decision boundary fragmentation from Somepalli et al. 2022) and showing that \(P\) adds predictive power beyond them would strengthen the claim of novelty.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Strength: "Conceptual framework unifies observed behaviors under 'imperfect learners'"** — This strength (from the Strength Finder) conflicts with a verified weakness: the framework is speculative and untested. Per the consolidation rules, when a strength and weakness disagree, the weakness wins. The framework is discussed in the paper but is not experimentally grounded. Moved here for completeness.

## Novel Insights

The ResNet18 result is arguably the paper's most interesting finding, but the paper treats it as a contradiction rather than a discovery. That different architectures can exhibit the same double descent curve through *different* representation-level behaviors (noise "isolation" for CNN vs. noise "memorization" for ResNet18) suggests that double descent may be a robust phenomenon with multiple, architecture-dependent mechanisms, rather than a single unified one. The paper does not develop this insight — it frames it as a problem to be explained away — but the data itself hints at a richer picture than the paper's title suggests.

## Suggestions

1. **Re-scope the central claim.** The paper would be more defensible if it claimed that *for some architectures* (FCNN, CNN) the k-NN measure \(P\) correlates with test accuracy and is consistent with a noise-isolation story, rather than claiming a general mechanism for double descent. Acknowledging that different architectures may admit different explanations would make the contribution accurate rather than overreaching.

2. **Resolve or explain the ResNet18 discrepancy.** At minimum, analyze why the behavior differs: compare effective dimensionality of the feature space, clustering metrics (e.g., silhouette score), or nearest-neighbor distances across architectures. If the mechanism is truly architecture-dependent, that is itself a publishable finding.

3. **Specify and validate the k-NN parameter \(k\) and distance metric.** Report the value of \(k\) used, show sensitivity to \(k\), and test at least one alternative distance metric (e.g., Euclidean distance) to confirm the trends are robust.

4. **Tone down the causal language.** Replace "elucidate the internal mechanism" and similar phrasing with "correlates with" or "is consistent with" unless causal evidence is provided.

## Score and Decision

This paper makes an honest empirical contribution — the k-NN analysis is a clean idea, the experiments are thorough, and the contradictory ResNet result is openly reported — but the central claim is undermined by the paper's own data. The proposed mechanism (noise isolation driving the second descent) does not hold for ResNet18, which exhibits double descent as clearly as the other architectures. Together with the purely correlational evidence and the untested conceptual framework, the paper's contribution is better described as an interesting *observation* than a validated *explanation* of double descent. The paper could be strengthened substantially by re-scoping its claims and addressing the ResNet discrepancy, but in its current form the gap between claim and evidence is too large.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>