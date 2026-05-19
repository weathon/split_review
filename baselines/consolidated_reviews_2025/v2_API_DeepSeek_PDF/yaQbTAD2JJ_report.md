## Summary
This paper presents CUBE-LLM, a multi-modal large language model that extends 2D MLLMs to 3D grounding and reasoning from RGB images. The authors introduce LV3D, a large-scale pretraining dataset unifying 24 2D and 3D recognition datasets under a multi-turn QA formulation, totaling ~9.6M images and ~40.9M QA pairs. The method achieves this through three key components: (1) data standardization via virtual camera projection following Omni3D, (2) task scaling that decomposes 3D labels into subtasks (2D point/box, depth, 3D point/box), and (3) visual chain-of-thought training that interleaves easy-to-hard QA sequences. CUBE-LLM builds on LLaVA-1.5 with DINOv2 vision encoder and two-stage training (low-res frozen-encoder stage followed by high-res full finetuning).

The main results show: (1) On Talk2Car 3D grounding, CUBE-LLM with LiDAR specialist prompting achieves 71.4 BEV APA (+21.3 vs prior LiDAR-vision methods), while camera-only reaches 79.2 AP0.5 on 2D grounding (+5.7 vs prior SOTA FA). (2) On DriveLM, BEV APA improves from 33.2 to 66.0, and overall QA score from 32.4 to 50.1. (3) On refCOCO/+/g, CUBE-LLM achieves 87.0 average, competitive with state-of-the-art generalist MLLMs. (4) General VQA performance is preserved versus LLaVA-1.5, confirming no degradation from 3D training.

The paper is well-structured, the problem is timely, and the LV3D dataset is a valuable resource. However, several issues limit the current version: overclaiming "pure data scaling" given significant architectural and training design choices, missing variance and significance testing, unclear separation of camera-only vs LiDAR-assisted results, and limitations deferred to the appendix. With revisions addressing these issues, the paper would be substantially stronger.

## Strengths
**S1. Timely and well-motivated problem.** Extending MLLMs from 2D to 3D grounding is a natural and important research direction with clear practical applications in autonomous driving, robotics, and AR/VR. The paper correctly identifies that prior MLLMs operate in 2D image coordinates and cannot reason about object depth, size, and orientation in 3D space.

**S2. Large-scale unified dataset (LV3D).** The authors compile and standardize 24 existing datasets into a single multi-turn QA format comprising ~9.6M images and ~40.9M QA pairs. This is a significant engineering contribution that the community can build upon. The dataset blending of 2D and 3D data, along with automatic QA generation from existing labels, is thoughtful and practical.

**S3. Clean ablation study on DriveLM-Grounding.** Table 2(b) provides a clear sequential ablation showing the contribution of each component (CLIP→DINOv2: +6.4 BEV APA, +LV3D 2D: +10.9, +LV3D 3D: +15.5). This decomposition is informative and convincingly shows that each design choice adds value.

**S4. Visual chain-of-thought is a neat contribution.** The idea of training the model with easy-to-hard QA sequences (2D first, then 3D) to enable test-time CoT prompting is elegant and leverages the autoregressive nature of LLMs without requiring architectural changes. The 3.2-point zero-shot improvement from V-CoT training (Figure 5) validates the concept.

**S5. Strong empirical results on multiple benchmarks.** CUBE-LLM achieves impressive gains on Talk2Car 3D grounding (21.3 BEV APA with LiDAR prompting) and competitive results on refCOCO (87.0 average), while maintaining general VQA capability. The comprehensive evaluation across 3D grounding, complex reasoning, and standard MLLM benchmarks strengthens the paper's claims.

**S6. Detailed failure analysis.** Appendix F provides a thoughtful breakdown of failure modes (inaccurate depth, semantic confusion) with visual examples. This transparency helps readers understand the method's limitations and guides future improvement directions.

## Weaknesses
**W1. Overclaimed "pure data scaling" narrative (Major).** The paper repeatedly claims that "pure data scaling enables 3D understanding without 3D-specific architectural design or training objectives." This is contradicted by multiple design choices: (1) DINOv2 visual encoder is explicitly selected over CLIP for 3D superiority, (2) two-stage training with frozen/unfrozen components is an explicit training strategy, (3) coordinate normalization, log-scale depth, virtual camera standardization, and Euler angle ordering are representational engineering choices, (4) the V-CoT curriculum and task decomposition with 30 QA pairs per object are deliberate training designs. The core contribution — demonstrating that 3D grounding can be achieved without a dedicated 3D detection head or point cloud encoder — is still valuable and should be stated accurately.

