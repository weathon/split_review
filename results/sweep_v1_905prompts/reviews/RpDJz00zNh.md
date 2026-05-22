## Summary

ConciseHint proposes a novel paradigm for improving reasoning efficiency in large reasoning models (LRMs): instead of encouraging conciseness *before* reasoning (via prompting or fine-tuning), it injects hints *during* the generation process. The method adaptively controls hint intensity based on current generation length (serving as a complexity proxy) and dynamically positions the hint injection to balance accuracy and computational cost. Experiments across Qwen3-4B/8B, DeepSeek-R1-14B, and three benchmarks (GSM8K, AIME24, GPQA-Diamond) show consistent token reductions of 30–65% with minimal accuracy loss. A trained variant (ConciseHint-T) further improves efficiency and provides controllable length through embedding interpolation.

---

## Strengths

- **Genuinely novel paradigm — in-reasoning intervention.** Prior work almost exclusively operates *before* reasoning (prompting, SFT, RL). Intervening *during* generation by injecting hints into the intermediate token stream is conceptually distinct and largely unexplored. The paper clearly articulates this distinction and provides concrete evidence that it works (e.g., Ours(Ori) on Qwen3-4B GSM8K: 2381→1213 tokens, −48.9%, accuracy preserved within 0.07%).

- **Complexity-adaptive interval is well-motivated and empirically validated.** The adaptive formula τ_k = α + β·l_k (Eq. 1) is simple and the ablation (Table 3) convincingly demonstrates that fixed high-intensity injection (interval=64) collapses accuracy on hard benchmarks (Qwen3-4B AIME24: 67.00%→45.33%) while the adaptive method preserves it. The evidence that easy and hard queries require different hint intensities is clear.

- **Dynamic injection position ablation is strong.** Table 4 shows that "at the tail" causes a severe accuracy drop (42.93% vs. 55.56%), "at the head" achieves good accuracy but requires 100% prefilling, and the dynamic position hits a sensible middle ground. This ablation cleanly justifies the design choice.

- **Seamless integration with existing methods.** ConciseHint consistently reduces token usage when combined with four different baselines (Prompt, BeConcise, Deer, NoWait) while staying within ~1% accuracy of each baseline on most settings. This plug-in compatibility meaningfully raises the efficiency upper bound (e.g., Ours(Deer) on Qwen3-4B GSM8K: 1405→841 tokens, −40%).

- **Evaluation across multiple state-of-the-art LRMs.** The paper tests on Qwen3-1.7B/4B/8B and DeepSeek-R1-14B — a broader model zoo than many comparable efficiency papers. Results are consistent across model scales.

---

## Weaknesses

### Major

1. **"Efficiency" claim lacks wall-clock time or overhead analysis.** Algorithm 1 makes sequential model calls (one per chunk of τ_k tokens). Even if each individual call is fast, the total wall-clock time depends on the number of sequential rounds and the overhead of re-prefixing after hint injection. The paper focuses exclusively on token usage as the efficiency metric and does not report latency, average number of injection steps per query, or wall-clock time on a standard hardware setup. Without this, a reader cannot assess whether the token reduction translates to actual speedup, especially when comparing against single-call baselines (Prompt, BeConcise) that avoid round-trip overhead entirely. The paper references Appendix A.2 for prefilling cost analysis, but the overhead of repeated inference calls (KV cache recomputation, context re-processing) is a separate concern that should be addressed in the main text.

2. **No statistical significance or variance reporting.** The paper runs 5–10 trials per setting and reports only point averages. Many accuracy differences are small (e.g., 94.74 vs. 94.60, or 95.51 vs. 95.65). Without standard deviations or confidence intervals, readers cannot assess whether the accuracy preservation (or small degradation) is real or within noise. This is a standard expectation for experimental papers and limits the reliability of the quantitative claims.

### Minor

3. **Training variant (ConciseHint-T) only evaluated on the smallest model.** ConciseHint-T results (Table 2) are limited to Qwen3-1.7B. The out-of-domain generalization claim is weak — on GPQA-Diamond, accuracy drops from 39.39 (Ori) to 37.37 (Ours) and further to 35.05 at γ=1. It is unclear whether the learned embeddings transfer to larger models or whether the accuracy-efficiency trade-off is acceptable in harder domains. The paper should honestly discuss this limitation.

4. **Key hyperparameters in the injection position formula are empirically chosen without sensitivity analysis.** The normalization constant 1024 and the cap 0.8 in Eq. (3) (p = τ_k · min((τ_k − α)/1024, 0.8)) are motivated by brief intuition but no sweep is shown. A sensitivity study across different cap values (e.g., 0.6, 0.7, 0.8, 0.9) on at least one large model/dataset would strengthen the design.

5. **The adaptive formula's reliance on current length as a complexity proxy is not empirically analyzed.** The paper asserts that easy queries "will complete in a short length" and that l_k would stay small under ConciseHint, but does not directly compare the dynamics of l_k across easy vs. hard queries. While not fatal (the method works empirically), this analysis would strengthen the theoretical grounding.

