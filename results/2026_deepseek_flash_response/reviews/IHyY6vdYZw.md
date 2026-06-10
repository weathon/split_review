## Summary

This paper introduces VisualPRM400K (~400K multimodal process supervision data), VisualPRM (an 8B multimodal Process Reward Model), and VisualProcessBench (a human-annotated benchmark with 26,950 step-level labels across 5 reasoning benchmarks). The data is generated via a Monte Carlo-based automatic pipeline, and the PRM is used for Best-of-N (BoN) test-time scaling of MLLMs. Experiments show consistent BoN gains across diverse policy models (MiniCPM, QwenVL, InternVL families at 7B–78B) and demonstrate that PRM outperforms ORM and Self-Consistency under controlled comparisons, with the gap widening as N increases.

## Strengths

1. **Consistent BoN gains across diverse model families and scales**: Table 2 shows VisualPRM improves every policy model tested (6 models across 3 families), with overall gains of 3.7–8.9 points across 7 multimodal reasoning benchmarks. The improvements are not concentrated in a single favorable configuration — they hold across MiniCPM, QwenVL, and InternVL at parameter counts from 7B to 78B.

2. **PRM advantage over ORM and SC grows with N under controlled comparison**: Figure 4 and Section 4.3 provide the paper's strongest evidence. For InternVL2.5-8B, PRM beats SC and ORM by 2.4 and 1.5 points at N=8, widening to 3.1 and 4.3 points at N=128. ORM performance *regresses* from N=64 to N=128 while PRM continues improving — a clean signal that step-level supervision adds value beyond outcome-level rewards.

3. **VisualProcessBench fills a genuine gap in multimodal evaluation**: Unlike prior benchmarks (ProcessBench, PRM800K) that only require finding the first erroneous step, VisualProcessBench requires detecting all erroneous steps, directly addressing false negatives from models with reflection abilities. The benchmark comprises 2,866 samples and 26,950 human-annotated steps, constructed at documented cost (13 experts, 3 days, ~$37/person-day). The striking finding that most open-source MLLMs score near random (50% F1) underscores the need for specialized PRMs.

4. **Efficient single-forward-pass inference**: VisualPRM scores all steps in one forward pass via generation probability of a "+" token, unlike MLLM-as-judge approaches that autoregressively evaluate each step. This is a concrete architectural advantage for practical use as a BoN critic.

5. **Generalization to text-only reasoning**: Table 5 shows VisualPRM improves text-only performance on GSM8K, MATH-500, and GPQA for both Qwen2.5 (7B–72B) and InternVL2.5 (8B–78B) series, suggesting the process supervision signal transfers across modalities and is not overfitted to multimodal patterns.

## Weaknesses

### Major

- **Headline results conflate sampling gain with PRM selection ability**: Table 2 compares "+VisualPRM" (BoN=8, temperature=0.7) against "Base" scores, where "Part of the results are collected from the OpenCompass leaderboard" (line 210). The Base scores may come from greedy decoding or different configurations than the BoN runs, meaning the reported gains include both the benefit of sampling 8 candidates and PRM-guided selection. The paper *does* include a controlled comparison (Figure 4) that separates these factors, but the abstract, introduction, and conclusion build their primary claims on the uncontrolled Table 2 numbers. For instance, the abstract states "improves the reasoning performance... by 8.0, 3.7, 8.4, and 5.9 points" without caveat. This framing needs correction: either add a "BoN with random selection" column to Table 2, or cite the controlled ablation numbers in headline claims.

### Minor

- **Text-only evaluation methodology not explained**: Table 5 applies VisualPRM to text-only LLMs (Qwen2.5, InternVL2.5) on GSM8K, MATH-500, and GPQA. The paper does not specify how the image modality is handled for these text-only inputs (e.g., blank image, dummy placeholder, or bypassing the visual encoder). Since VisualPRM is a multimodal model requiring image input, this gap affects reproducibility.

- **Low Monte Carlo samples for data labeling**: The automatic pipeline uses only 16 MC continuations per step (line 144), compared to 64 in MathShepherd. With 16 samples, expected accuracy estimates are coarsely quantized at 1/16 granularity, which is especially problematic for distinguishing near-borderline steps. The paper should either discuss whether this noise affects training quality or provide evidence (e.g., correlation between 16-sample and 64-sample estimates on a subset).

- **Potential data contamination unaddressed**: Training data (VisualPRM400K) sources questions from MMRP/MMLR v1.1, while several evaluation benchmarks in Table 2 (MMMU, MathVista, MathVision, MathVerse, DynaMath, WeMath) overlap in domain. The paper does not analyze whether MMRP/MMLR v1.1 shares questions with these benchmarks, which could inflate reported gains.

- **Naming inconsistency**: The source dataset is called "MMRP v1.1" in the abstract (line 21) and "MMLR v1.1" in Section 3.1 (line 130). These should be aligned.

- **Figure 4 legend ambiguity**: The figure description lists "VisualPRM-8B" for both the red curve (squares) and blue curve (triangles), with no separate label for the ORM baseline mentioned in the caption. This appears to be an extraction artifact in the parsed PDF, but in the original submission, these should be clearly distinguished (presumably value-based vs. advantage-based PRM, or PRM vs. ORM).

### Trivial

None.

## Nice-to-Haves

- Add a "BoN with random selection" baseline column to Table 2 so readers can directly see how much gain comes from having N=8 candidates vs. from PRM-guided selection.
- Explicitly state whether the VisualProcessBench evaluation threshold is simply P(+) > P(-) or a tuned value.
- Quantify the extent of overlap between MMRP/MMLR v1.1 training questions and the evaluation benchmarks.

