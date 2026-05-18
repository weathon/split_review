Now I have all the information I need. Let me verify the remaining claims against the paper and produce the consolidated review.

---

## Summary

This paper introduces RULES (with an inconsistent alternate name "BIND" in the abstract), a benchmark for programmatically evaluating rule-following behavior in LLMs. It contains 15 text-based scenarios with 22 rules (negative and affirmative), each paired with a concise evaluation program using string matching and regex. Through manual red-teaming the authors identify 6 attack strategy categories, construct 862 hand-written test cases, and evaluate 12 proprietary and open-source models. Results show universal failures: even GPT-4 passes only 73.9% of systematic test cases, and GCG adversarial suffixes drive open 7B models to near 0% pass rates.

## Strengths

1. **Timely and well-motivated problem.** The paper addresses a critical gap: evaluating whether LLMs follow specified rules currently requires expensive human judgment, and the paper proposes a viable programmatic alternative. The motivation (Section 1) is clearly articulated and grounded in safety concerns.

2. **Careful scenario construction with inherently checkable rules.** The 15 scenarios are designed around stateless decision trees (Figure 3) where correct behavior depends only on the last user message. Rules are operationalized as concrete textual behaviors (e.g., "do not print the secret key"), making programmatic evaluation feasible by construction. The paper's design choice to focus on stateless scenarios (Section 2.2) after finding models failed even benign stateful tasks is a pragmatic and sensible scoping decision.

3. **Systematic attack taxonomy and large test suite.** From exploratory red-teaming, the authors distil 6 attack strategy categories (Just Ask, Indirection, Legalese, Obfuscation, Rule Change, Simulation) and instantiate them in 862 hand-written test cases covering all 22 rules across all 15 scenarios. Table 2 provides concrete examples of each strategy type. This represents substantial engineering effort and provides a reusable evaluation resource.

4. **Comprehensive model evaluation with rigorous statistics.** The paper evaluates 12 models spanning proprietary (GPT-4, GPT-3.5, Claude, PaLM 2) and open-source (Llama 2, Vicuna, Mistral) families. Variance from non-deterministic API outputs is quantified (Table 3: std. dev. ≤1.1/39 test cases), and McNemar's test is used for pairwise significance comparisons with clearly marked p-value thresholds (underlined for p<0.01). This level of rigor is creditable.

5. **Error detection analysis extends beyond generation.** The zero-shot classification experiment (Section 3.5) asking whether models can *detect* rule violations in other models' outputs provides a complementary perspective. Even GPT-4 achieves only 82.1% accuracy, showing recognition of rule-breaking is itself unsolved.

6. **GCG adversarial suffix experiments demonstrate vulnerability to automated attacks.** The finding that GCG can drive pass rates to near zero for open 7B models (Table 5) provides evidence that rule-breaking failures are not limited to human-crafted inputs.

## Weaknesses

### Fatal
None.

### Major

1. **No systematic validation of evaluation programs against human judgments.** The paper relies on the premise that simple string matching and regex "cannot exactly reproduce human judgment in edge cases, but we observe in practice that the vast majority of rule-breaking outputs from models are unambiguous" (§2.3). This observation is asserted, not demonstrated. No sample of model outputs is independently labeled by human raters and compared against the programmatic judgments. Without this, the reader cannot calibrate how often edge cases arise or whether systematic biases exist in the evaluation. This is not a fatal flaw — the rules are designed to be inherently checkable (e.g., "do not print the secret key" is evaluated by checking for that string) — but it is the single largest gap in the paper's evidence. A validation study with 100–200 examples spanning all scenarios would substantially strengthen the core contribution. Note: this does not invalidate the results; for the concrete rules tested, string matching provides strong ground truth. But the paper would benefit from quantifying the edge-case rate rather than leaving it as an informal observation.

### Minor

1. **Naming inconsistency (BIND vs. RULES).** The abstract (line 5) introduces the "Benchmark for Identifying Non-compliant Decisions (BIND)", while Section 1 (line 23) and every subsequent section refer to "Rule-following Language Evaluation Scenarios (RULES)". This is not a parser artifact — both names are clearly different in the text. The benchmark should have a single consistent name throughout. This does not affect the technical contribution but undermines presentation polish.

