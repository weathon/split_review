## Summary
# Final Review Report

## Summary

This paper proposes Swin4TS, a model that adapts the Swin Transformer's window-based attention and hierarchical representation design to long-term time series forecasting (LTSF). The key technical contributions are: (1) window-restricted attention that achieves O(M L) complexity — linear in both series length L and number of channels M; (2) a K-stage hierarchical structure that captures temporal patterns at multiple scales; and (3) flexible support for both channel-independent (CI) and channel-dependent (CD) strategies. The method is evaluated on 32 prediction tasks across 8 standard benchmarks, showing competitive or superior performance against 7 recent baselines. The paper also demonstrates that another ViT variant, TNT, can be adapted for time series (TNT4TS) with comparable results.

**Strengths**: The core idea — adapting vision-oriented window/hierarchical attention to time series — is well-motivated by the structural similarity between image patches and time-series segments. The linear complexity analysis is clear and contrasts favorably with PatchTST (O(M L²)) and Crossformer (O(M L²)). The ablation studies (shift-window and hierarchical design) provide some evidence for the contribution of each component. The CI/CD flexibility is a practical advantage.

**Weaknesses (overview)**: (1) The SOTA and "first" claims are overextended relative to the reported evidence. Baseline comparisons are confounded by asymmetric input lengths (L=512 for Swin4TS vs L=96 default for several baselines). (2) No variance or statistical significance is reported, making small-margin improvements unverifiable. (3) Ablation deltas (2-3%) are small and may not be statistically significant. (4) The core motivation (structural analogy between time series and images) is asserted rather than rigorously justified. (5) The conclusion overclaims the cross-domain transfer finding (C3) without sufficient evidence or any discussion of limitations. External literature verification was unavailable in this run (Retrieval-Disabled Mode); all novelty verdicts are deferred for manual verification.

## Strengths
**S1. Clear linear-complexity advantage.** The paper provides a clean complexity analysis showing that Swin4TS achieves O(M L) encoder complexity, which is linear in both series length L and number of channels M. This contrasts favorably with PatchTST (O(M L²)) and Crossformer (O(M L²)), and is explicitly verified with inference time and memory benchmarks (Table 4). For practitioners working with long time series, this is a genuine practical advantage.

**S2. Well-motivated architectural transfer.** The adaptation of window-based attention (restricting self-attention to local windows, then using shift operations for cross-window communication) from Swin Transformer to time series is technically sound. The idea that temporal locality mirrors spatial locality in images is intuitive and provides a clear design rationale. The hierarchical downsampling (Eq. 7-8) that aggregates windows across K stages is a natural way to capture multi-scale temporal patterns.

**S3. Flexible CI/CD design.** Supporting both channel-independent (CI) and channel-dependent (CD) strategies within the same framework is a practical strength. The paper correctly identifies that CI is more efficient for high-channel datasets (Traffic, Electricity) while CD captures cross-channel correlations useful for smaller-channel datasets (ILI, ETT). The channel-shuffle ablation (Table 12, Appendix C.3) is a nice diagnostic showing that CD benefits from order-agnostic attention.

**S4. Comprehensive benchmark evaluation.** The paper evaluates on 32 prediction tasks across 8 standard datasets with 7 baselines. The additional effort to re-evaluate baselines at multiple input lengths (L=96, 336, 512) and select the best per dataset is a good-faith attempt at fair comparison. The supplementary experiments (randomness test, hierarchical design sensitivity, historical length study) provide useful diagnostic information.

**S5. Cross-domain validation with TNT4TS.** The additional TNT4TS experiment (Appendix E), while limited, demonstrates that the ViT-to-time-series transfer idea is not specific to Swin architecture, strengthening the paper's broader claim that vision Transformer designs can work for time series.

## Weaknesses
**W1. Unbounded SOTA and novelty claims.** The paper repeatedly claims "state-of-the-art performance across all datasets" (Page 1 Abstract, Page 6 Results, Page 9 Conclusion) and "first Transformer-based model owning linear complexity with both L and M" (Page 9). The SOTA claim is not bounded to the set of evaluated baselines, and the "first" claim omits important caveats about models with M-independent complexity. Without external literature verification (Retrieval-Disabled Mode), these claims cannot be independently confirmed. (Annotation: Page 1 Abstract, Page 9 Complexity)

