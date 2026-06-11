## Summary
This paper introduces High-Entropy Sum (HES), a training-free metric that sums the entropy of only the top 0.5% highest-entropy tokens in a reasoning sample. The key intuition is that "forking tokens"—where the model considers multiple competing options—carry the signal about reasoning quality, while averaging over all tokens dilutes this signal. The paper validates HES across three training paradigms (SFT, RFT, RL) and three domains (math, code, STEM), showing that HES-based data selection consistently matches or outperforms full-dataset training while using less data.

## Strengths

1. **HES achieves dramatically better separation between correct and incorrect samples than existing entropy-based metrics.** Figure 1 shows normalized mean HES differs by 0.39 between correct (0.29) and incorrect (0.68) samples, while Average Entropy of All Tokens differs by only 0.01 (0.52 vs 0.53). This ~39× improvement in separation directly validates the paper's central claim that focusing on high-entropy tokens captures reasoning quality far better than global averaging.

2. **Pruning the bottom 20% of HES-ranked data consistently beats full-dataset training — a result no prior training-free selection metric has demonstrated.** Table 1 shows Highest-HES-80% achieves 35.36% average accuracy vs Full-Dataset's 32.61% on Qwen3-8B; Table 2 replicates this on DeepSeek-R1-Distilled-7B (32.35% vs 30.22%). The bottom-20%-HES data achieves only 14.90% — far below even a random-20% baseline (25.89%) — showing HES isolates genuinely harmful samples, not just less-useful ones.

3. **Comprehensive validation across three training paradigms (SFT, RFT, RL) and three domains (math, code, STEM).** This breadth is rare in data-selection papers. The core trend—HES-based selection outperforms random baselines and matches or surpasses full-data training—is consistent across all paradigms, with the SFT results being particularly strong and the RL results still positive.

4. **Small-to-large model transfer works effectively.** Using Qwen3-0.6B to screen data for training Qwen3-8B achieves 32.12% AVG, comparable to 8B self-selection (31.14%), while reducing inference costs by over an order of magnitude (Table 1). This practical efficiency for large-scale data curation is a genuine contribution.

5. **The RL asymmetric sampling strategy (Pos-High, Neg-Rand) is a clean design and the paper already includes the proper budget-matched control.** Pos-Rand, Neg-Rand (19.88%) uses the same number of rollouts as the HES strategy, and Pos-High, Neg-Rand (21.30%) still beats it, demonstrating that HES adds value beyond computational savings.

## Weaknesses

### Major

1. **No variance or statistical reliability information for any experimental result.** All tables report single point estimates (pass@1 averaged over 16 sampling paths) with no standard deviations, confidence intervals, or multiple independent runs. The severity of this gap varies across experiments:
   - **SFT**: These results are likely robust given the large and consistent margins (e.g., Highest-HES-80% at 35.36% vs Full-Dataset at 32.61%). The gap of ~2.75 points on average across 8 benchmarks makes variance concerns less critical here.
   - **RFT**: Gains over Random are modest (0.97–1.69 points average, Table 5). Without variance information, the reader cannot determine whether these gains are statistically significant.
   - **RL**: The headline improvement is 0.67 points average over Full-Batch (21.30% vs 20.63%), and the proposed method underperforms Full-Batch on 2 of 8 benchmarks (HMMT25, GPQA). With a single training run and pass@1 on 16 paths, these results may not be statistically significant. The paper's claim of "significantly surpassing existing training-free selection methods" is not adequately supported for the RL experiment.
   
   Adding bootstrap confidence intervals from the 16 sampling paths already collected, or running multiple seeds for the RL experiment, would substantially strengthen the paper.

2. **The RFT Global Pool (k=2) Random baseline has an unexplained GPQA score of 58.35%.** In Table 5, this value is far outside the range of all other GPQA entries in the RFT experiments (which cluster around 30–42%). This is likely a typo or a single-run outlier. While the overall HES vs. Random trend is consistent across other conditions and this anomaly does not threaten the paper's central claims, it undermines confidence in the evaluation protocol and should be corrected or explained.

### Minor

1. **The threshold p=0.005 sensitivity analysis uses only four coarse values (0.005, 0.05, 0.5, 1.0) and is only conducted in the SFT setting.** Testing intermediate values (e.g., 0.001, 0.01, 0.1) would give a clearer picture of how critical the exact threshold is. Additionally, MMLU STEM and LiveCodeBench show identical performance across all four ratios (Figure 4), which the paper does not comment on—this suggests either a ceiling effect or metric insensitivity on these benchmarks.

2. **Limited discussion of failure cases or limitations of HES.** The paper does not address scenarios where HES might underperform—e.g., if a model is poorly calibrated and assigns high entropy to uninformative tokens, or if the "high entropy = reasoning complexity" assumption breaks down for certain reasoning styles (e.g., repetitive long-CoT that rephrases the same uncertainty). A brief limitations section would improve rigor.

