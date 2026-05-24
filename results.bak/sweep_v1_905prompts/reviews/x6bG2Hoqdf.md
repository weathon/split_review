Now let me write the final consolidated review.

## Summary

This paper introduces CALM, a framework for automatic heuristic design (AHD) that couples evolutionary prompt search with on-the-fly RL fine-tuning (GRPO) of a small quantized LLM. Unlike prior LLM-based AHD methods that keep the LLM frozen, CALM treats the heuristic generation process as a source of training data and uses it to adapt the model's parameters, thereby enabling "co-evolution" of the LLM and the heuristic search. Experiments across four challenging optimization problems (OBP, TSP, CVRP, OP) show that CALM, running on a single 24GB GPU with an INT4-quantized Qwen2.5-7B model, consistently outperforms API-based baselines relying on GPT-4o-mini.

## Strengths

1. **First joint optimization of prompt evolution and LLM adaptation for AHD.** The paper is the first to combine verbal guidance (evolutionary prompt manipulation) with numerical guidance (RL fine-tuning of the LLM) in a single framework. This is clearly stated and contrasted with all prior work that keeps the LLM static (Section 2).

2. **A local, quantized 7B model beats SOTA API-based methods.** Tables 1–3 show CALM (INT4 Qwen2.5-7B on a single 24GB GPU) achieves lower optimality gaps than all GPT-4o-mini baselines on OBP (avg 0.71% vs best baseline 0.89%), CVRP at all scales (e.g., N=200 gap 3.95% vs best baseline 4.70%), and OP at out-of-domain scales (N=200 gap 12.58% vs best baseline 15.97%). This is an impressive result that validates the core contribution.

3. **Ablation studies pinpoint the RL component as the primary driver.** Table 4 shows that disabling GRPO causes the largest performance drop across nearly all settings (OBP gap rises from 0.71% to 1.78%; OP from 17.41% to 19.89%), cleanly isolating the effect of RL fine-tuning from contributions of the verbal operators.

4. **Thorough and well-designed ablation suite.** Beyond the GRPO ablation, the paper tests alternative reward schemes, collapse mechanism hyperparameters, removal of each evolutionary operator, and crossover without diversity awareness. Each ablation is informative and supports a specific design choice (e.g., the diversity-aware crossover ablation confirms that performance-based crossover alone is worse than no crossover at all — an interesting finding noted in the paper).

5. **Out-of-domain generalization is demonstrated.** The paper tests on problem scales not seen during training (e.g., OBP sets 10k_100 and 10k_500; TSP/CVRP/OP at N=100 and N=200), and CALM generally maintains or even widens its advantage at these larger scales, supporting the claim that the approach does not simply overfit to the training distribution.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Overstated claim about the verbal-guidance-only variant.** The conclusion states that "even without the power of RL, CALM matches or exceeds prior best results using the same LLM API." This is imprecise when examined per-problem. On CVRP (Table 3), the GPT-4o-mini–based CALM (without RL) is *consistently worse* than MCTS-AHD at all three scales (gaps 5.81% vs. 5.44% at N=50, 7.46% vs. 6.98% at N=100, 5.72% vs. 4.70% at N=200). The discussion section (Section 5.2) hedges more carefully ("on par with or superior to"), but the conclusion reverts to a broader statement. This does not affect the core contribution — the RL-driven variant is the main result — but the framing should be tightened to "competitive with" or "firmly in the top tier of" rather than "matches or exceeds."

2. **GRPO distribution shift not discussed.** GRPO is designed for a fixed prompt distribution, but CALM's prompts change over time as evolutionary operators generate new heuristics. The paper does not discuss how this distribution shift affects GRPO's convergence properties or whether the model might overfit to a narrowing prompt distribution as search progresses. The empirical results suggest this is not a practical problem, but a brief acknowledgment and explanation (e.g., whether group advantage normalization mitigates this) would strengthen the exposition and aid reproducibility.

3. **Only 4 training instances used for OBP.** The OBP experiments train on just four instances. While the out-of-domain results suggest generalization is robust, the paper offers no discussion of whether this small training set was chosen to match baselines or because larger training sets degraded performance. A short comment would preempt reader concern about training set sensitivity.

### Trivial
None.

## Nice-to-Haves