**W2. No statistical significance or variance reporting.** All main results (Tables 1, 2) report only point estimates (MSE/MAE) without standard deviations, confidence intervals, or significance tests. The randomness test (Appendix C.1) shows non-negligible seed variation for Swin4TS/CD (up to ~0.01 MSE on ETT datasets), yet the main tables use only one seed (2023). For improvements as small as 0.005 MSE (Weather 96: 0.143 vs 0.148), the ranking is not statistically reliable. (Annotation: Page 6 Results)

**W3. Confounded baseline comparison.** Swin4TS uses L=512 for all datasets, while several baselines (MICN, TimesNet, Crossformer, FEDformer, Autoformer) were originally designed for L=96. Although the authors evaluate baselines at L=96, 336, 512 and select best results, this gives Swin4TS an asymmetric advantage because its architecture is tuned for long inputs. The paper does not report which L produced each baseline's best result, reducing transparency. (Annotation: Page 6 Experimental Setup)

**W4. Ablation gains are small and lack statistical verification.** The ablation study shows 2-3% MSE increases when removing shift-window and/or hierarchical designs (Table 3: ETTm1 0.348→0.361, ETTm2 0.248→0.263). These deltas are small enough that they could fall within random seed variation (as shown in Appendix C.1). No confidence intervals or significance tests are provided. Only two datasets (ETTm1, ETTm2) are used for ablation. (Annotation: Page 7 Ablation)

**W5. Core motivation is not rigorously justified.** The central premise — that time-series and image patches share structural similarity justifying direct ViT transfer — is asserted with two weak arguments (fixed length, need for patching) rather than rigorous reasoning. The paper does not address fundamental differences: temporal causality (time cannot look ahead), trend/seasonality decomposition, and the physical meaning of time indices have no image analogues. (Annotation: Pages 1-2 Introduction)

**W6. Conclusion overclaims C3 without limitations.** The paper concludes that Swin4TS "confirms that time series and image can be modeled using the same framework" and that "characteristics such as trend and seasonality can be learned by Transformer." No limitations are discussed — not even the clear weakness that Swin4TS/CD underperforms on high-channel datasets. The TNT4TS evidence (4 ETT datasets only) is too thin to support the broad cross-domain claim. (Annotation: Page 9 Conclusion)

**W7. Notation and reproducibility gaps.** Equations (3)-(6) reuse variable `z_i` ambiguously. The hierarchical downscaling (Eq. 7) does not explain how the feature map dimension relates back to the original time axis. The paper does not discuss padding for non-power-of-2 window counts or provide pseudocode. (Annotation: Page 4, Page 5 Method)

## Key Issues
**Issue 1 (Critical) — Overclaimed SOTA and novelty without statistical grounding.** The paper's central claims ("state-of-the-art," "first Transformer with linear complexity in L and M") are stated as facts rather than bounded, testable propositions. Combined with the absence of any variance or significance testing (Issue 2), the reader cannot distinguish genuine architectural superiority from random variation or favorable comparison settings. **Fix**: Replace unbounded SOTA language with precise scope qualifiers; report mean±std over ≥3 seeds; add significance tests against strongest baseline.

**Issue 2 (Major) — Missing statistical reliability.** All 32 prediction tasks report only single-seed point estimates. The randomness test (Appendix C.1) shows seed variation exists, yet no main-table result carries confidence intervals. Improvements ≤0.01 MSE (e.g., Weather 96: 0.143 vs 0.148) are within the range of seed variation observed in the appendix. **Fix**: Re-run all main experiments with 3-5 seeds; report mean±std in Tables 1 and 2; add a paired significance test across all tasks.

**Issue 3 (Major) — Asymmetric baseline evaluation.** Swin4TS uses L=512 (its designed input length) while several baselines are re-run at L=96, 336, 512 with default hyperparameters not tuned for longer inputs. The comparison does not control for input length as an independent variable. **Fix**: Add a controlled experiment where all methods use the same L=96; report per-dataset which L gave each baseline's best result; consider fine-tuning baseline hyperparameters for longer L.

**Issue 4 (Major) — Ablation study too narrow for strong conclusions.** Ablation only on ETTm1/ETTm2 with 2-3% deltas, no variance, no significance test. **Fix**: Expand to ≥4 datasets; run 3 seeds per ablation variant; statistically test whether deltas exceed seed variation.

**Issue 5 (Major) — Conclusion lacks limitations and overclaims C3.** The paper claims that time series and images "can be modeled using the same framework" but provides only weak supporting evidence (TNT4TS on 4 datasets). No limitations are discussed. **Fix**: Add a dedicated limitations paragraph; tone down the cross-domain claim; explicitly state that the result is specific to window-based ViT designs, not all ViT models.