2. **Error detection experiment uses the same distribution as the generation evaluation.** Section 3.5 samples "1098 pairs of user messages and assistant responses from the outputs of models evaluated on the systematic test suite" to test detection ability. Since the detector models may encounter the same types of violations they themselves produced, this conflates the ability to detect rule violations with the ability to detect patterns in the distribution they participated in generating. A cleaner design would use held-out outputs (e.g., from a different set of models or from adversarial suffixes) to measure generalization. That said, the finding that even detection is imperfect remains informative.

3. **GCG experiments are limited in scope.** Only 7B open models are tested, using a single test case per rule repeated 20 times. The finding that GCG drives pass rates to near zero for small open models is consistent with prior work and does not test whether larger or proprietary models might be more robust. The paper's claims are appropriately qualified, but the practical significance of this experiment is limited.

4. **Evaluation program fragility not discussed in detail.** The paper acknowledges edge cases (§2.3) but does not describe the specific failure modes (e.g., models that paraphrase the secret key to evade regex, or innocuous outputs that accidentally trigger a match). A brief discussion of the types of false positives/negatives observed (or the safeguards built into the regex patterns) would help readers assess reliability.

### Trivial

1. The paper does not include a compact table listing all 22 rules across the 15 scenarios. Figure 3 provides a visual overview but the actual rule texts are not shown in one place, making it harder for readers to understand the full scope without reconstructing from the scenarios section.

2. Systematic test suite counts (355 negative, 507 affirmative) are given only in aggregate. A per-scenario breakdown would help identify whether certain scenarios are over- or under-represented.

## Nice-to-Haves

- **Human validation study** for evaluation programs (as described in Major Weakness 1). Even 100–200 examples with two raters and Cohen's κ would substantially strengthen confidence in the benchmark.
- **Per-scenario breakdown** of systematic test suite counts.
- **Compact table** of all 22 rule texts.
- **Discussion of evaluation program fragility** with specific edge-case examples encountered during development.

## Removed Points

- *"Systematic test suite coverage is not justified / does not exhaust the space of plausible strategies"* — The paper (line 117) explicitly states that strategies were derived from retrospective analysis and does not claim exhaustiveness. Criticizing the absence of a claim the paper never makes is a strawman.
- *"Distinction between following instructions and rules remains speculative"* — This is a discussion point in §4, explicitly presented as speculation/conceptual framing. It is not claimed as an experimental result and is not required to be operationalized for the paper's contributions.
- *"Adversarial suffix experiment is not a strength of the paper"* — This is an opinion, not a factual weakness. The experiment is limited but still provides useful evidence that rule-breaking extends to automated attacks.
- *Various formatting/style nitpicks* — These are parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The reviews confirm the paper's central findings (models universally fail at rule-following) and surface a validation gap that is genuine but not fatal. The key methodological observation — that the evaluation programs are definitional rather than approximative for the designed scenarios — is underappreciated by the harsh critic but correct, and it tempers the severity of the validation concern.

## Suggestions

1. **Fix the naming inconsistency:** Choose either BIND or RULES and use it consistently throughout the paper.
2. **Add a human validation study:** Collect 150–200 model outputs spanning all 15 scenarios, have two independent raters label pass/fail against the rules, and report agreement metrics (Cohen's κ, percentage agreement) along with analysis of disagreement types. This can be a brief appendix section.
3. **Include a compact table** listing all 22 rules with their scenario assignment and type (negative/affirmative).
4. **Add per-scenario breakdown** of test case counts for the systematic test suite.
5. **Expand discussion of evaluation program limitations:** describe concrete edge cases encountered during development and how the regex patterns handle (or fail to handle) them.
6. **Clarify the error detection experimental setup:** note that the test distribution may overlap with the detector models' own generation distribution and discuss whether this limits conclusions.

## Score and Decision

This is a solid benchmark paper with a clear contribution, substantial effort in scenario/test-case construction, and thorough model evaluation. The main gap — lack of human validation for evaluation programs — is real but not fatal, given the concrete, string-level nature of the rules. The paper would benefit from a validation study before publication. The contribution is timely, the experimental design is otherwise sound, and the resource (test suite, evaluation code, scenarios) will be valuable to the community.

Assessing key axes:
- **Originality:** Good — programmatic rule-following evaluation with security/game-inspired scenarios is a novel framing
- **Importance:** High — rule-following is a critical safety capability
- **Claims supported:** Mostly supported — the main finding (models fail) is robustly demonstrated
- **Soundness:** Generally sound — some methodological gaps (validation, distributional overlap in error detection) but no fatal errors
- **Clarity:** Good, despite the naming inconsistency
- **Value to community:** High — usable benchmark, reproducible evaluation, extensive test suite

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>