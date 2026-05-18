Now I have a thorough understanding of both the paper and the calibration anchors. Let me write the final consolidated review.

---

## Summary

This paper identifies a "model collapse" phenomenon in Deep Canonical Correlation Analysis (DCCA), where downstream task performance degrades with prolonged training despite DCCA's strong early performance. The authors hypothesize that the collapse stems from weight matrices in DNNs becoming low-rank, and propose NR-DCCA, which adds a noise regularization loss that enforces a Correlation Invariant Property (CIP) — the correlation between data and random noise should be preserved after transformation. Theorem 1 proves that, for a square linear transformation, CIP is equivalent to the weight matrix being full-rank. Experiments on synthetic data (with a novel controllable common-rate framework) and three real-world datasets show NR-DCCA avoids the performance degradation seen in DCCA and its variants.

## Strengths

- **Identification of a genuine practical problem**: The paper documents a clear and reproducible phenomenon — DCCA-based methods exhibit severe downstream performance degradation with extended training (Figure 2a). This is a noteworthy observation that had not been systematically studied in the DCCA literature, and documenting it across both synthetic and real-world settings is valuable.

- **Theorem 1 (CIP ↔ full-rank for linear transforms) is rigorous and well-motivated**: The proof that, for a square matrix $W_k$, the correlation with noise is invariant under transformation if and only if $W_k$ is full-rank provides a clean theoretical foundation for the noise regularization idea within the linear setting. This is a non-trivial result based on an MPI-based reformulation of correlation.

- **The synthetic data framework with controllable Common Rate is a useful contribution**: The construction (Figure 2, Definition 1) allows systematic variation of shared information between views via a tunable overlap percentage. This provides a principled testbed for evaluating MVRL methods under controlled conditions, going beyond the typical ad-hoc use of real-world datasets.

- **NR-DCCA empirically prevents the performance degradation**: On synthetic data (Figure 2a), NR-DCCA maintains stable and competitive performance across all common rates and training epochs while DCCA, DCCAE, and DCCA_PRIVATE all degrade. On real-world datasets (Figure 3), NR-DCCA shows competitive and stable performance.

- **Theorem 2 provides a useful diagnostic tool**: The result linking full-rank weight matrices (CIP) to low reconstruction and denoising losses gives operationalizable metrics for evaluating representation quality, and the paper confirms these metrics align with performance in Figure 2(d,e).

## Weaknesses

### Major

- **The theoretical bridge from linear CIP to DNN internals is asserted, not proved**: Theorem 1 establishes CIP ↔ full-rank for a *single square linear transformation*. The paper then applies this to nonlinear multi-layer networks $f_k$ and states that "the NR approach constrains the weight matrices to be full-rank" (line 232). No argument is provided for why enforcing approximate CIP at the *output* of a multi-layer nonlinear network would constrain the *intermediate* weight matrices to be full-rank. The eigenvalue plots (Figure 1) and NESum metrics (Figure 2c) show a correlation between NR training and slower eigenvalue decay, but correlation does not establish that CIP is the causal mechanism. This gap matters because the entire theoretical motivation — that NR-DCCA works by keeping weight matrices full-rank via CIP — rests on this extension from linear to deep models.

- **Missing regularization baselines prevent attribution of the effect**: The paper compares NR-DCCA against unregularized DCCA variants (DCCA, DCCAE, DCCA_PRIVATE, DGCCA) and Linear CCA, but includes no comparison against DCCA with standard regularizers such as weight decay, dropout, or spectral normalization. Any form of regularization could plausibly stabilize training and prevent the observed performance drop. Without these baselines, it is impossible to determine whether the benefits come specifically from the CIP/full-rank mechanism or simply from the presence of *some* regularizing pressure on the network. The authors acknowledge this gap in the conclusion ("It is also interesting to further investigate the difference between our developed NR and other neural network regularization approaches") but the absence of these baselines weakens the central claim that NR uniquely addresses a low-rank weight problem.

### Minor

- **The definition of "model collapse" is purely downstream-performance-based**: The paper defines collapse as a drop in $R^2$ / F1 scores with continued training (Section 4). While the paper is explicit about this definition, it does not report how the actual CCA correlation objective evolves during training. If the CCA correlation continues to increase while downstream metrics drop, the phenomenon would be ordinary overfitting rather than a degenerative collapse of the representation — a distinction that matters for interpreting both the problem and the solution. The supporting metrics in Figure 2(b-e) are helpful but do not substitute for showing the training objective itself.

