Now I have a thorough understanding of the paper. Let me synthesize the final review.

---

## Summary

This paper introduces KOR-Bench, a benchmark for evaluating LLMs on "knowledge-orthogonal reasoning" — tasks designed to minimize reliance on domain-specific knowledge from pre-training. The benchmark comprises 1,250 problems across five categories (Operation, Logic, Cipher, Puzzle, Counterfactual), with rules modified to be sufficiently novel. The authors evaluate 30+ models, finding O1-Preview (72.88%) and O1-Mini (70.16%) substantially outperform GPT-4o (58.00%) and Claude-3.5-Sonnet (58.96%), and conduct further analyses on cipher sub-step bottlenecks, self-correction dynamics, and complex task processing.

## Strengths

- **Novel and well-motivated concept.** The paper identifies a real limitation in current reasoning benchmarks — the confounding of knowledge recall with genuine reasoning — and proposes "knowledge orthogonality" as a design principle to address it. The five-category taxonomy (new symbols, new concepts, new execution rules, new problem-solving frameworks, new story contexts) is thoughtful and covers diverse reasoning modalities. (Supported by Section 1, Section 3.1)

- **Comprehensive evaluation revealing meaningful performance gaps.** The benchmark differentiates models in a way that does not simply recapitulate existing leaderboards: O1-Preview (72.88%) and O1-Mini (70.16%) dramatically outperform GPT-4o (58.00%) and Claude-3.5-Sonnet (58.96%), especially on Cipher (+40pp) and Puzzle (+20pp) tasks where the gap is largest. This suggests the benchmark captures dimensions of reasoning not fully probed by existing evaluations. (Supported by Table in Section 5)

- **Stepwise prompting analysis identifies specific reasoning bottlenecks.** By decomposing cipher tasks into 9 sub-steps and testing models on each, the paper provides concrete, actionable findings: spatial operations (Rotation, Conditional Filling, Conditional Reading) have near-100% error rates across models, while Encoding and Partition are relatively easy. This granular diagnostic value is a genuine contribution beyond simple accuracy scoring. (Supported by Section 6.1, Figure 2)

- **Practical findings on self-correction and complex task processing.** The analysis showing that two rounds of self-corction yield optimal improvement (~10.36% average gain) and the complex task processing experiments (Multi-Q/Multi-R/Multi-RQ) provide useful guidance for inference-time strategies and multi-rule reasoning. (Supported by Section 6.2, Section 6.3)

## Weaknesses

### Fatal
None.

### Major
- **The "knowledge orthogonality" claim lacks systematic verification.** The paper's central differentiating claim — that rules are "suitably modified to ensure that they do not appear in common pre-training data" (Section 3.1) — is asserted rather than demonstrated. The description of modifications (combining/adjusting classical operations, altering substitution tables, adapting puzzles) provides plausible qualitative evidence, but no quantitative validation is offered (e.g., n-gram overlap with pretraining corpora, probing whether models recall rule-like patterns, comparing performance on modified vs. unmodified versions of the same rule). Without such evidence, it is unclear whether KOR-Bench is genuinely more "knowledge-orthogonal" than existing benchmarks like PuzzleBench or RuleBench, or whether it simply presents a harder collection of tasks. This gap weakens the paper's core novelty claim.

### Minor
- **Stepwise prompting analysis is limited to only 5 cipher rules.** The analysis that identifies specific sub-step bottlenecks (Section 6.1) selects "five highly erroneous rules" out of 25 available. While the findings are informative, their generalizability to the full cipher category is unclear. The paper does not justify why these 5 rules are representative.

- **"More Experiments and Analyses" section is substantially underdeveloped.** The subsection (Section 6.4) contains only a single sentence about an attention-visualization PDF, with no analysis, figures, or takeaways in the main text. This section as presented contributes nothing to the paper.

- **The counterfactual "real-life answer" metric lacks direct validation.** The paper interprets a lower proportion of real-life answers as better rule-following (Table 5 notes), but provides no manual annotation or qualitative check to confirm that low-ratio models are genuinely following counterfactual rules rather than, e.g., guessing randomly or refusing to answer. This would strengthen the metric's credibility.

### Trivial
- **The self-correction analysis lacks a token-budget control.** The analysis shows accuracy improves after self-correction (Section 6.2), but does not compare against a baseline of generating a longer single response with the same total token budget. This limits the ability to attribute improvement specifically to the correction mechanism.

