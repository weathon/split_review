Now I have sufficient anchor data. Let me synthesize everything and write the final review.

**Round-1 bracket:** Based on calibration search, I placed the paper between 3.5 and 6.5.

**Round-2 narrowing:** Comparing to anchors, the paper sits above "Do Think Tags" (avg 4.0, withdrawn/reject) due to better novelty and more striking results, but below well-executed papers with rigorous ablations like "Planning Anything with Rigor" (avg 4.75, accepted poster). The paper's interdisciplinary novelty and impressive raw results are counterbalanced by the absence of a content-vs-format ablation control and extraction methodology ambiguity. Final score: **4.5**.

Here is my consolidated review:

---

## Summary

This paper introduces TMK (Task-Method-Knowledge)—a knowledge representation framework borrowed from cognitive science—as a structured JSON prompt to improve LLM planning performance on the PlanBench Blocksworld benchmark. The key finding is that TMK-structured prompting produces large accuracy gains, most strikingly for o1 on the opaque Random Blocksworld variant (31.5% → 97.3%), along with a performance inversion where symbolic tasks become easier than semantically-cued ones under TMK. The paper attributes this to TMK acting as a "symbolic steering mechanism" that shifts models from linguistic approximation toward code-like formal reasoning.

## Strengths

1. **Novel interdisciplinary transfer.** Bringing the TMK framework from cognitive science/education into LLM prompting is a genuinely creative contribution. The paper grounds this transfer in prior work on TMK for procedural learning, offering a well-motivated alternative to CoT/ReACT-style methods.

2. **Striking raw results with a clean inversion pattern.** Table 2 documents that o1 rises from 31.5% to 97.3% on Random Blocksworld—a 65.8 percentage-point gain. More importantly, Section 4.2 documents a clean *performance inversion*: under plain text, o1 scores Mystery (74.3%) > Random (31.5%); under TMK, Random (97.3%) > Mystery (83.3%). This reversal is harder to explain by simple context enrichment than by a shift in reasoning modality, lending real support to the paper's core hypothesis.

3. **Explicit handling of known criticisms.** Section 5.1 directly addresses three common criticisms of prior prompting work (pattern-matching from similar n-shot examples, evaluating only the final answer, and zero-shot-only demonstrations). The paper shows that (a) the one-shot example is random and not tailored to the query, (b) the entire plan sequence is validated, and (c) zero-shot plain text often outperforms one-shot plain text—isolating the TMK structure as the source of gains.

4. **Concrete, reproducible prompt design.** Figure 1 and Section 3.1 provide a full hierarchical TMK decomposition serialized in JSON, with Tasks (goals/preconditions/effects), Methods (mechanisms with requires/provides/process), and Knowledge (concepts/relations). This enables direct replication and extension.

## Weaknesses

### Fatal
None.

### Major

1. **No ablation to distinguish TMK content from structured formatting.** The paper claims that TMK's specific task-method-knowledge decomposition drives the improvements, but presents no control condition that separates content from format. The TMK prompt is a structured JSON; the plain-text baseline is unstructured natural language. Any structured JSON—even one with randomly shuffled keys or a trivial attribute-value list—could plausibly produce gains by imposing format discipline. Without a content-control condition (e.g., the same JSON structure with semantically empty or irrelevant content), the central attribution to TMK's teleological and hierarchical decomposition is unsubstantiated. This is the most significant gap in the experimental design.

2. **Modified extraction pipeline without validated comparability.** Section 3.2 states that the Valmeekam (2023) code "required update" for Random Blocksworld extraction and that the authors added new extraction code. The paper does not establish that the modified extraction produces equivalent results to the official pipeline on a shared subset of problems. Since plain-text baselines for some models are drawn from the leaderboard (which used the original extraction), while TMK results used the modified extraction, it is unclear whether the reported gains reflect improved planning or a relaxed evaluation standard. For the headline o1 result (31.5% → 97.3%), the baseline was likely from the authors' own runs and thus uses the same extraction, but the paper should state this explicitly.

### Minor

1. **No variance or reliability metrics.** All results in Table 2 are single numbers per condition. LLM outputs can be stochastic, and the paper does not report temperature settings, number of runs, confidence intervals, or standard deviations. While single-run evaluation is common on the PlanBench leaderboard, the paper's central claim about *performance inversion* rests on the difference between two single numbers (31.5% vs. 97.3% and 74.3% vs. 83.3%), and the reliability of these measurements is unknown.

