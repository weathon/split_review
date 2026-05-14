Now I have sufficient understanding of the paper and its calibration anchors. Let me write the final consolidated review.

---

## Summary

This paper introduces (i) the first model merging benchmark for Multimodal LLMs that categorizes tasks into five distinct capabilities (VQA, Geometry, Chart, OCR, Grounding) and explores merging across vision, audio, and video modalities; and (ii) OptMerge, a data-free merging method that denoises task vectors via low-rank SVD approximation and stabilizes merged-vector optimization through SGD, mean initialization, and norm control. Extensive experiments on InternVL2.5, Qwen2-VL, and Vicuna-7B show OptMerge achieves consistent, though modest, gains over prior merging methods while requiring significantly less compute than mixture training.

## Strengths

- **Well-constructed benchmark with public release.** The benchmark provides fine-grained capability categorization across two fine-tuning paradigms (full FT on InternVL2.5-1B-Instruct, LoRA on Qwen2-VL-7B-Base) with ≥100k training samples per task (Table 1). All checkpoints and code are publicly released, filling a genuine gap in the MLLM merging literature.
- **Consistent gains from OptMerge across diverse settings.** OptMerge achieves the highest or near-highest average on full FT (57.44 vs. 57.00 for next-best, Table 2), LoRA FT (63.30 vs. 61.88, Table 3), modality merging (67.00, Table 5), and HuggingFace checkpoints (66.70, Table 6). The gains are modest but consistent.
- **Honest and informative ablation.** Table 4 shows that replacing Adam with SGD alone *hurts* performance (58.65 → 48.88 for Qwen2-VL), and improvements only emerge when combined with mean initialization and low-rank approximation. This transparency strengthens rather than weakens the contribution.
- **Practical efficiency demonstrated.** Table 7 shows merging Qwen2-VL-7B takes 3.78h and 21.97 GB GPU memory vs. 24.56h and 256 GB for mixture training — a ~6.5× reduction in time and ~11.6× in memory, making the approach genuinely practical for resource-constrained settings.
- **Empirical motivation via CLIP-ViT analysis (App. B.1).** The finding that merging performance rises then declines with fine-tuning steps (Figs. 5–6) provides empirical grounding for the benchmark's training protocol (1 epoch, reduced LR), independent of the theoretical analysis.

## Weaknesses

### Fatal

None.

### Major

- **Hyperparameter tuning protocol is ambiguous and potentially problematic (Section 5.1).** The paper states that λ is determined "by searching within the range [0.1, 0.3, 0.5, 0.7, 1.0, 1.5]" for all methods, but never specifies whether this search uses a held-out validation set or the test benchmarks themselves. No validation split or cross-validation protocol is described. This is a real methodological concern: if λ is tuned directly on test data, absolute performance numbers are inflated, and methods with more flexibility could benefit disproportionately. That said, (a) all methods share the identical grid search protocol, so *relative* comparisons retain some validity, (b) the grid is coarse (only 6 discrete values), limiting overfitting, and (c) this practice is unfortunately common in the model merging literature (Task Arithmetic itself tunes λ on evaluation data). Nevertheless, this weakens claims about absolute performance and "surpassing mixture training," and the paper should clarify the protocol.

### Minor

- **Modality merging evaluation is narrow (Section 5.2, Table 5).** Claims about "effectively integrating information from three modalities" and "complementary nature" rest on only two audio-visual QA datasets (MUSIC-AVQA, AVQA). No vision-language-only, audio-language-only, or cross-modal transfer tasks are evaluated, which would be needed to substantiate claims about true multi-modal integration. The modality merging contribution is secondary, so this does not undermine the paper's core claims, but it limits the strength of conclusions drawn in that section.

- **Modality merging baseline comparison is acknowledged but under-discussed.** The paper compares static merging methods against online composing methods (NaiveMC, DAMC) that require 3× parameter storage and additional inference overhead. The paper notes the storage difference (line 774) but the claim that static merging "outperforms these online composition methods" (line 777) should be qualified by the resource asymmetry. This is a presentation weakness rather than a methodological flaw — the comparison itself is informative.