**W2. No variance or statistical significance reporting (Major).** None of the 5 tables report standard deviations, confidence intervals, or significance tests. This is a significant concern because many comparisons show small differences (e.g., Table 5: CUBE-LLM 7B vs LLaVA-1.5 7B on GQA: 62.4 vs 62.0, +0.4; on VizWiz: 51.0 vs 50.0, +1.0). Without multi-seed experiments, readers cannot assess whether claims of improvement are statistically reliable.

**W3. Mixed presentation of camera-only vs LiDAR-assisted results (Major).** The abstract and introduction present the 21.3-point BEV APA improvement as a headline result without clarifying that this is achieved with LiDAR specialist prompting (CenterPoint proposals). The camera-only improvement is +5.7 2D AP0.5 and +15.7 BEV APA vs Talk2Car-3D (which uses LiDAR+RGB). These settings are fundamentally different and should be clearly separated throughout the paper.

**W4. Limitations deferred to appendix (Major).** Important limitations — single-frame input, no token resampling, moving/stationary confusion — are only in Appendix G and not mentioned in the main paper's conclusion. The conclusion instead makes a broad claim about "pure transformer-based MLLM with minimal inductive bias can learn about 3D understanding solely by data scaling" that does not acknowledge these significant limitations.

**W5. Unfair baseline comparisons (Medium).** Camera-only CUBE-LLM is compared against 2D specialist models using smaller backbones and less data. A controlled comparison where a competitive baseline (e.g., FA or Stacked VLBert) is retrained on the same LV3D data mixture would isolate architecture benefits from data benefits. The DriveLM baseline achieving 0.0 accuracy is also suspicious and needs explanation.

**W6. Equation (8) is mathematically imprecise (Medium).** The "maximize" formulation in the V-CoT section does not correspond to the actual training objective, which is standard autoregressive next-token prediction. This could confuse readers about the optimization procedure.

**W7. Evaluation metric "Overall" in DriveLM-QA is poorly defined (Medium).** The paper mentions combining "accuracy, match, BLEU/ROUGEL/CIDEr, and ChatGPT score" but does not specify the aggregation formula, making the result non-reproducible. The sub-metrics show different patterns: accuracy is identical (38.5) between CUBE-LLM and LLaVA-1.5 on the baseline split, yet Overall differs by 14 points — the weighting clearly favors CUBE-LLM's output style but the formula is opaque.

## Key Issues
**Issue 1: Claim-evidence gap in "data scaling" narrative (P0 Critical).**
- **Location**: Page 1 Abstract, Page 2 Introduction second paragraph, Page 10 Conclusion.
- **Problem**: The paper claims 3D understanding emerges from "pure data scaling" and "without 3D-specific architectural design or training objectives," but the method uses DINOv2 (selected for 3D superiority), two-stage training, coordinate normalization, log-depth, and V-CoT curriculum — all explicit design choices. This mismatch weakens the paper's core narrative.
- **Impact**: Reviewers familiar with prior work on 3D-aware VLMs (3D-LLM, PointLLM) may view this as overclaiming. A controlled experiment isolating "data scaling" from "task/representation design" is needed.
- **Fix**: (a) Replace "pure data scaling" with "careful data curation and standardized task formulation." (b) Add an ablation fixing architecture while varying only data scale. (c) Acknowledge that DINOv2 selection and task decomposition are deliberate design decisions.

**Issue 2: Missing statistical rigor in all experiments (P0 Critical).**
- **Location**: Tables 1-5 (Pages 7-9), Figures 5 (Page 8).
- **Problem**: No standard deviations, confidence intervals, or significance tests are reported. Many key comparisons are small (VQA: +0.2 on 78.3 vs 78.5; GQA: +0.4). Without statistics, readers cannot assess whether improvements are reproducible or noise.
- **Impact**: High risk of irreproducibility claims. The 21.3-point gain on Talk2Car BEV APA may be robust, but this cannot be verified without variance.
- **Fix**: Report mean and std over >=3 seeds for all main tables. Add paired bootstrap significance tests for the key Talk2Car comparison. Even for large-scale pretraining (which is expensive), a 2-3 seed evaluation on the fine-tuned models is feasible.

