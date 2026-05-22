Now I have sufficient understanding of the paper and the anchors. Let me construct the final review.

## Summary

This paper introduces the Task-Method-Knowledge (TMK) framework as a structured prompt to improve LLM planning on PlanBench Blocksworld variants. TMK, originally developed for cognitive architectures and educational applications, decomposes domain knowledge into hierarchically linked Tasks (goals), Methods (procedures), and Knowledge (ontology). The paper reports that replacing the standard domain description with a TMK-formatted prompt (in JSON) yields substantial accuracy improvements, most dramatically on o1 for Random Blocksworld (31.5% → 97.33%). The authors argue that TMK acts as a "symbolic steering mechanism" that shifts model inference from semantic approximation to code-like symbolic manipulation, evidenced by a performance inversion where Random blocksworld becomes easier than Mystery blocksworld under TMK.

## Strengths

- **Large, well-documented accuracy gains on the hardest domain variant:** Table 2 reports o1 going from 31.5% to 97.33% on Random Blocksworld under TMK — a 65.8-point improvement. This is the strongest quantitative evidence in the paper and, if valid, constitutes a meaningful advance for prompting-based planning.
- **Novel, well-motivated framework drawn from cognitive science:** Applying TMK (a knowledge representation framework from cognitive architectures) to LLM prompting is genuinely novel. The paper clearly explains TMK's three components (Task, Method, Knowledge) and why its emphasis on teleology and causal decomposition might help LLMs.
- **Conscious effort to address known criticisms of prior prompting work:** Section 5.1 explicitly engages with criticisms of CoT/ReACT (pattern matching on n-shot examples, contradictory chains, lack of cross-domain improvement) and explains how the study avoids each. This shows methodological awareness.

## Weaknesses

### Major

1. **Extraction-function uniformity is not established, creating a potential confound for the headline result.** The paper describes an "enhanced extraction function" (Section 3.2) for Random Blocksworld that tolerates extra symbols, synonyms, and word-order variations, preventing formatting noise from being scored as incorrect. The text states this "was applied for random blocksworld data set" (line 235) but does **not** specify whether it was applied uniformly to both plain-text and TMK conditions. For older models (GPT4, GPT4o, o1preview), the plain-text baselines are taken from the public PlanBench leaderboard (Valmeekam, 2023), which uses strict exact-match validation. If the enhanced extraction was applied only to TMK results while leaderboard plain-text results used strict extraction, then some portion of the reported TMK gain — especially on Random Blocksworld where the extraction differences matter most — could be an evaluation artifact rather than a genuine planning improvement. The paper's claim that such errors are "rare in classic blocksworld" but "evident within random blocksworld domains" (line 243) acknowledges this is precisely where the largest improvements are reported. **This must be clarified and ablated before the core claims can be accepted.**

2. **The plain-text baseline comparison is asymmetric and under-documented.** Table 2 compares TMK (always one-shot) against plain-text "best of sampled Zero & One shot." The authors argue this is conservative (zero-shot > one-shot for plain text), and cite sample testing in the OSF repository, which is a reasonable methodological choice. However, the actual one-shot plain-text numbers are not reported in the paper. For the models whose baselines the authors ran themselves (o1, GPT5), the exact prompt template and extraction method used are not specified in sufficient detail to allow independent replication or assessment.

### Minor

1. **Per-domain problem counts are not reported.** The paper gives accuracy percentages but never states how many problems each domain variant contains. Without denominator information, small differences (e.g., GPT4 Classic: 34.6 vs. 39.7; GPT4o Random: 0.83 vs. 4.83) cannot be evaluated for statistical significance. This is standard information that should be included.

2. **The "performance inversion" claim is over-interpreted.** The paper treats the reversal (o1: Random 31.5% → 97.33% under TMK, surpassing Mystery 74.3% → 83.3%) as strong evidence that TMK shifts models from "linguistic approximation" to "symbolic manipulation." However, this pattern is observed strongly in only one model (o1); GPT5 shows a much weaker version (Random 92.5% → 99.0%, Mystery 98.1% → 98.3%). Alternative explanations — such as TMK providing more complete domain knowledge that disproportionately helps in domains where the model has less pre-trained familiarity — are not ruled out. The paper should acknowledge this more explicitly and discuss what additional evidence would confirm the steering mechanism hypothesis.

