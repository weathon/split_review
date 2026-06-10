Below is the synthesized final review.

---

## Summary

This paper investigates how LLMs encode truthfulness-related information in their internal representations. It makes four main contributions: (1) truthfulness signals are concentrated in **exact answer tokens** (not the last generated token), yielding substantial improvements in probe-based error detection (AUC 0.85–0.95 across models/datasets); (2) probe classifiers trained on one task rarely generalize beyond what logit-level signals provide, contradicting claims of a universal truthfulness encoding; (3) error types (derived from repeated sampling) are predictable from a single greedy-decoding pass; and (4) a probe can identify the correct answer from a pool of candidate generations even when the model itself consistently generates the wrong answer, revealing a discrepancy between internal encoding and external behavior.

---

## Strengths

- **Novel discovery of truthfulness concentration in exact answer tokens (Section 3, Table 1, Figure 2).** The paper systematically maps layer-by-layer, token-by-token AUC heatmaps and demonstrates that probing on exact answer tokens (AUC 0.85–0.95) markedly outperforms conventional locations (last token: 0.71–0.86; before-last: 0.73–0.88; end of question: 0.72–0.82). This is a concrete, previously overlooked finding with clear practical value.

- **Rigorously controlled generalization analysis (Section 4, Figure 4).** Raw generalization heatmaps (Figure 4a) appear to support universal truthfulness, but the paper subtracts the logit-min-exact baseline (Figure 4b), showing that most apparent generalization is actually accessible through external logit features alone. This methodological check is cleaner than prior work and yields a meaningful negative result.

- **Fine-grained evidence of internal–external discrepancy by error type (Section 6, Figure 5).** Disaggregating by error type (rather than reporting aggregate accuracy) shows that probe-based answer selection improves accuracy by 30–40 points specifically for error types where the model shows no external preference for the correct answer (categories C2, D, E1). This is the most concrete evidence for the paper's central claim.

- **Broad evaluation coverage.** Experiments span 4 models (Mistral-7b, Mistral-7b-instruct, Llama3-8b, Llama3-8b-instruct) and 10 diverse datasets (factual QA, gender bias, commonsense reasoning, NLI, math, sentiment), strengthening generality claims.

---

## Weaknesses

### Fatal
None.

### Major

- **The "know more than they show" / discrepancy claim outruns what probing can establish.** The paper's most striking headline — that LLMs internally "know" the correct answer while generating incorrect ones — rests on a probe's ability to select the correct answer from a pool of candidates. However, a linear probe achieving high AUC on this task means that *some linear direction in the representation space correlates with correctness* on the training distribution. This does not warrant the conclusion that the model "knows" the correct answer in any cognitive sense; the probe may exploit surface statistical regularities (e.g., activation patterns that correlate with correctness without the model representing the answer per se). The paper cites Belinkov (2021) but does not engage with the probing limitations literature (e.g., Hewitt & Liang 2019, Voita & Titov 2020, Pimentel et al. 2020) on control tasks, selectivity, or the representation-use vs. representation-encoding distinction. Absent a control task, the "know more than they show" framing conflates correlational probe evidence with a causal claim about what the model internally represents. **This does not invalidate the paper's core contributions** (the exact-answer-token finding, the generalization analysis, and the empirical discrepancy are all real), but the title and abstract overstate what the methodology can support. The authors should add a probing control analysis and temper the strongest interpretational claims.

### Minor

- **Error-type taxonomy validated on only one dataset (TriviaQA).** The taxonomy in Section 5 covers 96% of TriviaQA errors for Mistral-7b-instruct, but the paper's claim that "error types are predictable from LLM representations" is supported only for factual retrieval errors. Error structure for reasoning, bias, or math tasks may differ qualitatively. The paper mentions this scope limitation in passing but does not discuss how task-specific the taxonomy might be, leaving the generality of the finding unclear.

- **Generalization experimental design could be more thorough.** The paper trains probes at the target dataset's optimal (token, layer) combination and tests on source data at that same position. This design is reasonable, but it leaves open the possibility that a shared truthfulness signal exists at a different (token, layer) for different tasks and would be missed by fixing to one position per target. The authors could strengthen this by showing heatmaps of generalization AUC across *all* layers (not just the optimal one), or by training a probe at the source's optimal position and testing across all target layers. This is a suggestion for improvement, not a flaw in the current results.

- **Exact-answer extraction fidelity not analyzed.** The exact answer is extracted using Mistral-7b-Instruct in a few-shot setting. The paper does not report how often the extractor correctly identifies the exact answer, nor how extraction errors affect downstream probing results. A sensitivity analysis or human evaluation of extraction quality would strengthen the paper's core finding.

- **Logit-min-exact baseline choice somewhat underspecified.** The paper uses Logit-min-exact as the subtraction baseline in the generalization analysis (Figure 3B) and calls it "our strongest logit-based baseline," but Table 1 shows that Logit-min-exact is not always the strongest (e.g., for Winobias, Logits-min achieves 0.59 vs. Logit-min-exact's 0.53 on Mistral-Instruct). The choice is still reasonable (a conservative baseline makes the negative result stronger), but a brief justification or robustness check across alternatives would improve clarity.

- **No discussion of class imbalance.** Error detection datasets can be imbalanced, and AUC is insensitive to prevalence, but the probe training procedure and interpretation could still be affected. The paper does not discuss whether class ratios were controlled.

### Trivial
None.

---

## Nice-to-Haves

- Add a probing control task (e.g., selectivity analysis following Hewitt & Liang 2019) to calibrate what the probe AUC values actually reveal about encoding vs. surface correlation.
- Evaluate error type taxonomy on at least one non-factual dataset (e.g., Math or Winobias) to test generality.
- Report exact-answer extraction accuracy on a human-annotated subset.
- Report how many random seeds / data splits were used for probe training.
- Justify the choice of Logit-min-exact over other logit baselines for the subtraction experiment, or show robustness across alternatives.

---

## Removed Points

These points were raised in the inputs but removed because they are not supported by the paper text or are otherwise invalid:

- **Generalization methodology conflates two questions (harsh critic #2):** The critic claimed the probe "is trained using the optimal token+layer combination for the *source* dataset, then tested on the target dataset using the target's optimal token+layer combination." The paper states (line 252): "We select the optimal token and layer combination for each dataset, train all probes using this combination on other datasets, and then test them on the original dataset." Under the natural reading, the probe is trained on source data *at the target's optimal position* — not the source's. The critic's specific concern about misaligned positions is therefore based on a misreading. However, a related (weaker) concern about not checking all layers is retained in Minor weaknesses.
- **Missing related works / missing references:** Per instructions, I cannot add or verify missing references.
- **Formatting/style nitpicks:** Removed per rules.
- **"Probe generalization is a cautionary result" (strength finder's phrasing):** This is accurate but already captured by the main strengths.

---

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions

1. **Add a probing control task** (e.g., an auxiliary syntactic property) to demonstrate that the probe's success reflects genuine encoding of truthfulness rather than surface correlations. Control-task AUCs should remain near chance if the probe is selectively capturing truthfulness.
2. **Reframe the discrepancy claim** from "LLMs know more than they show" to something like "probes can identify correct answers even when the model under-generates them, suggesting exploitable signals in the hidden states." This preserves the empirical novelty without making an unsupported epistemological claim.
3. **Report extraction accuracy** for the LLM-based exact-answer extractor on a hand-labeled subset, and show that probe results are robust to extraction errors.
4. **Expand the error-type analysis** to at least one additional task domain to support the claim that error types are generally predictable from representations.

---

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>