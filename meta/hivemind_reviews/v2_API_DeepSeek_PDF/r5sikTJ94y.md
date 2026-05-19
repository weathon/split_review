## Summary
# Final Review Report

## Summary

This paper proposes RAOQ (Reshape and Adapt for Output Quantization), a quantization-aware training framework to address ADC quantization errors in analog in-memory computing (IMC) systems. The framework consists of three technical components: (1) A-shift, which shifts activation distributions to increase the second moment and improve ADC signal-to-quantization-noise ratio (SQNR); (2) W-reshape, which applies kurtosis regularization on quantized weights to reshape weight distributions toward larger variance; and (3) BitAug, which augments training with multiple ADC bit precisions to improve optimization landscape smoothness.

The paper demonstrates results across image classification (ResNet, MobileNet, EfficientNet on ImageNet), object detection (YOLOv5s on COCO), and NLP (BERT-base/large on SQuAD), at various activation/weight/ADC bit precisions. RAOQ consistently recovers accuracy to within 0.3-2% of no-ADC baselines across 7-9 bit ADCs, substantially outperforming conventional quantization-aware training.

**Overall assessment:** The paper addresses a well-motivated and practically important problem (ADC quantization in analog IMC). The proposed techniques are technically sound and the experimental evaluation is broad in terms of models, tasks, and bit precisions. However, the paper has several notable weaknesses: (1) the core theoretical rationale relies on a postulated proportional relationship validated on only the first few layers; (2) results lack statistical significance reporting; (3) important layers are excluded from IMC mapping without clear disclosure of the fraction mapped; (4) the conclusion lacks explicit limitations; and (5) novelty claims are partially over-reaching. These issues are addressable through targeted revisions and additional experiments. The research value is moderate: the work provides practical engineering solutions for ADC quantization, but the theoretical depth is limited and novelty versus prior ADC-QAT works is incremental rather than foundational.

## Strengths
1. **Practical and well-motivated problem.** ADC quantization is a genuine bottleneck in analog IMC systems, and addressing it at the algorithmic level (rather than requiring hardware modifications) has clear practical value. The paper correctly identifies that ADC quantization differs fundamentally from activation/weight quantization because its parameters are fixed by hardware.

2. **Broad empirical evaluation.** The paper evaluates on 8 model architectures spanning image classification (ResNet18/50, MobileNetV2, EfficientNet-lite0), object detection (YOLOv5s), and NLP (BERT-base/large), across 3 datasets (ImageNet, COCO, SQuAD). This breadth is a clear strength and supports the claim of generalizability.

3. **Ablation completeness.** Table 3 systematically ablates each component (A-shift, W-reshape, BitAug) individually and in combination across three diverse models. The ablation confirms that all components contribute and that the full combination yields the best results.

4. **Comparison with prior methods.** Table 2 provides direct comparisons against three prior ADC-QAT methods (Jin et al., Sun et al., Wei et al.) on CIFAR-10, carefully matching their configurations (memory dimensions, bit precisions, hardware noise levels). RAOQ shows consistently lower degradation.

5. **Hardware compatibility analysis.** Appendix B shows that A-shift is compatible with both 0/1 and -1/1 number representations used in different IMC designs, demonstrating the method's practical deployability.

6. **Training overhead disclosure.** Section 5.1 and Appendix E transparently report GPU usage, training epochs, and the 14% memory / 1.5× speed overhead of BitAug, which helps reviewers assess practicality.

7. **Toy example for BitAug mechanism.** Appendix F uses a single-layer network with a spiking loss function to illustrate how BitAug helps escape local minima. This provides intuitive understanding even if not a formal proof.

## Weaknesses
1. **Core theoretical rationale is empirically thin (Page 4 - Analysis).** The central claim that ADC SQNR improves by maximizing Var[Y], and that Var[Y] is proportional to E[X²] and E[W²], is supported by empirical data from only the "first few layers" of ResNet50 and MobileNetV2. The paper acknowledges this limitation but does not test whether the proportional relationship holds in deeper layers, where activations become sparser. This weakens the theoretical foundation of W-reshape and A-shift.

