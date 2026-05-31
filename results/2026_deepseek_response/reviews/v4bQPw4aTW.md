Now I have all the calibration I need. Let me write the final review.

## Summary

AdaBoN proposes a two-stage, prompt-adaptive allocation strategy for Best-of-N alignment: first explore each prompt with a fixed budget \(d\) to estimate reward distributions (via Gaussian KDE with Scott's rule), then greedily allocate the remaining budget based on estimated marginal gains. The method is model-agnostic, requires no auxiliary training, and needs only two sequential rounds of LM calls. Experiments across 12 LM–RM pairs, 3 datasets, and 50 batches show consistent BWR > 0.50 against uniform allocation, with EST values equivalent to ~20% larger budgets.

## Strengths

- **Model-agnostic and no auxiliary training required.** Unlike Damani et al. (2024), which requires training an MLP for each LM–RM pair and each budget level, AdaBoN works out-of-the-box for any LM–RM combination using only test-time sampling and KDE estimation. (Section 3, Algorithm 2, Section 1.1)

- **Consistent empirical outperformance of uniform allocation.** Across 12 LM–RM pairs and 50 batches per pair, AdaBoN achieves BWR > 0.50 for 76–100% of batches (Table 2b). Qwen-Mistral achieves 100% win rate, and individual batches reach BWRs of 0.70. (Section 4.3, Table 2b, Figure 2a)

- **Competitive against ~20% larger inference budgets.** EST values of 148–153 (Table 2a) show that AdaBoN with B=120 matches uniform allocation with B≈145–155, demonstrating real computational savings. (Section 4.3, Table 2a)

- **Performance improves with batch size.** Average BWR increases monotonically with K ∈ {3, 5, 10, 15, 20} for all LM–RM pairs, with gains up to 0.15 (e.g., Qwen-Mistral). (Figure 3, Section 4.3)

- **Extensive evaluation across diverse models and datasets.** The study covers 4 LMs × 3 RMs = 12 LM–RM pairs, 3 datasets (AlpacaEval, HH-RLHF, PKU-SafeRLHF), and 50 distinct batches — significantly broader than prior work (Damani et al. evaluates a single LM, RM, and batch). (Section 4.1)

## Weaknesses

### Major

- **No comparison against any adaptive baseline.** The paper's central claim is that AdaBoN's *specific* adaptive allocation is valuable, but the only baseline is uniform (non-adaptive) allocation. The authors explain why reproducing Damani et al. (2024) is prohibitively expensive (Section 4.2), but they do not implement even simple adaptive heuristics — e.g., explore-then-allocate-to-best (allocate remaining budget to the prompt with the highest observed max reward after exploration), or explore-then-allocate-by-variance. Such baselines would take at most a few lines of code and would directly demonstrate whether AdaBoN's KDE-based greedy allocation improves over obvious alternatives. Without them, the experiments only establish that *some* adaptivity helps, not that AdaBoN is a good adaptive strategy relative to plausible alternatives.

### Minor

- **The degree of adaptivity is limited.** With the default exploration budget \(d = 0.75B\), only 25% of the total budget is allocated adaptively. For \(B=120, K=5\), that is 450 out of 600 samples spent uniformly in exploration and only 150 reallocated. The paper tunes \(d\) only over the narrow range \([0.60B, 0.80B]\) and does not report results for smaller \(d\) values (e.g., \(0.3B, 0.5B\)) in the main text. Results at smaller \(d\) would clarify whether the adaptive allocation itself drives the gains or the large exploration phase does most of the work. (Section 4.3, Appendix G.1)

- **No reporting of reward magnitude differences.** The paper reports win rates (BWR) and survival times (EST) but not the raw difference in cumulative max reward or normalized reward margins. Since the improvements are modest (median BWR ~0.58), reporting effect sizes would help calibrate practical significance. The authors argue that absolute reward values are incomparable across prompts (Section 4.2), but they could report the average per-batch difference in normalized cumulative max reward.

- **Latency claim in the abstract is unqualified.** The abstract states AdaBoN "minimizes latency." The paper body clarifies that it minimizes sequential rounds (two calls), which is a real benefit. However, the per-round depth could be higher than uniform allocation (max sequential depth of ~150 for AdaBoN vs. 120 for uniform in the reported setting). The abstract should qualify that the advantage is in sequential rounds, not total compute. (Abstract, Section 3)

- **Decoding strategy not fully specified.** The paper states it "use[s] the standard generation function from Hugging Face, and thus use[s] the default decoding strategy for all LMs." Default strategies vary across models (greedy, temperature sampling, top-p, etc.), which should be explicitly documented for reproducibility. (Section 4.3)

### Trivial

- KDE bandwidth sensitivity and comparisons with alternative distribution estimators (Gaussian MLE, Skew-Normal MLE) are relegated to the appendix; a brief summary in the main text would improve self-containedness.

## Nice-to-Haves

- Compare against simple adaptive heuristics (e.g., explore-then-allocate-to-best, explore-then-allocate-by-variance) to demonstrate that AdaBoN's specific allocation is better than obvious alternatives.
- Include results for smaller exploration budgets (e.g., \(d = 0.3B, 0.5B\)) in the main text to clarify the source of gains.
- Report the average difference in normalized cumulative max reward alongside win rates.
- Document Hugging Face generation parameters (temperature, top-p, etc.) for each LM.

## Removed Points

These points were flagged for removal but may contain useful context; treat with caution.

1. **"The appendix is said to contain ablation on d, but that material is not available to the reviewer"** — Removed per rule: appendix content is stripped by the parser and exists in the original submission.
2. **"The paper should discuss how sensitive the results are to the choice of KDE bandwidth"** — The paper *does* discuss this: it tried Gaussian MLE and Skew-Normal MLE and found KDE performed best (Section 3.1, Appendix K.3). The concern is partially addressed.
3. **Criticisms based on missing appendix content, missing proofs, or absent references** — Removed per rule about stripped appendices.
4. **"No discussion of runtime or compute cost of the Monte Carlo estimation of V_{i,j}"** — While this is a reasonable point, the paper notes this estimation "does not exhaust our total budget BK as we no longer need to query the base LM" (Section 3), which partially addresses it.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add at least two simple adaptive baselines** (e.g., explore-then-allocate-to-best, explore-then-allocate-by-variance) to demonstrate AdaBoN's allocation is genuinely superior to obvious heuristics. This is the single highest-leverage improvement.
2. **Include results for smaller exploration budgets** (e.g., \(d = 0.3B, 0.5B\)) in the main text to clarify whether the adaptive allocation itself or the large exploration phase drives performance.
3. **Report reward magnitude differences** (e.g., normalized cumulative max reward difference) alongside win rates to let readers gauge effect sizes.
4. **Qualify the latency claim** in the abstract to clarify it refers to sequential rounds, not total compute.
5. **Explicitly document** the Hugging Face generation parameters (temperature, top-p, etc.) for each LM.

## Score and Decision

**Calibration anchors:**  
All anchors from `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/`.

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| BjZP3fTlVg.md | 3.00 | R1 (low) | Weak paper with unclear contributions; AdaBoN substantially stronger |
| n7iwmPacDt.md | 3.00 | R1 (low) | Weak paper with unclear contributions; AdaBoN substantially stronger |
| V4Xs283LHH.md | 2.50 | R1 (low) | Weak paper; AdaBoN stronger |
| ulGwcj1egv.md | 3.00 | R1 (low) | Weak paper; AdaBoN stronger |
| **6qUUgw9bAZ.md (Damani et al.)** | **6.50** | **R1 (mid), R2** | Most similar paper, addresses same problem. Damani et al. has a more novel learned predictor approach and evaluates against adaptive baselines. AdaBoN has broader evaluation (12 vs 1 LM–RM pair) but weaker baseline comparison. **AdaBoN is slightly weaker.** |
| **77gQUdQhE7.md (Inference-Aware FT)** | **5.67** | **R1 (mid), R2** | Inference-aware fine-tuning for BoN. Methodologically different but related. Much narrower evaluation (1 model, 1 dataset). **AdaBoN is slightly stronger.** |
| **0xUEBQV54B.md (Large Language Monkeys)** | **5.00** | **R1 (mid), R2** | Scaling inference compute via repeated sampling. Novelty concerns (considered somewhat obvious). AdaBoN has a more specific algorithmic contribution. **AdaBoN is stronger.** |
| **xOtOfdbBqK.md (Speculative Decoding adapter)** | **5.75** | **R2** | On-the-fly adaptation for speculative decoding. Similar weakness: missing baselines, marginal improvements. AdaBoN has more thorough evaluation. **AdaBoN is comparable to slightly stronger.** |
| **J0qTpmbSbh.md (GenARM)** | **6.50** | **R2** | Test-time alignment with autoregressive RM. Stronger theoretical grounding, cleaner narrative, broader experiments. **AdaBoN is weaker.** |
| OfjIlbelrT.md | 8.00 | R1 (high) | Highly innovative sparse attention mechanism; far stronger than AdaBoN |
| xoXn62FzD0.md | 8.00 | R1 (high) | SMC for controlled generation; far stronger than AdaBoN |

**Round 1 bracket:** [4.5, 6.5]  
**Round 2 narrowing:** Compared against anchors at 5.00 (weaker), 5.67 (slightly weaker but accepted), 5.75 (comparable), 6.50 (stronger). AdaBoN sits between 5.5 and 6.0 — it has broader evaluation than the 5.67 anchor and a cleaner method than the 5.75 anchor, but the missing adaptive baselines is a real gap that prevents it from reaching the 6.0–6.5 range occupied by Damani et al. and GenARM.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>