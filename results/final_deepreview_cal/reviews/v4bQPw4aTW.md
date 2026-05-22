Now let me write the full consolidated review.

---

## Summary

This paper proposes AdaBoN, a two-stage adaptive Best-of-N alignment method that allocates a fixed inference budget across a batch of prompts. In the first stage, a small exploration budget (d samples per prompt) is used to estimate each prompt's reward distribution via Gaussian KDE. In the second stage, the remaining budget is greedily allocated across prompts based on the estimated marginal gains. The method is test-time only, model-agnostic, and requires no auxiliary training. Experiments across 12 LM-RM pairs on AlpacaEval (with HH-RLHF and PKU-SafeRLHF results in the appendix) show that AdaBoN consistently outperforms uniform allocation with the same total budget, achieving median BWRs of 0.54–0.62 and ESTs of ~148–153 (competitive with uniform allocations using 20–33% larger budgets).

---

## Strengths

- **Consistent empirical gains across diverse settings.** Tables 1 and 2b show that AdaBoN achieves median BWR > 0.50 for all 12 LM-RM pairs on AlpacaEval (K=5, B=120), with 75–100% of 50 batches beating the uniform baseline. The Qwen-Mistral pair reaches 100% of batches above 0.50. This breadth of evaluation (4 LMs × 3 RMs, 50 batches each) is a genuine strength compared to prior work, which typically covers fewer configurations.

- **Clean, practical two-stage design with no auxiliary training.** AdaBoN requires only two sequential rounds of parallelizable LM calls (exploration then allocation) and works with any LM-RM pair out of the box. The greedy allocation algorithm (Algorithm 1) is justified by Proposition 3.1 (concavity of the expected-max function), and the Monte Carlo estimation from the K density does not consume additional inference budget. This contrasts favorably with Damani et al. (2024), which requires training separate MLPs for each LM-RM pair and budget setting.

- **New evaluation metrics (BWR and EST) that are well-motivated for the problem.** The paper carefully defines BWR (Eq. 3) and EST (Eq. 5) to measure adaptive-allocation performance in a setting where RM scores are only meaningful comparatively. The EST metric in particular (Table 2a, Figure 2b) provides an interpretable measure of computational savings — showing that AdaBoN with B=120 is competitive with uniform budgets of 148–153, a 23–28% effective savings.

- **Performance scaling with batch size.** Figure 3 and Table 14 (Appendix K.2) show that average BWR increases with K ∈ {3,5,10,15,20}, and for Mistral-LM the win rate reaches 100% of batches at K=20. This supports the paper's claimed relevance for small-batch settings.

- **Theoretical grounding for the greedy allocation.** Proposition 3.1 proves concavity and monotonicity of the expected-max function for any distribution with finite first moment, providing formal justification for the greedy algorithm.

---

## Weaknesses

### Fatal

None.

### Major

- **Missing ablation to isolate the adaptive mechanism.** AdaBoN uses 75% of the total budget (d = 0.75B) for exploration — generating samples that are then used *both* for distribution estimation and as part of each prompt's final Best-of-N set. This means the exploration phase already injects substantial non-uniformity across prompts (due to random sampling). The paper does not compare against a baseline that uses the same exploration phase but then allocates the remaining (B−d)K budget *uniformly* across prompts. Without this control, it is unclear whether the reported BWR gains are driven by the adaptive allocation rule or by the randomness of the exploration samples themselves. This is the single most important missing experiment.

- **No empirical comparison to the most directly related prior work (Damani et al., 2024).** The paper acknowledges that Damani et al. addresses the identical allocation problem and discusses qualitative differences (Section 1.1), but provides no empirical comparison. The stated reasons — lack of available implementation and computational cost of training 216K MLPs — are partially understandable, but the paper's central claim is that AdaBoN offers a practical alternative. Some controlled comparison, even on a reduced scale (e.g., a single LM-RM pair, one budget value, one batch size where Damani's method can be approximated or their reported results used as a reference), would substantially strengthen the contribution. Without it, the paper reads as an alternative approach whose relative merits are unquantified.

- **Coarseness of the hyperparameter tuning for the exploration budget d.** The exploration budget d is tuned over only four values: {0.60B, 0.70B, 0.75B, 0.80B}. The paper claims that d=0.75B incurs only a "minimal drop" relative to the optimal, but this conclusion is drawn from a very small grid. The chosen range (60–80% of B) also means that the remaining adaptive budget is at most 40% of B, further emphasizing the need for the ablation described above.

### Minor

- **BWR as primary metric vs. the optimization objective.** The method optimizes expected cumulative maximum reward (Eq. 1), while the primary evaluation metric is BWR — a pairwise win probability against uniform. The paper's justification (RM scores are only meaningful comparatively) is valid, but reporting only the win rate rather than the actual distribution or effect size of the optimized objective means the reader cannot assess how much AdaBoN improves the quantity it is designed to maximize. The EST metric partially addresses this, but reporting the raw distribution of \(\sum_i \max_j R_{i,j}\) for AdaBoN vs. uniform would be more direct.

- **The "latency" claim is slightly overstated.** The paper states that AdaBoN "minimizes latency" because it requires only "two calls to the base LM." In practice, each of these "calls" involves generating d (exploration) or up to (B−d)K (allocation) samples in parallel. While parallelization is possible, the wall-clock latency is determined by the longest single generation, and the paper does not report actual latency measurements. The claim is not false — the two-stage design does reduce sequential round-trips — but the phrasing could mislead readers about practical speedups.