**Issue 3: Camera-only vs LiDAR-assisted conflated in headline claims (P0 Critical).**
- **Location**: Page 1 Abstract lines 23-24, Page 2 Introduction lines 37-38.
- **Problem**: The 21.3-point BEV APA improvement is achieved with LiDAR specialist prompting (CenterPoint proposals), not camera-only. The camera-only model achieves 46.3 BEV APA, which trails MSSG (50.1) — the "camera-only outperforms LiDAR-vision" impression is incorrect.
- **Impact**: Misleads readers about the true camera-only capability of CUBE-LLM. The LiDAR-assisted variant depends on an external 3D detector (CenterPoint), so the combined system's performance is not solely attributable to CUBE-LLM.
- **Fix**: Restructure the abstract to first present camera-only results, then present LiDAR-assisted results with explicit disclaimers. In the introduction, state: "With camera-only input, CUBE-LLM achieves X; when augmented with a LiDAR-based specialist, it further reaches Y."

**Issue 4: Limitations absent from main text (P1 Major).**
- **Location**: Page 10 Conclusion, Appendix G (Page 21).
- **Problem**: Important limitations (single-frame, no token resampling, depth error, semantic confusion) are only in the appendix. The conclusion makes broad, unsupported claims.
- **Impact**: Reviewers may view this as lack of scientific candor. The paper's claims about "3D understanding" are overly strong given that depth estimation is a primary failure mode.
- **Fix**: Move limitations to main-text conclusion. Add quantitative depth error analysis. Bound all claims to single-frame, box-level 3D understanding from RGB.

**Issue 5: Eq. (8) uses incorrect mathematical formalism (P1 Major).**
- **Location**: Page 5 Section 3.3.
- **Problem**: "maximize { p(A|Q), p(A|Q,A,Q), ... }" is not a well-defined optimization problem. The actual training is standard autoregressive next-token prediction on concatenated multi-turn sequences.
- **Impact**: Mathematical imprecision reduces reproducibility and may confuse readers about the actual training procedure.
- **Fix**: Replace Eq. (8) with the actual log-likelihood objective and describe the multi-turn sequence as a standard causal language modeling loss.

## Actionable Suggestions
**Suggestion 1: Revise the "data scaling" narrative (Must, P0).**
Replace all instances of "pure data scaling" and "without 3D-specific architectural design or training objectives" with more accurate descriptions. Suggested replacements:
- Abstract: "We show that careful data curation and task design enable a standard MLLM to perform 3D grounding without task-specific 3D detection heads or point cloud encoders."
- Introduction: "Our approach centers on data and task design rather than specialized 3D architectures."
- Conclusion: Remove "solely by data scaling."

**Suggestion 2: Add statistical reporting to all tables (Must, P0).**
For Tables 2-5 and Figure 5, report mean and standard deviation over at least 3 random seeds. For the large-scale Talk2Car experiment, a 3-seed fine-tuning with different random seeds (varying data shuffle, weight initialization) is feasible within one additional training run. Report the seed values used.

**Suggestion 3: Restructure headline claims to separate camera-only and LiDAR results (Must, P0).**
Revise the abstract to first present camera-only results, then LiDAR-assisted results with explicit context. Example structure:
- Sentence 4: "With only camera input, CUBE-LLM achieves 79.2 AP0.5 on Talk2Car 2D grounding and 46.3 BEV APA on 3D grounding."
- Sentence 5: "When augmented with a LiDAR-based 3D detector (CenterPoint), CUBE-LLM reaches 71.4 BEV APA, outperforming prior LiDAR-vision methods by 21.3 points."

**Suggestion 4: Move limitations to main text (Must, P1).**
Add a Limitations subsection to the Conclusion section covering: (a) single-frame limitation, (b) depth estimation inaccuracy, (c) semantic confusion under similar appearance, (d) no token resampling limiting resolution scaling, (e) box-level 3D only (no segmentation or free-form 3D reasoning). Add quantitative depth error analysis (mean absolute depth error, correlation with distance).

