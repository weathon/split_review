Now I have a clear picture of the calibration landscape. Let me produce the final consolidated review.

## Summary

This paper proposes TMK (Task-Method-Knowledge) structured prompting — a JSON-based knowledge representation framework that replaces plain-text domain descriptions in LLM prompts — and evaluates it on PlanBench's Blocksworld domain across five OpenAI models (GPT-4, GPT-4o, o1-mini, o1, GPT-5). The headline result is o1's Random Blocksworld accuracy jumping from 31.5% to 97.33%, and improvements are observed in 14 of 15 model-domain pairs. The paper also highlights a performance inversion (Random becomes easier than Mystery under TMK for o1), which it interprets as evidence that TMK acts as a symbolic steering mechanism.

## Strengths

1. **Impressive empirical gains on the most challenging variant.** TMK yields a 65.8% absolute improvement for o1 on Random Blocksworld (31.5% → 97.33%) and lifts o1-mini from 9.33% to 27.0% (Table 2). These gains are on the variant where semantic priors are absent, which directly supports the paper's claim about TMK enabling symbolic manipulation.

2. **Performance inversion provides an interesting empirical pattern.** Under plain text, o1 scores 74.3% on Mystery vs. 31.5% on Random. Under TMK, this flips to 83.3% on Mystery vs. 97.33% on Random (Section 4.2). This inversion is a genuine finding that goes beyond what one would expect from simply adding more context.

3. **Systematic evaluation across models and domains.** Table 2 reports accuracy for five models across all three Blocksworld variants (Classic, Mystery, Random), with improvements observed in 14 of the 15 model-domain pairs. The o1-mini Mystery regression (19.1% → 16.83%) is acknowledged and discussed.

4. **Rigorous plan verification.** Plans are validated by automated planning tools (VAL, Fast Downward) requiring full stepwise correctness, avoiding the "close enough" approximation problem (Section 2.2). The paper also uses a random, non-tailored one-shot example, which mitigates pattern-matching concerns raised in prior critiques of prompting methods (Section 3.2).

5. **Robust output handling.** The enhanced extraction function tolerates stochastic output variations (extra symbols, word substitutions like "object" for block names) without incorrectly marking valid plans as incorrect (Section 3.2), following ICAPS conventions.

## Weaknesses

### Fatal
None.

### Major

1. **No variance or multiple-trial reporting.** All results are single-point estimates with no confidence intervals, standard deviations, or seed sensitivity analysis (Table 2). LM outputs are stochastic; near-ceiling results (e.g., 97.33%) could be influenced by a lucky sample. Without evidence of consistency across multiple runs, the magnitude of claimed improvements is not fully trustworthy. This is the most significant methodological gap.

2. **Missing empirical comparison against established structured prompting methods.** The related work (Section 2.1) extensively discusses the limitations of CoT, ReACT, and Chain-of-Symbols — implicitly arguing that TMK addresses their shortcomings — yet the paper never directly compares TMK against any of these methods empirically. The evaluation is limited to TMK vs. plain-text prompts, which is a weaker comparison than the framing implies. While the paper scopes itself to Blocksworld and OpenAI models (line 47), the extensive related-work discussion of CoT/ReACT limitations sets reader expectations for a direct comparison that is not delivered.

3. **Claims about the steering mechanism overreach the correlational evidence.** The conclusion states that the performance inversion "confirms that TMK acts as a symbolic scaffold, effectively steering reasoning models toward formal code-like manipulation" (line 299; also Abstract and Section 5.2.1). However, the evidence is purely correlational — different accuracy patterns across two conditions do not directly demonstrate a change in the model's internal reasoning modality. No probing of reasoning traces, controlled experiments, or analysis of intermediate tokens is provided to support the claim. The mechanism is a plausible hypothesis but is presented as a confirmed finding.

### Minor

4. **Shot-count asymmetry, though explained, complicates the comparison.** The paper compares one-shot TMK against the best of zero-shot *and* one-shot plain text (Section 3.2), arguing this is conservative because zero-shot often outperforms one-shot for plain text. While this reasoning is sound, it conflates two variables (prompt structure and number of examples). Reporting plain-text zero-shot and one-shot separately (alongside TMK zero-shot and one-shot) would be more transparent. The current design leaves some ambiguity about the magnitude of the effect attributable specifically to the TMK structure.

5. **Plain-text baselines from the public leaderboard may not be directly comparable.** The plain-text results in Table 2 are from the public PlanBench leaderboard, while the TMK results were generated separately. These could involve different API versions, sampling parameters, or inference settings. Running all conditions in the same experimental setup would eliminate this potential confound.

6. **The o1-mini Mystery regression (19.1% → 16.83%) is noted but not analyzed.** The paper hypothesizes it is due to "cognitive overload" or "semantic interference" (Section 5), but provides no failure analysis — e.g., whether the model outputs invalid TMK structures, incomplete plans, or semantically plausible but formally incorrect actions. A brief analysis would strengthen the discussion.

7. **The extraction function details are only available via an external OSF link.** The description of how the enhanced extraction handles stochastic output variations is at a high level (Section 3.2, lines 183-193). While citing an OSF repository is standard, including a concrete example or pseudocode would improve accessibility for reviewers.

### Trivial
None.

## Nice-to-Haves

- Running each condition with 3–5 trials and reporting variance
- Including CoT and/or ReACT as baseline prompting methods
- Adding a probe or analysis of model reasoning traces to support (or qualify) the steering mechanism claim
- Reporting plain-text zero-shot and one-shot separately (alongside TMK under both conditions)
- Analyzing failure cases for o1-mini on Mystery Blocksworld

