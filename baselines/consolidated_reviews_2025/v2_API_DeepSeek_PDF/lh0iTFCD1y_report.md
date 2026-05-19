## Summary
# Final Review Report

## Summary

This paper presents LUMA, a multimodal benchmark dataset (image, audio, text) designed for evaluating uncertainty quantification (UQ) methods. LUMA extends CIFAR-10/100 with audio samples from three speech corpora (Spoken Wikipedia, LibriSpeech, Common Voice) and LLM-generated text descriptions (via Gemma-7B). The key claimed contributions are (C1) the dataset itself with 42 in-distribution classes and 8 OOD classes, (C2) a Python package for controlled injection of four uncertainty types (data diversity, sample noise, label noise, OOD), and (C3) baseline models using three UQ methods (Monte Carlo Dropout, Deep Ensemble, Reliable Conflictive Multi-View Learning).

**Strengths:** The paper addresses a genuine need — multimodal UQ benchmarking currently lacks datasets with controllable per-modality uncertainty. The audio data collection process is thorough (three corpora, forced alignment, automatic + manual validation). The bias analysis for LLM-generated text is a commendable addition. The Python toolkit abstraction is practical and reusable.

**Key weaknesses:** (1) Critical lack of variance reporting — baseline results (Table 1) are single-run point estimates without standard deviations or significance tests. (2) The diversity formula (Eq. 1) has ambiguous notation and misses the normalization step needed for categorical sampling. (3) The text validation pipeline uses the same model (Gemma-7B) for both generation and validation, creating circular evaluation. (4) Conclusion omits any limitations section despite several important caveats (synthetic EDM images, residual text biases, restricted class count). (5) Section 2 (related work) is unstructured — it lists datasets without a comparison table or taxonomy. (6) Novelty claims cannot be fully assessed in this run (external retrieval disabled), so they are deferred for manual verification.

**Overall assessment:** LUMA is a potentially useful resource for the MUQ community, but the manuscript in its current form lacks the experimental rigor (no variance, limited baselines) and structured positioning (no related-work comparison table, no limitations) expected of a benchmark dataset paper at a top venue. With substantial revision — especially variance reporting, formula corrections, circular validation fixes, and a dedicated limitations section — the paper could become a solid contribution.

## Strengths
1. **Addresses a genuine gap in the MUQ benchmarking landscape.** Current multimodal UQ datasets (CUB, HandWritten, Scene15, Caltech101) repurpose unimodal data and add only Gaussian noise. LUMA's controlled injection of diversity, sample noise, label noise, and OOD samples across three independently sourced modalities fills a clear unmet need. The Python toolkit abstraction is practical and lowers the barrier for MUQ researchers to design controlled experiments.

2. **Thorough audio data collection pipeline.** The authors mine three major speech corpora (Spoken Wikipedia, LibriSpeech, Common Voice), use forced alignment for word-level extraction, and implement a two-stage validation pipeline (automatic Whisper-based transcription + manual verification by 17 annotators with 71.61% agreement). This level of detail is commendable and provides transparency for future users.

3. **Bias analysis and mitigation for LLM-generated text.** The paper goes beyond simple text generation by systematically identifying gender bias in 4 classes (man, woman, boy, girl), reconstructing prompts with keyword constraints, re-running bias detection, and filtering biased samples. This represents a good-faith effort to address a known LLM limitation, and the candid disclosure (including examples of biased texts) is scientifically responsible.

4. **Clean and reproducible dataset packaging.** The dataset is available with clear licensing (CC BY-SA 4.0 for data, GPL-3.0 for code), and the compilation pipeline is fully scripted, enabling users to generate custom variants with different noise configurations. The choice of well-known CIFAR imagery simplifies baseline setup for most computer vision researchers.

5. **Interesting empirical finding about MCD/DE OOD detection failure.** The paper reports that MCD and Deep Ensemble methods achieve near-chance OOD detection AUC (~0.50) on LUMA, while RCML reaches 0.91. This negative result is scientifically valuable — it demonstrates that common UQ methods can fail on multimodal data and motivates the need for the benchmark.