**Suggestion 5: Add a controlled 2D baseline retrained on LV3D (Nice-to-have, P1).**
To fairly demonstrate that CUBE-LLM's architecture contributes beyond data, retrain a competitive 2D baseline (e.g., FA or Stacked VLBert) on the same LV3D data mixture for 2D grounding. This would isolate the benefit of the MLLM architecture from the benefit of more/better training data.

**Suggestion 6: Fix Eq. (8) and clarify V-CoT training objective (Must, P1).**
Replace "maximize { p(...), p(...), ... }" with the standard autoregressive language modeling loss applied to multi-turn sequences. See the detailed fix in the annotation on Page 5.

**Suggestion 7: Define the DriveLM "Overall" metric explicitly (Must, P1).**
Report the decomposition: state the weighting of accuracy, match, BLEU/ROUGEL/CIDEr, and ChatGPT score. Ideally, report each sub-metric separately in a supplementary table.

**Suggestion 8: Clarify the data leakage risk (Nice-to-have, P2).**
The paper uses GRIT (linked to Kosmos-2) and AS-filtered (linked to All-Seeing) which may overlap with evaluation datasets. Provide a data overlap analysis between training sources and evaluation benchmarks (especially refCOCO and VQAv2).

**Suggestion 9: Report training compute cost (Nice-to-have, P2).**
Add total GPU-hours for pretraining and fine-tuning stages. This aids reproducibility assessment.

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current introduction follows: MLLMs are powerful (background) -> MLLMs do 2D grounding well but not 3D (gap) -> We use pure data scaling to solve this (solution) -> We have results (evidence). The main weaknesses are: (1) the gap statement is too binary ("has not explored"), ignoring existing point-cloud-based 3D LLMs; (2) the "data scaling" claim overstates what is demonstrated; (3) results mixing camera-only and LiDAR-assisted settings confuses the takeaway.

### Recommended Storyline (Candidate A)

**Big Picture -> Precise Gap -> Solution Intuition -> Method Highlights -> Key Results (separated by setting) -> Contribution Summary**

Paragraph breakdown:

**P1 (Background):** MLLMs have achieved strong 2D vision-language capabilities through large-scale pretraining. A critical aspect is grounding language to image coordinates, which enables referring and reasoning about visual content. However, the physical world is 3D — for autonomous driving, robotics, and AR, models must reason about object positions, sizes, and orientations in 3D space.

**P2 (Gap):** Prior MLLMs operate solely in 2D image space. While 3D-aware LLMs exist (e.g., 3D-LLM, PointLLM), they require point cloud encoders or 3D-specific architectures. No prior work has shown that a standard 2D-pretrained MLLM can acquire 3D grounding from RGB images alone through data and task design — without 3D detection heads or LiDAR inputs.

**P3 (Solution Intuition):** We hypothesize that if 3D labels are standardized into the same token representation as 2D labels, and if training tasks are structured in a 2D-to-3D progression, an autoregressive MLLM can learn 3D grounding as an extension of its existing 2D capability. We test this by constructing LV3D, a large-scale unified dataset, and training CUBE-LLM with visual chain-of-thought.

**P4 (Method Highlights):** Key ideas: (a) data standardization via virtual camera projection; (b) task scaling by decomposing 3D labels into subtasks; (c) visual CoT with easy-to-hard QA sequences; (d) DINOv2 encoder for improved spatial understanding.

**P5 (Key Results, separate settings):** With camera-only input, CUBE-LLM achieves strong 2D grounding (79.2 AP0.5 on Talk2Car) and competitive 3D grounding (46.3 BEV APA). When augmented with LiDAR-based proposals, it reaches 71.4 BEV APA (+21.3 over prior LiDAR-vision methods). On DriveLM, the framework nearly doubles BEV APA (33.2 to 66.0). CUBE-LLM also achieves 87.0 average on refCOCO and maintains strong general VQA performance.

**P6 (Contribution Summary):** (1) LV3D dataset, (2) unified training framework, (3) demonstration that 3D grounding is achievable without 3D-specific heads, (4) visual CoT and specialist prompting capabilities.

### Abstract Outline (Complete)

