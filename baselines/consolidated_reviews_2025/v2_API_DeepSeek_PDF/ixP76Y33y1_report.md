## Summary
# Final Review Report

## Summary

This paper investigates why neural networks generalize differently across natural and medical imaging domains, focusing on the role of intrinsic dataset properties. The authors propose a new metric — intrinsic label sharpness (KF), defined as the Lipschitz constant of the ground-truth labeling function — and incorporate it into a generalization scaling law with respect to dataset intrinsic dimension (ddata). The paper also establishes connections between KF and adversarial robustness (higher KF → lower robustness), and shows that dataset intrinsic dimension bounds the intrinsic dimension of learned representations (drepr ≲ ddata). Experiments span six CNN architectures and eleven datasets across both domains.

**Overall assessment**: The paper addresses a genuine and interesting question — why neural network behavior differs between imaging domains — and offers a systematic theoretical-empirical framework. The proposed KF metric is intuitive and computationally efficient. The experimental scope (6 models × 11 datasets × 6 training sizes) is substantial. However, several weaknesses reduce confidence in the core claims: the theoretical derivation of the central scaling law (Theorem 1) is inherited from prior work (Bahri et al., 2021), the key convergence result (Theorem 2) lacks empirical verification, the causal attribution of the domain gap to KF remains correlational, and some mathematical derivations (particularly Theorem 5) rely on heuristic bound-equating arguments. The paper is well-written and the limitations are honestly acknowledged, but the novelty increment over prior work (Pope et al., 2020; Bahri et al., 2021; Konz et al., 2022) is moderate. With targeted revisions to tighten claims and add empirical support for Theorem 2, the paper could achieve higher impact.

## Strengths
1. **Well-motivated research question**: The paper asks a timely and practically important question — why neural network behavior differs between natural and medical imaging domains. This is relevant to the growing deployment of deep learning in medical imaging and the common practice of transferring techniques from computer vision to medical applications.

2. **Comprehensive experimental scope**: The study evaluates six CNN architectures (ResNet-18/34/50, VGG-13/16/19) across seven medical and four natural image datasets, with six different training set sizes (N=500 to 1750). This breadth provides reasonable empirical grounding for the scaling law analysis.

3. **Novel measurable concept**: The proposed label sharpness (KF) is a conceptually clean and computationally efficient metric (computable in <1 second with M=1000 samples). It captures an intuitive notion — how visually similar images from different classes can be — that differs systematically between domains (Fig. 1).

4. **Honest limitation disclosure**: The limitation paragraph (Page 9) candidly acknowledges the causal ambiguity between KF and the observed generalization gap. This scientific honesty is commendable and should be retained.

5. **Multi-layer theoretical structure**: The paper attempts to connect three levels — dataset properties (ddata, KF), representation properties (drepr), and model behavior (generalization, robustness). This multi-layer theoretical framework, while imperfect, provides a coherent narrative that could inspire further work.

6. **Practical relevance**: The adversarial robustness finding (Section 6) has concrete implications for medical imaging deployment, where subtle adversarial perturbations could cause misdiagnosis. The paper correctly identifies that medical-image models are more vulnerable, and connects this vulnerability to a measurable dataset property.

## Weaknesses
1. **Limited novelty increment over prior work**: The core scaling law (Theorem 1) is directly from Bahri et al. (2021). The main theoretical novelty — Theorem 2 (Kf → KF) — is deferred to the appendix without a proof sketch, and lacks empirical verification. The paper would benefit from a clearer demarcation of what is inherited versus newly contributed.

2. **Causal attribution gap**: The central claim that higher KF "explains" the generalization scaling discrepancy between natural and medical images is supported only by correlational evidence. The paper correctly acknowledges this in the limitations, but the main text (Section 5.2) uses language that may overstate the causal link (e.g., "results in" stronger generalization scaling). Without controlled experiments manipulating KF independently of other factors, the claim remains a hypothesis.

3. **Theorem 5 derivation is mathematically heuristic**: The argument for drepr ≲ ddata equates two asymptotic O-bounds to derive a relationship between exponents. This is not mathematically rigorous — O-notation absorbs constants and the two bounds have different Lipschitz terms (max(Kf, KF) vs. no such term). The empirical evidence in Figure 5 supports the conclusion, but the theorem as stated overstates the theoretical foundation.