- **Qualitative analysis of what RL changes in the model.** The paper would benefit from a few concrete examples comparing heuristics produced before and after RL fine-tuning (e.g., code samples or structural comparisons). This would make the "co-evolution" narrative more tangible and answer the natural question of whether the model learns to avoid specific failure modes.
- **Wall-clock time comparison.** The paper mentions a "detailed breakdown of running time" in Appendix I (stripped by parser). If practical, a concise summary in the main text comparing total training+search time against cumulative API costs of baselines would help readers evaluate practical deployment.

## Removed Points
- *Duplicate definition ambiguity*: The paper clearly defines duplication as "identical performance" (g(h) = g(h_new)), so there is no ambiguity. **Removed** — already clearly specified in the paper.
- *Crossover without diversity is worse than no crossover — lack of explanation*: The paper explicitly comments on this finding ("highlighting the importance of diversity awareness in the most-used operator"). **Removed** — already addressed.
- *Missing wall-clock time*: The paper states running time is reported in Appendix I. **Removed** — covered in appendix (stripped by parser).
- *Missing hyperparameters / reproducibility details*: The paper provides complete algorithm pseudocode (Appendix C) and prompt details (Appendix D). **Removed** — these are present in the original submission.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Tighten the conclusion's claim about the verbal-guidance-only variant to reflect the actual per-problem comparison (e.g., "competitive with prior best results" rather than "matches or exceeds").
2. Add a brief paragraph in Section 4.3 or 5.2 acknowledging that GRPO is applied to a varying prompt distribution and noting why this does not destabilize training (or how the group-advantage normalization handles it).
3. If space permits, include one qualitative example of a heuristic generated before vs. after RL fine-tuning to illustrate what kind of structural changes the RL process induces.

## Score and Decision

**Round 1 (bracketing):** Three queries on LLM-based optimization and evolutionary heuristic design. Low-band anchors (scores 2.5–3.4, Reject) were papers with weak novelty or limited evaluation. Middle-band anchors (scores 4.0–5.75, various decisions) included LLMOPT (5.5, Accept) and LLaMoCo (5.75, Reject), both of which had simpler finetuning approaches and were considered borderline. High-band anchors (scores ~8.0) were papers in other domains with more foundational contributions. **Initial bracket: plausibly 5.5–7.5.**

**Round 2 (narrowing):** Queried for (5.5, 7.5) on topics matching this paper's combination of LLMs with evolutionary algorithms. EvoPrompt (6.5, Accept) — connects LLMs with EAs for prompt optimization, considered a solid contribution but somewhat straightforward. MOLLEO (7.0, Accept) — uses LLMs as genetic operators in molecular discovery, praised for novelty but noted as a "simple substitution." LASeR (6.25, Accept) — LLM-aided evolutionary search for robot design. Promptbreeder (5.8, Reject) — self-referential prompt evolution, criticized for limited novelty. CALM is clearly stronger than LLMOPT (5.5) and Promptbreeder (5.8). It is comparable to EvoPrompt (6.5) in contribution level, but adds the RL fine-tuning component that goes beyond prompt-only evolution, making it technically more ambitious. It is slightly less polished than MOLLEO (7.0) due to the minor framing issues noted above. **Final score: 6.5.**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| XTxdDEFR6D (LLM4Solver) | 3.40 | 1 (low) | Weaker — limited experiments, rejected |
| sUywd7UhFT (MHRE) | 2.50 | 1 (low) | Weaker — rejected with major novelty concerns |
| MpA6HMD7Wq (Symbolic Optimization) | 3.00 | 1 (low) | Weaker — rejected |
| 9OMvtboTJg (LLMOPT) | 5.50 | 1 (mid) | Weaker — simpler finetuning, data labeling issues, accepted but lower |
| EKCubxFdOs (LLaMoCo) | 5.75 | 1 (mid) | Weaker — instruction tuning is standard, rejected |
| ZG3RaNIsO8 (EvoPrompt) | 6.50 | 2 (mid) | Comparable — both combine LLMs+EAs; CALM adds RL fine-tuning |
| awWiNvQwf3 (MOLLEO) | 7.00 | 2 (mid) | Slightly stronger — different domain, similar approach; CALM has more thorough ablations |
| cJPUpL8mOw (REvolve) | 6.00 | 2 (mid) | Slightly weaker — LLM+EA for reward design |
| kWtP5ZOErR (EvoPress) | 6.25 | 2 (mid) | Comparable but different topic (model compression) |
| HKkiX32Zw1 (Promptbreeder) | 5.80 | 2 (mid) | Weaker — self-referential prompt evolution, rejected |
| OXv0zQ1umU (Evoke) | 6.25 | 2 (mid) | Comparable — prompt editing framework, accepted |

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>