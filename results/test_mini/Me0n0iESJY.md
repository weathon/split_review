Now I have all the information I need. Let me write the final consolidated review.

## Summary

The paper introduces OptMerge, a data-free model merging method for Multimodal LLMs that applies low-rank denoising of task vectors via truncated SVD and robust optimization (SGD with mean initialization). It also presents the first comprehensive benchmark for MLLM model merging, covering five capability tasks (VQA, Geometry, Chart, OCR, Grounding) across both full fine-tuning and LoRA settings, plus modality merging (vision, audio, video). The benchmark releases task-specialized checkpoints and evaluation suites, enabling systematic comparison of 10 merging algorithms. OptMerge shows modest average improvements over prior methods (e.g., +0.44% on InternVL2.5 full fine-tuning, +1.9% on Hugging Face checkpoints) and demonstrates that static merging can approach or exceed mixture training while requiring orders of magnitude less compute.

## Strengths

- **Useful, well-constructed benchmark for MLLM model merging.** The paper curates five task categories with ≥100k samples each, trains and releases expert checkpoints for InternVL2.5-1B, Qwen2-VL-7B, and Vicuna-7B across both full and LoRA fine-tuning, and evaluates using standard libraries (VLMEvalKit, LMMs-Eval). This is the first benchmark that systematically categorizes MLLM capabilities for model merging research, filling a clear gap relative to prior work (AdaMMS, UQ-Merge) which had narrower scope. The public release of checkpoints and code is a genuine community contribution.

- **Modality merging experiments are novel and well-executed.** The exploration of merging vision-language, audio-language, and video-language encoders into a unified omni-modal model is a direction not addressed by prior MLLM merging work. Results in Table 5 show that static merging methods can outperform online composing methods (NaiveMC, DAMC) that require 3× parameter storage, demonstrating the promise of data-free omni-model construction.

- **Extensive empirical coverage.** The paper evaluates 10 merging algorithms across diverse settings (full fine-tuning, LoRA, modality merging, real Hugging Face checkpoints, 32B scale), provides ablation studies, rank sensitivity analysis, and computational cost comparisons (Table 7: 0.22h for 1B vs. 25h for mixture training). This thoroughness strengthens the empirical claims.

- **Computational efficiency is convincingly demonstrated.** OptMerge requires only 0.22h (2.62 GB GPU memory) for InternVL2.5-1B and 3.78h (21.97 GB) for 7B models, versus 25+ hours and 240+ GB for mixture training. This makes the method practically deployable.

## Weaknesses

### Fatal
None.

### Major

- **Unexplained performance discrepancy for WUDI between Table 3 and Table 4.** In Table 3 (Qwen2-VL LoRA setting), WUDI Merging achieves an average of 63.65 (or 59.97 depending on column alignment), while in Table 4 (the ablation study for the exact same model setting) the WUDI baseline is reported as 58.65. This ~5% gap is never acknowledged or explained. If Table 4's "WUDI Merging" uses different hyperparameters (λ, optimization iterations, etc.) than Table 3, then the ablation's incremental gains (+4.43%, +4.65%) cannot be directly attributed to the proposed components — they may partly reflect catching up to a stronger WUDI configuration. The paper must clarify why the same method produces different baseline numbers across tables and demonstrate that the claimed improvements hold against the properly configured WUDI baseline.

- **The central claim that model merging "can outperform mixture training" is not convincingly supported for the LoRA setting.** For InternVL2.5 (full fine-tuning), the paper provides a proper mixture training baseline (57.66 vs. OptMerge 57.44 — mixture training wins). For Qwen2-VL (LoRA), the paper substitutes Qwen2-VL-Instruct as an "upper bound," which was trained with vastly more data and computational resources. While OptMerge (63.30) beats Instruct (62.23), this comparison conflates two variables (data scale vs. the merging vs. training question). A controlled experiment training Qwen2-VL-Base on the union of the five task datasets would be required to support the claim that merging beats mixture training in the LoRA regime. The current evidence is suggestive but not conclusive.

### Minor

- **Theorem 3.1 is peripheral.** The theorem provides an upper bound on merging loss decomposing into convergence, cross-task interference, and curvature terms. However, it does not drive any component of OptMerge's design — the method uses low-rank SVD denoising and optimizer choices, none of which follow from the bound. The remark's claim of providing "the first theoretical explanation" is overstated; the core insight (moderate fine-tuning helps merging) was already empirically documented in prior work (Yu et al., 2024; Li et al., 2025b) and the theorem adds no actionable guidance. It could be removed or significantly trimmed without affecting the paper's contribution.

- **Design choices for full vs. LoRA fine-tuning lack empirical justification.** The paper treats centered SVD for full fine-tuning and non-centered SVD for LoRA, along with Adam vs. SGD, without isolating why these asymmetric choices are necessary. The ablation (Table 4) shows that "SGD alone" hurts (−9.77%), and the gain comes from the combination of SGD + initialization + low-rank approximation, making it impossible to attribute improvement to any single design decision. An ablation testing centered SVD on LoRA would help justify the separate treatment.

