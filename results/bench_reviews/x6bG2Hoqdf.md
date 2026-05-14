Now I have all the evidence I need. Let me write the final consolidated review.

---

## Summary

CALM introduces a framework that jointly evolves both the prompt-generation process and the LLM itself for automatic heuristic design (AHD). Unlike prior LLM-based AHD methods that keep the LLM frozen and rely solely on textual prompt manipulation ("verbal gradients"), CALM uses GRPO-based reinforcement learning to fine-tune the LLM on-the-fly using prompt-response-performance triplets from the evolutionary search loop. The framework includes novel fine-granularity mutation operators (injection, replacement) designed to produce token-level variation that GRPO can credit-assign effectively, plus a diversity-aware crossover and collapse mechanism. Using an INT4-quantized Qwen2.5-7B-Instruct model on a single 24GB GPU, CALM discovers heuristics that outperform GPT-4o-mini-based baselines across OBP, TSP, CVRP, and OP.

## Strengths

- **RL-based co-evolution is a genuine advance for LLM-based AHD.** Prior work keeps the LLM frozen; CALM demonstrates that treating the evolutionary loop as a training-data source and adapting the LLM via GRPO yields consistent, substantial improvements. The API-based CALM variant (matching baseline query budgets) is competitive with SOTA (Tables 1–3, Section 5.2), and adding GRPO on a quantized 7B model pushes performance past GPT-4o-mini-based baselines — a result that would be impossible without the learned adaptation.

- **Fine-granularity operators are well-motivated and empirically validated.** The injection and replacement operators are explicitly designed to create token-level variation that maps naturally onto GRPO's per-token advantage signal (Section 4.1). The ablation (Table 4) shows removing any operator degrades performance, and removing diversity-aware crossover hurts more than removing crossover entirely, confirming that the design choices matter.

- **Thorough experimental validation across diverse problems and comparisons.** The paper evaluates on four distinct optimization tasks (OBP, TSP step-by-step, CVRP with ACO, OP with ACO), compares against 7+ LLM-based baselines plus hand-crafted and NCO methods, and includes ablations for every major component (operators, reward function, collapse mechanism). Appendix I.9 further compares GRPO-enhanced MCTS-AHD vs CALM under matched training conditions, isolating the benefit of CALM's design beyond simply adding GRPO to any method.

- **Practical and accessible computational footprint.** Running entirely on a single 24GB GPU with a heavily quantized model (1.15% weights fine-tuned, 5–7 hours per experiment) while outperforming API-based methods is a meaningful demonstration of efficiency.

- **Reward function design is carefully considered and ablated.** The progressive reward scheme (infeasible  duplicate  new < improvement) with credit relative to the best base heuristic in the prompt (Equation 4) is shown to outperform simpler alternatives (Table 4: rew=performance and binary-improvement variants), confirming that prompt-aware credit assignment matters.

## Weaknesses

### Fatal

None. The core claim — that RL-based fine-tuning within the evolutionary loop improves heuristic discovery — is well-supported by the evidence.

### Major

None.

### Minor

- **Query budget asymmetry for non-OBP tasks when comparing CALM (w/ GRPO) to baselines.** CALM uses 2,000 LLM queries for non-OBP tasks while most baselines use 1,000 heuristic evaluations (≈1,000 LLM queries). The paper is transparent about this (Section 5, "Baselines"), and the asymmetry is partially mitigated by (a) the API-based CALM variant that matches baseline budgets and still performs competitively, (b) the EvoTune comparison using the same Qwen 7B model at 1,000 evaluations, and (c) the Appendix I.9 comparison of MCTS-AHD+GRPO vs CALM+GRPO under matched training conditions. However, the main headline comparison in Tables 1–3 between CALM (local, w/ GRPO) and the GPT-4o-mini baselines compounds both the model-quality gap (in CALM's favor) and the query-budget gap (in baselines' partial favor), making it slightly harder to attribute the full performance delta to the method alone. This does not invalidate the core claim but should be discussed more explicitly.