- **No human performance baseline.** Without human accuracy on these tasks, it is difficult to calibrate whether model scores indicate strong or weak reasoning, or whether the questions are well-calibrated.

## Nice-to-Haves

- **Correlation analysis with existing benchmarks** (e.g., MMLU, GSM8K, PuzzleBench). Reporting Spearman rank correlations would help establish whether KOR-Bench measures something genuinely distinct, and would directly address a natural reader question.
- **Ablation comparing original vs. modified rules.** For a subset of rules where the original version is well-known, comparing accuracy on original vs. modified variants would provide direct evidence that the modifications achieve orthogonality.
- **Human evaluation spot-checks** on a sample of model outputs to validate that the regex-based extraction and the counterfactual metric align with human judgment.

## Removed Points

- Criticism about the prompt subsection being truncated: This is a PDF parser artifact, not an author issue. The content exists in the original submission. (Hard Rule on formatting artifacts)
- Criticism about the results table being garbled: Parser artifact. The original PDF has proper formatting. (Hard Rule on formatting artifacts)
- Criticism that Counterfactual tasks use anime/TV worlds (known in training data): This misunderstands the task design — the Counterfactual category deliberately uses known worlds to test whether models can *override* their pre-trained knowledge. The metric (proportion of real-life answers) directly measures this. (Factually wrong criticism)
- Criticism that "O1 models' superior performance 'highlights KOR-Bench's effectiveness' is circular": The paper uses this framing loosely (Abstract), but the core logic is straightforward: a benchmark that shows large, interpretable performance gaps is useful for distinguishing models. There is nothing circular about this.
- Criticism that the evaluation via regex is "fragile" and that no human evaluation is performed: Regex-based answer extraction with fallback to single brackets is standard practice in LLM evaluation. Human evaluation of 1,250 questions is neither standard nor expected.
- Several generic nitpicks (pace/scope concerns, presentation preferences) from the Harsh Critic.

## Novel Insights

The most striking finding is not simply that O1 models lead — it is the *asymmetry* of the gap. On Operation and Logic, O1-Preview is only modestly ahead of Claude-3.5-Sonnet (88.80 vs. 88.40 on Operation; 63.20 vs. 67.20 on Logic — Claude is actually slightly ahead on Logic). But on Cipher the gap is 82.80 vs. 42.80, and on Puzzle 36.80 vs. 14.80. This pattern suggests that the O1 series' advantage is concentrated in tasks requiring multi-step, spatially-grounded procedural reasoning with tight rule constraints — not in general rule comprehension or application. The cipher sub-step analysis corroborates this by pinpointing spatial operations (Rotation, Conditional Filling) as the near-universal bottleneck. This convergence of evidence (benchmark-level gaps and sub-step error patterns) gives us a specific, testable hypothesis about what O1's "reasoning" does differently: it appears to manage complex procedural state and spatial transformations that other models cannot reliably execute step-by-step.

## Suggestions

1. **Provide validation of knowledge orthogonality.** The most impactful addition would be a simple experiment: take a handful of rules where the unmodified version is well-known (e.g., a standard cipher), compare accuracy on original vs. modified versions, and show that modification significantly reduces accuracy. This directly supports the orthogonality claim.
2. **Expand the stepwise prompting analysis** from 5 rules to more cipher rules (or at least justify why the chosen 5 are representative) to strengthen the generalizability of the bottleneck findings.
3. **Flesh out or remove Section 6.4.** A single sentence about an attention PDF adds no value. Either provide actual analysis or remove the subsection.
4. **Add human performance on a sample** (e.g., 50-100 questions) to calibrate difficulty and validate question quality.
5. **Report confidence intervals** for the main results table, especially for smaller models where variance may be higher.

## Score and Decision

**Summary evaluation:** The paper proposes a genuinely novel and well-motivated evaluation concept, builds a substantial benchmark, and produces interesting empirical findings (the O1 advantage is concentrated in procedural/spatial reasoning, cipher bottlenecks are specifically spatial operations, self-correction saturates at 2 rounds). These are real contributions. The primary weakness is that the central differentiating claim — knowledge orthogonality — is asserted rather than systematically validated. This is a significant gap but not a fatal one; the benchmark remains valuable even with imperfect orthogonality, and the gap is addressable with additional experiments. On originality, the KOR concept is new. On importance, the question of how to evaluate reasoning without knowledge confounds is timely. Claims are partially supported — the benchmark findings are solid, but the orthogonality claim needs stronger backing. Experiments are sound within their scope. Writing is clear. The benchmark has clear value to the community.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>