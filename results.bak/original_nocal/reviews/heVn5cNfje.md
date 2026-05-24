Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

The paper proposes High-Entropy Sum (HES), a training-free metric that measures reasoning quality by summing the entropy of only the top 0.5% highest-entropy tokens in a reasoning trajectory. HES is used to select training data across three paradigms — SFT, RFT, and RL — and the authors demonstrate that HES-guided selection consistently outperforms random baselines and heuristic alternatives (length, difficulty, average entropy), with the strongest results in SFT where pruning the lowest-HES 20% of data improves over the full dataset.

## Strengths

1. **Validated across three training paradigms on multiple domains.** The paper evaluates HES under SFT (Tables 1–4, two model families, Math/Code/STEM), RFT (Table 5, per-query and global-pool settings), and RL (Table 6, GRPO). This breadth of validation is unusual for a data-selection metric and provides converging evidence that HES captures a generally useful signal.

2. **Small-to-large model transfer works quantitatively.** Section 4.1.2 reports that using Qwen3-0.6B as a proxy to compute HES for selecting data to train Qwen3-8B achieves 32.12% average accuracy, comparable to the 8B's self-selection (31.14%) — cutting inference cost by over an order of magnitude. This is a concrete, practically valuable finding.

3. **Simple, training-free, and cheap.** HES requires only a single forward pass to compute token-level entropy; no external reward model, LLM-as-judge, or additional training is needed. The sensitivity analysis (Section 4.4, Figures 3–4) confirms robustness to the key hyperparameters (selection ratio and entropy percentile).