2. **Results lack statistical significance (Page 8 - Table 1).** All accuracy/mAP/F1 results are reported as single-point values without standard deviation, confidence intervals, or multi-seed averaging. Given that RAOQ improvements are often within 0.3-2% of the no-ADC baseline, and several comparisons (e.g., ResNet18 8,8 at ba=8: RAOQ=70.46 vs No ADC=70.66; BERT-large 4,4 at ba=9: RAOQ=89.55 vs No ADC=89.57) show near-identical numbers, readers cannot assess statistical reliability.

3. **Incomplete disclosure of IMC mapping coverage (Page 7 - Experimental Setup).** The paper excludes depthwise convolutions, BMM2, and first/last layers from IMC mapping but does not report the fraction of total operations that ARE mapped to IMC. A reader cannot determine how much of the model actually runs on IMC versus digital. This directly affects the interpretation of energy-efficiency analysis in Section 6.

4. **Over-reaching novelty claim (Page 2 - Introduction).** The statement "first to demonstrate approaches that enable IMC for inference across various scales of models and challenging datasets/tasks" is not adequately scoped. Prior work (Jin et al., Sun et al., Wei et al.) addressed ADC quantization on simpler datasets; the paper's clear contribution is scaling to harder benchmarks, but the "first" claim should explicitly state this scaling dimension.

5. **Conclusion lacks limitations and future work (Page 9 - Conclusion).** The conclusion simply restates methods and claims generalizability without acknowledging any limitations (e.g., partial IMC mapping, single IMC configuration tested, no multi-seed statistics). This reduces scientific credibility.

6. **Equation (6) notational inconsistency (Page 5 - A-shift).** The final equality "= x - 2^(bx-1)" in Eq. (6) implies the clip/round/scale operation reduces to the identity, which is mathematically incorrect. This appears to be a notational shortcut that redefines `x` as the quantized output, but this is not clearly stated.

7. **BitAug design choices lack mechanistic justification (Page 7 - BitAug).** The asymmetric bit-precision set B = {ba-1, ba+1, ba+2} and uniform weighting λb are empirically motivated but not explained mechanistically. It is unclear why ba+2 is included but ba-2 is not, and whether different bit precisions should receive different gradient weights.

8. **Ablation study missing interaction combinations (Page 9 - Table 3).** The ablation tests all 7 single/double/triple combinations *except* A-shift+BitAug (without W-reshape) and W-reshape+BitAug (without A-shift). These missing entries would help disentangle overlapping benefits, especially since the combined gain (+4.22 for ResNet50) is only slightly larger than A-shift alone (+3.72).

## Key Issues
### Issue A: Missing statistical significance in all experiments [Severity: Major]
**Anchor:** Page 8 - Table 1, Page 8 - Section 5.2 Results, Page 9 - Table 3 Ablation

**Evidence:** All results (Table 1, Table 2, Table 3) report single values without standard deviation, confidence intervals, or multi-seed averaging. Many RAOQ results are within 0.3% of the no-ADC baseline (e.g., ResNet18 8,8 ba=8: RAOQ=70.46 vs No ADC=70.66; BERT-large 4,4 ba=9: RAOQ=89.55 vs No ADC=89.57). The CIFAR-10 comparison (Table 2) shows RAOQ achieving +0.09% over the no-ADC case, which is likely within run-to-run noise.

**Impact:** Without variance information, the core claim that RAOQ "restores the performance to high accuracy" cannot be statistically verified. Small deltas between RAOQ and baselines may not be reproducible.

**Required Fix:** Report all results as mean ± std over ≥3 random seeds. Add a statistical significance note for key comparisons (RAOQ vs. QAT-only, RAOQ vs. prior methods in Table 2).

---

### Issue B: Core theoretical rationale validated on limited data [Severity: Major]
**Anchor:** Page 4 - Analysis and Rationale section, Fig. 2c-2d

**Evidence:** The proportional relationship between Var[Y] and E[X²]/E[W²] (which motivates W-reshape and A-shift) is tested on only "the first few layers" of ResNet50 and MobileNetV2. The paper does not verify that this relationship holds in deeper layers where activations are sparser. The causal direction (maximizing Var[W] increases Var[Y]) is asserted rather than tested via controlled intervention.

**Impact:** If the proportional relationship degrades in deeper layers, W-reshape may have diminishing returns in later network stages. The paper does not provide layer-wise SQRN or accuracy analysis to rule this out.

