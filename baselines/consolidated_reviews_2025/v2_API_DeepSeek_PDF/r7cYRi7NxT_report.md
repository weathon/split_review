## Summary
# Final Review Report

## Summary

This paper presents Hierarchical Side-Tuning (HST), a parameter-efficient transfer learning (PETL) method for Vision Transformers (ViTs). The key idea is to separate trainable parameters from the frozen ViT backbone into a lightweight Hierarchical Side Network (HSN) that generates multi-scale pyramid features suitable for both recognition and dense prediction tasks. Three technical components are introduced: (1) Meta-Tokens (MetaT) — learnable prompts prepended to each Transformer block, tuned via layer normalization to align their distribution with patch tokens; (2) Adaptive Feature Bridge (AFB) — a module that reshapes and aligns backbone intermediate activations with HSN feature stages, with a shared linear weight design for parameter efficiency; and (3) Side blocks with cross-attention and FFN that fuse backbone features into multi-scale outputs.

The method is evaluated on VTAB-1k (19 tasks, 76.0% average accuracy with 0.78M parameters), COCO object detection/instance segmentation (3 detectors, 2 schedules), and ADE20K semantic segmentation (2 frameworks). Results show that HST outperforms existing PETL methods across all tasks and, under certain settings (Cascade Mask R-CNN 3x+MS), matches or slightly exceeds full fine-tuning performance.

The paper has clear technical merit: the pyramidal side network design is a well-motivated departure from flat adapter/prompt methods, and the empirical scope across classification, detection, and segmentation is impressive. However, several major issues reduce confidence in the claims: inference efficiency is overstated (actual measurements show HST is ~40-80% slower than full fine-tuning, contradicting claims of no significant slowdown), statistical significance is not reported (single-run results without variance), and some performance claims are selectively favorable (detection superiority only holds under specific schedules). The paper would benefit from more precise claim bounding, additional ablations to isolate component contributions, and a candid discussion of efficiency trade-offs.

## Strengths
1. **Well-motivated architectural departure.** The pyramidal side network (HSN) is a principled solution to a genuine limitation of existing PETL methods: their inability to produce multi-scale features for dense prediction tasks. Unlike flat adapters or single-token prompts, HSN generates four-stage outputs at resolutions {1/4, 1/8, 1/16, 1/32} that integrate naturally with FPN-based detectors and segmentation heads. This design choice is technically sound and addresses a real gap in the literature.

2. **Comprehensive empirical evaluation.** The paper evaluates across 19 classification tasks (VTAB-1k), 3 detection frameworks (Mask R-CNN, Cascade Mask R-CNN, ATSS) on COCO, and 2 segmentation frameworks (Semantic FPN, UperNet) on ADE20K. This breadth is significantly more extensive than typical PETL papers, which often focus on recognition tasks only. The inclusion of both ImageNet-21K and MAE pre-training variants (Appendix B) further strengthens the evaluation.

3. **Strong VTAB-1k results with very few parameters.** HST achieves 76.0% average accuracy with only 0.78M trainable parameters (0.9% of backbone parameters), outperforming full fine-tuning (65.6%) by a substantial margin on this low-data benchmark. The consistent improvement across all 19 tasks — especially on structured/synthetic tasks (+7.9% on SmallNORB/ele, +6.9% on Clevr/Count) — demonstrates that the HSN effectively captures task-relevant features from the frozen backbone.

4. **Ablation study with clear cumulative design.** The progressive ablation in Table 5 traces performance from a bare HSN baseline (72.1%, 30.0 APb) to the full HST (76.0%, 40.5 APb) through four well-defined component additions. This design allows readers to assess each component's marginal contribution, even though some mechanistic interpretations remain incomplete (see Weaknesses).

5. **Practical value for multi-task deployment.** Because the ViT backbone remains frozen and the lightweight HSN is the only trainable component, HST offers a practical advantage for scenarios where a single pre-trained ViT must be adapted to many downstream tasks with limited per-task storage budget — a use case explicitly relevant for cloud-based vision APIs and embedded systems.

## Weaknesses
The following weaknesses are ordered by severity and impact on core validity claims.

1. **Inference efficiency contradiction (Major).** The introduction (Page 2) states: "HST does not necessarily increase inference time significantly because computations for the same level of the backbone network and HSN can be performed in parallel." However, Appendix C Table 7 shows HST has the slowest inference among all PETL methods at every batch size (70.5 imgs/sec at bs=1 vs. 118.0 for full fine-tuning; 240.2 at bs=32 vs. 302.8 for full fine-tuning). The claim is contradicted by the authors' own latency data. The parallel execution argument is presented as current fact when it is a future possibility. This is a factual inaccuracy that must be corrected.