2. **Rhetoric–content gap on the "why" dimension.** The paper emphasizes that TMK uniquely captures "why" actions are taken (teleology), distinguishing it from HTN and BDI frameworks. However, the actual TMK prompt shown in Figure 1 encodes standard PDDL-style preconditions and effects (Given/Makes, Requires/Provides). There is no explicit teleological reasoning step or "why" explanation separate from the action semantics. The paper should clarify how the prompt operationalizes the teleological claim, or temper the rhetoric to match what the prompt actually contains.

3. **Ambiguous baseline provenance.** The caption of Table 2 states "Plain Text (%)" is "best of sampled Zero & One shot" and that o1preview results are "extracted from Valmeekam (2023)." For GPT-4, GPT-4o, o1-mini, o1, and GPT-5, it is not explicitly stated which baselines were re-run by the authors with the same extraction pipeline and which were taken from the leaderboard. This makes it difficult for readers to assess the fairness of individual comparisons.

## Nice-to-Haves

- A controlled experiment comparing TMK-JSON to a JSON with the same nesting but randomized keys, or to a simple bullet-list of PDDL rules, would directly test whether TMK's specific decomposition is the active ingredient.
- Re-running all baseline models with the authors' extraction code and reporting zero-shot and one-shot separately for every model would eliminate the baseline comparability concern entirely.
- Reporting the exact number of test instances per variant and whether the same set was used across all conditions would improve transparency.
- Analyzing failure modes (what plans does TMK cause the model to generate when it does err?) could inform the code-execution hypothesis.

## Removed Points

These points are flagged to be removed, treat them with caution:

- "The o1 baseline on Random (31.5%) is lower than o1-preview (37.3%)"—different model families can have different strengths; this is not inherently problematic and is not presented as a central comparison.
- "o1-mini regression on Mystery is not explored"—the paper acknowledges this result and offers a hypothesis (capacity limitations in semantic interference); leaving full exploration to future work is reasonable.
- "No comparison to PDDL domain directly"—scoped outside the paper's experiments; could strengthen but is not a flaw in the current scope.
- "No analysis of failure cases"—a nice-to-have, not a weakness in the current analysis.
- "Missing multiple runs" downgraded from critical to minor because single-run evaluation is the PlanBench norm and the paper's main claims (inversion pattern, large gains) are robust even to modest variance.

## Novel Insights

None beyond the paper's own contributions. The reviews primarily surface known categories of concern (ablation controls, evaluation fairness, statistical grounding) that apply across many LLM-prompting papers rather than revealing something unique about this work.

## Suggestions

1. Add a content-control condition: present the same Blocksworld domain in a structurally identical JSON but with TMK-specific content replaced (e.g., by recipe descriptions or random key-value pairs). If TMK-specific gains persist, the effect is attributable to format; if they disappear, TMK content is the driver.
2. Clarify for every model in Table 2 whether the plain-text baseline was run by the authors or taken from the leaderboard, and confirm that the same extraction pipeline was used for both conditions.
3. Run each condition with at least 3–5 seeds (or, if temperature=0, state this explicitly) and report means or ranges.
4. Add a brief description of how the TMK prompt operationalizes the "why" (teleological) dimension that the paper emphasizes in its framing but does not illustrate in the prompt example.

## Score and Decision

My round-1 bracket (calibration_search with banded queries) placed the paper between 3.5 and 6.5. Round-2 narrowing compared against four anchors in the middle band:

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| "Do Think Tags Really Help LLMs Plan?" | 4.00 | R2 | Stronger experimental design (systematic ablations) but less novel findings. Our paper has a more creative contribution but weaker controls. Our paper is somewhat stronger overall. |
| "Planning Anything with Rigor" (accepted poster) | 4.75 | R2 | Stronger empirical methodology with ablations and clear evaluation. Our paper has a more novel interdisciplinary approach but lacks the same rigor. Comparable but slightly weaker. |
| "Query-Efficient Planning with Language Models" | 4.75 | R2 | Mixed reviews (5,8,3,3). Strong empirical work with clear framing but novelty questioned. Our paper has more novel approach but weaker experiments. Comparable. |
| "SciBench" (rejected) | 5.60 | R2 | Comprehensive benchmark with mixed reviews (3-8). Broader scope but less focused contribution. Different paper type; our paper is slightly weaker in overall assessment. |

Based on these comparisons, the paper is stronger than a typical 3-range reject but not as strong as a 5+ accept, primarily due to the missing content-vs-format ablation and extraction comparability concern. The interdisciplinary novelty and striking inversion pattern push it above purely negative papers, but the experimental gaps prevent acceptance.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>