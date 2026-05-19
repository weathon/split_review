## Summary
# Final Review Report

## Summary

This paper presents MaskComp, an object completion method that reconstructs a complete object from its partially visible components by iteratively alternating between a generation stage (mask-conditioned diffusion model based on ControlNet) and a segmentation stage (SAM-based mask extraction and voting). The core idea is to treat the partial object mask as a "noisy" version of the complete mask and progressively denoise it through an iterative mask denoising (IMD) process. The method additionally introduces a time-dependent gating mechanism that adjusts the influence of the conditioning signal across diffusion timesteps.

On the AHP and DYCE benchmarks, MaskComp achieves substantially lower FID scores (16.9 and 20.0) compared to baselines including ControlNet (40.2/42.4) and Stable Diffusion 2.1 (30.8/30.0), and ranks highest in user studies. The paper includes extensive ablations on IMD step count, number of sampled images, diffusion iterations, gating, occlusion types, and segmentation models.

**Key strengths:** The iterative generation-segmentation loop is a intuitively appealing framework for object completion; the gating mechanism is a reasonable adaptation for handling imprecise conditioning; empirical gains over baselines are large and consistent across two datasets.

**Core weaknesses:** (1) The mathematical formulation in Eq. (1) has a circular dependency and the additive noise model for binary masks is ill-defined; (2) the FID evaluation using object-area-only cropping may favor MaskComp's black-background training over baselines; (3) inference is ~77s per image, orders of magnitude slower than baselines, yet this limitation is not adequately discussed; (4) the "training without complete objects" claim lacks quantitative support; (5) the Gibbs sampling analogy and "slack condition" are not concretely specified; (6) the third contribution bullet is a performance-only claim without conceptual advance. External literature verification is unavailable in this run; novelty/comparison conclusions are marked as deferred.

## Strengths
**S1 — Intuitive and principled framework.** The iterative mask denoising (IMD) process that alternates between generation and segmentation is conceptually clean and well-motivated. The key observation — that mask-conditioned generation quality depends on mask quality — is directly supported by the ablation in Table 2a (FID improves from 16.9 with visible masks to 12.7 with complete masks). This makes the iterative refinement strategy self-consistent.

**S2 — Strong empirical results.** Table 1 shows MaskComp achieving FID-G of 16.9 on AHP and 20.0 on DYCE, substantially outperforming ControlNet (40.2/42.4), Kandinsky 2.1 (43.9/44.3), Stable Diffusion 1.5 (35.7/31.2), and SD 2.1 (30.8/30.0). The user study also shows MaskComp ranked best 53% and 63% of the time on the two datasets — a clear margin over baselines (next best at 14% and 12%). These gains are consistent across two datasets with different characteristics (human-centric AHP vs. indoor objects DYCE).

**S3 — Comprehensive ablation study.** The paper systematically ablates design choices: IMD step number (T), number of sampled images (N), diffusion iterations, gating, mask conditioning types, occlusion rates, segmentation models, and voting strategies (Tables 2-4). This thoroughness helps isolate the contribution of each component.

**S4 — Practical generalization capability.** The exploration of training without complete objects (Appendix B, Fig. 9) is a forward-looking direction that could extend the method to settings where ground-truth masks are unavailable, increasing real-world applicability.

**S5 — Clean writing and good visualizations.** The paper is generally well-organized with clear figures (Fig. 1 IMD process, Fig. 3 architecture, Fig. 7 step-by-step visualization) that help convey the iterative refinement concept.

## Weaknesses
**W1 — Mathematical imprecision in core formulation (Major).** Equation (1) has a circular dependency: `Mc ← S(G(Ip, Mc + Δ))` references `Mc` on both sides when `Mc` is the unknown target. The additive noise model `Mp = Mc + Δ` is inappropriate for binary masks (values leave [0,1] range). See Annotation ID ee3db9f4 (Page 3).

