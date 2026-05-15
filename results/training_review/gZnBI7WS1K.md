Now I have a thorough understanding of the paper and all the reviewer claims. Let me write the consolidated review.

## Summary

This paper proposes LLaVA-PruMerge, a plug-and-play token reduction method for large multimodal models (LMMs). The key idea is to exploit the sparsity of CLS-to-patch attention scores in CLIP-ViT's penultimate layer to adaptively identify and retain only the most important visual tokens (via IQR-based outlier detection), then supplement these retained tokens by merging information from similar pruned tokens (via k-NN weighted averaging). A variant called PruMerge+ additionally performs spatial-uniform sampling to recover some coverage. Applied to LLaVA-1.5 with LoRA fine-tuning, PruMerge compresses visual tokens to ~5.5% (≈32 tokens) on average while PruMerge+ uses ~25% (≈144 tokens). The method also generalizes to Video-LLaVA without retraining.

## Strengths

- **Novel use of CLS-token attention sparsity for adaptive token selection in LMMs.** The observation that CLS-to-patch attention in CLIP-ViT is highly sparse (Figure 3a) is well-motivated, and using IQR-based outlier detection to adaptively determine the number of retained tokens per image is a clean design. This go beyond fixed-budget pruning methods by letting image complexity dictate the token count, which the paper validates by showing per-task token variation (16 tokens for SQA, 40 for TextVQA/MME).

- **Strong ablation structure isolating each component's contribution.** The ablations (Tables 3 and 4 in the paper) cleanly separate the effects of (a) adaptive IQR-based selection vs. sequential/spatial baselines, (b) the token supplement (TS) merging step on top of AITS, and (c) training-free vs. LoRA fine-tuning. The adaptive selection consistently outperforms uniform sampling at the same token budget, and the merging step recovers meaningful performance (e.g., MME 1221.6 → 1350.3, POPE 75.7 → 76.3).

- **Training-free generalization to video.** Applying PruMerge to Video-LLaVA during inference without any additional training yields competitive or improved results (e.g., ActivityNet-QA accuracy 45.3 → 48.3), demonstrating that the method captures genuine redundancy in video tokens.

- **Detailed efficiency analysis using roofline modeling.** Table 5 reports FLOPs, estimated prefill time, and memory savings from token reduction under both FP16 and INT4 settings, showing substantial reductions (e.g., 9.3 TB → 0.91 TB FLOPs for Vicuna-7B FP16). This provides useful quantification of the potential savings.

## Weaknesses

### Fatal
None.

### Major

- **The "comparable performance" claim is overstated for the high-compression PruMerge variant.** PruMerge (5.5% tokens) incurs substantial drops on several key benchmarks: VQAv2 78.5→72.0 (-8.3%), POPE 85.9→76.3 (-11.2%), MME 1510.7→1350.3 (-10.6%). On the larger Vicuna-13B backbone, the drops are similar or larger. While PruMerge+ (25% tokens) shows much milder degradation, the paper's abstract and introduction repeatedly emphasize the 14× compression figure (associated with PruMerge) while claiming "comparable performance" — this conflation is misleading. The paper would benefit from separating the claims per variant and being more precise about which benchmarks see which degradation levels.

- **No empirical comparison against established token-reduction methods.** The paper only compares to naïve sequential and spatial sampling baselines. Established ViT token-reduction techniques such as ToMe (Bolya et al., 2023), EViT (Liang et al., 2022), or DynamicViT (Rao et al., 2021) are cited in the related work and discussion sections, but never benchmarked under the same LMM evaluation protocol. Without this comparison, it is unclear whether PruMerge's performance is attributable to its specific design or simply to the general benefit of aggressive token pruning with subsequent fine-tuning. The paper argues in Section 3.5 that these methods target ViT acceleration rather than LMM token reduction, but an empirical head-to-head at matched token budgets would substantially strengthen the contribution.

- **Efficiency analysis is based entirely on roofline estimates, with no real-world latency or throughput measurements.** Table 5 uses LLM-Viewer (a roofline model) to report FLOPs and estimated prefill time. The overhead of the prune-merge algorithm itself — extracting penultimate-layer attention, computing IQR, performing k-NN search over 576 tokens, computing weighted merges — is never measured or accounted for. A 4–10× FLOP reduction in the LLM prefill stage could be partially or fully offset by this overhead in wall-clock time. Actual GPU latency, tokens/second, and peak memory measurements are needed to substantiate the efficiency claims.

### Minor

- **The value of k in the k-NN merging step is never specified.** Algorithm 1 (line 208) uses k without definition or default value. This is a missing implementation detail that affects reproducibility and the method's behavior.

