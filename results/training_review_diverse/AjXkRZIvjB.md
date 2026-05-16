Now I have all the information I need. Let me produce the consolidated final review.

## Summary

This paper introduces GSM-Symbolic, a template-based benchmark generation framework that creates multiple instantiations of GSM8K questions by varying names and numerical values while preserving the reasoning structure. Using this framework on 25 LLMs, the paper demonstrates that (1) model performance on a single static test set is unreliable and should be viewed as a distribution with noticeable variance, (2) performance on the original GSM8K often appears as an optimistic outlier consistent with contamination, (3) models are more robust to name changes than numerical changes, (4) performance degrades and variance increases with more clauses, and (5) adding a single irrelevant clause (GSM-NoOp) causes catastrophic drops of up to 65% that cannot be mitigated even by providing same-question in-context shots.

## Strengths

- **GSM-Symbolic provides a more reliable evaluation methodology that exposes performance as a distribution rather than a single point.** The paper creates symbolic templates that generate multiple instantiations of each question while preserving the required reasoning steps (Section 3, Figures 1–2). By showing that a model's accuracy varies by 12–15% across different instantiations of the same mathematical question, the paper directly challenges the reliability of single-point metrics on popular static benchmarks. This is a concrete methodological contribution.

- **The paper demonstrates that original GSM8K performance is often an optimistic outlier, consistent with contamination.** Across 21 out of 25 models, the original GSM8K accuracy lies more than one standard deviation from the center of the GSM-Symbolic distribution, on the right tail (Section 4.1, Figure 2). The paper appropriately frames this as "one explanation" (data contamination) rather than a proven conclusion. Even without a definitive contamination verdict, the observation that static benchmark performance is systematically biased upward is a valuable finding for the community.

- **The GSM-NoOp experiment reveals a critical and robust failure mode: adding a single irrelevant clause causes catastrophic drops across all models (up to 65%), and models cannot recover even with same-question in-context shots.** The paper shows that in the NoOp-Symb setting—where all eight shots are different instantiations of the *same* question—performance remains within the standard deviation of the baseline drop (Section 4.4, Figures 3b–c). This goes beyond prior work (e.g., GSM-IC) by showing the flaw persists even when the model is shown the exact reasoning chain, strongly supporting the pattern-matching hypothesis.

- **Systematic ablation of change types (names vs. numbers) shows that performance variance is not just noise but tied to the semantic depth of the change.** The paper separates modifications into "only names," "only numbers," and "both," and shows that variance is lower for names while accuracy drops progressively (Section 4.2, Figure 4). This granular analysis strengthens the overall argument about shallow pattern matching.

- **Large-scale evaluation across 25 models (open and closed) with nearly 500 evaluations adds robustness to the findings.** The consistent trends across models of vastly different sizes and families (Phi, Gemma, Llama, GPT-4o, o1) indicate that the observed limitations are not artifacts of a single model or training recipe (Sections 3.2, 4).

## Weaknesses

### Fatal
None.

### Major
None. The paper's core contributions are sound, and no single weakness undermines its main claims.

### Minor

- **The selection criteria for the 100 templates from GSM8K's 1319 test questions are not provided.** The paper states (Section 3) that "we maintained a manageable dataset size by using 100 templates" but does not explain how these were chosen (e.g., random subset, first 100, selection for templatability, or stratified across difficulty). If templates were chosen for ease of annotation, this could introduce systematic bias (e.g., simpler problems are easier to template), and the paper would benefit from a discussion of potential selection effects.

- **The contamination hypothesis would benefit from either stronger evidence or clearer acknowledgment of alternative explanations.** The paper presents "data contamination" as one explanation for why original GSM8K accuracy sits on the right tail of the GSM-Symbolic distribution (Section 4.1). This is a reasonable hypothesis and is appropriately hedged ("One explanation for this could be..."), but the paper does not discuss equally plausible alternatives—e.g., that the symbolic instantiation process may produce harder versions (more awkward numbers, larger ranges), or that the original test set naturally contains easier examples. A brief acknowledgment of these alternatives would make the narrative more balanced.