3. **Limited domain scope.** The paper only evaluates on Blocksworld within PlanBench. While this is a reasonable starting point, generalizability to other planning domains (e.g., Logistics, maze navigation) is entirely unknown. The paper acknowledges this limitation but does not temper the broader claims ("likely to demonstrate similar gains in planning tasks for other domains," line 33) accordingly.

### Trivial

None.

## Nice-to-Haves

- Including confidence intervals or statistical significance tests for the main comparisons would strengthen the evaluation.
- Reporting one-shot plain-text results for all models (even if only in an appendix or supplementary table) would increase transparency and remove the current ambiguity.

## Removed Points

- **Missing one-shot plain-text numbers as a "fatal" or "critical" issue:** The authors explicitly explain why the asymmetric comparison is conservative (zero-shot > one-shot for plain text; Section 3.2). While transparency would be improved by reporting these numbers, the argument that this undermines the results is not supported given the paper's stated reasoning.
- **o1 vs o1preview score discrepancy:** The footnote (Table 2) clearly states o1preview results are from Valmeekam (2023) while o1 results were run by the authors under potentially different conditions. This is explainable and not a valid weakness.
- **"Missing related work" type criticisms:** These are excluded per the hard rules (cannot verify external sources).
- **Speculative reproach about pattern matching:** The paper addresses this directly in Section 5.1.
- **Formatting/style complaints from harsh critic:** Excluded per hard rules.
- **Strength about "rigorous evaluation infrastructure":** The strength mentions the VAL/Fast Downward verification and enhanced extraction as evidence of rigor, but the extraction concern cuts against this. Strength is demoted but included here for reference.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Clarify and isolate the extraction function.** Report explicitly whether the enhanced extraction was applied uniformly to both plain-text and TMK conditions for every model. Provide an ablation: how do the TMK results change under strict (exact-match) extraction vs. the enhanced extraction? If the plain-text baselines for GPT4/GPT4o were from the leaderboard (strict extraction), re-evaluate those baselines with the same enhanced extraction to enable a fair comparison.
2. **Report one-shot plain-text numbers for all models,** even if only in a supplementary table, to eliminate the shot-count asymmetry concern.
3. **Include per-domain problem counts** and, where possible, confidence intervals or error bars.
4. **Temper the "symbolic steering mechanism" claims** and more clearly delineate which parts of the interpretation are supported by the current evidence vs. which are speculative hypotheses for future work.

## Score and Decision

### Calibration

**Round 1 — Bracketing:** Three queries on LLM/planning/PlanBench topics returned anchors in three bands:
- Low band (avg < 3.5): VmB1GGeU7y (3.0), LOqTK59rxd (2.0), uqVBUDwtS6 (2.0), zHexNab8uH (2.5)
- Middle band (3.5–7.5): FKhMrV1nvz (4.5), qDFegAnCin (4.5), LmyjuhNgML (4.0), mBxFCTlFmW (4.0)
- High band (>7.5): VKGTGGcwl6 (8.0), DM0Y0oL33T (8.0), 9gw03JpKK4 (8.0), qOyF214xmg (8.0)

**Initial bracket:** 3.5 – 5.5. The paper is clearly above the weak-band papers (which score 2–3 on flawed or thin contributions) but well below the 8.0 papers (broad, rigorous contributions).

**Round 2 — Narrowing:** Read FKhMrV1nvz (PDDL-Instruct, 4.5) and qDFegAnCin (VERA, 4.5) for close comparison; read WIXohR7mEo (ACPBench Hard, 6.0) and 5EKY1epoff (Countdown, 5.33) for upper-boundary reference.

- Compared to **PDDL-Instruct (4.5):** That paper presents a more rigorous evaluation (multiple domains, per-domain results with standard deviations, clear comparison against baselines). The current TMK paper is weaker on evaluation transparency and narrower in domain scope, but brings a novel prompting-only approach (no fine-tuning). Slightly below.
- Compared to **VERA (4.5):** That paper has thorough ablations and multi-domain evaluation. The TMK paper's evaluation is less complete. Slightly below.
- Compared to **Countdown (5.33):** That paper provides theoretical analysis (NP-completeness proof) and broader evaluation. The TMK paper does not have comparable theoretical grounding.

**Final placement:** 4.0 — The paper has a genuinely novel idea and striking results, but the evaluation transparency concerns (especially the extraction-function ambiguity) prevent it from reaching the evidentiary standard of the 4.5–5.5 anchors. If the authors clarify the extraction uniformity and the results hold, the score could rise to the 4.5–5.0 range.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>