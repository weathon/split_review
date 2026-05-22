Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper applies the Task-Method-Knowledge (TMK) framework—a structured knowledge representation from cognitive science—to prompt design for LLMs on planning tasks (PlanBench Blocksworld). By replacing the plain-text domain description with a hierarchical JSON structure encoding tasks, methods, and knowledge (including teleology / "why"), the authors report substantial accuracy gains across several OpenAI models. The headline result: o1 goes from 31.5% to 97.3% on Random Blocksworld, an inversion where opaque symbolic tasks become easier than semantically labeled ones under TMK prompting.

## Strengths

1. **Dramatic and robust empirical results on Random Blocksworld.** The o1 improvement from 31.5% to 97.3% (Table 2) is striking. This is the paper's strongest contribution—it shows that structured prompting can unlock near-perfect planning performance on a challenging symbolic variant where standard prompting fails. The effect also generalizes to GPT-5 (92.5% → 99.0%).

2. **Identification of the performance inversion phenomenon.** The inverted difficulty ordering (Random > Mystery under TMK for o1) is a genuinely interesting behavioral finding. Whether or not the paper's mechanistic interpretation is correct, this observation warrants attention and could motivate future work on how prompt structure interacts with reasoning modality.

3. **Concrete, reproducible TMK design and careful addressal of known criticisms.** The TMK decomposition for Blocksworld is fully specified (Figure 1) and the one-shot example is explicitly non-matching (random, not tailored to the test problem). This directly addresses the pattern-matching concern raised by Stechly et al. (2024) and Bhambri et al. (2025) about prior prompting work—the improvement cannot be explained by example similarity.

4. **Novel cross-disciplinary framing.** Bringing TMK from cognitive science and educational applications into LLM prompting is a creative and well-motivated connection. The paper correctly identifies that TMK's emphasis on teleology (the "why" of actions) goes beyond what frameworks like HTN and BDI provide.

## Weaknesses

### Fatal
None.

### Major

1. **No ablation isolating TMK structure from content.** The paper replaces the plain-text domain description with TMK JSON. There is no control condition where an equivalently detailed domain description is presented in natural language prose (same information, same length, without the TMK formatting). Without this, it is impossible to attribute the gains to TMK's hierarchical/teleological structure versus: (a) simply providing more explicit/redundant information, (b) the JSON format triggering code-execution pathways, or (c) the added length and structure providing better formatting guidance. This gap directly undermines the paper's central claim that TMK acts as a "symbolic steering mechanism"—the experiments do not isolate what drives the improvement. The absence of "ablation" from the paper confirms this gap was unaddressed.

2. **The central mechanistic claim (code-execution pathway steering) is speculative and unsupported by direct evidence.** Section 5.2.1 hypothesizes that TMK's JSON structure "activates formal reasoning pathways" from code training data, but no empirical evidence is provided: no internal representation analysis, no attention or logit analysis, no test with transparent-reasoning models, and no comparison of TMK outputs against code-language perplexity. The reference to Chen et al. (2024) is invoked as support, but that work studies a different setup (plain-text vs. code-based execution for optimization) and does not directly support the claim that JSON-structured prompts engage code-execution pathways. The performance inversion (Section 4.2) is presented as "empirical validation of this steering effect," but alternative explanations exist (e.g., Mystery words conflict with the rigid JSON structure, or Random tokens present no semantic interference to distract from the TMK scaffold). The paper's own conclusion language ("We theorize," "It is feasible that," "This should be tested...as part of future work") appropriately hedges, but the abstract and introduction present this as a finding rather than a hypothesis.

3. **Ambiguity about whether the modified extraction function was applied uniformly.** The paper states it "added new code to the extraction criteria which was applied for random blocksworld data set" and that an "enhanced extraction function prevents [stochastic artifacts] from getting evaluated as incorrect." This modification is reasonable in principle (handling irrelevant surface-form variation), but the paper does not explicitly state whether the same extraction was applied to both plain-text and TMK conditions. If the plain-text baselines for newer models (o1, GPT5) used a different extraction than the TMK results, the gains could be partially artifactual. This needs clarification; as written, the comparison is not fully verifiable.

### Minor

1. **Limited domain scope.** The paper only tests Blocksworld (with its three label variants) from PlanBench. The limitations section (5.3) acknowledges this, but the title and abstract discuss "planning tasks" in general. Without at least one additional domain (e.g., Logistics), the generalizability claim is unsupported.