## Actionable Suggestions
### Suggestion 1: Revise SOTA claim to be scoped (Must)
Replace "Swin4TS achieves state-of-the-art performance across all datasets" with:
"Swin4TS achieves competitive or superior results against 7 recent baselines on 32 forecasting tasks across 8 datasets, under the evaluated settings (input length L=512 for Swin4TS and PatchTST, L=96/336/512 for other baselines with best selected)."

### Suggestion 2: Add statistical rigor (Must)
Report all main results (Tables 1, 2) as mean ± std over ≥3 random seeds. Add a footnote stating that bold/underline rankings are based on mean MSE, and that statistical significance is assessed via a paired Wilcoxon signed-rank test comparing Swin4TS/CI against the strongest baseline across all 32 tasks. Include a compact significance table in the appendix.

### Suggestion 3: Add controlled input-length experiment (Must)
Add one supplementary table where all methods use L=96 (the most common default) with Swin4TS configured accordingly. This controls for the input-length confound and isolates the architectural contribution. The paper claims (Appendix C.4) that "even with L=96, Swin4TS is better than most baselines" — this claim should be explicitly verified in a dedicated table.

### Suggestion 4: Strengthen ablation (Must)
Expand ablation to at least 4 datasets (add Weather and ETTh1). Run each ablation variant with 3 seeds. Report p-values for the difference between full model and each ablation variant using a paired bootstrap test. If 2-3% deltas are not significant after variance accounting, tone down the claim from "play important roles in ensuring prediction accuracy" to "contribute to modest accuracy improvements."

### Suggestion 5: Add limitations paragraph (Must)
Add a "Limitations" subsection to the conclusion covering: (a) CD underperformance on high-channel datasets, (b) no OOD evaluation, (c) window-size sensitivity not explored, (d) no decision rule for CI vs CD choice.

### Suggestion 6: Improve related-work structure (Nice-to-have)
Reorganize Section 2 around comparison axes (complexity class, patching strategy, channel modeling, multi-scale capability) rather than paper-by-paper summaries. Add a comparison table.

### Suggestion 7: Clarify notation and reproducibility (Nice-to-have)
Rename variables in Eqs (3)-(6) to distinguish each transformation stage. Add a brief description of how the hierarchical output shape maps to the prediction length T, and how non-power-of-2 window counts are handled.

### Suggestion 8: Tighten contribution list (Nice-to-have)
Merge C2 and C3 into C1's evidence narrative. Present the contribution as one methodological claim (Swin4TS design) supported by two forms of evidence (benchmark performance and cross-ViT validation with TNT4TS).

## Storyline Options + Writing Outlines
### Current Storyline Assessment
The current introduction (4 paragraphs) follows: Application motivation (P1) → ViT background (P2) → Prior cross-domain work (P3) → Proposed method description (P4) → Contribution list. The main weakness is that the gap ("what is missing in existing LTSF methods that requires a new approach") is not explicitly stated — the reader is told that existing methods "exhibit gradually improved performance" but not what specific limitation Swin4TS addresses beyond complexity.

### Recommended Storyline: "Gap-First, Architecture-Transfer"

**Abstract Outline (4 sentences, self-contained)**:
- S1 (Problem): "Long-term time series forecasting (LTSF) is challenging due to long-range dependencies and the quadratic cost of Transformer-based models."
- S2 (Gap): "Existing methods reduce complexity at the cost of expressiveness, or model multi-scale patterns without linear scaling — and none offer flexible channel-dependent/independent modeling in a unified architecture."
- S3 (Method): "We propose Swin4TS, which adapts Swin Transformer's window-based attention (O(M L) complexity) and hierarchical representation to time series, supporting both channel-dependent and channel-independent strategies."
- S4 (Evidence): "On 32 tasks across 8 benchmarks, Swin4TS achieves competitive or superior results against 7 recent baselines."
- S5 (Implication): "These results suggest that vision Transformer architectures with local-window inductive biases can transfer effectively to time series analysis."