## Weaknesses
1. **No variance reporting on baseline results (Critical).** Table 1 reports single-run uncertainty estimates for MCD, DE, and RCML without standard deviations, confidence intervals, or significance tests. This is particularly problematic because MCD and DE are inherently stochastic methods — MCD averages multiple stochastic forward passes, and DE averages across ensemble members — so the numbers should naturally have measurable variance. Without this information, the observed changes (e.g., DE Image -7.43% aleatoric under label noise) cannot be assessed for statistical reliability. This undermines the paper's value as a benchmark reference.

2. **Missing structured related-work comparison (Major).** Section 2 ("Limitations of Current Datasets") is written as a narrative critique rather than a proper related-work section with a taxonomy or comparison table. Key dimensions (number of modalities, class count, noise types, uncertainty controllability, OOD splits, code availability) are not tabulated. Readers cannot quickly compare LUMA against existing datasets. This is a significant omission for a dataset paper.

3. **Diversity formula (Eq. 1) has unresolved mathematical issues (Major).** The notation $\|\cdot\|_2^k$ is ambiguous (should be $(\|\cdot\|_2)^k$). The equation does not include normalization to convert $D_i$ into sampling probabilities, and there is no numerical stability mechanism for the case when $F_i$ equals the class centroid exactly. These issues could affect reproducibility.

4. **Circular text validation pipeline (Major).** The text modality uses Gemma-7B both to generate the text and to validate it (by masking labels and re-classifying). This creates a self-confirming loop — the validator may succeed because it shares the same training distribution and biases, not because the text is genuinely descriptive. Bias detection also uses Gemma-7B, compounding the circularity concern.

5. **No dedicated limitations section (Major).** The 4-sentence conclusion does not mention any limitations despite several important caveats: synthetic EDM images (which may not reflect real-world visual characteristics), residual text bias (acknowledged but not quantified in the final dataset), audio restricted to single-word pronunciation, the limited class count (42 in-distribution), and the use of simple baseline architectures.

6. **Introduction narrative could be sharper (Moderate).** The first two introduction paragraphs are generic (MDL benefits, UQ importance) without establishing a multimodal-specific gap. The aleatoric/epistemic background paragraph (P3) is textbook content that delays the paper's original contribution. The actual gap statement (current datasets cannot control per-modality uncertainty) appears in the second half of Page 2 — too late for maintaining reader engagement.

7. **EDM synthetic images without caveats (Moderate).** The image modality supplements CIFAR-100 with diffusion-generated synthetic images to reach 600 samples per class. This is not discussed as a limitation, yet synthetic images may have different distributional and uncertainty properties than real photographs. Users benchmarking on LUMA's image modality may get results that do not transfer to real data.

8. **Conclusion is too brief (Moderate).** The conclusion is only 4 sentences and does not summarize quantitative findings (e.g., RCML AUC = 0.91, image baseline accuracy ~34%). It makes an unsubstantiated claim ("easily extended with additional modalities") without providing API documentation or code examples.

9. **Novelty assessment deferred (Moderate).** External literature retrieval was not available in this run. Claims of "unique" (Abstract) and related positioning against prior MUQ datasets could not be independently verified. This is noted as a deferred judgment for manual review.

## Key Issues
### Issue 1 (Critical): No variance reporting — baseline results are single-run point estimates
**Location:** Page 9 — Section 4.3 Results, Table 1
**Risk:** Invalidates the benchmark reference value of the paper
**Evidence:** Table 1 reports absolute uncertainty values and percentage changes without any standard deviation, confidence interval, or significance test. The MCD method inherently involves stochastic dropout sampling; DE averages across 10 networks — both should exhibit measurable variance across repetitions.
**Fix:** Re-run all experiments with 3-5 random seeds. Report mean ± std for all entries. Add a paired significance test (e.g., paired t-test or Wilcoxon) comparing noisy vs clean conditions.

### Issue 2 (Major): Diversity formula (Eq. 1) lacks normalization and numerical stability
**Location:** Page 6-7 — Section 3.4 Data Diversity, Eq. (1)
**Risk:** Reproducibility failure
**Evidence:** $D_i$ as defined is an inverse-distance score, not a probability. The text says "sample points from categorical distribution $x_n \sim \text{Categorical}(D)$" but provides no normalization step. Also, $\|\cdot\|_2^k$ is ambiguous notation — should be $(\|\cdot\|_2)^k$.
**Fix:** Add explicit normalization $p_i = D_i / \sum_{j \in C} D_j$, add numerical stability epsilon, and use standard notation $(\|\cdot\|_2)^k$.

