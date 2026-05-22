Now I have all the calibration data I need. Let me compile the final review.

**Round 1 Bracket:** Based on the calibration search, TSPulse sits above the weak band (scores 2.5-3.0, rejected) and the mid-range papers like DADA (6.0) and ROSE (5.75). It's below the top band (FITS 8.0, TimeMixer++ 8.0). My initial bracket is **5.5 to 7.5**.

**Round 2 Narrowing:** Comparing against anchors within the bracket:
- vs DADA (6.0): TSPulse covers more tasks, has stronger empirical breadth, and released code/models. **TSPulse is stronger.**
- vs ROSE (5.75, Reject): TSPulse covers more tasks and has stronger results. ROSE was rejected partly due to complexity and limited task scope. **TSPulse is clearly stronger.**
- vs DAM (7.0, Accept): DAM focuses on a single task (forecasting) with a novel architecture. TSPulse covers 4 tasks but has more framing issues. **Comparable but different.**
- vs Time-MoE (7.33): Billion-scale MoE, different league entirely. Not directly comparable.

TSPulse lands between 6.0 and 7.0. I'll go with **6.5**.

---

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses

### Fatal

### Major

### Minor

### Trivial

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

Let me now write the full review.Here is my consolidated final review.

---

## Summary

TSPulse introduces a family of ultra-light pre-trained time-series models (1M parameters) that learn disentangled representations across temporal, spectral, and semantic spaces. It achieves strong results on four diagnostic tasks — anomaly detection (leaderboard-topping on TSB-AD), imputation (50%+ gains under hybrid masking), classification (5–16% improvement on UEA), and similarity search (25–40% improvement) — while being 10–100× smaller than competing pre-trained models and supporting GPU-free deployment.

## Strengths