**Required Fix:** (1) Extend the empirical study to at least middle and deep layers of ResNet50 and BERT-base. (2) Add an experiment that directly measures Var[Y] before and after applying W-reshape (not just final accuracy). (3) Add a correlation coefficient (Pearson r) to quantify the strength of the proportional relationship.

---

### Issue C: Incomplete disclosure of IMC mapping coverage [Severity: Major]
**Anchor:** Page 7 - Experimental Setup paragraph

**Evidence:** The paper states that depthwise convolutions (<7%), BMM2 (<1.5%), and first/last layers are kept in 8-bit digital precision and not mapped to IMC. However, the fraction of total operations that ARE mapped to IMC is not reported. The energy-efficiency analysis in Section 6 appears to assume full IMC operation.

**Impact:** Readers cannot determine if the claimed IMC advantages apply to a partial or near-complete deployment. The energy comparison in Section 6 may overstate the benefit if a significant fraction of operations remain in digital.

**Required Fix:** Report for each model: (a) percentage of operations mapped to IMC, (b) percentage of parameters stored in IMC arrays, (c) clarify whether the energy-efficiency plot in Fig. 5 assumes full or partial mapping.

---

### Issue D: Over-reaching novelty claim [Severity: Major]
**Anchor:** Page 2 - Introduction, lines 14-16

**Evidence:** "To the best of our knowledge, this work is the first to demonstrate approaches that enable IMC for inference across various scales of models and challenging datasets/tasks." The paper's own related work (Section 2.2) acknowledges that prior works (Jin et al., Sun et al., Wei et al.) addressed ADC quantization on CIFAR-10. The clear contribution is scaling to harder benchmarks, but the "first" framing is ambiguous.

**Impact:** If literature exists that addressed ADC quantization at ImageNet scale (even partially), this claim is invalid. The paper should bound the claim to the demonstrated scope.

**Required Fix:** Replace with scoped wording: "To the best of our knowledge, this is the first work to demonstrate ADC quantization-aware training that scales to ImageNet classification, COCO object detection, and SQuAD question answering with consistent accuracy recovery."

---

### Issue E: Conclusion lacks limitations [Severity: Major]
**Anchor:** Page 9 - Conclusion

**Evidence:** The conclusion claims "generalizability and robustness" without acknowledging any of the paper's limitations (partial IMC mapping, single IMC configuration k=4, no multi-seed statistics, limited theoretical validation).

**Impact:** Reduces scientific credibility and may mislead readers about deployment readiness.

**Required Fix:** Add explicit limitations paragraph covering: partial IMC mapping, single IMC configuration (k=4, 512×512), missing statistical significance, and unverified generalization to other modalities (speech, generative models).

## Actionable Suggestions
### S1 (Must) — Add multi-seed variance reporting
**Target:** Page 8, Table 1; Page 9, Table 3

Run all experiments for at least 3 random seeds and report mean ± std. If full computational budget is prohibitive, run at least 2 seeds for the largest models (BERT-large, YOLOv5s) and 3 seeds for smaller models (ResNet18, MobileNetV2). Add a sentence: "Results are reported as mean ± std over N seeds. Differences smaller than the std range should be interpreted as not statistically significant."

### S2 (Must) — Extend empirical validation of Var[Y] proportional relationship
**Target:** Page 4, Section 3, Fig. 2c-2d

Extend the empirical study of Var[Y] vs. E[X²] and E[W²] to include middle and deep layers of at least one model (e.g., all 48 layers of ResNet50). Report Pearson correlation coefficients per layer and show a summary plot. If the relationship weakens in deep layers, discuss the implications for W-reshape effectiveness.

### S3 (Must) — Report IMC mapping coverage fraction
**Target:** Page 7, Experimental Setup

For each model, report: "% of total multiply-accumulate operations mapped to IMC" and "% of total model parameters stored in IMC arrays." This allows readers to assess the completeness of IMC deployment.

### S4 (Must) — Bound novelty claim
**Target:** Page 2, Introduction

Replace "first to demonstrate approaches that enable IMC for inference across various scales of models and challenging datasets/tasks" with a scoped version: "To the best of our knowledge, this is the first work to demonstrate ADC quantization-aware training that scales to ImageNet classification, COCO object detection, and SQuAD question answering across multiple model families."

