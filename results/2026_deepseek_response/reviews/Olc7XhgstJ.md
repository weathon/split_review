Now let me produce the final, complete review.

## Summary

Steady Thought (ST) proposes a three-stage framework to mitigate "under-thinking" (excessive thought switching) in Large Reasoning Models: (1) entropy-based thought segmentation, (2) logit-suppressed thought completion to generate correct trajectories from segmented thoughts, and (3) a thought-level preference optimization objective (STPO) that trains the model to prefer committing to promising thoughts over switching. Experiments across three model sizes (1.5B, 8B, 14B) and four benchmarks (MATH-500, AIME 2024, GSM8K, LiveCode) show accuracy improvements up to 5.3% with token reductions up to 39.3%.

## Strengths

1. **Novel thought-level formulation of the under-thinking problem**: The paper formalizes under-thinking as a preference between commit and switch trajectories at the thought level (Section 2.1), and derives STPO (Eq. 7), a reference-free, length-normalized objective operating at the point of reasoning divergence. This is a genuine departure from token-level or representation-level global suppression methods (NoThink, NOWAIT, SEAL).

2. **Consistent accuracy gains with substantial token reduction**: Table 1 shows ST improves accuracy across all 12 model–dataset combinations (e.g., +3.12% average on Qwen3-8B, +1.9% on DeepSeek-R1-Distill-Qwen-1.5B, +2.52% on 14B) while reducing tokens by 17.3%–24.9%. These gains are consistent across model sizes and architectures.

3. **Direct behavioral evidence of reduced invalid switching**: Table 2 demonstrates that ST reduces the proportion of correct intermediate thoughts that are abandoned (invalid switches) — from 54.90% to 40.40% on MATH500 and 14.50% to 7.90% on AIME2024 for the 1.5B model. This directly links the method to the mechanism it targets.

4. **Ablation isolating the contribution of STPO**: Table 4 compares STPO against SFT and DPO on the exact same segmentation+completion pipeline. STPO achieves the best accuracy (84.4% vs 80.4% SFT, 82.6% DPO on MATH500) and competitive token reduction, showing that the thought-level preference optimization itself (not just shorter completions or standard DPO on this data) drives improvements.

5. **Generalization to out-of-distribution code reasoning**: ST improves accuracy on LiveCode (+5.3% for Qwen3-8B, +4.2% for 14B) despite training only on math data (omni-math), suggesting the method teaches a transferable reasoning pattern rather than dataset-specific memorization.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The selectivity claim is not tested with a targeted stress test**: The paper claims ST preserves exploration flexibility where global suppression methods (NOWAIT, SEAL) do not. While Figure 2 provides partial evidence (the 1.5B model increases the number of thoughts on AIME 2024 while improving accuracy, contradicting a "global suppression" account), the paper does not include a direct experiment on problems where the initially promising thought is a trap or dead end. Such a test would cleanly separate ST from a tuned global suppressor. The paper's core distinguishing claim — that ST is *selective* rather than a *global suppressor* — remains the least empirically supported part of the narrative.

2. **No statistical significance or variance reporting**: The paper averages 8 runs on AIME 2024 (30 problems) and 2 runs on LiveCode (400 problems) but reports no variance, confidence intervals, or significance tests. Given the small size of AIME (30 problems), some improvements (e.g., 1.5B model: 27.5% → 31.2%) could fall within noise. Standard deviations would substantially strengthen credibility.

3. **Entropy threshold tuning not clearly separated from test data**: Section 4.4.3 tunes the entropy threshold (2.8, 3.0, 3.2) and reports performance on MATH500 and AIME 2024, but does not clarify whether these datasets were held out during tuning. The paper only states the threshold was determined "through hyperparameter tuning" (Section 3.1). If tuning was performed on these test sets, the reported optimal threshold and corresponding results may not generalize.

4. **OOD gains vs in-distribution gains are not fully explained**: LiveCode improvements (+5.3% for Qwen3-8B, +4.2% for 14B) are larger in absolute terms than in-distribution MATH-500 gains (+3.0%, +0.6%). The paper attributes this to "teach[ing] the model a more precise pattern," but an alternative explanation is that lower base performance on LiveCode leaves more room for improvement from any regularization-like effect. Some discussion of this asymmetry would strengthen the analysis.

### Trivial
None.

## Nice-to-Haves

- A targeted experiment on problems requiring backtracking (where the first promising thought is a dead end) would directly test the selectivity claim over global suppression methods.
- Reporting the computational overhead of the thought completion stage (number of completions generated per training example, training time) would help practitioners assess practicality.
- Using an external verifier or human annotation for the thought quality metric (Table 2) would make this behavioral analysis more independent from the training pipeline.

## Removed Points

**1. "Thought Completion stage injects test-set supervision (FATAL)" — Removed.**  
The critic argued that using answer correctness from the thought completion process creates an information leak. This is incorrect: the training data (omni-math) and test data (MATH-500, AIME, GSM8K, LiveCode) are completely separate datasets. Using ground-truth answers on the *training set* to construct preference labels is standard practice in supervised preference optimization. No test-set information is used.