### Issue 3 (Major): Circular text validation pipeline
**Location:** Page 5 — Section 3.3 Text Modality
**Risk:** Validation quality is unverifiable
**Evidence:** Gemma-7B is used both to generate text and to validate it (by masking the label and re-classifying). The same model is also used for bias detection. This creates circular dependencies.
**Fix:** Use an independent classifier (e.g., fine-tuned BERT or a different LLM) for validation. Use a dedicated bias-detection model. Report per-class residual bias rates in the final dataset.

### Issue 4 (Major): No limitations section
**Location:** Page 10 — Section 5 Conclusion
**Risk:** Reduces scientific credibility
**Evidence:** The 4-sentence conclusion lists no limitations despite synthetic images, residual text biases, restricted class count, and weak image baselines.
**Fix:** Add a dedicated limitations paragraph covering: (a) synthetic EDM images affecting real-world transfer, (b) residual text biases, (c) single-word audio only, (d) 42 in-distribution class limit, (e) simple baseline architectures.

### Issue 5 (Major): Section 2 is unstructured related work
**Location:** Page 2-3 — Section 2 Limitations of Current Datasets
**Risk:** Weak positioning of contribution
**Evidence:** The section lists datasets (HandWritten, CUB, Scene15, Caltech101) without a comparison table. The gap analysis is narrative rather than structured.
**Fix:** Add a comparison table with columns: Dataset | Modalities | Size | Uncertainty Control | Noise Types | OOD Splits | Code Availability. Reorganize around comparison axes.

## Actionable Suggestions
### S1 (Must): Add multi-seed variance to all baseline results
Replace Table 1 with mean ± std over 3-5 random seeds. Also add a column showing whether the uncertainty change from clean to noisy condition is statistically significant (e.g., paired t-test p < 0.05). This is **non-negotiable** for a benchmark dataset paper.

### S2 (Must): Fix diversity formula (Eq. 1)
Replace Eq. (1) with:
$$D_i = \frac{1}{\|F_i - \mu_C\|_2^k + \epsilon}, \quad \mu_C = \frac{1}{|C|}\sum_{j \in C}F_j, \quad i \in C$$
and add: "Sampling probabilities are then $p_i = D_i / \sum_{j \in C} D_j$." Add $\epsilon = 10^{-8}$ for numerical stability.

### S3 (Must): Fix circular text validation
Replace the Gemma-based text validation with an independent classifier (e.g., fine-tuned BERT or DistilBERT trained on CIFAR-100 label descriptions). Use a separate bias-detection API or model. Report residual bias percentages per class in the main text.

### S4 (Must): Add a dedicated limitations section
Insert after the conclusion (or merge into it) a paragraph covering: (a) synthetic EDM images may not reflect real-world visual uncertainty characteristics; (b) residual gender bias in text for 4 classes despite mitigation; (c) audio is limited to single-word pronunciations, not natural speech; (d) only 42 in-distribution classes; (e) baseline models use simple architectures; (f) only 3 UQ methods are benchmarked.

### S5 (Must): Reorganize Section 2 as a structured related work with comparison table
Add a table comparing LUMA against HandWritten, CUB, Scene15, Caltech101, and any other relevant MUQ datasets across: modalities, classes, total samples, uncertainty control dimensions (diversity/sample noise/label noise/OOD), code availability, and license.

### S6 (Nice-to-have): Improve introduction narrative
Restructure the introduction to follow: (P1) concrete multimodal-specific UQ challenge (not generic MDL benefits), (P2) why current datasets cannot address it, (P3) brief aleatoric/epistemic background (1 sentence), (P4) LUMA proposal with contribution list. This would front-load the gap and solution.

### S7 (Nice-to-have): Add accuracy-uncertainty joint analysis in main text
Move Table 4 (classification accuracies) from appendix into the main results section and add a paragraph analyzing the accuracy-uncertainty trade-off across methods and noise conditions.

### S8 (Nice-to-have): Add EDM image subset analysis
Report classification accuracy and uncertainty on real CIFAR vs EDM-synthetic images separately to quantify the distributional shift introduced by synthetic data.

### S9 (Nice-to-have): Fix typos and minor writing issues
- "uncertainly" → "uncertainty" (Page 2, contribution 3)
- "as as" → "as" (Page 8, line 100)
- "a lots of" → "a lot of" or "substantial" (Page 5, line 104)
- "consitently" → "consistently" (Page 10, line 65)

