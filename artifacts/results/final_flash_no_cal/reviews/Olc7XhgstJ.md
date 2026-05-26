## Summary

This paper introduces Steady Thought (ST), a framework that mitigates "under-thinking" (excessive, unproductive thought switching) in Large Reasoning Models. ST operates in three stages: (1) segmenting responses into thoughts via entropy-based detection, (2) generating committed continuations for each thought through logit suppression, and (3) performing thought-level preference optimization (STPO) that teaches the model to prefer completing a promising thought over switching away from it. Experiments across three model scales (1.5B, 8B, 14B) and four benchmarks (MATH-500, AIME 2024, GSM8K, LiveCode) show that ST reduces output length by up to 39.3% while improving accuracy by up to 5.3%, and generalizes to out-of-distribution code tasks.

---

## Strengths

1. **Novel and well-motivated thought-level preference optimization framework.** Unlike prior methods that globally suppress switching (NoThink, NOWAIT, SEAL), ST operates at the granularity of individual thoughts, constructing preference pairs from committed continuations. The three-stage pipeline (segmentation → completion → optimization) is cleanly designed and each stage is justified by a clear intuition. The STPO loss (Eq. 7) instantiates this by conditioning on the specific thought prefix, providing more targeted supervision than response-level methods.

2. **Consistent gains across diverse architectures and out-of-distribution settings.** Table 1 shows that ST improves both accuracy and token efficiency across DeepSeek-R1-Distill-Qwen-1.5B, Qwen3-8B, and DeepSeek-R1-Distill-Qwen-14B on all four benchmarks. The gains on LiveCode (an OOD code benchmark, trained only on math data) are particularly telling — e.g., Qwen3-8B improves by +5.3% while cutting tokens by 19.0% — suggesting the method learns a generalizable reasoning discipline rather than dataset-specific memorization.

3. **Mechanistic analysis corroborates the intended behavior.** Table 2 shows that the proportion of correct intermediate thoughts (PCT) drops consistently after ST (e.g., DeepSeek-1.5B on MATH-500: 54.90% → 40.40%), directly confirming that the model abandons fewer correct reasoning paths. Figure 2 further shows that in most configurations the number of thoughts decreases and the proportion of the final thought increases, consistent with more committed reasoning.

