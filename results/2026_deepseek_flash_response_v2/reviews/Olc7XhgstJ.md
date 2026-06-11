I now have enough information to calibrate and write the final review.

## Calibration Summary

**Round 1 — Bracketing:**
- Weak anchors (<3.5): avg ~2.5–3.0 (papers with fundamental issues or minimal contributions)
- Middle anchors (3.5–7.5): avg ~4.0–6.5
- Strong anchors (>7.5): avg ~7.6–8.0

The paper clearly belongs in the middle band — it has a genuine contribution and substantial experiments, but also notable issues.

**Round 2 — Narrowing (4.5–7.5):**
- TPO (6.33, Accept): Preference optimization for reasoning via tree-of-thoughts. ST is comparable but has the unresolved token discrepancy.
- "Deliberate Reasoning" (5.50, Reject): Similar weakness structure (inference-only baselines vs. training-based method). ST is more thorough (more models, behavioral analysis), so slightly stronger.
- "Rationality of Thought" (6.50, Reject): Cleanly executed but simpler contribution. ST has more depth but also more flaws.

The paper sits between 5.0 and 6.0 on this spectrum. It has a genuine contribution and meaningful evidence, but the token count discrepancy and comparison asymmetry are real issues that need addressing.

**Final Score: 5.5**

---

## Summary

This paper proposes Steady Thought (ST), a three-stage framework to mitigate "under-thinking" in Large Reasoning Models (LRMs). ST (1) segments model responses into thoughts using entropy-based detection, (2) generates preferred continuations by suppressing switch tokens during decoding, and (3) applies thought-level preference optimization (STPO) — conditioning on the shared prefix at the divergence point — to encourage commitment to promising reasoning trajectories. Experiments across three model scales (1.5B–14B) and four datasets, including OOD code tasks, show accuracy gains of up to 5.3% with token reductions of 19–39%.

## Strengths

- **Thought-level preference optimization provides finer-grained supervision than holistic response-level methods.** The paper identifies a genuine limitation of DPO/SimPO — treating entire reasoning chains as monolithic blocks discards correct initial reasoning. STPO (Eq. 7) conditions on the shared prefix (Q, T_i) at the divergence point, directly optimizing the decision to commit vs. switch. This is a principled improvement over methods that only compare full responses.

- **Consistent accuracy gains and token reductions across three model scales with OOD generalization evidence.** Table 1 shows ST improves average accuracy by +1.9% (1.5B), +3.12% (8B), and +2.52% (14B) while reducing average tokens by 24.9%, 25.5%, and 17.3% respectively. The LiveCode OOD benchmark shows meaningful gains (e.g., +5.3% on Qwen3-8B with 19.0% fewer tokens), ruling out simple memorization of shorter responses.

- **Direct behavioral evidence: proportion of correct intermediate thoughts (PCT) drops after training.** Table 2 shows PCT decreases substantially after ST (e.g., from 54.90%→40.40% on MATH500, 14.50%→7.90% on AIME2024 for the 1.5B model). This directly validates that the model makes fewer wasteful switches, not merely produces shorter outputs.

- **Ablation isolates the benefit of STPO over simpler alternatives.** Table 4 compares STPO against SFT and DPO on identical preference data. STPO achieves the best accuracy-token tradeoff (84.4% accuracy, 2809 tokens on MATH500 vs. 80.4%/2650 for SFT and 82.6%/4273 for DPO), demonstrating that the design choices matter beyond just data construction.

- **Proportion-of-last-thought metric provides convergent behavioral evidence.** Figure 2 shows the final thought accounts for a markedly larger share of the response after ST (e.g., MATH500: 28.95%→54.36% for 1.5B), consistent with deeper rather than truncated exploration.

## Weaknesses

### Major

1. **Token count discrepancy between Table 1 and Figure 2.** For DeepSeek-R1-Distill-Qwen-1.5B on MATH500, Table 1 reports 4,385 tokens (Vanilla) and 2,809 (ST), while Figure 2(a) reports "Average Length of Responses" as 2,343 (Base) and 1,459 (ST) — a ~1.87× difference. A similar gap exists for all model/dataset pairs reported in both. The paper never clarifies whether these measure different quantities (e.g., thinking-only tokens vs. total response tokens), and the labels used are nearly identical. The systematic ratio suggests a plausible explanation (thinking-part-only vs. full response), but the paper's failure to state this explicitly undermines trust in the reported token reduction magnitudes. This must be clarified.

2. **Main experimental comparison (Table 1) structurally favors the proposed method.** The primary baselines — NoThink, NOWAIT, and SEAL — are all inference-time interventions applied to frozen models. ST, by contrast, trains on thousands of labeled problems from omni-math. The only training-based comparison (Table 4, Section 4.4.4) is confined to the 1.5B model and does not appear in the main results table. Additionally, NoThink trades massive accuracy drops for token reduction (e.g., 37.20% overall accuracy for 1.5B, a 33% relative drop) and NOWAIT catastrophically degrades Qwen3-8B (59.03% vs. 80.23% base). SEAL is the only competitive baseline, and ST's per-dataset gains over SEAL on 8B/14B models are modest (0.77–1.45%), with SEAL actually beating ST on LiveCode for 14B (75.1% vs. 74.3%). The main results table would benefit from including training-based baselines (SFT, DPO) or prominently acknowledging this asymmetry.

