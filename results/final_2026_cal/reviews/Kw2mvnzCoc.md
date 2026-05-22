## Summary

TSPulse introduces a family of ultra-compact (1M parameter) pre-trained time-series models that learn three embedding views (temporal, spectral, semantic) through multi-objective reconstruction heads, a hybrid masking scheme, and lightweight post-hoc fusers for anomaly detection, classification, imputation, and similarity search. Across 75+ datasets, TSPulse consistently matches or outperforms models 10–100× larger while enabling CPU-only inference. The paper is well-engineered with broad empirical coverage.

## Strengths

- **State-of-the-art performance at 1M parameters.** TSPulse achieves strong results across four diagnostic tasks on 75+ datasets, outperforming models 10–100× larger (e.g., +24% VUS-PR over SubPCA on TSB-AD-U with fine-tuning, +73% MSE reduction over MOMENT for zero-shot imputation under hybrid masking, +5–16% classification accuracy on UEA). The compact size enables genuine CPU-deployable real-time inference (0.387ms per query on CPU).

- **Clear architectural contributions validated by ablations.** The ablation study (Table 1) systematically validates each design choice: multi-head triangulation beats all single-head variants by 9–16%; replacing TSLens with pooling drops classification accuracy 11–16%; identity initialization of channel-mixers prevents 9% degradation; removing hybrid pre-training causes 79% MSE increase in imputation. This is unusually thorough for a systems paper.

- **Sensitivity analysis demonstrates meaningful embedding specialization.** Table 2 shows that temporal embeddings are 130% sensitive to phase shifts, FFT embeddings 21%, and semantic embeddings only 12%, confirming that different embedding segments capture genuinely complementary properties rather than redundant information. This goes beyond what most time-series pre-training papers provide.

- **Extreme efficiency without sacrificing accuracy.** The timing comparison (Figure 7) shows 14–120× faster CPU inference than MOMENT and Chronos from a model 40× smaller, using 240-dim embeddings (2× smaller). This makes a credible case for GPU-free real-time deployment.

## Weaknesses

### Major

- **Imputation evaluation favors TSPulse's own pre-training corruption.** The main imputation results (Figure 6, showing 73% improvement over MOMENT) evaluate on hybrid masking after TSPulse was pre-trained with hybrid masking, while MOMENT was pre-trained with block masking only. This is acknowledged in the ablation (w/o Hybrid PT causes 79% MSE increase) and block-masking results are deferred to the appendix, but the headline claim is inflated by this misalignment. The paper should report both masking types prominently in the main paper or use a test distribution not explicitly matched to one method's pre-training.

- **"Disentanglement" framing exceeds what is demonstrated.** The paper claims "disentangled" embeddings in the title, abstract, and contributions, but the mechanism is that different segments of the decoder output are optimized with different loss functions while the backbone processes all tokens jointly — this produces *specialization*, not disentanglement in any standard sense (no MIG, DCI, mutual information, or factor-independence analysis). The sensitivity analysis (Table 2) shows complementary properties, which is genuine and valuable, but the term "disentangled" should be replaced with "specialized" or "multi-view" throughout. This is a framing issue, not a methodological flaw.

### Minor

- **Zero-shot AD uses labeled data for head selection.** TSPulse-ZS selects the best reconstruction head using the labeled official tuning set. While the paper is transparent about this practice (it is standard on the TSB-AD benchmark), calling it "zero-shot" is imprecise. The Head_ensemble variant (no labels) is reported in Table 1(a) and still performs well (0.44 on univariate), so the concern is primarily terminological. Renaming to "unsupervised (label-free head selection)" or adding a truly label-free variant would resolve this.

- **Ablation on 17/29 UEA datasets without selection rationale.** The classification ablation (Table 1b) uses a subset of 17 UEA datasets described only as "representative" for faster analysis, with no justification of the selection criteria. If the subset is biased, the ablation conclusions may not generalize. Either use all 29 datasets or state the selection criteria explicitly.

- **Abstract "20%" claim is ambiguous.** The abstract states "+20% on the TSB-AD anomaly detection leaderboard" without specifying the variant. TSPulse-ZS achieves 14% improvement over SubPCA; TSPulse-FT achieves 24%. The paper should specify which variant is being compared.

### Trivial

- The IMP(%) column in Figure 4(a) shows "33%" for TSPulse(ZS) over MOMENT(FT) — 0.48 vs 0.39 is actually a 23% relative improvement, not 33%. The IMP figures appear to use different baselines for different rows rather than a consistent reference, which can confuse readers.

## Nice-to-Haves