2. **Missing statistical significance (Major).** All results in Tables 1, 2, 3, 5, and 6 are reported as single-point estimates without variance, confidence intervals, or significance tests. Many PETL comparisons are within small margins (e.g., HST 76.00% vs NOAH 73.20% is ~3%, but HST vs AdaptFormer 73.10% is a larger gap). Without multi-seed reporting, readers cannot assess whether improvements are statistically reliable or within noise. This is especially concerning for VTAB-1k where each task has only 1000 training samples, making single-run results potentially unstable.

3. **Selective performance framing (Major).** The detection section (Page 7) claims HST "breaks through this performance limit" and achieves "superior performance." However, under Mask R-CNN 1x schedule, HST (40.5 APb) still trails full fine-tuning (43.1 APb) by 2.6 APb. The superiority claim only holds under specific schedules (3x+MS) and specific detectors (Cascade Mask R-CNN). The narrative should frame HST as competitive with full fine-tuning under extended training, not universally superior.

4. **Incomplete method description — HSN architecture (Major).** Section 3.1 states Side blocks are "evenly distributed" across 4 stages of a 12-block ViT-B, but the distribution ratio (3-3-3-3?) is not explicitly stated. The convolutional stem is mentioned without any architectural details (kernel size, stride, output channels, normalization). These omissions compromise reproducibility.

5. **MetaT recycling benefit not causally isolated (Major).** The claim that routing MetaT outputs to AFB (rather than discarding them as in VPT) improves performance is asserted but not ablated. The ablation in Table 5 combines LN tuning + MetaT, but there is no variant that uses MetaT + discards its outputs while keeping all other HST components. Therefore, the value of the recycling mechanism itself is unknown.

6. **Ablation asymmetry between classification and detection (Major).** The FG Injection component adds +0.8% to classification accuracy but +6.0 APb to detection. This 7.5x difference in relative gain is not explained. Without mechanistic analysis, the reader cannot tell whether FG Injection genuinely provides more benefit to dense tasks or whether detection metrics are simply more sensitive to any improvement.

7. **O(L) complexity claim with unstated constant factor (Minor).** The O(L) linear attention complexity claim is mathematically correct for bounded d and M, but the constant factor (d × M = 768 × 2 = 1536 operations per token) is large enough that it materially affects practical efficiency. This is standard in the efficient attention literature and not a novel contribution; the paper should acknowledge the constant-factor cost.

8. **MAE pre-training results overclaimed (Minor).** The appendix claims HST "maintains a minimal performance gap" on MAE-pretrained models, but CIFAR-100 shows a 9.2% deficit (79.7% vs 88.9%). The claim should be bounded to cases where the gap is genuinely small.

9. **Conclusion adds unsupported speculation (Minor).** The future direction "designing a unified model for simultaneous multiple visual tasks with different HSNs" is not grounded in any preliminary evidence or analysis in the current paper.

## Key Issues
### Issue 1: Inference efficiency claim contradicts measured data (Severity: Major)
**Evidence:** Page 2 claims HST "does not necessarily increase inference time significantly" because of parallel computation. Appendix C Table 7 shows HST achieves 70.5 imgs/sec at bs=1 vs. 118.0 for full fine-tuning — a 40% slowdown. At bs=32, HST achieves 240.2 vs. 302.8 imgs/sec. The parallel computation is not implemented; all measurements are from serial execution.

**Impact:** This factual inaccuracy undermines credibility across the efficiency narrative. A reader who checks Appendix C will find the claim contradicted, reducing trust in other claims.

**Fix:** Replace the efficiency claim in the introduction with: "In our current implementation, HST incurs higher inference latency than baseline PETL methods (see Appendix C), but the architecture is designed for parallel execution at matched backbone stages, which is left for future work."

### Issue 2: Statistical evidence insufficient for strong claims (Severity: Major)
**Evidence:** Tables 1, 2, 3 report single-run results. The paper states results "strongly validate the effectiveness and parameter efficiency" (Page 7) and "consistently outperforms" (Page 9). 

**Impact:** Without variance or significance tests, the stated confidence level is not supported by the evidence. For publication at ICLR, multi-seed reporting with confidence intervals is standard practice.

