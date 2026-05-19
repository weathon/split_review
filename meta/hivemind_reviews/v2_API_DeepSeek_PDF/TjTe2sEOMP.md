## Summary
# Final Review Report

## Summary

This paper proposes a prompt-driven mixture-of-experts (MoE) framework for universal unsupervised anomaly detection across multiple medical imaging modalities and organs. The method combines a shared vision encoder, a CLIP-based text encoder for prompt conditioning, a routing network, and multiple "hallucination-aware" decoder experts that jointly predict reconstruction and per-pixel hallucination scores. The key technical idea is to learn a per-pixel hallucination weight $u$ that down-weights reconstruction errors at normal-region boundaries during training, thereby reducing false-positive anomalies at inference. The authors compile a benchmark dataset of 12,153 images across 5 modalities (X-ray, MRI, OCT, ultrasound, CT) and 4 organs (lung, brain, retina, breast) from existing public datasets. Experiments comparing against 10 single-task and 4 universal baselines show consistent improvements in AUC, F1, and accuracy across all five datasets.

**Core strengths**: The universal multi-organ multi-modal setting is practically motivated and addresses a clear gap in prior work. The hallucination quantification mechanism is a plausible approach to reducing boundary false positives in reconstruction-based anomaly detection. The paper provides comprehensive baselines and ablation studies.

**Core weaknesses**: (1) The MoE framework with supervised routing (Eq. 4) deviates from standard MoE design — the K=N result means all experts are always active, making the model an ensemble rather than sparsely routed experts. (2) No statistical variance or confidence intervals are reported for any experiment, making the claimed improvements unverifiable. (3) The "hallucinatory anomaly" phenomenon is a known boundary-artifact issue, not a new discovery, and the loss formulation (Eq. 5) may permit degenerate solutions. (4) Dataset limitations (BUSI: 99 training samples, HeadCT: highly imbalanced test set) undermine the generality of conclusions. (5) The prompts are trivial single-sentence descriptions (Table 4), providing no evidence for the claimed "interpretability and user interaction" benefits.

**External literature verification**: Not available in this run (Retrieval-Disabled Mode). Novelty conclusions relative to external literature are deferred for manual verification.

## Strengths
**S1 — Clinically motivated problem formulation.** The target task — universal anomaly detection across multiple organs and imaging modalities within a single network — addresses a real deployment bottleneck in medical AI. Current practice requires training and maintaining separate models per organ/modality, which is resource-intensive and prevents cross-domain knowledge transfer. The paper clearly motivates this problem.

**S2 — Clean ablation study design.** The ablation study (Table 2) decomposes the method into two components (hallucination quantification HQ and text prompting TP) and evaluates each variant individually. This provides clear attribution of which component contributes what gain. The +7.27% AUC from HQ and +3.35% AUC from TP are informative and support the design rationale.

**S3 — Comprehensive baseline coverage.** With 10 single-task baselines (AE, MemAE, CFLOW-AD, FastFlow, GAN Ensemble, CutPaste, NSA, MorphAEus, SQUID, EfficientAD) and 4 universal baselines (UniAD, HVQ-Trans, MADDR, HGAD), the experimental comparison is more extensive than typical for medical anomaly detection papers. All baselines use official implementations and default settings, ensuring fair comparison.

**S4 — Qualitative localization visualization.** Figures 10-13 provide side-by-side comparison of anomaly maps from competing methods (MemAE, NSA) and the proposed method, including separate visualization of the hallucination quantification map $u$. This helps the reader assess spatial behavior qualitatively and supports the claim that $u$ captures boundary artifacts.

**S5 — Open-source commitment.** The paper states code and data will be made publicly available, which supports reproducibility and community adoption.

## Weaknesses
**W1 — K=N finding invalidates MoE sparsity claim (Major).** Section 4.5.3 reports that optimal performance requires K=N (all 5 experts active). This means the TopK operation in Eq. (1) degenerates to a no-op, and the router functions as a weighted averaging ensemble rather than a sparse expert selection mechanism. The claimed benefits of conditional computation and specialized expert routing are not realized. The performance gain when increasing K from 1 to 5 may simply reflect increased parameter count, not routing efficiency.

