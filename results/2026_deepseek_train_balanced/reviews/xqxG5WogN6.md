Now I have all the information needed to synthesize the final review.

---

## Summary

This paper proposes DART, a test-time adaptation method designed to handle the underexplored problem of *combined* covariate and label distribution shifts. DART trains a lightweight MLP prediction refinement module during an "intermediate time" (between training and testing) on training batches with diverse class distributions sampled via a Dirichlet distribution. At test time, the module takes the averaged pseudo-label distribution and a proposed *prediction deviation* metric as inputs and outputs an affine transformation (matrix $W$ and bias $b$) that reverses class-wise confusion patterns caused by label shifts. The method shows sizable gains (5–18% on CIFAR-10C-LT) and can be plugged into 8 existing TTA methods without degrading performance when no label shift exists.

## Strengths

1. **Well-documented diagnosis of BNAdapt failure under label shifts.** The paper provides both a toy Gaussian-mixture analysis (Sec 2, lines 106–120) and empirical confusion-matrix evidence (Fig 1) showing that BN-adapted classifiers suffer systematic, corruption-invariant class-wise confusion patterns that intensify with imbalance ratio. This clearly establishes the problem the method solves.

2. **Prediction deviation metric resolves a detection failure of existing metrics.** The paper identifies (lines 159–160, Fig 2) that the averaged pseudo-label distribution $D(u,\bar{p}_\mathcal{B})$ becomes *indistinguishable from uniform* under severe label shifts (IR > 50) even as accuracy continues to drop. The proposed prediction deviation $d_\mathcal{B}$ monotonically decreases with IR, enabling detection where prior approaches fail. This is a concrete, evidenced improvement over the default approach used by ODS, DELTA, and LSA.

3. **Large gains without degradation on balanced data.** DART improves BNAdapt by 5.7% and 18.1% on CIFAR-10C-LT at $\rho=10,100$ while maintaining nearly identical accuracy ($85.2\pm0.1$ vs $85.2\pm0.0$) when $\rho=1$ (Table 4). This "no-harm" property is critical for a plug-in method and is explicitly validated.

4. **Dirichlet sampling ablation cleanly isolates the key design choice.** Table 4 shows that replacing Dirichlet sampling with uniform + long-tailed ($\rho=20$) distributions collapses performance on CIFAR-10C-imb at IR5000 (28.7% vs 82.4% for full DART) while actually *improving* on the simpler CIFAR-10C-LT. This cleanly separates the value of diverse-distribution exposure from simpler alternatives.

5. **Consistent plug-in improvements across 8 TTA baselines.** DART improves accuracy when combined with BNAdapt, TENT, PL, NOTE, DELTA, ODS, LAME, and SAR on CIFAR-10C-LT, PACS, and OfficeHome (Table 1), demonstrating that the refinement mechanism generalizes beyond any single adaptation strategy.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Scalability concern requiring DART-split is under-discussed.** The original DART outputs a $K\times K$ matrix, which for 1000-class ImageNet amounts to 1M parameters — already a non-trivial output for a 2-layer MLP with 1000 hidden units. The paper introduces DART-split (lines 323–326), which fundamentally splits the module into a detector ($g_{\phi_1}$) and a refiner ($g_{\phi_2}$) with a hard decision threshold (0.5). This is a significant architectural change motivated by scalability, yet it is presented as a straightforward variant. The improvements on ImageNet-C-imb (0.2–4.8%) are also notably more modest than on CIFAR. The paper should more prominently discuss this scalability limitation.

2. **No explicit limitations section or discussion of key assumptions.** The method relies on several assumptions that are not scrutinized: (a) confusion patterns learned on *clean* training data with *simulated* label shifts transfer to *corrupted* test data with *real* label shifts; (b) Dirichlet sampling during training adequately covers the space of possible test-time shifts; (c) the two-stage design ($g_\phi$ inputs from $f_{\bar{\theta}_0}$ while modifying $f_\theta$'s predictions, lines 236–240) is stable even when $f_\theta$ drifts during test-time adaptation. These are plausible assumptions and the main results indirectly validate them, but explicitly discussing failure modes would strengthen the paper.

3. **"Theoretical analysis" framing is overstated.** Line 104 states the paper "theoretically and experimentally analyze[s]" the impact of label shifts, but the toy example (lines 106–120) presents three observations derived from a specific Gaussian-mixture setup without formal proof. The analysis is a useful illustration, not a theoretical derivation. The framing is a minor overstatement.

4. **Hyperparameter $\alpha$ (set to 0.1) is not ablated.** The regularization weight $\alpha$ in Eq 3 controls the trade-off between correction capability on imbalanced batches and identity preservation on balanced batches. Its value is stated as a default (line 232) without any sensitivity analysis. Since this parameter directly influences the "no-harm" property, its robustness should be demonstrated even briefly.

### Trivial
None.

## Nice-to-Haves

- Ablation of the DART-split gating threshold (0.5) to assess robustness near the decision boundary.
- A focused experiment isolating the clean-to-corrupted transfer: train $g_\phi$ on clean training data with simulated label shifts, then evaluate the affine corrections it produces on *held-out clean data* with label shifts before introducing corruption.
- Ablation of the regularization weight $\alpha$ to confirm the default value is not brittle.

## Removed Points

These points were raised by reviewers but removed after cross-checking against the paper:

1. **"Asymmetric evaluation — DART has privileged access to training labels that baselines do not."** Removed. DART's intermediate-time training follows the same paradigm as prior work (LSA Park et al., SWR Choi et al., TTN Lim et al., all cited at line 210). Comparing against baselines without this training phase is standard; the proposed method includes intermediate training as part of its design. This is a legitimate comparison.

2. **"Central generalization assumption (clean-to-corrupted transfer) is not tested."** Removed. The full evaluation on corrupted benchmarks (CIFAR-10C, CIFAR-100C, ImageNet-C) *is* the test of this generalization. The requested controlled experiment would be a nice-to-have addition, but the main results already validate the transfer across 15+ corruption types.

3. **"Reported standard deviations are implausibly tight."** Removed. CIFAR-10 evaluations with fixed architectures and deterministic components typically produce stable results. Values of 0.0–0.7% are standard for this setting and consistent with prior work.

4. **"DART-split is a fundamentally different approach."** Removed. DART-split decomposes the original module into detection + refinement — a natural modularization for large class counts, not a fundamentally different method.

## Novel Insights

The reviews corroborate the paper's key claims but do not surface any genuinely new perspective beyond the paper's own contributions. The most important observation from the reviews is that DART's two-stage design (using $f_{\bar{\theta}_0}$ for inputs but modifying $f_\theta$'s predictions) creates a potential train-test mismatch that the paper does not analyze — this is a concrete avenue for future work but is already partially addressed (lines 236–240 explain the design rationale).

## Suggestions

1. Add a Limitations section explicitly discussing: (a) the scalability issue motivating DART-split, (b) the assumption that training-data Dirichlet-sampled shifts cover test-time shifts, (c) the two-stage input design and potential drift between $f_{\bar{\theta}_0}$ and $f_\theta$ during online adaptation.
2. Add an ablation study of $\alpha$ and the DART-split gating threshold.
3. Reframe the toy example analysis as "illustrative analysis" rather than "theoretical investigation."

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>