**Fix:** Report mean ± std over 3-5 seeds for all main results. Add a supplementary table with statistical significance tests (paired t-test against the best baseline per task). If full multi-seed VTAB-1k is too expensive, run at least 3 seeds on a representative subset (1 task per category) and state the limitation transparently.

### Issue 3: Related work lacks systematic comparison axes (Severity: Major)
**Evidence:** The PETL related work (Page 3) lists methods sequentially without a structured comparison. The key differentiating claim — that HST uses a pyramid architecture while Side-Tuning and LST use flat architectures — is stated but not quantified or tabulated.

**Impact:** Reviewers familiar with the side-tuning family (Zhang et al., 2020a; Sung et al., 2022) may question the novelty increment without an explicit side-by-side comparison.

**Fix:** Add a comparison table covering: (a) where trainable params are inserted, (b) number of feature scales produced, (c) whether intermediate activations are reused, (d) parameter count for ViT-B/16, and (e) reported dense prediction performance.

## Actionable Suggestions
### P0 — Must Fix Before Resubmission

**S1. Correct the inference efficiency overclaim.**
- **Location:** Page 2, Introduction, Paragraph 2 ("HST does not necessarily increase inference time significantly").
- **Action:** Replace with a candid statement: "Currently, HST is implemented serially and incurs higher inference latency than other PETL methods (see Appendix C), but the architecture is designed for future parallel execution."
- **Expected benefit:** Removes a factual contradiction and improves trustworthiness.

**S2. Add variance/statistical significance to all main tables.**
- **Location:** Tables 1, 2, 3, 5, and 6.
- **Action:** Report mean ± std over 3-5 seeds. Add a footnote stating the number of runs.
- **Fallback:** If full multi-seed is infeasible, run 3 seeds on a representative subset (e.g., VTAB-1k: 1 Natural, 1 Specialized, 1 Structured task; COCO: Mask R-CNN 1x; ADE20K: UperNet) and report variance for those while noting the limitation.
- **Expected benefit:** Enables reviewers to assess statistical reliability of all reported improvements.

**S3. Bound detection performance claims precisely.**
- **Location:** Page 7, Section 4.3, Paragraph 1.
- **Action:** Replace "breaks through this performance limit" and "enables ViT models to achieve superior performance" with: "Under the 3x+MS schedule with Cascade Mask R-CNN, HST slightly exceeds full fine-tuning (+1.0 APb). Under the shorter 1x schedule, HST still trails full fine-tuning by 2.6 APb on Mask R-CNN, indicating that longer training is needed to close the gap."
- **Expected benefit:** Eliminates selective framing and presents balanced evidence.

### P1 — Should Fix

**S4. Add HSN architecture details for reproducibility.**
- **Location:** Page 3-4, Section 3.1.
- **Action:** (a) Specify Side block distribution: "For ViT-B/16 with 12 blocks, we assign 3 Side blocks per stage (stages 1-4)." (b) Describe convolutional stem: kernel size=7x7, stride=2, output channels matching stage 1 dimension, followed by BatchNorm+ReLU. (c) Confirm whether stem parameters are included in the 0.78M count.
- **Expected benefit:** Enables independent reproduction.

**S5. Isolate MetaT recycling benefit via ablation.**
- **Location:** Page 9, Section 4.7 (extend Table 5).
- **Action:** Add ablation variant: HSN + LN tuning + MetaT (re-use disabled = discard after each block). Compare to HST.a (LN tuning only) and full HST. Report VTAB-1k accuracy and COCO APb/APm.
- **Expected benefit:** Validates or refutes the claimed advantage of recycling prompt outputs.

**S6. Explain asymmetric FG Injection gains.**
- **Location:** Page 9, Ablation discussion.
- **Action:** Add analysis explaining why FG Injection yields +0.8% classification gain but +6.0 APb detection gain. Include a hypothesis: FG Injection preserves fine-grained spatial details essential for dense prediction but less critical for classification's pooled representation.
- **Expected benefit:** Provides mechanistic insight and strengthens the paper's scientific contribution.

### P2 — Nice to Have

**S7. Add related-work comparison table.**
- **Location:** Page 3, Section 2.
- **Action:** Create a table comparing VPT, Adapter, LoRA, SSF, Side-Tuning, LST, and HST across axes: inserted params location, number of feature scales, intermediate activation reuse, ViT-B/16 tunable param count, and best dense prediction performance.
- **Expected benefit:** Makes the novelty positioning explicit and reviewer-friendly.