**2. "Preference optimization framing has theoretical tension / circularity" — Removed.**  
The critic argued that training on outcome-labeled thoughts is circular because the model doesn't know which thoughts are promising at inference time. This misunderstands preference optimization: the entire point is to use outcome labels available during training to teach better inference-time behavior — the same principle underlying all of RLHF, DPO, and SimPO.

**3. "Table 1 contradicts claimed motivation for Qwen3-8B" — Partially merged into Minor weakness #1.**  
The critic argued the gap between SEAL and ST on Qwen3-8B (0.77pp) is too small. But the paper provides counterevidence (Figure 2, 1.5B on AIME) showing ST increases thoughts while improving accuracy, contradicting a "global suppression" explanation. The critic's request for a targeted flexibility test is valid but is a minor concern, not a contradiction.

**4. "NOWAIT-like mechanism criticism" — Removed.**  
The critic noted that the thought completion stage uses logit suppression (same mechanism as NOWAIT) but only during training. This is an intentional design choice described in the paper — using suppression as a data construction tool rather than at inference — and is not a weakness.

**5. "Proportion of correct thoughts metric is circular" — Partially merged into Nice-to-Haves.**  
The accuracy benchmarks (Table 1) are fully independent of the training pipeline, so there is no circularity at the core evaluation level. The concern applies only to the behavioral analysis metric (Table 2), which shares methodology with training data construction; using an external verifier would strengthen this analysis.

**6. "Reproducibility concern about unspecified sampling procedure" — Removed.**  
The paper describes the training data source (omni-math, Section 4.1) and inference procedure. The parser stripped the Appendix, which likely contains further implementation details. The level of detail provided is standard for a conference paper.

## Novel Insights

None beyond the paper's own contributions. The combination of (a) entropy-based segmentation to isolate thought boundaries, (b) using logit suppression as a data construction tool rather than an inference intervention, and (c) a SimPO-derived conditional preference objective operating at the thought level — constitutes the paper's genuine methodological contribution.

## Suggestions

1. Report standard deviations or confidence intervals for the key results in Table 1, particularly for AIME 2024 given the small test set size (30 problems).
2. Clarify whether the entropy threshold was tuned on a held-out validation set or on the test sets, and adjust the experimental narrative accordingly.
3. Design a small-scale diagnostic experiment on problems where the initial promising thought is a dead end, to directly test the selectivity claim over global suppression methods.
4. Discuss the LiveCode vs. MATH-500 improvement asymmetry in more detail.

---

**Calibration Anchors Consulted:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| EVZnnhtMNX.md | 3.00 | R1 (weak) | Much weaker — rejected alignment variant with flawed evaluation |
| 28TLorTMnP.md | 2.50 | R1 | Much weaker — rejected listwise preference method |
| aYYZBPoSHb.md | 3.40 | R1 | Much weaker — rejected multi-objective alignment |
| fTdhM7q1o2.md | 3.00 | R1 | Much weaker — rejected preference modeling variant |
| IlQxeKrWDt.md | 5.50 | R1 (mid) | Similar tier but mixed reviews; this paper has cleaner evidence |
| SBoRhRCzM3.md | 6.67 | R1 (mid) | Similar tier; accepted prompting method; this paper's training-based contribution is more substantive |
| L9j8exYGUJ.md | 5.00 | R1 (mid) | Weaker — rejected analysis paper |
| ElYRG3pJcv.md | 4.25 | R1 (mid) | Weaker — rejected reasoning method with weak baselines |
| OfjIlbelrT.md | 8.00 | R1 (strong) | Stronger — mature efficiency paper with thorough evaluation |
| f4gF6AIHRy.md | 8.00 | R1 (strong) | Stronger — systematic data selection paper |
| 07yvxWDSla.md | 8.00 | R1 (strong) | Stronger — comprehensive synthetic data paper |
| xoXn62FzD0.md | 8.00 | R1 (strong) | Stronger — controlled generation with rigorous evaluation |
| O0sQ9CPzai.md | 6.33 | R2 | Similar tier; TPO addresses related problem (preference optimization for reasoning) with comparable rigor |
| VIUisLx8lQ.md | 6.00 | R2 | Similar tier; TypedThinker has comparable evaluation breadth but mixed reviews |
| 8QkpCRio53.md | 5.75 | R2 | Slightly weaker — rejected CO preference optimization |
| xS4XOS4NQ5.md | 5.00 | R2 | Weaker — rejected preference modeling |
| Tigr1kMDZy.md | 7.33 | R2 | Stronger — LM analysis paper with deeper investigation |

**Bracketing:** Round 1 placed the paper firmly in the middle band (3.5–7.5), well above the weak anchors (~3.0) and clearly below the strong anchors (~8.0). **Narrowing:** Round 2 positioned it alongside TPO (6.33, Accept) and TypedThinker (6.00, Accept) — papers with similar methodological ambition, evaluation breadth, and reviewer reception. The paper's novel thought-level formulation, consistent multi-model results, and clean ablations (especially Table 4) warrant a score at the upper end of this cluster.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>