4. **Lowest-HES data is demonstrably harmful.** The Lowest-HES-20% subset achieves only 14.90% average in SFT (vs. 25.89% for Random-20%), confirming the metric reliably identifies genuinely poor training samples. The Highest-HES-80% result (35.36%, surpassing Full-Dataset's 32.61%) makes a clean case that data quality, not quantity, drives performance.

## Weaknesses

### Fatal
None.

### Major

1. **Length confound is not analyzed or controlled for.** HES sums the entropy values of the top *p*% of tokens, so the number of tokens summed scales linearly with response length. Longer responses mechanically tend to have higher HES. The paper compares HES against length-based selection across all three paradigms (Tables 1, 5, 6), and HES does consistently outperform length — but the margins are modest (e.g., +0.47 points in SFT Table 1; ~+0.5–1.3 points in RFT Table 5). Without any correlation analysis between HES and length, length-controlled ablation, or partialling out length effects, it remains unclear whether HES's signal is meaningfully distinct from "longer responses are often better." This is the paper's most significant evidential gap, because the central claim of HES's superiority depends on it capturing something beyond what a simple length heuristic already captures.

2. **No variance or significance reporting.** All reported results are from single training runs. No error bars, multiple random seeds, or statistical tests are provided for any experiment. Given that many key comparisons hinge on small margins (e.g., RL Table 6: 21.30 vs. 20.63, a 0.67-point gap; SFT Table 1: 31.14 vs. 30.67, a 0.47-point gap), it is impossible to assess whether these differences are reliable or within run-to-run noise. This is particularly concerning for the RL experiments, where GRPO is known to have non-trivial variance across seeds.

### Minor

3. **Figure 1 polarity is not explained, creating confusion about the metric's interpretation.** Figure 1 shows that incorrect responses have substantially *higher* normalized HES (mean 0.68) than correct responses (mean 0.29). The paper describes HES as "distinguishing high- and low-quality samples" and states that "a higher HES score signifies greater diversity and complexity of reasoning patterns, indicating a higher learning value." The paper never explains why incorrect responses — presumably low-quality — score higher than correct ones. The practical use of HES is within pools of correct responses (SFT datasets, RFT correct-filtered pools, RL positive rollouts), where the empirical ranking aligns with better training outcomes. But the Figure 1 analysis mixes correct vs. incorrect, and readers will reasonably ask why a metric that flags incorrect responses as "high complexity" should be trusted to rank within correct ones. This does not invalidate the paper, but the authors should explicitly articulate that high HES reflects *complexity (fork density)* rather than *correctness*, and that within correct responses, high-complexity examples provide richer learning signal.

4. **RL evidence is narrow and the claimed advantage is small.** The RL experiments are conducted only with a 1.5B model, and absolute performance on most benchmarks is ~20%. The best strategy (Pos-High, Neg-Rand, 21.30%) outperforms Full-Batch (20.63%) by 0.67 points and the random-downsampling baseline (19.88%) by 1.42 points. While the directional result is consistent with the paper's thesis, these margins are small for a single-run experiment. The paper claims HES is "the unique strategy that ... surpasses the performance of the Full-Batch baseline," but Pos-Difficulty (20.27) and Pos-Longest (20.23) fall only slightly below Full-Batch, and whether any of these differences are meaningful cannot be determined without replication. The claim of uniquely superior performance is overstated relative to the evidence.

5. **The sensitivity analysis is limited to SFT.** Figures 3–4 vary the high-entropy token ratio and data selection ratio only for SFT experiments. The RFT and RL settings inherit the same hyperparameter choices without a dedicated sensitivity study, so the claim that HES is "robust" across all three paradigms is partially assumed rather than demonstrated.

### Trivial

6. **"Unique" language in RL conclusion (Section 4.3.2) slightly overstates the data.** The paper says HES is "the unique strategy that ... surpasses Full-Batch." This is technically correct (the other tested strategies fall below Full-Batch), but given the small margins and lack of replication, a more measured claim would be appropriate.

## Nice-to-Haves

- **Correlation analysis between HES and response length** across each dataset, to quantify how much of HES's signal is length-mediated.
- **Length-controlled ablation**: bin responses by length, then compare HES-selected vs. length-matched random controls within each bin.
- **Multiple random seeds (≥3) for at least the key comparisons** (SFT Table 1 Highest-HES-20% vs. Random-20% vs. Length-20%; RFT Table 5 per-query k=2; RL Table 6 Pos-High,Neg-Rand vs. Full-Batch).
- **RL at a larger scale (e.g., 7B–8B)** to demonstrate that the asymmetric sampling strategy generalizes beyond the 1.5B setting.
- **Concrete case studies** of high-HES vs. low-HES correct responses with annotated high-entropy tokens, to help readers build intuition for what HES captures qualitatively.

## Removed Points

- **"Figure 1 contradicts the paper's premise" (fatal framing).** The harsh critic claimed this as a fatal contradiction. However, the paper uses HES to rank *within* pools of correct responses (SFT datasets contain only correct solutions; RFT filters to correct; RL positive pool = correct rollouts). Figure 1's correct-vs.-incorrect comparison is about discriminative *ability*, not about the direction of ranking within correct responses. The paper's empirical results confirm that within correct responses, higher HES → better training outcomes. The lack of explanation is a real clarity issue (retained as Minor weakness #3) but not a contradiction invalidating the core claims.
- **"Duplicated paragraph in RFT section."** The extracted text shows a paragraph appearing twice (lines 290 and 292). This is a PDF extraction artifact from figure/table placement in the original PDF — not an author error.
- **"Sensitivity analysis only shows a few discrete values."** Four values (0.005, 0.05, 0.5, 1.0) spanning three orders of magnitude are shown across three domains. This is standard coverage for a hyperparameter sweep.
- **"Does not compare against DSD or influence-function approaches."** These are not claimed baselines. The paper scopes itself to training-free, efficient metrics. Comparing against expensive methods that serve as "upper bounds" is outside the stated scope.
- **"Missing related work."** A general concern about missing references without specific evidence cannot be reliably raised.
- **Strength Finder's generic strengths** ("important problem," "interesting question"): removed as superficial and not specific to this paper's evidence.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add a correlation analysis** (Pearson/Spearman) between HES and response length across the training datasets, and include a length-controlled experiment where you bin responses by length and compare HES selection vs. random within each bin. This would directly address the central confound concern.

2. **Run key experiments with at least 3 seeds** and report mean ± std or individual run values. This is essential for the RL results and the borderline SFT comparison against Length.

3. **Clarify the Figure 1 narrative.** Explicitly state: "HES measures reasoning complexity (fork density) rather than correctness. Among incorrect responses, higher HES reflects exploration of plausible but ultimately wrong paths. Among correct responses, higher HES reflects successful navigation of difficult forks, which provides richer training signal." This resolves the apparent polarity confusion without changing any results.

4. **Tone down the RL claims.** Replace "uniquely superior" / "unlocks superior performance" with language appropriate to the observed margin and single-run evidence, e.g., "suggests potential benefits" or "is a promising strategy."

## Score and Decision

**Score**: 7.0

**Decision**: Accept

The paper proposes a simple, intuitive, and cheap metric with a clean motivation. The evaluation is broad (3 paradigms, 2 model families, 3 domains), and the results are consistently positive and directionally aligned with the claims. The main weaknesses — the unaddressed length confound, the lack of variance reporting, and the overclaimed RL narrative — are real but addressable in revision. The SFT results alone (Highest-HES-80% surpassing the full dataset by nearly 3 points, Lowest-HES-20% collapsing to 14.90%) provide strong evidence that HES captures a meaningful quality signal. With the suggested analyses added, this would be a solid contribution with clear practical value for training-efficient reasoning systems.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>