## Storyline Options + Writing Outlines
### Current Storyline Analysis
The introduction currently follows: (P1) MDL is important → (P2) trustworthiness and UQ are important → (P3) aleatoric/epistemic definitions → (P4) MUQ is new but current datasets lack controlled injection → (C1-C3 list). The problem: the reader has to wait until P4 (bottom of Page 2) to understand the concrete gap. P1 and P3 do not advance a multimodal-specific argument.

### Recommended Storyline (Best Candidate)
A tighter, gap-forward structure:

**Abstract (S1-S5):**
- S1: Problem — Multimodal deep learning models need reliable uncertainty quantification for safety-critical deployment.
- S2: Challenge — Evaluating MUQ methods requires datasets where per-modality uncertainty can be independently controlled and ground-truth known.
- S3: Gap — Existing MUQ benchmarks (CUB, HandWritten, Scene15) re-purpose unimodal data and add only Gaussian noise, lacking per-modality control.
- S4: Solution — We introduce LUMA, a multimodal benchmark (image, audio, text, 42 classes) with a Python toolkit for controlled injection of diversity, sample noise, label noise, and OOD samples.
- S5: Key finding + implication — Baselines with 3 UQ methods reveal that MCD/DE achieve near-chance OOD detection (AUC ~0.50) while RCML reaches 0.91, demonstrating the need for this benchmark.

**Introduction (P1-P4):**
- P1: Concrete multimodal-specific UQ challenge. *Example opening: "When diagnosing a patient, a doctor integrates MRI scans (image), patient history (text), and heart sounds (audio). Each modality has its own noise characteristics, and the model must distinguish aleatoric uncertainty (e.g., noisy MRI) from epistemic uncertainty (e.g., missing patient history). Current UQ methods are primarily designed and tested on unimodal data; extending them to multimodal settings is an open problem because uncertainty sources interact in complex ways."*
- P2: Gap in current benchmarks. *"Evaluating MUQ methods requires datasets where per-modality uncertainties can be independently injected and controlled. However, existing MUQ datasets [citations] either repurpose unimodal features or add only global Gaussian noise — they cannot independently control diversity, sample noise, label noise, and OOD exposure per modality."*
- P3: Brief background on aleatoric/epistemic uncertainty (compress to 1-2 sentences with citation).
- P4: LUMA proposal. *"To address this gap, we introduce LUMA..."* followed by the contribution list.

### Revised Title Suggestion
Current: "LUMA: A Benchmark Dataset for Learning from Uncertain and Multimodal Data"
Improved: "LUMA: A Controllable Multimodal Benchmark for Evaluating Uncertainty Quantification under Per-Modality Noise, Diversity Shifts, and OOD Exposure"

This title is longer but more informative — it tells the reader what LUMA enables (controlled per-modality evaluation) rather than just stating it is a benchmark.

### Paragraph-by-Paragraph Rewrite Guidance

**Abstract rewrite (copy-ready):**
Multimodal deep learning models require reliable uncertainty quantification (UQ) for safe deployment in healthcare, autonomous driving, and other high-stakes domains. Evaluating UQ methods in multimodal settings demands datasets where per-modality uncertainty sources — noise, diversity, label ambiguity, and out-of-distribution (OOD) samples — can be independently controlled. Existing multimodal UQ benchmarks reuse unimodal datasets with simple Gaussian perturbations, lacking such control. We present LUMA, a multimodal dataset with 101K images (CIFAR-10/100 + synthetic augmentations), 135K audio samples (three speech corpora), and 63K text passages (LLM-generated), across 42 in-distribution and 8 OOD classes. A companion Python toolkit enables controlled injection of data diversity reduction, per-modality sample noise, label noise, and OOD samples. Baseline experiments with Monte Carlo Dropout, Deep Ensemble, and Reliable Conflictive Multi-View Learning reveal that MCD and DE achieve near-chance OOD detection (AUC ~0.50) while RCML reaches 0.91, underscoring the need for systematic MUQ benchmarking. LUMA is released under open licenses to support community-driven UQ research.

