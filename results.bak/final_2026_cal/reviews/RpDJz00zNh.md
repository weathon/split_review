Here is the consolidated review.

---

## Summary

ConciseHint proposes an "in-reasoning intervention" paradigm for making large reasoning models (LRMs) more concise. Unlike prior work that adds control prompts before generation or fine-tunes the model offline, ConciseHint injects hints ("make answer concise!") *during* token generation at adaptively determined intervals. The injection interval grows with reasoning length (Equation 1), automatically reducing hint intensity for complex queries. The paper evaluates on GSM8K, AIME24, and GPQA-Diamond across Qwen3-4B/8B and DeepSeek-R1-14B, showing token reductions of 27–49% on GSM8K, 4–17% on AIME24, and 26–44% on GPQA-Diamond with accuracy largely preserved. A trained embedding variant (ConciseHint-T) using prompt-tuning-like SFT on concise data yields further gains, and the method is shown to combine additively with existing efficiency methods (prompting, early exit, no-wait).

---

## Strengths

- **Novel in-reasoning intervention paradigm, clearly differentiated from prior work.** The paper identifies and fills a genuine gap: all prior efficiency methods intervene *before* reasoning (prompting, SFT, RL), while ConciseHint intervenes *during* token generation. This framing is well-motivated and the distinction is crisp. The claim is supported by a direct comparison to prompting baselines (BeConcise, Prompt) where ConciseHint achieves lower token usage without accuracy loss — e.g., on Qwen3-4B GSM8K, Ours(Ori) uses 1213 tokens vs. Prompt's 1263 and BeConcise's 1597, at comparable accuracy.

- **Consistent and substantial token reductions across models and benchmarks while preserving accuracy.** Table 1 reports reductions of 27–49% on GSM8K, 4–17% on AIME24, and 26–44% on GPQA-Diamond across three model families, with accuracy changes within ±2% (often improving). For example, Qwen3-4B on GSM8K: 2381→1213 tokens (−49%) with accuracy 94.81→94.74. Accuracy *improves* on AIME24 for Qwen3-4B (64.33→66.67) and Qwen3-8B (64.67→67.33).

- **Complexity-adaptive injection interval prevents accuracy collapse on hard tasks.** The ablation (Table 3) is the strongest evidence: fixed interval 64 collapses AIME24 accuracy from 67.00→45.33 on Qwen3-4B, while the adaptive method maintains 67.00. On GSM8K (easy), the same fixed interval causes only minor loss (94.75→93.42). This validates the core design choice.

- **Seamless plug-and-play integration pushes existing methods further.** Table 1 shows ConciseHint consistently improves every baseline it is combined with (Prompt, Deer, NoWait). For Qwen3-4B GSM8K, Ours(Deer) reduces Deer's 1405→841 tokens (−40%); Ours(Prompt) reduces Prompt's 1263→839 (−34%). This compatibility is a practical strength not demonstrated by most competing methods.

- **Mechanistic analysis links token reduction to reduced self-reflection.** Table 5 shows transition words ("Wait", "Alternatively") drop by ~60–70% with ConciseHint while their average spacing stays stable, indicating the model removes unnecessary self-correction steps rather than simply compressing text.

---

## Weaknesses

### Major

None that threaten the core claims.

### Minor

- **The claim that "in-reasoning timing" is the causal factor is not experimentally isolated.** The paper frames in-reasoning intervention as the key novelty, but the experiments compare ConciseHint (injection during generation) to prompting baselines (injection before generation). This conflates timing with "dosage" — ConciseHint injects the hint multiple times, while baselines inject it once. A control where the hint text is repeated in the initial prompt (e.g., prepended 5×) would isolate whether the gains come from *timing* or simply from higher effective hint strength. The Prompt baseline (which already uses a complexity-adaptive instruction) partially mitigates this concern, but the core experimental validation of the "in-reasoning" framing per se is incomplete. The paper would be strengthened by acknowledging this and adding the control.

- **ConciseHint-T (trained embeddings) is underspecified.** The training description (Section 3, paragraph starting "ConciseHint-T") states that hint embeddings are injected at fixed intervals into concise responses and trained via SFT "like Prompt Tuning (Lester et al., 2021)." Critical details absent: (a) the number of embedding parameters and their position within the sequence (are they inserted as extra token positions in the embedding layer?); (b) how the gradient flows back through a frozen model to the embeddings; (c) whether training uses the same fixed interval for all samples and how that interval is chosen; (d) training hyperparameters (learning rate, steps, batch size). The Prompt Tuning reference provides a starting point, but adapting it to *injection at intervals within the sequence* rather than *prepending* is non-trivial and needs explicit specification.

- **No error bars or confidence intervals.** The paper reports that experiments are run multiple times (5 for GSM8K, 10 for others) and averages are reported, but no standard deviation or variance is reported. For small accuracy differences (e.g., Ours(Ori) vs. Ori on GPQA-Diamond DeepSeek-R1-14B: 54.65 vs. 56.06, a 1.41% drop), it is impossible to judge whether this is within noise. This is a standard reporting expectation for empirical papers in this area.

- **The computational cost of injection is discussed but not measured.** The paper acknowledges prefilling costs, provides prefilling ratios in Table 4, and refers to Section A.2 (stripped by the PDF parser) for analysis. However, no wall-clock latency, throughput, or FLOP measurements are reported. For an "efficient reasoning" paper, real efficiency in terms of time or compute is at least as relevant as token count. Without this, a scenario where token savings are partially or fully offset by prefilling overhead cannot be ruled out.

### Trivial