- **The NoOp experiment, while striking, could benefit from more thorough characterization.** The paper reports performance drops for one type of NoOp clause (the "smaller kiwis" example). It is not clear whether the catastrophic failure generalizes to other types of irrelevant clauses (e.g., discounts, color changes, units) or whether the severity is specific to this particular phrasing. Additionally, the paper states that NoOp-Symb performance "remains within the standard deviation" but does not report the actual standard deviation values—these would be helpful for readers to assess the claim.

### Trivial
None.

## Nice-to-Haves

- A human performance baseline on GSM-NoOp would help contextualize the results: if humans also occasionally err on these problems, the interpretation changes.
- Systematic variation of the irrelevant clause type in GSM-NoOp (discounts, quantities, units, etc.) would strengthen the generality of the finding.
- A brief discussion of why greedy decoding was chosen (vs. sampling with temperature) would address a natural reader question, though this is a standard choice for math evaluation.

## Removed Points

These points from the reviews are removed or downgraded per the filtering rules:

- **"Paper does not state benchmark release status":** Removed per hard rules about questioning release status of cited entities. The paper's own contribution is the benchmark; this is a fair observation but the rule explicitly removes such criticisms.
- **"Variable domains are vague — specific ranges mentioned for some but not all":** The paper provides a concrete, fully specified example in Figure 1 (right panel) including ranges and conditions. This is standard for a template illustration.
- **"No verification that 50 instantiations differ in difficulty in controlled ways":** The paper's core claim is the opposite—that reasoning steps are identical across instantiations and performance should therefore be similar. The observed variance *is* the finding.
- **"The P2 example introduces multiplication beyond clause count":** The paper explicitly acknowledges in a footnote that "adding or removing a clause does not always result in an exact increase or decrease of one in the number of required reasoning steps," and states that the focus is on the *evolution* of the distribution.
- **"Criticism about greedy decoding choice":** Greedy decoding is standard for math evaluation. This is a preference, not a weakness.
- **Strengths removed from Strength Finder:** None of the strengths were generic or nonsensical; all were specific and evidence-backed. No strengths were dropped.
- **"Related work on missing papers":** The paper's related work section (Section 2) is appropriate and well-connected to prior work. No missing related work complaints were present in the reviews.

## Novel Insights

The most interesting observation that goes beyond the paper's own explicit contributions is the asymmetry in the NoOp-Symb results: weaker models (e.g., Gemma-2B, Mistral-7B) actually *improve* when given same-question instantiations as shots (Figure 3c), while stronger models do not. This is the opposite of what one might naively expect—stronger models should benefit more from relevant in-context examples. The paper notes this observation but does not analyze it. If weaker models benefit from the additional pattern-matching surface area (more examples to match against) while stronger models' more sophisticated (but still brittle) processes are disrupted, this would be a revealing clue about the nature of the underlying mechanism. Conversely, it could mean that weaker models are less "committed" to the wrong operation and more easily corrected. This asymmetry deserves deeper investigation.

## Suggestions

1. **Specify template selection methodology.** State whether the 100 templates were randomly sampled from GSM8K's 1319 test questions, selected by ease of templating, or chosen via some other criterion. If the selection is biased toward simpler problems, discuss the implications.
2. **Add alternative explanations for the right-tail observation.** Explicitly note that the original GSM8K questions may be easier than their symbolic instantiations (e.g., due to more natural numbers or smaller values), in addition to the contamination hypothesis.
3. **Report standard deviation values for the NoOp-Symb and NoOp-NoOp conditions.** The claim that performance "remains within standard deviation" would be more useful with explicit numbers.
4. **Systematically vary the NoOp clause type.** Adding 2–3 additional types of irrelevant clauses (e.g., discounts that don't apply, color changes that don't matter) would demonstrate whether the catastrophic failure generalizes beyond the specific "smaller kiwis" construction.

## Score and Decision

The paper makes a solid empirical contribution: GSM-Symbolic is a useful benchmark, and the findings about variance, sensitivity, difficulty scaling, and NoOp failures are well-evidenced and important. The weaknesses are minor—missing methodological details, partial over-interpretation of one hypothesis, and a need for broader characterization of the NoOp effect. None threaten the core claims. The paper meets the bar for a strong evaluation/benchmark contribution.

MY FINAL SCORE: <pineapple>8.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>