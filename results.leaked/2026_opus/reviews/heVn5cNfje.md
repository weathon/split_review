## Summary
The paper proposes High-Entropy Sum (HES), a training-free data selection metric that sums entropy values of only the top 0.5% highest-entropy tokens in a reasoning trajectory. The authors validate HES across SFT, RFT, and RL settings, claiming that the top-20% HES subset can match or surpass full-dataset performance, and that an asymmetric RL sampling (Pos-High, Neg-Rand) outperforms standard GRPO. The paper positions HES as a unified, model-agnostic metric for efficient training of reasoning LLMs.

## Strengths
- **Concrete SFT data-efficiency result.** Training on the top‑20% HES subset (31.14) closely approaches full-dataset performance (32.61), and the top‑80% HES subset (35.36) surpasses the full dataset by 2.75 points on Open-Math-Reasoning (Table 1). The Lowest‑HES‑20% catastrophe (14.90) is a striking, easily‑replicable finding.
- **Empirical breadth.** Validation spans two SFT datasets, two base models, three RFT candidate-pool sizes (k=2,4,8) in both per-query and global-pool settings, an RL configuration with multiple baselines, and out-of-domain transfer to Code (Table 3) and STEM (Table 4) where Highest-HES-20% beats the full dataset (39.54 vs 36.28; 49.56 vs 44.42).
- **Small-to-large proxy transfer.** A 0.6B model used as a selector for an 8B model achieves Avg 32.12% (Table 1), an order-of-magnitude cheaper than self-selection while remaining competitive. This is a practical and concrete finding.
- **Discrimination evidence in Figure 1.** Compared to AvgE (0.52 vs 0.53) and AvgHE (0.82 vs 0.82), HES does produce strongly separated means between correct (0.29) and incorrect (0.68) groups, demonstrating that the high-entropy-sum signal separates these populations more than averaging-based metrics.

## Weaknesses

### Fatal
None.

