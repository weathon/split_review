Here is my consolidated final review.

---

## Summary

This paper introduces Conditional Activation Steering (CAST), a method that augments standard activation steering with a "condition vector" so that behavior modifications (e.g., refusal) are applied selectively based on input content rather than indiscriminately. The core idea is to compute the similarity between the model's hidden state and its projection onto the condition vector, using a threshold to gate whether the behavior vector is applied. The paper demonstrates selective refusal across multiple models, logical composition of conditions (OR rules), domain constraining via duality (flipping comparison direction), and generalization to unseen categories.

## Strengths

- **Demonstrates selective refusal at scale** — Table 1 reports that CAST on Qwen 1.5 Chat (1.8B) achieves 90.7% refusal on harmful prompts while maintaining only 2.20% refusal on harmless prompts, for a discrepancy of 88.5 percentage points. This directly supports the paper's central claim that context-dependent activation steering is feasible.

- **Logical composition of condition vectors** — Section 5 and the associated figures demonstrate that multiple condition vectors can be combined with OR logic (e.g., "if hate speech OR legal opinion, then refuse") and that refusal can be both induced and removed through sign reversal, enabling programmable behavioral rules without weight optimization.

- **Duality property enables bidirectional control** — The paper shows that flipping the comparison direction (from `<` to `>`) intervenes on the exact complement set, enabling domain constraining (refusing everything except a target category). This is a clean and useful property that goes beyond what standard activation steering can offer.

- **Efficiency and scaling properties** — Figure 6a shows performance saturates with ~700–800 training examples, and Figure 6b shows linear time scaling for condition vector extraction. These support the claim that CAST remains lightweight compared to weight-optimization methods.

- **Generalization to unseen categories** — Figure 7b demonstrates that domain constraining to a target category (e.g., hate speech) effectively refuses novel categories (gambling, malware generation) never seen during vector extraction, which is a genuine strength of the complement-based approach.

- **Consistent results across multiple models** — Experiments span 7 different model architectures/sizes (Qwen 1.5 Chat, OLMo SFT, Hermes 2 Pro, Llama 2, Llama 3.1, NeuralDaredevil, Zephyr Beta), showing the method is model-agnostic.

## Weaknesses

### Fatal

None.

### Major

- **The primary evaluation metric ("refusal rate") is never defined.** The paper reports refusal rates throughout (Table 1, Figures 1–3, etc.) but does not specify how a model's response is classified as refusal vs. compliance. No keyword list, classifier, annotation protocol, or agreement statistic is provided. The closest the paper comes to validation is stating that "authors manually checked every item in the test set to ensure integrity" (line 207), but this refers to the test set prompts, not to response classification. Without a reproducible definition of the central metric, the paper's quantitative results cannot be independently verified or compared to prior work (e.g., Sorry-Bench uses a specific classifier). This is a fundamental reproducibility gap that the authors must address.

### Minor

- **Table 1 does not include unconditional AST refusal rates for the same models.** The paper claims CAST improves over activation steering (AST) by enabling selective refusal, but Table 1 only shows CAST results alongside base-model and reference-model numbers. The AST comparison is relegated to Figure 1 (qualitative, across models different from those in Table 1) and an appendix table (stripped by the parser). Having AST refusal rates in the main comparison table would cleanly quantify the improvement in selectivity and strengthen the paper's central empirical claim.

- **No statistical uncertainty reported.** All refusal rates are point estimates without confidence intervals, standard deviations, or error bars. Given that threshold θ, layer, and comparison direction are grid-searched on training data, the risk of overfitting to the test set is non-negligible and some variance measure (e.g., across different data splits) would help assess stability.

- **The non-linear transformation (tanh) is introduced but neither justified nor ablated.** Line 159 states "we apply a non-linear transformation sim(h, tanh(proj_c h)) for more predictable behavior" without any ablation study or explanation of why tanh is preferable. Since this is part of the core gating mechanism, an ablation would clarify whether it materially improves performance.

- **The prompting baseline for domain constraining (Figure 3c, red dotted line) is underspecified.** The paper describes it only as "the model is simply prompted to comply with the target condition and refuse other conditions" without providing the exact prompt template. This makes the baseline difficult to reproduce or interpret fairly.

