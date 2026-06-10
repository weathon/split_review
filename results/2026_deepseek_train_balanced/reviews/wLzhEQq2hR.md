## Summary

This paper investigates whether LVLMs (GPT-4V, GPT-4o, Gemini 1.5 Pro) genuinely understand diagrams, or whether their apparent success is an artifact. The authors design a test suite of synthetic and real diagrams spanning six domains, decompose diagram understanding into entity and relation sub-tasks, and further split these into recognition (NRQ) and counting-based reasoning (NCQ) questions, as well as knowledge-free (KFQ) and knowledge-required (KRQ) variants. The core empirical contribution is a controlled demonstration that all three models reliably identify and count entities (>90% accuracies with CoT) but struggle substantially with relations (~60–70% recognition, ~40–66% counting on synthetic diagrams). The paper further argues that the unexpectedly better relation performance on real diagrams is driven by knowledge shortcuts rather than genuine relational parsing.

## Strengths

- **Clean decomposition of diagram understanding into entity vs. relation sub-tasks.** The paper constructs synthetic diagrams where entity recognition and relation recognition can be independently measured, and achieves near-ceiling entity accuracy (>95% for text, >88% for visual with CoT) while relation accuracy lags at ~68–70% for explicit relations (Table 3). This controlled decomposition cleanly demonstrates that the bottleneck in diagram understanding is relational, not perceptual — a finding that goes beyond aggregate benchmark scores in prior work.

- **Converging multi-pronged evidence pointing toward a knowledge-shortcut mechanism.** Three independent quantitative patterns corroborate each other: (a) knowledge-grounded synthetic diagrams improve relation recognition by +15.44% (ZS) over semantically random diagrams (Table 5); (b) KRQ relation questions outperform KFQ relation questions by +11.13% (CoT) on real diagrams (Table 7); (c) the complexity analysis (Figure 5) shows relation accuracy falls from ~84% to ~51% as entity count increases, while entity accuracy stays flat, explaining the apparent real-diagram success as an artifact of simpler diagrams. The convergence across three distinct experimental designs strengthens the plausibility of the hypothesis.

- **Complexity analysis that resolves an otherwise puzzling contradiction.** The paper resolves the apparent paradox that models appear better at relations in complex real diagrams than in simple synthetic ones. By binning diagrams by entity count (Figure 5), the authors show that real-diagram relation performance is driven almost entirely by simple diagrams (≤4 entities, ~84–88% accuracy), collapsing to ~51% for complex diagrams — a result that cleanly reconciles Observations 2 and 3 and is the paper's most novel analytical contribution.

- **Case study providing a striking qualitative illustration.** Removing all relations from a food-web diagram and replacing them with random ones causes GPT-4o to give the same answers as on the original diagram (Section 5.2). This single-case demonstration vividly illustrates what the knowledge-shortcut mechanism looks like in practice, even if it does not constitute scalable evidence on its own.

## Weaknesses

### Fatal
None.

### Major

- **The headline knowledge-shortcut claim is supported by correlational evidence with plausible confounds that are not adequately addressed.** The paper asserts that models "*simply retrieve relevant pre-learned knowledge*" (line 68) and that their diagram reasoning performance is "*an illusion*" (line 10), but the causal mechanism is not convincingly established.
  * **Knowledge-grounded synthetic diagrams (Table 5):** Relations are assigned based on Word2Vec similarity > 0.5 between entity labels (line 305). This creates a selection bias — entities in knowledge-grounded diagrams are semantically coherent (animals with animals, objects with objects), which likely produces more conventional and predictable visual layouts. The improvement may partly reflect easier visual structure, not just knowledge retrieval. The paper does not control for this or discuss it as an alternative explanation.
  * **KRQ vs. KFQ comparison (Table 7):** KRQ relation questions (e.g., "Which is not the predator of Krill?") and KFQ relation questions (e.g., "Which entity is connected to Fish?") differ in question specificity and answer-space constraints, not just knowledge requirement. The KRQ question is inherently more constrained and cues a specific semantic schema, which could aid visual search independent of knowledge retrieval. The paper does not control for this confound.
  * **Case study (Section 5.2):** The manipulation is compelling but involves a single diagram from a single model (GPT-4o). The paper generalizes this to all LVLMs and all diagram types without addressing the n=1 limitation.

  Individually each of these three pieces is only suggestive; the paper would benefit from at least one controlled experiment that directly manipulates the *conflict* between visual relations and knowledge (e.g., diagrams where arrows contradict commonsense, tested at scale) to strengthen the causal inference.

- **The "reasoning" tasks are counting tasks, which inflates the entity-reasoning claim.** NCQ (Number Counting Questions) ask "how many" — counting entities or relations (line 94). While counting requires systematic enumeration, the paper consistently labels this as "*reasoning*" (lines 28–29, 209–211), invoking Kahneman's slow System 2. The finding that models achieve 98.46% on entity counting with CoT is presented as evidence that they can "*reason about entities*" (Observation 1). This conflates procedural counting with the multi-step logical inference that "reasoning" typically implies. Since the relation side of the dichotomy uses the same task type (NCQ), the comparison is fair *within* the paper's framing — but the strong claim that models possess entity-reasoning capabilities is overstated. The paper would be more precise to relabel NCQ as "counting" and reserve "reasoning" for genuinely multi-step relational tasks (e.g., transitive inference).

### Minor