**Revision of P1 Introduction (copy-ready):**
"Deploying multimodal deep learning in safety-critical applications — such as medical diagnosis from imaging and clinical notes, or autonomous driving from camera and LiDAR — requires models that not only achieve high accuracy but also reliably quantify their uncertainty. In these settings, each modality carries its own noise characteristics: an X-ray may be blurry (aleatoric), while text notes may be missing for certain patient subgroups (epistemic). Extending uncertainty quantification from unimodal to multimodal settings is challenging because uncertainties can interact — conflicting modalities may increase overall uncertainty while redundant ones may mask it. Despite progress in unimodal UQ, multimodal UQ (MUQ) remains under-explored, partly due to the lack of benchmarks where per-modality uncertainty can be independently controlled."

**Revision of P2 Introduction (copy-ready):**
"Several datasets have been used in MUQ research, including HandWritten (multi-feature), CUB (image+captions), Scene15, and Caltech101. While valuable, these datasets share two limitations. First, they repurpose unimodal data by extracting different feature sets, rather than providing inherently multimodal observations with independent noise sources. Second, existing MUQ studies introduce uncertainty by adding Gaussian noise globally to features or views [citations], without the ability to control different uncertainty types (aleatoric vs. epistemic) separately per modality. A benchmark that supports independent, controllable injection of multiple uncertainty types across modalities is needed to systematically diagnose how UQ methods behave under each condition."

## Priority Revision Plan
| Priority | Task | Effort | Impact | Section Affected | Annotation |
|----------|------|--------|--------|------------------|------------|
| **P0** | Add multi-seed variance to all baseline results (mean ± std, 3-5 seeds) | Medium (re-run experiments) | Critical — benchmark credibility | Section 4.3, Table 1 | #d63da20e |
| **P0** | Fix Eq. (1): add normalization, epsilon, correct notation | Low (text + LaTeX edit) | High — reproducibility | Section 3.4, Eq. (1) | #103e2810 |
| **P0** | Replace circular text validation with independent classifier | Medium (re-run text validation) | High — validation integrity | Section 3.3 | #37deb059 |
| **P0** | Add dedicated limitations section | Low (writing) | High — scientific credibility | Section 5 | #03a72bcb |
| **P1** | Reorganize Section 2 with comparison table | Low-Medium (writing + formatting) | High — positioning clarity | Section 2 | #5599d7df |
| **P1** | Fix C2 overclaim ("effectively increase") | Low (1 sentence) | Medium — defensive writing | Page 2, Contributions | #81c019d8 |
| **P1** | Add RCML uncertainty metric derivation details | Low (text) | Medium — reproducibility | Section 4.2, Eq. (2) | #73515bb2 |
| **P2** | Restructure introduction narrative (P1-P4) | Medium (rewrite) | Medium — reader engagement | Section 1 | #497fce22, #df2d0a79 |
| **P2** | Add EDM image subset analysis | Medium (re-run) | Medium — transparency | Section 3.1 / Appendix | #3a2c953f |
| **P2** | Move accuracy table to main text + trade-off analysis | Low (move text) | Medium — completeness | Section 4.3 | #d63da20e |
| **P2** | Typo fixes | Very low | Minor — polish | Multiple | Multiple |