- Equation (3) uses the constants 1024 and 0.8 without empirical justification beyond "it works well." A brief sensitivity analysis would strengthen the presentation.
- The hyperparameters α=128 and β=0.2 are claimed to be "fixed across all experiments" but their sensitivity is relegated to the appendix.

---

## Nice-to-Haves

- A control experiment comparing (a) hint repeated in the initial prompt vs. (b) hint injected during generation at the same frequency would cleanly isolate whether timing matters beyond dosage.
- Measuring wall-clock latency or throughput (tokens/second) alongside token count would make the efficiency claims self-contained.
- Reporting standard deviations or confidence intervals for accuracy and token usage numbers would improve statistical rigor.
- Testing on larger models (e.g., Qwen3-32B, DeepSeek-R1-32B) would strengthen generality claims, though the current set (4B–14B) is already reasonable.
- A brief analysis of failure cases — queries where ConciseHint degrades accuracy — would provide deeper insight into the method's limitations.

---

## Removed Points

These points from the inputs were evaluated and removed with justification:

- **"Performance on hard benchmarks is unconvincing" (Harsh Critic):** The reviewer claimed results on AIME24 are "modest" (10% token reduction on Qwen3-4B). However, accuracy actually *improves* from 64.33→66.67 and token reduction is meaningful on a very hard benchmark. On DeepSeek-R1-14B (the largest model), drops of 2% on AIME24 (63.0→61.0) with 17% token reduction are a reasonable trade-off. The overstatement claim is a judgment, not a factual error, and the results are consistently positive.
  
- **"Missing comparison to more recent works" (Harsh Critic):** The paper compares against four representative baselines (BeConcise, Prompt, Deer, NoWait). Claiming missing comparisons to ThinkLess, Token-Budget-Aware, etc., without evidence that these are clearly stronger baselines is speculative scope creep.

- **"Limited domain coverage" (Harsh Critic):** The paper tests on math (GSM8K, AIME24) and science (GPQA-Diamond), with additional results in the appendix for CommonsenseQA and HumanEval. This is standard coverage for an efficient reasoning methods paper.

- **"The trained embedding mechanism is underspecified to the point of irreproducibility" (full-strength framing):** The description references Prompt Tuning (Lester et al., 2021), which defines a standard framework for injecting learnable continuous embeddings. While more detail would help, the combination of the algorithmic description + Prompt Tuning reference provides sufficient guidance for reproduction. Demoted to Minor.

---

## Novel Insights

**The complexity-adaptive injection interval (Equation 1) elegantly sidesteps a problem that training-based methods solve with expensive reward engineering.** Training-based conciseness methods (e.g., LASER, PALU) require careful reward design to balance conciseness and accuracy across query difficulties. ConciseHint's insight — that reasoning length is a usable online proxy for complexity, and that injecting hints less frequently as length grows naturally achieves this balance — is both simpler and more transparent. The ablation in Table 3 (fixed 64 interval causing 22-point accuracy drop on AIME24 but only 1-point drop on GSM8K) starkly validates why the adaptive mechanism is necessary. This suggests a general principle: for any intervention that trades off efficiency against accuracy, making the intervention intensity a function of the model's own behavior (here, generation length) can automatically calibrate to query difficulty without per-dataset tuning.

---

## Suggestions

1. Add a controlled experiment that compares repeated hint injection in the prompt vs. during generation to directly validate the "in-reasoning" timing claim.
2. Provide training details for ConciseHint-T (embedding dimension, insertion mechanism, learning rate, number of steps) and ideally release the trained embeddings.
3. Report standard deviations for all accuracy and token usage numbers.
4. Measure and report wall-clock latency or throughput to complement token counts.
5. Add a brief failure-case analysis section discussing queries where token reduction harms accuracy.

---

## Score and Decision

### Calibration Report

**Round 1 — Bracketing (3 queries):**
- Weak anchors (score < 3.5): "EPiC" (3.33), "LitePruner" (3.00), "Efficient Reasoning via Reward Model" (2.50), "Think Just Enough" (3.00). These papers had significant flaws or withdrawn status. ConciseHint is clearly stronger.
- Middle anchors (3.5–7.5): "Don't Overthink It" (4.40), "Concise Reasoning via Lagrangian" (5.00), "Concise Reasoning via RL" (4.40), "Early Stopping CoT" (4.00). These papers are directly in the same area. ConciseHint has stronger novelty and more comprehensive experiments.
- Strong anchors (>7.5): "Transducing Language Models" (8.00), "LLMs Get Lost In Multi-Turn" (8.00). These are fundamentally different contributions and not directly comparable.

**Round 1 bracket:** 5.0–6.5

**Round 2 — Narrowing (2 queries, score 5.0–7.5):**
- "A State-Transition Framework" (5.50, accept poster): Different approach (linear attention). Comparable quality; ConciseHint has cleaner method but narrower benchmark coverage.
- "DEER - Dynamic Early Exit" (5.33, accept poster): Most directly comparable (training-free, during-generation intervention). ConciseHint has stronger ablations and compatibility demonstration but less model coverage. Approximately equal quality.
- "LASER/LASER-D" (5.50, accept poster): RL-based approach with strong results. ConciseHint is simpler, training-free, and has clearer conceptual contribution.
- "CoT Vectors" (6.00, accept poster): Different domain. Not directly comparable.

**Comparison summary:** ConciseHint is comparable to or slightly stronger than DEER (5.33) and LASER (5.50), but has detailing issues that prevent it from reaching the 6+ tier.

**Final score:** 5.5

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>