### S5 (Must) — Add limitations and future work to conclusion
**Target:** Page 9, Conclusion

Add a limitations paragraph covering: (a) partial IMC mapping (certain layers kept in digital), (b) single IMC configuration (k=4, 512×512 array), (c) missing statistical significance, (d) unverified generalization to speech/generative tasks. Add a future work sentence: "Extending RAOQ to larger transformer models, adaptive per-layer ADC configuration, and validation on speech and generative AI tasks are natural next steps."

### S6 (Nice-to-have) — Add missing ablation combinations
**Target:** Page 9, Table 3

Add rows for A-shift+BitAug (without W-reshape) and W-reshape+BitAug (without A-shift) to Table 3, or include them in the appendix and reference in the main text. This enables readers to assess whether A-shift and W-reshape have overlapping or orthogonal benefits.

### S7 (Nice-to-have) — Fix Eq. (6) notation
**Target:** Page 5, Eq. (6)

Replace the ambiguous final equality "= x - 2^(bx-1)" with two-step notation:
```
x_u = clip(⌊(x-β)/sx⌉, 0, 2^bx - 1)
x_s = x_u - 2^(bx-1)
```
This clarifies that `x_u` is the quantized unsigned value.

### S8 (Nice-to-have) — Add BitAug weighting analysis
**Target:** Page 7, Section 4.2

Add an ablation varying λb per bit-precision bucket, or at minimum report gradient norms from different auxiliary bit precisions to explain why equal weighting works.

### S9 (Nice-to-have) — Restructure Related Work
**Target:** Page 3, Section 2.2

Reorganize the prior ADC-QAT methods by methodology category (STE-modification, quantization-range regularization, hardware-statistics-informed) rather than chronologically. Add a comparison table summarizing each prior method's tested datasets, model types, and key limitation.

### S10 (Nice-to-have) — Intro narrative efficiency
**Target:** Page 1, Introduction, first paragraph

Condense the opening paragraph to directly state the IMC-ADC quantization problem within 2-3 sentences instead of starting with broad AI advances. A suggested replacement is provided in the annotations (annotation ID 2 on Page 1).

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current introduction (Pages 1-2) follows this structure:
- P1: Broad AI advances → growing model complexity → hardware demands
- P2: Digital accelerators' data-movement bottleneck → IMC as solution
- P3: Focus on analog IMC → ADC as critical bottleneck
- P4 (Page 2): ADC quantization differs from weight/activation quantization → prior work limitations
- P5: RAOQ proposed → contribution list

**Problem:** The narrative reaches the paper's core problem (ADC quantization) only in paragraph 3, after 1.5 pages of background. The first two paragraphs could be condensed into 1 paragraph.

**Alignment Check:**
- Problem alignment: Yes (IMC ADC quantization is consistently the focus)
- Variable alignment: Yes (A-shift, W-reshape, BitAug appear in both intro and method)
- Contribution-evidence alignment: Mostly yes (Table 1 supports contributions, but missing variance undermines confidence)

### Recommended Storyline (Option A) — "Bottleneck-First"

**Abstract Outline (4-5 sentence structure):**
- S1 (Problem+Domain): "Analog in-memory computing (IMC) promises high energy efficiency for AI inference by performing computation directly in memory arrays."
- S2 (Challenge): "However, analog IMC requires analog-to-digital converters (ADCs) that introduce a unique quantization bottleneck—ADC errors cannot be mitigated by standard quantization-aware training because their parameters are hardware-fixed."
- S3 (Prior Gap): "Existing algorithmic approaches to ADC quantization have been validated only on small datasets (CIFAR-10, MNIST) and do not scale to modern AI workloads."
- S4 (Proposed Method): "We propose RAOQ, a training framework with three components: activation-shifting (A-shift) and weight reshaping (W-reshape) to improve ADC signal-to-noise ratio, and bit augmentation (BitAug) to stabilize optimization across ADC precisions."
- S5 (Key Result): "On ImageNet classification, COCO detection, and SQuAD question answering, RAOQ recovers accuracy to within 0.3-2% of no-ADC baselines across 7-9 bit ADCs and 8 model architectures."

