- Decision: Accept
- Avg Score: 7.33
- Scores: 8, 6, 8
Now I have all the information needed to construct a thorough, verified review.

---

## Summary

This paper introduces Conditional Activation Steering (CAST), which extends standard activation steering by adding "condition vectors" — polarity directions extracted from hidden states via PCA on contrastive prompt pairs. At inference, cosine similarity between the current hidden state and the condition vector gates whether a behavior vector (e.g., refusal) is applied. This enables selective, context-dependent refusal (e.g., "refuse if hate speech OR adult content") and domain constraining (refuse everything except a target category), all without weight optimization. The paper demonstrates selective refusal on harmful prompts while maintaining low harmless refusal, logical composition of condition vectors, and domain constraining via duality.

## Strengths

- **Selective refusal demonstrated quantitatively across multiple models**: Table 1 reports that CAST achieves a harmful/harmless refusal discrepancy of 88.5% (Qwen 1.5 Chat), 80.2% (OLMo SFT), and 80.9% (Hermes 2 Pro), where standard activation steering refuses nearly all prompts indiscriminately. This is direct evidence that CAST enables context-dependent refusal.

- **Logical composition of condition vectors works empirically**: Figure 5a shows that OR-combining condition vectors (e.g., `if c_hate or c_legal then +v_refusal`) produces refusal rates on the union of target categories that are nearly additive, while non-target categories remain largely unaffected. This validates the claim that CAST supports composable behavioral rules.

- **Domain constraining via duality generalizes to unseen categories**: Figure 6a-b demonstrates that flipping the comparison direction allows constraining the model to respond to only one domain (e.g., health) by refusing all others, including unseen categories. Figure 6c further provides an insightful analysis linking constraining effectiveness to the semantic distinctiveness of the target category.

- **Data efficiency and computational efficiency**: Figure 3a shows performance plateaus after ~1000 examples, and Figure 3b shows linear time scaling. The paper states most experiments are replicable within an hour, supporting the claim that CAST maintains the efficiency of activation steering while adding controllability.

- **Modulation via threshold adjustment**: Figure 2 demonstrates that varying θ provides progressive loosening/tightening of the safety guardrail, giving practitioners fine-grained control.

## Weaknesses

### Fatal
None.

### Major

1. **Refusal metric is never defined.** The paper reports "refusal rate" as the sole dependent variable across every experiment (Tables 1, Figures 1–5) but never specifies how it is measured. Is it a keyword match on phrases like "I cannot" or "I'm sorry"? An LLM-as-judge? Human annotation? The test sets are described (500 Alpaca harmless, 450 Sorry-Bench harmful in Section 4), but the detection mechanism for what constitutes a "refusal" is entirely absent. This is the central quantitative evidence for every claim in the paper; without the metric specification, the reported numbers cannot be properly interpreted or reproduced. This is a fixable omission, but it must be addressed.

2. **Inadequate baselines for the core claim.** The paper's central claim is that CAST enables *selective* refusal. The only baseline in the main experiment (Section 4, Table 1) is standard activation steering (uniform refusal). Reasonable alternatives for selective refusal are not compared: (a) a well-crafted system-prompt-level safety rule, (b) a two-stage pipeline (classifier → forced refusal), (c) the base model's existing refusal behavior. A prompting baseline appears only in the domain-constraining experiment (Figure 5c), where it is vaguely described as "the model is simply prompted to comply with the target condition and refuse other conditions without any conditional steering techniques" — insufficient detail to assess fairness. Without testing against these alternatives, the added value of CAST over simpler approaches is unquantified.

### Minor

3. **Tanh nonlinearity introduced but never evaluated.** Line 159 states: "In practice, we apply a non-linear transformation sim(h, tanh(proj_c h)) for more predictable behavior." This is the only mention of tanh in the paper. No ablation compares the tanh variant against the simpler absolute-cosine version, no analysis of what "more predictable" means, and no justification for why tanh is needed. This is a loose thread in an otherwise well-specified method.