2. **No statistical significance or variance reporting.** Table 2 reports single percentage values. The paper does not specify the number of problems per condition, runs, or confidence intervals. Given the small number of test problems in PlanBench Blocksworld, some of the smaller gains (e.g., GPT4 Classic: 34.6% → 39.7%) may not be statistically reliable.

3. **o1-mini anomaly is noted but not explained.** The paper correctly reports that o1-mini's Mystery performance drops under TMK (19.1% → 16.83%). This is an important boundary condition for the claimed steering effect, but the paper only offers a vague "semantic overload" hypothesis without analysis.

### Trivial
None.

## Nice-to-Haves

- An error categorization analysis: when TMK fixes plain-text failures, what kind of errors does it eliminate (hallucinated actions, precondition violations, non-termination)?
- Validation that the TMK JSON correctly encodes all preconditions and effects for the Random labels.
- Reporting the plain-text zero-shot and one-shot values separately rather than as "best of sampled" would increase transparency.

## Removed Points

- **One-shot TMK vs. zero-shot plain-text comparison (critic's fatal claim):** The harsh critic asserted that TMK (one-shot) is compared against baselines from "a separate zero-shot evaluation pipeline," invalidating all quantitative comparisons. This is contradicted by the paper: Table 2's caption explicitly states "plain-text prompts (best of sampled Zero & One shot)," and Section 3.2 notes the authors "ran the PlanBench benchmark for newer models" themselves. For the headline results (o1, GPT5), the plain-text baselines are the authors' own runs. Only o1preview values are extracted from the public leaderboard. The critic's characterization of this as "fatal" and requiring "the entire experimental design to be re-executed" is inaccurate.

- **Extraction modification inflates gains (critic's "evidential issue" framing as fatal):** The paper states the enhanced extraction was "applied for random blocksworld data set" (the dataset, not a condition). This language suggests uniform application, though the paper is ambiguous. The critic's stronger claim—that "the gains cannot be attributed to TMK" because of this—overstates what can be concluded from the available text. Kept as a Major weakness above (ambiguity), but not fatal.

- **Performance inversion has simpler explanation (critic's Section 4.2 note):** The critic's alternative explanation (Mystery words "interfere with the rigid JSON structure") is actually compatible with the paper's own discussion. The paper already acknowledges that Mystery vocabulary creates "semantic interference" and that o1-mini's degradation is due to "capacity limitations in resolving [this] conflict." This is a discussion point, not a weakness.

- **Section-by-section nitpicks about missing appendix content, related work, and format:** Removed per instructions.

- **"Statistical significance and variance" from Missing Experiments:** Demoted to Minor since single-run evaluation is common practice in this benchmark line of work, but still worth noting.

- **Missing experiments about other domains or models:** Kept as Minor (domain scope) since the paper explicitly scopes to Blocksworld.

## Novel Insights

The most novel observation emerging from the reviews is that the performance inversion (Random > Mystery) is itself interesting enough to motivate future work regardless of the paper's mechanistic interpretation. If TMK's effect is "simply" providing better redundant information, that is still a practically useful finding. If it genuinely shifts how models process the prompt (code-like pathways), that is scientifically significant. The reviews converge on the point that the paper would benefit from pitting these explanations against each other experimentally rather than arguing for one.

## Suggestions

1. Add a natural-language control: an equivalent-length, equivalent-information paragraph describing actions, preconditions, and effects without TMK/JSON structure. If TMK still outperforms this, the structure matters.
2. Clarify explicitly whether the same extraction function (original vs. enhanced) was applied to both plain-text and TMK conditions for Random Blocksworld.
3. Report the plain-text zero-shot and one-shot values separately so the reader can verify the claim that zero-shot is better.
4. Provide variance information (number of problems, bootstrap intervals) for at least the headline o1 results.
5. Tone down the mechanistic claim from a finding to a hypothesis, consistent with the paper's own hedging in Section 5.

## Score and Decision

The paper has a genuine empirical contribution: TMK prompting produces large and practically meaningful improvements on PlanBench Blocksworld, particularly for Random variants where o1 jumps from 31.5% to 97.3%. This result appears robust even accounting for the extraction ambiguity. However, the paper's central interpretive claim—that TMK steers models toward code-execution pathways—is not supported by the experiments, and the absence of a content-matched control makes it impossible to know what drives the gain. The paper would benefit from repositioning its contributions around the empirical finding and the performance inversion phenomenon rather than the speculative mechanism.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>