- **No "collect-then-fine-tune" baseline to isolate the benefit of online co-evolution.** The paper shows CALM (w/ GRPO) vs CALM (w/o GRPO), establishing that RL fine-tuning helps. It also shows CALM+GRPO benefits more than MCTS-AHD+GRPO (Appendix I.9), suggesting the co-evolution design matters. However, comparing online co-evolution against a two-stage pipeline (run verbal evolution to collect data, then fine-tune offline on that static corpus) would more cleanly isolate whether continuous on-the-fly adaptation is necessary. This is a reasonable ablation to request but does not threaten the paper's main contribution.

- **Selective reporting on OP N=50 in-domain.** The paper states CALM "outperforms EoH and the most recent approach, MCTS-AHD and EvoTune" on OP in-domain, which is factually correct (15.054 vs 13.388, 14.847, 15.053 respectively). However, ReEvo achieves 15.103 (gap 23.98%) on this same metric, outperforming CALM. The paper never claims to beat ReEvo on this metric, but readers may find the omission noticeable given ReEvo is a prominent baseline in the table.

### Trivial

- The collapse mechanism's analytical approximation (Equation 2) relies on δ₀ ≪ 1 per Appendix G, while experimental values δ₀=0.005 are borderline for this assumption. The practical results in Table 4 confirm the mechanism works, so this is a minor precision concern.

## Nice-to-Haves

- A "collect-then-fine-tune" offline baseline as discussed above would further strengthen the co-evolution narrative.
- Replacing each operator with a simpler alternative (e.g., random mutation instead of injection) rather than removing it entirely, to test whether the specific operator design matters beyond just having some mutation.
- A visualization (e.g., embedding plot) of how the LLM's output distribution shifts over the course of fine-tuning to make the co-evolution dynamic more tangible.
- An experiment with a larger model (e.g., Qwen2.5-14B) to assess whether gains scale with model capacity.

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **"Unfair evaluation budget renders headline comparisons invalid" (harsh critic).** The budget asymmetry is real but the paper addresses it through (1) the API variant matching baseline budgets, (2) the Appendix I.9 matched-setting comparison, and (3) the EvoTune comparison at equal budget. The asymmetry does not invalidate the core claims. Downgraded from fatal to minor.

- **"Inaccurate result reporting for OP" (harsh critic).** The critic claimed MCTS-AHD achieves 15.103 on OP N=50 vs CALM's 15.054. This is factually incorrect — the 15.103 value belongs to ReEvo, not MCTS-AHD. MCTS-AHD's OP N=50 result is 14.847 (Table 3, line 615). CALM (15.054) does outperform MCTS-AHD (14.847), as the paper states. Removed entirely; the reviewer misread the table.

- **"Missing comparison to GRPO-enhanced MCTS-AHD" (harsh critic).** This experiment exists in Appendix I.9 (Tables 15–16), comparing MCTS-AHD+Qwen w/GRPO vs CALM+Qwen w/GRPO under matched training conditions. Removed.

- **"Introduction oversimplifies prior work" (harsh critic).** The paper acknowledges concurrent fine-tuning work (Surina et al., Liu et al.) in Section 2, lines 124–127. The introduction's framing is a stylistic choice, not a factual error. Removed.

- **"Collapse derivation not rigorously justified" (harsh critic).** The approximation is in Appendix G, and the experimental results validate the mechanism empirically. Downgraded to trivial.

- **"Reward function confound: base heuristic quality" (harsh critic).** The paper addresses this in Appendix I.7 (sensitivity analysis). Removed.

- **"Ablation should replace rather than remove operators" (harsh critic).** This is a nice-to-have methodological improvement, not a weakness. Moved to Nice-to-Haves.

- **Strength Finder generic strengths about "the paper addressing an important problem" or "targeting an interesting question" without concrete evidence.** Removed.