- **The AITS-only ablation reveals a very weak importance signal.** LLaVA-1.5 with AITS alone (Table 3 ablation table) drops from 85.9 to 75.7 on POPE and from 1510.7 to 1221.6 on MME — severe degradations. The recovery from merging (TS) is meaningful but the fact that AITS alone performs so poorly raises questions about whether the CLS-attention signal is sufficiently informative for hard tasks like object hallucination detection.

- **The video performance improvement claim is overstated.** The paper states the method "enhances its performance" across multiple benchmarks, but results are mixed: MSVD-QA sees 70.7→71.1 (+0.4), MSRVT-QA sees 59.2→58.4/59.3 (flat to slightly negative), and only ActivityNet-QA shows a clear gain (45.3→48.3). This is better described as "competitive performance with modest gains on some tasks."

- **LoRA fine-tuning confound.** The main results (Table 1) apply LoRA fine-tuning with reduced tokens, while the baseline LLaVA-1.5 was fully fine-tuned with 576 tokens. This asymmetry means the method benefits from additional training that the baseline did not receive. Although the paper also reports training-free results (Table 3 ablation-training), the main comparison is not perfectly apples-to-apples.

### Trivial

- The paper mentions "6.9% of visual tokens" in the Conclusion (line 444) while the Abstract and Table 1 caption say "5.5%." These refer to different settings (uniform token count in ablation vs. adaptive average across tasks), but the inconsistency is confusing without clarification.

## Nice-to-Haves

- Ablation of the IQR multiplier (1.0×, 1.5×, 2.0×) to justify the default choice, given that adaptivity hinges on this threshold.
- Quantitative validation of the adaptivity claim (e.g., correlation between number of retained tokens and image complexity metrics such as object count or entropy).

## Removed Points

- **Criticism about the method not being compared to "existing token-reduction methods" as a missing related work issue**: This is kept (not removed), because the paper itself cites ToMe and related methods, and the concern is about missing *empirical baselines*, not missing citations. Valid weakness kept in Major.

- **Criticism that the paper claims PruMerge "even shows better performance" on POPE**: This claim appears in the paper (line 266: "in POPE and ScienceQA, our approach even shows better performance") but is not supported by the table — PruMerge POPE = 76.3 < 85.9 and PruMerge+ POPE = 84.0 < 85.9. However, this specific error was not raised by any reviewer, so it is not a point to include or remove; it is simply noted here.

- **Strength Finder's claim that PruMerge "matches or exceeds the baseline on... MMB (64.9 vs. 64.3)"**: This conflates PruMerge+ (64.9) with PruMerge (60.9). The MMB 64.9 belongs to PruMerge+, not PruMerge. The Strength Finder's claim is inaccurate, but since strengths are not being "removed" per se, this correction is noted.

## Novel Insights

None beyond the paper's own contributions. The reviewers' analyses surface the tension between achieving aggressive compression (14×, 5.5% tokens) and maintaining performance, and the need for realistic efficiency measurements, but these observations follow naturally from the paper's own data.

## Suggestions

1. **Separate claims by variant.** Make it explicit in the abstract and introduction that the 14× compression (PruMerge) comes with non-trivial accuracy trade-offs on several benchmarks, while the milder 4× variant (PruMerge+) is closer to lossless. The current framing conflates the two.

2. **Add real-world latency benchmarks.** Measure wall-clock prefill time, tokens/second, and peak GPU memory for both PruMerge variants, including the overhead of the reduction algorithm itself. Without this, the efficiency contribution rests on unvalidated estimates.

3. **Compare against ToMe adapted for LMMs.** Use ToMe (or EViT) to reduce visual tokens before the LLM and evaluate under the same protocol. This is the most direct way to demonstrate that the specific design choices (IQR selection + k-NN merging) matter.

4. **Specify k and ablate it.** State the value of k used in all experiments and show sensitivity to this hyperparameter.

5. **Quantify adaptivity.** Report the distribution of retained tokens per image across benchmarks and correlate it with a complexity metric (e.g., number of detected objects, text density) to substantiate the adaptivity claim beyond visual examples.

## Score and Decision

Score: 5.5 — The paper proposes a sensible and well-ablated token reduction method with a genuinely interesting design. However, the overclaimed "comparable performance" for the high-compression variant, the lack of real-world efficiency measurements, and the absence of comparisons to relevant token-reduction baselines prevent it from meeting the bar for a top-tier venue in its current form. The contributions are real but the evidence is incomplete in several important dimensions.

Decision: Reject

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>