- A per-dataset breakdown of the classification ablation (for the 17 UEA datasets) would show whether the benefit is consistent or driven by a few datasets.
- Results with standard deviations across multiple random seeds would strengthen statistical claims.
- Failure-case analysis (datasets where TSPulse underperforms) would increase trust.

## Removed Points

These points from the input reviewers are removed for the following reasons:

- **Criticism that the backbone processes all tokens jointly and thus "no disentanglement"** — REMOVED as overstatement. The paper's loss functions assign different objectives to different embedding segments, and the sensitivity analysis (Table 2) shows that this produces measurably different properties across embedding types. Whether one calls this "disentanglement" or "specialization" is a semantic debate, not a factual error. The criticism is retained in the "Major" section as a framing concern.

- **"No runtime comparison across all tasks"** — REMOVED. The paper provides runtime for similarity search (Figure 7) which is the most latency-sensitive task. Classification, imputation, and AD inference are each a single forward pass through a 1M-parameter model; the timing data generalizes.

- **"Missing analysis of model size scaling"** — REMOVED. The paper's claim is about the sufficiency of small (1M) models, not about scaling properties. Requesting 500K and 5M variants is scope creep.

- **"Missing hyperparameter ranges for fusers"** — REMOVED. These are detailed in the appendix (which is stripped from the parser view but exists in the original submission).

- **"Missing anomaly score computation details for MHT"** — REMOVED. The paper states anomaly scores are computed "based on the deviations between the original and predicted signals" (Section 3.3) and Figure 3(D) illustrates the process. This is sufficient for a conference paper; full details belong in the appendix.

- **Strength Finder's strength about "extreme CPU efficiency"** — RETAINED as it is concrete and backed by specific numbers.

## Novel Insights

None beyond the paper's own contributions. The reviews primarily surface framing/terminology issues that should be corrected, not new scientific insights about the method.

## Suggestions

1. Replace "disentangled" with "specialized" or "multi-view" throughout the paper, or add a precise definition and quantitative disentanglement metric (e.g., MIG, DCI) to justify retaining the term.
2. Present imputation results under both hybrid and block masking in the main paper, not the appendix.
3. Clarify the "zero-shot" AD framing — either rename the variant or include a truly label-free variant using a fixed rule.
4. Specify the selection criteria for the 17-dataset ablation subset and ideally expand to all 29 UEA datasets.
5. Clarify the abstract: specify which variant achieves the +20% gain on TSB-AD.
6. Add per-dataset results for classification to understand variance.

## Score and Decision

### Calibration Report

**Round 1 (Bracketing):**
- Weak anchors (< 3.5): IJDztMLEXw (2.50, Reject — cross-domain AD, limited), 1ndthBqbyK (2.50, Reject — teacher-student pre-training), G7owOY1NcF (2.00, Reject — anomaly detection), kIQFvnCCIp (3.00, Reject — multivariate scaling).
- Middle anchors (3.5–7.5): iqUMjxfDNH (5.00, Accept — compact model portfolios), wNEzRYiyZM (5.50, Accept — medical TS classification), H27kvyG4qf (5.00, Accept — critiques TSFMs for AD), 5jkzTzV5Ao (5.50, Accept — TS FM biases analysis).
- Strong anchors (> 7.5): kkBOIsrCXh (8.00 — embodied navigation, different domain), oBXfPyi47m (8.00 — RL, different domain).

**Round 1 bracket**: (4.5, 7.0). The paper is clearly above the weak-anchor band but below the 8+ band given its framing issues.

**Round 2 (Narrowing):**
- p9azaewKgh (5.33, Reject — LVM for TS, different topic), iqUMjxfDNH (5.00, Accept — model portfolios, mixed reviews), fMdVvUGrl3 (5.33, Reject — memory transformers, different topic), XrmXvv75KP (4.67, Accept — model selection framework).
- VVJ6Ck9JBl (6.00, Accept — Aurora, multimodal FM), RXaoGgjrFs (6.00, Reject — SlotFM, motion FM), qetBM8nLkf (6.00, Accept — irregular TS benchmark), JRlNrcTllN (6.00, Accept — CoRA, correlation adapter).

**Comparison to key anchors**: TSPulse is stronger than the model-portfolios paper (5.00) in terms of architectural innovation and breadth of evaluation. It is comparable to CoRA (6.00) and Aurora (6.00) — both accepted as posters with solid contributions but notable weaknesses. TSPulse has more extensive evaluation (75+ datasets, 4 tasks) than CoRA or Aurora, but its framing issues (disentanglement overclaim, imputation evaluation bias) are somewhat more central to its identity.

**Final score**: 6.0. This positions the paper in the solid-acceptable range, above the middle (5.0), recognizing its genuine empirical and engineering contributions while accounting for the fixable framing issues that prevent it from being a top-tier contribution.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>