**W2 — No statistical significance or variance reporting (Major).** All experiments report single point estimates without standard deviations, confidence intervals, or multi-seed averages (Table 1, 2, 3). With improvements of 1-3% AUC (e.g., RSNA: 83.51 vs 82.13), the reader cannot determine whether reported gains are statistically significant or within noise. The F1 and ACC metrics are computed with thresholds tuned on the test set, which inflates their values and makes them unsuitable for method comparison.

**W3 — Loss formulation (Eq. 5) may permit degenerate solutions (Major).** The term $e^{-u^2}$ decays rapidly: for $u > 2$, the reconstruction gradient nearly vanishes. The model could learn to set $u$ high for challenging textures (not only boundaries), effectively ignoring reconstruction errors for those pixels. No spatial regularization or bounded range is imposed on $u$. The hyperparameters $\alpha$ and $\beta$ in Eq. (6) are also not reported, making the total loss behavior opaque.

**W4 — Weak dataset foundation (Major).** BUSI uses only 99 training images, and HeadCT uses 90 training images with a heavily imbalanced test set (10 normal vs 100 abnormal). These datasets are too small to draw reliable conclusions. The dataset is compiled from existing public sources, not a novel clinical collection. No modality-specific preprocessing is described (e.g., CT windowing, MRI bias field correction).

**W5 — Overclaimed interpretability and SOTA statements (Moderate).** The abstract and conclusion claim "state-of-the-art performance" and "interpretability and user interaction" from natural language prompts. However, the prompts (Table 4) are trivial organ/modality labels. No interpretability experiment (attention analysis, user study, prompt perturbation test) is conducted.

**W6 — Supervised routing vs. standard MoE design (Moderate).** Eq. (4) trains the router via classification supervision against task category labels, rather than through reconstruction loss gradients as in standard MoE. This prevents the router from discovering cross-task synergies and may cause the K=N result — since the router is forced to match a fixed label, it never learns to suppress irrelevant experts entirely.

## Key Issues
**Issue 1: K=N result contradicts MoE motivation (Top Ranked)**
- **Severity**: Major | **Fixability**: Moderate
- **Evidence**: Page 9 — Section 4.5.3, Table 3. K=N=5 achieves best mean AUC 88.12 vs K=1 gets 85.31. All experts always active.
- **Root cause**: The router is trained via classification supervision (Eq. 4) against task labels rather than reconstruction loss gradients, so it never learns to suppress task-irrelevant experts.
- **Required fix**: (1) Compare against unsupervised routing (no L_rn, gating gradients through Eq. 2/5). (2) Add a matched-capacity single-decoder baseline to isolate capacity confound. (3) Report FLOPs for each K.
- **Expected impact**: Clarifies whether the method is truly a routing approach or an ensemble.

**Issue 2: No statistical rigor in experiments (Top Ranked)**
- **Severity**: Major | **Fixability**: High
- **Evidence**: Page 7 — Table 1, 2, 3. All metrics are point estimates without std/CI.
- **Root cause**: Single-seed runs; F1/ACC threshold tuned on test set.
- **Required fix**: Repeat all experiments ≥3 seeds; report mean±std; bootstrap AUC 95% CI; use validation set for threshold selection.
- **Expected impact**: Claims of improvement become verifiable.

**Issue 3: Eq. (5) loss may permit degenerate solutions (Top Ranked)**
- **Severity**: Major | **Fixability**: Moderate
- **Evidence**: Page 5 — Eq. (5). $e^{-u^2}$ decay, no bound on u, no spatial regularization.
- **Root cause**: The two-term loss can be minimized by pushing u large for any high-error region, not only boundaries.
- **Required fix**: (1) Visualize u maps and compute boundary-distance correlation. (2) Add spatial smoothness or bounded range on u. (3) Report α and β values.
- **Expected impact**: Validates the core technical claim about hallucination quantification.

**Issue 4: Overclaimed interpretability and SOTA**
- **Severity**: Moderate | **Fixability**: High
- **Evidence**: Abstract (Page 1), Conclusion (Page 10), Prompts (Page 13 Table 4).
- **Root cause**: Prompts are trivial organ/modality labels; no interpretability experiment.
- **Required fix**: Tone down SOTA/interpretability claims; add prompt perturbation test; bound claims to evaluated benchmarks.
- **Expected impact**: Scientific credibility and defensibility.

