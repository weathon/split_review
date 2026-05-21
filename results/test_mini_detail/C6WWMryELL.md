Now I have all the information needed. Let me produce the final consolidated review.

## Calibration Summary

**Round 1 — Bracketing:**
- Low band (scores < 3.5): Anchors scoring 1.5–3.25 (weak papers)
- Middle band (scores 3.5–7.5): LongGenBench (6.40), LongWriter (6.00), LV-Eval (5.50), HelloBench (4.75)
- High band (scores > 7.5): Papers scoring 8.0+ (oral accept — clearly stronger)

The paper belongs in the middle band. Initial bracket: **4.0–6.0**.

**Round 2 — Narrowing:**
- Genomics LRB (5.00, Reject): Benchmark paper with good contributions but missing comparisons and overclaiming. The paper under review has a more novel benchmark focus but a more serious framing error.
- HelloBench (4.75, Withdrawn/Reject): Benchmark for long-text generation with evaluation concerns. The paper under review is stronger on benchmark novelty (volatility) but weaker on presenting its method.
- Unlocking Anticipatory Text Generation (4.25, Reject): Constrained decoding paper with limited gains and overclaiming. The paper under review's SELB is more effective but also oversold.
- MAP's not dead yet (5.25, Reject): Decoding degeneracy paper with polarizing opinions.

The paper sits at approximately the same level as these 4.25–5.25 anchors. The benchmark contribution is stronger than HelloBench's, but the misleading "base model" claims and the anecdotal attention analysis are serious weaknesses that pull the score down. Final bracket: **4.5–5.5**.

**Final Score: 5.0** — The benchmark (VOLTBench) is genuinely novel and the empirical findings are useful, but the paper significantly overstates its claims (the "base model" framing error appears in the abstract, contributions list, and conclusion), and the attention analysis is too thin to support the claimed diagnostic contribution.

Now writing the review.

---

## Summary

This paper addresses the overlooked problem of output length volatility in long-form LLM generation across multiple runs. It presents three contributions: (1) VOLTBench, a multi-dimensional benchmark with unstructured and structured tasks across instruction complexities, languages, and scales up to ~100k words; (2) attention trace analysis identifying two internal patterns (Attention Collapse and Attention Instability); and (3) SELB, a training-free constrained decoding strategy that boosts section-title tokens and suppresses failure-prone tokens.

## Strengths

- **VOLTBench is a well-designed benchmark that fills a genuine gap.** Table 1 compares against seven existing benchmarks, showing VOLTBench is the only one incorporating both multiple-sampling and stability evaluation while spanning unstructured/structured tasks, multiple languages, instruction complexity levels, and ~100k-word scale. The chapter-based format enabling scaling from 5 to 500 sections is a practical design choice that surfaces hard failure modes.

- **The paper provides the first large-scale quantification of severe length volatility in mainstream LLMs.** Figure 1 and Table 2 document concrete volatilities: LongWriter-8B has LSD = 2866 (mean 6320) and LVC = 45.4%; even GPT-4o mini shows LVC = 33.9%. The finding that all models fail on tasks exceeding ~50 sections (Section 4.3: "For requests exceeding 50 sections, all models failed to complete the task as instructed") is stark and practically important.

- **SELB is effective at improving length adherence.** On the 100-section structured task, SELB achieves MLA = 78.25% and SCA = 100%, compared to LongWriter-8B's 31.6% and 32.6%. The method is training-free and lightweight (logit manipulation at decoding time), making it easy to apply to existing models.

- **Fine-grained constraints enable automated quality evaluation** for unstructured tasks (character-level pattern, keyword presence, specified theme), allowing programmatic verification rather than relying solely on LLM-as-a-Judge.

## Weaknesses

### Fatal
None.

### Major