**S1 (Domain + Challenge):** Multi-modal large language models (MLLMs) have demonstrated strong capabilities in 2D vision and language tasks, but lack the ability to ground and reason about images in 3-dimensional space.

**S2 (Prior Limitation):** While prior work on 3D-aware LLMs relies on point cloud encoders or specialized architectures, it remains unclear whether a standard 2D-pretrained MLLM can acquire 3D grounding from RGB images alone.

**S3 (Method):** We introduce LV3D, a large-scale unified dataset of 2D and 3D recognition data formatted as multi-turn QA, and CUBE-LLM, an MLLM trained on LV3D with data standardization, task decomposition, and visual chain-of-thought.

**S4 (Key Results — Camera-only):** With camera-only input, CUBE-LLM achieves 79.2 AP0.5 on Talk2Car 2D grounding, improving over prior methods by 5.7 points. On DriveLM, our framework improves 3D grounding BEV APA from 33.2 to 66.0 and overall QA score from 32.4 to 50.1.

**S5 (Key Results — Augmented + General):** When augmented with a LiDAR-based specialist detector, CUBE-LLM reaches 71.4 BEV APA on Talk2Car (+21.3 vs prior LiDAR-vision methods). CUBE-LLM also achieves 87.0 average on refCOCO and maintains strong general VQA performance, demonstrating that 3D capability is additive without degrading 2D reasoning.

### Introduction Outline (Complete)

Following the Candidate A storyline above (P1-P6), each paragraph's role, claim, and evidence anchor:

- **P1 (Background & Motivation):** State that MLLMs excel at 2D tasks but the world is 3D. Anchor: mention autonomous driving and robotics as concrete applications needing 3D understanding.
- **P2 (Precise Gap):** Differentiate from point-cloud-based 3D LLMs. Claim: "No prior work achieves 3D grounding from RGB images using a standard 2D-pretrained MLLM without 3D-specific heads."
- **P3 (Approach Intuition):** Explain the core hypothesis about autoregressive 2D-to-3D transfer. Evidence anchor: Eq. (1-4) showing token format unification.
- **P4 (Method Summary):** List four key components with section references.
- **P5 (Results Preview — Separated):** First camera-only results with explicit numbers, then LiDAR-assisted results with explicit "when augmented" language.
- **P6 (Contributions):** Four numbered contributions as listed above.

## Priority Revision Plan
| Priority | Task | Effort | Impact | Related Issue |
|---|---|---|---|---|
| **P0** | Revise "pure data scaling" narrative across abstract, intro, conclusion | Low (wording) | High (accuracy, reviewer trust) | Issue 1 |
| **P0** | Add statistical reporting (std, CI, seeds) to all main tables | Medium (compute) | High (reproducibility, credibility) | Issue 2 |
| **P0** | Restructure abstract to separate camera-only and LiDAR results | Low (wording) | High (clarity, fairness) | Issue 3 |
| **P0** | Fix Eq. (8) to use correct autoregressive objective | Low (wording) | High (mathematical precision) | Issue 5 |
| **P1** | Move limitations from appendix to main-text conclusion | Low (wording) | Medium (completeness) | Issue 4 |
| **P1** | Define DriveLM "Overall" metric decomposition and sub-metrics | Low (wording) | Medium (reproducibility) | Issue 7 |
| **P1** | Add controlled 2D baseline retrained on LV3D | Medium (compute) | Medium (fair comparison) | Issue 6 |
| **P1** | Add depth error analysis (mean absolute error, distance correlation) | Low (compute) | Medium (transparency) | Issue 4 |
| **P2** | Report total training GPU-hours | Low (wording) | Low (reproducibility) | Suggestion 9 |
| **P2** | Add data overlap analysis (training vs evaluation) | Low (compute) | Low (leakage risk) | Suggestion 8 |

### Revision Execution Order (Recommended)

1. **Week 1 — Text revisions only**: Fix P0 wording issues (narrative, abstract structure, Eq. 8, limitations). These require no additional compute and immediately improve accuracy.
2. **Week 2 — Reproducibility experiments**: Add 3-seed evaluation for main tables, compute std and significance tests. Retrain one controlled 2D baseline on LV3D.
3. **Week 3 — Analysis additions**: Add depth error analysis, define DriveLM metric, compute data overlap.
4. **Before resubmission**: Proofread all revised sections for consistency.