4. **Theorem 3 applies to on-manifold robustness, not off-manifold attacks**: The robustness radius bound uses Lipschitz assumptions on the data manifold, but FGSM attacks produce off-manifold perturbations. This mismatch between theory and experiment is not acknowledged.

5. **KF estimator is sensitive to worst-case pairs**: The max-based estimator (Eq. 1) can be dominated by outlier pairs with near-zero denominator (very similar images with different labels), potentially inflating ˆKF. A percentile-based alternative would be more robust.

6. **Training details are underspecified for reproducibility**: The description "trained with Adam until the model fully fits" (Page 4) lacks hyperparameters (learning rate, batch size) and a precise convergence criterion in the main text. These are deferred to the appendix, which reduces readability and reproducibility confidence.

7. **Introduction narrative could be stronger**: The current introduction does not articulate why interpreting the domain gap through KF is a fundamentally new insight versus an incremental extension. The explicit gap statement ("no existing theoretical explanation") appears implicitly rather than as a standalone motivator.

8. **Related work is a citation list rather than structured comparison**: Section 2 reads as a chronological bibliography without clear organizing axes or explicit statements of how this paper differs from each prior line of work.

## Key Issues
### Issue 1 (Major): Unverified Theorem 2 — Kf convergence to KF
The entire scaling-law simplification L ≃ O(KL KF N^{-1/ddata}) depends on Theorem 2 (Kf → KF). This theorem is essential but: (a) the proof is fully in the appendix, (b) no proof sketch is provided in the main text, (c) no empirical estimate of Kf is reported to verify the claim. Without showing Kf ≈ KF for at least one representative model-dataset pair, readers cannot assess whether this holds under practical conditions. **Severity: Major — affects the validity of the main scaling law claim.**

### Issue 2 (Major): Theorem 5 — Invalid equating of O-bounds
Theorem 5 derives drepr ≲ ddata by equating L = O(KL max(Kf, KF) N^{-1/ddata}) and L ≃ O(KL N^{-1/drepr}). This is not mathematically rigorous: O-bounds are inequalities, not equalities, and the two bounds have structurally different Lipschitz terms. The empirical evidence (Fig. 5) is consistent with the claim, but the theorem as stated overstates the theoretical foundation. **Severity: Major — needs reformulation as an observation, not a theorem.**

### Issue 3 (Major): Causal overreach in Section 5.2
The paper claims KF "explains" the generalization gap, but no experiment manipulates KF independently. The evidence is exclusively correlational. While the limitation paragraph addresses this, the main-text narrative in Section 5.2 uses language implying causation ("results in," "is explained by") that goes beyond what the evidence supports. **Severity: Major — requires rewording throughout Section 5.2 and clearer separation of correlation vs. causation.**

### Issue 4 (Major): Reproducibility gaps in training protocol
The training description is underspecified: "until the model fully fits" leaves the convergence criterion ambiguous. Learning rate, batch size, weight decay, and stopping tolerance are not reported in the main text. The paper also does not clarify whether multi-seed experiments were run for all datasets or only natural-image ones. **Severity: Major — undermines reproducibility confidence.**

### Issue 5 (Major): KF estimator sensitivity to outliers
The max-based estimator (Eq. 1) is sensitive to near-duplicate image pairs with different labels, which could produce arbitrarily large ˆKF values. The paper should report sensitivity analysis using percentile-based alternatives. **Severity: Major — affects the reliability of the central empirical quantity.**

### Issue 6 (Moderate): Theorem 3 — on-manifold vs. off-manifold mismatch
The robustness bound (Ω(1/KF)) relies on Lipschitz assumptions on Mddata, but FGSM attacks produce off-manifold perturbations. The empirical correlation in Table 1 is useful, but the theoretical justification does not fully cover the experimental setting. **Severity: Moderate — needs explicit qualification.**

### Issue 7 (Moderate): Related work lacks structured positioning
Section 2 reads as a list of references rather than an organized comparison across axes. The paper's contributions relative to Bahri et al. (2021), Pope et al. (2020), and Ansuini et al. (2019) are not clearly delineated. **Severity: Moderate — weakens novelty communication.**

### Issue 8 (Minor): Conclusion dilutes validated findings with speculative extensions
The first conclusion paragraph spends excessive space on future work (satellite imaging, histopathology, transformers, NLP) rather than consolidating validated contributions. **Severity: Minor — structural improvement.**