1. **Misleading headline claims about "base model" improvement.** The abstract states SELB "improves the mean output length of the **base model** by 148% and reduces the length volatility by 69%." The contributions list and conclusion repeat identical phrasing. However, the numbers in Section 6.3 and Table 2 show that these figures are calculated against LongWriter-8B (mean 6320, LVC 45.4%), *not* the model that SELB is applied to (Qwen2.5-7B, mean 445, LVC 17.0%). Against the actual base model (Qwen2.5-7B), the length improvement is ~3418% and the LVC reduction is ~17.5% — vastly different numbers. This is a material framing error in the paper's most prominently advertised results. A reader would naturally interpret "base model" as the model SELB is built on (Qwen2.5-7B), not a separate fine-tuned baseline. This appears three times (abstract, contributions, conclusion) and needs correction.

2. **The attention trace analysis is anecdotal and insufficient to support the claimed diagnostic contribution.** The paper claims to "identify and define several common internal patterns of length volatility" as a key contribution (second bullet). The evidence is two example traces from Qwen2.5 models on a single task (40-section diary), shown in Figure 4. There is no systematic quantification across multiple runs, models, or tasks; no statistical testing of whether these patterns precede failures more often than chance; and no control comparison (attention traces from generations that *do* meet length requirements). The claim that "output volatility is not random but closely linked to and preceded by measurable failures in the model's internal attention dynamics" is a causal statement supported only by post-hoc interpretation of two plots. This is hypothesis-generating observation, not validated analysis.

### Minor

3. **Uneven baseline comparison.** SELB is compared most prominently against LongWriter-8B (a specialized fine-tuned model), while the comparison against other *decoding strategies on the same base model* is relegated to subsidiary rows in Table 2. From that table: Lookahead Decoding achieves LVC = 9.3% on Qwen2.5-7B, which is *lower* than SELB's 14.02% on the same model. Lookahead's MLA (14.4%) is much lower than SELB's (78.25%), so this is a trade-off, not a clear win either way. But the paper does not discuss this trade-off or explain why SELB is preferable despite higher relative volatility on the same base model.

4. **Overclaiming on "content volatility."** The abstract mentions "inconsistency in length **and content** across multiple generations," but the benchmark metrics (LSD, LVC, MLA) measure only length volatility. Content volatility is never directly measured or quantified. The definition of volatility shifts between sections.

5. **N=5 may be insufficient for stable variance estimation.** The paper uses 5 runs for all volatility metrics but does not discuss whether this is sufficient, especially given the high variance observed (e.g., LongWriter-8B LSD = 2866 on mean 6320). This is acknowledged as a limitation.

6. **SELB results are shown for only one base model (Qwen2.5-7B) in the main table.** Figure 5 shows SELB applied to Qwen3-8B and Llama-3.1-8B, but the main quantitative comparison (Table 2 with SELB row) only reports results on Qwen2.5-7B. Transferability claims would be strengthened by full quantitative results for all base models.

### Trivial

- Figure 3's labels are hard to read in the extracted text (parser issue, not author error).
- MLA definition (capped at 100) is mathematically natural given the formula but would benefit from a brief justification.

## Nice-to-Haves

- A direct comparison of SELB vs. Lookahead Decoding on length accuracy vs. volatility trade-offs would make the method's advantages clearer.
- Validating the automated fine-grained constraint evaluation against human judgments would strengthen the benchmark's quality assessment.
- Reporting SELB results for all base models (not just Qwen2.5-7B) in the main table rather than only in Figure 5.

## Removed Points

- **"SELB has access to privileged information (P_total, τ_max)"** — This information is extracted from the prompt, which all models receive equally. SELB uses it explicitly; other models fail to act on it. That is the method's job, not unfairness. [Removed: misunderstands the experimental setup]

- **"Missing comparison with FUDGE, GeDi, CTRL"** — These are attribute-control methods (sentiment, topic), not designed for length/structural control. The paper compares against relevant decoding baselines (Repetition Penalty, Entropy-Based Stopping, Length Constraint, Lookahead Decoding). [Removed: compares apples to oranges]

