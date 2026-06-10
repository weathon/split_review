Now let me write the consolidated review.

## Summary

This paper proposes Conditional Activation Steering (CAST), an extension of activation steering that uses learned "condition vectors" (derived from prompt hidden states) as binary gates to selectively apply "behavior vectors" (steering vectors for refusal). The method enables rules like "if hate speech OR legal opinion, then refuse" without weight updates. Experiments across seven models demonstrate selective refusal: CAST raises harmful-prompt refusal while keeping harmless-prompt refusal rates near baseline levels, and supports logical composition (OR) of conditions as well as domain constraining via the duality property.

## Strengths

- **Clean mathematical generalization of ActAdd.** Eq. 2 (`h' ← h + f(sim(h, proj_c h)) · α · v`) extends the standard activation addition formulation with a principled gating mechanism based on cosine similarity between hidden states and learned condition vectors. This provides a concrete way to add context-dependent control while preserving the simplicity of activation steering.

- **Strong empirical evidence of selective refusal across multiple models.** Table 1 (Section 4) shows CAST increases the harmful/harmless refusal discrepancy from 45.8 to 88.5 (Qwen 1.5 Chat), 47.9 to 80.2 (OLMo SFT), and 18.3 to 80.9 (Hermes 2 Pro), while keeping harmless refusal rates near base-model levels (~2–6%). The experiment covers seven models of varying sizes and architectures, demonstrating generalizability.

- **Demonstration of logical composition of condition vectors (OR).** Section 5 (Figure 9) shows that multiple condition vectors can be combined via logical OR to create composite refusal rules (e.g., "if hate speech OR legal opinion, then refuse"). Using the duality property, the method also implements a form of negation by flipping the comparison direction, enabling domain-constraining applications.

- **Useful analyses of method properties.** The paper provides empirical characterization of saturation (Figure 6a: performance plateaus with relatively little data), linear time scaling (Figure 6b), duality (Figure 8: flipping the comparison direction intervenes on the complement set), and the correlation between semantic distance and constraining effectiveness (Figure 11c).

## Weaknesses

### Fatal

None.

### Major

- **Refusal measurement methodology is never stated.** The paper reports refusal rates throughout (Table 1, Figures 1, 5–7) but never specifies how "refusal" is determined from a model's raw output. Is it keyword matching on patterns like "Sorry, I can't" or "I cannot"? An LLM-as-judge evaluation? The test sets are from Sorry-Bench (harmful) and Alpaca (harmless), but no classification protocol is described for either. This is a foundational evidential gap: without knowing the metric, the reported refusal rates cannot be verified, interpreted, or compared across settings. The method's central quantitative claims rest on this undefined measurement.

### Minor

- **The claim that CAST "achieves performance comparable to or exceeding that of models specifically aligned for safety" is broader than the evidence supports.** The conclusion (Section 6) references Table 1, but the comparison is cross-model (CAST on Qwen 1.5 Chat / OLMo SFT / Hermes 2 Pro vs. LLaMA3.1 Inst 8B and LLaMA2 Chat 13B as "references") rather than a controlled within-model comparison with fine-tuning baselines. The table explicitly caveats that reference models "might have been aligned using different harm taxonomies," but the concluding sentence overstates what the experiment actually shows. A direct comparison where the same base model is either fine-tuned for safety or steered with CAST would be needed to support this claim.

- **No statistical uncertainty reported for any quantitative result.** Refusal rates are reported to two significant figures with no confidence intervals, standard deviations, or sensitivity analysis w.r.t. the threshold θ. Given the manual tuning of θ via grid search, the stability of results is unknown.

- **The "programming" framing overstates the method's compositionality.** What is implemented is binary thresholded gates with logical OR across independently trained condition vectors, plus complement via duality. There is no formal language, no compositionality beyond disjunction and negation, and the condition vectors are not verified to correspond to their category labels in any semantically grounded way. "Conditional gating of steering vectors" would be a more accurate description.