## Actionable Suggestions
### S1: Add empirical verification of Theorem 2 (Kf → KF) [Must]
Estimate the Lipschitz constant of trained models (Kf) for at least 2 architectures × 4 datasets using techniques from Fazlyab et al. (2019). Show that Kf approaches KF as N increases across 500→1750 training samples. This single addition would substantially strengthen the paper's central claim. If the convergence is not observed, revise the claim to reflect the empirical finding.

### S2: Reformulate Theorem 5 as an observation [Must]
Replace Theorem 5 with: "Observation. Under the heuristic of equating the dominant N-dependence in Theorems 1 and 4, one expects drepr ≲ ddata. This is supported by empirical evidence (Fig. 5) and aligns with the information bottleneck principle (Tishby & Zaslavsky, 2015)." The empirical evidence is sufficient to support the claim; the mathematical formalism needs adjustment.

### S3: Reword causal language in Section 5.2 [Must]
Replace all instances of "results in," "causes," and "explained by" with correlation-consistent phrasing such as "is associated with," "is consistent with," and "is partially attributed to" (the latter is already used appropriately in some places). This is a low-effort, high-impact revision that will significantly improve the paper's scientific defensibility.

### S4: Add training hyperparameters to main text [Must]
Include learning rate (1e-4), batch size (32), optimizer parameters, and precise convergence criterion (e.g., "training accuracy reached 100% or BCE loss < 0.01, whichever occurred first") in Section 4 rather than deferring to Appendix F. Clarify whether multi-seed experiments were conducted for all datasets.

### S5: Add robustness analysis for KF estimator [Nice-to-have]
Replace the max-based estimator (Eq. 1) with a percentile-based version (e.g., 95th or 99th percentile), and report both versions for key results (Fig. 2, Fig. 3). This would demonstrate that the main findings are not driven by outlier pairs. Computational cost is negligible.

### S6: Add structured related work comparison [Nice-to-have]
Reorganize Section 2 around 3 comparison axes: (1) generalization scaling laws — how this paper extends Bahri et al. (2021) by estimating KF, (2) representation intrinsic dimension — how this paper's theoretical scaling law differs from Ansuini et al. (2019)'s empirical observations, (3) adversarial robustness — how Theorem 3 formalizes Ma et al. (2021)'s observations. This clarifies novelty positioning.

### S7: Qualify Theorem 3 for off-manifold attacks [Nice-to-have]
Add a sentence after Theorem 3: "This bound applies to on-manifold perturbations; off-manifold adversarial examples (as used in our FGSM experiments) may be governed by additional factors beyond KF."

### S8: Restructure conclusion [Nice-to-have]
Move the future-work sentences (satellite imaging, histopathology, transformers, NLP) to a separate "Future Directions" paragraph. The first conclusion paragraph should foreground validated contributions.

## Storyline Options + Writing Outlines
### Current Storyline Analysis

The current narrative arc is: (P1) scaling laws with ddata exist but differ between domains → (P2) this paper studies how intrinsic dataset properties affect network behavior → contribution list. The gap is identified but the specific role of label sharpness is introduced only as one of several contributions rather than as the central explanatory mechanism.

**Alignment check**: Problem alignment is acceptable (ddata scaling differs → KF explains difference). Variable alignment is strong (ddata and KF used throughout). Contribution-evidence alignment is moderate (scaling law evidence is strong, causal attribution is correlational).

### Recommended Storyline: "One Dataset Property, Two Consequences"

This storyline frames label sharpness (KF) as the central character: (1) KF differs between domains → (2) KF explains generalization scaling differences → (3) KF explains robustness differences → (4) KF relates to representation complexity.

### Abstract Outline (complete)

- **S1 (Problem + Domain)**: "This paper investigates why neural networks generalize differently across imaging domains — a factor often overlooked when transferring computer vision to medical imaging."
- **S2 (Prior gap)**: "Prior work shows generalization error increases with dataset intrinsic dimension (ddata), but the steepness varies drastically between domains without theoretical explanation."
- **S3 (Proposed concept + method)**: "We introduce label sharpness (KF) — a Lipschitz-based measure of how visually similar same-labeled images can be — and derive a generalization scaling law L ∝ KF·N^{-1/ddata} incorporating it."
- **S4 (Key empirical result)**: "Experiments on 6 architectures × 11 datasets show that higher KF in medical datasets partially explains their steeper generalization scaling and higher adversarial vulnerability."
- **S5 (Auxiliary finding)**: "We also show ddata bounds the intrinsic dimension of learned representations (drepr), linking data complexity to representation complexity."