- **Theorem 3.1 assumptions are unverified for the actual MLLM setting.** The theoretical bound relies on the PL condition, bounded gradients, and near-orthogonal task vectors — none of which are empirically verified for the fine-tuned InternVL2.5 or Qwen2-VL models. The theorem serves as motivation rather than a rigorous guarantee, and the paper is transparent about this (the benchmark construction is also justified by CLIP-ViT experiments in App. B.1). The theorem reads as a theoretical add-on rather than a necessary pillar of the contribution.

- **HuggingFace checkpoint-to-benchmark alignment is imperfect (Table 6).** A Pokémon fine-tuned model and a PDF-to-text model are evaluated on ChartQA and Grounding benchmarks, which do not align with their intended expertise. The merged model's improvement over individual models may partly reflect the base model's strength rather than successful knowledge integration. This weakens the "practical model merging in communities" argument but does not invalidate the result.

- **Mixture training comparison is favorable but not universally superior.** For InternVL2.5, mixture training achieves 57.66 vs. OptMerge's 57.44 (Table 2) — a marginal edge for mixture training. The paper's phrasing "closely match or even surpass" (line 696) is fair, but the stronger claim in the abstract that merging "can outperform mixture training" should be tempered for InternVL2.5.

### Trivial

- The claim that OptMerge "requires no hyperparameter search" (line 191) is slightly inconsistent with the fact that OptMerge still participates in the same λ grid search as all other methods. The intended meaning (no search for internal method-specific hyperparameters, unlike AdaMMS) is clear from context, but the phrasing could be more precise.
- The rank ratio for SVD truncation (rank divided by number of tasks = 5) is described as "simply defined" without theoretical justification; however, Table 8 shows robustness across a wide range (10%–30%), largely mitigating this concern.

## Nice-to-Haves

- A validation-split protocol for λ tuning would strengthen all experimental claims and bring the evaluation in line with standard ML practice.
- Broader modality merging evaluation (e.g., vision-only QA, audio-only QA to isolate per-modality contributions) would strengthen the modality claims.
- An empirical study correlating the low-rank SVD proxy (Eq. 3) with actual data representations would strengthen the methodological motivation for the SVD truncation.

## Removed Points

These points from the input reviews are flagged as removed; treat them with caution:

1. **"Test-set leakage is a structural flaw that invalidates all results" (Harsh Critic #1).** Removed as stated. While the λ tuning protocol is ambiguous, calling it a "structural flaw that invalidates all results" is an overstatement. All methods share the same tuning protocol, so relative comparisons remain informative. The coarse grid (6 values) limits overfitting. This concern is downgraded to a **Major** weakness focusing on ambiguity and absolute performance claims rather than claiming all results are invalid.

2. **"SGD claim is post-hoc" (Harsh Critic, Methodology section).** Removed as a standalone criticism. The ablation table (Table 4) honestly reports that SGD alone hurts performance (-9.77%), and the paper does not hide this. The claim that SGD provides implicit regularization is stated in the context of the full method pipeline, which is reasonable.

3. **"Benchmark construction decisions are already justified by CLIP-ViT experiments" (Harsh Critic, Theorem 3.1).** Partially removed — folded into the minor weakness that Theorem 3.1 assumptions are unverified. The harsh critic's claim that the theorem is "a theoretical add-on" is incorporated into the minor weakness rather than presented as a fatal flaw.

4. **Strength: "This paper addressed an important problem" (Strength Finder).** Removed — generic, applies to nearly every paper.

5. **Strength: "The problem is timely and interesting" variants.** Removed — superficial without specific evidence.

6. **Formatting/style nitpicks from all reviewers.** Removed per instructions — parser artifacts, not author issues.

7. **"Missing related works" from any reviewer.** Removed per instructions — cannot verify external sources.

## Novel Insights

None beyond the paper's own contributions. The reviewers' observations largely confirm or refine points already present in the paper: the benchmark fills a genuine gap, OptMerge's components synergize in a non-trivial way (SGD alone hurts), and the data-free efficiency is practically meaningful.

## Suggestions

- **Clarify the λ tuning protocol.** Explicitly state whether λ is selected on a held-out validation split or on the test benchmarks. If using test data, consider a simple validation protocol (e.g., leave-one-task-out or a small held-out portion of training data) for final camera-ready results. Even a statement that "all methods share identical λ search, making relative comparisons fair" would improve transparency.
- **Expand modality merging evaluation.** Add at least vision-only and audio-only QA baselines to isolate per-modality contributions in the merged model. This would substantially strengthen the modality claims without requiring new training.
- **Tone down the "surpasses mixture training" claim** for InternVL2.5 where mixture training edges out OptMerge by 0.22 points. "Matches or approaches" is more precise.

## Score and Decision

### Anchor comparison:

| Path | Avg Score | Decision | Comparison |
|------|-----------|----------|------------|
| `/home/wg25r/review_agent/human_reviews_2026/NYUxN6plEh.md` | 4.50 | Reject | Meta-learning for merging coefficients; marginal gains, missing key baselines. Our paper is clearly stronger — it provides both a benchmark and a method with better ablation across more settings. |
| `/home/wg25r/review_agent/human_reviews_2026/nsmow1yhEE.md` | 3.50 | Reject | Primarily descriptive analysis of modality extension; weak novelty, unsupported claims. Our paper is substantially stronger with concrete benchmark + method contributions. |
| `/home/wg25r/review_agent/human_reviews_2026/7x6TxVIarj.md` | 5.00 | Accept (Poster) | MME-Unify benchmark; well-motivated but mainly a "benchmark of benchmarks" with evaluation metric concerns. Our paper is comparable — adds a novel method on top of the benchmark, but shares similar evaluation concerns (λ tuning for us, CLIP-score evaluation for them). |
| `/home/wg25r/review_agent/human_reviews_2026/awyJs71tE7.md` | 5.00 | Accept (Poster) | FlexMerge; novel framework but major limitation (requires task ID at inference). Our paper is comparable — different weaknesses (λ tuning vs. task-ID requirement), similar overall contribution level. |
| `/home/wg25r/review_agent/human_reviews_2026/PtPYZYfa0h.md` | 6.00 | Accept (Poster) | MCIF benchmark; human-annotated, carefully constructed, comprehensive. Our paper is somewhat weaker — the λ tuning ambiguity and narrow modality evaluation prevent it from reaching this tier. |
| `/home/wg25r/review_agent/human_reviews_2026/Zg1YH8R5GG.md` | 4.50 | Accept (Poster) | JointAVBench; audio-visual reasoning benchmark. Our paper is comparable or slightly stronger due to broader scope (benchmark + method). |
| `/home/wg25r/review_agent/human_reviews_2026/ItRYEe8E61.md` | 4.50 | Accept (Poster) | OmniVideoBench. Our paper is comparable or slightly stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/jXgDfBpwHH.md` | 4.00 | Reject | Fork-Merge Decoding for AV-LLMs. Our paper is clearly stronger with more comprehensive contributions. |
| `/home/wg25r/review_agent/human_reviews_2026/B9iMn59jFE.md` | 4.00 | Withdrawn/Reject | OmniEval benchmark. Our paper is stronger with both benchmark and method. |

The paper sits squarely in the 5.0 range: it has genuine contributions (the first MLLM merging benchmark with capability categorization, a simple-but-effective merging method with honest ablation), but the λ tuning ambiguity and narrow modality evaluation prevent it from reaching the 6.0 tier. Relative to the 5.0 anchors (MME-Unify, FlexMerge), this paper has comparable strengths and different but comparable weaknesses. It is clearly above the 3.5–4.5 reject-tier papers.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>