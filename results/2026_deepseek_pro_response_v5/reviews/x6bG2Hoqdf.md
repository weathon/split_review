Now I have sufficient calibration data. Let me synthesize everything into the final review.

**Round 1 Bracket:** 5.0–7.0

**Round 2 Narrowing:** The most relevant anchors are Hercules (5.25), Evo-Step (5.50), Promptbreeder (5.80), STOP (6.20), and BOPRO (6.25). CALM is clearly stronger than the 5.25–5.80 range due to its novel RL co-evolution component and unusually thorough ablation study. It is roughly comparable to STOP (6.20) — both have a novel meta-level self-improvement concept, but CALM has more extensive evaluation across benchmark domains while STOP has a cleaner concept. The budget comparison issue (different units, missing G) and unexplained EvoTune results prevent placing it higher. **Final score: 6.0.**

---

## Summary
CALM proposes a framework for automatic heuristic design that jointly evolves prompts and fine-tunes the underlying LLM using GRPO reinforcement learning — moving beyond prior methods that keep the LLM frozen. The paper introduces novel fine-granularity evolutionary operators (injection, replacement, diversity-aware crossover) and a probabilistic collapse mechanism, and demonstrates that the RL-trained 7B quantized model on a single GPU can discover heuristics competitive with or better than those found by stronger API-based models across four benchmark domains (OBP, TSP, CVRP, OP).

## Strengths
- **Thorough ablation study (Table 4) isolates the RL contribution.** Removing GRPO ("local, w/o GRPO") degrades OBP optimality gap from 0.71% to 1.78% and OP from 17.41% to 19.89% — the largest single ablation effect. This, combined with ablations of alternative reward schemes and individual operators, provides unusually strong internal evidence that each design component matters.
- **Novel operator design motivated by GRPO's credit assignment.** The injection and replacement operators (Section 4.1) are specifically designed to target heuristic sub-components, motivated by the observation that GRPO's per-token advantage estimates benefit from finer-grained mutations (lines 76–78). This connects RL algorithm mechanics to operator design in a way not previously explored in LLM-based AHD.
- **The diversity-aware crossover is directly validated.** Table 4 shows that crossover without diversity-based selection is worse than no crossover at all (OBP: 1.05% vs 0.88%; OP: 19.44% vs 18.49%), demonstrating that the diversity mechanism is not merely a nice addition but essential.
- **Resource-constrained setup outperforms API-based baselines using stronger models.** The INT4-quantized Qwen2.5-7B on a single 24GB GPU (acknowledged as weaker than GPT-4o-mini, line 132–136) discovers better heuristics than all GPT-4o-mini-based baselines across OBP, CVRP, and OP — substantiating the claim that on-policy fine-tuning can overcome a substantial model-quality deficit.

## Weaknesses

### Fatal
None.

### Major
- **Budget comparison uses different units for CALM and baselines, and G is not reported in the main text for GRPO experiments.** The paper compares baselines under "1,000 heuristic evaluations" against CALM under "2,000 LLM queries" (line 140). Since CALM with GRPO samples G responses per query, the actual number of heuristics evaluated is T × G. G is specified only for the API variant (G=1, line 221) — for the GRPO-based experiments, neither G nor T appears in the main body. Without this information, the reader cannot assess the evaluation budget asymmetry, which directly bears on whether CALM's gains come from RL fine-tuning or simply from evaluating more heuristics. The "local, w/o GRPO" ablation in Table 4 partially addresses this (assuming same G and T as full CALM), but this too is unstated.

- **EvoTune's poor performance is never discussed or explained.** EvoTune (Surina et al., 2025) is the closest concurrent work — it also fine-tunes an LLM (via DPO) for AHD using the same Qwen2.5-7B-INT4 model. On OBP (Table 1), EvoTune achieves 2.40%, identical to Best Fit (a hand-crafted heuristic from 1995) and worse than nearly every GPT-4o-mini baseline. On OP at N=200 (Table 3), EvoTune's gap (20.32%) is far worse than GPT-4o-mini baselines. The paper never addresses why its closest competitor performs so poorly, raising questions about whether EvoTune was run under fully comparable conditions.

### Minor
- **TSP results undercut the generality narrative.** On TSP at N=50 (in-distribution), CALM with GRPO achieves a 10.04% optimality gap, ~25× worse than POMO's 0.39%. While the paper acknowledges TSP as "challenging for LLM-based AHD" (line 138), the headline framing of generality across "various optimization tasks" (abstract) sits uneasily with results where the method remains an order of magnitude behind specialized neural solvers on in-distribution instances.
- **DeepACO is listed as a baseline (line 140) but never compared against as a separate row.** It is used only to approximate optimal solutions for CVRP and OP (Table 3 note). It should either appear as a comparison row or be clarified as serving a different role.
- **Two HSEvo rows appear in the OP section of Table 3 without explanation** — they appear to represent different configurations or runs but no distinction is drawn.

