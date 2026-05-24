Now I have a clear picture of where this paper sits. Let me write the final review.

## Summary

This paper investigates whether translating English benchmarks into Arabic can conceal data contamination while still providing models an unfair advantage. The authors fine-tune four open-weight LLMs on mixtures of English test data and Arabic-translated test data at varying proportions (0%, 10%, 50%, 100%), then evaluate on the original English benchmarks. They extend TS-Guessing with a choice-reordering strategy to probe cross-lingual memorization. The core finding is that translation obscures surface-level contamination signals (since Arabic text evades standard English-centric detection) while memorized knowledge persists — models recall original answer indices at rates far above chance, as captured by the index-recall rate (IDR) metric. The paper also proposes a Translation-Aware Contamination Detection (TACD) framework as a forward-looking blueprint.

## Strengths

- **Choice-reordering TS-Guessing provides clean evidence of cross-lingual memorization.** By shuffling MCQ answer choices and then masking one incorrect option, the index-recall rate (IDR) in Table 3a directly exposes memorization of answer-letter positions. LLaMA-3.2-1B-Instruct reaches IDR = 0.643 at 50% contamination and 0.410 at 100%, showing the model retains the original answer letter even after Arabic translation. This is a genuinely clever probe and the strongest result in the paper.

- **Systematic contamination experiments across models, benchmarks, and contamination levels.** The fine-tuning setup (Section 3.1) varies the proportion of Arabic-translated test data across four contamination levels (0%, 10%, 50%, 100%) on four models and three benchmarks. The divergent patterns — MMLU rising monotonically while XQuAD/MLQA exhibit non-monotonic fluctuations — demonstrate that translation-based contamination affects closed-book MCQ and extractive QA fundamentally differently, which is an interesting and well-documented finding.

- **Novel multilingual perspective on a well-studied problem.** Using Arabic — a low-resource language — to translate standard English benchmarks and evaluating models on the original English versions exposes a genuine blind spot in English-only contamination detection. This is an underexplored angle with practical relevance.

## Weaknesses

### Major

- **The "flatness" claim in Section 4.2 is contradicted by the paper's own results.** Section 4.2 states that "across contamination levels p ∈ {10, 50, 100}%, the models exhibit approximately equal performance on all evaluated benchmarks" and interprets this as evidence that translation masks contamination. Table 2 directly contradicts this: Mistral's MMLU jumps from 0.580 to 0.690 (an 11-point increase), Mistral's XQuAD collapses from 0.455 to 0.114 (a 34-point drop), Gemma's XQuAD rises from 0.481 to 0.606, and Qwen's MLQA spikes to 0.409 then drops to 0.153. These are not "approximately equal" by any reasonable standard. The claim of flatness as evidence for masking is unsupported, and this overstatement weakens the paper's central interpretive argument.

- **The experimental design confounds translation effects with direct English memorization.** The training condition is always D_EN^d ∪ D_AR^d(p), meaning every model — including the p=0 baseline — is fine-tuned on the English test items it will later be evaluated on. The p=0 condition therefore does not represent a clean baseline. While the TS-Guessing probe with shuffled answer choices partially mitigates this concern (since index recall after shuffling is not explained by English exposure alone), the broader performance comparisons across p values cannot cleanly isolate the marginal effect of Arabic contamination from English memorization. The paper would be substantially stronger with a truly clean baseline (no test data exposure) and/or an Arabic-only condition.

### Minor

- **Referenced embedding analysis is absent.** Section 4.3 invokes "the embedding figure" showing that Arabic→English translations remain close to English originals with high cosine similarity, and the equation s = cos(e^{ar→en}, e^{en}) is presented. No such figure or quantitative embedding analysis appears in the paper. Without it, the claim that semantic proximity compresses detectability across contamination levels is unsubstantiated.

- **TACD framework is purely conceptual with no validation.** Section 5 presents three components (cross-translation benchmarking, TS-Guessing across variants, back-translation consistency) as a forward-looking blueprint. The paper acknowledges this explicitly ("we offer TACD as a forward-looking blueprint rather than a complete implementation"), but this means the claimed contribution of the framework remains aspirational. The paper's value rests entirely on the experimental results in Section 4.

- **No statistical significance testing or variance reporting.** Given the non-monotonic and sometimes volatile trends (particularly in MLQA, where Qwen spikes from 0.162 to 0.409 then collapses to 0.153), reporting confidence intervals or run-to-run variance would help distinguish genuine signal from noise. Single-run results on fine-tuning experiments are the norm in this area, but the specific patterns the paper highlights would benefit from this rigor.

