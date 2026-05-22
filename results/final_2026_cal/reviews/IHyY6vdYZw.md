## Summary

This paper introduces VisualPRM400K, a dataset of ~400K multimodal process supervision samples with step-level correctness labels, and VisualProcessBench, a benchmark of 2,866 human-annotated samples for evaluating step-wise error detection in multimodal reasoning. Built on these resources, the authors train VisualPRM, an 8B process reward model. Under Best-of-N evaluation, VisualPRM improves reasoning performance across four MLLM families and seven benchmarks (e.g., +8.4 for InternVL2.5-8B, +5.9 for InternVL2.5-78B), outperforms ORM and self-consistency, and matches or exceeds GPT-4o and Gemini-2.0-Flash on process error detection.

## Strengths

- **First large-scale multimodal process supervision dataset.** VisualPRM400K (400K samples, ~2M steps) fills a clear gap left by text-only PRM datasets (PRM800K, MathShepherd), enabling a new line of research on multimodal PRMs. The dataset will be released.

- **Consistent and substantial BoN gains across diverse MLLMs.** Table 2 shows VisualPRM improves overall scores by 3.7–8.4 points for 7B–8B models (MiniCPM-V2.6, Qwen2.5-VL-7B, InternVL2.5-8B/26B/38B/78B) and 5.9 points for InternVL2.5-78B on seven multimodal reasoning benchmarks. The pattern holds across model families (InternVL, Qwen, MiniCPM) and scales, convincingly demonstrating the dataset's utility.

- **PRM consistently outperforms ORM and self-consistency, with gap widening at larger N.** Figure 4 shows VisualPRM surpasses ORM and SC by 1.5 and 2.4 points at N=8, growing to 4.3 and 3.1 at N=128 for InternVL2.5-8B. This is direct evidence that step-level supervision from VisualPRM400K produces a more effective critic than outcome-level alternatives.

- **Well-designed benchmark requiring all errors to be identified.** VisualProcessBench (2,866 samples, 26,950 human-annotated step labels) improves on prior benchmarks by requiring models to find *all* erroneous steps, not just the first. This reduces false negatives and aligns with modern reflection abilities.

- **VisualPRM (8B) matches proprietary models on process error detection.** On VisualProcessBench (Table 3), VisualPRM achieves macro F1 of 62.0, outperforming GPT-4o (60.3) and matching Gemini-2.0-Flash (62.3), despite being much smaller.

- **Generalization to text-only reasoning.** Table 5 shows meaningful gains on GSM8K, MATH-500, and GPQA-Diamond for both LLMs (Qwen2.5) and MLLMs (InternVL2.5), demonstrating the PRM is not limited to visual inputs.

## Weaknesses

### Major

- **No human validation of the training dataset labels.** The core contribution is VisualPRM400K, whose step-level labels are produced entirely automatically (16 Monte Carlo continuations per step, `mc_i > 0` → correct). The paper provides no human evaluation—not even a small random sample—of these labels. While the downstream BoN improvements provide *indirect* evidence of useful signal, they cannot rule out confounds (e.g., step position, length, or language style correlating with final answer correctness). The PRM literature standard includes human validation or at least agreement measurement (Math-Shepherd, PRM800K). This is the most important gap to address.

- **No error bars or statistical significance.** All BoN results (Tables 2, 4, 5, Figure 4) are reported as point estimates from what appears to be a single evaluation run. With temperature=0.7 sampling, the stochasticity is non-trivial, and some reported gains (e.g., +0.7 on MMMU for InternVL2.5-78B) could fall within evaluation noise. The paper makes strong comparative claims (PRM > ORM > SC) without confidence intervals, standard deviations, or multiple seeds. This weakens the reliability of the quantitative comparisons.

### Minor

- **ORM training baseline is underspecified.** The paper states ORM data is "nearly identical" to PRM data except that "step-wise correctness annotations are converted into a single correctness label for the outcome," but does not specify whether this label is final-answer correctness (matching ground truth) or an aggregation of step labels (e.g., incorrect if any step is wrong). These choices lead to different baselines. The ORM results (saturating at N=64, falling at N=128 in Figure 4) could be an artifact of the training choice rather than a fundamental limitation of ORMs.

- **Step decomposition methodology is not described.** The paper states that solutions are "split each of them into at most 12 steps" and "evenly merge the steps if the number of current steps exceeds the threshold," but does not explain how raw CoT solutions are initially chunked into steps. This is needed for reproducibility of both the training dataset and the benchmark.

- **No inter-annotator agreement for VisualProcessBench.** The benchmark uses human-annotated step labels, but no quantified agreement (Cohen's κ, Krippendorff's α) is reported. The paper mentions authors manually reviewed ~10% of samples, but this does not constitute a reliability measure. Given that the benchmark is intended for community use, this is a significant omission.

- **The base model for VisualPRM is not explicitly stated.** The paper describes VisualPRM as "an advanced multimodal Process Reward Model (PRM) with 8B parameters" but never explicitly states which base model it fine-tunes from. From context it appears to be InternVL2.5-8B, but this should be spelled out.