4. **STPO outperforms SFT and DPO in ablation.** Table 4 demonstrates that STPO yields better accuracy (84.4% vs. 80.4% SFT, 82.6% DPO on MATH-500) while maintaining low token usage, and the paper correctly explains why (SFT encourages memorization, DPO suffers from length bias, STPO's length-normalized thought-level objective avoids both).

---

## Weaknesses

### Fatal
None.

### Major

1. **Missing comparison against whole-response SimPO baseline.** The ablation in Table 4 compares STPO against SFT and DPO, but not against SimPO applied to whole responses. Since STPO's loss function is directly inspired by SimPO's length-normalized objective (Eq. 7 builds on Eq. 3), the cleanest ablation isolating the benefit of *thought-level* conditioning is to contrast STPO (conditioned on Q and T_i) with whole-response SimPO (conditioned on Q alone) using the same preference data. Without this, it is unclear whether the gains come from the thought-level granularity or simply from replacing DPO's objective with SimPO's.

2. **Anomalous NOWAIT behavior on Qwen3-8B raises configuration concerns.** In Table 1, NOWAIT on Qwen3-8B increases tokens by **84.6%** overall and drops accuracy catastrophically (e.g., MATH-500: 91.4% → 61.0%; GSM8K: 95.6% → 73.3%). This is the opposite of what a suppression method should do, and the pattern is inconsistent with NOWAIT's behavior on other models (where it reduces tokens). This strongly suggests the baseline was not properly tuned for this model, which undermines the fairness of the comparison and leaves the reader wondering whether similar configuration issues affect other baselines.

### Minor

1. **Claim of preserved exploratory flexibility is only indirectly supported.** The paper states that ST does not harm the model's ability to explore alternative reasoning thoughts, but the evidence is indirect: (a) PCT reduction shows fewer *invalid* switches, not that the model can still make *necessary* switches, and (b) the increased thought count for DeepSeek-1.5B on AIME (12.87 → 18.21) is cited as evidence of flexibility, but this same data point shows the proportion of last thought *decreasing* (18.96% → 15.66%), which sits awkwardly with the narrative of deeper commitment. Accuracy improvements provide some indirect reassurance (if the model were over-committing to bad thoughts, accuracy would likely drop), but a direct analysis of appropriate abandonment behavior would substantially strengthen this central claim.

2. **No variance or confidence intervals reported.** The paper states it averages eight runs for AIME and two for LiveCode but reports only point estimates. For AIME 2024 (30 problems), a 3.7% absolute improvement (e.g., 62.1 → 65.8 for Qwen3-8B) represents roughly one additional correct problem, and without variance the reader cannot judge whether gains are reliable or due to noise. This is a common practice in LLM evaluation but remains a limitation.

3. **Training ablation limited to one model.** Table 4 compares SFT, DPO, and STPO only on DeepSeek-R1-Distill-Qwen-1.5B. Replicating this ablation on at least one more model (e.g., Qwen3-8B) would strengthen the conclusion that STPO is broadly preferable.

4. **Logit suppression mechanism underspecified.** Section 3.2 says trigger words' logits are "sharply decrease[d]" to drive probability "close to zero," but the exact suppression magnitude, the complete list of trigger words, and whether suppression is applied at every decoding step are not provided. This hinders exact reproducibility, though the high-level idea is clear.

### Trivial

- The formal "steadiness score" in Section 2.1 is a conceptual framing device that is not directly used in the loss or evaluation; it sets up the preference optimization view but could be streamlined.
- Token reduction is reported but no wall-clock latency measurements are given, so the practical speed benefit is only proxy-level.

---

## Nice-to-Haves

- Add a whole-response SimPO baseline to the main results or ablation table to isolate the effect of thought-level conditioning.
- Report standard deviations (or at least per-run ranges) for AIME 2024 and LiveCode results.
- Directly measure the model's ability to correctly abandon unpromising thoughts (e.g., by annotating whether a switch after a wrong thought is correct), to validate the preserved flexibility claim.
- Include wall-clock speedup measurements alongside token-count reductions.

---

## Removed Points

*These points were considered but removed during consolidation under the filtering rules. They are listed here for transparency and should be treated with caution.*

- **Missing training hyperparameters (learning rate, batch size, etc.):** Removed per the rule that parser-stripped appendix content is assumed to exist in the original submission. The paper references Appendix E for consumption details, and training hyperparameters are likely there.
- **Criticism that the entropy threshold was only tuned on one model and not discussed for transfer:** The paper explicitly states "We provide threshold tuning results on more models and datasets in the appendix D." Since the appendix is stripped, this concern is addressed in the original submission.
- **The formalism in Section 2.1 being disconnected from the method:** On re-reading, the formalism connects to the method via the instantiation of the steadiness score as log-probabilities and the use of preference optimization. The connection exists, though it is primarily motivational.
- **Strength Finder's generic claim about the problem being important:** This is generic and not specific to the paper's contributions.

---

## Novel Insights

The reviews surface two integrative observations that go beyond what the paper individually states. First, the paper's entropy-based thought segmentation and the thought-completion stage together create a form of *automated data augmentation* for preference pairs — the model generates its own "committed" continuations, which are then used as chosen trajectories. This self-supervision loop is an elegant property of the framework that the paper could foreground more explicitly. Second, the tension in the DeepSeek-1.5B/AIME results (more thoughts but shorter total length, lower proportion of last thought) suggests a failure mode worth investigating: for small models on very hard problems, ST may induce a "fragmented exploration" pattern where the model switches rapidly among many shallow thoughts rather than truly committing. Whether this is beneficial (as the paper argues) or a limitation of the approach for resource-constrained settings is an open question that would enrich the discussion.

---

## Suggestions

1. Add a whole-response SimPO baseline to the ablation (Table 4) to directly validate that thought-level conditioning provides additional value over the base preference optimization objective.
2. Investigate and explain the anomalous NOWAIT results on Qwen3-8B, and verify that all baselines use equally tuned hyperparameters.
3. Add a direct analysis of "appropriate switches" — e.g., measure whether ST reduces switches after *correct* thoughts but preserves or increases switches after *incorrect* ones — to rigorously support the preserved-flexibility claim.
4. Report per-run results or confidence intervals for AIME 2024 and LiveCode, or at minimum note the range across runs.

---

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>