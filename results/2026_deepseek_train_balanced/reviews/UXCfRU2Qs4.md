## Summary

This paper proposes a computational framework for using LLMs to probe the mental representational structure associated with psychopathology. The authors induce nine psychopathologies in five LLMs using three prompting methods (Naive, Chain, React), validate the induction via standard clinical questionnaires, analyze the semantic structure of LLM-generated word lists using GloVe embeddings, and present a schizophrenia case study replicating a known verbal-fluency finding. The core empirical contributions—reliable psychopathology induction validated by questionnaires, and a demonstrated correspondence between LLM and human comorbidity structure via Representational Similarity Analysis (RSA)—are solid and well-executed.

## Strengths

- **Clinically-validated psychopathology induction across 9 conditions**: The paper demonstrates that LLMs prompted with a specific psychopathology score above clinical diagnosis thresholds on the corresponding standardized questionnaire (SDS, STAI, EAT-26, AUDIT, BIS-10, etc.) and above their own no-pathology baseline. The diagonal-dominance analysis confirms that each induction preferentially raises its target questionnaire score. This extends prior work on personality-type induction (Jiang et al., 2024) to clinically validated psychopathologies with complex, overlapping symptom profiles.

- **LLMs capture human comorbidity structure between questionnaires (RSA = 0.59)**: Representational similarity analysis between LLM-generated 9×9 questionnaire-score matrices and human data from Gillan et al. (2016) yields a correlation of 0.59 for Dolphin with React prompting. This is a more stringent test than single-questionnaire accuracy—showing that LLMs reproduce the correlational structure across multiple psychopathologies—and goes beyond prior psychopathology-LLM studies.

- **Systematic variation of prompting complexity as an ablation**: Testing three prompting methods (Naive → Chain → React) that increase in impersonation complexity across all analyses allows the paper to demonstrate that the more elaborate React method consistently yields better human-data alignment. This structured ablation strengthens the causal claim that psychopathology induction, not just generic prompting, drives the observed patterns.

- **Multi-model, multi-temperature comparison**: Evaluation of five LLMs (dolphin-7B, mistral-7B, gpt-3.5-turbo, llama-2, gemma) at three temperatures provides practical guidance for which configurations to use and reveals systematic differences (e.g., RLHF-aligned Llama-2 scores high even without pathology induction).

## Weaknesses

### Fatal
None.

### Major

- **Promised novel hypotheses are never stated**: The abstract announces that the framework "allows us to generate several empirical hypotheses on the link between mental representation and psychopathologies," and the conclusion reiterates that the method "can help generating novel hypothesis." Yet no concrete, specific, testable empirical hypothesis is stated anywhere in the paper. The semantic trajectory results that match *previously documented* patterns (Bartczak & Bokus, 2017; Brody, 1964) are presented as validation, not as novel predictions. The limitations section acknowledges this gap ("the novel hypotheses advanced by our framework still need to be confirmed"), but the framing throughout oversells hypothesis generation as a delivered contribution when it is, at best, a promissory note. A framework paper that advertises hypothesis generation as a key deliverable must actually generate at least one concrete hypothesis.

- **Absence of statistical inference**: The paper presents RSA values, semantic expansion differences, and schizophrenia comparisons as point estimates without confidence intervals, significance tests, or effect sizes. The RSA value of r = 0.59 (Dolphin + React) has no accompanying uncertainty quantification, and there is no baseline comparison (e.g., what RSA would arise from random matrices or a trivial model). Without this, the reader cannot assess whether the reported values are meaningfully distinguishable from chance. This is a significant methodological gap for a paper making comparative claims across models, prompting methods, and psychopathologies.

### Minor

- **Schizophrenia case study reports only one model for the primary finding in the main text**: Dolphin + React captures the qualitative pattern of higher consecutive semantic distance in schizophrenia vs. healthy controls, and Gemma captures the rank order of additional distance measures. However, the main text does not state whether the other three models (Mistral, GPT-3.5, Llama-2) capture the *primary* consecutive-distance pattern. The paper directs readers to supplementary figures, but the omission of this information from the main body makes it difficult to assess the robustness of the result across models. This is a reporting gap, not a fatal flaw—the data ostensibly exist in the supplement—but it weakens the in-text argument.