- **Grid search hyperparameter space is not reported.** The paper states that a grid search identifies optimal threshold θ, layer l, and comparison direction, but does not specify the step sizes, number of layers tested, or the search budget. This is a minor completeness issue.

### Trivial

- **The t-SNE visualizations (Figures 2a–c) are qualitative and not quantitatively linked to refusal rates.** This is inherent to t-SNE; the paper could note the limitation.

- **Table 1's comparison with Reference models (LLaMA 3.1 8B, LLaMA 2 13B) is across different architectures and sizes.** The paper partially acknowledges this in a footnote (lines 354–356), but the conclusion's claim that "CAST achieves performance comparable to or exceeding that of models specifically aligned for safety" should more clearly caveat the uncontrolled nature of this comparison.

## Nice-to-Haves

- **Replace pie charts in Figures 3–4 with bar charts** that can be read more precisely and accommodate error bars.
- **Provide concrete examples of the model's responses** for the logical composition experiments, e.g., showing the actual output for "if hate speech OR legal advice then refuse."
- **Include a comparison to a simple cosine similarity with c** (without the projection step) to justify the projection design choice.
- **Test on additional LLM families** (e.g., Gemma, Mistral v0.2/v0.3) to further validate scalability claims.

## Removed Points

These points are flagged to be removed, treat them with caution:

- *Test-train contamination concern* (Harsh Critic, point under Section 3.2): The paper explicitly states that the test sets are "unseen" (line 296) and uses machine-generated prompts (not Sorry-Bench itself) for vector extraction. The criticism is unfounded.
- *PCA alternating concatenation is ambiguous* (Harsh Critic, point under Section 3.3): The paper clearly explains the construction (lines 264–268) — the alternating order is simply a description of matrix assembly and does not affect PCA.
- *Missing AST baseline entirely* (Harsh Critic, Critical Issue 1, first sentence): The paper does provide AST comparison in Figure 1 and an appendix table (tab:appbd-fig1). The criticism that it is completely absent is inaccurate, though having AST in the main Table 1 would be beneficial (kept as a minor weakness above).
- *Missing appendix proofs/references*: The parser strips these; they exist in the original submission.

## Novel Insights

The most interesting observation beyond the paper's own contributions is the semantic-distinctiveness analysis (Figure 4c): domain constraining works better for categories that are more semantically distant from others. This suggests a fundamental limitation — condition vectors for semantically overlapping categories will have less discriminative power — which is an inherent property of the approach rather than a fixable engineering issue. The comparison between fine-grained condition vectors (Section 5) and the coarser harmful/harmless condition (Section 4) also implicitly reveals that condition vectors operate on a spectrum of specificity, with more specific conditions likely requiring more careful threshold calibration, a dynamic the paper does not fully explore.

## Suggestions

1. **Define the refusal classifier.** This is the single most important fix. Specify whether you use keyword matching (provide the keyword list), a trained classifier (provide training details), or manual annotation (provide inter-annotator agreement). Without this, all quantitative results are uninterpretable.

2. **Add unconditional AST refusal rates to the main results table (Table 1)** for the same models on the same test sets. This directly quantifies the improvement CAST offers over the baseline method and addresses the paper's central claim.

3. **Ablate the tanh non-linear transformation** to show whether it materially improves separation or threshold robustness. If it does not, consider removing it for simplicity; if it does, explain why.

4. **Report variance across data splits** — at minimum, repeat the main experiments (Section 4) with 3–5 random splits of contrastive data and test sets, reporting mean and standard deviation of refusal rates.

5. **Provide the exact prompting baseline template** used in Section 5 (Figure 3c) so that the comparison is reproducible.

6. **Replace pie charts with bar charts** that include per-model breakdowns and error bars.

## Score and Decision

The paper presents a conceptually clean and well-motivated extension of activation steering with useful properties (selective refusal, logical composition, duality, domain constraining). The contributions are real and the method is demonstrated across multiple models. However, the evaluation has a significant reproducibility gap: the primary metric (refusal rate) is never defined, making the core quantitative claims unverifiable. This weakness does not invalidate the paper's qualitative demonstrations and ablation-style analyses, but it substantially undermines the experimental rigor. The paper has genuine contributions that would be of interest to the community, but the metric definition must be clarified before the work can be accepted.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>