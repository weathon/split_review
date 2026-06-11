Now I have a comprehensive calibration picture. Let me write the final review.

---

## Summary
This paper proposes High-Entropy Sum (HES), a training-free metric that sums the entropy of only the top 0.5% highest-entropy tokens in a reasoning sample, and demonstrates its use as a unified data selection signal across SFT, RFT, and RL training paradigms. The core intuition — that global entropy averaging dilutes the signal from critical "forking tokens" — is well-motivated, and the method is validated across a broad set of experimental configurations spanning two model families, three domains, and three training regimes.

## Strengths
- **Comprehensive cross-paradigm validation**: HES is validated across SFT (Tables 1–4), RFT (Table 5), and RL (Table 6) — three qualitatively different training regimes. In SFT, HES consistently outperforms random, difficulty, length, and four alternative entropy metrics across two models, two datasets, and three domains (Math, Code, STEM). In RFT, Highest-HES beats Random in all 10 per-query and global-pool settings.

- **Pruning-beyond-baseline result**: Training on the top 80% of data ranked by HES (discarding the bottom 20%) consistently outperforms training on the full dataset — e.g., 35.36% vs 32.61% (Table 1, Qwen3-8B), 32.35% vs 30.22% (Table 2, DeepSeek-R1-7B), replicated across Code and STEM domains (Tables 3–4). The Lowest-HES-20% control (14.90%, Table 1) confirms that low-HES samples actively harm training. This is counterintuitive and practically significant.

- **Small-to-large model transfer**: Using Qwen3-0.6B to compute HES for data selection for Qwen3-8B yields 32.12% average accuracy, comparable to the 8B model's self-selection at 31.14% (Table 1), while reducing inference cost by over an order of magnitude. This demonstrates practical utility for large-scale data curation.

- **Rigorous metric ablation**: The SFT design compares 12 configurations (Table 1), isolating each component: summing vs averaging (HES vs AvgHE), high-entropy-only vs all tokens (HES vs ES), and relative vs absolute thresholding (HES vs HES_absolute). HES_relative (31.14%) outperforms HES_absolute (30.11%), AvgHE (27.97%), and AvgE (27.40%).

- **RL negative-sampling insight**: Table 6 shows that curating negatives by HES degrades performance (Pos-High/Neg-Low: 19.50%) relative to random negatives (Pos-Rand/Neg-Rand: 19.88%), while curating positives by HES provides the best result (Pos-High/Neg-Rand: 21.30%). This asymmetric finding — HES is valuable for selecting challenging positives but random diversity is better for negatives — is non-obvious and practically useful.

- **Sensitivity analysis demonstrating robustness**: Section 4.4 and Figures 3–4 test the two key hyperparameters across domains, showing the top 0.5% percentile consistently yields best performance and the metric is not brittle to these choices.

## Weaknesses

### Fatal
None.

### Major
- **The model used to compute token entropy is not specified for the main experiments.** HES is computed from token-level probability distributions, which are inherently model-dependent. The paper specifies the entropy source only for the Figure 1 discriminative analysis (Qwen3-14B) and the proxy-model experiment (Qwen3-0.6B/1.7B). For the main SFT results (Tables 1–4, using Qwen3-8B-Base and DeepSeek-R1-Distilled-7B), the RFT experiments (Table 5), and the RL experiments (Table 6), which model's logits were used to compute HES is never stated. This affects reproducibility: different models produce different entropy values for the same token sequence, potentially leading to different HES rankings and selected subsets. The proxy-model transfer experiment (0.6B → 8B works well, Table 1) suggests some robustness across model scales, but the omission remains significant. This is addressable in rebuttal by simply stating the entropy source model for each experiment.

### Minor
- **Quality vs. complexity framing is inconsistent.** Figure 1 shows incorrect samples have substantially higher HES (normalized mean 0.68) than correct ones (0.29). So higher HES correlates with incorrectness globally, and HES-based selection only works when applied after filtering for correctness — which the paper in fact does across all paradigms. The paper acknowledges HES "quantifies the complexity of a reasoning path" (line 36) but also repeatedly calls it a "quality" metric and labels low-HES samples as "low-quality." The logical chain — HES measures complexity, and among correct samples, more complex reasoning provides richer training signal — is implicitly followed but should be made explicit to resolve the internal tension with Figure 1.