## Removed Points

These points were flagged but removed for the reasons noted:

- **"Cognitive scaffolding argument (Section 5.2.2) is not tested"** — The paper presents this as a hypothesis in the Discussion section, not as a tested claim. No removal needed; it's not a weakness.

- **"The paper should test TMK in other domains"** — The paper explicitly scopes itself to Blocksworld (Section 5.3). Scope limitation is acknowledged by the authors and not a weakness.

- **"Missing related works"** — Removed per policy: I do not have external sources to verify the existence of missing citations.

- **"The extraction function raises concerns about favoring TMK"** — The extraction function handles stochastic variations symmetrically across all conditions. No evidence of bias was presented, and the approach follows ICAPS conventions. This is speculative.

- **Strength Finder: "rigorous evaluation addresses known criticisms" and "benchmark uses formal plan validation"** — These are generic or already covered by the evaluation setup. Merged into Strengths 4 and 5 above.

- **Strength Finder: "robust handling of output variance"** — Kept as Strength 5.

- **"Formatting/style nitpicks"** — Removed per policy.

## Novel Insights

The most striking observation from the reviews is that the paper's strongest evidence — the performance inversion on o1 (Random becomes easier than Mystery under TMK) — is simultaneously its most compelling result and its most overclaimed one. The inversion genuinely is an unusual pattern that goes beyond what simple context-addition would predict, making it worthy of serious attention. But the paper jumps from this pattern directly to a mechanistic claim about "code-execution pathways" without any intermediate analysis (e.g., comparing token-level patterns, measuring attention distributions, or probing internal representations). A follow-up paper that uses the performance inversion as motivation for a mechanistic investigation could be very strong. The reviews also collectively highlight a recurring pattern in prompting-for-planning papers: strong empirical results that are weakened by missing variance reporting and the absence of CoT/ReACT baselines, which are considered standard comparisons in this area.

## Suggestions

1. **Add variance reporting.** Run each condition at least 3–5 times and report mean ± std or individual trials. This is the single most impactful improvement you can make and is standard practice for LM evaluations.

2. **Add at least one structured prompting baseline.** CoT is the most natural comparison for a paper that positions itself against prior prompting work. Even a small-scale CoT comparison (on o1 and o1-mini, for example) would substantially strengthen the paper's claim that TMK offers advantages over existing methods.

3. **Tone down the mechanistic claim.** Replace "confirms that TMK acts as a symbolic steering mechanism" with "is consistent with the hypothesis that TMK acts..." throughout. Add a brief discussion of alternative explanations (e.g., TMK simply provides more complete domain knowledge in a structured way, which helps a model that already has latent planning abilities).

4. **Report plain-text zero-shot and one-shot separately**, and ideally test TMK under both zero-shot and one-shot as well. This would cleanly separate the effect of the TMK structure from the effect of the shot count.

5. **Provide a brief failure analysis for o1-mini on Mystery Blocksworld**, even a small qualitative sample showing what types of errors occurred.

## Score and Decision

**Calibration summary:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|-----------|
| Exploring and Benchmarking Planning Capabilities | koza5fePTs.md | 2.00 | R1 | Much weaker — no new method, purely evaluative. Current paper is clearly above. |
| Planning in Strawberry Fields (o1 eval) | jOuHjFw71C.md | 3.00 | R1 | Weaker — evaluative only, no new prompting method. Current paper has a novel method. |
| Planning with MCTS | sdpVfWOUQA.md | 3.00 | R1 | Weaker — narrower evaluation. Current paper has broader model coverage. |
| LLMs Can Plan Only If We Tell Them (AoT+) | K3KrOsR6y9.md | 6.40 | R1/R2 | Stronger — includes CoT/ToT baselines, ablation studies, variance analysis, broader evaluation. Current paper has larger reported gains but less methodological rigor. |
| ActionReasoningBench | NUD03NBDOE.md | 6.75 | R2 | Different focus (benchmark paper). Not directly comparable. |
| Chain-of-Symbol (CoS) | B0wJ5oCPdB.md | 6.00 | R2 | Similar style (new prompting method, limited baselines). CoS compares against CoT; current paper doesn't. CoS has more tasks. |
| Learning Planning Abstractions from Language | 3UWuFoksGb.md | 5.50 | R1 | Broader scope (abstraction learning). Current paper is similar tier. |
| Tree-Planner | Glcsog6zOe.md | 5.25 | R2 | Closer comparison — similar contribution level, similar evaluation gaps. Both have missing baselines concerns. |

**Round 1 bracket:** The paper sits between the weak anchors (2–3) and the strong anchors (8+). The plausible range is 4.0–6.5.

**Round 2 narrowing:** Comparing against Chain-of-Symbol (6.00) — same style of paper, similar limitations, but CoS compares against CoT whereas the current paper does not, and CoS evaluates on more tasks. The current paper has stronger individual results (65.8% gain vs 60.8% gain) but faces the same types of criticisms. Comparing against AoT+ (6.40) — that paper had more comprehensive evaluation (multiple baselines, ablation studies) despite also being criticized for missing some things. The current paper is clearly below AoT+ in methodological rigor. Comparing against Tree-Planner (5.25) and Learning Planning Abstractions from Language (5.50) — similar tier of contribution with comparable evaluation gaps.

**Final calibration:** The paper makes a genuine contribution with an interesting prompting method and some striking results, but the lack of variance reporting, missing structured-prompting baselines, and overclaimed mechanistic findings place it below the CoS/CoS-like papers (6.0 range) and closer to the 5.0–5.5 range. The contribution is real but the evidence is not yet at the standard expected at a top venue.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>