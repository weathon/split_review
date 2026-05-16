Now I have all the information needed. Here is the synthesized final review.

## Summary
This paper proposes ECP (Entropy-scaled Conformal Prediction) and EACP (Entropy base-Adapted Conformal Prediction), two methods that adjust CP score functions using the base model's prediction entropy on unlabeled test data to handle distribution shifts without test labels. ECP scales scores by an entropy quantile over the test set, and EACP further refines the model via unsupervised test-time adaptation (ETA). Extensive experiments on ImageNet variants, WILDS datasets, and continuous shifts show consistent recovery of target coverage across diverse architectures.

## Strengths
- **Novel integration of entropy scaling and test-time adaptation for label-free CP under distribution shifts**: The paper directly addresses an important gap in the CP literature—handling distribution shifts without test labels—by exploiting the base model's own uncertainty (entropy) on unlabeled data. The core idea (scaling scores by the entropy quantile, then refining via TTA) is simple, well-motivated, and demonstrably effective. Evidence: Table 1 shows EACP₂ achieves coverage 0.91 (ImageNet-V2), 0.80 (ImageNet-R), 0.30 (ImageNet-A) versus SCP's 0.81, 0.50, 0.03.
- **Consistent recovery of target coverage across diverse datasets, architectures, and shift types**: The evaluation covers 6 natural shift datasets, 19 ImageNet-C corruptions at 5 severity levels, and continuous shifts, using ResNet, DenseNet, and Vision Transformers. EACP₂ consistently brings coverage close to the 0.90 target across almost all settings while SCP and ETA alone fail. Evidence: Table 2 (ImageNet-C) shows EACP₂ coverage hugging 0.93 across nearly all corruption types and severities; Figure 4 shows this pattern holds across multiple architectures.
- **Competitive performance with supervised online CP methods on continuous shifts without labels**: On gradual and sudden shifts (ImageNet-C severity 1→5), EACP₂ achieves average coverage 0.88/0.86—close to supervised FACI (0.90/0.90)—with dramatically smaller set sizes (22.4 vs. 101). Evidence: Table 3, gradual and sudden shift columns.
- **Demonstrates that TTA alone is insufficient and that uncertainty scaling is the critical additional component**: The paper shows that ETA (TTA only) often remains far from target coverage (e.g., 0.81 on ImageNet-V2), while ECP alone already improves coverage, and EACP combines both benefits. Evidence: Table 1, ETA vs. ECP vs. EACP columns.
- **Design choices are empirically justified**: The paper provides supporting analyses (entropy vs. softmax correlation in Figure 1, quantile selection in Figure 2, scaling function analysis in Figure 3) that back key hyperparameter choices.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **No measure of variability on any result**: All results are reported as point estimates without error bars, confidence intervals, or information about the number of independent runs. While the calibration set is large and fixed (25,000 points), the TTA updates and test set composition introduce randomness that should be quantified. The reader cannot assess whether the improvements of ECP/EACP over baselines are reliable or artifacts of a single split. Given that the paper draws comparative conclusions throughout, this is a non-trivial omission.
- **The transductive nature of ECP/EACP is not explicitly stated or discussed**: The entropy quantile \(u_{D_{\text{test}}} = q_{1-\alpha}(h_{D_{\text{test}}})\) requires the full test dataset (or a substantial batch) to compute. The paper mentions "we crucially evaluate its uncertainty on the whole distribution-shifted test dataset" (Section 3.1) and "On a batch of new test data" (Section 3.2), but never explicitly states that the method cannot handle streaming single-point-at-a-time scenarios, nor discusses how the quantile is updated during the continuous shift experiments (e.g., sliding window, recomputed from scratch, or accumulated over time). This gap between the claimed setting ("no labels at test time") and the actual data-access requirement undermines reproducibility and practical applicability assessment.
- **The abstract's claim of "nearly match the performance of supervised algorithms" is too strong without qualification**: In the continuous shift experiments (Table 3), while average coverage is indeed close (EACP₂: 0.88 vs. FACI: 0.90), the worst-case local coverage error (LCE₁₂₈) shows a 2–3× gap (EACP₂: 0.20 vs. FACI: 0.07 on gradual shifts). The paper does discuss this trade-off in the text (line 264: "While the supervised methods unsurprisingly result in better local coverage"), but the abstract and high-level claims use "nearly match" without caveats, which could mislead readers.
- **No dedicated limitations section**: The conclusion does not discuss the method's known limitations: the need for batched test data, the lack of any formal coverage guarantee, the failure on extremely hard shifts (ImageNet-A coverage remains at 0.30), and the inability to control local coverage. Including these would strengthen credibility.
- **No ablation on the quantile parameter \(\beta\)**: The paper sets \(\beta = 1-\alpha\) based on Figure 2, but does not show what happens when \(\beta\) is varied. While the justification is reasonable, an ablation would strengthen the claim that this heuristic is robust and not overfitted.

