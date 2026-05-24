Now I have a clear picture of the landscape. Let me formulate the review.

**Round 1 bracket**: Between 4.5 and 6.0.

**Round 2 narrowing**: Comparing to specific anchors — the paper is weaker than "LLMs Can Plan Only If We Tell Them" (6.40) and Tree-Planner (5.25) on experimental rigor, but stronger than MAP (4.50) in novelty and result magnitude. I place it at approximately 5.0.

Let me now produce the final consolidated review.

**Summary of my filtering decisions**:

1. **Extraction issue (Harsh Critic #1)**: Keep as Major. The paper modified extraction for Random Blocksworld but doesn't explicitly state whether plain-text baselines were re-evaluated with the same extraction. However, NOT fatal — the effect sizes are so large (31.5%→97.3%) that formatting artifacts could explain at most a few points.

2. **No control for structure vs. content (HC #2)**: Keep as Minor. Valid point but doesn't invalidate the core empirical finding. The paper shows TMK helps; whether other structured formats would help as much is a separate question.

3. **Unsupported mechanistic claims (HC #3)**: Keep as Minor. The paper does overclaim the mechanism, but the main contribution is the empirical result, not the mechanism.

4. **One-shot confound (HC #4)**: Downgrade to Minor/Nice-to-have. The paper already provides reasonable justification (zero-shot > one-shot in plain-text PlanBench). The critic's suggestion of zero-shot TMK is valid but the concern is significantly addressed.

5. **Missing variance/CI**: Minor. Standard for this type of work but worth noting.

6. **Strength Finder strengths**: Keep strengths 1 and 2 (both concrete and specific). Strength 3 (detailed TMK instantiation) — keep as it's concrete.

Let me also check if the critic says anything about "not yet released" or reproducibility that I should remove.

The critic says: "the paper does not report which specific baseline was used for each model or whether the one-shot examples in those baselines were comparable in length to the TMK prompt. This matters: if GPT4's one-shot plain-text baseline included a long example, it might change conclusions. The lack of transparency is a reproducibility concern."

This is a reasonable point, not a "not released" concern. I'll keep it as Minor.

The critic also says: "The paper should state explicitly whether Classic and Mystery baselines were also re-evaluated with the same extraction. Currently, it is unclear, and this ambiguity undermines all three domain comparisons."

This is part of the extraction issue. Let me merge all extraction-related points into one Major weakness.

Let me write the review now.Now let me write the consolidated review.

## Summary

This paper introduces TMK (Task-Method-Knowledge) prompting, a structured JSON-based prompt format grounded in a cognitive science framework, for improving LLM performance on the PlanBench Blocksworld planning benchmark. The central empirical result is striking: o1 goes from 31.5% to 97.3% accuracy on the opaque Random Blocksworld variant, and the paper documents a "performance inversion" where symbolic tasks (Random) become easier than semantically-labeled ones (Mystery) under TMK. The paper also takes care to address known criticisms of prior prompting work — using one-shot examples that do not match the query, evaluating full plan correctness, and noting that zero-shot outperforms one-shot in the plain-text baseline.

## Strengths

- **Large, well-documented accuracy gains on symbolic tasks (Table 2).** The o1 improvement from 31.5% → 97.3% on Random Blocksworld is a dramatic result. Even accounting for potential confounds, a gain of this magnitude on a benchmark where the model previously failed is substantial evidence that the TMK structure provides meaningful benefits for planning. The performance inversion (Random becoming easier than Mystery under TMK for o1) is an interesting and non-obvious pattern.

- **Experimental design addresses known criticisms of prior prompting work (Sections 3.2 and 5.1).** The evaluation follows the precautions identified by Stechly et al. (2024) and Bhambri et al. (2025): the one-shot example does not match the query problem, full plan validity is required (not just final-state matching), and the paper verifies that zero-shot plain text outperforms one-shot plain text (so the gain is not simply from having an example). This shows awareness of the methodological pitfalls that have undermined prior claims about LLM planning.

- **Detailed, reusable instantiation of the TMK framework (Figure 1, Section 3.1).** The paper provides a complete hierarchical decomposition of Blocksworld into Tasks, Methods, and Knowledge with preconditions, effects, and teleological links. This goes well beyond the action templates in CoT or ReACT and could serve as a reusable template for other planning domains.

## Weaknesses

### Major

- **Ambiguity about the extraction pipeline for Random Blocksworld (Section 3.2).** The paper states that it "added new code … to the extraction criteria which was applied for random blocksworld data set" to handle formatting artifacts (extra symbols, words like "object" or "from"). The enhanced extraction accepts plans whose action sequence and object order match the ground truth even if the surface form contains extra tokens. **However, the paper does not explicitly state whether the same relaxed extraction was applied to the plain-text baselines.** If the baselines for models like GPT-4, GPT-4o, and o1preview were taken directly from the Valmeekam (2023) leaderboard (which used the original, stricter extraction), while the TMK results used the relaxed extraction, then the accuracy comparison is confounded — TMK's apparent advantage could be partially or entirely an artifact of a more forgiving evaluation. The paper should at minimum disclose which baselines were recomputed and which were taken from prior work, and ideally re-run all baselines through the same extraction pipeline. Without this clarity, the quantitative comparisons in Table 2, particularly for Random Blocksworld, lack a clean evidential foundation.

### Minor

- **No control for structured format vs. TMK-specific content.** The paper attributes improvements to TMK's specific teleological decomposition (Tasks, Methods, Knowledge). But the prompt is a JSON-formatted hierarchical description of Blocksworld actions, and the gains could come from *any* sufficiently structured, code-like format (YAML, a pseudo-code list of pre/post-conditions, a flat PDDL-like description). Without a control condition that uses a similarly structured but non-TMK prompt, the paper cannot isolate TMK's specific architecture as the causal factor. This is a standard ablation that would sharply strengthen the contribution.

- **Mechanistic claims outrun the evidence (Sections 5.2.1, Abstract, Conclusion).** The paper repeatedly asserts that TMK "steers reasoning models away from their default linguistic modes to engage formal, code-execution pathways" and that the performance inversion is "empirical validation of this steering effect." These are strong mechanistic claims, but the paper provides no direct evidence: no analysis of model reasoning traces, no comparison of output token distributions, no ablation isolating the format from the content. The alternative explanation — that TMK simply provides clearer, less ambiguous task specifications — is equally consistent with the accuracy numbers. The mechanistic narrative should be presented as speculation or as a hypothesis for future work, not as a conclusion supported by the experiments.

- **Limited evaluation scope and missing statistical reporting.** The evaluation covers only the Blocksworld domain within PlanBench and only OpenAI models. The paper does not report the number of problems per domain, variance across runs, or confidence intervals for any result. While single-run evaluation on fixed problem sets is common practice in planning benchmarks, the absence of any uncertainty quantification weakens the reliability assessment, especially for borderline improvements (e.g., GPT-4o Mystery: 0% → 5.5%).

- **One-shot confound not fully controlled (Section 3.2).** TMK is evaluated with one-shot prompts while the plain-text baselines are the best of zero-shot and one-shot (often zero-shot). The paper argues convincingly that zero-shot outperforms one-shot for plain text in PlanBench, making this a conservative comparison. However, a direct zero-shot TMK experiment would have cleanly eliminated this concern. The argument is reasonable but indirect.

### Trivial

- None that survive filtering.

## Nice-to-Haves

- Evaluate TMK in zero-shot mode to remove the example confound entirely.
- Add a control condition with a structured but non-TMK prompt (e.g., a flat list of action signatures with pre/post-conditions, or a YAML equivalent).
- Test on a second PlanBench domain (e.g., Logistics) to demonstrate generalizability beyond Blocksworld.
- Report the number of problems per domain and ideally multi-seed runs or confidence intervals.

## Removed Points

The following points from the harsh critic were considered and removed with justification:

- **"The critical problem: there is no evidence that the same relaxed extraction was applied to the plain-text baselines... this is a structural flaw: without it, the accuracy numbers in Table 2 cannot be trusted, and the core empirical claim is unsupported."** — *Downgraded from Fatal to Major.* The concern is valid but the critic overstates its severity. The extraction changes handle formatting artifacts (extra symbols, alternate wording like "object" vs. "obj"). Even if the baselines were underestimated by a few points due to stricter extraction, the core result (o1: 31.5% → 97.3%) is a ~66-point gain that cannot be explained away by lenient extraction. The critic's framing as "fatal" and "decisive structural flaw" exceeds what the evidence supports.

- **"The paper never states whether these are single runs or averaged across seeds, nor provides confidence intervals. For results like GPT4o Mystery: 0→5.5, stochasticity could flip the conclusion entirely."** — *Downgraded from Major to Minor.* The concern about variance is valid, but for the main result (o1 Random: 31.5→97.3), stochasticity cannot flip the conclusion. The critic's example (GPT4o Mystery 0→5.5) uses the smallest delta in the table as if it were representative. Merged into the general "missing statistical reporting" point.

- **"The paper should state explicitly whether Classic and Mystery baselines were also re-evaluated with the same extraction."** — *Merged into the extraction issue (Major).* This is part of the same ambiguity.

- **"The abstract claims TMK 'functions not merely as context, but also as a mechanism that steers reasoning models...' This assertion appears before any evidence is presented, and the body never provides evidence for the mechanism."** — *Merged into the mechanistic overclaiming point (Minor).*

- **"The paper does not report which specific baseline was used for each model or whether the one-shot examples in those baselines were comparable in length to the TMK prompt."** — *Merged into the extraction/reporting point (Major).*

## Novel Insights

The most interesting observation from the reviews — beyond the paper's own contributions — is the tension between the "performance inversion" as an empirical finding and the strong mechanistic claims built on top of it. The inversion (Random becoming easier than Mystery under TMK for o1) is genuinely intriguing and worth highlighting, but it supports multiple interpretations. The review process surfaces the fact that the paper conflates the existence of this inversion with evidence for a specific internal mechanism (code-execution pathway activation), when in reality the inversion is equally consistent with several simpler explanations (e.g., that TMK provides better-structured task descriptions, or that the Random domain has more room for improvement from a lower baseline). This suggests the paper's most durable contribution is the empirical pattern itself, not the mechanistic interpretation.

## Suggestions

1. **Clarify the extraction pipeline.** Explicitly state whether each plain-text baseline in Table 2 was (a) taken directly from the Valmeekam leaderboard, (b) recomputed by the authors using the original extraction, or (c) recomputed using the same relaxed extraction as TMK. Ideally, re-run all Random Blocksworld baselines with the same extraction and report any differences.
2. **Add a structured control condition.** Test a non-TMK structured prompt (e.g., a flat list of action signatures in JSON or YAML format) to isolate whether TMK's specific teleological decomposition matters beyond just having a structured format.
3. **Scale back the mechanistic claims.** Present the performance inversion as an observed pattern and the code-execution hypothesis as speculation. The empirical contribution (TMK improves planning accuracy) stands on its own.
4. **Add zero-shot TMK results** to eliminate the one-shot confound directly.

## Score and Decision

**Round 1 bracketing**: The paper sits between the weak anchors (scores 2.0–3.0, papers that merely benchmark models without proposing new methods) and the strong anchors (scores 6.4–8.0, papers with well-controlled experiments and novel, validated methods). Initial bracket: 4.5–6.0.

**Round 2 narrowing**: Compared against specific anchors within this bracket:
- *"LLMs Can Plan Only If We Tell Them" (6.40, accept)* — This paper also works on Blocksworld with structured prompting and has better-controlled experiments (AoT+). The TMK paper has a more novel theoretical grounding (cognitive science) but weaker experimental controls. The TMK paper is weaker → below 6.40.
- *"Tree-Planner" (5.25, accept)* — Scores 3,5,8,5. Similar scope of contribution but better-controlled experiments. TMK paper is comparable but with weaker controls → around 5.0–5.5.
- *"Deliberate Reasoning as Structure-aware Planning" (5.50, reject)* — Similar methodological gaps (missing comparisons, unclear mechanism). TMK paper is comparable → ~5.0.
- *"Modular Agentic Planner" (4.50, reject)* — Rejected for lack of novelty despite reasonable results. TMK paper has clearer novelty → above 4.50.

**Final score**: 5.0. The paper has a genuine contribution (TMK prompting improves planning, with striking results on Random Blocksworld) and a well-motivated framework. However, the extraction pipeline ambiguity is a meaningful reporting gap, the lack of a structured control weakens the specificity of the contribution, and the mechanistic overclaiming undermines the overall presentation. With revisions addressing these issues, the paper could become a solid contribution; as submitted, it does not meet the acceptance threshold for a top venue.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>