### Trivial

- The paper's internal inconsistency between Section 4.1 (which correctly notes MMLU's "generally monotonic increase") and Section 4.2 (which claims "approximately equal performance") suggests the sections were written at different times without reconciliation.

## Nice-to-Haves

- A truly clean baseline (no test data exposure in any language) and an Arabic-only training condition would allow clean isolation of translation-mediated contamination effects.
- Applying standard contamination detection metrics (n-gram overlap, Min-K% Prob) to the Arabic data would directly substantiate the claim that translation "obscures traditional contamination signals."
- A small-scale proof-of-concept for one TACD component would substantially strengthen the paper's forward-looking contribution.

## Removed Points

These points were flagged in reviewer inputs but are removed from the final review:

- **"Baseline is fundamentally contaminated" as a fatal flaw**: While the design choice to always include English test data is a limitation (retained as Major), it does not render the entire study unsound. The TS-Guessing probe with choice reordering specifically controls for English exposure by shuffling answer choices — if the model had only memorized the English answer ordering, shuffling would break that signal. The IDR results therefore remain valid evidence for cross-lingual memorization regardless of the English baseline.

- **"TACD contribution is minimal" as a fatal criticism**: The paper explicitly positions TACD as a forward-looking blueprint, not a validated contribution. This is a Minor limitation, not a fatal one.

- **Criticism about the paper questioning whether translation can act as a "natural barrier"**: The harsh critic argues the design "pre-empts that barrier test." The paper's experimental question is reasonable given the design — it tests whether Arabic-translated test data, when added to English data, produces detectable performance changes and detectable memorization patterns. The paper could have been designed more cleanly, but the design is not meaningless.

- **Demand for statistical significance testing as a fatal issue**: Single-run evaluation is standard practice in large-scale LLM benchmark evaluation. Including variance would be nice but its absence does not invalidate the results.

- **Criticism of the literature review length**: The survey is competent and establishes context. Length preferences are subjective.

- **All formatting, typo, and grammar criticisms**: These are parser artifacts or subjective preferences.

- **Criticism about missing appendix content**: The parser strips appendices. The original submission may contain the embedding figure and additional analyses.

## Novel Insights

None beyond the paper's own contributions. The paper's most novel observation — that choice-reordering can reveal cross-lingual index memorization even when surface forms are translated — is the paper's own finding and is well-supported by the TS-Guessing results.

## Suggestions

- Either remove the "approximately equal performance" / "flat trend" framing in Section 4.2, or qualify it carefully with specific numbers showing where it holds and where it does not. As written, it is directly falsified by Table 2.
- Include the embedding analysis referenced in Section 4.3 with actual cosine similarity values and methodology, or remove the claim.
- Add a limitations section that honestly acknowledges the English-data confound in the training design and the conceptual-only status of TACD.
- Consider reporting Min-K% Prob or n-gram overlap on the Arabic data to directly demonstrate that translation evades standard detection while the model still benefits.

## Score and Decision

**Calibration summary:**

Round 1 bracket: **4.0–6.5**. The paper is stronger than Nk1MegaPuG (4.25, EAL evasion paper with fundamental clarity/novelty issues) and rAylWUIKtu (4.25, Benchmark Inflation with methodological weaknesses), but weaker than m2NVG4Htxs (6.75, longitudinal cutoff analysis with a clever natural-experiment design) and Nsms7NeU2x (6.75, forgetting paper with both theory and extensive experiments).

Round 2 narrowing:
- **FDhAngvHuf (5.50, Reject)**: Dataset bias paper with interesting findings but limited model scale and somewhat narrow scope. Our paper has a comparably interesting angle and arguably more impactful implications (contamination detection vs. dataset bias), but shares similar limitations in robustness of claims. Our paper is comparable in overall quality.
- **zWqr3MQuNs (6.25, Accept)**: The Min-K% Prob paper. Introduced a concrete, validated method with a constructed benchmark and multiple case studies. Our paper's TS-Guessing extension is clever but less substantial as a standalone contribution, and TACD is conceptual only. Our paper is weaker than this anchor.
- **9QPH1YQCMn (6.25, Accept)**: Infilling Score paper with a novel detection method and strong validation. Our paper is weaker.

The paper sits closest to FDhAngvHuf (5.50) in overall quality — an interesting idea with some real evidence but also notable gaps in the strength of its central claims. The TS-Guessing results are genuinely good, but the overclaimed flatness argument and missing embedding analysis pull the score down. I assign **5.5**.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>