**W2 — FID evaluation fairness concern (Major).** The paper uses object-area-only FID (FID-G, FID-S) computed by cropping to ground-truth or SAM-segmented regions. MaskComp is trained on black-background images, giving it an advantage when evaluated on object-only areas, while baselines generate natural backgrounds that may be unfairly penalized by cropping. Standard full-image FID is not reported. See Annotation ID f4fbe070 (Page 7).

**W3 — Prohibitive inference cost (Major).** At ~77 seconds per image (15.5s per IMD step × 5 steps), MaskComp is 15-40× slower than baselines. The speed optimization (2/3 of original time) is mentioned without reporting the resulting absolute time. No latency comparison against baselines is provided. See Annotation ID 3caf0bad (Page 8).

**W4 — Unsubstantiated generalization claim (Major).** The claim that MaskComp can be trained "without complete objects" (Appendix B) is supported only by visual examples (Fig. 9) without quantitative FID or user study results. This is a potentially important capability, but the evidence is insufficient. See Annotation ID 1eb214b2 (Page 11).

**W5 — Underspecified gating mechanism (Major).** The time-dependent gating operation is a claimed technical novelty, but the description omits critical details: the gating value range, whether it's applied per-channel or globally, and its behavior across timesteps. See Annotation ID fcdfe797 (Page 5).

**W6 — Vague "slack condition" in mathematical framing (Major).** The Gibbs sampling analogy in Section 3.3 introduces a "slack condition" to make p(M|I) a real distribution, but never specifies how this is implemented algorithmically. The consistency between the two learned conditionals (ControlNet and SAM) is not verified. See Annotation ID a9c7ffaa (Page 6).

**W7 — Performance-only third contribution (Minor).** The third contribution bullet is purely performance-based without stating any conceptual advance. Per contribution extraction guidelines, such bullets dilute the paper's novelty signal. See Annotation ID ef9b059b (Page 2).

**W8 — Abstract lacks gap statement (Minor).** The abstract does not establish the prior limitation before presenting the method. See Annotation ID f3a98d6d (Page 1).

**W9 — Related work is a flat list (Minor).** The related work sections (2.1, 2.2) read as chronological paper lists without comparison axes that highlight MaskComp's position. See Annotation ID 5337af53 (Page 2) and e622945a (Page 3).

**W10 — Mask voting threshold not justified (Minor).** The τ=0.5 threshold is used without sensitivity analysis or principled justification. See Annotation ID 022f5bda (Page 5).

**W11 — Gating improvement magnitude small relative to gap (Minor).** The gating mechanism improves FID by only 1.3 points (16.9 vs 18.2 in Table 3d), whereas the overall gain over baselines is 15-25 FID points. The paper attributes much of the gain to the mask condition and IMD process, but does not ablate these separately from the gating mechanism.

**W12 — Conclusion lacks limitations and quantitative summary (Minor).** The conclusion does not mention any limitations and uses generic "robustness and effectiveness" language instead of citing specific metrics. See Annotation ID 04b7119a (Page 9).

## Key Issues
### Ranked Top-5 Core Defects

| Rank | Issue | Severity | Research-Value Impact | Validity Risk | Fixability | Confidence |
|------|-------|----------|----------------------|--------------|------------|------------|
| 1 | Eq. (1) circular dependency and invalid binary mask noise model | Major | High — core mathematical framing is flawed | Medium — the actual implementation likely avoids this issue but the written formulation is misleading | High — simply rewrite Eq. (1) to use iterative indexing M_{t} ← V({S(G(Ip, M_{t-1}^{(i)}))}) | High |
| 2 | FID evaluation with object-area cropping may favor MaskComp unfairly | Major | High — claimed superiority may be partially artifactual | High — if evaluation is biased, core results are not trustworthy as reported | Medium — add full-image FID and discuss background bias | Medium |
| 3 | ~77s inference time without adequate discussion or baseline comparison | Major | Medium — practical deployability is limited | Low — does not affect reported results, but transparency is missing | High — report optimized time, add comparison row, add limitation paragraph | High |
| 4 | "Training without complete objects" claim lacks quantitative support | Major | Medium — interesting direction but unverified | Medium — visual-only evidence may not generalize | High — add FID evaluation on held-out OpenImage split | High |
| 5 | Underspecified gating mechanism | Major | Low-Medium — minor technical detail but affects reproducibility | Low — likely implementable from context but undocumented | High — add explicit gating formula with sigmoid range and timestep behavior | High |

