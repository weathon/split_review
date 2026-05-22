Now I have a thorough understanding of the paper and calibration anchors. Let me write the final review.

---

## Summary

This paper investigates whether structuring LLM prompts using the Task-Method-Knowledge (TMK) framework — a knowledge representation formalism from cognitive science — improves planning performance on PlanBench's Blocksworld domain. The authors replace the natural-language domain description in PlanBench prompts with a JSON-encoded TMK specification that hierarchically decomposes actions into tasks (goals with pre/post-conditions), methods (mechanisms), and knowledge (domain ontology). Experiments across GPT-4, GPT-4o, o1-mini, o1, and GPT-5 show consistent improvements, with the most dramatic gain being o1 on Random Blocksworld: 31.5% → 97.3%. The paper also reports a "performance inversion" where TMK makes symbolic (Random) tasks easier than semantic (Mystery) tasks for reasoning models, and hypothesizes this reflects a shift from linguistic to code-like reasoning modes.

## Strengths

- **Genuinely novel interdisciplinary idea**: Applying the TMK framework from cognitive science and intelligent agent architectures to LLM prompt engineering is creative and, to my knowledge, unexplored. The paper makes a clear case for why TMK's explicit decomposition into tasks, methods, and knowledge might address known LLM planning deficiencies (Section 2.3).

- **Large, consistent empirical gains**: The TMK-structured prompt improves performance across all tested flagship models and Blocksworld variants (Table 2). The 65.8 percentage-point gain on o1 for Random Blocksworld (31.5% → 97.3%) is striking. GPT-5 also shows non-trivial improvement even from a high baseline (92.5% → 99.0% on Random).

- **Methodological care in addressing prior criticisms**: The paper takes concrete steps to avoid known pitfalls in prompting research: (a) the one-shot example does not match the target problem in length or block configuration, ruling out simple pattern matching; (b) evaluation requires every step of the reasoning trace to be correct, not just the final answer; (c) they demonstrate that zero-shot plain-text often outperforms one-shot plain-text on this benchmark, strengthening the case that TMK structure (not the extra example) drives the gains (Section 3.2).

- **Interesting performance inversion observation**: The reversal where o1 goes from better-on-Mystery (74.3%) to better-on-Random (97.3%) under TMK is a genuine empirical finding that resists trivial explanation. It plausibly indicates a shift in the model's processing strategy and invites further investigation (Section 4.2).

## Weaknesses

### Major

- **No control condition isolating TMK-specific structure from generic structured domain knowledge**: The paper compares TMK only against a plain-text natural-language domain description. It never tests a comparably structured but non-TMK format (e.g., a flat JSON list of actions with preconditions/effects, or a PDDL-like encoding without the teleological task-method linkage). The central claim — that TMK's specific teleological and causal decomposition drives the improvement — therefore lacks direct experimental support. Any structured, code-like encoding of the domain might produce similar gains. This is a structural gap in the evaluation design that weakens the paper's core contribution.

- **Absence of statistical rigor**: Table 2 reports point estimates with no confidence intervals, standard deviations, or information about multiple independent runs. Model outputs are stochastic; without replication and variance reporting, the reliability of even large numerical differences is uncertain. The footnote "Bold values indicate significantly improvements" is unsupported — no statistical test is described or conducted anywhere in the paper. For an empirical paper making comparative performance claims, this is a significant omission.

- **Potential baseline extraction inconsistency for older models**: The paper modified PlanBench's extraction code for Random Blocksworld to handle formatting artifacts (Section 3.2). However, the plain-text baselines for GPT-4 and GPT-4o appear to be taken from the PlanBench leaderboard (Valmeekam, 2023), which used the original extraction code. The paper does not clarify whether these baselines were re-run with the improved extraction. While this primarily affects models where both plain-text and TMK scores are near floor (GPT-4: 0% → 4.17%; GPT-4o: 0.83% → 4.83%), the inconsistency undermines the rigor of those specific comparisons.

### Minor

- **Gap between TMK's aspirational framing and what is demonstrated**: The paper emphasizes TMK's unique ability to capture "why" actions are taken (teleology) and distinguishes it from HTN and BDI on this basis (Section 2.3). But the TMK encoding shown (Figure 1) largely consists of preconditions, effects, and a mechanism link — structures that are also present in standard hierarchical domain encodings. The practical difference between TMK and a well-structured domain specification is asserted rather than demonstrated. The conceptual framing outpaces the experimental evidence.

- **Interpretive claims sometimes presented as conclusions rather than hypotheses**: While the paper hedges in several places ("we hypothesize," "it is feasible that," "this should be tested in future work"), other sections present the code-steering mechanism as an established finding. The abstract states TMK "steers reasoning models away from their default linguistic modes to engage formal, code-execution pathways" as though verified. The Discussion (Section 5.2.1) says "the prompt successfully steers the model out of the semantic interference zone and into a robust symbolic manipulation zone." Without access to reasoning tokens, attention patterns, or any direct test of this mechanism, these claims should be presented as interpretations requiring further validation, which the paper itself acknowledges in the conclusion ("the cause of that increase is left to future work").

- **The o1-mini regression on Mystery is discussed but not explained**: TMK causes o1-mini to drop from 19.1% to 16.83% on Mystery. The paper attributes this to "capacity limitations" and "semantic overload" (Sections 4.2, 5.3), but these explanations are post-hoc and not tested. This outlier is flagged honestly but weakens the claim that TMK consistently helps.

### Trivial

- "Significantly improvements" in Table 2 caption is a grammatical error and should be "significant improvements."

## Nice-to-Haves