**Issue 5: Weak datasets undermine conclusions**
- **Severity**: Moderate | **Fixability**: Low (requires additional data)
- **Evidence**: Page 6 — BUSI: 99 training images; HeadCT: 90 training images, test 10 normal vs 100 abnormal.
- **Root cause**: Small-sample datasets adopted from prior work (Cai et al. 2022).
- **Required fix**: Report AUPRC for imbalanced sets; add confidence intervals; consider excluding or augmenting small datasets.
- **Expected impact**: More reliable benchmarking.

## Actionable Suggestions
### Suggestion 1 (Must) — Add statistical variance to all experiments
- **What**: Repeat all experiments (Table 1, 2, 3) with ≥3 random seeds. Report mean ± std for all metrics. Add bootstrapped 95% CI for AUC.
- **Where**: Page 7-9, all result tables.
- **Why**: Without variance, the 1-3% improvements claimed are unverifiable.
- **Effort**: Medium (compute time × 3).

### Suggestion 2 (Must) — Address K=N = MoE sparsity contradiction
- **What**: Add ablation comparing classification-supervised routing vs. reconstruction-gradient gating (standard MoE). Add a single decoder with matched parameter count as a control for K=N.
- **Where**: Page 9, Section 4.5.3.
- **Why**: The current K=N result invalidates the sparsity claim. If the method is actually an ensemble, it should be framed as such.
- **Effort**: Medium (additional training runs).

### Suggestion 3 (Must) — Report α, β and analyze u behavior
- **What**: Report the specific values of α and β used in Eq. (6). Add visual and quantitative analysis of u maps: correlation with boundary distance, distribution statistics, spatial smoothness.
- **Where**: Page 5-6, Section 3.4.
- **Why**: The loss formulation's behavior depends on the trade-off between the two terms. Without these values, the method is not reproducible.
- **Effort**: Low (already trained models exist; just report the values and analyze u outputs).

### Suggestion 4 (Must) — Bound SOTA and interpretability claims
- **What**: Replace "state-of-the-art" with "outperforms evaluated baselines under reported settings." Remove or substantially qualify the "interpretability and user interaction" claim unless new experiments are added.
- **Where**: Abstract (Page 1), Conclusion (Page 10).
- **Why**: The current claims exceed what the evidence supports.
- **Effort**: Low (text revision only).

### Suggestion 5 (Nice-to-have) — Expand prompts and test interpretability
- **What**: Add prompt perturbation experiments (misspelling, abbreviation, semantic equivalence). Optionally add attention visualization linking prompt tokens to spatial regions.
- **Where**: Page 13, Appendix A.
- **Why**: Validates the claimed prompt advantage beyond trivial organ/modality labels.
- **Effort**: Low-Medium (prompt perturbation requires only inference runs).

### Suggestion 6 (Nice-to-have) — Improve dataset documentation
- **What**: Add modality-specific preprocessing details (intensity normalization, CT windowing, MRI bias correction). Report AUPRC for imbalanced datasets.
- **Where**: Page 6, Section 4.1.
- **Why**: Reproducibility and fair cross-modal comparison.
- **Effort**: Low (documentation only).

## Storyline Options + Writing Outlines
### Current Storyline Analysis

The current Introduction has 3 paragraphs:
- **P1**: General ML success → annotation scarcity → prior methods (survey) → limitation: per-organ specialization → (implicit) need for universal model
- **P2**: Universal AD motivation → prior universal work → prompt advantage → interpretability claim → Figure 2 hallucination illustration
- **P3**: Method overview → hallucination-aware experts description → contribution list

**Problems**: (1) P1 is a dense citation list that buries the core motivation. (2) P2 introduces prompt advantage and interpretability without concrete evidence. (3) The structure does not cleanly follow Big Picture → Gap → Solution → Evidence → Contribution.

### Abstract Outline (Revised)

**S1 (Problem + Domain)**: "Unsupervised anomaly detection in medical imaging typically requires separate models per organ and imaging modality, preventing knowledge transfer and scalable deployment."

**S2 (Gap)**: "Existing universal anomaly detection frameworks rely solely on visual features to infer the target anatomy, missing the opportunity to leverage task-specific prior information available in clinical workflows."