### Expected Impact After Revisions

- **Scientific accuracy**: Improved claim-evidence alignment, no overstatement
- **Reproducibility**: Statistical reporting enables verification of claimed gains
- **Fairness**: Clear separation of camera-only vs LiDAR-assisted contributions
- **Completeness**: Limitations transparently stated, metric definitions explicit
- **Score improvement**: Post-revision target of [7, 8]/10 (from current ~6/10)

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | Talk2Car 3D grounding — camera-only | Talk2Car val (1163 samples), fine-tuned at 672×672 | 2D AP0.5, BEV APA/B, 3D APA/B | 79.2 AP0.5, 46.3 BEV APA | Camera-only CUBE-LLM surpasses prior camera-only methods (+5.7 AP0.5) | No variance; compares against methods trained on less data |
| E2 | Talk2Car 3D grounding — LiDAR + specialist prompt | Top-30 CenterPoint proposals as visual prompts | Same as E1 | 71.4 BEV APA (+21.3 vs MSSG) | LiDAR prompting greatly improves 3D accuracy | Performance ceiling set by CenterPoint proposal quality |
| E3 | DriveLM-Grounding ablation | DriveLM-Grounding (600 train scenes) | BEV APA/B, 3D APA/B | 66.0 BEV APA (vs 33.2 LLaVA baseline) | Each component (DINOv2, 2D data, 3D data) adds value | Ablation does not isolate V-CoT from 3D data |
| E4 | DriveLM-QA complex reasoning | DriveLM-QA (96 val scenes) | Acc, Match, Overall | Overall 50.1 (baseline split) | Pretraining improves driving QA reasoning | "Overall" metric is a black-box composite |
| E5 | Indoor 3D grounding | Objectron, ArkitScenes, SUN-RGBD | mAPcls3D, mAPcls+loc3D | +13.1 (Obj), +1.9 (Arkit), +4.2 (SUN) | Outdoor data scaling transfers to indoor | Large variance across datasets unexplained |
| E6 | refCOCO/+/g 2D grounding | 8 standard test splits | Accuracy per split | 87.0 average | Competitive with SOTA generalist MLLMs | Small margin vs Qwen-VL (85.7) and Ferret (83.9) |
| E7 | General VQA benchmarks | VQAv2, GQA, VizWiz, SQA, POPE | Accuracy per benchmark | Competitive with LLaVA-1.5 | 3D training does not degrade 2D VQA | Some metrics show near-identical scores (VQAv2: 78.3 vs 78.5) |
| E8 | Zero-shot Talk2Car with data scaling | Varying % of LV3D, zero-shot eval | BEV APA | Scaling improves performance monotonically | Data scaling benefits 3D grounding | Only zero-shot; fine-tuned scaling not shown |
| E9 | V-CoT ablation (zero-shot) | Zero-shot Talk2Car with/without V-CoT training | 3D AP | V-CoT adds +3.2 points | V-CoT training improves CoT prompting | Zero-shot only; fine-tuned V-CoT benefit not isolated |

### Research-Theme Gap Diagnosis

The paper's intended contributions span three research-value themes:

1. **New knowledge (partially supported)**: The key insight — that standard MLLM architectures can learn 3D grounding through task decomposition and data unification — is supported but weakened by the overclaimed "pure data scaling" narrative. The DINOv2 choice and two-stage training introduce architectural confounds that make it unclear how much of the result is due to data scaling vs architecture/training design.

2. **Reproducibility/Reusability (partially supported)**: LV3D is a valuable resource, but the missing variance reporting, undefined composite metric, and opaque "Overall" score limit reproducibility. Training compute cost is not reported.

3. **Potential to change practice/understanding (moderate)**: If validated, the finding that 3D grounding is achievable without 3D-specific heads could influence MLLM design. However, the reliance on external specialists for top performance weakens this claim.

### Proposed Research Experiments