- **EST truncation at 2B.** The paper caps the EST sum (Eq. 5) at 2B for computational reasons (Section 4.3). This introduces a negative bias for prompts that could survive longer in expectation. The authors should discuss how frequently this cap binds and whether a larger cap (e.g., 3B or 4B) would materially change any qualitative conclusions.

### Trivial

- Figure 1's caption describes three histograms but the paper's description is adequate. (Minor presentation issue, not affecting evaluation.)

---

## Nice-to-Haves

- A comparison against an "exploration + uniform remainder" baseline as described in the Major weaknesses section.
- Reporting the mean and distribution of \(\sum_i \max_j R_{i,j}\) directly (not just BWR/EST) to validate the optimization objective.
- A limited-scale comparison with Damani et al. (2024), even on a single LM-RM pair, budget value, and batch size.
- Reporting the computational overhead of KDE and Monte Carlo estimation steps (Line 2–3 of Algorithm 2) to support the "practical" claim.

---

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Figure captions reference 'Medical, Math, ArXiv' datasets not used in the paper"** — The extracted text shows duplicate figure descriptions. The image alt-text (which mentions Medical/Math/ArXiv) appears alongside the paper's actual text captions (which correctly reference AlpacaEval datasets on lines 439–440 and 444–445). Based on the paper structure, this is a PDF extraction artifact where text rendered inside figure images was transcribed as duplicate captions. The paper's own caption text is consistent with the experimental setup.

- **"No justification for KDE beyond visual inspection"** — The paper explicitly states in Section 3.1 that they also tried Gaussian and Skew-Normal MLE fits and reports in Appendix K.3 (Table 16) that KDE outperforms these alternatives across most LM-RM pairs. While the appendix is stripped in the extracted version, the claim is made in the paper and the comparison exists.

- **"Default decoding strategy unspecified"** — The paper states in Section 4.3: "we use the standard generation function from Hugging Face... and thus use the default decoding strategy for all LMs." This is transparent and reproducible.

- **Damani et al. comparison is a "fatal" omission** — The paper provides explicit reasoning for the absence of comparison (no public implementation, prohibitive training cost), and positions itself in a complementary regime (small K, large B). While the absence weakens the paper, it does not invalidate the core finding that AdaBoN outperforms uniform allocation.

---

## Novel Insights

None beyond the paper's own contributions. The key insight — that per-prompt reward distributions are smooth enough to be estimated via simple KDE with small sample budgets, enabling effective greedy allocation — is well articulated. The observation that performance improves with batch size (K) is a useful practical property that could inform deployment decisions.

---

## Suggestions

1. **Add the ablation control**: Run AdaBoN with identical exploration (d=0.75B) but allocate the remaining budget uniformly across prompts. Compare BWR distributions to the full AdaBoN to isolate the benefit of adaptive allocation.
2. **Attempt a reduced-scale comparison with Damani et al. (2024)**: Even a single LM-RM pair and budget value, using the authors' reported results as a reference or implementing a simplified version, would significantly strengthen the empirical positioning.
3. **Report the optimization objective directly**: Show the mean and distribution of \(\sum_i \max_j R_{i,j}\) for AdaBoN vs. uniform allocation across the 50 batches for at least one representative setting (e.g., Qwen-Mistral, K=5, B=120).
4. **Expand the d-hyperparameter grid** or provide a sensitivity curve rather than comparing only 4 values. Also check that the optimal d changes with B.

---

## Calibration Report

**Round 1 bracket**: [3.5, 7.5] — clearly above low-quality papers (scoring 2.5–3.5) and clearly below top-tier papers (scoring 8+).

**Round 2 narrowing**: Compared against the following anchors:

| Anchor ID | Avg Score | Round | Comparison to AdaBoN |
|-----------|-----------|-------|---------------------|
| 6qUUgw9bAZ (Damani et al.) | 6.50 | R1 middle | Most directly related work. AdaBoN has broader empirical evaluation (12 LM-RM pairs vs. limited) but Damani includes empirical comparisons AdaBoN omits. AdaBoN is slightly weaker overall. |
| 77gQUdQhE7 (BoN-Aware Fine-Tuning) | 5.67 | R1 middle & R2 | Similarly scoped BoN paper. AdaBoN has broader evaluation and cleaner problem framing. Comparable quality. |
| 8HQS1X2AK4 (Test-Time Alignment via HyRe) | 5.33 | R2 | Had missing baselines and justification gaps similar to AdaBoN's gaps. AdaBoN's evaluation is broader and cleaner. AdaBoN is slightly stronger. |
| Yz7ts36V7A (Backoff Decoding) | 3.67 | R1 middle | Had overlapping content concerns and limited evaluation. AdaBoN is clearly stronger. |
| 1Uem0nAWK0 (Inference-time LLM Alignment) | 4.25 | R1 middle | Had novelty and comparison concerns. AdaBoN is stronger. |

AdaBoon sits between anchors scoring 5.33 and 5.67 in the round 2 set — weaker than Damani (6.50) but stronger than the rejected papers in the 3.5–5.3 range. The missing ablation and missing comparison to Damani prevent it from reaching the 6+ level, while its broad evaluation and clean results put it clearly above papers scoring ≤5.3.

**Final score**: 5.5

---

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>