**Introduction Outline (5 paragraphs)**:
- P1 (Stakes + Gap): "LTSF is critical for transportation, healthcare, manufacturing. Key challenge: long-range dependencies + multi-variable interactions. Existing Transformer methods (Informer, Autoformer, FEDformer, PatchTST) have improved performance but still face a trilemma: they cannot simultaneously achieve (i) linear complexity in L and M, (ii) multi-scale temporal representation, and (iii) flexible CI/CD channel modeling."
- P2 (Structural insight): "Images and time series share a property absent in NLP: local neighborhoods dominate correlations, while long-range dependencies can be captured through hierarchical aggregation. This locality suggests that window-restricted attention — successful in Swin Transformer for vision — is a natural fit for time series."
- P3 (Prior cross-domain attempts and their limitations): "Existing cross-domain work either fine-tunes language models (GPT for TS) or converts time series to images (MV-DTSA, ViTST). These approaches do not directly align time-series data structure with the vision model's design, potentially introducing artifacts."
- P4 (Proposed solution): "We propose Swin4TS, directly adapting Swin Transformer's window attention and hierarchical downsampling to time series. Window attention gives O(M L) complexity. Hierarchical representation captures multi-scale patterns. The model naturally supports both CI and CD strategies."
- P5 (Contributions — consolidated): "Our contributions are: (1) Swin4TS design with O(M L) complexity, multi-scale hierarchy, and CI/CD flexibility. (2) Comprehensive evaluation on 32 tasks showing competitive results. (3) Evidence that window-based ViT designs can transfer to LTSF, validated also via TNT4TS."

### Alternative Storyline: "Complexity-First, Method-Centric"
Lead with the complexity problem (O(L²) is the bottleneck), then introduce window attention as the solution, then show that hierarchical representation and CD/CI flexibility are natural extensions. This storyline is more technical and appeals to a practitioner audience. Use if targeting a more systems-oriented venue.

### Alignment Checks
- **Problem alignment**: The revised introduction's gap (trilemma) directly matches the three claimed benefits of Swin4TS (linear complexity, multi-scale, CI/CD).
- **Variable alignment**: Key concepts from P2 (window attention, hierarchy, CI/CD) appear as core method variables in Section 3.
- **Contribution-evidence alignment**: Claims are supported by Table 1 (performance), Table 4 (complexity), and Table 3 (ablation), though variance reporting is needed for full alignment.

## Priority Revision Plan
```text
ASCII Diagram — Revision Strategy Roadmap

[Issue 1: Unbounded SOTA claims without variance]
    -> Fix: Scope SOTA language; add multi-seed std to tables
    -> Expected impact: Claims become defensible
[Issue 2: Missing statistical rigor]
    -> Fix: Re-run all experiments with 3-5 seeds; add significance test
    -> Expected impact: Rankings verifiable, not seed-dependent
[Issue 3: Confounded baseline comparison]
    -> Fix: Add controlled L=96 experiment; report per-dataset best L
    -> Expected impact: Fairer head-to-head comparison
[Issue 4: Weak ablation]
    -> Fix: Expand to 4+ datasets; multi-seed; add significance
    -> Expected impact: Ablation conclusions become reliable
[Issue 5: Conclusion overclaim + missing limitations]
    -> Fix: Add limitations paragraph; tone down C3
    -> Expected impact: Paper becomes scientifically honest
[Issue 6: Weak related-work structure]
    -> Fix: Reorganize by comparison axes
    -> Expected impact: Clearer positioning
[Issue 7: Notation gaps]
    -> Fix: Clarify Eqs (3)-(6); add padding description
    -> Expected impact: Improved reproducibility
```

### Priority Table

| Priority | Action | Effort | Impact | Requirement |
|----------|--------|--------|--------|-------------|
| **P0** | Add multi-seed std to Tables 1, 2 | Medium (re-run ~32 tasks × 3 seeds) | High — enables statistical verification | Must |
| **P0** | Add controlled L=96 comparison | Low-medium (re-run Swin4TS at L=96) | High — resolves confound | Must |
| **P0** | Add limitations paragraph | Low (writing) | High — scientific completeness | Must |
| **P0** | Scope SOTA/first claims | Low (wording edits) | High — defensibility | Must |
| **P1** | Expand ablation: ≥4 datasets + multi-seed | Medium | Medium-high — strengthens main claim | Must |
| **P1** | Significance test across tasks | Low (computational) | Medium — supports ranking claims | Must |
| **P2** | Reorganize related work by axes | Medium (writing) | Medium — improves positioning | Nice-to-have |
| **P2** | Clarify notation (Eqs 3-6, Eq 7) | Low | Medium — reproducibility | Nice-to-have |
| **P2** | Merge contribution list (C2 into C1) | Low | Low — cosmetic | Nice-to-have |