- **RSA matching procedure underspecified**: The selection of 100 human subjects "that scored above the diagnosis threshold of each pathology" from Gillan et al. (2016) is described without details on how subjects were selected from larger samples, whether demographic variables were matched, or how the threshold criterion was simultaneously applied across multiple pathologies. This makes the comparison harder to evaluate.

- **Psychopathology induction is robust, but unevenly so**: The paper claims "robust psychopathology induction" but the text reveals that Llama-2 scores high even when prompted with no pathology, Dolphin fails for social anxiety (no-pathology induction also scores above threshold), and results vary substantially by prompting method. The overselling of "robust" sits uneasily with the variability documented within the same section.

### Trivial

- **Semantic trajectory presentation**: The paper uses two anti-correlated metrics (κ and δ) and sometimes discusses results in terms of "expanded"/"constricted" space without consistently naming which metric is being reported. Clarifying which metric drives each claim would improve readability.

## Nice-to-Haves

- The concrete/abstract word analysis (Section 4.1) is exploratory and interesting; a statistical test of the interaction between psychopathology condition and word type (concrete vs. abstract) would substantially strengthen it.
- Using LLMs' own hidden-state embeddings rather than GloVe for the semantic trajectory analysis could strengthen the connection between the analysis and the claim of probing "internal structure," though this would preclude direct comparison with human studies that use external embeddings.

## Removed Points

*These points were flagged for removal. Treat them with caution; they may contain factual inaccuracies or misunderstandings.*

- **Criticism: "GloVe embeddings do not probe LLMs' internal representations (structural flaw)"** — REMOVED. The paper explicitly states that it analyzes "lexical output patterns of LLMs (a proxy of their internal representations)" (abstract, line 4), and it follows the exact methodology used in the human literature (Nour et al., 2023 uses word2vec; Vives et al., 2023 uses external embeddings). Measuring semantic structure of generated word lists via external embeddings is standard practice; the paper does not claim to directly access LLM internals. The critic's framing of this as a "structural flaw" misreads what the paper claims and ignores the explicit "proxy" qualifier. The parallel with human studies—which also cannot directly measure "internal representations" and rely on behavioral output projected through external semantic spaces—makes this a methodological choice, not a flaw.

- **Criticism: "RSA comparing 100 repeated LLM runs against 100 humans is asymmetrical and inflates similarity"** — DEMOTED from its original framing. While it is true that repeated LLM runs at temperature 0.3 produce lower-variance data than human subjects, the paper averages these runs into a single 9×9 matrix per model before RSA, so the concern about individual trial noise is partly mitigated. The broader point about missing confidence intervals and baseline comparisons is retained in Major weaknesses above.

- **Criticism: "Semantic trajectory analysis conflates within-LLM word associations with LLM's representational structure"** — REMOVED. Same issue as the GloVe point; this is the standard methodology for analyzing behavioral output in this literature.

- **Criticism: "Abstract vs. concrete word analysis is entirely post hoc with thin interpretation"** — REMOVED. Exploratory analyses are permissible and the paper does not claim this as a core contribution; it labels the interpretation as preliminary.

- **Strength: "The single strongest piece of evidence is the schizophrenia case study"** — REMOVED. This conflicts with verified weaknesses showing the results are mixed and selectively reported. The case study is partially successful, not the strongest evidence. The induction validation and RSA correspondence are stronger.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no observation about the paper that the paper itself does not already articulate.

## Suggestions

1. **State at least one concrete, testable hypothesis** derived from the semantic trajectory analyses (e.g., "our framework predicts that OCD patients will show expanded semantic space in free association, which can be tested in humans using the same verbal-fluency paradigm used in Nour et al. 2023"). This would substantiate the paper's central advertised benefit.

2. **Add bootstrapped confidence intervals and significance tests** for all core quantitative comparisons (RSA values, semantic expansion differences, schizophrenia pattern comparisons). Include a null baseline for RSA (e.g., what r is obtained with shuffled labels or random matrices).

3. **Complete the main-text reporting for the schizophrenia case study**: explicitly state whether Mistral, GPT-3.5, and Llama-2 capture the consecutive-distance pattern, not just Dolphin and Gemma.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>