- **"Table 2 mixes models at different scales without controlling for model size"** — The paper surveys available models; this is an empirical observation, not a controlled experiment. All long-form generation benchmarks do this. [Removed: standard practice in the field]

- **"No statistical tests or confidence intervals"** — Single-run evaluation on large benchmarks is the norm in this area. This is a nice-to-have, not a weakness. [Demoted to minor/removed from weaknesses]

- **"The paper does not report inter-annotator agreement for UCA"** — UCA uses LLM-as-a-Judge, which does not have traditional inter-annotator agreement. [Removed: misunderstands the evaluation setup]

- Various formatting/style nitpicks from the harsh critic. [Removed per instructions]

## Novel Insights

None beyond the paper's own contributions. The harsh critic's observation that the 148%/69% figures conflate comparisons against different baselines is a genuine finding about the paper's framing, but it is a detection of an error, not a novel synthesis.

## Suggestions

1. **Correct the headline claims.** Replace "base model" with "LongWriter-8B" (or specify the exact comparison baseline) in the abstract, contributions list, and conclusion. Or, for a more impactful claim, compare SELB against Qwen2.5-7B directly (3418% length increase, 17.5% volatility reduction), but ensure the numbers match the stated comparison.

2. **Either strengthen the attention analysis or re-scope the contribution.** If the diagnostic analysis is to remain a claimed contribution, provide: (a) quantitative evidence across multiple runs, models, and tasks; (b) control comparisons with successful generations; (c) a clear methodology for distinguishing Attention Collapse from normal attention dynamics. Alternatively, re-scope this section to "preliminary observations" or "hypothesis-generating analysis."

3. **Discuss the Lookahead Decoding comparison explicitly.** Acknowledge that Lookahead achieves lower LVC (9.3%) on the same base model and explain why SELB's much higher MLA (78.25% vs 14.4%) justifies the design.

4. **Provide full quantitative SELB results for all base models** in the main table, not just in Figure 5.

5. **Disentangle the benchmark contribution from the method.** The VOLTBench results (Section 4) document important model limitations independently of SELB. Consider presenting these findings as a standalone contribution even if the method were not proposed.

## Score and Decision

**Round-1 bracket:** 4.0–6.0 (the paper sits between the weak anchors at 1.5–3.25 and the strong anchors at 8.0+).

**Round-2 anchors consulted:**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| LongGenBench (3A71qNKWAS) | 6.40 | R1 | Stronger benchmark novelty, no misleading claims. The paper under review's benchmark is about equally novel, but its framing errors pull it below. |
| LongWriter (kQ5s9Yh0WI) | 6.00 | R1 | Method paper with cleaner claims and more thorough evaluation. The paper under review has a better benchmark but weaker method validation. |
| Genomics LRB (8O9HLDrmtq) | 5.00 | R2 | Benchmark paper with overclaiming and missing comparisons. Similar in structure; the paper under review is slightly stronger on benchmark differentiation but has a more serious framing error. |
| HelloBench (QM2WoPu1It) | 4.75 | R2 | General long-text benchmark without volatility focus. The paper under review's volatility focus is more novel, but the claim issues are worse. |
| Unlocking Anticipatory (774elYc5tw) | 4.25 | R2 | Constrained decoding with limited gains. SELB is more effective, but the paper's championing of it is undermined by the misleading baseline claim. |
| Attention Satisfies (gfFVATffPd) | 6.00 | R2 | Rigorous attention analysis across 40k prompts, multiple models. The paper under review's attention analysis is far weaker (2 examples). |

**Final score anchored at 5.0.** The paper's VOLTBench contribution and empirical observations about model failures are real and publishable. However, the misleading framing of the headline numerical claims (three times in the paper) and the anecdotal attention analysis (insufficient to support a claimed diagnostic contribution) are significant weaknesses that bring the paper below the acceptance threshold. With substantial corrections to the claims and either strengthened analysis or properly re-scoped contributions, the paper could reach acceptance level.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>