### Expected Impact After Full Fixes
After addressing all P0 and P1 items, the paper would present defensible, variance-aware results with a fair baseline comparison and honest limitation discussion. The core technical contribution (linear-complexity window attention + hierarchy for time series) is solid enough to withstand scrutiny once the statistical and framing issues are resolved.

## Experiment Inventory & Research Experiment Plan
### A. Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|-----------------|-------------------|
| E1 | Multivariate forecasting performance | 8 datasets, 32 tasks, 7 baselines, L=512 (Swin4TS), L=96/336/512 (baselines) | MSE, MAE | Swin4TS/CI best avg on Weather, Traffic, Electricity; Swin4TS/CD best on ILI, ETT | C1 (architecture works), C2 (SOTA) | No variance; asymmetric L; some margins very small |
| E2 | Univariate forecasting | 4 ETT datasets, 7 baselines | MSE, MAE | Swin4TS best on all 4 ETT | C2 | Only ETT datasets; small margins on ETTm2 |
| E3 | Ablation (shift-window + hierarchy) | ETTm1, ETTm2, CD variant | MSE, MAE | 2-3% MSE increase after removal | C1 (design components matter) | Only 2 datasets; no variance; small deltas |
| E4 | Randomness test | All 8 datasets (CI), 4 ETT (CD), 5 seeds | MSE | Low seed sensitivity | Robustness claim | Single-seed in main tables; non-overlapping seeds for CI/CD |
| E5 | Channel order effect | 4 ETT, CD variant | MSE, MAE | Shuffled > fixed order | CD benefits from order-agnostic attention | Only ETT datasets |
| E6 | Historical length study | All datasets, L=96 to 720 | MSE, MAE | Longer L generally better | Swin4TS scales with L | No L=96 controlled comparison vs baselines |
| E7 | Hierarchical design sensitivity | All datasets, 1/2/3/4-stage | MSE, MAE | Optimal stage varies by dataset | Hierarchy useful | No theoretical guidance for choosing K |
| E8 | Dynamic covariate effect | All datasets, CI variant | MSE, MAE | Most datasets worse with timestamps | — | Negative result not analyzed |
| E9 | Transferability (fixed channel) | 4 ETT, CI variant | MSE, MAE | Model transfers across channels | C3 (cross-domain learning) | Only ETT; only CI |
| E10 | TNT4TS validation | 4 ETT, CI variant | MSE, MAE | Comparable to Swin4TS/CI | C3 (ViT-to-TS transfer) | Only 4 datasets; similar but not better |
| E11 | Computational efficiency | Electricity dataset, 7 Transformer baselines | Time (ms), Memory (GB) | Swin4TS/CI fastest (11.3ms); Swin4TS/CD slower (45.3ms) | O(M L) complexity verified | Only one dataset; no theoretical roofline |

### B. Research-Theme Gap Diagnosis

**New Knowledge**: The paper's primary knowledge claim — that window-based ViT attention transfers effectively to time series — is partially supported but narrowly evidenced. The TNT4TS experiment (only 4 ETT datasets, CI only) is insufficient to prove broad cross-domain transferability.

**Reproducibility**: The method description is adequate but has notation ambiguities (Eqs 3-6) and missing details (padding strategy, window alignment for non-power-of-2 lengths). Hyperparameters are mostly reported in Appendix A.2 but no pseudocode is provided.

**Impact on Practice**: The linear-complexity advantage is practically useful for long-sequence LTSF. However, without a decision rule for CI vs CD, practitioners cannot easily choose between the two variants.

### C. Proposed Research Experiments

| ID | Target Claim | Hypothesis | Minimal Design | Controls | Metrics | Success Criterion | Est. Cost | Expected Gain |
|----|-------------|-----------|---------------|----------|---------|------------------|-----------|---------------|
| **P0-R1** | Statistical reliability (all results) | Multi-seed ranking consistent with single-seed | Re-run Tables 1, 2 with 3 seeds; report mean±std | Same hyperparams, same L | MSE mean, std, min-max range | std ≤ 0.01 × mean for ≥80% of tasks | 2-3 GPU days | High: enables statistical verification |
| **P0-R2** | Fair comparison (L=96) | Swin4TS still competitive at L=96 | Run Swin4TS/CI with L=96 on all 8 datasets | Same baselines at L=96 | MSE, MAE | Swin4TS within 5% of best baseline avg | 4-6 GPU hours | High: controls for L confound |
| **P1-R3** | Ablation robustness | Effect sizes consistent across datasets | Expand ablation to Weather + ETTh1; 3 seeds per variant | Full model vs w/o shift vs w/o scale vs w/o both | MSE mean±std, p-value | p < 0.05 for full vs w/o both on ≥3 of 4 datasets | 4-8 GPU hours | Medium-high: strengthens core claim |
| **P1-R4** | Significance test | Swin4TS significantly better than best baseline | Paired Wilcoxon signed-rank test across 32 tasks | Swin4TS/CI vs PatchTST (best CI baseline) | MSE per task, W statistic | p < 0.01 | 1 CPU hour | Medium: supports SOTA framing |
| **P2-R5** | OOD robustness | Swin4TS degrades gracefully under distribution shift | Evaluate on corrupted/noisy test splits (Weather + ETT) | Same model, corrupted vs clean | MSE ratio (corrupted/clean) | Ratio ≤ 1.2 (20% degradation max) | 2 GPU hours | Medium: addresses generalization gap |