- Adding a structured non-TMK control condition (e.g., flat JSON action specification with preconditions/effects) would substantially strengthen the paper's core claim and is the single highest-leverage improvement.
- Extending evaluation to open-weight models where reasoning tokens are accessible would allow direct testing of the code-steering hypothesis.
- Reporting accuracy over multiple independent runs with standard deviations and appropriate significance tests would bring the evaluation up to expected empirical standards.

## Removed Points

These points from the harsh critic were considered but removed or demoted:

- **"Performance inversion relies on a single model, single domain pairing"**: Removed. The inversion pattern is observed across o1, o1-mini, and GPT-5 (albeit most dramatically in o1). The harsh critic's claim of "a single model, a single domain pairing" is factually incorrect — GPT-5 also shows larger gains on Random (92.5% → 99.0%) than Mystery (98.1% → 98.3%).

- **"The TMK is a flat specification of individual actions"**: Removed. Figure 1 clearly shows a hierarchical decomposition with tasks linked to methods via a Mechanism field. The harsh critic's characterization as "flat" is inaccurate.

- **"Plain-text one-shot data missing from main paper"**: Demoted. The paper explicitly addresses why they compare against zero-shot baselines (Section 3.2) and references the one-shot data in their OSF repository. This is a reasonable reporting choice, not a flaw.

- **"The o1-preview results in Table 2 are confusing"**: Removed. The footnote clearly notes o1-preview has been deprecated and replaced by o1. Including these as reference points is reasonable.

- **"SoTA has moved; 2.8 percentage point improvement over o1's plain-text 95.7% could be noise"**: Partially removed. The claim about "SoTA has moved" is a reviewer knowledge claim not grounded in the paper. The noise concern is folded into the statistical rigor weakness above rather than kept as a separate point.

- **Various formatting/style nitpicks**: Removed per hard rules.

## Novel Insights

The most interesting finding in this paper — and one the reviewers independently converged on — is the performance inversion pattern: under TMK prompting, models shift from being better at semantically cued (Mystery) tasks to being better at purely symbolic (Random) tasks. This is a genuine empirical phenomenon that cannot be trivially explained as "more context helps." If replicated with proper controls, it would constitute evidence that prompt structure can qualitatively shift a model's inference mode, which has implications beyond planning for how we design LLM interfaces. The paper's hypothesis linking this to code-trained reasoning pathways is speculative but directionally interesting and worth pursuing with models that expose internal reasoning tokens.

## Suggestions

1. **Add a structured non-TMK control**: A flat JSON encoding of the same domain information (actions with preconditions/effects, no task-method-knowledge hierarchy) would directly test whether TMK's specific structure matters or whether any structured format produces the gains. This is the single most important experiment to add.

2. **Report statistics**: Run 5–10 independent evaluations per condition, report means with standard deviations, and conduct appropriate significance tests. Replace "bold values indicate significantly improvements" with actual statistical evidence.

3. **Clarify baseline provenance**: Explicitly state which plain-text baselines were re-run with the improved extraction code and which come from the leaderboard. Ideally, re-run all baselines with consistent extraction.

4. **Tone down mechanistic claims**: Reframe the code-steering discussion (Section 5.2.1) as a hypothesis supported by circumstantial evidence, not as a validated finding. The paper already acknowledges this in the conclusion — make the language consistent throughout.

5. **Expand domain coverage**: Blocksworld alone is a narrow testbed. Even one additional PlanBench domain (e.g., Logistics) would substantially strengthen generalizability claims.

## Score and Decision

### Calibration anchor comparison (all rounds):

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| jOuHjFw71C ("Planning in Strawberry Fields") | 3.00 | R1 | Pure o1 evaluation; this paper proposes a novel method and is clearly stronger |
| OPdmIxdkPb ("Query-Efficient Planning with LLMs") | 4.75 | R1 | Simple idea, overclaimed; this paper has a more novel interdisciplinary contribution |
| Sc382pFw86 ("Structure-aware Domain Knowledge Injection") | 5.25 | R2 | Similar tier: novel idea from cognitive/educational science, evaluation concerns; comparable |
| BaMkS6E2Du ("Deliberate Reasoning for LLMs") | 5.50 | R2 | Structured reasoning framework, unclear methodology; this paper has cleaner results but similar evaluation gaps |
| pRIPRDALBV ("Open-World Planning via Lifted Regression") | 5.50 | R2 | Different domain (embodied agents); this paper's evaluation is narrower but results are more dramatic |
| K3KrOsR6y9 ("LLMs Can Plan Only If We Tell Them") | 6.40 | R1/R2 | AoT+ prompting; more thorough methodology with ablations and multiple benchmarks; this paper is clearly weaker on evaluation rigor |
| NUD03NBDOE ("ActionReasoningBench") | 6.75 | R2 | New benchmark contribution; stronger contribution |

**Round 1 bracket**: 4.5 – 6.5 (clearly above the 3.0 evaluation-only paper, below the 7.5+ strong-accept tier).

**Round 2 narrowing**: The paper sits near the 5.25–5.50 region. It has a more novel idea and cleaner results than the 5.25 "Structure-aware Domain Knowledge Injection" paper but shares similar evaluation rigor concerns. It is clearly below the 6.40 AoT+ paper, which has more thorough ablations, multiple benchmarks, and proper experimental methodology. Score: **5.0**.

The paper presents a genuinely interesting idea with impressive headline results, but the evaluation gaps — absence of a structured control condition, lack of statistical measures, and potential baseline extraction inconsistencies — prevent the evidence from fully supporting the paper's specific claims about TMK's unique value. The paper would benefit substantially from addressing these gaps before publication.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>