**S8. Restructure the related work by comparison axes.**
- **Location:** Page 3, Section 2.
- **Action:** Replace flat listing with three subsections: (a) PETL for recognition, (b) Side-tuning approaches, (c) Decoders for dense prediction with plain ViT. Each subsection ends with a sentence explaining HST's difference.
- **Expected benefit:** Improves readability and positions HST's contribution more clearly.

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current introduction follows this structure:
- P1: ViT success → PETL motivation → categories (adapters, prompts)
- P2: PETL limitation for dense tasks → HST overview (MetaT, AFB, Side blocks, parallel inference claim)
- P3: Experiment scope → SOTA claims
- P4: Contribution bullets

**Problems identified:**
1. The first paragraph is a citation-heavy literature survey that delays the problem statement.
2. The inference efficiency claim (P2) is contradicted by evidence, weakening the narrative.
3. The dense prediction gap is stated but not quantified (no concrete numbers).
4. Parallel computation is presented as a present advantage rather than a future aspiration.

### Recommended Storyline: "Gap-First Framing"

This storyline prioritizes research clarity by stating the problem before surveying solutions.

**Abstract Outline (S1-S5):**
- S1 (Problem): "Parameter-efficient transfer learning (PETL) adapts large Vision Transformers to downstream tasks with minimal training, but existing PETL methods fail to generate the multi-scale feature representations required for dense prediction tasks such as object detection and segmentation."
- S2 (Gap): "While adapters and prompt tuning achieve strong results on image classification, they incur a substantial performance gap relative to full fine-tuning on detection and segmentation benchmarks—a gap of 5-10 AP/mIoU points depending on the task."
- S3 (Idea): "We propose Hierarchical Side-Tuning (HST), which separates trainable parameters from the frozen backbone into a lightweight hierarchical side network (HSN) that produces pyramid-style multi-scale features."
- S4 (Method): "HST uses three components: Meta-Tokens for learning task-specific prompts per block, an Adaptive Feature Bridge for aligning backbone activations, and Side blocks with cross-attention for feature fusion."
- S5 (Result): "On VTAB-1k, HST achieves 76.0% average accuracy with 0.78M parameters. On COCO detection with Cascade Mask R-CNN, it matches full fine-tuning (49.7 APb) while using 55% fewer total parameters."

**Introduction Outline (P1-P5):**

- P1 (Stakes): Open with the deployment challenge: "Deploying a single large ViT across many downstream tasks requires per-task storage proportional to model size, making full fine-tuning impractical at scale. Parameter-efficient transfer learning (PETL) addresses this by freezing the backbone and updating only a small set of task-specific parameters."
- P2 (Gap): "However, existing PETL methods — adapters, prompts, and LoRA variants — were designed primarily for image classification. When applied to dense prediction tasks, they produce single-scale features that are poorly suited for detection and segmentation, where multi-scale pyramid representations are critical. For instance, on COCO object detection, the best PETL method (LoRA) still trails full fine-tuning by 7 APb under Mask R-CNN 1x."
- P3 (Idea): "We propose Hierarchical Side-Tuning (HST), a PETL framework that generates multi-scale features through a dedicated Hierarchical Side Network (HSN). Unlike prior side-tuning approaches that use a single branch summing at the last layer, HSN produces a 4-stage feature pyramid."
- P4 (Components): Briefly introduce MetaT, AFB, and Side blocks. State: "The AFB reuses learned prompt features (MetaT) as cross-attention keys, and linear weight sharing reduces parameters without sacrificing expressiveness."
- P5 (Results preview): Summarize key numbers and state: "A limitation of the current implementation is higher inference latency due to serial execution; future work will target parallel execution at matched stages."

### Alignment Checks

| Check | Current Storyline | Recommended Storyline |
|-------|------------------|----------------------|
| Problem alignment | PETL categories listed before problem | Problem stated immediately |
| Variable alignment | Dense prediction mentioned late | Dense prediction = core focus from P2 |
| Contribution-evidence alignment | SOTA claims without variance | Results with bounded wording |

## Priority Revision Plan
```text
Priority | Task                        | Effort   | Impact   | Section
---------|-----------------------------|----------|----------|--------
P0       | Fix inference overclaim     | Low      | High     | P2 Intro
P0       | Add statistical variance    | Medium   | Critical | Tables 1-3
P0       | Bound detection claims      | Low      | High     | Sec 4.3
P1       | Add HSN arch details        | Low      | High     | Sec 3.1
P1       | MetaT recycling ablation    | Medium   | Medium   | Sec 4.7
P1       | Explain FG Injection gains  | Low      | Medium   | Sec 4.7
P2       | Related-work comparison table| Medium  | Medium   | Sec 2
P2       | Restructure related work    | Medium   | Low      | Sec 2
```