### Introduction Outline (complete)

- **P1 (Territory + Gap)**: Current scaling laws with ddata exist but previously unexplained domain gap. "No existing theory explains why medical images show steeper scaling." [Revise from current version: make the gap sentence explicit and standalone.]
- **P2 (Bridge to solution)**: Introduce KF as a measurable dataset property. Explain intuitively: KF measures how similar images can be with different labels. Preview that KF differs between domains (Fig. 1) and appears in the scaling law.
- **P3 (Contribution overview)**: List C1-C3 with a unified framing sentence: "Together, these findings show that a single dataset property — label sharpness — has measurable consequences for both generalization and robustness across imaging domains."
- **P4 (Roadmap)**: "Section 2 reviews related work. Section 3 defines KF and ddata estimators. Section 4 describes the experimental setup. Section 5 presents the scaling law and domain comparison. Section 6 connects KF to adversarial robustness. Section 7 extends to representation intrinsic dimension. Section 8 concludes."

### Alternative Storyline 2: "Theoretical- Empirical Bridge"

Frame the paper as bridging Bahri et al. (2021)'s theory with empirical observations from Konz et al. (2022), using KF as the bridge. Stronger for a theory-focused venue. Risk: makes the novelty increment over prior work more apparent.

### Alternative Storyline 3: "Dataset-Centric View of Model Behavior"

Frame all three findings (generalization, robustness, representation) as consequences of dataset-intrinsic properties rather than model architecture. Stronger for emphasizing the practical implication that dataset analysis should precede model selection. Recommended for revision.

## Priority Revision Plan
### P0 (Must — before resubmission)

| # | Issue | Action | Effort | Impact |
|---|-------|--------|--------|--------|
| 1 | Theorem 2 unverified | Add empirical Kf estimation for 2×4 model-dataset pairs | 2-3 days | High — validates main scaling law |
| 2 | Causal overreach in Section 5.2 | Replace causal language with correlational wording | 0.5 day | High — improves defensibility |
| 3 | Theorem 5 rigor | Reformulate as observation, keep empirical evidence | 0.5 day | High — fixes mathematical overclaim |
| 4 | Training details underspecified | Add hyperparameters + convergence criterion to Section 4 | 0.5 day | High — improves reproducibility |

### P1 (Nice-to-have — strengthens paper)

| # | Issue | Action | Effort | Impact |
|---|-------|--------|--------|--------|
| 5 | KF estimator sensitivity | Add percentile-based analysis (95th/99th) | 1 day | Medium — strengthens central metric |
| 6 | Theorem 3 qualification | Add on-manifold vs off-manifold note | 0.5 day | Medium — clarifies theory-experiment link |

### P2 (Quality improvement)

| # | Issue | Action | Effort | Impact |
|---|-------|--------|--------|--------|
| 7 | Related work structure | Reorganize as 3-axis comparison | 1-2 days | Medium — improves positioning |
| 8 | Conclusion restructuring | Move future work to separate paragraph | 0.5 day | Low — readability improvement |

### Revision Sequence