### Trivial
- The first case of the reward function (Eq. 4) assigns the penalty α₁·r_invalid to any heuristic whose performance equals any base heuristic, which could penalize structurally novel heuristics with coincidentally equal performance. In practice the ablation validates the reward design, but the distinction is theoretically imprecise.
- The analytical expectation in Eq. (2) depends on the assumption C > 1/δ₀ and provides only an expectation — its practical utility for hyperparameter selection beyond the empirical grid search is unclear.

## Nice-to-Haves
- Report G, T, and other hyperparameters for GRPO experiments in the main text.
- A study varying G at fixed total heuristic evaluations would illuminate the trade-off between per-prompt diversity and number of distinct prompts, and help resolve the budget comparison concern.
- Discuss whether the TSP results indicate a structural limitation of LLM-based AHD for step-by-step construction, or whether the problem formulation (step-by-step vs. ACO-based) explains the gap.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Harsh Critic claim that the budget issue is "fatal"** — downgraded to Major because the ablation study (Table 4: "local, w/o GRPO" vs "local, w/ GRPO") and the API variant (G=1) provide within-framework controls that partially isolate the RL effect. The issue is significant but the paper has multiple lines of evidence.
- **Harsh Critic speculation about G=4–8 implying 8:1 budget asymmetry** — this depends on G values not specified anywhere; the core concern about different units is retained but the speculated magnitude is removed.
- **Harsh Critic claim that GRPO "requires G ≥ 2"** — GRPO functions with G=1 (though advantage estimates would be degenerate); this overstatement is removed.
- **Harsh Critic claim that FunSearch/EoH baselines are "missing" from CVRP/OP tables** — the paper never promised those specific baselines for CVRP/OP; baselines are task-dependent. Removed.
- **Strength Finder claim about "verbal guidance alone is competitive with SOTA"** — partially confounded by the budget concern; the API variant evidence is retained but the framing is toned down.
- **Strength Finder claim that collapse mechanism is "formalized with a principled probabilistic trigger"** — the formalism exists but has limited practical utility (see Trivial weakness); the ablation evidence is the real strength.
- **Strength Finder claim about "thorough positioning against concurrent work"** — this is a quality-of-writing point, not a substantive strength.
- **Strength Finder claim that "scale generalization without retraining" is a distinct advantage** — this is generally true of many LLM-based AHD methods, not specific to CALM. Moved to removed.

## Novel Insights
The paper's design of fine-granularity mutation operators specifically motivated by GRPO's token-level credit assignment is a genuinely novel insight. The reasoning that targeting sub-components rather than whole heuristics improves the signal-to-noise ratio for GRPO's per-token advantage estimates (lines 76–78) connects RL algorithm mechanics to evolutionary operator design in a way not previously explored in LLM-based AHD. This is a contribution that could influence future work combining RL fine-tuning with evolutionary search frameworks.

## Suggestions
- Report G and T explicitly in the main text for all GRPO experiments, ideally in a single visible location near the experimental setup.
- Either control for total heuristic evaluations when comparing CALM to baselines, or provide a clear argument for why LLM queries (rather than heuristic evaluations) are the appropriate budget unit given the training signal they provide.
- Add a brief discussion of why EvoTune underperforms, particularly on OBP.
- Clarify the role of DeepACO and the two HSEvo rows in the results tables.

---

## Anchor Comparison Summary

| Anchor | Path | Avg Score | Round | Comparison to CALM |
|--------|------|-----------|-------|---------------------|
| Hercules | `0fwJMANq9P.md` | 5.25 | R1/R2 | Same domain (LLM heuristic generation for COPs). CALM is stronger: adds novel RL fine-tuning, new operators, more thorough ablations. |
| LLM-LNS | `Usk4KzBxLW.md` | 5.25 | R1 | LLM for MILP neighborhood search. Different approach; CALM has broader evaluation. |
| Evo-Step | `aapUBU9U0D.md` | 5.50 | R2 | LLM fine-tuning for OR but via data generation. CALM has more novelty (on-policy RL during search vs. SFT). |
| Promptbreeder | `HKkiX32Zw1.md` | 5.80 | R1 | Prompt evolution, different domain (reasoning). CALM adds RL component and has more thorough ablations. |
| STOP | `1gkePTsAWf.md` | 6.20 | R2 | Self-improving code generation. Comparable novelty level; CALM has broader evaluation but STOP has cleaner concept. |
| BOPRO | `aVfDrl7xDV.md` | 6.25 | R1/R2 | LLM + BO for search, essentially negative results. CALM has clearly stronger empirical outcomes. |
| Vanishing Gradients | `IcVNBR7qZi.md` | 6.25 | R1 | Theory + empirical on RL fine-tuning. Different paper type; hard to compare directly. |
| LLM-SR | `m2nmp8P5in.md` | 8.00 | R1 | LLM for scientific equation discovery. Clearly stronger paper (straight 8s). CALM is not at this level. |

CALM sits between the 5.25–5.80 cluster and the 6.20–6.25 cluster. It is clearly better than Hercules/Promptbreeder but its budget comparison issue prevents it from reaching the 6.25 level. Score: **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>