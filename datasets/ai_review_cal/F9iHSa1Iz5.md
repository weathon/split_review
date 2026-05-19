- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 5, 3, 3
Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

The paper proposes MuseD (Multi-step Deduction), a pipeline for automatically generating multi-step deductive reasoning data through **backward syllogistic expansion** — starting from a valid conclusion and recursively expanding backwards using valid syllogistic forms to create logically consistent prompts. The pipeline also scores model responses at the step level (counting eliminated middle terms) and constructs preference pairs for RLHF training. Experiments on Llama3-8B show that RLHF with MuseD data yields substantial improvements on both in-domain and out-of-domain reasoning benchmarks (e.g., +14–16% on PrOntoQA and LogicalDeduction), and that step-level process signals contribute meaningfully beyond outcome-only rewards.

## Strengths

- **Principled backward generation using valid syllogistic forms (Section 4.1).** By starting from a conclusion and expanding via the 15 valid syllogistic forms, the method guarantees that every generated prompt has a unique correct conclusion and contains no internal contradictions. Using virtual entities (Greek letters, virtual nouns) to avoid commonsense shortcuts is a reasoned design choice that forces models to rely on formal logic rather than world knowledge.

- **Step-level scoring provides dense process reward (Section 4.3).** The step score enumerates all valid middle-term elimination paths and credits any correct reasoning chain, even when multiple valid routes exist. This goes beyond outcome-only evaluation and enables finer-grained training signal than typical ORMs. The multi-dimensional scoring (step, result, wrong-step, noise, extra) provides useful diagnostic granularity.

- **Large and consistent out-of-domain improvements (Table 2).** PPO_Na-P achieves 86.8% on PrOntoQA (vs. 72.8% for PPO_UF, +14 points) and 48.3% on LogicalDeduction (vs. 32.7%, +15.6 points). Gains on ProofWriter and FOLIO are also present. These OOD results provide the strongest evidence that the MuseD data and step-level rewards transfer beyond the training distribution.

- **Systematic ablation of preference-pair composition isolates the role of process signals (Section 5.3.2).** Comparing PPO_Na-P (step + result scores) with PPO_Na-R (result only) shows that step-level signals yield 5–10 point gains across multiple OOD benchmarks. The comparison of P vs. PN further reveals that adding negative signals reduces step score, providing practical insight for reward design.

- **Multi-dimensional evaluation set (Section 6).** The MuseD evaluation set provides granular diagnostics (step score, result, wrong-step count, etc.) across 1–10 reasoning steps, enabling more nuanced model comparison than accuracy-only benchmarks.

## Weaknesses

### Fatal
None.

### Major

- **The experimental design does not fully isolate MuseD's specific structure from the general benefit of adding more reasoning data.** PPO_Na-P is trained on UF (27w pairs) + 15k MuseD logic prompts, while PPO_UF uses only UF data. The observed improvement could partly stem from simply increasing the volume of logical training data, regardless of its source. PPO_NaO-P (MuseD only, no UF) performs poorly, showing that UF data is necessary, but the paper lacks a control where an alternative source of logical data (e.g., ProofWriter-generated problems, or random valid triplets without backward chain structure) is added to UF at comparable volume. Without this, it is unclear whether MuseD's backward-generation structure and step scoring are the specific cause of improvement, or whether any additional exposure to reasoning problems would produce similar gains.

- **The step score metric lacks direct validation.** The step score is central to the paper's claim that "step signals can significantly improve the effect." While the metric has face validity from formal logic (it counts correctly eliminated middle terms), and while the OOD performance improvements provide indirect evidence that optimizing for step scores transfers to better reasoning, no direct validation is presented — no human agreement study, no analysis of whether step score correlates with human-judged reasoning quality, and no demonstration that the scoring resists trivial gaming. A calibration against human annotations or known-correct reasoning chains would substantially strengthen the central contribution.

### Minor

- **No error bars, confidence intervals, or significance tests.** The paper reports single values for each model on each metric, with many pairwise comparisons across 11 models × multiple datasets. Without measures of variability (e.g., standard deviations over seeds), some observed differences could be within the noise range. Adding variability estimates would substantially strengthen the quantitative evidence.