### Research-Value Assessment

The paper addresses a well-defined problem (object completion) with a conceptually appealing iterative refinement framework. The primary research value lies in demonstrating that alternating generation and segmentation can progressively improve mask quality. However, the core technical novelty is incremental — it adapts ControlNet with a time-dependent gating mechanism and combines it with SAM in a loop — rather than introducing a fundamentally new learning paradigm. Without external literature verification, the exact novelty boundaries cannot be definitively established, but based on the manuscript alone, the primary value contribution is **empirical demonstration** of the iterative generation-segmentation loop for object completion, rather than a theoretical or algorithmic breakthrough.

## Actionable Suggestions
### Suggestion 1 (Must) — Fix Eq. (1) circular dependency and noise model
**Target:** Page 3 - Method, Eq. (1) and surrounding text.
**Problem:** `Mc ← S(G(Ip, Mc + Δ))` uses `Mc` on both sides, and `Mp = Mc + Δ` is invalid for binary masks.
**Action:** Replace Eq. (1) with a proper iterative formulation:
`M_t ← V({S(G(Ip, M_{t-1}^{(i)}))}_{i=1}^N)`
Replace the additive noise model with a structural occlusion model: `Mp = Mc ⊙ (1 - O)` where O is a binary occlusion mask. Explain that the mask corruption is structural (pixels zeroed out), not additive Gaussian.
**Expected benefit:** Removes mathematical circularity and aligns the written formulation with the actual implementation.

### Suggestion 2 (Must) — Add full-image FID and discuss evaluation bias
**Target:** Page 7 - Table 1 and Section 4.1.
**Problem:** Object-area-only FID may favor MaskComp's black-background training.
**Action:** (a) Report standard full-image FID for all methods in a new table row. (b) Add a paragraph discussing that MaskComp is trained on black-background images while baselines are general-purpose models, and that the reported FID-G/FID-S should be interpreted as object-focused quality metrics. (c) If possible, retrain baselines with black-background fine-tuning for a fairer comparison.
**Expected benefit:** Restores reader trust in the comparison fairness.

### Suggestion 3 (Must) — Report optimized inference time and baseline comparison
**Target:** Page 8 - Table 2(c) and Section 4.2.
**Problem:** ~77s/image is prohibitively slow, no comparison with baselines.
**Action:** (a) Add a row to Table 2(c) reporting the optimized inference time (with the 2/3 speed-up strategy) in absolute seconds. (b) Add baseline inference times (ControlNet, SD 2.1) on the same hardware. (c) Add a limitation paragraph in the conclusion quantifying the latency gap and outlining mitigation directions.
**Expected benefit:** Transparent reporting of practical trade-offs.

### Suggestion 4 (Must) — Add quantitative results for "training without complete objects"
**Target:** Page 11 - Appendix B.
**Problem:** The generalization claim is supported only by visual examples.
**Action:** Add a quantitative evaluation: (a) Report FID-G and FID-S for the OpenImage-trained model on a held-out test split. (b) Compare against the model trained with complete masks to quantify the performance gap. (c) Report the average number of IMD steps needed for convergence.
**Expected benefit:** Validates (or bounds) a potentially important capability.