- **No measure of uncertainty or statistical significance reported for any experimental result.** Every accuracy in every table is a single point estimate with no confidence intervals, standard deviations, or significance tests. For a benchmark/empirical paper where the narrative hinges on comparing conditions (e.g., synthetic vs. real, KFQ vs. KRQ, knowledge-grounded vs. vanilla), the absence of any statistical framing is a meaningful gap. With 1,000 synthetic diagrams and 1,001 real diagrams, the standard errors are small enough that the main gaps are likely robust, but the reader cannot assess this from the paper itself. Reporting CIs or bootstrapped error bars (especially in Figure 5) would substantially strengthen credibility.

- **Severe domain imbalance in the real-diagram set is not discussed as a limitation.** Of the 1,001 real diagrams, 462 (46%) are from ecology (Table 2, line 162), while physics has 77 and chemistry has 54. Ecology diagrams (food chains, food webs) involve highly stereotyped relational structures that align closely with commonsense knowledge about predation. The paper's central knowledge-shortcut findings may be driven primarily by the ecology subset, and it is unclear whether the conclusions hold for domains where relational structures are less aligned with everyday knowledge (e.g., circuits, water cycles). Domain-specific breakdowns of results should be reported in the main paper rather than deferred to the appendix.

- **Knowledge grounding helps relation recognition but not relation counting — this asymmetry is not discussed.** In Table 5, knowledge-grounded diagrams improve NRQ (recognition) by +15.44% (ZS) but leave NCQ (counting/reasoning) essentially flat (+2.56% ZS, with Gemini actually decreasing). If knowledge shortcuts were the primary mechanism, one would expect them to help both tasks. This asymmetry is interesting and potentially informative about the nature of the shortcut, but the paper reports the numbers without analysis.

- **The "entity reasoning" label (Observation 1) is inconsistent with the paper's own more measured later language.** Line 213 acknowledges that the entity task involves "*simple object detection and count objects*" — which is more accurate than "reasoning about them." This discrepancy between the bold Observation 1 and the more careful phrasing in the body suggests the paper should either rename the tasks or adjust the observational claims.

### Trivial

- The complexity analysis (Figure 5) plots line graphs without error bars or confidence bands, making it impossible to assess whether the observed declines are statistically reliable, especially given the varying bin sizes (≥100 per bin but not necessarily equal).

## Nice-to-Haves

- A large-scale controlled experiment with deliberately misleading visual relations that contradict commonsense knowledge (e.g., water flowing uphill, smaller fish eating larger fish) would directly test the knowledge-shortcut hypothesis at scale. The current n=1 case study is illustrative but not probative.
- Disentangling question format from knowledge requirement in the real-diagram KFQ vs. KRQ comparison by holding the visual search structure constant while varying only the knowledge component.
- Defining chance baselines explicitly. For a 4-option MC format, random chance is 25%. Some reported accuracies (e.g., GPT-4V implicit spatial counting at 30.36% in Table 3) are near chance, which sharpens the interpretation.

## Removed Points

These points were flagged in input reviews but are removed or demoted per the filtering rules:

- **Missing Related Work section** — REMOVED per instruction (do not note missing related works).
- **Missing Limitations section** — REMOVED: the conclusion serves as brief discussion; this is a structural observation, not a substantive weakness.
- **"The paper does not highlight the favorable conditions for relation testing"** — REMOVED: this is a presentation preference, not a flaw; the paper's design choice of text-only entities for relation experiments actually strengthens its conclusions.
- **Several Strength Finder claims were overly assertive or generic** — REMOVED: the strength about the case study being "the single most important piece of evidence" overstated what the paper itself presents as a qualitative demonstration.
- **The "strengthening the paper on its own terms" suggestions from the harsh critic** — MOVED to Nice-to-Haves as they describe alternative experimental designs, not flaws in the current paper.
- **Criticism that the KRQ/KFQ comparison confounds knowledge with question specificity** — KEPT (as a Major weakness, see above) because it is a concrete, verifiable issue with the experimental design, not speculation.
- **Speculation about "the model might be better because the question narrows visual search"** — This is framed as an alternative explanation for a verified confound, not speculation. KEPT in Major.

## Novel Insights

The reviewers surface a pattern that the paper itself under-analyzes: the knowledge-shortcut effect is concentrated in *recognition* (NRQ) but not *counting* (NCQ), across both the knowledge-grounded synthetic experiment (Table 5, +15.44% NRQ vs. +2.56% NCQ) and the real-diagram KRQ/KFQ comparison (Table 7, +11.13% NRQ vs. +2.40% NCQ). This asymmetry is consistent across all three models and both experimental paradigms, yet the paper mentions it only in passing. If knowledge shortcuts were the sole or dominant mechanism, one would expect them to benefit both task types. The fact that they systematically benefit only recognition suggests either (a) the shortcut operates at a shallow level (retrieving which relations *exist* without encoding their structure well enough to count them), or (b) counting relations requires genuine visual parsing even when recognition can be shortcut. This pattern is worth deeper investigation and could inform a more nuanced theory of what LVLMs are actually doing when they "understand" diagrams. None beyond the paper's own contributions.

## Suggestions

1. **Tone down the "illusion" language** to match the strength of the evidence. The entity-relation gap is robust; the knowledge-shortcut causal claim needs more careful hedging.
2. **Add confidence intervals or bootstrapped standard errors** to all accuracy tables and to the complexity analysis figure.
3. **Report domain-specific breakdowns** for real-diagram results in the main paper, not just in the appendix.
4. **Run a "contradictory-knowledge" experiment at scale** (e.g., synthetic diagrams where arrows contradict commonsense) to provide a cleaner causal test of the shortcut hypothesis.
5. **Rename or clarify the NCQ tasks** — either call them "counting" directly or acknowledge that they are a limited proxy for reasoning, and add at least one genuinely multi-step relational reasoning task (e.g., transitive closure) to support the entity-reasoning claim.

---

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>