- **No discussion of limitations.** The paper does not acknowledge that: (a) the virtual entities make the tasks highly artificial, (b) the OOD evaluation sets are also synthetic (PrOntoQA, ProofWriter, LogicalDeduction) or narrow (FOLIO, AR-LSAT), (c) the step scoring likely relies on brittle parsing and matching of propositions from free-text responses. A limitations section would improve intellectual honesty.

- **The curriculum learning negative result is noted but not analyzed (Section 5.3.4).** PPO_Na-P-Cur hurts OOD performance by 8–10 points on some benchmarks. The paper reports this finding without discussion of possible causes (e.g., distribution shift from the easy-to-hard ordering, or interaction with the RM's training distribution). Given that curriculum learning is often beneficial in other settings, this negative result warrants deeper analysis.

### Trivial

- **Over-precise reporting.** Step scores and result scores are reported to four decimal places (e.g., 0.3485, 0.5715) and wrong/noise/extra step counts to four decimal places (e.g., 1.685, 0.7815), despite these being computed from counts over finite samples. Reporting to two decimal places with appropriate rounding would be more appropriate.

## Nice-to-Haves

- **Deeper analysis of the natural vs. formatted response comparison.** The finding that natural responses outperform formatted ones is interesting but underexplored. A diagnostic analysis (e.g., examining specific failure modes of formatted responses, or comparing the same reasoning trace expressed in both formats) would strengthen Section 5.3.3 and could inform future work on reward design for reasoning.

- **Direct validation of the step score metric** against human annotations would provide the strongest form of evidence for the paper's central claim about step signals.

- **A control experiment** where an alternative source of logical training data (same volume, different structure) is used in place of MuseD data would cleanly isolate the contribution of MuseD's specific design.

## Removed Points

These points from the reviewers were considered and removed from the main review with justification:

- **"The step score algorithm is relegated to a stripped appendix":** The main text (Section 4.3.1, lines 174–192) provides a clear description of the step score computation. The full algorithm was in the appendix, which the parser strips from all papers. Per the hard rules, criticisms about missing appendix content are removed.

- **"Related work is thin on PRMs":** The paper explicitly discusses ORM and PRM in Section 4.4 (lines 195–196) and situates its approach relative to both. The discussion is proportionate for the paper's scope.

- **"The claim that 'positive rewards are the primary motivator' undercuts the step-signal thesis":** This misreads the paper. The finding that P > PN (adding negative signals hurts) is compatible with the finding that step signals help (P > R). Both claims are supported and non-contradictory.

- **"The P vs. PN comparison gives contradictory signals":** The paper explicitly discusses this trade-off (Section 5.3.2): adding negative signals reduces negative indicators but also reduces step score. This is a reported finding, not a contradiction.

- **"Virtual entities limit ecological validity":** The paper explicitly justifies this choice as necessary to prevent models from taking commonsense shortcuts (Section 4.1, line 99–100). This is a reasoned design decision.

- **"Formatted responses confounding" raised as a critical issue:** The paper provides a plausible explanation (natural format is closer to the model's training distribution) and the finding is useful even without deeper diagnostics.

- **General concerns about OOD datasets being "also synthetic":** The paper tests on multiple OOD benchmarks from different sources and construction methods, including human-created (FOLIO). The OOD results are informative.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a data-source control experiment: train PPO on UF + logical data from an alternative generation method (e.g., random proposition triplets, or ProofWriter data) at the same volume as the MuseD data. If MuseD still outperforms, the specific contribution of backward-generation structure and step scoring is cleanly isolated.

2. Calibrate the step score metric against human judgments on a subset of responses (e.g., 100–200 responses), or show that it correlates with the number of logically valid steps in reference reasoning chains.

3. Report results with error bars (e.g., standard deviations over 3–5 random seeds) for key comparisons.

4. Add a limitations paragraph discussing the artificiality of virtual entities, the synthetic nature of evaluation sets, and potential brittleness of step scoring.

5. Explore the curriculum learning negative result: is the OOD performance drop caused by distribution shift in the training ordering, or by some other factor?
