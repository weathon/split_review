## Summary

This paper introduces ActionReasoningBench, a diagnostic benchmark for evaluating LLMs on Reasoning about Actions and Change (RAC). It spans 8 IPC domains with 152k questions across 6 RAC categories (*Fluent Tracking*, *State Tracking*, *Action Executability*, *Effects of Actions*, *Numerical RAC*, *Composite Questions*), action sequences up to 19 steps, and novel ramification constraints that model indirect action effects. The paper evaluates GPT-4o, o1-preview, Llama-3.1-8B-Instruct, and Llama-3.1-70B-Instruct, finding that models achieve moderate performance on basic RAC categories but struggle substantially on complex ones — with GPT-4o scoring 0% on ramification questions and o1-preview reaching only 18.4%.

## Strengths

- **Systematic six-category RAC decomposition that goes well beyond prior benchmarks.** Table 1 shows that PlanBench and TRAC together cover only *State Tracking* and *Action Executability*, while ActionReasoningBench adds four entirely new categories, ramification constraints, and fluent subcategories. This directly supports the paper's central claim of providing the most comprehensive RAC benchmark to date, and the decomposition is grounded in the RAC literature.

- **Ramification constraints expose a striking and previously undetectable failure mode.** GPT-4o scores 0% across all ramification questions (Table 8), and o1-preview achieves only 18.4% overall. The SEM values and the analysis of GPT-4o's outputs (consistently failing to mention ramification fluents despite explicit domain descriptions) concretely demonstrate the benchmark's diagnostic utility — it identifies a specific reasoning capability gap that no prior benchmark was designed to expose.

- **Rigorous and reproducible data-creation pipeline.** The four-stage pipeline (PDDL → ASP solver → state-space computation → template-based generation with Llama paraphrase, validated by two domain experts) is clearly described and makes the ground-truth labels trustworthy. Using PDDL solvers and ASP solvers for ground-truth generation avoids relying on LLM correctness at the data-creation stage.

- **Negative-fluent analysis yields a precise, actionable finding.** The paper isolates a 12.16% performance decline on questions involving negative fluents and notes that models systematically struggle more with recalling false fluents than true ones (Section 5). This is a fine-grained diagnosis enabled by the benchmark's design.

## Weaknesses

### Major

- **The memorization confound undermines the diagnostic interpretation of non-ramification results without being addressed.** The paper hypothesizes (line 319) that GPT-4o's 0% on ramification questions stems from pre-training exposure to IPC domains — the model memorized direct effects from the original domains and cannot handle the novel manually-added ramification fluents. This same hypothesis applies to all non-ramification results: a model could appear competent on RAC (GPT-4o achieving 60–94% on non-ramification binary questions) while actually retrieving memorized action effects from pre-training rather than performing genuine reasoning. The paper does not test this confound (e.g., by evaluating on domains with fictional object names, altered action effects, or held-out domains), yet it directly affects whether the benchmark cleanly measures RAC *ability* versus pre-training *memory*. This is the most significant threat to the paper's core claim that the benchmark diagnoses RAC reasoning capability.

- **Free-form answer evaluation methodology is acknowledged but not validated in the available text.** Free-form answers (1,303 questions, 37% of the test set) are evaluated by prompting Llama-3.1-70B-Instruct, a model that the paper itself shows achieves only 45–77% accuracy on binary RAC questions. The sentence reporting the correlation between this evaluator and human judges is truncated in the extracted text (line 171), so the correlation cannot be verified. Human evaluation was used only for the ramification subset. The paper candidly acknowledges this limitation (line 340), but without the correlation data in the available manuscript, readers cannot assess the reliability of the free-answer results that form a substantial portion of the paper's evidence. Details about human evaluation (number of annotators, inter-annotator agreement) are also absent.

- **The ramification results, while dramatic, are reported on very small samples with no explicit sample size reporting.** The SEM values for o1-preview range from 7.38% to 27.21%, which with binary scoring implies per-cell sample sizes of approximately n≈5–15. The paper never reports the exact number of ramification questions in the test set or per condition. The striking 0% GPT-4o result and the 7.69–25.00% o1-preview results are important findings, but their statistical reliability is unclear without per-cell sample sizes.

### Minor

- **The "outperforms GPT-4o" fine-tuning claim lacks the necessary qualification.** The paper states (line 278) that fine-tuned Llama-3.1-8B "even outperform[ed] GPT-4o by 4.2%." This comparison is on-distribution: the model was fine-tuned on the same domains and question types it was tested on, while GPT-4o was evaluated zero-shot. This is expected behavior and does not test generalization. The framing inflates the significance of a result that is useful primarily to show the benchmark is learnable. A qualification noting the on-distribution nature of the comparison is needed.