- **RL results have thin margins without variance estimates.** In Table 6, Pos-High/Neg-Rand achieves 21.30% vs Full-Batch at 20.63% (difference of 0.67 pp), with individual benchmark differences sometimes in the opposite direction (e.g., GPQA: 35.54 vs 36.71). No standard deviations or confidence intervals are reported. While this reporting level is common in the field, the paper's claim that HES "significantly surpasses" the full-batch baseline is not fully supported without statistical evidence.

### Trivial
- A paragraph in the RFT results section (beginning "HES shows robust performance in both Per-Query and Global Pool settings") is duplicated verbatim (lines 232–233 and 234–276).

## Nice-to-Haves
- The computational cost of computing per-token entropy at scale (running forward passes on 100K+ long-context samples) could be discussed, even briefly, to contextualize the "training-free" label.
- Clarifying how the "top 20%" selection interacts with problem-type coverage (e.g., does HES-based selection skew the distribution toward certain problem types?) would strengthen the analysis.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **Harsh Critic claimed Table 1 bolding is "incoherent"** — This is a parser formatting artifact; the original submission's bolding convention is standard (best per column). Removed per hard rules on formatting nitpicks.
- **Harsh Critic questioned the footnote about HES_relative superiority having only "a single row" of evidence** — The paper does provide direct experimental comparison (Table 1), and the footnote's claim is proportionate. Removed as overstatement.
- **Harsh Critic speculated about RL design concern regarding queries with few correct rollouts** — This is a speculative edge-case concern not demonstrated in the paper. Removed.
- **Strength Finder's generic framing strengths** — "This breadth of validation is unusual and compelling" was merged into the specific cross-paradigm strength rather than kept standalone.

## Novel Insights
Beyond the paper's own contributions, the reviews surface an important meta-point about the tension between "quality" and "complexity" in data selection metrics for reasoning. The paper's Figure 1 convincingly shows that HES is inversely correlated with correctness (incorrect samples have higher HES), yet HES works as a positive selection signal when applied within the correct-only subset. This pattern — a metric that is negatively correlated with a binary quality label but positively predictive of learning value conditional on correctness — represents a more nuanced understanding of what makes reasoning data valuable than simple "quality" heuristics. This insight generalizes beyond HES to how the field should think about training data valuation for reasoning.

## Suggestions
- Specify the entropy source model explicitly for every experiment (e.g., "For SFT, HES was computed using a single forward pass of Qwen3-8B-Base on each demonstration"). If different models were used across paradigms, explain why and discuss implications.
- Restructure the narrative to distinguish clearly between HES as a complexity metric and the quality-via-complexity selection strategy that applies it only to correct samples. This would resolve the tension between Figure 1 (incorrect samples have higher HES) and the selection methodology (select high-HES samples for training).
- Report per-benchmark standard deviations or at minimum an aggregate variance metric for the RL results, to better support claims of significant improvement.

## Calibration

### Round 1 — Bracketing
Initial bracket placed at **(5.5, 7.0)** based on comparison with:
- **"Rethinking Data Selection at Scale" (4.40, Reject)** — Found random selection hard to beat; current paper clearly stronger with HES consistently beating random.
- **"DELIFT" (6.00, Accept)** — Data selection across fine-tuning stages; comparable quality, current paper has broader paradigm coverage.
- **"What Makes Good Data for Alignment? / DEITA" (6.33, Accept)** — Well-executed data selection study; current paper comparable but with methodological underspecification.
- **"Smaller, Weaker, Yet Better" (7.00, Accept)** — Strong paper on compute-optimal sampling; current paper not at this level of polish.

### Round 2 — Narrowing
Within the bracket, further comparison with:
- **"3DS" (5.75, Reject)** — Narrower domain-specific case study; current paper is broader and stronger.
- **"DataMan" (6.00, Accept)** — Pre-training data quality tool; comparable quality level.
- **"DELIFT" (6.00, Accept)** — Re-confirmed as closest anchor; current paper has broader validation but less clear methodological specification.
- **"DEITA" (6.33, Accept)** — Slightly more polished than current paper; the unspecified entropy source in the current paper prevents it from reaching this tier.

### Final Score Determination
The current paper is clearly stronger than the 4.40 and 5.75 anchors, comparable to the 6.00 anchors (DELIFT, DataMan), but falls short of the 6.33 anchor (DEITA) due to the unspecified entropy source model and framing inconsistencies. The method is simple, effective, and validated impressively broadly; the weaknesses are real but addressable. **Score: 6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>