```
Step 1 (P0 items, ~3-4 days):
  Day 1:   Theorem 2 empirical verification (run experiments)
  Day 1-2: Analyze Kf estimation results
  Day 2:   Rewrite causal language in Section 5.2
  Day 2:   Reformulate Theorem 5 as observation
  Day 3:   Add training details to Section 4

Step 2 (P1 items, ~2 days):
  Day 3-4: KF percentile sensitivity analysis
  Day 4:   Theorem 3 qualification

Step 3 (P2 items, ~2 days):
  Day 4-5: Reorganize Related Work
  Day 5:   Restructure Conclusion

Total estimated effort: 7-10 working days
Expected quality improvement: From borderline accept to solid accept at ICLR-level venue
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|-----------|-------|---------|-------------|----------------|-------------------|
| E1 | Measure ddata of 11 datasets | 7 medical + 4 natural, MLE/TwoNN estimators | ddata (intrinsic dimension) | Medical and natural datasets have overlapping ddata ranges | C1 (partially) | Single estimator hyperparameter (k=20) |
| E2 | Measure KF of 11 datasets | Same datasets, M=1000 samples, Eq. (1) | ˆKF (label sharpness) | Medical datasets have higher ˆKF (Fig. 1) | C1 | Max-based estimator; outlier sensitivity not assessed |
| E3 | Generalization vs ddata scaling | 6 models, 11 datasets, N=500-1750 | Test loss, test accuracy | log L ∝ -1/ddata within domains; medical steeper (Fig. 2) | C1, C2 | Correlational; no causal control of KF |
| E4 | Adversarial robustness vs KF | Same models/datasets, FGSM ϵ=1-8/255 | Loss penalty, accuracy penalty | Positive r between loss penalty and KF (Table 1, Fig. 3) | C2 | FGSM only; no PGD, no adaptive attacks |
| E5 | Measure drepr and scaling | Same models/datasets, TwoNN on final hidden layer | drepr, test loss | L increases with drepr (Fig. 4) | C3 | Estimator choice (TwoNN vs MLE) affects values |
| E6 | drepr vs ddata comparison | Same models/datasets | drepr, ddata | drepr ≲ ddata (Fig. 5) | C3 (observation) | O-bound equating is heuristic |

### Research-Theme Gap Diagnosis

- **New Knowledge (weakest)**: The core innovation — estimating KF and using it to explain domain-specific generalization — is intuitive but lacks causal validation. The novelty increment over Bahri et al. (2021) is moderate, as Theorem 1 is inherited.
- **Reproducibility (moderate)**: Code is provided, but training hyperparameters are not specified in the main text, and Theorem 2's key convergence claim is not empirically verified.
- **Impact on Practice (stronger)**: The finding that medical-image models are more vulnerable to adversarial attacks, connected to a measurable dataset property, has practical utility.

### Proposed Research Experiments

#### P0-Exp1: Empirical verification of Kf → KF (Theorem 2)
- **Target Claim**: Kf (model Lipschitz constant) converges to KF as N → ∞.
- **Hypothesis**: For large enough N, Kf ≈ KF within a tolerance.
- **Minimal Design**: Train 2 architectures (ResNet-18, VGG-16) on 4 datasets (2 medical, 2 natural) at N=500, 1000, 1750. Estimate Kf using the method of Fazlyab et al. (2019). Compare Kf to ˆKF.
- **Controls/Baselines**: Use identical training hyperparameters; verify interpolation condition holds.
- **Metrics**: |Kf - ˆKF| / ˆKF, trend with increasing N.
- **Success Criterion**: At N=1750, |Kf - ˆKF| / ˆKF < 0.3 (30% relative error).
- **Estimated Cost**: 2-3 days (6 model-dataset pairs × 3 N values = 18 training runs + Kf estimation).
- **Expected Quality Gain**: Directly validates the main scaling law simplification; major improvement in theoretical credibility.

#### P0-Exp2: KF estimator robustness analysis
- **Target Claim**: The max-based ˆKF reliably captures label sharpness (Eq. 1).
- **Hypothesis**: KF ranking of datasets is stable under percentile-based alternatives.
- **Minimal Design**: Compute ˆKF using 95th, 99th, and 100th percentiles for all 11 datasets. Compute rank correlation between versions.
- **Metrics**: Spearman rank correlation between percentile versions.
- **Success Criterion**: Rank correlation > 0.9 between 99th and 100th percentile versions.
- **Estimated Cost**: <1 day (computational cost is negligible).
- **Expected Quality Gain**: Demonstrates the central metric is not outlier-driven.

#### P1-Exp3: Controlled synthetic dataset for causal KF test
- **Target Claim**: KF causes steeper generalization scaling (Section 5.2).
- **Hypothesis**: Two synthetic datasets with matched ddata but different KF will show different scaling slopes.
- **Minimal Design**: Generate synthetic manifolds where class boundaries are either well-separated (low KF) or close (high KF) by controlling the distance between class-conditional distributions. Compute ddata and KF. Train models and measure generalization scaling.
- **Controls/Baselines**: Match ddata within 10%, match training set sizes, match number of classes.
- **Metrics**: Scaling slope difference between low-KF and high-KF variants.
- **Success Criterion**: Statistically significant difference in scaling slope (p<0.05, two-sided t-test).
- **Estimated Cost**: 3-5 days.
- **Expected Quality Gain**: Transforms the core claim from correlational to causal; strong argument for a key feature of the paper.

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5 / 10**

**Score Rationale**: The paper addresses a genuinely interesting question with substantial experimental scope (6 models × 11 datasets). The KF metric is conceptually clean and practically efficient. The adversarial robustness finding has practical relevance. However, the core theoretical novelty is limited — Theorem 1 is inherited from Bahri et al. (2021), Theorem 2 lacks empirical verification, and Theorem 5 relies on heuristic bound-equating. The causal attribution of the domain gap to KF is correlational, not causal. The reproducibility is hampered by underspecified training details. These weaknesses reduce the research value contribution below what is expected for a top-tier venue.

**Scoring Breakdown**:
- Research Value / Contribution: 6/10 (solid empirical study, moderate theoretical increment)
- Novelty: 5/10 (incremental over Bahri et al. 2021, Pope et al. 2020; KF metric is novel)
- Validity / Soundness: 6/10 (theoretical gaps in Theorem 2 and 5; training underspecification)
- Reproducibility: 6/10 (code provided but hyperparameters and convergence criteria not in main text)
- Clarity / Presentation: 7/10 (well-organized, honest limitations, but intro could be stronger)

**Post-Revision Target: [7.0, 8.0] / 10**

If the P0 revisions are completed (Theorem 2 empirical verification, causal language correction, Theorem 5 reformulation, training detail addition), the score could rise to 7.0-8.0/10. The paper would then present a well-supported empirical framework with a clear theoretical contribution, and would be competitive at a top venue. The key determinant is whether the Kf → KF convergence can be empirically demonstrated.

```text
ASCII Diagram — Paper Structure & Evidence Map