### Revision Order

**Stage 1 (immediate, 1-2 days):** Fix the inference efficiency overclaim (P0-S1), bound detection claims precisely (P0-S3), add HSN architecture details (P1-S4), and explain FG Injection gain asymmetry (P1-S6). These are text-only changes that require no new experiments.

**Stage 2 (before resubmission, 1-2 weeks):** Run multi-seed experiments for variance reporting (P0-S2) — at minimum 3 seeds for a representative subset of tasks. Add the MetaT recycling ablation (P1-S5) — a single additional row in Table 5 requires minimal compute. Add a related-work comparison table (P2-S7).

**Stage 3 (optional but recommended):** Restructure the related work section (P2-S8) for improved readability. Reorganize the conclusion to avoid unsupported speculation.

### Expected Impact After Fixes

If all P0 and P1 items are addressed, the paper's core contribution (a pyramid side network for dense prediction PETL) would be clearly presented, its claims would be evidence-grounded, and its reproducibility would be significantly improved. The remaining concerns would be minor and would not affect the validity of the core findings.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective | Setup (data/split/protocol/baselines) | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|-----------|--------------------------------------|---------|-------------|-----------------|-------------------|
| E1 | Image classification (VTAB-1k) | 19 tasks, 1000 samples each, ViT-B/16 IN-21K pretrained, baselines: full FT, linear, Adapter, Bias, VPT, LoRA, NOAH, AdaptFormer, SSF, TOAST, EXPRES | Top-1 accuracy | 76.0% avg (SOTA among PETL) | HST outperforms PETL methods | No variance; single run |
| E2 | FGVC (5 datasets) | CIFAR-100, CUB-200, Flowers, Dogs, Cars; IN-21K and MAE pretrained | Top-1 accuracy (dual pretrain reporting) | Best or near-best on all 5 datasets | HST works across pretraining methods | Large MAE gap on CIFAR-100 (9.2%) |
| E3 | Object detection (COCO) | Mask R-CNN (1x, 3x+MS), Cascade Mask R-CNN (3x+MS), ATSS (3x+MS); baselines: full FT, VPT, AdaptFormer, SSF, LoRA | APb, APm, AP50, AP75 | Best among PETL; matches/exceeds full FT on Cascade 3x | HST competitive with full FT | Underperforms full FT on Mask R-CNN 1x (-2.6 APb) |
| E4 | Instance segmentation (COCO) | Same as E3 (Mask R-CNN, Cascade Mask R-CNN) | APm, APm50, APm75 | Best among PETL; matches full FT on Cascade 3x | HST effective for instance seg | See E3 |
| E5 | Semantic segmentation (ADE20K) | Semantic FPN (80k), UperNet (160k) | mIoU, +MS | Best PETL: 46.5/47.3 UperNet | HST improves PETL dense prediction | 3-point gap to full FT (49.5) |
| E6 | Efficiency analysis | V100 GPUs, 100 trials avg; training memory/time, inference FPS | GPU hours, memory (GB), imgs/sec | HST: slower than all PETL methods, lower memory than full FT | — | Contradicts efficiency claim in abstract/intro |
| E7 | Ablation: MetaT count | VTAB-1k + COCO Mask R-CNN 1x; N=1,4,8,16,32 | Mean%, APb, APm | N=1 sufficient for classification; N>1 helps detection | MetaT design is efficient | No variance across seeds |
| E8 | Ablation: Components | Progressive addition (LN-Tuning, Weight-Sharing, GlobalT, FG Injection) | Mean%, APb, APm | +3.9% acc, +10.5 APb cumulative | All components necessary | FG Injection gain asymmetry unexplained |

### Research-Theme Gap Diagnosis

1. **New knowledge — what is truly novel?** The main novel claim is that a pyramid-structured side network can generate multi-scale features for dense prediction PETL. However, the paper does not establish how this differs structurally from prior side-tuning work (Side-Tuning uses a flat additive branch; LST uses ladder connections). The novelty claim would be stronger with explicit architectural comparison.