**S3 (Solution)**: "We propose a prompt-driven mixture-of-experts framework that uses natural language prompts specifying organ and modality to route images to specialized decoder experts. The decoders jointly predict reconstruction and per-pixel hallucination scores to suppress false-positive boundary artifacts."

**S4 (Key Result)**: "On a compiled benchmark of 12,153 images across 5 modalities and 4 organs, our method outperforms 10 single-task and 4 universal baselines, with ablation studies confirming the contributions of both hallucination quantification and prompt conditioning."

**S5 (Impact + Availability)**: "Code and data will be released."

### Introduction Outline (Revised — 4 Paragraphs)

**P1 — Motivation and Gap (Revised)**:
- Role: Establish clinical stakes and concrete gap.
- Content: "Anomaly detection in medical images identifies abnormalities without requiring annotated examples, which is clinically valuable because labeled anomalies are scarce. However, current approaches train separate models for each organ and modality. This per-dataset specialization prevents knowledge transfer, causes redundant effort, and limits deployment scalability. A single universal model that can handle diverse organs and modalities would address these limitations."
- Evidence anchor: Reference Tschuchnig & Gadermayr (2022) for annotation scarcity; state that no existing method offers prompt-guided universal detection.

**P2 — Prior Universal AD and Prompt Advantage (Revised)**:
- Role: Summarize prior universal AD work; establish the specific limitation addressed.
- Content: "Recent work by You et al. (2022) and Zhang et al. (2023) introduced unified anomaly detection models for industrial and medical settings, respectively. However, these models identify the organ and modality purely from visual features (bottom-up). In clinical practice, imaging orders contain explicit anatomical information (e.g., 'Chest X-ray for lung evaluation') that the model could use as a top-down prior. Conditioning on such prompts could reduce ambiguity and allocate decoder capacity per task."
- Evidence anchor: Cite Zhang et al. (2023), You et al. (2022).

**P3 — Hallucination Problem and Proposed Solution (Revised)**:
- Role: Introduce the boundary false-positive issue and the proposed remedy.
- Content: "A known but under-addressed issue in reconstruction-based anomaly detection is that detectors produce high errors not only at true anomalies but also at normal-region boundaries, causing false positives. We term this 'hallucinatory anomaly.' To address it, we design decoder experts that output both a reconstruction $\mu_k$ and a per-pixel hallucination score $\sigma_k$. The loss function (Eq. 5) jointly learns to reconstruct and to attribute boundary errors to hallucination, so that at inference the corrected anomaly map suppresses false positives."
- Evidence anchor: Figure 2, Eq. (5).

**P4 — Method Overview and Contributions (Revised)**:
- Role: Brief architecture summary + contribution list.
- Content: "Our framework (Fig. 3) comprises a shared vision encoder, a CLIP-based text encoder, a routing network, and multiple hallucination-aware decoders. The contributions are: (C1) a prompt-guided universal AD setting with a compiled multi-modal multi-organ benchmark, (C2) a hallucination-aware MoE framework with joint reconstruction and false-positive suppression, (C3) comprehensive benchmarking against 14 baselines with ablation analysis."

### Title Option

**Current**: "ALL-IN-ONE: PROMPT-DRIVEN MIXTURE OF HALLUCINATION-AWARE EXPERTS FOR UNIVERSAL ANOMALY DETECTION ACROSS MULTI-MODAL MULTI-ORGAN MEDICAL IMAGES"
**Revised**: "Prompt-Driven Mixture of Experts with Hallucination-Aware Decoders for Universal Medical Anomaly Detection"

## Priority Revision Plan
### P0 — Publication-Critical (Must Fix Before Acceptance)

| # | Issue | Action | Expected Impact |
|---|-------|--------|-----------------|
| P0.1 | No variance/statistical reporting | Repeat all experiments ≥3 seeds; report mean±std; add 95% CI for AUC | Claims become empirically verifiable |
| P0.2 | K=N contradicts MoE sparsity | Add unsupervised routing ablation + matched-capacity single-decoder baseline | Clarifies whether the approach is MoE or ensemble |
| P0.3 | Eq. (5) degenerate solution risk | Report α, β values; visualize u maps; add boundary-distance correlation analysis | Validates the core hallucination mechanism |
| P0.4 | Overclaimed SOTA/interpretability | Replace "SOTA" with bounded wording; remove or qualify interpretability claim | Restores scientific credibility |