[Problem: Domain gap in generalization scaling]
    → [Prior evidence: Konz et al. 2022 show medical vs natural gap]
    → [No existing theoretical explanation]
    → [Proposed solution: KF (label sharpness)]
        ├── C1: Scaling law with KF (Thm 1-2 + Eq 2)
        │       Evidence: Fig 1 (KF measured), Fig 2 (scaling plot)
        │       Gap: Thm 2 unverified, causal link correlational
        ├── C2: KF ↔ adversarial robustness (Thm 3)
        │       Evidence: Table 1, Fig 3 (correlations)
        │       Gap: On/off-manifold mismatch
        └── C3: ddata bounds drepr (Thm 4-5)
                Evidence: Fig 4, Fig 5 (empirical support)
                Gap: Thm 5 derivation heuristic
    → [Core risk: All claims are correlational without causal control]
```

```text
ASCII Diagram — Revision Strategy Roadmap

[Key Weaknesses] → [P0 Fixes] → [Expected Improvement]
    │
    ├── Thm 2 unverified → Add empirical Kf estimation → Validates scaling law
    ├── Causal overreach → Rephrase to correlational language → Improves defensibility
    ├── Thm 5 heuristic → Reformulate as observation → Fixes mathematical overclaim
    ├── Training underspec → Add hyperparameters to main text → Better reproducibility
    │
    ├── KF estimator sensitivity → Percentile analysis → Robust central metric
    ├── Thm 3 qualification → Add on/off-manifold note → Theory-experiment alignment
    │
    └── Related work structure → 3-axis reorganization → Clearer positioning
```

```text
ASCII Diagram — Related-Work Taxonomy Tree (Layered)

Generalization & Intrinsic Dimension (Root)
├── Branch 1: Scaling Laws
│   ├── Leaf 1.1: Data/model size scaling [Kaplan et al., Hoffmann et al., Caballero et al.]
│   └── Leaf 1.2: Intrinsic dimension scaling [Pope et al., Bahri et al., Konz et al.]
│       └── This paper: extends Bahri et al. by estimating KF empirically
├── Branch 2: Representation Intrinsic Dimension
│   ├── Leaf 2.1: Empirical observation [Ansuini et al., Gong et al.]
│   └── Leaf 2.2: Model-space dimensionality [Birdal et al., Andreeva et al.]
│       └── This paper: provides theoretical scaling law for drepr
└── Branch 3: Adversarial Robustness
    ├── Leaf 3.1: Medical image vulnerability [Ma et al.]
    └── Leaf 3.2: Lipschitz-based robustness [Tsuzuku et al., Zhang et al.]
        └── This paper: connects robustness to dataset KF via Thm 3
```