## Removed Points

These points were identified by reviewers but are removed per filtering rules:

- **Threshold specification for VisualProcessBench**: The harsh critic noted that the evaluation threshold is "not specified" (line 236: "by a certain threshold"). However, details about threshold exploration are deferred to Appendix B (see also line 154: "We also try to set a threshold... negatively impacts the PRM performance, as shown in Section B"). Per removal rules, weaknesses about appendix-deferred content are removed — the appendix exists in the original submission.
- **Figure 4 legend duplication**: The duplicate "VisualPRM-8B" label for both red and blue curves is a PDF extraction artifact. The original submission would distinguish these curves. Per removal rules for formatting/parser artifacts.
- **Missing related works / concurrent work**: Removed per rule that the reviewer cannot verify the existence of unmentioned works.
- **Priority claim skepticism**: "the first multimodal process supervision dataset" — the reviewer notes the paper does not check for concurrent work. Removed as speculative.

## Novel Insights

The harsh critic's most useful observation is that the controlled ablation (Figure 4) tells a fundamentally cleaner story than the headline Table 2. The fact that ORM performance *regresses* from N=64 to N=128 while PRM continues improving is a much sharper argument for step-level supervision than the uncontrolled Pass@1 comparisons. The paper would be substantially strengthened by centering this narrative rather than the current emphasis on absolute improvement numbers of uncertain provenance. Additionally, the near-chance performance of open-source MLLMs on VisualProcessBench (Table 3) is a striking negative result — models like InternVL2.5-78B scoring only 52.6% F1 — that deserves more emphasis as motivation for the work.

## Suggestions

1. Reframe headline claims around the controlled BoN comparisons (Figure 4, Table 4) rather than the uncontrolled Table 2. The controlled evidence is strong enough to stand on its own.
2. Add a "BoN with random selection" column to Table 2, or explicitly report a "sampling-only" baseline.
3. Explain how VisualPRM handles text-only inputs (Table 5) — a one-sentence clarification suffices.
4. Add an ablation comparing 16 vs. 64 MC samples for data labeling quality on a held-out subset.
5. Check and report whether MMRP/MMLR v1.1 contains questions overlapping with the evaluation benchmarks.
6. Fix the MMRP/MMLR naming inconsistency.

## Score and Decision

**Calibration methodology:**
- Round 1 bracketing: Three parallel searches for similar-topic papers across score bands. Low band (avg < 3.5) returned unrelated dataset papers (2.3–3.3). Mid band (3.5–7.5) returned OpenPRM (6.00, Accept), "Let's Verify Step by Step" (5.50, Accept), and ToolComp (5.40, Reject). High band (>7.5) returned RM-Bench (8.00, Accept) and other strong benchmarks. Initial bracket: [5.0, 7.0].
- Round 2 narrowing: Searched within [4.5, 6.0] and [6.0, 7.5]. Retrieved MMMU-Pro (5.80, Reject), MME-RealWorld (6.80, Accept), VL-ICL Bench (6.50, Accept), MEGA-Bench (7.00, Accept). The paper is stronger than MMMU-Pro (more original contributions: dataset + model + benchmark vs. just a benchmark revision) and comparable to OpenPRM.

**Anchor comparisons:**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/fGIqGfmgkW.md (OpenPRM) | 6.00 | R1 | Similar scope (PRM dataset construction + BoN evaluation). This paper has clearer methodology and more comprehensive evaluation across model families. Slightly stronger. |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/v8L0pN6EOi.md (Let's Verify) | 5.50 | R1 | Classic PRM paper (text-only). This paper extends to multimodal with more comprehensive evaluation. Slightly stronger. |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/qHpfxfnIq3.md (ToolComp) | 5.40 | R1 | Process supervision benchmark with PRM training. This paper has a larger dataset and more extensive evaluation. Stronger. |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/2jTdHYuguF.md (MMMU-Pro) | 5.80 | R2 | Benchmark-only contribution (rejected for incrementality). This paper has 3 contributions (dataset + model + benchmark). Clearly stronger. |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/k5VHHgsRbi.md (MME-RealWorld) | 6.80 | R2 | Polished large-scale benchmark. This paper has more methodological components but is less polished. Weaker. |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/cpGPPLLYYx.md (VL-ICL Bench) | 6.50 | R2 | Comprehensive multimodal benchmark. This paper has more diverse contributions but more methodological gaps. Weaker. |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/2rWbKbmOuM.md (MEGA-Bench) | 7.00 | R2 | Large-scale multimodal evaluation suite. Less directly comparable. Weaker. |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/QEHrmQPBdd.md (RM-Bench) | 8.00 | R1 | Polished, rigorous benchmark with strong correlation analysis. Clearly weaker. |

**Final score justification:** The paper makes genuine contributions — first multimodal process supervision dataset, a challenging step-level benchmark, and a trained PRM that demonstrates real improvements under controlled comparisons. However, the framing of headline results conflates sampling gains with PRM selection, and several methodological gaps (text-only handling, low MC samples, contamination risk) need addressing. These are fixable issues, not fatal flaws. The paper is comparable to or slightly stronger than accepted PRM papers (OpenPRM at 6.00, Let's Verify at 5.50) but less polished than top-tier benchmark papers (6.5–8.0). 

**Score: 6.0 — Accept.** The controlled evidence (Figure 4) convincingly shows PRM > ORM > SC at the same N, and the dataset/benchmark contributions fill genuine gaps. The framing and methodological gaps should be addressed in the camera-ready version.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>