### Revision Strategy Summary
- **Phase 1 (immediate, ~1 week):** Fix P0 items — re-run baselines with seeds, fix formula, fix circular validation, add limitations. These are the most reviewer-visible issues.
- **Phase 2 (before resubmission, ~1 week):** Restructure Section 2, fix overclaims, add RCML derivation details, move accuracy table.
- **Phase 3 (polish, ~2 days):** Introduction rewrite, EDM analysis, typo fixes.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective / Hypothesis | Setup (data/split/protocol/baselines) | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|----------------------|--------------------------------------|---------|--------------|-----------------|-------------------|
| E1 | Evaluate UQ baselines on clean LUMA data | 42 classes, 500 train / 100 test per class; MCD, DE, RCML on image/audio/text/multimodal | Aleatoric uncertainty, Epistemic uncertainty, Accuracy | Clean multimodal accuracy: MCD 99.1%, DE 99.6%, RCML 97.3% | Baseline feasibility | Accuracy for image-only model is very low (33.5-38.7%) — suggests architecture is too weak |
| E2 | Evaluate UQ under reduced diversity (k=20) | Same as E1 with diversity parameter k=20 | % change in Ale./Epi. uncertainty; Δ Accuracy | Uncertainty generally decreases under reduced diversity for MCD/DE (counter to hypothesis) | C2: diversity control affects uncertainty | No explanation for counter-hypothetical behavior |
| E3 | Evaluate UQ under increased label noise (30% switch) | Same as E1 with 30% label switching to nearest class | % change in Ale./Epi. uncertainty; Δ Accuracy | Uncertainty increases consistently for RCML; mixed for MCD/DE (DE Image Ale. decreases -7.43%) | C2: label noise injection works for most cases | DE Image contradictory behavior unexplained; no variance reported |
| E4 | Evaluate UQ under increased sample noise | Per-modality noise: audio (ESC-50 bg, SNR 3-5), image (15 corruptions), text (keyboard/spelling/back-translation) | % change in Ale./Epi. uncertainty; Δ Accuracy | Uncertainty generally increases; multimodal MCD Ale. +59.14%, DE +45.97% | C2: sample noise injection works | No per-modality ablation of noise severity levels |
| E5 | OOD detection via epistemic uncertainty | 8 held-out classes as OOD; AUC score | AUC | MCD/DE ~0.50 (near chance), RCML 0.91 | C3: RCML suitable for OOD detection | No comparison with other OOD detection methods (Mahalanobis, ODIN, etc.) |

### Research-Theme Gap Diagnosis

- **New knowledge:** The paper provides a new dataset and initial baselines, but the empirical contribution is weakened by the lack of variance reporting and the absence of a dedicated analysis of why MCD/DE fail at OOD detection on LUMA. The most interesting finding (DE image uncertainty decreases under label noise) is not explained.
- **Reproducibility/reusability:** The Python package and dataset are positive steps. However, incomplete formula definitions (Eq. 1, Eq. 2) and circular validation pipeline reduce reproducibility.
- **Potential to change practice/understanding:** If the paper can demonstrate that per-modality controlled injection reveals systematic failure modes of standard UQ methods (as hinted by the DE anomaly and MCD/DE AUC ~0.50), it could influence how MUQ methods are evaluated. Currently this potential is underexploited.

### Proposed Research Experiments (P0/P1/P2)

**P0-Exp1: Multi-seed variance and significance analysis**
- **Target Claim:** All baseline results (Table 1)
- **Hypothesis:** Observed uncertainty changes will show substantial seed-to-seed variation, and some changes currently reported as meaningful will not reach statistical significance
- **Minimal Design:** Re-run all conditions (clean, reduced diversity, label noise, sample noise) for 5 random seeds
- **Controls/Baselines:** Fix all hyperparameters across seeds; use the same train/validation splits
- **Metrics:** Mean ± std of aleatoric/epistemic uncertainty and accuracy; paired t-test p-value for noisy vs clean comparison
- **Success Criterion:** At least 3 of 5 seeds produce consistent directional changes; p < 0.05 for reported effects
- **Estimated Cost:** ~50 GPU-hours (10 methods × 4 conditions × 5 seeds × ~15 min per run)
- **Expected Gain:** Transforms baseline from unverifiable to reference-quality

**P0-Exp2: Independent text validation**
- **Target Claim:** Text modality is valid (Section 3.3)
- **Hypothesis:** An independent classifier (fine-tuned BERT) will agree with Gemma-based validation at a rate significantly above chance, establishing external validity
- **Minimal Design:** Fine-tune BERT-base on the 42-class text classification task using LUMA training split; evaluate on held-out test set; compare accuracy with Gemma-based self-validation accuracy
- **Controls/Baselines:** Use identical train/test splits as Gemma validation
- **Metrics:** Classification accuracy, confusion matrix per class, agreement rate with Gemma validation
- **Success Criterion:** BERT accuracy > 85% on held-out test set (comparable to Gemma self-validation)
- **Estimated Cost:** ~5 GPU-hours
- **Expected Gain:** Replaces circular validation with independently verifiable quality metric

