Now I have enough information to write my final consolidated review. Let me carefully assess each point.

## Summary

DART is a plug-in test-time adaptation method that corrects class-wise confusion patterns arising from label distribution shifts. It trains a prediction refinement module at "intermediate time" on Dirichlet-sampled batches of clean training data, using the average pseudo-label distribution and a novel prediction deviation metric as inputs, and outputs an affine transformation (W, b) applied to logits. The method achieves 5–18% accuracy improvements across multiple TTA baselines and benchmarks under label distribution shifts, while preserving performance under balanced conditions.

## Strengths

- **Consistent class-wise confusion pattern observation**: The paper provides both theoretical (Gaussian mixture toy model) and empirical (confusion matrices across multiple corruption types on CIFAR-10 in Figure 1) evidence that confusion patterns under label shift are consistent across covariate shifts. This is the key insight that motivates the entire approach and is well-supported.

- **Prediction deviation as a diagnostic signal**: The observation (Figure 3) that average pseudo-label distribution alone fails to distinguish IR=1 (no shift) from IR=5000 (severe shift), and the introduction of prediction deviation d_B as a complementary metric that monotonically tracks shift severity, is a genuine and useful contribution. This insight extends beyond the specific method proposed.

- **Plug-in compatibility with 8 TTA methods**: Table 1 demonstrates DART's improvements across eight different TTA baselines (BNAdapt, TENT, PL, NOTE, DELTA, ODS, LAME, SAR) on multiple benchmarks. The ability to enhance existing methods rather than replace them is practically valuable and well-demonstrated.

- **Substantial and consistent performance gains under label shifts**: DART achieves notable improvements (5.7–18.1% on CIFAR-10C-LT, 16.7–39.8% on CIFAR-100C-imb) that scale with shift severity, while preserving performance when ρ=1, as confirmed by the ablation in Table 1.

- **Well-designed ablation studies**: Tables 4–5 systematically validate the contribution of each input (prediction deviation provides 3.2–6.7% gains) and output (W vs. b, affine vs. additive), and the Dirichlet sampling strategy (outperforms uniform+LT on online shifts, Table 4).

## Weaknesses

### Fatal

None.

### Major

- **Method for large-scale benchmarks (DART-split) is underspecified relative to its prominence**: DART-split, which partitions g_φ into a severity detector g_{φ₁} and a refinement generator g_{φ₂} with a hard threshold gate (s_B > 0.5), is used for all results on CIFAR-100C-imb and ImageNet-C-imb — the benchmarks most emphasized for headline improvements (16.7–39.8% gains). However, DART-split is described only in the experiments section (line 321–323), not in the method section. The core single-module DART (Sections 2–3) is validated only on CIFAR-10 (10 classes). This creates a misalignment: the paper's primary quantitative claims come from a variant that is less thoroughly specified than the base method. The paper notes DART-split is compared to DART on CIFAR-10C-LT (referenced as Table label "dart-split on cifar10clt"), but this comparison and DART-split's training procedure should be detailed in the method section.

- **Missing direct comparison with LSA**: LSA (Park et al.) is the most closely related prior work — both methods use intermediate-time training on class-shifted batches. The paper discusses LSA in Sections 1 and 5 and tests a "variant of DART" with additive parameters "inspired by LSA" (Table 5), but the actual LSA method is not included as a baseline in any experiment. The ablation in Table 4 (Dirichlet vs. uniform+LT sampling) tests a LSA-inspired sampling strategy within the DART framework — which differs from LSA's actual method in output representation (additive parameters vs. affine transformation) and other design choices. Without a direct LSA comparison, the paper's claims that DART's Dirichlet sampling and prediction deviation improvements over LSA are unsubstantiated empirically.

- **Distribution gap between intermediate-time and test-time inputs to g_φ is unaddressed**: During intermediate-time training, g_φ receives (p̄, d) features computed from the BN-adapted model processing **clean** training images with Dirichlet-sampled class distributions. At test time, the same model processes **corrupted** images, so the (p̄, d) inputs to g_φ come from a different distribution. The paper's core observation that confusion *patterns* are consistent across corruption types (Figure 1) explains why the *correction transformation* might generalize, but it does not explain why the *inputs* (p̄, d) to g_φ remain meaningful across this distribution gap. The paper should analyze or discuss this — for instance, by showing that (p̄, d) features for the same label shift, but different corruptions, cluster together, which would explain the observed generalization empirically. An ablation testing corruption-augmented intermediate-time data could also address this.

### Minor

- **The "no degradation" claim is slightly overstated**: The abstract states "without any performance degradation when there is no label distribution shift." While the table data for ρ=1 shows negligible differences (within noise), on PACS one domain shows a marginal decrease (e.g., Cartoon: 83.0→82.5). The claim should be softened to "minimal performance degradation" or "no significant degradation." While the difference is within standard deviation, the absolute claim is technically incorrect.

- **Quantitative analysis of confusion pattern consistency is missing**: The core motivation rests on confusion patterns being similar across corruptions under the same label shift, but this is demonstrated qualitatively via visual inspection of confusion matrices (Figure 1, 2 distributions × 4 conditions on CIFAR-10). A quantitative similarity metric (e.g., correlation between confusion matrices under different corruptions) would significantly strengthen this foundational claim.