4. **Overclaiming in the conclusion.** The paper asserts that "CAST achieves performance comparable to or exceeding that of models specifically aligned for safety" (Conclusion). While Table 1 shows CAST reaching 83–91% harmful refusal vs. 76–88% for the reference models, the paper's own footnote acknowledges that "reference models might have been aligned using different harm taxonomies," making the comparison non-apples-to-apples. The claim should be hedged (e.g., "on our test set" or "under these specific evaluation conditions").

5. **Grid search on training data without validation.** Section 4 states that grid search identifies the best threshold θ, layer, and comparison direction "that best separates the two classes of training data." No validation split or cross-validation is described. While threshold selection on training data is common for simple binary separators, reporting held-out performance would strengthen confidence that the thresholds are not overfit.

### Trivial

6. **The projection formulation is needlessly roundabout.** The core condition check uses `sim(h, proj_c h)`, which the paper's own derivation shows simplifies to `|cos(h, c)|`. Stating this directly would make the method more accessible and easier to adopt.

## Nice-to-Haves

- An ablation of the tanh nonlinearity (what changes if it is removed or replaced with a simpler absolute value?).
- The prompting baseline in the domain-constraining experiment should be specified with the exact prompt template used.
- Error bars or multiple-seed results for a subset of experiments would strengthen the evidence.

## Removed Points

These points were identified by reviewers but are removed from the main assessment, with justification:

- **"Alternating-row PCA could introduce ordering artifacts"** — REMOVED as factually incorrect. PCA computes the covariance matrix over all data points; row order (alternating positive/negative examples) has no effect on the resulting principal components.
- **"Condition vector is mathematically the same as behavior vector — should be acknowledged"** — REMOVED as already addressed. The paper explicitly says condition vectors are "extracted similarly to behavior vectors" (line 139). The novelty is in their *use* as gates, not their extraction.
- **"Reference model comparison is meaningless"** — REMOVED as self-addressed. The paper includes a footnote transparently acknowledging that reference models use different harm taxonomies. The comparison is presented as a reference, not as a controlled benchmark.
- **"Missing full results for all 7 models"** — REMOVED per hard rule about missing appendix content. The parser strips appendices; full results likely appear in the original submission's appendix.
- **"Logical composition is trivial OR"** — REMOVED as a mischaracterization. The paper demonstrates that OR-composition of condition vectors *works empirically*, which is a non-trivial finding. The paper never claims deeper logical operators.
- **"Method is mathematically overcomplicated and potentially incorrect"** — The math is correct (projection → absolute cosine similarity). The presentation is verbose but not incorrect. Demoted to Trivial (point 6 above).

## Novel Insights

Beyond the paper's own contributions, the most interesting observation emerging from cross-referencing the reviews is the tension between the paper's clear conceptual contribution (conditional gating of steering vectors via activation similarity) and the thinness of its evaluation scaffolding. The paper identifies a genuine limitation of activation steering and proposes a sensible, simple solution — but the refusal metric omission and baseline gap mean the reader cannot fully assess whether CAST works *better* than cheap alternatives (like system prompts) or just *differently*. The domain-constraining experiments (Section 5, especially the semantic-distance analysis in Figure 6c) are the most compelling part of the paper and suggest the method's real value may be in applications (niche domain assistants) rather than in general safety.

## Suggestions

1. **Specify the refusal metric** in full detail (detection method, threshold if keyword-based, prompt if LLM-as-judge, inter-annotator agreement if human). Without this, the paper's quantitative claims are unverifiable.
2. **Add at least two baselines** for selective refusal: (a) a system-prompt-level rule (e.g., "If the user's request involves [category], refuse to answer") and (b) the base model's existing refusal behavior. Show that CAST outperforms or matches these on the same test sets.
3. **Ablate the tanh nonlinearity** and report whether it changes results meaningfully.
4. **Tone down the conclusion claim** about "comparable to safety-aligned models" or add explicit caveats about different harm taxonomies.
5. **Simplify the method presentation** by replacing `sim(h, proj_c h)` with `|cos(h, c)|` directly — it is mathematically equivalent and much clearer.