- **No dedicated discussion of limitations or failure modes.** Important questions are unaddressed: how does CAST handle ambiguous prompts that could belong to multiple categories? How robust is the condition detector to adversarial prompts? How does performance degrade under distribution shift? What happens when refusal-induction and refusal-removal rules conflict (briefly mentioned but not analyzed)?

- **Key design choices lack motivation or ablation.** (a) The non-linear transformation `tanh(proj_c h)` is mentioned in one sentence (line 159) with no ablation, analysis, or justification. (b) Grid search identifies the "best" combination of θ/layer/direction that "best separates the two classes of training data," but the optimization metric (accuracy? F1? separation margin?) is never defined. (c) The condition detector's standalone accuracy (precision/recall/F1 on test-set classification) is never reported, making it impossible to distinguish between cases where the condition detector works vs. where the refusal vector dominates regardless.

- **The prompting baseline is unreproducible.** The prompting baseline (Section 5, Figure 8c) is described only as "the model is simply prompted to comply with the target condition and refuse other conditions." The prompt template is not provided. Given that prompting performance is highly sensitive to template wording, this baseline cannot be reproduced or compared against meaningfully.

- **The condition detector's accuracy on the test set is never reported.** Only downstream refusal rates are shown, not whether the condition vector correctly identifies prompt categories. This makes it difficult to assess whether failures are due to the condition detector or the refusal vector.

### Trivial

- The mathematical formulation `sim(h, proj_c h)` simplifies to the absolute cosine similarity between h and c scaled by h's projection magnitude, which could be stated more concisely. This does not affect correctness.
- Wall-clock overhead of the additional similarity computation per forward pass (compared to standard ActAdd) is not reported, though the paper notes experiments are replicable within an hour.

## Nice-to-Haves

- An ablation of the tanh non-linearity and the projection+cosine formulation vs. direct cosine similarity with c.
- A within-model comparison to a lightweight fine-tuning baseline (e.g., LoRA on the same contrastive data) to ground the efficiency claims.
- Reporting condition detector accuracy (precision, recall, F1) on held-out test sets separately from downstream refusal rates.

## Removed Points

The following points from the input reviews were removed with justification:

- **"duality property is trivial"** — The paper demonstrates this empirically and uses it for a practical application (domain constraining). Presenting it as a property is reasonable, not a weakness.
- **"Section 3 mathematical formulation is redundant"** — The paper provides a rationale for the projection-based formulation. The criticism is a subjective judgment about notational efficiency, not a substantive flaw.
- **"No related work section"** — The paper has a Background section that covers activation steering. Per review guidelines, I should not cite missing related works I cannot independently verify.
- **"Computational cost in wall-clock terms not discussed"** — The paper states "majority of experiments within an hour" and shows linear time scaling. Partially addressed.
- **"Contrastive data is synthetic/non-naturalistic"** — The paper explicitly describes and commits to this setup; it is a design choice the authors are transparent about, not an oversight.
- **Strengths from Strength Finder that are generic** — Generic statements about "addressing an important problem" and "targeting an interesting question" were removed as lacking specific content. Only evidence-grounded strengths were retained.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Specify the refusal measurement protocol** in the main text or at minimum by clear reference. State whether it is keyword matching (list patterns), LLM-as-judge (which model and prompt), or human annotation (with inter-annotator agreement).
2. **Report condition detector standalone accuracy** (precision, recall, F1 on test-set category classification) to validate that the condition mechanism works independently.
3. **Define the grid search optimization metric** when stating that θ/layer/direction "best separates" the training data.
4. **Ablate the tanh transformation** or remove it if it is not essential. Provide justification for its use.
5. **Provide the prompting template** used for the prompting baseline.
6. **Add confidence intervals or variability measures** for the main quantitative results (refusal rates), perhaps across multiple threshold settings or random splits.
7. **Add a limitations paragraph** addressing robustness to adversarial prompts, ambiguous inputs, distribution shift, and known failure modes of the condition detector.

## Score and Decision

MY FINAL SCORE: <score>5</score>
MY FINAL DECISION: <decision>Reject</decision>