- **Composite Questions category is underspecified.** As the largest test-set category (1,397 questions), the paper says it "combine[s] up to three distinct categories" but does not provide a breakdown of which combinations are present, their frequencies, or whether all combinations are equally represented (only two specific combinations are compared in the analysis, line 262). This makes it difficult to interpret aggregate results for this category.

- **The diagnostic analysis is shallower than the framing suggests.** The paper describes the benchmark as "diagnostic," which promises identification of *where and why* models fail. The analysis stays at the level of aggregate accuracy by question category, action-sequence length, and fluent type. Error-type breakdowns (e.g., false positives vs. false negatives on Action Executability, whether failures cluster on specific objects or positions in action sequences) are absent. These would make the benchmark more useful to the community as a diagnostic tool.

### Trivial

- The paper uses Llama-3.1-70B-Instruct for paraphrasing templated questions, which means the test set may contain linguistic patterns that favor or disfavor this same model when evaluated. A model-agnostic paraphrase strategy would be cleaner, though the practical impact is likely small.

## Nice-to-Haves

- Testing the memorization confound directly: evaluate models on domains with fictional object names or altered action effects to measure reasoning versus retrieval.
- Error-type analysis (false positives vs. false negatives per category) to strengthen the diagnostic utility.
- A complete breakdown of composite question combinations and their frequencies.
- Explicit reporting of per-condition sample sizes for the ramification subset.

## Removed Points

*The following points from the reviewers were removed with justifications:*

- **"No correlation metric between Llama-3.1-70B evaluator and human judges is ever reported"** — REMOVED. The sentence at line 171 is truncated mid-phrase ("the correlation between Llama-3."), which is a PDF extraction artifact. The original submission likely contains this correlation value. The general methodological concern about LLM-as-evaluator is retained above, but the specific claim that the data is missing is not verifiable from the extracted text.
- **"Missing appendix tables (few-shot results)"** — REMOVED. The parser strips appendix content from all papers. The few-shot tables existed in the original submission.
- **Criticisms about missing hyperparameters, training logs, or complete reproducibility details** — REMOVED per hard rules against nitpicks on reproducibility.
- **"No statistical testing"** — REMOVED. Reporting SEM is standard practice in benchmark evaluations, and the paper does not make strong comparative claims that require formal significance tests. This is a field-standard choice, not a weakness.
- **"The paraphrase step uses Llama-3.1-70B-Instruct which is also one of the evaluated models"** — DEMOTED to Trivial. The practical impact is small: the paraphrase step produces question wording variations, not the reasoning content of the questions. The ground-truth answers are computed by ASP solvers, not by the paraphrasing model.

## Novel Insights

None beyond the paper's own contributions. The most insightful observation emerging from the reviews is the interaction between the memorization confound and the ramification results: the paper convincingly shows that GPT-4o fails on ramification because it relies on memorized IPC domain knowledge that does not include the novel manually-added fluents. But this same mechanism implies that the non-ramification results may partly reflect memory retrieval rather than reasoning. This tension — that the benchmark's most striking success (diagnosing GPT-4o's ramification failure) simultaneously casts doubt on the interpretation of its other results — is the most important unresolved issue the paper raises.

## Suggestions

1. **Address the memorization confound directly.** Add an experiment where you evaluate on a held-out domain or a version of an existing domain with fictional object/fluent names and altered action effects, and compare performance. This would separate reasoning from retrieval and greatly strengthen the claim that the benchmark measures RAC ability.
2. **Report the correlation between the Llama-3.1-70B evaluator and human judges** for free-form answers (if not already present in the full text). If this data exists but was truncated, ensure it is clearly displayed.
3. **Report per-condition sample sizes** for the ramification subset alongside the existing SEM values.
4. **Provide an error-type breakdown** for at least one category (e.g., Action Executability: false positive vs. false negative rates) to better demonstrate the benchmark's diagnostic capability.
5. **Qualify the fine-tuning comparison** with a clear statement that the evaluation is on-distribution and that the result primarily validates the benchmark's learnability rather than demonstrating superiority.

## Score and Decision

This is a well-constructed benchmark that fills a genuine gap in LLM evaluation for RAC. The data-creation pipeline is rigorous, the coverage (8 domains, 6 categories, ramification constraints) substantially exceeds prior work, and the key findings — particularly the ramification results — are novel and informative. The main weaknesses are the unaddressed memorization confound (which affects how non-ramification results should be interpreted) and the unevaluated LLM-based evaluator for free-form answers (which the paper candidly acknowledges). Neither is fatal to the benchmark's value, and both are addressable. The benchmark itself is a solid contribution that will be useful to the community.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>