### Trivial
- None worth enumerating independently of the Minor items above.

## Nice-to-Haves
- Quantitative summary for Figure 4 (e.g., mean absolute deviation from 0.90) would be more informative than the qualitative description of "hugging."
- A brief discussion of why a data-driven selection of the scaling function order (e.g., based on a held-out subset) was not pursued would address a natural reader question.
- An explicit statement about whether the same model checkpoint was used across all experiments would clarify reproducibility (though the paper states methodology and hyperparameters are identical across models).

## Removed Points
These points are flagged to be removed, treat them with caution:

1. **Missing comparison with weighted CP / density ratio methods** (harsh critic): "There exist other approaches for distribution shift without labels (e.g., weighted conformal prediction using density ratios)." — Removed per rule: do not mention missing related works, as we cannot verify their existence.
2. **Reproducibility nitpicks about undisclosed hyperparameters** (harsh critic): "omits the number of runs, random seeds, hardware, learning rate for ETA, batch size" — Removed per rule: these are nitpicks about trivial implementation details. The paper states hyperparameters are identical across all models and uses a known TTA subroutine.
3. **"Conflates two different data-access models" framing** (harsh critic's Issue 3) — The paper clearly separates supervised (✗) from label-free (✓) methods in Table 3 with an explicit column. The comparison is presented informatively, not deceptively. The substantive concern about overselling the "nearly match" claim is retained above.
4. **Table 2 coloring missing a key / hard to parse in grayscale** — Pure formatting nitpick. Removed per rule.
5. **Figure 3 is too small to read** — Pure formatting nitpick. Removed per rule.
6. **Section 3.2 ETA description too vague for reproducibility** — The paper explicitly says "we only present its high level idea for the sake of completeness" and cites the original ETA paper. This is standard practice for a subroutine that is not the paper's core contribution.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Add a brief **Limitations** paragraph to the conclusion covering: (a) the batched/transductive nature of the entropy quantile computation, (b) the lack of formal coverage guarantees, (c) the failure on extremely hard shifts like ImageNet-A, and (d) the gap in local coverage compared to supervised OCP methods.
2. **Add variance estimates** for the headline results (Tables 1 and 3). Running each experiment 3–5 times with different calibration splits or random seeds would suffice.
3. **Clarify the online protocol** for the continuous shift experiments: specify whether the entropy quantile is computed over a sliding window, an accumulating set, or recomputed from scratch at each batch.
4. **Qualify the abstract's claim** "nearly match the performance of supervised algorithms" by noting that this refers to average marginal coverage, and that significant gaps remain in local coverage.
5. Add an **ablation study** on the \(\beta\) parameter to demonstrate robustness.

## Score and Decision

This paper makes a solid empirical contribution: the proposed ECP and EACP methods are simple, well-motivated, and consistently effective across a wide range of datasets, architectures, and shift types. The weaknesses are addressable with text clarifications and modest additional experiments; none threaten the core claims. The paper is clearly above the acceptance bar.

MY FINAL SCORE: <pineapple>8.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>