**P0-Exp3: Formula sensitivity analysis for diversity control**
- **Target Claim:** Diversity parameter k controls epistemic uncertainty (Section 3.4)
- **Hypothesis:** Adding explicit normalization and epsilon to Eq. (1) will produce consistent monotonic changes in epistemic uncertainty across k values
- **Minimal Design:** Implement corrected formula; evaluate MCD multimodal at k = {0, 5, 10, 15, 20, 30}; measure epistemic uncertainty and accuracy
- **Controls/Baselines:** Compare with original (unnormalized) implementation
- **Metrics:** Epistemic uncertainty vs k (monotonic trend expected), classification accuracy
- **Success Criterion:** Epistemic uncertainty shows monotonic increase with k (current results show decreases)
- **Estimated Cost:** ~10 GPU-hours
- **Expected Gain:** Validates the core diversity control mechanism and resolves the counter-hypothetical observation

**P1-Exp4: EDM vs real image subset analysis**
- **Target Claim:** Image modality represents real visual data (Section 3.1)
- **Hypothesis:** Classification accuracy and aleatoric uncertainty differ significantly between real CIFAR and EDM-synthetic images
- **Minimal Design:** Split image test set into real-CIFAR and EDM-synthetic subsets; evaluate MCD and DE on each subset separately; report accuracy and uncertainty per subset
- **Controls/Baselines:** Same model, same hyperparameters
- **Metrics:** Per-subset accuracy, aleatoric uncertainty, distributional distance (e.g., FID between subsets)
- **Success Criterion:** Report differences; if large (>5% accuracy gap), add caveat in limitations
- **Estimated Cost:** ~2 GPU-hours
- **Expected Gain:** Quantifies the synthetic data bias in LUMA's image modality

**P2-Exp5: Hyperparameter sensitivity analysis**
- **Target Claim:** Baseline results are stable under hyperparameter changes
- **Hypothesis:** Uncertainty estimates vary with learning rate, dropout probability, and ensemble size
- **Minimal Design:** For MCD multimodal, vary dropout {0.1, 0.3, 0.5}; for DE, vary ensemble size {5, 10, 15}
- **Metrics:** Aleatoric/epistemic uncertainty, accuracy
- **Success Criterion:** Sensitivity coefficients reported; if high, add as known limitation
- **Estimated Cost:** ~20 GPU-hours
- **Expected Gain:** Establishes robustness of baseline estimates

### ASCII Diagram — Experiment Upgrade Plan
```text
Experiment Upgrade Plan (P0/P1/P2)
====================================
P0 (Must, before resubmission)
├── Exp1: Multi-seed variance + significance (all baselines)
├── Exp2: Independent text validation (BERT)
└── Exp3: Corrected diversity formula sensitivity

P1 (Should, week 2)
├── Exp4: EDM vs real image subset analysis
├── Exp5: Hyperparameter sensitivity
└── Move accuracy table to main text

P2 (Nice-to-have, polish)
├── Additional UQ baselines (e.g., SVI, deep evidential regression)
└── Cross-modal uncertainty interaction study
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
### Final Score: **5.5/10**

**Rationale:** The paper addresses a genuine gap (controllable multimodal UQ benchmark) and provides a substantial data collection effort. However, the experimental evaluation has a critical flaw — no variance reporting — that makes the baseline comparisons unverifiable. Additional major issues (circular text validation, ambiguous formula, missing limitations, unstructured related work) further reduce confidence. The novelty assessment is deferred due to unavailable external retrieval, but the dataset creation and tooling contributions are clearly useful. The score prioritizes research value and experimental rigor as primary dimensions, leading to a below-acceptance-threshold score for a top venue. With all P0 fixes (multi-seed variance, formula correction, independent validation, limitations), the paper could reach the acceptance range.

### Post-Revision Target: **[6.5, 7.5]/10**

This interval reflects the expected score if all P0 and P1 items are addressed: multi-seed variance reporting, corrected diversity formula, independent text validation, structured related-work comparison table, and dedicated limitations section. The upper bound (7.5) assumes these are executed thoroughly. Further improvement beyond 7.5 would require more baselines, cross-modal interaction analysis, and external novelty verification — these are P2-level enhancements.

| Score Dimension | Current | After P0/P1 Fixes |
|----------------|---------|-------------------|
| Research Value / Problem Significance | 7/10 | 7/10 |
| Novelty (deferred, estimated) | 6/10 | 6/10 |
| Methodological Soundness | 4/10 | 7/10 |
| Experimental Rigor | 3/10 | 7/10 |
| Reproducibility | 5/10 | 8/10 |
| Clarity / Writing | 5/10 | 7/10 |
| **Overall** | **5.5/10** | **[6.5, 7.5]/10** |