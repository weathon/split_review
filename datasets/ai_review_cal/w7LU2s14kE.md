- Decision: Accept
- Avg Score: 7.33
- Scores: 6, 8, 8
Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

This paper investigates how transformer language models decode relational knowledge (e.g., *Miles Davis plays the trumpet*) from subject representations. The authors show that for many relations, this decoding is well-approximated by an affine transformation (a Linear Relational Embedding, LRE) estimated from the LM's Jacobian on a small number of prompts, without training any separate probe. Across GPT-J, GPT-2-XL, and LLaMA-13B, they find that ~48% of tested relations exhibit this linear structure, validate the LREs through faithfulness (top-1 match with the LM) and causal editing (inverting the LRE to change predictions), and build an "attribute lens" that reveals latent knowledge even when the LM is baited into outputting falsehoods.

---

## Strengths

- **Causal evidence that LREs drive model predictions, beyond correlation.** The editing experiment (Section 4.2) shows that inverting the estimated LRE to perturb a subject's hidden state changes the LM's predicted object at rates comparable to directly substituting the correct subject representation (oracle). This goes beyond standard probing—it demonstrates that the linear approximation captures a computation the model actually uses.

- **First-order Taylor approximation avoids probe-training confounds.** The LRE is computed directly from the LM's Jacobian on n=8 prompts (Section 3.1, Eq. 2–5), sidestepping the risk that a trained probe learns the task on its own. This is a principled methodological contribution that cleanly distinguishes the work from prior probing literature.

- **Systematic outperformance over simpler baselines across all relation types.** The LRE (with learned βW + b) substantially outperforms identity mapping, translation-only, and linear regression baselines (Section 4.1, Fig. 3). The low performance of LRE applied to the input embedding confirms the effect is not a word-level shortcut—the enriched mid-layer representation is necessary.

- **Discovery of a "mode switch" in later layers.** The paper identifies a sharp drop in LRE faithfulness at deeper layers that disappears when relation-specific context is removed (Section 4.3, Fig. 6). This offers a structural insight about how later transformer layers may transition from relation decoding to next-word prediction.

- **Attribute lens reveals latent knowledge under adversarial distraction.** Using the LRE as a relation-specific decoder, the attribute lens surfaces the correct object even when the LM is baited into falsehoods (Section 5, 11,891 adversarial prompts). This is a practically useful application that goes beyond what the Logit Lens alone provides.

- **Large-scale, multi-model evaluation across diverse relation types.** The study covers 45+ relations spanning factual, commonsense, bias, and linguistic knowledge across three models (GPT-J, GPT-2-XL, LLaMA-13B) with over 10k facts, demonstrating robustness and generality.

---

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Hyperparameter selection protocol is underspecified in the main text.** The paper states that per-relation hyperparameters (layer ℓ_r, pseudoinverse rank) are selected via grid-search, with details deferred to the appendix (line 172). The main text does not clarify whether this grid search uses held-out data or the same data as the evaluation trials. Since the appendix was stripped by the PDF parser, this cannot be verified from the submission as presented. While this is unlikely to produce inflated results given the 24-trial evaluation structure, the main text should at minimum state the validation protocol (e.g., "we select hyperparameters on a held-out subset and report results on the remaining data, across 24 random splits").

- **The explanation for the mode switch / prompt-removal experiment is unclear.** The paper reports that LRE faithfulness keeps improving in later layers when relation-specific text is removed from the prompt (line 218–219). The text is too terse to convey why this is expected and what it implies about the mode switch mechanism. Since removing the relation prompt changes the task entirely, it is not obvious that the same LRE (estimated from relation-prompted data) should remain applicable, and the reasoning behind the result is not developed.

- **The observation that causality scores exceed faithfulness scores for most relations is noted but not analyzed.** The paper mentions this result (lines 204–205) and offers a brief speculation ("the linear approximation remains powerful enough to perform a successful edit"). Deeper analysis—e.g., whether this gap correlates with properties like object vocabulary size or LRE rank—would strengthen the interpretation of the causality metric.

- **The main text does not report variance over the 24 trials.** The paper reports "average results over 24 trials" (line 172). Without error bars or distributional information, it is difficult to assess the stability of the faithfulness and causality scores, particularly for relations with small subject counts after filtering.

- **The global scalar β is fixed per LM; sensitivity analysis is deferred to the appendix.** The scalar β > 1 corrects for underestimation due to layer normalization. While the paper references empirical measurements in the appendix (line 105, \Cref{app:expain_beta}), the main text could briefly summarize the evidence that a single β works uniformly across relations and layers, or note the sensitivity of results to this choice.

### Trivial

- The abstract states that LREs can be obtained "from a single prompt," while the method averages Jacobians over n=8 examples. The intended meaning (a single prompt template) is clear from context, but the phrasing could be slightly more precise.

---

## Nice-to-Have

- **Systematic analysis of why some relations are linear and others are not.** The paper speculates that "range size" (names of people/companies) predicts nonlinearity (line 187). A quantitative analysis correlating LRE faithfulness with properties like object vocabulary size, frequency, or the number of distinct objects per relation would deepen the central finding.

- **Multi-token evaluation.** The paper uses only the first token of the object and acknowledges this limitation (line 149, referencing a limitations section). Extending to multi-token objects (even on a subset of relations where objects are short) would strengthen the evidence.

- **Attribute lens comparison to a trained linear probe.** The paper distinguishes the attribute lens from probing classifiers by noting it avoids probe training (lines 239–241). However, a direct comparison to a trained linear probe on the same task would help quantify the benefit of the Jacobian-derived approach over a supervised alternative.

---

## Removed Points

These points were raised by reviewers but are removed from the main evaluation with justifications:

- *"The assumption that noise in F has zero Jacobian in expectation seems strong."* — The paper explicitly states this assumption (line 94) and validates the LRE empirically on held-out subjects. The empirical results speak for themselves, making speculation about the assumption's strength moot. **Removed: strawman.**

- *"No comparison of attribute lens to Logit Lens on the same hidden state."* — The attribute lens is explicitly presented as a specialization of the Logit Lens (line 227). The comparison is implicit: the Logit Lens decodes the next token, while the attribute lens decodes the relation object. The paper's Table 2 reports attribute lens accuracy, which is a different quantity from Logit Lens next-token accuracy. **Removed: the paper's contribution is precisely that the attribute lens decodes something the Logit Lens cannot.**

- *"The paper could discuss computational cost."* — A minor implementation detail not central to evaluating the paper's claims. **Removed: reproducibility nitpick.**

- *"The paper doesn't describe how repetition-distracted prompts are constructed."* — The paper gives examples (lines 230–232) and notes the appendix covers full details. **Removed: appendix issue (parser-stripped).**

---

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any observation about the paper that the paper itself does not already make or imply.

---

## Suggestions

1. In the main text, add one sentence clarifying the hyperparameter validation protocol: e.g., "For each trial, we perform grid-search on a held-out subset of subjects and evaluate on the remaining subjects."
2. Expand the mode-switch / prompt-removal discussion to explicitly state the reasoning: removing relation text tests whether the drop in faithfulness is specific to relation-prompted contexts or a general property of later layers.
3. Add error bars or confidence intervals to the faithfulness/causality bar plots, or at minimum report the standard deviation across the 24 trials in a table.
4. Briefly summarize in the main text the empirical evidence for the global β scaling factor (currently only in the appendix).

---