### Major
- **Motivating evidence direction conflicts with how HES is used.** Figure 1's table (page 1) shows higher HES tracks *incorrect* model rollouts (0.68 vs 0.29). The method then selects *highest-HES* samples as high-learning-value for SFT/RFT/RL. The paper never reconciles this — it never explicitly distinguishes "HES on the model's own rollouts" (where high HES correlates with errors) from "HES on reference/positive trajectories used for training" (where the paper interprets high HES as quality). Without this distinction stated, the central conceptual story is at odds with the only piece of evidence presented to motivate it.
- **HES is structurally entangled with length and the paper offers no disentangling analysis.** The relative threshold sums the top-0.5% token entropies; by construction the number of summed tokens scales linearly with length, so HES ≈ length × upper-tail mean entropy. Footnote 1 claims the relative threshold "makes this metric robust to variations in length," but mathematically it does the opposite. Table 1 shows Length-20% selection (30.67) is only 0.47 below Highest-HES-20% (31.14), and in RFT (Table 5, k=2 per-query) Length 30.27 vs HES 31.38 — a single-point gap. No length-controlled comparison (e.g., bin by length and rank within bin) is reported, so the claim that HES captures "reasoning complexity" beyond length is not isolated.
- **Headline RL gains are within plausible noise; no variance is reported.** Table 6 reports Pos-High/Neg-Rand 21.30% vs Full-Batch 20.63% (+0.67) and Pos-Difficulty 20.27 / Pos-Longest 20.23 (+1.0). On AIME-style 30-problem benchmarks at pass@16, single-point differences correspond to a handful of problems flipping. No seeds, standard deviations, or significance tests are provided. The paper's abstract claim that HES "significantly surpasses" alternatives is not supported by the reported numbers. Notably HMMT25 actually drops from 15.21 (Full-Batch) to 11.88 (Pos-High/Neg-Rand), consistent with noise-level fluctuations.
- **The "top-0.5% only" central design choice barely beats the trivial alternative.** In Table 1, Highest-ES (sum of *all* token entropies, the trivial baseline that the paper's introduction explicitly argues against) reaches 30.92 vs. Highest-HES 31.14, a gap of 0.22. The paper's introduction argues "the averaging mechanism of traditional metrics dilutes the signal from these key tokens" and that summing only key tokens is what matters — but Highest-ES sums everything and still nearly matches HES. This near-tie undermines the conceptual case for the top-0.5% threshold.

### Minor
- **Sensitivity-analysis tables contain unrealistic identical-to-three-decimals values.** Figure 4 reports MMLU STEM = 0.855, 0.855, 0.855, 0.855 and LiveCodeBench = 0.544, 0.544, 0.544, 0.544 across four very different high-entropy-token ratios (0.005, 0.05, 0.5, 1.0). Either the entries are reporting/extraction errors, or the metric is not actually discriminating between these settings (in which case the paper's claim that the 0.005 ratio "consistently delivers the best performance" is not supported in these two domains).
- **Table 5 inconsistencies.** The Length row appears nearly duplicated across k=2 and k=4 in both per-query and global-pool settings (e.g., k=2 per-query Length: 46.04/33.33/33.75/28.13/19.58/35.94/4.81/40.56; k=4 per-query Length: 46.04/33.33/33.75/28.13/19.58/35.94/4.81/40.44). The Difficulty baseline is also missing from the per-query rows but present in the global-pool rows. The table needs auditing.
- **Small-proxy-better-than-self interpretation glosses over a tension.** Section 4.1.2 reports Qwen3-0.6B selection (32.12) outperforms Qwen3-8B self-selection (31.14). The paper frames this as transferability evidence, but a smaller model's selection outperforming the target model's own signal is more naturally read as evidence that the differences are within single-run variance, or that HES is picking up surface properties not specific to the model's reasoning. Some discussion is warranted.
- **RL ablation conflates two changes.** The Pos-High/Neg-Rand strategy changes both (a) the rollout-selection criterion and (b) reduces batch size by 50%, but the comparison to Full-Batch confounds these. A "highest-HES half vs. random half" comparison at fixed batch size would isolate the HES contribution; the current comparisons do not.
- **Open-R1-Math-220k essentially eliminates the benefit of careful selection.** Table 2: Random-20% (30.38) ≈ Full-Dataset (30.22). On this dataset Highest-HES‑20% (34.61) still wins, but the random baseline already matches full data — which complicates the universal "data-quality drives performance" framing.
- **Lowest-HES catastrophe is overinterpreted as identifying "quality."** The 14.90% result strongly demonstrates that bottom-HES samples are *bad* (likely trivial/memorized/very short), but this does not by itself establish that the *top* HES samples are *good* — a length floor or any triviality filter would likely produce similar exclusions. The paper's framing leans on the dramatic gap from the lowest end to claim discrimination of quality across the whole range.

### Trivial
- The §3.1 definition of AvgHE ends with "different from AvgHE," presumably a typo for "different from AvgE."

## Nice-to-Haves
- Add length-controlled comparisons (bin by length, rank within bin; or jointly regress accuracy on length and HES).
- Report multi-seed runs for the RL experiments (which is where the gains are smallest); report standard deviations across seeds for all main tables.
- Investigate the Highest-ES vs Highest-HES near-tie with a fine sweep over the top-k ratio, and an analysis of whether the signal lives narrowly in the top or is broadly distributed.
- Clarify whether HES is computed on the data sample's reference trajectory or on a model rollout, since this changes the interpretation completely; align Figure 1's setup with the actual selection setup used downstream.
- Audit Table 5 Length rows and Figure 4 identical values.

## Removed Points
These points are flagged to be removed, treat them with caution.
- *"Missing related work / why summation vs count vs max not justified beyond AvgHE ablation"* — Borderline scope creep, the paper does evaluate the natural alternative (AvgHE) and the trivial alternative (Highest-ES). Demoted into the Major weakness above about the small ES vs HES gap rather than carried as separate criticism.
- *"Important problem, timely topic"* (Strength Finder) — Removed as generic.
- *"Cross-model generality (proxy model)"* as a clean strength — In tension with the Minor weakness above that the smaller-model-beats-bigger-model finding is more easily explained by noise; kept as a strength but with caveat.
- *"Sensitivity analysis confirms HES is robust and 0.5% is optimal"* (Strength Finder) — Removed/weakened because the same Figure 4 also contains the identical-three-decimal artifact across all ratios; cannot serve as clean evidence for hyperparameter robustness.
- Any concern about "cannot be independently verified" or release status of cited models/datasets — Per hard rules.

## Novel Insights
None beyond the paper's own contributions. The most interesting empirical observation is that pruning the lowest-HES 20% improves over the full dataset (Highest-HES-80% surpassing 100%-data), which suggests a coherent low-quality-data-as-noise effect; however the paper does not establish that HES is the right *positive* signal as opposed to a good *triviality filter*.

## Suggestions
- Reframe the claim of the paper around what is robustly supported: HES (and arguably any reasonable triviality filter) effectively *excludes* low-quality data; the case that HES uniquely *identifies* high-quality data needs the length-controlled and finer top-k analyses described above.
- Replace Figure 1 with evidence aligned to the actual selection setting (HES computed on training-target trajectories, with downstream training utility as the dependent variable).
- Report multi-seed RL results before claiming statistical superiority.
- Add a "HES residualized on log-length" analysis to Table 1, Table 5, and Table 6 so readers can see how much signal remains after the length component is partialled out.
- Audit and correct Figure 4 and Table 5; clarify the small-model proxy result in light of within-noise variation.

## Evaluation along the requested axes
- **Originality:** Moderate. The core idea (sum top-entropy tokens) is an incremental aggregation choice on top of prior work (Wang et al. 2025, forking tokens). The unified deployment across SFT/RFT/RL is the more novel contribution.
- **Importance of the research question:** High. Training-free data selection for reasoning LLMs is a real and active problem.
- **Whether claims are well supported:** Partially. SFT-side claims (top-20% ≈ full, top-80% > full, Lowest-HES catastrophic) are well supported. RL "significantly surpasses" claim is not. The conceptual claim that the top-0.5% summation is the right design is weakly supported (Highest-ES near-tie).
- **Soundness of experiments:** Mixed. Broad coverage but no variance reporting on a paper that often claims sub-1-point wins; key confound (length) not analyzed; sensitivity-analysis artifacts.
- **Clarity:** Acceptable. Method definitions and tables are readable, but the motivation/method disconnect, definition typo, and Table 5 inconsistencies indicate insufficient proofreading.
- **Value to the research community:** Moderate. The negative finding (bottom-HES is highly harmful) is useful; the positive HES-as-quality story needs more work to be trusted.

## Calibration

Anchors retrieved across rounds:

Round 1 (bracketing):
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/OdoS6cH8MP.md` — avg 2.00, weak; far weaker scope and evidence than HES.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/z3DMFpaP6m.md` — avg 3.00, weak; entropy-as-metric paper with unclear evaluation, weaker than HES.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/EOPLy80bBm.md` — avg 3.00, weak; clearer methodological issues than HES.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/uMxiGoczX1.md` — avg 2.50, weak.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Z8Mfy0iK4n.md` — avg 3.67, entropy-based reliability work; comparable presentation but narrower scope.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Fty0wTcemV.md` — avg 6.00 (Accept), DELIFT; more thorough method validation than HES; HES is below this.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/qUJsX3XMBH.md` — avg 4.40 (Reject), "Random Selection is Almost All You Need"; very topically close, similar empirical breadth, similar level of caveats.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/SpTzsQjgxF.md` — avg 5.75, rule-based selection; comparable methodological care, possibly slightly more rigorous.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/51WraMid8K.md`, `f4gF6AIHRy.md`, `07yvxWDSla.md`, `WJaUkwci9o.md` — avg 8.00 each; all substantially stronger than HES.

Round-1 bracket: between 4.0 and 6.0.

Round 2 (narrowing):
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/YQvvJjLWX0.md` — avg 5.50 (Semantic Entropy Probes); cleaner methodology, narrower scope.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/uO0itv7XFa.md` — avg 4.67 (Disentangling Reasoning Tokens); very close conceptually (treat different tokens differently); HES has broader scope (3 paradigms) but more verifiable issues (Figure 4 artifacts, length confound, motivation/figure contradiction).
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/LDmJfJlo83.md` — avg 4.25; entropy-based UQ work, comparable.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/I5p1Gm8GFS.md` — avg 5.75 (3DS); more careful decomposition and evaluation, somewhat stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/diKRhKs5yl.md` — avg 5.25; comparable.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/tbx3u2oZAu.md` — avg 6.00 (Accept), narrower theoretical contribution; HES is below.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/ouRX6A8RQJ.md` — avg 6.40; somewhat stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/PfrpYGKGPL.md` — avg 5.50; different topic.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/ILStlRb1Sp.md` — avg 5.00; different topic.

The closest topical anchors are "Random Selection is Almost All You Need" (4.40) and "Disentangling Reasoning Tokens" (4.67). HES has broader scope (SFT+RFT+RL+cross-domain+proxy transfer) than either but more concrete methodological issues (length entanglement without disentanglement; motivation/figure direction conflict; identical-across-settings sensitivity entries; the 0.22-point gap to the trivial Highest-ES baseline). It is meaningfully below the cleaner 5.75 anchors (3DS, rule-based) and well below DELIFT (6.00, Accept).

Final placement: closer to the 4.67/4.40 cluster than to the 5.50–5.75 cluster, with the broader scope partially offsetting the methodological concerns.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>