**Introduction Outline (5 paragraphs):**
- P1 (Stakes + Bottleneck): "Analog IMC performs matrix-vector multiplications in memory arrays, dramatically reducing data movement. But the analog outputs must be digitized by ADCs, whose quantization is fundamentally different from weight/activation quantization because ADC parameters are fixed by hardware." (1-2 sentences replacing current paragraphs 1-2)
- P2 (Prior Work Gap): "Prior QAT methods focus on input quantization (weights, activations). ADC quantization on accumulated outputs is harder because neither clipping range nor step size is trainable. Prior ADC-specific methods [Jin, Sun, Wei] work on CIFAR-10/MNIST but fail to scale to ImageNet, COCO, or SQuAD."
- P3 (Our Approach - Intuition): "We observe that ADC SQNR depends on the variance of the compute output (ADC input). By reshaping weight distributions (W-reshape via kurtosis loss) and shifting activation distributions (A-shift via unsigned-to-signed conversion), we increase ADC input variance and thus SQNR. To handle the resulting optimization difficulty, we introduce BitAug, which uses multiple ADC bit precisions during training."
- P4 (Key Results Preview): "Across 8 architectures (ResNet, MobileNet, EfficientNet, YOLOv5s, BERT) and 3 tasks, RAOQ recovers accuracy to within 0.3-2% of no-ADC baselines, outperforming conventional QAT by 5-30 percentage points at 7-8 bit ADCs."
- P5 (Contributions): Numbered list of 3 contributions (analysis, A-shift+W-reshape, BitAug) as in the current version.

### Alternative Storyline (Option B) — "Mechanism-First"
Open with the insight: "ADC quantization on IMC compute outputs is fundamentally different from conventional quantization because its parameters are not trainable." Then derive the need for activation/weight reshaping, then introduce IMC background. This is more engaging for an ML audience but may lose hardware-focused readers.

### Alternative Storyline (Option C) — "Application-First"
Start with a concrete energy-accuracy trade-off plot (Fig. 5 early), showing that higher ADC precision costs energy. Then state: "This paper shows how to maintain accuracy at low ADC precision without hardware changes." This is direct but less technically deep.

**Recommendation:** Option A (Bottleneck-First) is best for the target ICLR audience. It preserves technical depth while reducing time-to-core-problem.

## Priority Revision Plan
| Priority | Issue | Required Action | Effort | Impact | Expectation |
|----------|-------|----------------|--------|--------|-------------|
| P0 (Must) | Missing statistical significance | Run 3-seed experiments; report mean±std for Tables 1, 2, 3 | High (compute-heavy) | High: core claim verification | Without this, the paper's main results are not scientifically verifiable |
| P0 (Must) | IMC mapping coverage undisclosed | Report % ops mapped to IMC per model; clarify energy analysis scope | Low (analysis only) | High: corrects potential overclaim | Essential for honest claim boundaries |
| P0 (Must) | Over-reaching novelty claim | Reword "first" claim with explicit scope qualifier | Low (text edit) | High: avoids rejection risk | Must do before resubmission |
| P0 (Must) | Conclusion lacks limitations | Add limitations paragraph (partial mapping, single config, no multi-seed) | Low (text edit) | Medium: scientific completeness | Required for scientific credibility |
| P1 (Strongly Recommended) | Eq. (6) notational inconsistency | Replace ambiguous final equality with two-step notation | Low (text edit) | Medium: reproducibility | Important but minor fix |
| P1 (Strongly Recommended) | Theoretical rationale limited to early layers | Extend Var[Y] correlation study to deeper layers | Medium (experiments) | Medium: theoretical rigor | Strengthens core argument |
| P2 (Recommended) | Missing ablation combinations | Add A-shift+BitAug, W-reshape+BitAug rows | Low (analysis) | Low-Medium: completeness | Nice to have |
| P2 (Recommended) | BitAug justification | Add gradient-norm analysis or λb weighting study | Medium (experiments) | Low-Medium: depth | Improves mechanistic understanding |
| P2 (Recommended) | Restructure Related Work | Reorganize by methodology category with comparison table | Low (text edit) | Medium: readability | Improves positioning |

### Revision Order

**Phase 1 (Text edits, 1-2 days):** Bound novelty claim (P0), add conclusion limitations (P0), fix Eq. (6) (P1), restructure Related Work (P2).