- **"Missing appendix, missing proofs" (harsh critic implication).** The parser strips appendices; they exist in the original submission. Removed.

## Novel Insights

Beyond the paper's own contributions, a notable insight emerging from this work is that token-level credit assignment from GRPO pairs particularly well with operators that produce localized, interpretable code changes (injection of new components, replacement of specific fragments). This design choice — making the mutation granularity match the RL signal granularity — is not obvious and may generalize beyond AHD to other code-generation domains where RL fine-tuning is applied.

## Suggestions

- Add an explicit discussion of the query-budget asymmetry in Section 5, perhaps noting that while CALM uses 2,000 queries vs 1,000 for baselines, the model used is substantially weaker (INT4-quantized 7B vs GPT-4o-mini), and the API-based variant at equal budget already shows competitive performance.
- Acknowledge in the OP results discussion that ReEvo achieves a slightly better gap on the in-domain N=50 scale (23.98% vs CALM's 24.22%), to avoid the appearance of selective reporting.
- Consider adding a "static fine-tuning" baseline for the final version to cleanly isolate the co-evolution benefit, though this is not essential for the current contribution.

## Score and Decision

### Anchor Comparisons

- **EvoPH** (`oD9RwlFqEE.md`, avg 2.00, withdrawn/rejected): Co-evolves prompts and heuristics but limited to 2 problems, one LLM, lacks RL-based model adaptation. CALM is substantially stronger in novelty, experimental breadth, and practical impact.

- **TPD-AHD** (`VEMknlIPtM.md`, avg 3.00, rejected): Textual preference differentiation for LLM-AHD; limited novelty (similar to reflection), poor reproducibility, restricted experiments. CALM significantly exceeds this in contribution and validation.

- **MoH** (`tIQZ7pVN6S.md`, avg 5.00, accepted poster): Meta-optimization of heuristics; novel idea but concerns about fairness and generalizability. CALM has stronger experimental validation, more thorough ablations, and a more concrete technical mechanism (GRPO co-evolution rather than meta-prompt optimization).

- **RedAHD** (`6f8qlK7wN4.md`, avg 5.33, rejected): Uses LLM for problem reductions; introduces new manual effort burdens, limited sensitivity analysis. CALM's contribution (RL co-evolution + specialized operators) is more technically novel and better validated.

- **HiFo-Prompt** (`imSLzfZ6av.md`, avg 4.40, accepted poster): Hindsight-foresight prompt for AHD. CALM's RL-based co-evolution is a more fundamental advance beyond prompt engineering.

- **HeuriGym** (`HWxHUO15Yy.md`, avg 6.00, accepted poster): Benchmark for LLM-crafted heuristics; different paper type. As a method contribution, CALM is comparable in quality — thorough experiments, clear novelty, practical value.

CALM sits above the 5.0–5.33 range (MoH, RedAHD) due to stronger experimental validation, more thorough ablations, and a more concrete technical contribution. It is comparable to HeuriGym (6.00) in quality though as a method rather than benchmark paper. The minor budget asymmetry and missing static-fine-tuning baseline prevent a higher score, but neither threatens the core contribution.

**Originality:** High — first to integrate RL-based LLM fine-tuning into the AHD evolutionary loop with operators designed for token-level RL signal.

**Importance:** The research question (can LLMs be adapted during heuristic search rather than used as static generators?) is important and timely. Demonstrating that a local quantized 7B model can outperform API-based methods has practical significance.

**Claims supported:** Well-supported overall. The API-based variant validates the verbal operators independently; GRPO comparisons and ablations validate the RL contribution; Appendix I.9 validates the co-evolution design against GRPO-enhanced baselines.

**Soundness:** Generally sound, with the minor budget asymmetry caveat discussed above.

**Clarity:** Well-written and well-organized. Tables and figures are informative.

**Value to community:** High — the framework, operators, and reward design provide a blueprint for future RL-enhanced AHD work; the code is open-sourced.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>