- **The causal evidence for the low-rank hypothesis is correlational**: The eigenvalue analysis (Figure 1) and NESum metrics (Figure 2c) show that eigenvalue decay coincides with performance degradation and that NR-DCCA maintains slower decay. However, no experiment manipulates rank directly (e.g., enforcing a low-rank bottleneck and observing whether collapse is induced, or showing that other full-rank-preserving regularizers also prevent collapse). The paper would be stronger with a causal manipulation rather than observational evidence alone.

### Trivial

- Figure references in the supplementary analysis (Section 6) are somewhat tangled: the text references panels (b), (c), (d) of Figure 2 in an order that doesn't match the visual layout, which can confuse readers trying to follow the argument through the metrics.

## Nice-to-Haves

- Tracking singular value spectra at multiple network depths (not just the first linear layer) would show whether the rank-preserving effect is global or localized.
- Evaluating NR on DGCCA (or other DCCA variants) in the experiments would substantiate the claim that the approach generalizes as a "pluggable module."
- Reporting the CCA correlation objective on training and test sets alongside downstream metrics would help readers distinguish between representation collapse and standard overfitting.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **HC claimed "the paper's central contribution does not hold" due to the linear-to-DNN theory gap.** While the theory gap is real and kept as a Major weakness, the claim that this *invalidates* the entire contribution overstates the case. The empirical results still demonstrate that NR-DCCA prevents performance degradation, and the synthetic data framework is independently valuable. Downgraded from fatal to major.

2. **SF Strength about generalization to DGCCA ("The method generalizes to other DCCA variants and real-world settings")**: The paper *states* that NR can be applied to DGCCA but provides no experimental evidence for this claim. This strength is aspirational, not demonstrated. Removed.

3. **SF made several references to "Figure 4a" which does not exist in the paper**: The strength finder hallucinated figure numbers. The actual figures are 1, 2, and 3. The underlying content claims are valid and have been retained with corrected references.

## Novel Insights

The paper's observation that nonlinear activation functions (like ReLU) can map a low-rank pre-activation to a full-rank output — meaning that the CCA objective's constraint on output representations being full-rank does *not* propagate backward to constrain weight matrices — is a genuinely insightful point (Section 4). This explains a structural asymmetry between Linear CCA and DCCA that had not been articulated before, and it provides a plausible mechanistic hypothesis for why DCCA is vulnerable to a failure mode that Linear CCA avoids.

## Suggestions

- The most impactful single experiment would be to train DCCA with an explicit low-rank bottleneck on weight matrices and show that this *induces* collapse even early in training, while NR-DCCA resists it. This would move the evidence from correlational to causal.
- Adding DCCA + weight decay and DCCA + dropout as baselines would clearly show whether NR provides benefits beyond generic regularization. If NR-DCCA still outperforms these, the CIP mechanism becomes much more credible.
- Reframing the CIP extension to DNNs as a *regularization heuristic motivated by* Theorem 1 (rather than a theoretically guaranteed mechanism) would align the claims more honestly with what is actually proved. This would not weaken the contribution — the method still works — but would avoid overclaiming.

## Score and Decision

**Anchor comparison:**

- **COPER** (`5ZEbpBYGwH`, avg 7.25): Stronger overall — novel CCA-based method with theory connecting to LDA, extensive experiments across 10 benchmarks. The paper under review has a weaker theoretical bridge and missing baselines.
- **Lambda-Skip Connections** (`1yJP5TVWih`, avg 6.25): Similar theme (preventing rank collapse) but offers rigorous theoretical guarantees for the actual architectures studied. This paper's theory is limited to the linear case. The paper under review is weaker.
- **Mind the Gap** (`X6xzYP2cMk`, avg 4.75): Also identifies a rank collapse phenomenon with theory limited to simplified settings. This paper has more practical validation (real datasets, actual training dynamics) than Mind the Gap but comparable theoretical limitations. The paper under review is roughly comparable to slightly better.
- **Simultaneous Dimensionality Reduction** (`4SrzKsJocx`, avg 3.80): Synthetic-only, linear-only, weak novelty. The paper under review is clearly stronger.
- **SpecRaGE** (`SNNdmfqWFu`, avg 3.40): Incremental contribution, weak novelty. The paper under review is clearly stronger.

The paper under review sits between the 4.75 and 6.25 anchors. It has real contributions (problem identification, NR-DCCA method, synthetic data framework, Theorem 1) but is held back by the theory-to-practice gap and missing baselines. The empirical results are consistent and promising but the central mechanistic claim is not firmly established.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>