- **Improvements over WUDI are modest and inconsistent across settings.** On InternVL2.5 full fine-tuning, OptMerge gains only +0.44% over WUDI (57.44 vs. 57.00). On real Hugging Face checkpoints (Table 6), the gain is +1.9% (66.70 vs. 64.80). On Qwen2-VL LoRA, the comparison is complicated by the numerical discrepancy noted above. No statistical significance or variance estimates are reported for any comparison. Given margins this small, single-run results are insufficient to establish reliable superiority.

### Trivial

- The paper claims "the first model merging benchmark" for MLLMs (Introduction, Section 1), which conflicts with the discussion of prior overlapping work (AdaMMS, UQ-Merge). The scope is narrower than the blanket claim suggests (these prior works do have merging-related evaluations, just without the same task categorization). This should be qualified.

## Nice-to-Haves

- Reporting results with multiple seeds or confidence intervals for the main comparisons would substantially strengthen the empirical claims given the small margins involved.
- A controlled mixture training baseline for Qwen2-VL-Base (same data as the five experts) would cleanly resolve the "merging vs. mixture training" question for the LoRA setting.
- Qualitative examples showing the merged model's outputs vs. individual experts on representative cases would help illustrate whether the merged model genuinely combines capabilities or hedges across tasks.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Table 3 bolding/misrepresentation issue**: The parsed text shows HTML bold tags that may be parser artifacts. Bold formatting in PDF tables can be misaligned during text extraction. The original paper likely has correct formatting. Removed per hard rules (parser formatting artifacts).
- **Modality merging comparison is "potentially misleading"**: The paper explicitly states that online composing requires "3× static merging" storage. The criticism ignored this transparent disclosure. Removed as factually incorrect.
- **Missing general-task "hedging" analysis**: The reviewer speculates that gains on general QA tasks may come from ensembling effects rather than genuine capability combination. This is speculative and not a concrete flaw. Removed.
- **Request for 72B scaling experiments**: Outside the stated scope of the paper. Removed.
- **Request for appendix content**: The parser strips appendix sections. The original submission contains them. Removed per hard rules.

## Novel Insights

Beyond the paper's own contributions, the most interesting observation from the review synthesis is the tension between the paper's two core claims: that merging "can outperform mixture training" (supported partially for InternVL2.5 and for the Instruct comparison) and the modest marginal improvements over WUDI. The paper's strongest contribution is arguably the benchmark infrastructure itself, not the method — OptMerge is an incremental improvement over WUDI, and the paper would be better served by presenting the benchmark as the primary contribution and the method as a secondary one, rather than the reverse. The modality merging results are the most surprising finding and deserve more emphasis.

## Suggestions

1. **Fix the Table 3 / Table 4 WUDI discrepancy.** Clarify what configuration of WUDI is used in each table. If different hyperparameters (λ, iterations) were used, report the ablation starting from the same WUDI configuration as Table 3.
2. **Add a proper LoRA mixture training baseline.** Train Qwen2-VL-Base on the union of the five task datasets to provide a clean comparison for the "merging vs. mixture training" claim.
3. **Tone down the theoretical contribution.** Either connect Theorem 3.1 to the method design explicitly, or move it to a background section without claiming it as a contribution.
4. **Add statistical significance or variance estimates** for the main comparisons, given the sub-1% margins.
5. **Add an ablation on the LoRA setting with centered SVD** to empirically justify the asymmetric design choice.

## Score and Decision

Let me now calibrate against the retrieved anchors.

**Anchors compared:**

1. **DisTaC (avg 5.50, Accept Poster)** — Well-motivated robustness analysis in model merging, thorough experiments, clean evaluation. Our paper has a weaker method contribution and some evaluation inconsistencies, placing it below this bar.

2. **Model Merging Scaling Laws (avg 5.50, Reject)** — Strong empirical contribution (10K+ experiments) but theoretical gaps and limited applicability. Our paper has similar empirical breadth but is less rigorous in evaluation.

3. **Learn to Merge (avg 4.50, Reject)** — Meta-learning for merging, marginal improvements, missing baselines. Comparable to our paper in terms of incremental contribution over baselines.

4. **StatsMerging (avg 4.00, Reject)** — Had experimental inconsistencies (data amounts, conflicting table results) and limited novelty. Most similar to our paper in both strengths (SVD-based approach, extensive experiments) and weaknesses (incremental method, evaluation discrepancies).

5. **PSO-Merging (avg 2.50, Reject)** — Very weak novelty, flawed evaluation, marginal improvements. Our paper is clearly stronger than this.

6. **Extending Modality (avg 3.50, Reject)** — Interesting research question but descriptive analysis, limited novelty, conclusions not fully supported. Our paper has more concrete contributions (benchmark + method) putting it slightly above.

Our paper sits between the 4.00 and 4.50 anchors — better contributions than StatsMerging (which had weaker novelty and no benchmark) but below Learn to Merge in terms of methodological clarity. The benchmark contribution is genuine, but the method is incremental and the evaluation has unresolved discrepancies that prevent acceptance in current form.

**Score: 4.0**
**Decision: Reject**

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>