### P1 — High Priority (Should Fix)

| # | Issue | Action | Expected Impact |
|---|-------|--------|-----------------|
| P1.1 | Weak dataset documentation | Add modality-specific preprocessing; report AUPRC for imbalanced sets | Improves reproducibility and evaluation fairness |
| P1.2 | Supervised routing (Eq. 4) | Add comparison against reconstruction-gradient-based routing | Tests whether routing is learning useful specialization |
| P1.3 | Missing hyperparameter reporting | Report α, β, learning rate schedule, weight decay, batch norm settings | Allows reproducibility |

### P2 — Quality Improvement (Nice to Fix)

| # | Issue | Action | Expected Impact |
|---|-------|--------|-----------------|
| P2.1 | Trivial prompts only (Table 4) | Add prompt perturbation tests | Validates prompt benefit beyond label encoding |
| P2.2 | Title formatting | Shorten and fix hyphenation | Clean presentation |
| P2.3 | Related work as flat survey | Restructure by comparison axes | Stronger positioning |

### Revision Sequence (Recommended Order)

```
Week 1: P0.4 (text revisions) + P0.1 (start multi-seed runs)
Week 2: P0.2 (routing ablation experiments) + P0.3 (analyze u maps)
Week 3: P1.1 (dataset documentation) + P1.2 (routing comparison)
Week 4: P1.3 (hyperparameter reporting) + Final manuscript polish
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|----------------|-------------------|
| E1 — Main Comparison (Table 1) | Evaluate overall AD performance vs 14 baselines | 5 datasets, 10 single-task + 4 universal baselines | AUC, F1, ACC | Ours best on 4/5 AUC, all F1/ACC | C3 (benchmarking) | No variance, single-seed |
| E2 — HQ Ablation (Table 2) | Measure hallucination quantification impact | Ours w/o HQ vs w/ HQ | AUC, F1, ACC | +7.27% mean AUC | C2 (hallucination-aware) | No u map quality metric |
| E3 — TP Ablation (Table 2) | Measure text prompting impact | Ours w/o TP vs w/ TP | AUC, F1, ACC | +3.35% mean AUC | C1 (prompt-guided) | Trivial prompts only |
| E4 — K sensitivity (Table 3) | Analyze routing sparsity impact | K=1..5 with N=5 | AUC, F1, ACC | K=N=5 optimal | C2 (MoE routing) | Contradicts sparsity claim |
| E5 — Qualitative localization (Fig 10-13) | Visual anomaly map comparison | MemAE, NSA, Ours on all datasets | Visual comparison | Ours reduces boundary FPs | C2 (hallucination) | No quantitative localization metric |
| E6 — t-SNE (Fig 9) | Feature distribution separation | Prompt-less vs full model | Visual | Full model separates better | C1 (prompt advantage) | No quantitative metric |

### Research-Theme Gap Diagnosis

- **New knowledge**: The hallucination quantification mechanism is novel, but its formulation (Eq. 5) needs deeper validation to confirm it captures boundary artifacts rather than general uncertainty.
- **Reproducibility**: Major gaps — no α/β values, no multi-seed runs, no data preprocessing details, CLIP encoder frozen/fine-tuned unspecified.
- **Impact on practice**: The universal setting is practical, but the small training sets (BUSI=99, HeadCT=90) and lack of OOD evaluation limit deployment readiness claims.

### Proposed Research Experiments

**P0 — Statistical Validation (Must)**
- **Target Claim**: All C1-C3 (any claimed improvement)
- **Hypothesis**: Reported gains are statistically significant
- **Design**: Repeat Table 1, 2, 3 with 3 random seeds, report mean ± std
- **Controls**: Same hyperparameters, same data splits
- **Metrics**: AUC (with 95% CI via bootstrap), F1, ACC
- **Success Criterion**: 95% CI does not overlap with best baseline AUC
- **Cost**: ~3× current compute
- **Expected Gain**: Verifiable claims, essential for acceptance

**P0 — Routing Design Ablation (Must)**
- **Target Claim**: C2 (MoE routing effectiveness)
- **Hypothesis**: Reconstruction-gradient-based routing outperforms classification-supervised routing
- **Design**: Compare (a) current supervised routing (Eq. 4), (b) unsupervised routing (no L_rn, gating gradients via Eq. 2/5), (c) single expert with matched total capacity
- **Controls**: All other components identical
- **Metrics**: AUC across all datasets
- **Success Criterion**: Unsupervised routing achieves comparable or better AUC with K<N
- **Cost**: ~5 additional training runs
- **Expected Gain**: Clarifies MoE vs ensemble contribution

**P1 — Hallucination Map Validation (Should)**
- **Target Claim**: C2 (u captures boundary artifacts)
- **Hypothesis**: u values correlate with distance to nearest organ boundary
- **Design**: On normal test images, compute u map, compute distance transform to organ boundary (or strong gradient mask using Sobel/Canny), report Pearson/Spearman correlation
- **Controls**: Compare against random spatial patterns and constant u
- **Metrics**: Mean correlation coefficient per dataset
- **Success Criterion**: Significant positive correlation (p<0.01)
- **Cost**: Low (requires only inference on existing model)
- **Expected Gain**: Direct evidence for the core technical claim

**P1 — Prompt Perturbation Test (Should)**
- **Target Claim**: C1 (prompt-guided advantage)
- **Hypothesis**: The model benefits from prompts beyond simple organ name encoding
- **Design**: Test with (a) correct prompt, (b) no prompt (empty string), (c) wrong organ prompt, (d) synonym prompt, (e) misspelled prompt
- **Controls**: Compare AUC drops
- **Metrics**: AUC per prompt variant
- **Success Criterion**: Correct prompt outperforms no-prompt; wrong prompt degrades performance significantly
- **Cost**: Low (inference-only)
- **Expected Gain**: Validates the interpretability/prompt advantage claim

**P1 — Loss Stability Analysis (Should)**
- **Target Claim**: C2 (loss formulation is well-behaved)
- **Hypothesis**: u values converge to stable, interpretable values
- **Design**: Track u mean, std, max, and spatial entropy across training epochs. Report final u distribution histograms per dataset
- **Controls**: Training without L_re's u^2 term (u only)
- **Metrics**: Convergence plots, final distribution statistics
- **Success Criterion**: u converges to consistent values without oscillation or collapse
- **Cost**: Low (logging from existing training runs)
- **Expected Gain**: Demonstrates training stability

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 5.5/10**

This score reflects the following assessment, prioritizing research value and novelty:
- **Research value**: The universal multi-organ multi-modal AD task is practically motivated (addresses a real deployment gap). The hallucination-aware decoder is a technically sound idea for boundary false-positive reduction. **Score contribution: +3.0**
- **Novelty**: The core components (prompt-guided MoE for medical AD, hallucination-aware decoders) are novel in combination, though individual elements (autoencoder AD, MoE routing, CLIP conditioning) are established techniques. The K=N finding weakens the novelty of the MoE routing contribution. External novelty verification is deferred. **Score contribution: +1.5**
- **Validity/Soundness**: Major validity concerns — no statistical variance, possible degenerate solutions in Eq. (5), K=N contradicts sparsity claim. The experiments lack the rigor needed to support the stated claims. **Score contribution: -1.5** (starting from neutral)
- **Reproducibility**: Several unreported details (α, β values, CLIP encoder training status, data preprocessing specifics, weight initialization) reduce reproducibility. Code/data release commitment is positive. **Score contribution: -0.5**
- **Presentation**: Generally clear writing, good figures. Title has formatting artifacts. Related work is flat rather than structured. Overclaiming in abstract and conclusion. **Score contribution: -0.0** (neutral, based on net good/weak balance)

**Post-Revision Target: [6.5, 7.5]/10**

This target assumes the following critical revisions are fully addressed:
- Multi-seed experiments with variance reporting (+0.5)
- Resolution of K=N issue (routing ablation or honest reframing as ensemble) (+0.5)
- Eq. (5) loss validation (u map analysis + hyperparameter reporting) (+0.3)
- Bounded SOTA/interpretability claims (+0.3)
- Expanded dataset documentation and AUPRC for imbalanced sets (+0.2)

If all P0 and P1 items are addressed, the paper could reach a score of 6.5-7.5, placing it in the acceptable-to-solid range. Without addressing P0.1-P0.4, the validity concerns remain unresolved and the score would stay at 5.5 or lower.