**Phase 2 (Experiments, 3-7 days):** Run 3-seed experiments for all models (P0). Extend Var[Y] study to deeper layers (P1). Add missing ablation rows (P2). Run BitAug weighting analysis (P2).

**Phase 3 (Analysis and write-up, 2-3 days):** Compute IMC mapping coverage percentages (P0). Write up new results. Update Tables 1-3 with statistics. Revise conclusion and abstract.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|-----------------|-------------------|
| E1 | Main evaluation (Table 1) | 8 models × 3 tasks × 2 (bx,bw) × 3 ADCs | Top-1 acc, mAP, F1 | RAOQ recovers to within 0.3-2% of no-ADC baseline | C1 (analysis), C2 (A-shift+W-reshape), C3 (BitAug) | Single seed; no variance |
| E2 | Comparison with prior methods (Table 2) | CIFAR-10, match configs of Jin/Sun/Wei | Accuracy, degradation | RAOQ outperforms all prior methods | C2, C3 | Small dataset only (CIFAR-10); hardness mismatch possible |
| E3 | Ablation study (Table 3) | 3 models, 4b/8b, 8b ADC, 7 combinations | Top-1 acc, F1 | All three components help; A-shift+BitAug most impactful | C2, C3 | Missing A-shift+BitAug and W-reshape+BitAug combos |
| E4 | IMC configuration sweep (Table 8, App. D) | ResNet50/MobileNetV2/BERT-base, rows 128-1024 | Accuracy | RAOQ robust across memory dimensions | Generalizability claim | Single config (k=4) |
| E5 | k parameter sweep (Table 9, App. D) | ResNet50/MobileNetV2/BERT-base, k=1..16 | Accuracy | k=4-8 optimal; k=16 degrades | Practical deployability | Only one IMC mem dim |
| E6 | BitAug candidate set study (Table 6, App. C) | MobileNetV2/ResNet50/BERT-base, k=1 | Accuracy | {ba-1, ba+1, ba+2} is optimal | C3 (BitAug design) | k=1 only (more noise); effect may differ at k=4 |
| E7 | BitAug sampling mode (Table 7, App. C) | MobileNetV2, single vs all candidates | Accuracy | Single-sample outperforms all-batch | C3 (efficiency) | Only one model tested |
| E8 | W-reshape λκ sensitivity (Tables 4-5, App. A) | ResNet50/MobileNetV2, λκ sweep | Accuracy (w/ and w/o ADC) | λκ=0.0005 optimal; trade-off visible | C2 (W-reshape design) | Only two models |
| E9 | QAT method compatibility (Table 10, App. G) | BERT-base, 3 QAT methods + RAOQ | F1 | RAOQ works with LSQ+, LSQ, PACT+SAWB | Generalizability | One model only |
| E10 | Toy example for BitAug (App. F) | Single-layer net, spiking loss | Weight distribution, loss landscape | BitAug reduces local minima | C3 mechanism | Toy setting; may not reflect real NNs |

### Research-Theme Gap Diagnosis

1. **New knowledge (theoretical):** Weak. The core proportional relationship (Var[Y] ∝ E[X²]·E[W²]) is postulated and tested on limited data (early layers only). No formal derivation or bound is provided.
2. **New knowledge (empirical):** Moderate-strong. The paper provides the broadest evaluation of ADC-QAT methods to date across tasks, models, and bit precisions. However, the lack of statistical significance reduces confidence.
3. **Reproducibility:** Moderate. Training details are thorough (Appendix E), hyperparameters are reported, and a code example is provided. Missing: exact IMC simulation code, random seed specification, and per-epoch logs for all experiments.
4. **Potential to change practice:** Moderate. RAOQ is practical and does not require hardware changes, making it immediately applicable to existing IMC systems. The 14% memory and 1.5× speed overhead of BitAug are acceptable. However, the partial IMC mapping (excluded layers) limits the headline impact.

### Proposed Research Experiments