1. **Strong and consistent empirical breadth across four diagnostic tasks.** TSPulse achieves SOTA or near-SOTA results on anomaly detection (first on TSB-AD-U and TSB-AD-M leaderboards), imputation (MSE 0.074 ZS vs MOMENT's 0.276), classification (0.733 vs VQShape's 0.701 on UEA), and similarity search (PREC@3 0.68 vs MOMENT's 0.53). This coverage of multiple tasks in a single 1M-parameter model is a genuine practical contribution.

2. **Extreme parameter efficiency and CPU-friendly deployment.** At 1M parameters, TSPulse is 40× smaller than MOMENT (40M) and 46× smaller than Chronos (46M), while running 14× faster on CPU (0.387ms vs 5.51ms). The GPU-free deployment claim is well-supported and practically valuable for edge/real-time settings.

3. **Sensitivity analysis provides concrete evidence of embedding complementarity.** Table 2 shows that semantic embeddings distort only 4.6% under 30% missing data versus 27.4% for FFT embeddings, and 12% under phase shifts versus 130% for temporal embeddings. This controlled experiment directly validates the claimed disentanglement properties, beyond what ablation alone can show.

4. **Multi-head triangulation and TSLens are practically useful post-hoc designs.** Ablation shows MHT (Head_triang) outperforms any single head by 14–16%, and TSLens provides 11–16% gains over pooling baselines. These are clean, task-specific adaptations that leverage the disentangled representations effectively.

5. **Hybrid masking is a simple but impactful contribution.** The ablation shows that removing hybrid pre-training causes a 79% drop in imputation MSE (0.074 → 0.354). The design of mask tokens at the raw patch level (rather than embedding space) to flexibly support both full and partial masking is clean and effective.

## Weaknesses

### Major

1. **"Zero-shot" anomaly detection uses labeled validation data for head selection, which stretches the standard definition.** The paper transparently states (Section 4.1 Setup) that the official labeled tuning set is used for multi-head triangulation to select the best head. While the paper notes this tuning set is "consistently used across all leaderboard methods" for hyperparameter selection, the nature of usage differs — TSPulse uses labeled anomaly scores to pick the best head, whereas baselines use the same set for standard hyperparameter tuning. The headline "+20% on the TSB-AD leaderboard" and the "ZS" label conflate two regimes. This does not invalidate the results (the comparison to other pre-trained methods is still favorable), but the paper would benefit from more precise terminology — e.g., "Head-tuned zero-shot" or "ZS+Tune" — and a clear statement of what the tuning set provides to each method.

2. **Classification results lack statistical rigor.** The UEA comparison (Figure 5) reports only mean accuracy over 29 datasets without confidence intervals, per-dataset breakdown, or statistical significance tests (e.g., Wilcoxon signed-rank test against VQShape, the strongest baseline). With 29 datasets, a 5% mean difference could be driven by a few datasets. Similarly, the ablation (Table 1b) uses only 17 of 29 UEA datasets "for faster analysis" without specifying the selection criterion. If the subset is not representative, the reported drops may not generalize.

### Minor

3. **The disentanglement claim is supported but oversold relative to the evidence.** The ablation shows that hybrid masking (w/o Hybrid PT → 79% MSE increase) contributes far more to imputation gains than dual-space learning (w/o Dual-Space → 8% increase). Classification ablations show similar patterns (w/o Short/Long embedding → 8–10% drop; w/o Dual-space → 7% drop). The sensitivity analysis in Section 6 provides genuine evidence of complementary embedding properties, but disentanglement is framed as "the core novelty" while the ablation data suggests hybrid masking is the larger performance driver. The paper would be stronger if it acknowledged this attribution balance more explicitly.

4. **No error bars or variance estimates are reported for any experiment.** Given the variability of time-series datasets (especially small UEA datasets), single-run evaluations make it hard to assess whether reported gains are statistically reliable. This is a common omission but worth noting.

5. **No direct ablation tests disentanglement against an entangled control with equal capacity.** The paper does not compare against a variant where the same total parameter budget and loss functions are used, but embedding segments are not assigned to different heads (i.e., all tokens participate in all losses). Such an ablation would directly test whether the architectural separation — rather than additional capacity or multi-task losses — drives the gains. The sensitivity analysis is indirect evidence.

### Trivial

6. The "virtual channel expansion" trick is mentioned in the classification ablation (2% drop) but never described in the main text; readers must infer what it is.

## Nice-to-Haves

- Adding a direct disentanglement ablation (entangled control with equal capacity and losses) would strengthen the core claim.
- Per-dataset results for UEA classification in the main paper (or a clear pointer to the appendix) would improve transparency.
- A variant of TSPulse without tuning-set head selection would clarify the true zero-shot AD performance.
- Brief exploration of scaling (e.g., 3M or 5M variants) would be informative but is not necessary given the paper's explicit focus on ultra-compact models.

## Removed Points

- **Criticism about the disentanglement not being formally guaranteed (no explicit regularization contrast).** Removed because the sensitivity analysis (Table 2) provides empirical evidence of disentanglement, which is standard practice in representation learning papers. The paper does not claim formal disentanglement guarantees.
- **Criticism that MOMENT (ZS) may not have used the tuning set.** Removed because the paper states the tuning set is "consistently used across all leaderboard methods." This is a factual claim in the paper; questioning it is speculation.
- **Criticism about missing related works.** Removed per protocol — I cannot verify missing references.
- **Criticism about missing appendix content.** Removed — parser artifacts.
- **Strength about "State-of-the-art zero-shot AD across 40-method leaderboard."** Weakened and moved into the main strengths with caveat about the tuning set usage, which is now reflected in Weakness #1.
- **Strength about "Multi-head triangulation superior to any single head."** Retained as Strength #4 but noted as supporting rather than core.
- **Several generic/superficial strengths from the Strength Finder.** Removed.

## Novel Insights

The key insight that is not fully explored in the paper but emerges from the ablation analysis is that hybrid masking (a relatively simple engineering contribution) drives more of the performance gains than the architectural disentanglement (the paper's marquee novelty). This is not a fatal contradiction — both are valid contributions — but it suggests that future work on pre-training strategies for time-series diagnostics might benefit more from focusing on masking diversity than from complex architectural separation of representations. The sensitivity analysis provides a secondary novel insight: semantic embeddings are remarkably robust to distortions (4.6% distortion under 30% missing data vs 27.4% for FFT embeddings), which directly explains why they work well for similarity search and opens a clear path for retrieval-focused applications.

## Suggestions

1. **Clarify the AD zero-shot protocol.** Rename "TSPulse (ZS)" to something like "TSPulse (ZS+Tune)" and explicitly state that the tuning set is used for head selection, reporting what the purely zero-shot (no tuning set) performance would be for reference, even if lower.
2. **Add statistical testing for classification.** Report per-dataset accuracy, average rank, and a Wilcoxon signed-rank test against VQShape. Justify the 17-dataset ablation subset or expand to all 29.
3. **Add a direct disentanglement ablation.** Train a variant where all embedding segments share all losses (no head-specific assignment) with the same total capacity, and report the accuracy/MSE difference. This would directly validate the disentanglement claim.
4. **Include error bars or confidence intervals** for at least the main experiment (UEA classification, imputation).
5. **Acknowledge contribution attribution balance** in the paper: state clearly that hybrid masking contributes substantially to imputation gains, and position disentanglement as complementary rather than primary.

## Score and Decision

**Calibration Report:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|-----------|
| xJ5CF1aOOX | 2.50 | 1 (weak) | Much weaker — single-task classification pre-training |
| xFvHcgj1fO | 3.00 | 1 (weak) | Much weaker — online ML for AD only |
| qZz7PKt4bE | 3.00 | 1 (weak) | Much weaker — LoRA tuning pipeline |
| XhdckVyXKg | 3.00 | 1 (weak) | Much weaker — wearable sensing only |
| jC6E2iTgfr (NuwaTS) | 4.00 | 1 (mid) | Weaker — imputation only, PLM-based |
| KJ1w6MzVZw | 3.80 | 1 (mid) | Weaker — pre-trained, limited task coverage |
| ZkEsEFFUyo | 4.33 | 1 (mid) | Weaker — CloudOps forecasting only |
| tdttNKCtyB (ROSE) | 5.75 | 2 (mid) | Similar complexity, fewer tasks, comparable weaknesses — TSPulse is stronger |
| rGdEM131Ht | 5.60 | 2 (mid) | Weaker — generative, fewer tasks |
| NPSZ7V1CCY | 6.25 | 2 (mid) | Comparable — zero-shot imputation for dynamical systems |
| aKcd7ImG5e (DADA) | 6.00 | 1&2 (mid) | Less broad — AD only. TSPulse is stronger in breadth and empirical scope |
| 4NhMhElWqP (DAM) | 7.00 | 2 (mid) | Different — forecasting-only foundation model. Similar overall quality |
| oANkBaVci5 | 6.75 | 2 (mid) | Not directly comparable — simple forecasting baseline |
| Unb5CVPtae (Time-LLM) | 7.00 | 2 (mid) | Different paradigm — LLM reprogramming |
| e1wDDFmlVu (Time-MoE) | 7.33 | 2 (mid) | Billion-scale, different league — not comparable |
| bWcnvZ3qMb (FITS) | 8.00 | 1 (strong) | Simpler, more elegant, but only 2 tasks. TSPulse is less elegant but broader |
| 1CLzLXSFNn (TimeMixer++) | 8.00 | 1 (strong) | More comprehensive but not pre-trained — different contribution type |

**Round 1 bracket:** 5.5 – 7.5. **Round 2 narrowing:** Compared against DADA (6.0), ROSE (5.75), DAM (7.0), Time-LLM (7.0). TSPulse is clearly stronger than DADA and ROSE, comparable to DAM in overall value but with a different profile (more tasks, more framing issues). **Final score anchored at 6.5.**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>