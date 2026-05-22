Now I have all the information I need. Let me compose the final review.

---

## Summary

This paper introduces OptMerge, a data-free model merging method for Multimodal LLMs, along with the first MLLM-specific merging benchmark that categorizes capabilities into VQA, Geometry, Chart, OCR, and Grounding, and also explores modality merging (vision, audio, video). The method denoises task vectors via truncated SVD and stabilizes optimization using SGD with mean initialization, showing consistent improvements across full fine-tuning (InternVL2.5), LoRA (Qwen2-VL), and real Hugging Face checkpoints, while requiring orders-of-magnitude less compute than mixture training.

## Strengths

1. **Comprehensive MLLM merging benchmark with capability categorization.** The paper provides the first model merging benchmark specifically for MLLMs, with five well-defined capability groups (VQA, Geometry, Chart, OCR, Grounding), ≥100k training samples per group, both full fine-tuning (InternVL2.5) and LoRA (Qwen2-VL) settings, and an extension to modality merging (vision, audio, video). This fills a clear gap — prior work (AdaMMS, UQ-Merge) either merged only two MLLMs or treated each dataset as a separate task without capability-level organization. Code and checkpoints are publicly released.

2. **OptMerge method with principled components.** The method addresses two distinct problems: (a) full fine-tuning task vectors contain noise that is reduced via centered SVD truncation (Eq. 2–3); (b) LoRA task vectors suffer from norm explosion during optimization, which is controlled by switching from Adam to SGD (providing implicit regularization) and initializing with the mean of task vectors. The ablation (Table 4) confirms each component contributes positively, with the full method showing a 4.65% gain over WUDI on Qwen2-VL and 2.35% on Vicuna-7B.

3. **Thorough empirical evaluation across diverse settings.** The paper compares 10 merging methods across two model families, two fine-tuning paradigms, five capability benchmarks, three modalities, real Hugging Face checkpoints, and scaling up to Qwen2.5-VL-32B. The merged model also shows emergent capabilities on general QA benchmarks (Table 10), outperforming every individual specialist by an average of 10.85%.

4. **Large computational efficiency.** On InternVL2.5-1B, OptMerge requires 0.22h and 2.62GB of GPU memory versus 25.38h and 240GB for mixture training (Table 7). While mixture training is the stronger baseline, this cost differential makes merging a practical alternative for rapid model development.

5. **Theoretical bound connecting fine-tuning extent to mergeability.** Theorem 3.1 provides an upper bound showing how the merged model's task loss depends on learning rate η and iterations T, offering formal grounding for the empirical observation that less intensive fine-tuning yields better merging.

## Weaknesses

### Fatal
None.

### Major

1. **Arithmetic error in Table 3 (WUDI Merging average).** The WUDI Merging row in Table 3 reports an average of 63.65, but the ten visible values (37.19, 56.45, 42.96, 27.63, 67.34, 82.54, 65.56, 79.72, 68.34, 71.99) sum to 599.72, which averages to 59.97 — a ~3.7 point discrepancy. Other rows in the same table (Weight Averaging, TIES, OptMerge, Instruct) correctly compute their averages. This error must be corrected. Notably, the mistake makes OptMerge's advantage over WUDI look smaller than it actually is (63.30 vs. 63.65 reported = −0.35; 63.30 vs. 59.97 actual = +3.33), so it is not a case of result inflation, but it damages the paper's trustworthiness.

### Minor

2. **Misleading bolding in Table 5.** For both MUSIC-AVQA and AVQA datasets, TSV Merging achieves higher scores (53.78 and 80.90) than OptMerge (53.17 and 80.82), yet OptMerge values are also bolded. The caption states bolding indicates the best score. This visual presentation overstates OptMerge's standing. The numbers still show OptMerge is competitive — this should be presented transparently.

3. **Overstated "surpasses mixture training" claim.** The paper claims merging "potentially surpasses mixture training" and "surpasses multi-task learning" (Sections 1, 6). The evidence is mixed: on InternVL2.5, OptMerge (57.44) is below mixture training (57.66). For Qwen2-VL, the comparison is to Qwen2-VL-Instruct, which was trained with a different data mixture and protocol — not a controlled ablation. The paper acknowledges this ("For Qwen2-VL-Base, we directly use Qwen2-VL-Instruct as the upper bound for mixture training") but the framing in the title, abstract, and conclusion gives a stronger impression than the data supports. The results are better described as "competitive with" or "closely matching" mixture training.