### Minor

3. **No variance or statistical significance reporting.** Accuracy numbers are reported without confidence intervals or standard deviations. This is especially concerning for AIME 2024 (only 30 problems), where reported gains (e.g., 31.2% vs. 27.5% for 1.5B) could fall within noise. The paper states it averages 8 runs for AIME and 2 for LiveCode but never reports the variance across those runs.

4. **The "Overall" accuracy column averages across datasets of very different difficulty using arithmetic mean.** GSM8K (~95% for Qwen3-8B) and AIME 2024 (~62%) are averaged with equal weight, which can be misleading. Per-dataset reporting (already present) is more informative, but the "Overall" column's construction should be justified or replaced.

5. **Training dataset (omni-math) details are underspecified.** The paper describes it only as "thousands of problems at the level of the International Mathematical Olympiad" with "problems from various difficulty levels." The exact size, difficulty distribution, and filtering criteria are not stated, which hampers reproduction.

6. **The claim of "selectivity" (preserving switching when necessary while reducing it when unpromising) is asserted but not directly measured.** The paper shows that ST reduces overall switching (PCT drops), but does not partition test examples by whether the first thought was correct or not to verify that ST preserves switching when the initial trajectory is wrong. This would directly support the selectivity claim versus global suppression methods.

7. **Thought Completion data generation uses the same token-suppression technique the paper critiques in prior work.** While ST uses suppression only during data generation (not inference), the paper does not analyze whether suppression-generated training data might inadvertently teach the model to under-switch in cases where switching would be beneficial. No analysis of the hit rate (how often suppression-aided completion yields a correct answer) is provided, so the reader cannot assess how much training data is actually usable.

### Trivial

None.

## Nice-to-Haves

- A direct selectivity analysis partitioning test examples by whether the base model's first thought was correct, showing that ST behaves differently in each regime.
- GPU-hour cost reporting for the full three-stage pipeline.
- Entropy threshold tuning analysis for the 8B and 14B models (currently only shown for 1.5B in the main text).

## Removed Points

The following points from the reviewers were removed:
- **Table 1 header uses ↓ for both accuracy and tokens (implying lower=better for accuracy)**: This is a parser/formatting artifact from PDF extraction; the original submission likely formats this correctly. Removed per formatting artifact rule.
- **"Section 2.1 formalism is decorative"**: The formalism provides a clean framework that is then instantiated; this is standard practice and not a weakness.
- **"Promising thought identification is circular"**: The procedure IS described in the paper (complete each thought → check correctness → if correct, it's promising). Using ground-truth answers for supervised training data is standard practice, not circular logic.
- **"NoThink is a strawman, NOWAIT is misconfigured"**: The paper reports these as published methods; criticizing their inclusion without evidence of misconfiguration in the specific setup is speculative.
- **Various criticisms about missing appendix content**: The parser strips appendices from all papers. Removed per rules.
- **"Missing related works"**: Per instructions, we cannot verify missing references.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- Clarify the token count discrepancy between Table 1 and Figure 2 (specify whether they measure thinking-only vs. total response tokens).
- Add training-based baselines (SFT, DPO) to the main results table or prominently acknowledge the asymmetry between training-based ST and inference-only baselines.
- Report variance (standard deviation or confidence intervals) for main results, especially AIME 2024.
- Provide a selectivity analysis: partition test examples by whether the base model's first thought was correct, and show that ST behaves differently in each regime.
- Provide concrete statistics for the omni-math training data (size, difficulty breakdown).
- Analyze the hit rate of the Thought Completion stage (how often suppression-aided completion yields a correct answer).

## Score and Decision

**Round 1 Bracket**: The paper sits between weak anchors (~3.0) and strong anchors (~8.0). It clearly belongs in the middle band (4.0–7.0) — it has a genuine contribution and substantial experiments, but also notable issues that prevent it from being a top paper.

**Round 2 Anchors (consulted)**:
- *TPO* (avg 6.33, Accept): Preference optimization via tree-of-thoughts for reasoning. ST is comparable in contribution depth but has the unresolved token discrepancy issue, placing it slightly below.
- *Deliberate Reasoning* (avg 5.50, Reject): Structure-aware planning framework. ST is more thorough (more models, more datasets, behavioral analysis) and has a cleaner contribution. Comparable to slightly stronger.
- *Rationality of Thought* (avg 6.50, Reject): Prompting technique with moderate novelty but clean execution. ST has more methodological depth but also more evaluation issues.
- *Mind Your Step* (avg 5.00, Reject): Empirical study on when CoT hurts. ST has a more substantial constructive contribution, placing it clearly above.
- *RouteLLM* (avg 6.33, Accept): Routing framework. Different domain but similar level of contribution depth.

**Final Anchoring**: The paper is most comparable to "Deliberate Reasoning" (5.50) and "TPO" (6.33) — similar structure of contribution and evaluation. ST is more thorough than Deliberate Reasoning but has the token count issue that Deliberate Reasoning doesn't. ST has a clearer contribution than TPO but less clean evaluation. The unresolved token discrepancy prevents it from reaching the 6+ range typical for Accept decisions.

MY FINAL SCORE: 5.5
MY FINAL DECISION: Reject