| Experiment ID | Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost/Time | Quality Gain |
|--------------|-------------|-----------|---------------|-------------------|---------|------------------|---------------|-------------|
| P-Exp-1 [P0] | All claims | RAOQ results are statistically significant | Run 3 seeds for ResNet50 (4b/8b, ba=7,8,9) and BERT-base (4b, ba=8) | Use same training configs as current paper | Mean ± std accuracy/F1 | std < 0.3% for classification; < 0.5% for BERT | ~20 GPU-days (A100) | High: enables proper claim verification |
| P-Exp-2 [P1] | C1 (analysis) | Var[Y] ∝ E[X²]·E[W²] holds across all layers | Compute Var[Y]/E[X²]/E[W²] for all 48 ResNet50 layers; plot Pearson r per layer | Same models as Fig. 2 | Per-layer Pearson correlation coefficient | r > 0.7 in >75% of layers | ~1 GPU-day | Medium: strengthens theoretical foundation |
| P-Exp-3 [P1] | C2 (A-shift+W-reshape) | Var[Y] increases measurably after applying W-reshape | Measure Var[Y] before/after W-reshape intervention at fixed checkpoint | Without vs with W-reshape; same QAT baseline | Var[Y] ratio (after/before); SQNR change | Var[Y] ratio > 1.2 on average across layers | ~1 GPU-day | Medium: provides direct causal evidence |
| P-Exp-4 [P2] | C3 (BitAug) | BitAug gradient diversity improves convergence | Compute gradient cosine similarity between ba and auxiliary ba,i over training | Compare with/without BitAug | Gradient similarity; final accuracy | Lower similarity correlates with higher gain | ~2 GPU-days | Low-Medium: mechanistic understanding |
| P-Exp-5 [P2] | Generalizability claim | RAOQ transfers to speech task | Apply RAOQ to Wav2Vec2 or HuBERT on LibriSpeech (4b weights, 8b ADC) | Same RAOQ config; compare vs conventional QAT | Word Error Rate (WER) | WER within 2% of no-ADC baseline | ~10 GPU-days | Medium: extends claim to new modality |

### ASCII Diagram — Experiment Upgrade Plan

```text
Stage 1 (P0, 1 week): Statistical Significance
  ├── Run 3 seeds: ResNet50 (all ADCs), BERT-base (4b, ba=8)
  ├── Update Tables 1-3 with mean±std
  └── Gate: std < 0.3% (classif) and < 0.5% (NLP)
        ↓ pass
Stage 2 (P1, 2-3 days): Theoretical Foundation
  ├── Extend Var[Y] study to all 48 layers of ResNet50
  ├── Measure Var[Y] before/after W-reshape
  └── Gate: Pearson r > 0.7 in >75% of layers
        ↓ pass
Stage 3 (P2, 1 week): Completeness
  ├── Add missing ablation combos
  ├── BitAug gradient analysis
  ├── Speech task validation (optional)
  └── Finalize: update claims, conclusion, abstract
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 6.0 / 10

**Rationale:** The paper addresses a genuine and practically important problem (ADC quantization in analog IMC). The proposed techniques (A-shift, W-reshape, BitAug) are well-motivated, clearly described, and evaluated on an impressively broad set of models and tasks. The empirical results consistently show RAOQ outperforming conventional QAT across all tested configurations.

However, the score is constrained by several significant weaknesses: (1) the lack of statistical significance (multi-seed variance) across all experiments makes the core results unverifiable; (2) the theoretical foundation is empirically thin, relying on a proportional relationship tested only on early layers; (3) the IMC mapping coverage is incompletely disclosed, potentially exaggerating the practical scope; (4) the novelty claim is over-reaching; and (5) the conclusion lacks limitations. These are primarily rigor/completeness issues rather than fatal flaws—they are addressable through targeted revisions.

Research value is moderate: the work provides practical, deployable solutions for a hardware bottleneck, but the theoretical depth is limited and the core ideas (reshaping weight/activation statistics for better quantization) are conceptually incremental over existing QAT literature.

**Post-Revision Target:** [7.0, 7.5] / 10

If the authors address the P0 items (multi-seed statistics, IMC mapping disclosure, bounded novelty claim, conclusion limitations) and at least the P1 item (extended theoretical validation), the paper would be substantially stronger. The upper bound of 7.5 reflects the inherent limitation that the theoretical contribution is not at the level of a major new principle or framework, but rather a well-engineered combination of known techniques (kurtosis regularization, unsigned-to-signed shifting, network augmentation) applied to a specific hardware problem. With all issues fully addressed, the paper would be a solid contribution to the IMC+ML community.