- **Properties #1–#3 from the toy model are presented ambiguously**: The three properties in Section 2 are stated with mathematical notation, but it is unclear whether these are formally proven or derived empirically from the toy model. The paper should clarify whether these are theorems (with proofs ideally in the appendix) or empirical observations.

### Trivial

- The regularization hyperparameter α=0.1 is stated without ablation, but this is a minor concern given the robust overall results.

## Nice-to-Haves

- Per-class accuracy analysis for the CIFAR-10C-imb results at IR=5000 (BNAdapt+DART achieves 82.4% vs. 20.3%), to verify that tail classes also benefit, not just head classes.

- Analysis of (p̄, d) feature distributions under clean vs. corrupted inputs for the same label shift, to explain the generalization across corruptions.

- Corruption-augmented intermediate-time data ablation to test whether closing the domain gap further improves performance.

## Removed Points

*These points are flagged to be removed, treat them with caution:*

- **Harsh critic's claim that DART-split is "fundamentally different" from the described method**: Overstated. DART-split is an extension of the same core idea (prediction refinement via affine transformation guided by label shift detection) adapted for scalability. It is a legitimate variant, not a fundamentally different method. The real concern is about underspecification placement, not about DART-split being a different method altogether.

- **Harsh critic's Figure 2 critique (only one corruption type at one severity level)**: The paper's Figure 3 (not Figure 2) actually shows CIFAR-10C-imb data with multiple IR values (1, 20, 50, 5000) under Gaussian noise. The prediction deviation metric's behavior across different corruption *types* (not severities) is indeed not shown, but the paper's experiments validate across all 15 corruption types, so this is a presentation gap, not a methodological flaw.

- **Harsh critic's concern about staleness between f_{θ̄₀} and f_θ**: The paper explicitly addresses this on line 236 — it uses f_{θ̄₀} (the BN-adapted pre-trained model) for computing g_φ inputs, not the continually updated f_θ, precisely to maintain consistency with intermediate-time training. Predictions from f_θ are then refined using g_φ's output. This is a design choice, not an oversight.

- **Strength Finder's claim that "Table 6 and related work show DART's affine logit transformation outperforms additive parameter generation (82.0±2.2 vs 85.2±0.1)" constitutes a comparison with LSA**: This is a comparison of a design choice *within* the DART framework, not a comparison with LSA itself. The DART variant with additive parameters differs from LSA in multiple ways (training procedure, inputs, sampling strategy).

- **Strength Finder's claim about "comprehensive ablation studies" as a separate strength**: This overlaps with the plug-in compatibility strength and the core results. The ablations are good but primarily validate design choices that are already well-motivated theoretically.

- **Harsh critic's concern about the 82.4% recovery at IR=5000 being "too good"**: The baseline accuracy at ρ=1 is 85.3%, so recovering from 20.3% to 82.4% (within 3% of the balanced baseline) is plausible for a method that directly corrects confusion patterns. The 0.7 standard deviation also indicates reasonable variance. Without evidence of a problem, this speculation is not a valid criticism.

## Novel Insights

The core insight — that BN-adapted classifiers under label distribution shifts exhibit consistent class-wise confusion patterns *regardless of covariate shift type* — is both novel and well-supported. Combined with the prediction deviation metric, which elegantly disentangles "uniform predictions from balanced data" from "uniform predictions from unconfident predictions under severe shift," this provides a principled foundation for test-time label shift correction. The observation that the average pseudo-label distribution becomes unreliable precisely when it's most needed (severe shifts) is a striking finding that should inform future TTA work beyond DART.

## Suggestions

- Move DART-split's specification (architecture, training procedure, threshold mechanism) from the experiments section to the method section, since it is used for the most important large-scale benchmark results.
- Add a direct comparison with LSA as a baseline, even on just one benchmark (e.g., CIFAR-10C-LT), to empirically substantiate the claimed advantages.
- Add an analysis of how (p̄, d) feature distributions cluster by label shift vs. corruption type, which would directly address the intermediate-time/test-time domain gap concern and could become a key strength of the paper.

## Score and Decision

The paper makes a genuine contribution in identifying consistent confusion patterns under label shifts and proposing a practical plug-in correction method with substantial empirical gains. The two major weaknesses — DART-split being underspecified for its prominence, and the missing LSA comparison — are significant but do not invalidate the core claims. The distribution gap concern is valid but the empirical results suggest it is not fatal in practice. The contributions are real and the method is well-motivated.

Originality: Moderate. The intermediate-time training idea is shared with LSA, but the prediction deviation metric and the confusion-pattern-based affine transformation approach are novel.

Importance: The problem of label distribution shift in TTA is important and timely.

Claims support: Strong on CIFAR-10, weaker on large-scale benchmarks due to method variant discrepancy.

Experiments: Comprehensive on CIFAR-10, with a reasonable but underspecified extension to larger benchmarks.

Clarity: Generally clear, with the DART-split specification being the main gap.

Value: The plug-in design and prediction deviation metric should be useful to the TTA community.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>