4. **Baseline inconsistency between Table 3 and Table 4.** WUDI Merging for Qwen2-VL is reported as 63.65 (Table 3) but 58.65 (Table 4, ablation). If the ablation uses a different setup or subset, this should be stated explicitly. The actual calculated average from Table 3 (~59.97) is closer to 58.65, suggesting the Table 3 average is a typo, but the discrepancy between tables needs clarification.

5. **"2.48% average improvement" not clearly traceable to reported numbers.** The abstract and contribution list claim "an average performance gain of 2.48%" but this figure does not straightforwardly derive from the reported tables. From Table 4, the two reported improvements are 4.65% (Qwen2-VL) and 2.35% (Vicuna-7B), averaging to 3.5%. Across Tables 2, 3, and 6, the improvements over WUDI are 0.44%, ~3.33%, and 1.9%, averaging 1.89%. The paper should clarify which aggregation produces 2.48%.

### Trivial

- Some figure captions in the extracted text appear duplicated (Figure 1, Figure 2, Figure 4).
- "A12D" in Table 10 appears to be a minor typo for "AI2D."
- The percentage signs in Table 4 ("+4.43%", "+4.65%") appear to be absolute percentage-point differences from the WUDI baseline, not relative percentages. Clarifying this would prevent confusion.

## Nice-to-Haves

- A controlled comparison for Qwen2-VL where mixture training is done on the exact same data as the individual models (rather than using the Instruct variant) would cleanly settle whether merging can surpass multi-task training under identical data conditions.
- Variance estimates or even single-seed replication results would help assess whether the margins (e.g., 57.44 vs. 57.66) are meaningful.
- An analysis verifying that the discarded singular components from the SVD step are indeed noise (e.g., showing they have higher variance across tasks or correlate negatively with task performance) would strengthen the method's motivation.

## Removed Points

These points from the inputs were removed with justification:

- **Modality merging underspecified (Harsh Critic Claim 4):** The paper explicitly says "See App. C for details" — the appendix was stripped by the parser. Not a paper flaw.
- **Theorem 3.1 not truly "first":** Requires external literature verification beyond this review's scope. The paper asserts this claim; whether it is strictly "first" is a judgment call, not a factual error that can be verified from the paper alone.
- **GPU memory implausibility for InternVL2.5-1B (240GB):** For multi-task mixture training with data loading, optimizer states, gradient accumulation across 8×V100 GPUs, 240GB is not implausible. Not a verified issue.
- **Missing ablation of rank k on Qwen2-VL:** The requirement is reasonable but not a core flaw; the existing ablation on InternVL2.5 (Table 8) covers the full fine-tuning case, and for LoRA models (which are already low-rank) this is less informative.
- **Missing statistical significance/reproducibility details:** These are generic reviewer concerns applying to most papers in this area. Single-run evaluation without error bars is standard practice in model merging benchmarks.
- **Strength about "surpassing mixture training":** Dropped because it conflicts with a verified weakness (the claim is overstated). The strength is better phrased as "competitive with mixture training at a fraction of the cost."
- Several generic strengths from the Strength Finder about "addressing an important problem" — these lack specific evidence anchors.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Correct the WUDI average in Table 3 and add a footnote explaining the fix.
2. Clarify the "2.48%" figure by specifying which settings it averages over.
3. Fix the bolding convention in Table 5 so OptMerge is only bolded where it actually achieves the best score, or use a clearer formatting scheme (e.g., bold for best, underline for second-best).
4. Soften the "surpasses mixture training" language to "closely matches or, in some settings, surpasses" to accurately reflect the evidence.
5. Add a brief note explaining the baseline discrepancy between Tables 3 and 4.

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `UQ-Merge` (SO0manOwUF.md) | 5.50 | Directly comparable MLLM merging paper. Current paper has a more comprehensive benchmark, more baselines, and also proposes a new method — stronger overall. |
| `What Matters for Model Merging at Scale` (fvUVe2gJh0.md) | 5.33 | Pure empirical study without a new method. Current paper has more novelty (benchmark + method). |
| `Realistic Evaluation of Model Merging` (Bq3fEAGXUL.md) | 5.33 | Benchmark/study paper. Current paper has comparable evaluation breadth plus a novel method. |
| `Uncertainty-Based Gradient Matching` (D7KJmfEDQP.md) | 6.00 | Similar hybrid profile (theory + method + experiments). Both papers accepted. Current paper has a more extensive benchmark but some presentation issues the other paper lacks. |
| `ATM: Improving Model Merging` (lNtio1tdbL.md) | 3.00 | Has fundamental framing issues (not truly data-free model merging). Not comparable. Current paper is substantially stronger. |

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>