**P0 Experiment: Controlled Data Scaling Ablation**
- **Target Claim**: "Pure data scaling enables 3D understanding" 
- **Hypothesis**: Increasing data volume alone (without task decomposition or V-CoT) accounts for most of the gain
- **Minimal Design**: Fix the architecture (DINOv2, LLaVA backbone) and training recipe. Compare: (a) baseline LLaVA training, (b) + raw 3D data without task decomposition, (c) + task decomposition, (d) + V-CoT
- **Controls**: Same compute budget, same number of training steps
- **Metrics**: BEV APA on Talk2Car zero-shot
- **Success Criterion**: If (b) ≈ (d), then data scaling dominates; if (d) >> (b), then task design dominates
- **Cost**: ~2-3 additional training runs (feasible with 8×8 A100s within 1-2 days)
- **Expected Gain**: Clarifies the core claim; removes reviewer uncertainty about the "data scaling" narrative

**P1 Experiment: Multi-Seed Variance and Significance**
- **Target Claim**: All quantitative claims of improvement
- **Hypothesis**: The 21.3-point BEV APA gain is statistically significant; smaller gains may not be
- **Minimal Design**: Fine-tune CUBE-LLM on Talk2Car with 3 different random seeds. Report mean ± std for all metrics. Compute paired bootstrap p-value vs MSSG.
- **Controls**: Same hyperparameters, same data order (shuffled with different seeds)
- **Metrics**: BEV APA, 3D APA
- **Success Criterion**: p < 0.05 for the key comparison
- **Cost**: Low (single-node, ~1 day for 3 seeds)
- **Expected Gain**: Core evidence for statistical reliability

**P1 Experiment: Depth Error Analysis**
- **Target Claim**: "CUBE-LLM can ground and reason about images in 3D"
- **Hypothesis**: Depth errors correlate with object distance; close objects are accurately localized
- **Minimal Design**: Compute per-object depth error (predicted - ground truth z) on Talk2Car val. Report MAE, median error, and error vs distance correlation.
- **Controls**: Compare against a simple baseline (e.g., predict mean depth)
- **Metrics**: Mean Absolute Depth Error (m), Spearman correlation with distance
- **Success Criterion**: Error characteristics are informative for downstream use
- **Cost**: Low (analysis only, no training needed)
- **Expected Gain**: Quantifies the actual 3D understanding capability; bounds claims appropriately

**P2 Experiment: Fine-tuned V-CoT Ablation**
- **Target Claim**: "Visual chain-of-thought prompting improves 3D reasoning"
- **Hypothesis**: V-CoT provides gains even after fine-tuning
- **Minimal Design**: On Talk2Car fine-tuned model, compare direct 3D prediction vs V-CoT (first predict 2D box, then 3D box)
- **Controls**: Same model, same input, different prompting
- **Metrics**: BEV APA, 3D APA
- **Success Criterion**: V-CoT prompting outperforms direct prediction
- **Cost**: Minimal (inference only)
- **Expected Gain**: Validates the V-CoT claim under the actual evaluation protocol

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6/10**

This score reflects the paper's substantive strengths (timely problem, large-scale dataset, strong empirical results, clean ablation) weighed against its weaknesses (overclaimed narrative, missing statistical rigor, conflated results, limitations deferred to appendix). The core technical contribution — demonstrating that an MLLM can perform 3D grounding from RGB without 3D detection heads — is valuable and well-supported. However, the presentation overstates what is achieved and omits critical details needed for reproducibility assessment. The score prioritizes research value and novelty as primary dimensions.

**Score breakdown:**
- Research value (primary): 7/10 — timely problem, practical direction, useful dataset
- Novelty (primary): 5/10 — visual CoT and task decomposition are interesting but the core approach (data unification + 2D-to-3D transfer) has partial precedent in Omni3D and 3D-LLM; novelty is moderate and bounded
- Validity/soundness: 5/10 — strengths in empirical demonstrations undercut by missing variance, unfair baselines, conflated settings
- Reproducibility: 5/10 — training details are mostly present but metric aggregation is opaque and variance is missing
- Presentation: 7/10 — generally well-written but the narrative overclaim reduces credibility

**Post-Revision Target: [7, 8]/10**

If the authors address all P0 and P1 items (revise narrative, add statistical reporting, separate camera-only/LiDAR results, move limitations, fix Eq. 8), the score is expected to rise to 7-8/10. The remaining limitations (single-frame, no token resampling, depth inaccuracy) are inherent to the current method and would cap the upper bound at 8/10. Achieving 8+ would require additional methodological contributions such as video input, token compression, or depth-specific architectural improvements.