- **Text-only input handling not explained.** When evaluating on text-only benchmarks (Table 5), the paper does not explain how a multimodal PRM (trained on image+text inputs) handles text-only inputs — e.g., whether a blank image is passed. This detail is important for reproducibility.

### Trivial

None.

## Nice-to-Haves

- A small human validation study on 200–500 randomly sampled steps from VisualPRM400K, reporting agreement between the automatic `mc_i > 0` labels and human judgments, would substantially strengthen confidence in the dataset.
- Reporting BoN results with 3 random seeds (mean ± std) for the main tables would make the quantitative comparisons convincing.
- A discussion of dataset bias: training solutions come exclusively from the InternVL2.5 family, so the PRM may specialize to their error patterns. The paper already shows it works on other model families (a good start), but a brief discussion of possible distribution mismatch would strengthen the paper.
- An analysis of the distribution of `mc_i` values across steps (how many are near 0.5 vs 0 vs 1) would help assess label sharpness.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Harsh critic's specific calculation about mc_i threshold noise** ("a step with true success probability 0.4 will be labeled 'correct' about 46% of the time") — This calculation is mathematically incorrect under the paper's `mc_i > 0` threshold. For 16 samples with p=0.4, P(mc_i > 0) ≈ 99.97%, not 46%. Removed as factually wrong. The general concern about no human validation stands separately.
- **Strength Finder: "Addressed an important problem" / "filling a gap" framing** — These are generic and not concrete evidence. Removed.
- **Criticism that "ORM results could be an artifact of how it was trained"** — Partially valid, but softened by noting the ambiguity is minor and fixable. Moved to Minor weakness above with simplified framing.

## Novel Insights

Beyond the paper's own contributions, the most noteworthy finding across the reviews is the observation (from the review process of this paper and related concurrent works) that the multimodal PRM landscape is rapidly converging on Monte Carlo-based automatic labeling pipelines, and that the primary differentiator between papers is increasingly the *validation* strategy (consistency filtering in Athena, weak/strong completer checks, or, as missing here, human validation). This suggests the community may benefit from a standardized protocol for evaluating the quality of automatically generated process supervision labels.

## Suggestions

1. **Validate a random subset of VisualPRM400K with human annotators** (200–500 steps) and report agreement metrics (accuracy, Cohen's κ). This single addition would address the most significant gap in the paper.
2. **Report BoN results with confidence intervals** from at least 3 seeds or bootstrap sampling, at least for the headline results (Table 2 and Figure 4).
3. **Clarify the ORM training setup** — explicitly state whether outcome labels are final-answer correctness or step-aggregated.
4. **Report inter-annotator agreement** for VisualProcessBench (Krippendorff's α or Cohen's κ on a double-annotated subset).
5. **Describe the step-splitting mechanism** used to chunk raw CoT solutions into steps, and clarify how text-only inputs are handled.

## Score and Decision

### Calibration Report

**Round 1 — Bracketing:** Three queries on "multimodal process reward model dataset benchmark" returned weak anchors (scores 2.5–3.0: RoboReward, GUI-Shepherd, MOSS-ChatV — topically distant), middle anchors (scores 4.0–5.0: VRPRM, VL-PRM, MM-PRM, Athena), and strong anchors (scores 8.0: Embodied Navigation, Gaia2 — topically distant). The middle-anchor band is the relevant comparison: papers on multimodal PRMs average 4–5. The paper under review is clearly stronger than these (broader evaluation, larger dataset, new benchmark). **Initial bracket: 5–7.**

**Round 2 — Narrowing:** Two queries inside the bracket returned OCR-Reasoning (6.5, Accept Poster), MMR-Life (6.0, Accept Poster), R1-Reward (6.5, Accept Poster), and Omni-Reward (6.5, Accept Oral). Reading OCR-Reasoning (6.5), MMR-Life (6.0), and R1-Reward (6.5) in full provides the comparison: VisualPRM400K is comparable to MMR-Life (similar scope, similar data quality concerns) and slightly below OCR-Reasoning and R1-Reward (which have stronger methodological rigor or more novel technical contributions).

**Anchors consulted:**
- jEGH4snE99 (3.00, round 1, MOSS-ChatV) — distantly related RL+PRM paper; this paper is substantially stronger.
- sj9jmrBjMf (4.50, round 1, VRPRM) — similar PRM approach; this paper has broader evaluation and larger dataset.
- YyCgWQFGtL (5.00, round 1, Athena) — data-efficient PRM; this paper has more comprehensive experiments.
- E8t1iwV5Td (4.00, round 1, VL-PRM) — MCTS-based PRM; this paper has better evaluation breadth.
- aH7eyx64pC (6.50, round 2, OCR-Reasoning) — benchmark paper; this paper is slightly weaker on methodological rigor (no human training data validation).
- ds8bBklDV5 (6.00, round 2, MMR-Life) — benchmark paper; comparable in quality and contribution, similar data quality concerns.
- 4Ewgw9M2xE (6.50, round 2, R1-Reward) — reward model with RL training; this paper has a simpler but less novel technical approach.

**Final score: 6.0** — A solid Accept (Poster) level. The paper makes a genuine contribution (first large-scale multimodal PRM dataset + comprehensive benchmark + broad validation) with real but addressable weaknesses (no human validation of training labels, no error bars).

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>