### Suggestion 5 (Must) — Specify gating mechanism details
**Target:** Page 5 - Section 3.1, last paragraph.
**Problem:** Gating function is underspecified.
**Action:** Add the following details: (a) Define `g_τ = σ(Linear(e_τ))` where `σ` is sigmoid, producing a scalar in [0,1]. (b) Specify whether gating is applied per-channel or globally. (c) Describe the expected behavior: `g_τ ≈ 1` at early timesteps, `g_τ ≈ 0` at late timesteps. (d) Optionally visualize `g_τ` as a function of τ.
**Expected benefit:** Enables reproducibility of the gating mechanism.

### Suggestion 6 (Must) — Revise Conclusion
**Target:** Page 9 - Section 5.
**Problem:** No limitations, no quantitative summary.
**Action:** Replace the current conclusion with the Mentor Revised Version from Annotation ID 04b7119a. Include specific FID numbers, acknowledge limitations (inference cost, SAM dependency, occlusion ceiling), and state 1-2 future directions.
**Expected benefit:** Conclusion becomes scientifically rigorous rather than promotional.

### Suggestion 7 (Nice-to-have) — Clarify slack condition and Gibbs consistency
**Target:** Page 5-6 - Section 3.3.
**Problem:** The slack condition enabling many-to-many mask-image relation is never concretely specified.
**Action:** Add a paragraph explaining how the slack condition is implemented (e.g., training on interpolated masks makes p(I|M) multimodal; SAM's probabilistic segmentation makes p(M|I) a distribution). Acknowledge that the two conditionals are not guaranteed to be consistent with a single joint distribution, and discuss whether convergence is still guaranteed under this approximation.
**Expected benefit:** Strengthens the theoretical framing and clarifies limitations.

### Suggestion 8 (Nice-to-have) — Mask voting threshold sensitivity
**Target:** Page 5 - Eq. (3) and Page 7 - Implementation details.
**Problem:** τ=0.5 is used without justification.
**Action:** Add a small ablation table testing τ ∈ {0.3, 0.4, 0.5, 0.6, 0.7} and report FID for each value. Alternatively, justify τ=0.5 as the majority voting rule under a uniform prior.
**Expected benefit:** Improves reproducibility and shows robustness of the voting mechanism.

## Storyline Options + Writing Outlines
### Abstract Outline (Full Sentence Plan)

The abstract should follow a compact 5-sentence structure:

- **S1 (Problem):** "This paper tackles object completion — reconstructing a complete object from its partially visible components."
- **S2 (Challenge/Gap):** "Existing conditional generation methods lack explicit shape guidance and often produce textures that do not align with the true object geometry."
- **S3 (Proposed Method):** "We propose MaskComp, which bridges image generation and segmentation through an iterative mask denoising (IMD) process: a mask-conditioned diffusion model generates candidate objects, and a segmentation model refines the object mask from those candidates, progressively transforming a partial mask into a complete shape."
- **S4 (Key Result):** "On the AHP and DYCE benchmarks, MaskComp achieves FID scores of 16.9 and 20.0, substantially improving over ControlNet (40.2/42.4) and Stable Diffusion 2.1 (30.8/30.0)."
- **S5 (Bounded Implication):** "These results demonstrate that iterative generation-segmentation alternation provides effective shape guidance for object completion under moderate occlusion."

### Introduction Outline (Paragraph-by-Paragraph Plan)

**P1 — Problem setting and gap.**
Role: Establish the task (object completion) and why it is harder than inpainting.
Current defect: Overstates the inpainting vs. completion distinction and does not cite specific prior object completion methods.
Revised focus: "Object completion requires inferring the precise shape of occluded parts from partial observations. Unlike inpainting, which can interpolate from surrounding context, object completion must recover the full object geometry — a task that existing conditional diffusion models struggle with because they lack explicit shape conditioning."

**P2 — Background on mask conditioning and motivation.**
Role: Introduce the key observation (mask quality determines generation quality) and why it motivates iterative refinement.
Current defect: The paragraph jumps from segmentation as a shape guide to the IMD idea without clearly stating why existing mask-conditioned methods (e.g., ControlNet) are insufficient.
Revised focus: "Prior work on mask-conditioned generation, such as ControlNet, assumes the input mask is accurate. However, in object completion only a partial mask is available. This paper asks: can we start from the partial mask and iteratively refine it using the generative model itself?"

**P3 — Method overview.**
Role: High-level description of the IMD process (generation ↔ segmentation).
Current defect: Contains too much low-level detail for an introduction (e.g., "segmentation stage is geared towards segmenting the object mask within the generated images").
Revised focus: "We propose the iterative mask denoising (IMD) process. In each iteration, a mask-denoising ControlNet generates candidate complete objects conditioned on the current mask estimate. A frozen SAM model then extracts masks from these candidates, and majority voting produces an improved mask for the next iteration. This loop progressively turns the partial mask into a complete mask."

**P4 — Contributions.**
Role: Explicit, non-hyped contribution list.
Current defect: Third contribution is performance-only.
Revised bullet 3: "We demonstrate through controlled ablations that iterative mask denoising provides monotonic mask refinement, that the time-dependent gating mechanism yields a 1.3 FID improvement, and that the approach is robust up to 60% occlusion."

### Storyline Comparison

| Alignment Check | Current Storyline | Proposed Storyline |
|---|---|---|
| Problem alignment | Adequate (object completion distinguished from inpainting) | Stronger (explicitly states why existing methods fail at shape recovery) |
| Variable alignment | Core concepts (mask condition, IMD iterations) appear in method section | Same — no change needed |
| Contribution-evidence alignment | Third contribution (experiments) is a performance-only claim | Replaced with specific experimental findings (gating gain, occlusion robustness) |

The proposed storyline is preferred because it establishes a clearer research gap (existing methods lack shape guidance) and frames the contribution around a specific technical insight (iterative refinement via generation-segmentation alternation) rather than a general "bridging" claim.

## Priority Revision Plan
### P0 — Critical (must fix before resubmission)

| ID | Task | Effort | Impact | Related Annotation |
|----|------|--------|--------|-------------------|
| P0.1 | Fix Eq. (1) circular dependency and binary mask noise model | Low (text edit) | High — removes mathematical error | ee3db9f4 |
| P0.2 | Add full-image FID and discuss background bias | Medium (re-run evaluation) | High — restores evaluation credibility | f4fbe070 |
| P0.3 | Report optimized inference time + baseline comparison | Low (add rows to Table 2) | Medium — transparency on practical cost | 3caf0bad |
| P0.4 | Add quantitative results for training without complete objects | Medium (evaluate on OpenImage split) | High — validates generalization claim | 1eb214b2 |

### P1 — Major (should fix for strong submission)

| ID | Task | Effort | Impact | Related Annotation |
|----|------|--------|--------|-------------------|
| P1.1 | Specify gating mechanism with sigmoid range and timestep behavior | Low (add 2-3 sentences) | Medium — improves reproducibility | fcdfe797 |
| P1.2 | Revise Conclusion with quantitative summary + limitations | Low (text rewrite) | Medium — improves scientific rigor | 04b7119a |
| P1.3 | Clarify slack condition and Gibbs consistency in Section 3.3 | Low-Medium (add paragraph) | Medium — strengthens theoretical framing | a9c7ffaa |
| P1.4 | Revise third contribution bullet to state specific findings | Low (text edit) | Low-Medium — improves contribution clarity | ef9b059b |

### P2 — Nice-to-have (quality improvements)

| ID | Task | Effort | Impact | Related Annotation |
|----|------|--------|--------|-------------------|
| P2.1 | Mask voting threshold sensitivity analysis (τ ∈ {0.3, 0.7}) | Low (add ablation) | Low — robustness demonstration | 022f5bda |
| P2.2 | Restructure related work around comparison axes | Medium (rewrite paragraphs) | Medium — improves positioning | 5337af53, e622945a |
| P2.3 | Abstract rewrite with gap statement | Low (text edit) | Low-Medium — improves first impression | f3a98d6d |
| P2.4 | Introduction P1 rewrite with sharper gap definition | Low (text edit) | Medium — clarifies motivation | 7f559a8d |

### Revision Sequence Recommendation

1. **Text fixes first (P0.1, P1.1, P1.2, P1.3, P1.4, P2.3, P2.4):** These require only editing and no new experiments; they can be done immediately.
2. **Evaluation additions (P0.2, P0.3, P0.4, P2.1):** These require re-running the model/baselines; plan 1-2 weeks of compute.
3. **Related work rewrite (P2.2):** This requires literature review; plan alongside evaluation runs.

### Page Coverage Audit

| Page | Section | Annotation Count | Coverage Status |
|------|---------|-----------------|-----------------|
| 1 | Abstract + Intro P1 | 2 | Covered |
| 2 | Intro P2 + Related Work 2.1 | 2 | Covered |
| 3 | Related Work 2.2 + Method (Problem, Eq.1) | 2 | Covered |
| 4 | Method (Diffusion model, Eq. symbol issue) | 1 | Covered |
| 5 | Method (Gating, Segmentation, Voting) | 2 | Covered |
| 6 | Method (Discussion, Gibbs sampling) | 1 | Covered |
| 7 | Experiments (Table 1, FID metrics) | 1 | Covered |
| 8 | Experiments (Ablations, Inference time) | 1 | Covered |
| 9 | Conclusion | 1 | Covered |
| 10 | Appendix (Image diffusion vs mask denoising) | 1 | Covered |
| 11 | Appendix (Training without complete obj.) | 1 | Covered |
| 12-16 | User study details, more visualizations | 0 | Skipped (non-substantive/boilerplate) |
| 17-19 | References | 0 | Skipped (bibliography) |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|-----------------|-------------------|
| Main Results (Table 1) | Compare MaskComp against ControlNet, Kandinsky, SD 1.5, SD 2.1 | AHP, DYCE datasets; FID-G, FID-S, user study | FID-G, FID-S, Avg Rank, Best % | MaskComp achieves lowest FID and best user ranking | Mask-conditioned IMD outperforms unconditional baselines | Object-area-only FID may favor MaskComp's black-background training; no full-image FID reported |
| Mask Conditioning (Table 2a) | Test if mask completeness improves generation quality | AHP; visible vs noisy vs complete masks | FID | Complete mask gives best FID (12.7), visible mask worst (16.9) | Mask quality directly affects generation quality | Ablation only on AHP; generalization to DYCE not tested |
| Occlusion Rate (Table 2b) | Test robustness to increasing occlusion | AHP; 20%-80% occlusion | FID | FID stays stable up to 60% (17.2), degrades at 80% (29.9) | MaskComp is robust up to 60% occlusion | Only tested on AHP; no other occlusion types tested |
| Inference Time (Table 2c) | Measure per-step timing | AHP; single V100 GPU | Seconds per component | Gen: 14.3s, Segm: 1.2s, Total: 15.5s per step | IMD is computationally expensive | No baseline comparison; optimized time not reported in absolute terms |
| IMD Steps (Table 3a) | Test effect of iteration count | AHP; T∈{1,3,5,7} | FID | FID improves from 24.7 (T=1) to 16.1 (T=7), saturates near T=5 | More iterations improve mask quality | Diminishing returns beyond T=5 |
| Sampled Images (Table 3b) | Test effect of N | AHP; N∈{4,5,6} | FID | FID slightly improves with larger N (17.4→16.8) | More samples give better voting | Small range tested (4-6 only) |
| Diffusion Iterations (Table 3c) | Test effect of diffusion budget | AHP; iter∈{20,40,50} | FID | More iterations improve FID (16.9→15.1) | Standard diffusion quality-speed trade-off | Already well-known result |
| Gating (Table 3d) | Test if time-variant gating helps | AHP; with vs without gating | FID | Gating improves FID from 18.2 to 16.9 (1.3 gain) | Gating is beneficial | Small absolute gain; no analysis of gating behavior across timesteps |
| Segmentation Model (Table 4a) | Compare SAM vs Mask2Former vs ClipSeg | AHP | FID | SAM best (16.9), ClipSeg 19.9, Mask2Former 22.5 | SAM is the best choice among tested models | Only 3 models tested; no analysis of why SAM is better |
| Voting Strategy (Table 4b) | Compare logits voting vs mask voting, voting vs mean | AHP | FID | Logits+Voting best (16.9) | Voting with logits is best | Only 4 strategies tested |
| Amodal Baseline (Table 4c) | Compare against AISFormer+ControlNet | AHP | FID | MaskComp (16.9) vs AISFormer+CN (29.4) | IMD outperforms single-pass amodal segmentation + generation | Single baseline comparison; no state-of-the-art amodal methods |
| Occlusion Type (Table 4d) | Test rectangle vs oval vs object-shaped occlusion | AHP | FID | Rectangle: 15.3, Oval: 15.1, Object: 16.9 | Object-shaped occlusion is hardest | Only tested on AHP |

### Research-Theme Gap Diagnosis

1. **New knowledge gap:** The paper's primary conceptual novelty (iterative generation-segmentation for mask refinement) is demonstrated empirically, but the theoretical understanding is weak. The Gibbs sampling analogy is not formally validated, and the "slack condition" enabling the approach is never concretely specified.

2. **Reproducibility gap:** Critical implementation details are missing: (a) the gating mechanism is underspecified, (b) the mask interpolation strategy during training is described only qualitatively, (c) the OpenImage training protocol details are in the appendix but the data filtering criteria are not specified.

3. **Impact on practice gap:** The 77s/image inference cost is a major barrier to practical adoption. No analysis of how to reduce this (e.g., through distillation, fewer samples, or faster backbones) is provided.

### Proposed Research Experiments

#### P0 Experiments (Complete before resubmission)

**Exp-A: Full-image FID evaluation (Targets W2)**
- **Target Claim:** MaskComp outperforms baselines in object completion quality.
- **Hypothesis:** The gap narrows but remains significant under full-image FID.
- **Minimal Design:** Compute standard full-image FID (not object-area-cropped) on AHP and DYCE for all methods in Table 1.
- **Controls/Baselines:** Same baselines as Table 1.
- **Metrics:** Full-image FID.
- **Success Criterion:** MaskComp still achieves lowest FID (gap may narrow).
- **Estimated Cost/Time:** 1 GPU-day (re-running evaluation on existing generated images).
- **Expected Paper-Quality Gain:** Restores evaluation fairness; addresses the most serious validity concern.

**Exp-B: Training without complete masks — quantitative evaluation (Targets W4)**
- **Target Claim:** MaskComp can be trained without complete ground-truth masks.
- **Hypothesis:** FID of the "no-complete-mask" variant is within 2-3 points of the full-supervision version.
- **Minimal Design:** Evaluate the OpenImage-trained model (Section 4.2 mentions training on OpenImage) on a held-out test set; compute FID-G and FID-S.
- **Controls/Baselines:** Compare against the standard MaskComp trained with complete masks on same data.
- **Metrics:** FID-G, FID-S.
- **Success Criterion:** FID < 25 (or within 3 points of the full-supervision model).
- **Estimated Cost/Time:** 1 GPU-day (inference on existing model).
- **Expected Paper-Quality Gain:** Validates a key generalization claim.

#### P1 Experiments (Strongly recommended)

**Exp-C: Gating mechanism analysis (Targets W5)**
- **Target Claim:** Time-dependent gating improves generation quality by 1.3 FID.
- **Hypothesis:** The gating scalar g_τ decreases monotonically from ~1 to ~0 across diffusion timesteps.
- **Minimal Design:** Log g_τ values at each timestep τ during inference and plot g_τ vs. τ.
- **Controls/Baselines:** Compare gating vs. no-gating visually on failure cases.
- **Metrics:** g_τ plot, FID.
- **Success Criterion:** g_τ shows interpretable behavior (high early, low late).
- **Estimated Cost/Time:** 0.5 GPU-day (single inference logging run).
- **Expected Paper-Quality Gain:** Makes gating mechanism transparent and reproducible.

**Exp-D: Inference speed-quality Pareto frontier (Targets W3)**
- **Target Claim:** MaskComp can be accelerated to 2/3 original time with only 0.5 FID penalty.
- **Hypothesis:** There exists a (T, N, diffusion_iter) configuration that achieves FID < 18 at <30s per image.
- **Minimal Design:** Sweep (T in {1,3,5}, N in {3,4,5}, diffusion_iter in {10,20,30}) and report FID vs. total inference time.
- **Controls/Baselines:** Default MaskComp (T=5, N=5, iter=50).
- **Metrics:** FID, total inference time (seconds/image).
- **Success Criterion:** Identify at least one configuration with <30s inference and FID < 18.
- **Estimated Cost/Time:** 2-3 GPU-days (systematic sweep).
- **Expected Paper-Quality Gain:** Provides practical guidance for deployment.

#### P2 Experiments (Quality improvements)

**Exp-E: Mask voting threshold sensitivity (Targets W10)**
- **Target Claim:** Voting threshold τ=0.5 is near-optimal.
- **Hypothesis:** FID is stable for τ ∈ [0.3, 0.7].
- **Minimal Design:** Test τ ∈ {0.3, 0.4, 0.5, 0.6, 0.7} on AHP.
- **Metrics:** FID.
- **Expected Gain:** Demonstrates robustness of voting mechanism.

```text
ASCII Diagram — Experiment Upgrade Plan
Stage 1 (P0, must fix, ~2 GPU-days)
├── Exp-A: Full-image FID for all methods
└── Exp-B: Quantitative eval of OpenImage model
    │
    ▼
Stage 2 (P1, strongly recommended, ~3 GPU-days)
├── Exp-C: Gating mechanism analysis (g_τ vs τ plot)
└── Exp-D: Speed-quality Pareto frontier (T×N×iter sweep)
    │
    ▼
Stage 3 (P2, nice-to-have, ~0.5 GPU-day)
└── Exp-E: Threshold sensitivity (τ ∈ [0.3, 0.7])
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5 / 10**

**Score rationale:** The paper presents a conceptually appealing iterative refinement framework for object completion and demonstrates substantial FID improvements over strong baselines. However, several weaknesses reduce the score below the acceptance threshold:

- **Research value (primary dimension):** The empirical demonstration is solid, but the conceptual novelty is incremental (adapting ControlNet + SAM in a loop). The mathematical framing contains errors (Eq. 1 circularity), and the Gibbs sampling analogy is not rigorously validated. _Score weight: 6/10._
- **Validity and soundness:** The FID evaluation using object-area cropping raises fairness concerns. The inference cost is prohibitive but not adequately disclosed. The "training without complete objects" claim lacks quantitative support. _Score weight: 6/10._
- **Novelty:** Without external literature verification, the novelty position cannot be definitively established. Based on manuscript evidence alone, the core contribution (iterative generation-segmentation loop) is a reasonable engineering contribution but not a fundamental algorithmic breakthrough comparable to works at top venues. _Score weight: 6/10._
- **Reproducibility:** Missing implementation details (gating mechanism specification, mask interpolation protocol) and the heavy reliance on frozen Stable Diffusion and SAM limit independent reproducibility. _Score weight: 5/10._

**Post-Revision Target: [7.5, 8.0] / 10**

If the authors address all P0 and P1 items (fix Eq. (1), add full-image FID, report inference time transparently, quantify the "no-complete-mask" setting, specify the gating mechanism, revise the conclusion, and clarify the Gibbs framing), the score could rise to 7.5-8.0. The upper bound is constrained by the inherently incremental nature of the contribution and the strong dependence on existing foundation models (Stable Diffusion + SAM).