6. **Transition word analysis (Table 5) is shallow.** The observation that ConciseHint reduces transition words is a useful surface-level statistic, but it does not distinguish between "removing redundant self-reflections" and "suppressing all self-reflections including useful ones." A qualitative case study showing that the remaining self-reflections are of higher quality would significantly strengthen this analysis.

---

## Nice-to-Haves

- Compare against an alternative complexity proxy (e.g., a lightweight classifier on the input query) or an oracle that knows the dataset-level difficulty, to benchmark the length-based proxy.
- Report results for ConciseHint-T on larger models (Qwen3-8B, DeepSeek-R1-14B) to demonstrate scalability of the learned embeddings.
- A sweep of the cap parameter in Eq. (3) (e.g., 0.5–0.9) to justify the 0.8 choice beyond intuition.

---

## Removed Points

- **"Complexity-adaptive mechanism is circular"** (Harsh Critic's Critical Issue 1). The critic argued that since LRMs overthink on easy queries, the current length l_k would be large even for easy queries. This misreads the method: ConciseHint injects hints from the very first interval (α=128 tokens), so l_k reflects the *current length under the method's own guidance*, not the original model's length. The hints actively prevent easy-query length from growing. The paper's logic is sound. (Strawman weakness — REMOVED per hard rules.)

- **"Overstated claim of filling a blank"** about prior work. The paper correctly frames the before-reasoning vs. in-reasoning distinction and cites relevant prior work. The phrasing is standard for positioning. (Generic concern — REMOVED.)

- **"Missing baselines: ThinkLess, token-budget prompting"** — The paper already compares against 4 baselines plus combinations (8 method columns in Table 1). Coverage is thorough for the experiments conducted. (Scope creep — REMOVED per soft rules.)

- **"Formatting artifacts reduce readability"** (Figure 1). These are parser artifacts, not author errors. (REMOVED per hard rules.)

---

## Novel Insights

The key insight that emerges across the paper is that *in-reasoning* intervention creates a fundamentally different dynamic from pre-reasoning methods: the model can be steered toward conciseness *while it is in the middle of thinking*, not just at the start. This means the method can react to the model's current behavior rather than relying on a one-shot instruction. The adaptive interval mechanism (Eq. 1), while simple, exploits this dynamic property — it can afford to be aggressive early (when the query might be easy) and backs off naturally if the model continues generating (indicating a harder query). This self-correcting dynamic is qualitatively different from prompting or fine-tuning, which cannot adjust intensity mid-generation. The paper's demonstration that this approach works across 4 model scales and 3 difficulty levels, achieving 30–65% token reductions, makes a compelling case that in-reasoning intervention deserves more attention as a distinct paradigm.

---

## Suggestions

1. **Report latency / wall-clock time** for ConciseHint vs. baselines on a standard GPU setup, or at minimum the average number of injection steps per query. This is the single most impactful addition — without it, the "efficiency" claim is incomplete.

2. **Add standard deviations** to all tables reporting accuracy and token usage. The paper already runs multiple trials, so this is a presentation improvement, not an additional experiment.

3. **Analyze the dynamics of l_k** on easy vs. hard queries under ConciseHint — show empirically that easy queries stay short and thus maintain high hint intensity, vindicating the complexity proxy logic.

4. **Add a qualitative case study** (appendix-friendly) comparing the reasoning chains of ConciseHint vs. original, highlighting which transition words are removed and whether useful self-reflections are preserved.

---

## Score and Decision

**Round-1 bracketing:** Three queries on "efficient reasoning LLM token reduction" across score bands. Weak anchors (avg 2.5–3.4) — topic-mismatched, clearly weaker. Middle anchors (avg 5.0–6.67) — highly relevant papers on reasoning efficiency (Rational Metareasoning 5.00, CoTFormer 5.75, Skeleton-of-Thought 5.67, DOTS 6.25). Strong anchors (avg 8.0+) — exceptional papers on a different tier (theoretical analyses). **Bracket: [5.0, 7.0].**

**Round-2 narrowing:** Queried within (4.5, 6.5) and (6.0, 7.5) for reasoning-efficiency papers. Compared against: DOTS (6.25, accept) — ConciseHint has a more novel paradigm but less thorough OOD evaluation; comparable in quality. CoTFormer (5.75, accept) — ConciseHint is slightly stronger empirically (more models, direct results). Rational Metareasoning (5.00, reject) — ConciseHint has a clearly more novel approach and broader experiments. Hint Marginalization (5.75, reject) — ConciseHint is stronger. **Final score anchored between DOTS (6.25) and CoTFormer (5.75), closer to DOTS in novelty but pulled down by the missing latency analysis and standard deviations.**

**Score distribution rationale:** 6.0 is a solid accept. The paper introduces a genuinely novel paradigm (in-reasoning intervention) with consistent evidence across multiple models and benchmarks. The ablations are thorough. The main weaknesses — lack of latency/overhead analysis and missing standard deviations — are addressable and do not undermine the core contribution. The paper compares favorably to accepted papers at the 5.75–6.25 level in this domain.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>