2. **Reproducibility — can it be reimplemented?** Partially. The HSN stage distribution (3 blocks per stage for ViT-B/16) is not explicitly stated. The convolutional stem is not described. The exact dimensions of AFB linear projections and Side block hidden dimensions are not reported.

3. **Practical value — does it change practice?** The strong VTAB-1k results with few parameters suggest practical value for low-data classification scenarios. However, the inference speed penalty (~40% slower at bs=1) limits deployment value for latency-sensitive applications.

### Proposed Research Experiments

**P0 Experiment — Multi-Seed Variance Reporting**
- **Target Claim:** HST outperforms existing PETL methods
- **Hypothesis:** HST's improvements are statistically significant across seeds
- **Minimal Design:** Run HST + top-3 baselines (LoRA, SSF, AdaptFormer) on 3 VTAB-1k tasks (1 per category: Caltech101, EuroSAT, Clevr/count) with 3 seeds each. Report mean ± std.
- **Controls/Baselines:** Same seed, same data order, same hyperparameters
- **Metrics:** Top-1 accuracy; paired t-test p-value
- **Success Criterion:** p < 0.05 for HST vs. each baseline on at least 2 of 3 tasks
- **Estimated Cost:** ~3 GPU-days (3 seeds × 3 tasks × ~8 hours each)
- **Expected Gain:** Provides first statistical evidence for the paper's core claim

**P1 Experiment — MetaT Recycling Ablation**
- **Target Claim:** Reusing MetaT outputs (routing to AFB) improves performance
- **Hypothesis:** MetaT → AFB pathway provides non-trivial gains beyond LN tuning alone
- **Minimal Design:** Add variant: HSN + LN tuning + MetaT with output discarded after each block (mimicking VPT). Compare to HST.a (LN tuning only, no MetaT) and full HST.
- **Controls/Baselines:** Same training budget, same HSN structure
- **Metrics:** VTAB-1k Mean%, COCO APb (Mask R-CNN 1x)
- **Success Criterion:** MetaT-output-discarded variant performs measurably worse than full HST
- **Estimated Cost:** ~1 GPU-day
- **Expected Gain:** Validates or refutes one of the paper's claimed design innovations

**P2 Experiment — Parallel Execution Speed Benchmark**
- **Target Claim:** HST's side network can be computed in parallel with backbone
- **Hypothesis:** Overlapping ViT and HSN computation at each stage reduces effective latency
- **Minimal Design:** Implement CUDA-level parallel execution of ViT block i and Side block i using streams or multi-threaded execution. Measure end-to-end latency vs. serial baseline.
- **Controls/Baselines:** Serial HST, full fine-tuning, LoRA
- **Metrics:** imgs/sec at bs=1, bs=32, bs=128
- **Success Criterion:** Parallel HST achieves >85% of full fine-tuning throughput
- **Estimated Cost:** ~1-2 weeks engineering effort (not pure compute)
- **Expected Gain:** Converts an architectural promise into verified efficiency data, supporting the main narrative

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.0 / 10**

This score reflects the following weighted assessment:
- **Research Value & Novelty (primary): 6/10** — The pyramidal side network design is a meaningful extension of the side-tuning family, but the core architectural components (cross-attention with small KV set, linear complexity claim, prompt tokens) are individually well-established. The main novelty lies in their combination for dense prediction PETL, which is a valid contribution but incremental in nature. The paper over-claims on efficiency and detection superiority, which tempers the research value.
- **Validity & Soundness: 5/10** — The major issues (missing variance, inference efficiency contradiction, selective performance framing) reduce confidence in core claims. The abundant experimental scope is a strength, but single-run reporting prevents rigorous validity assessment.
- **Reproducibility: 5/10** — HSN architectural details (stem specification, block distribution, channel dimensions) are partially missing. Multi-seed variance is absent, preventing reproducibility assessment.
- **Presentation & Clarity: 6/10** — The overall structure is clear, but the introduction delays the core problem, the related work is a flat list, and efficiency claims are inconsistent with the evidence.

**Post-Revision Target: [7.0, 7.5] / 10**

This target assumes all P0 and P1 items from the Priority Revision Plan are fully addressed: inference claim correction, multi-seed variance reporting with statistical tests, bounded detection claims, added HSN architectural details, MetaT recycling ablation, and FG Injection gain analysis. If these fixes are implemented, the paper's core contribution would be clearly and honestly presented, with sufficient evidence to support its claims. The score cannot exceed 7.5 because the novelty increment over Side-Tuning/LST remains modest even with perfect execution.