- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 3, 5
Here is the final consolidated review.

---

## Summary

This paper introduces the task of *scoping* language models — preventing them from answering queries outside a specified set of tasks — and compares six methods (system prompting, SFT, DPO, probing classifiers, Circuit Breakers, and SFT+CB layering) across three diverse tasks. The main finding is that Circuit Breakers (CB), originally proposed for general safety alignment, can be adapted for scoping and offers good out-of-distribution generalization even when trained on narrow rejection data. The study is broad in scope, covering adversarial robustness, data diversity requirements, multiple accept tasks, and additional ablations.

---

## Strengths

- **CB generalizes from narrow rejection sets to OOD tasks.** The diversity experiment (Section 4.2, Figure 3) shows that with only a single reject category, CB and SFT-CB achieve high out-of-distribution rejection rates, whereas DPO requires substantially more diverse data to reach similar performance. This is the paper's most practically significant finding.

- **SFT-CB layering improves accept-task performance without compromising rejection.** Across all three accept tasks, SFT-CB attains the highest Accept Score while maintaining strong in-distribution and OOD rejection, exceeding both plain CB and SFT alone. This validates the layering strategy as a practical recipe.

- **Comprehensive empirical benchmark for a new problem.** The paper systematically compares six methods across three tasks (sentiment analysis, summarization, program execution) on adversarial robustness, data diversity, multiple-accept scenarios, and precise scoping, using a unified evaluation framework. This establishes a reproducible starting point for the scoped-LLM task.

- **Clear identification of each method's failure modes.** The paper honestly documents where each method breaks down: the high over-rejection rate of Probe, DPO's need for diverse rejection data, CB's degradation on large/overly-diverse rejection sets and its inheritance of base-model over-rejection, and the brittleness of system prompting.

---

## Weaknesses

### Fatal

None.

### Major

- **No statistical uncertainty quantification.** All experiments appear to be run once with no multiple seeds, confidence intervals, standard deviations, or significance tests. Training methods like CB, DPO, and SFT involve randomness from data sampling, weight initialization, and optimization order, yet all comparisons are made on single runs and interpreted via visual inspection of figures. The TAP evaluation (N=10 prompts per dataset) is an order of magnitude too small for reliable comparison. Without variance estimates, the reader cannot distinguish systematic differences from noise, and the claimed relative ordering of methods is not statistically grounded. This is the paper's most significant weakness.

- **Detection asymmetry between CB and other methods.** For CB-based methods, rejection is detected via *two* mechanisms (string matching for "cannot"/synonyms *plus* repetition detection of ≥4 repeated strings), whereas for SFT, DPO, and system-prompted models, rejection is detected via string matching alone. The detector was tuned on only 90 completions total (30 per set). A 1% detection error in either direction could shift rankings across the many experimental conditions. Because the detection methodology differs, rejection-rate comparisons between CB and non-CB methods are not on equal footing. This is a confound that weakens every rejection-rate comparison.

### Minor

- **CB inherits base-model over-rejection on accept tasks.** This is explicitly a design property of the CB loss (it preserves accept-task representations), but it means CB cannot fix cases where the base model already rejects queries it should accept. The paper documents this for Program Execution (Section 4.2, Figure 3) and the multiple-accept experiment (Section 4.3, Figure 4), yet the overall positive tone about CB's superiority is not consistently calibrated to this limitation. A deployment-relevant comparison should account for the fact that CB's accept-set rejection rate is often *worse* than SFT or DPO.

- **Main experiments use a single model (Mistral-7B).** The paper acknowledges this (line 140) and provides a teaser with Granite (Figure 1 only, not in the main experiments), but the generality of the findings across model families is unestablished. Methods that work well on Mistral may not transfer to models with different alignment procedures, architectures, or scales.

- **Several important analyses are presented as one-sentence claims without supporting results in the main text.** "Precise Scoping," "Effect of Data Quantity," and "Effect of LoRA Rank" are each described in a single sentence (Section 4.5) with no numbers, tables, or figures to substantiate them. While details may be in a stripped appendix, the main text alone does not support the claims made about these analyses.

### Trivial

- The paper states that "we catch rejection by string matching for a few different tokens that are synonyms for 'cannot' at the beginning of the generation" but uses the example string `I cannot answer that.` (line 111) — there is a stray character `11` before "I cannot" in line 127, which appears to be a PDF extraction artifact but is present in the source.

---

## Nice-to-Haves

- **Multi-seed experiments:** Running each condition with 3–5 seeds and reporting means with standard errors would be the single most impactful improvement, converting the study from a set of observations into a reliable comparison.
- **Unified rejection detection:** Using a single detection scheme across all methods (e.g., judge-based evaluation on a held-out sample, or a consistent set of string-matching rules) would eliminate the confound in the current two-detector design.
- **Numerical result tables:** For the main adversarial and diversity experiments, tables with key numbers would allow readers to verify claimed rankings without relying solely on visual inspection of figures.
- **Two-stage pipeline baseline:** A separate small classifier operating on the *input text* (not on LLM representations) before querying the LLM would be a natural baseline given how the introduction frames existing approaches.

---

## Removed Points

These points were flagged for removal; treat them with caution.

- *"Missing appendix / Additional Analysis not substantiated in the presented material"* — Per instructions, the parser strips appendix sections from all papers; the original submission contains them.
- *"Direct comparison with a two-stage pipeline (trained binary classifier followed by generation) is missing and is the obvious baseline"* — The paper *does* include the Probe baseline, which is a classifier. A separate two-stage text-level classifier is a reasonable baseline but not "obviously missing" — the paper's scope is about methods that modify the LLM itself, and the Probe already covers representation-based classification.
- *"Figures are small and difficult to read"* — This is a formatting/presentation nitpick about the PDF rendering, not a substantive weakness.
- *"Y-axis in Figure 3 not clearly labeled"* — Cannot be verified from the text; it may be present in the actual figure.
- *"The paper claims precise scoping but doesn't show it"* — The claim appears (briefly) in Section 4.5; full details are likely in the appendix.
- *"Only run TAP with N=10"* — This is acknowledged by the paper as a cost constraint and already covered under the statistical-rigor weakness.

---

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions

1. Add multi-seed (3–5) results with error bars / confidence intervals for the main experimental conditions (adversarial evaluation and diversity experiment). This is the single most important improvement.
2. Unify the rejection-detection methodology: either apply both string-matching and repetition-detection to all methods, or use a held-out judge-based evaluation to verify that the detection asymmetry does not drive the reported differences.
3. Provide numerical result tables for the key figures (Figures 2, 3, 4) in the main text or appendix.
4. Explicitly recalibrate the tone of the Discussion — some sentences claim CB is "quite strong" in conditions where the data show non-trivial degradation (e.g., CB's crash at high diversity, the high accept-set rejection in multiple-accept scenarios).
5. Expand the single-sentence descriptions in Section 4.5 (Precise Scoping, Data Quantity, LoRA Rank) with at least summary statistics or a reference to the appendix table.

---