3. **The per-query vs. global-pool diversity trade-off is acknowledged but underexplored.** Section 4.2.2 correctly notes that per-query selection preserves query diversity, but the paper does not explore whether combining HES with explicit diversity mechanisms could improve global-pool performance. This is a natural extension worth discussing.

### Trivial

- The phrase "training-free" could be clarified: HES requires a forward pass (not cost-free), but the paper means "no additional model training or reward model is required." This is standard usage but a brief clarification would help.

## Nice-to-Haves

- An ablation varying training epochs for different-sized subsets could clarify whether HES selects data that converges faster or data that is fundamentally higher quality.
- Finer-grained threshold ablation (e.g., p ∈ {0.001, 0.01, 0.1}) would strengthen the claim about HES's robustness.
- A discussion of when HES might fail (e.g., with poorly calibrated models or degenerate high-entropy patterns).

## Removed Points

- **Budget-matched baseline in RL**: Removed because the critic claimed the paper lacks a baseline using 16 rollouts. However, Table 6 already includes Pos-Rand, Neg-Rand (19.88%), which is exactly the requested budget-matched control. The criticism is factually wrong.
- **Training epochs confound**: Removed because the critic argued fixed epochs confound data quality with optimization budget. However, the full dataset receives *more* gradient steps (3×100k vs 3×20k), which if anything advantages the full-dataset baseline. The concern's direction weakens rather than strengthens the argument.
- **Forking-Only convergence (32.51% vs Full-Dataset 32.61%)**: Removed because this empirical convergence validates the forking-token hypothesis that HES builds upon. It is a confirmation, not a weakness.
- **Code/STEM evaluation breadth**: Removed because the paper's primary evaluation is on math (6 benchmarks), with code and STEM as generalization checks (3 benchmarks each). Adequate for demonstrating cross-domain validity.
- **Missing related works**: Removed per policy — the reviewer cannot confirm missing citations exist.
- **Formatting/style nitpicks and typo comments**: Removed per policy — these are parser artifacts.

## Novel Insights

The reviews reveal a gradient not foregrounded in the paper: HES's effectiveness varies substantially by paradigm. In SFT, the gains are large (2-5 points) and the evidence is robust. In RFT and RL, the gains are small (0.67-1.69 points). This suggests HES may be most impactful as a pre-training data curation tool (SFT) and less impactful as a per-step signal during online training (RL). The paper's framing of "unified effectiveness" would benefit from acknowledging this gradient more explicitly, as it informs practitioners about where to deploy HES for maximum benefit.

## Suggestions

1. Add bootstrap-estimated confidence intervals (from the 16 existing sampling paths) or run multiple seeds for the core results, particularly for RFT and RL where margins are small.
2. Investigate and resolve the GPQA anomaly in Table 5 (Global Pool, k=2, Random = 58.35%).
3. Add a brief limitations paragraph discussing when HES might underperform.
4. Expand the threshold sensitivity analysis with finer granularity (e.g., p ∈ {0.001, 0.01, 0.1}).
5. Clarify "training-free" to specify that it means "no additional model training required," with the caveat that a forward pass is needed.

---

### Calibration Anchors

**Round 1 (Bracketing):**
- `EOPLy80bBm.md` (3.00) — Data pruning disentanglement study. Much weaker paper with questionable theoretical analysis and no novel method. Our paper is substantially stronger.
- `cijO0f8u35.md` (5.25) — Scaling relationships on GSM8K only. Our paper has broader evaluation (7+ benchmarks vs 1), a cleaner novel metric, and stronger results.
- `f4gF6AIHRy.md` (8.00) — DiSF submodular file selection for pre-training. Stronger paper with thorough analysis and no variance gap, but on a different task (pre-training vs. fine-tuning data selection).
- `SaOxhcDCM3.md` (3.20) — Self-consuming training loop study. Not directly comparable; our paper is clearly stronger.

**Round 2 (Narrowing):**
- `Fty0wTcemV.md` (6.00) — DELIFT for instruction fine-tuning. Our paper has a cleaner metric and broader validation across 3 paradigms vs. 3 stages of fine-tuning.
- `BTKAeLqLMw.md` (6.33) — What Makes Good Data for alignment. Our paper's HES is training-free (vs. requiring GPT-4 scoring) and validated on harder reasoning benchmarks.
- `SpTzsQjgxF.md` (5.75) — Rule-based rating with DPP. Our paper has a more novel core idea and stronger results.
- `I5p1Gm8GFS.md` (5.75) — 3DS for medical domain adaptation. Comparable scope but our paper's contribution is cleaner and the evaluation is broader.

**Bracket:** Round 1 placed the paper between ~5 and ~8. Round 2 narrowed to 6.0–7.0. The paper is consistently stronger than all 5.75–6.33 anchors (cleaner metric, broader validation, more striking results) but the absence of variance information prevents it from reaching the 7+ tier.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>