```text
ASCII Diagram — Experiment Upgrade Plan

P0 (Immediate, before resubmission)
├── R1: Multi-seed variance (Tables 1, 2)
├── R2: Controlled L=96 comparison
└── [Wording: Scope SOTA claims; add limitations]

P1 (This week)
├── R3: Expanded ablation (4 datasets, 3 seeds, p-values)
├── R4: Significance test (Wilcoxon, 32 tasks)
└── [Writing: Reorganize related work, fix notation]

P2 (Before final submission)
├── R5: OOD robustness experiment
└── [Writing: Merge contribution list, add decision rule for CI vs CD]
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6/10**

**Rationale**: The paper has a solid technical core (window-based attention with O(M L) complexity adapted to time series) and demonstrates competitive performance across multiple benchmarks. However, the score is constrained by:

- **Novelty (deferred, estimated moderate)**: The core idea — adapting Swin Transformer to time series — is intuitive and the paper is among the first to do so, but the novelty is incremental (engineering adaptation rather than a new architectural principle). Without external literature verification, the "first" and "SOTA" claims cannot be confirmed. Estimated novelty value: moderate.
- **Validity concerns (major)**: No variance reporting, no significance tests, asymmetric baseline comparison, and ablation deltas within seed-variation range collectively weaken confidence in all quantitative conclusions. These issues are fixable (see P0 items).
- **Research value (moderate-high)**: The linear-complexity advantage and CI/CD flexibility are practically useful. The cross-domain transfer insight (C3) is interesting but overclaimed in current wording.
- **Reproducibility**: Adequate but not strong — notation ambiguities and missing details (padding, pseudocode) need correction.

**Post-Revision Target: [7, 8]/10**

If all P0 and P1 items are addressed (multi-seed variance, controlled L=96 comparison, expanded ablation, limitations paragraph, scoped claims), the paper's validity and scientific honesty would improve substantially. The upper bound of 8 assumes that the controlled experiments confirm Swin4TS's advantages hold under fair comparison. If the controlled experiments show that gains are primarily driven by longer input length rather than architecture, the target would be [6, 7].

### Page Coverage Audit

| Page | Annotation Count | Coverage Status | Notes |
|------|-----------------|----------------|-------|
| 1 (Abstract + Intro P1-P3) | 2 | Covered | Abstract rewrite, Intro P1 gap |
| 2 (Intro P4, Contributions, RW P1) | 3 | Covered | Structural analogy, contributions overlap, RW organization |
| 3 (RW P2-P3, Method problem def) | 1 | Covered | ViT section connection to LTSF |
| 4 (Window attention, Eqs 1-6) | 1 | Covered | Notation ambiguity |
| 5 (Hierarchical, CD strategy) | 1 | Covered | Downscaling clarity |
| 6 (Exp setup, Results P1) | 2 | Covered | Baseline fairness, SOTA claim scope |
| 7 (Ablation results) | 1 | Covered | Small deltas, no variance |
| 8 (Hierarchical info, Other results) | 1 | Covered | Qualitative analysis lacks metrics |
| 9 (Complexity, Conclusion) | 2 | Covered | "First" claim, conclusion overclaim |
| 10-12 (References) | 0 | Skipped (non-substantive) | Reference list only |
| 13-23 (Appendix) | 0 | Pending | Appendix contains key experiments but main-body coverage was the priority |

**Skipped paragraphs**: The reference list (pages 10-12) is non-substantive. Appendix sections contain important experimental details but are supplementary; main-body coverage was prioritized per review guidelines.